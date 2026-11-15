#!/usr/bin/env python3
"""Cari entri pelafalan di leksikon skill, atau pindai teks untuk menemukan token yang butuh interpretasi.

Pemakaian:
  python scripts/lookup.py HP                 # cari satu bentuk tulis
  python scripts/lookup.py "Content ID" --json
  python scripts/lookup.py --scan "Cek HP kamu, CTR naik 4,2%."
  python scripts/lookup.py --search kecap      # cari di text, spoken_form, dan varian

Hanya pustaka standar Python 3.9+. Membaca assets/lexicon.json relatif terhadap folder skill.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
LEXICON = SKILL_ROOT / "assets" / "lexicon.json"


def normalize_key(text: str) -> str:
    text = unicodedata.normalize("NFC", text).lower()
    return re.sub(r"\s+", " ", text).strip()


def load_lexicon(path: Path = LEXICON) -> dict:
    if not path.exists():
        sys.exit(f"Leksikon tidak ditemukan: {path}. Di repo, jalankan scripts/build-skill-assets.py.")
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def lookup(lex: dict, text: str) -> list[dict]:
    """Cocok persis (peka huruf besar) dulu; jika kosong, cocok normalized_text."""
    exact = [e for e in lex["entries"] if e["text"] == text]
    if exact:
        return exact
    key = normalize_key(text)
    return [e for e in lex["entries"] if e["normalized_text"] == key]


def search(lex: dict, term: str) -> list[dict]:
    key = normalize_key(term)
    out = []
    for e in lex["entries"]:
        hay = [e["normalized_text"], normalize_key(e["spoken_form"])] + [normalize_key(v["spoken_form"]) for v in e["variants"]]
        if any(key in h for h in hay):
            out.append(e)
    return out


def _boundary_regex(text: str) -> re.Pattern:
    return re.compile(r"(?<![\w])" + re.escape(text) + r"(?![\w])")


NUMERIC_HINT = re.compile(r"\d|[%&/@#±~×÷=<>+]")


def scan(lex: dict, sentence: str) -> dict:
    """Temukan entri leksikal (peka huruf besar) dan pola (angka, tanggal, simbol) dalam teks."""
    hits, taken = [], []
    lexical = [e for e in lex["entries"] if e["entry_type"] == "lexical" and e["category"] != "general"]
    lexical += [e for e in lex["entries"] if e["category"] == "general" and e.get("ambiguous")]
    for e in sorted(lexical, key=lambda x: -len(x["text"])):
        t = e["text"]
        if len(t) == 1 and t.isalpha():
            continue  # huruf tunggal terlalu bising; tangani manual
        for m in _boundary_regex(t).finditer(sentence):
            span = (m.start(), m.end())
            if any(a < span[1] and span[0] < b for a, b in taken):
                continue
            taken.append(span)
            hits.append({"match": m.group(0), "start": m.start(), "id": e["id"], "dataset": e["dataset"],
                         "ambiguous": bool(e.get("ambiguous")), "confidence": e["confidence"]})
    for e in lex["entries"]:
        if e["entry_type"] != "pattern":
            continue
        for m in re.finditer(e["pattern"], sentence):
            hits.append({"match": m.group(0), "start": m.start(), "id": e["id"], "dataset": e["dataset"],
                         "pattern": e["text"], "ambiguous": bool(e.get("ambiguous")), "confidence": e["confidence"]})
    hits.sort(key=lambda h: (h["start"], -len(h["match"])))
    unknown = []
    for m in re.finditer(r"\b[A-Z][A-Z0-9&]{1,}\b", sentence):
        if not any(h["start"] <= m.start() < h["start"] + len(h["match"]) for h in hits):
            unknown.append(m.group(0))
    return {"input": sentence, "hits": hits, "unknown_uppercase_tokens": unknown,
            "has_numeric_or_symbol": bool(NUMERIC_HINT.search(sentence))}


def summarize(e: dict) -> str:
    lines = [f"[{e['id']}] {e['text']}  ({e['dataset']} / {e['category']} / {e['subcategory']})",
             f"  bacaan       : {e['spoken_form']}"]
    if e.get("respelling"):
        lines.append(f"  respelling   : {e['respelling']}  (untuk teks TTS)")
    lines.append(f"  IPA          : {e['ipa'] or '— (tidak tersedia; jangan ditebak)'}")
    lines.append(f"  keyakinan    : {e['confidence']} | provenance: {e['provenance']} | review: {e['review_status']}")
    if e.get("ambiguous"):
        lines.append(f"  AMBIGU       : {e['disambiguation']}")
    for v in e["variants"]:
        tag = " [beda makna]" if v.get("meaning_changing") else ""
        extra = f" /{v['ipa'].strip('/')}/" if v.get("ipa") else ""
        resp = f" (respelling: {v['respelling']})" if v.get("respelling") else ""
        lines.append(f"  varian       : {v['spoken_form']}{resp}{extra} — {v['context']}{tag}")
    if e.get("tts_notes"):
        lines.append(f"  catatan TTS  : {e['tts_notes']}")
    if e.get("notes"):
        lines.append(f"  catatan      : {e['notes']}")
    return "\n".join(lines)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("text", nargs="?", help="bentuk tulis yang dicari")
    ap.add_argument("--scan", metavar="TEKS", help="pindai kalimat/paragraf")
    ap.add_argument("--search", metavar="ISTILAH", help="cari substring di text/bacaan/varian")
    ap.add_argument("--json", action="store_true", help="keluaran JSON")
    args = ap.parse_args()
    lex = load_lexicon()
    if args.scan:
        res = scan(lex, args.scan)
        print(json.dumps(res, ensure_ascii=False, indent=2))
        return 0
    results = search(lex, args.search) if args.search else (lookup(lex, args.text) if args.text else None)
    if results is None:
        ap.print_help()
        return 2
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif not results:
        print("Tidak ditemukan di leksikon. Terapkan aturan di references/, dan jika ragu tandai sebagai RAGU — jangan menebak.")
        return 1
    else:
        print("\n\n".join(summarize(e) for e in results))
    return 0


if __name__ == "__main__":
    sys.exit(main())
