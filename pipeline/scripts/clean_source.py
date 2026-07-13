#!/usr/bin/env python3
"""Clean PDF->markdown conversion artifacts from a book source file.

Usage: clean_source.py <slug>
Reads source path from sources/manifest.yml, writes pipeline/work/<slug>/clean.md

Rules (extend as new books reveal new artifacts):
- Drop page-stamp lines (e.g. "17. zari 2004  ...  123 ze 412")
- Drop markdown table separator rows (| --- | --- |)
- Flatten fake layout tables: | THE | FIFTH | -> THE FIFTH
- Collapse runs of blank lines
"""
import re, sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]   # living-books/
SOURCES = ROOT / "sources"
WORK = ROOT / "pipeline" / "work"

PAGE_STAMP = re.compile(r'\b\d+\s+ze\s+\d+\s*$')          # "N ze M" (Czech "of") page marker
TABLE_SEP  = re.compile(r'^\s*\|[\s\-:|]+\|\s*$')
TABLE_ROW  = re.compile(r'^\s*\|.*\|\s*$')

def flatten_table_row(line: str) -> str:
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    return re.sub(r'\s{2,}', ' ', ' '.join(c for c in cells if c))

def clean(text: str) -> str:
    out = []
    for line in text.splitlines():
        if PAGE_STAMP.search(line) or TABLE_SEP.match(line):
            continue
        if TABLE_ROW.match(line):
            line = flatten_table_row(line)
            if not line:
                continue
        out.append(line.rstrip())
    result = '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', result).strip() + '\n'

def main():
    slug = sys.argv[1]
    manifest = yaml.safe_load((SOURCES / "manifest.yml").read_text())
    entry = manifest["shelf"].get(slug) or manifest.get("library", {}).get(slug)
    if not entry or not entry.get("source"):
        sys.exit(f"no source for slug '{slug}' in manifest.yml")
    src = SOURCES / entry["source"]
    raw = src.read_text(encoding="utf-8", errors="replace")
    cleaned = clean(raw)
    dest = WORK / slug / "clean.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(cleaned, encoding="utf-8")
    print(f"{slug}: {len(raw.splitlines())} -> {len(cleaned.splitlines())} lines, "
          f"{len(cleaned.split())} words -> {dest.relative_to(ROOT)}")

if __name__ == "__main__":
    main()
