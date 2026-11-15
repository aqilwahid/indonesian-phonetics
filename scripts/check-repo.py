#!/usr/bin/env python3
"""Pemeriksaan kebersihan repo: tautan Markdown, rujukan id entri, frontmatter SKILL.md, sinkron sumber, berkas sementara, dan rahasia.

Pemakaian:  python scripts/check-repo.py
Hanya pustaka standar.
"""
from __future__ import annotations

import re
import subprocess
import sys
import unicodedata
from pathlib import Path

from _common import META_DIR, ROOT, SKILL_DIR, Report, load_json

LINK_RE = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
IMG_RE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)\)")
SECRET_PATTERNS = {
    "GitHub token": re.compile(r"gh[pousr]_[A-Za-z0-9]{36,}"),
    "OpenAI/Anthropic-style key": re.compile(r"\bsk-(?:ant-)?[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "ElevenLabs key assignment": re.compile(r"(?i)xi-api-key\s*[:=]\s*['\"]?[a-f0-9]{24,}"),
    "Generic secret assignment": re.compile(r"(?i)\b(api[_-]?key|secret|password|token)\b\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"]"),
}
TEMP_PATTERNS = ["*.pyc", "*~", "*.swp", ".DS_Store", "Thumbs.db", "*.tmp", "*.bak", ".env", "*.log"]
TEXT_EXT = {".md", ".json", ".py", ".yml", ".yaml", ".txt", ".toml", ".cfg"}


def slugify(heading: str) -> str:
    """Perkiraan aturan anchor GitHub."""
    h = heading.strip().lower()
    h = re.sub(r"[`*_~]", "", h)
    h = unicodedata.normalize("NFKD", h)
    out = []
    for ch in h:
        if ch.isalnum() or ch in "-_":
            out.append(ch)
        elif ch == " ":
            out.append("-")
        elif unicodedata.category(ch) == "Mn":
            continue
    return "".join(out)


def anchors_of(md: Path) -> set[str]:
    anchors, seen = set(), {}
    in_code = False
    for line in md.read_text(encoding="utf-8").splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = re.match(r"^#{1,6}\s+(.*)$", line)
        if m:
            s = slugify(m.group(1))
            n = seen.get(s, 0)
            anchors.add(s if n == 0 else f"{s}-{n}")
            seen[s] = n + 1
    return anchors


def iter_files():
    """Berkas yang akan masuk repo (menghormati .gitignore bila git tersedia)."""
    try:
        out = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT,
                             capture_output=True, text=True, check=True).stdout.splitlines()
        for rel in out:
            p = ROOT / rel
            if p.is_file():
                yield p
        return
    except (OSError, subprocess.CalledProcessError):
        pass
    for p in ROOT.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        yield p


def check_links(report: Report):
    for md in sorted(ROOT.rglob("*.md")):
        if ".git" in md.parts:
            continue
        text = md.read_text(encoding="utf-8")
        text_nocode = re.sub(r"```.*?```", "", text, flags=re.S)
        for target in LINK_RE.findall(text_nocode) + IMG_RE.findall(text_nocode):
            if re.match(r"^(https?:|mailto:)", target):
                continue
            path_part, _, anchor = target.partition("#")
            dest = md if not path_part else (md.parent / path_part).resolve()
            rel = md.relative_to(ROOT)
            if not dest.exists():
                report.error(f"{rel}: tautan rusak → {target}")
                continue
            if anchor and dest.suffix == ".md" and anchor not in anchors_of(dest):
                report.error(f"{rel}: anchor tidak ditemukan → {target}")
            if SKILL_DIR in md.parents or md.parent == SKILL_DIR:
                if SKILL_DIR not in dest.parents and dest != SKILL_DIR:
                    report.error(f"{rel}: tautan keluar dari folder skill ({target}); skill harus mandiri")


def check_skill(report: Report):
    skill_md = SKILL_DIR / "SKILL.md"
    text = skill_md.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, flags=re.S)
    if not m:
        report.error("SKILL.md: frontmatter YAML tidak ditemukan")
        return
    fm = m.group(1)
    fields = dict(re.findall(r"^([a-z-]+):\s*(.*)$", fm, flags=re.M))
    name = fields.get("name", "").strip()
    desc = fields.get("description", "").strip()
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        report.error(f"SKILL.md: name '{name}' tidak memenuhi spesifikasi Agent Skills")
    if name != SKILL_DIR.name:
        report.error(f"SKILL.md: name '{name}' harus sama dengan nama folder '{SKILL_DIR.name}'")
    if not (1 <= len(desc) <= 1024):
        report.error(f"SKILL.md: description {len(desc)} karakter (harus 1–1024)")
    comp = fields.get("compatibility", "")
    if comp and len(comp) > 500:
        report.error("SKILL.md: compatibility > 500 karakter")
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    for key in fields:
        if key not in allowed:
            report.error(f"SKILL.md: field frontmatter tidak dikenal '{key}'")
    if "metadata:" in fm:
        for line in fm.split("metadata:", 1)[1].splitlines()[1:]:
            if line.startswith("  ") and ":" in line:
                val = line.split(":", 1)[1].strip()
                if not (val.startswith('"') and val.endswith('"')):
                    report.warn(f"SKILL.md: nilai metadata sebaiknya string berkutip: {line.strip()}")
    lines = text.count("\n")
    if lines > 500:
        report.error(f"SKILL.md: {lines} baris (rekomendasi spesifikasi < 500)")
    words = len(text.split())
    if words > 3500:
        report.warn(f"SKILL.md: {words} kata; pertimbangkan memindahkan isi ke references/")
    for ref in re.findall(r"\]\((references/[^)#]+)", text):
        if not (SKILL_DIR / ref).exists():
            report.error(f"SKILL.md: rujukan {ref} tidak ada")
    for f in (SKILL_DIR / "references").glob("*.md"):
        if f"references/{f.name}" not in text:
            report.warn(f"SKILL.md tidak merujuk references/{f.name}")


