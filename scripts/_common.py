"""Shared helpers for repository scripts. Standard library only (jsonschema is optional, used by validate-data.py)."""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DICT_DIR = ROOT / "dictionary"
META_DIR = DICT_DIR / "meta"
SCHEMA_DIR = ROOT / "schemas"
SKILL_DIR = ROOT / "skills" / "indonesian-phonetics"
LEXICON_PATH = SKILL_DIR / "assets" / "lexicon.json"

DATASET_FILES = [
    "abbreviations.json",
    "acronyms.json",
    "technology.json",
    "loanwords.json",
    "numbers.json",
    "symbols.json",
    "dates-and-times.json",
    "pronunciation-dictionary.json",
]


def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def normalize_key(text: str) -> str:
    """NFC + lowercase + single spaces. Must match `normalized_text` in every entry."""
    text = unicodedata.normalize("NFC", text).lower()
    return re.sub(r"\s+", " ", text).strip()


def iter_datasets():
    for name in DATASET_FILES:
        path = DICT_DIR / name
        yield name, path, load_json(path)


class Report:
    def __init__(self, title: str):
        self.title = title
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, msg: str):
        self.errors.append(msg)

    def warn(self, msg: str):
        self.warnings.append(msg)

    def finish(self) -> int:
        for w in self.warnings:
            print(f"  WARN  {w}")
        for e in self.errors:
            print(f"  ERROR {e}")
        status = "FAILED" if self.errors else "OK"
        print(f"[{status}] {self.title}: {len(self.errors)} error(s), {len(self.warnings)} warning(s)")
        return 1 if self.errors else 0
