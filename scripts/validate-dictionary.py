#!/usr/bin/env python3
"""Validasi semantik dataset: id, taksonomi, duplikasi, provenance, IPA, pola regex, rujukan silang.

Pemakaian:  python scripts/validate-dictionary.py [--stats]
Hanya pustaka standar.
"""
from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict

from _common import META_DIR, Report, iter_datasets, load_json, normalize_key

# IPA fonemis yang diizinkan (lihat docs/ipa.md). Alofon [ɪ ɛ ɔ ʊ] tidak dipakai di transkripsi fonemis.
IPA_PHONEMIC = set("ieəaouɘpbtdkgʔmnɲŋszʃxhfvʒrlwjq. ") | {"̯"}
IPA_ALLOPHONES = set("ɪɛɔʊ")
IPA_FORBIDDEN_HINTS = {"y": "pakai /j/ untuk huruf y", "c": "pakai /tʃ/ untuk huruf c", "ñ": "pakai /ɲ/", "ng": "pakai /ŋ/", "ny": "pakai /ɲ/", "'": "pakai /ʔ/"}


def check_ipa(report: Report, where: str, ipa: str):
    if not (ipa.startswith("/") and ipa.endswith("/")):
        report.error(f"{where}: IPA harus diapit garis miring fonemis: {ipa}")
        return
    body = ipa[1:-1]
    bad = {ch for ch in body if ch not in IPA_PHONEMIC and ch not in IPA_ALLOPHONES}
    if bad:
        report.error(f"{where}: simbol IPA tidak dikenal {sorted(bad)} dalam {ipa}")
    if IPA_ALLOPHONES & set(body):
        report.warn(f"{where}: simbol alofon dalam IPA fonemis {ipa} (gunakan /e o i u/)")
    for hint, msg in IPA_FORBIDDEN_HINTS.items():
        if hint in body:
            report.error(f"{where}: '{hint}' dalam IPA {ipa} — {msg}")
    if "  " in body or body != body.strip():
        report.error(f"{where}: spasi ganda/tepi dalam IPA {ipa}")