def check_sources_doc(report: Report):
    doc = (ROOT / "docs" / "sources.md").read_text(encoding="utf-8")
    for s in load_json(META_DIR / "sources.json")["sources"]:
        if f"`{s['id']}`" not in doc:
            report.error(f"docs/sources.md belum memuat sumber '{s['id']}'")


def check_entry_refs(report: Report):
    """Id entri yang disebut di Markdown (mis. `tech-0005`) harus ada di dataset."""
    ids = set()
    for f in (ROOT / "dictionary").glob("*.json"):
        ids |= {e["id"] for e in load_json(f)["entries"]}
    rx = re.compile(r"\b((?:abbr|acr|tech|loan|num|sym|dt|word)-\d{4})\b")
    for md in ROOT.rglob("*.md"):
        if ".git" in md.parts:
            continue
        for ref in set(rx.findall(md.read_text(encoding="utf-8"))):
            if ref not in ids:
                report.error(f"{md.relative_to(ROOT)}: rujukan entri '{ref}' tidak ada di dataset")


def check_hygiene(report: Report):
    for p in iter_files():
        rel = p.relative_to(ROOT)
        if any(p.match(pat) for pat in TEMP_PATTERNS) or "__pycache__" in p.parts:
            report.error(f"berkas sementara/sensitif: {rel}")
        if p.suffix.lower() in TEXT_EXT:
            text = p.read_text(encoding="utf-8", errors="ignore")
            for label, rx in SECRET_PATTERNS.items():
                if rx.search(text):
                    report.error(f"kemungkinan rahasia ({label}) di {rel}")
        if p.stat().st_size > 5 * 1024 * 1024:
            report.warn(f"berkas besar (>5 MB): {rel}")
    for name in ("README.md", "LICENSE", "CONTRIBUTING.md", "CHANGELOG.md"):
        if not (ROOT / name).exists():
            report.error(f"berkas wajib tidak ada: {name}")


def main() -> int:
    report = Report("check-repo (tautan, skill, sumber, kebersihan)")
    check_links(report)
    check_skill(report)
    check_sources_doc(report)
    check_entry_refs(report)
    check_hygiene(report)
    return report.finish()


if __name__ == "__main__":
    sys.exit(main())
