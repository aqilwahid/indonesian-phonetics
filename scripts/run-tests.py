#!/usr/bin/env python3
"""Jalankan tests/pronunciation-tests.json terhadap leksikon skill dan normalize.py.

Pemakaian:  python scripts/run-tests.py [-v]
"""
from __future__ import annotations

import sys
from collections import Counter

from _common import LEXICON_PATH, ROOT, SKILL_DIR, load_json

sys.path.insert(0, str(SKILL_DIR / "scripts"))
from lookup import load_lexicon, lookup  # noqa: E402
from normalize import normalize  # noqa: E402


def run_case(case: dict, lex: dict) -> tuple[bool, str]:
    typ, inp, exp = case["type"], case["input"], case["expected"]
    opts = case.get("options", {})
    if typ in ("lookup", "variant", "ambiguity", "ipa"):
        hits = lookup(lex, inp)
        if not hits:
            return False, "entri tidak ditemukan"
        e = hits[0]
        if typ == "lookup":
            if e["spoken_form"] != exp["spoken_form"]:
                return False, f"spoken_form '{e['spoken_form']}' != '{exp['spoken_form']}'"
            if "respelling" in exp and e.get("respelling") != exp["respelling"]:
                return False, f"respelling '{e.get('respelling')}' != '{exp['respelling']}'"
            return True, ""
        if typ == "variant":
            forms = {v["spoken_form"] for v in e["variants"]} | {v.get("respelling") for v in e["variants"]}
            return (exp["spoken_form"] in forms or any(exp["spoken_form"] == v.get("respelling") for v in e["variants"])), f"varian tersedia: {sorted(f for f in forms if f)}"
        if typ == "ambiguity":
            ok = bool(e.get("ambiguous")) and len(e["variants"]) >= exp.get("min_variants", 1) and bool(e.get("disambiguation"))
            return ok, f"ambiguous={e.get('ambiguous')} variants={len(e['variants'])}"
        if typ == "ipa":
            return e["ipa"] == exp["ipa"], f"ipa {e['ipa']!r} != {exp['ipa']!r}"
    if typ in ("normalize", "flag"):
        res = normalize(inp, mode=opts.get("mode", "tts"), time_style=opts.get("time_style", "formal"), lexicon=lex)
        if typ == "normalize":
            return res["output"] == exp["output"], f"keluaran: {res['output']!r}"
        tokens = [r["token"] for r in res["ragu"]]
        return any(exp["contains"] in t for t in tokens), f"RAGU: {tokens}"
    return False, f"tipe tidak dikenal: {typ}"


def main() -> int:
    verbose = "-v" in sys.argv
    if not LEXICON_PATH.exists():
        print("lexicon.json belum ada. Jalankan scripts/build-skill-assets.py")
        return 2
    lex = load_lexicon(LEXICON_PATH)
    suite = load_json(ROOT / "tests" / "pronunciation-tests.json")
    passed, failed = Counter(), []
    for case in suite["tests"]:
        ok, detail = run_case(case, lex)
        if ok:
            passed[case["category"]] += 1
            if verbose:
                print(f"  PASS {case['id']} [{case['category']}] {case['input']}")
        else:
            failed.append((case, detail))
            print(f"  FAIL {case['id']} [{case['category']}/{case['type']}] {case['input']!r}: {detail}")
    total = len(suite["tests"])
    print("  per kategori lulus: " + ", ".join(f"{k}={v}" for k, v in sorted(passed.items())))
    status = "OK" if not failed else "FAILED"
    print(f"[{status}] run-tests: {total - len(failed)}/{total} lulus")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