def main() -> int:
    show_stats = "--stats" in sys.argv
    report = Report("validate-dictionary (semantik dataset)")
    taxonomy = load_json(META_DIR / "taxonomy.json")
    sources = {s["id"]: s for s in load_json(META_DIR / "sources.json")["sources"]}
    src_kind = {"zip-reference": "zip-reference", "external": "external-source", "interpretation": "interpretation"}

    all_ids: dict[str, str] = {}
    by_text_cat: dict[tuple, str] = {}
    by_norm: defaultdict[str, list] = defaultdict(list)
    related_refs: list[tuple[str, str]] = []
    stats = defaultdict(Counter)
    used_sources: Counter = Counter()
    used_sub: set = set()

    for name, path, data in iter_datasets():
        spec = taxonomy["files"].get(name)
        if not spec:
            report.error(f"{name}: tidak terdaftar di taxonomy.json")
            continue
        texts_in_file = set()
        for idx, e in enumerate(data["entries"], 1):
            eid = e["id"]
            where = f"{name}:{eid}"
            # --- id ---
            prefix, num = eid.split("-")
            if prefix != spec["id_prefix"]:
                report.error(f"{where}: prefix id harus '{spec['id_prefix']}'")
            if int(num) != idx:
                report.warn(f"{where}: id tidak berurutan (posisi {idx})")
            if eid in all_ids:
                report.error(f"{where}: id duplikat (juga di {all_ids[eid]})")
            all_ids[eid] = name
            # --- taxonomy ---
            cat, sub = e["category"], e["subcategory"]
            if cat not in spec["categories"]:
                report.error(f"{where}: kategori '{cat}' tidak diizinkan di {name}")
            if sub not in taxonomy["subcategories"].get(cat, []):
                report.error(f"{where}: subkategori '{sub}' tidak valid untuk '{cat}'")
            used_sub.add((cat, sub))
            if e["language"] not in taxonomy["languages"]:
                report.error(f"{where}: kode bahasa '{e['language']}' tidak ada di taxonomy")
            # --- text / duplicates ---
            if e["normalized_text"] != normalize_key(e["text"]):
                report.error(f"{where}: normalized_text harus '{normalize_key(e['text'])}'")
            if e["text"] in texts_in_file:
                report.error(f"{where}: text '{e['text']}' duplikat dalam berkas")
            texts_in_file.add(e["text"])
            key = (e["text"], cat)
            if key in by_text_cat:
                report.error(f"{where}: text+kategori duplikat dengan {by_text_cat[key]}")
            by_text_cat[key] = where
            by_norm[e["normalized_text"]].append((where, cat, e["spoken_form"]))
            if e.get("respelling") is not None and e["respelling"] == e["spoken_form"]:
                report.warn(f"{where}: respelling sama dengan spoken_form (isi null saja)")
            # --- sources & provenance ---
            all_srcs = list(e["source"])
            for v in e["variants"]:
                all_srcs += v["source"]
            for s in all_srcs:
                if s not in sources:
                    report.error(f"{where}: sumber '{s}' tidak ada di sources.json")
                used_sources[s] += 1
            kinds = {src_kind[sources[s]["type"]] for s in all_srcs if s in sources}
            expected = kinds.pop() if len(kinds) == 1 else "mixed"
            if e["provenance"] != expected:
                report.error(f"{where}: provenance '{e['provenance']}' seharusnya '{expected}'")
            entry_types = {sources[s]["type"] for s in e["source"] if s in sources}
            if e["confidence"] == "standard" and "external" not in entry_types:
                report.error(f"{where}: confidence 'standard' wajib punya sumber eksternal normatif")
            if e["confidence"] == "attested" and entry_types == {"interpretation"}:
                report.error(f"{where}: confidence 'attested' butuh sumber ZIP atau eksternal")
            if e["review_status"] == "reviewed" and "review" not in e["notes"].lower():
                report.warn(f"{where}: status reviewed tanpa catatan reviewer di notes")
            # --- IPA ---
            if e["ipa"]:
                check_ipa(report, where, e["ipa"])
            for vi, v in enumerate(e["variants"]):
                if v.get("ipa"):
                    check_ipa(report, f"{where}/variants[{vi}]", v["ipa"])
                if v["spoken_form"] == e["spoken_form"] and v.get("respelling") in (None, e.get("respelling")) and v.get("ipa") in (None, e["ipa"]) and not v.get("meaning_changing"):
                    report.warn(f"{where}/variants[{vi}]: varian identik dengan bentuk utama")
            # --- ambiguity / homograph ---
            if sub == "homograph":
                mc = [v for v in e["variants"] if v.get("meaning_changing")]
                if len(mc) < 2:
                    report.error(f"{where}: homograf wajib punya >= 2 varian meaning_changing")
                if not e.get("ambiguous"):
                    report.error(f"{where}: homograf wajib ambiguous=true")
            # --- patterns ---
            if e["entry_type"] == "pattern":
                try:
                    rx = re.compile(e["pattern"])
                except re.error as exc:
                    report.error(f"{where}: regex tidak valid: {exc}")
                    rx = None
                if rx:
                    for ex in e["examples"]:
                        if not rx.search(ex["input"]):
                            report.error(f"{where}: contoh '{ex['input']}' tidak cocok dengan pola")
            for r in e.get("related", []):
                related_refs.append((where, r))
            # --- stats ---
            stats["file"][name] += 1
            stats["confidence"][e["confidence"]] += 1
            stats["provenance"][e["provenance"]] += 1
            stats["entry_type"][e["entry_type"]] += 1
            stats["ipa"]["dengan IPA" if e["ipa"] or any(v.get("ipa") for v in e["variants"]) else "tanpa IPA"] += 1
            if e.get("ambiguous"):
                stats["flags"]["ambiguous"] += 1

    cross_category: list = []
    for where, r in related_refs:
        if r not in all_ids:
            report.error(f"{where}: related '{r}' tidak ditemukan")
    # True duplicates: same normalized text, category and reading.
    for norm, items in by_norm.items():
        seen = {}
        for where, cat, spoken in items:
            k = (cat, spoken)
            if k in seen:
                report.error(f"duplikat isi: '{norm}' {where} == {seen[k]}")
            seen[k] = where
        cats = {c for _, c, _ in items}
        if len(items) > 1 and len(cats) > 1:
            cross_category.append((norm, [w for w, _, _ in items]))
    for s in sources:
        if s not in used_sources and s not in ("agentskills-spec", "ipa-handbook-1999", "ipa-chart-2020", "cohn-1989", "goedemans-vanzanten-2007", "chaer-2009", "muslich-2008", "hdi-ebook-2026", "hdi-toolkit-2026"):
            report.warn(f"sumber '{s}' tidak dirujuk entri mana pun (boleh jika dirujuk dokumen)")
    declared = {(c, s) for c, subs in taxonomy["subcategories"].items() for s in subs}
    for c, s in sorted(declared - used_sub):
        report.warn(f"subkategori '{c}/{s}' terdaftar tetapi belum dipakai")

    total = sum(stats["file"].values())
    if show_stats and cross_category:
        print("  INFO homograf lintas kategori (disengaja, mis. huruf 'M' vs satuan 'm'):")
        for norm, ws in cross_category:
            print(f"       '{norm}': {ws}")
    print(f"  Total entri: {total}")
    if show_stats:
        for group, counter in stats.items():
            print(f"  {group}: " + ", ".join(f"{k}={v}" for k, v in sorted(counter.items())))
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
