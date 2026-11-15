#!/usr/bin/env python3
"""Kompilasi dictionary/*.json menjadi skills/indonesian-phonetics/assets/lexicon.json.

Skill harus mandiri (bisa disalin tanpa folder dictionary/), jadi leksikon dibundel.
dictionary/ tetap sumber kebenaran; jangan edit lexicon.json secara manual.

Pemakaian:
  python scripts/build-skill-assets.py          # tulis ulang lexicon.json
  python scripts/build-skill-assets.py --check  # gagal jika lexicon.json tidak sinkron
"""
from __future__ import annotations

import hashlib
import json
import sys

from _common import DATASET_FILES, DICT_DIR, LEXICON_PATH, META_DIR, load_json


def build() -> str:
    files, entries = [], []
    for name in DATASET_FILES:
        raw = (DICT_DIR / name).read_bytes()
        files.append({"file": f"dictionary/{name}", "sha256": hashlib.sha256(raw).hexdigest()})
        data = json.loads(raw)
        for e in data["entries"]:
            e = dict(e)
            e["dataset"] = data["dataset"]
            entries.append(e)
    sources = {s["id"]: {"type": s["type"], "title": s["title"]} for s in load_json(META_DIR / "sources.json")["sources"]}
    doc = {
        "about": "Leksikon terkompilasi untuk skill indonesian-phonetics. Dibangkitkan oleh scripts/build-skill-assets.py; jangan diedit manual.",
        "version": "1.0.0",
        "generated_from": files,
        "entry_count": len(entries),
        "sources": sources,
        "entries": entries,
    }
    return json.dumps(doc, ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\n"


def main() -> int:
    content = build()
    if "--check" in sys.argv:
        current = LEXICON_PATH.read_text(encoding="utf-8") if LEXICON_PATH.exists() else ""
        if current != content:
            print("[FAILED] lexicon.json tidak sinkron dengan dictionary/. Jalankan: python scripts/build-skill-assets.py")
            return 1
        print(f"[OK] lexicon.json sinkron ({json.loads(content)['entry_count']} entri)")
        return 0
    LEXICON_PATH.parent.mkdir(parents=True, exist_ok=True)
    LEXICON_PATH.write_text(content, encoding="utf-8")
    print(f"Ditulis {LEXICON_PATH} ({json.loads(content)['entry_count']} entri, {len(content.encode()) // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
