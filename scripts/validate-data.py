#!/usr/bin/env python3
"""Validasi sintaks JSON seluruh repo dan kesesuaian dataset terhadap JSON Schema.

Pemakaian:  python scripts/validate-data.py
Butuh: jsonschema>=4.18 (pip install -r requirements.txt)
"""
from __future__ import annotations

import json
import sys

from _common import DATASET_FILES, DICT_DIR, META_DIR, ROOT, SCHEMA_DIR, Report, load_json

try:
    from jsonschema import Draft202012Validator
except ImportError:  # pragma: no cover
    print("jsonschema belum terpasang. Jalankan: pip install -r requirements.txt")
    sys.exit(2)


def check_syntax(report: Report) -> int:
    count = 0
    for path in sorted(ROOT.rglob("*.json")):
        if ".git" in path.parts or "node_modules" in path.parts:
            continue
        count += 1
        try:
            with open(path, encoding="utf-8") as f:
                json.load(f)
        except json.JSONDecodeError as exc:
            report.error(f"{path.relative_to(ROOT)}: JSON tidak valid: {exc}")
    return count


def validate(report: Report, schema_name: str, data_path):
    schema = load_json(SCHEMA_DIR / schema_name)
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema)
    data = load_json(data_path)
    errs = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    for err in errs[:50]:
        loc = "/".join(str(p) for p in err.absolute_path) or "(root)"
        report.error(f"{data_path.relative_to(ROOT)} @ {loc}: {err.message}")
    if len(errs) > 50:
        report.error(f"{data_path.relative_to(ROOT)}: {len(errs) - 50} error tambahan disembunyikan")


def main() -> int:
    report = Report("validate-data (sintaks JSON + JSON Schema)")
    n = check_syntax(report)
    if report.errors:
        return report.finish()
    for name in DATASET_FILES:
        validate(report, "pronunciation.schema.json", DICT_DIR / name)
    validate(report, "sources.schema.json", META_DIR / "sources.json")
    validate(report, "tests.schema.json", ROOT / "tests" / "pronunciation-tests.json")
    print(f"  {n} berkas JSON terbaca; {len(DATASET_FILES)} dataset + sources + tests divalidasi terhadap schema.")
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
