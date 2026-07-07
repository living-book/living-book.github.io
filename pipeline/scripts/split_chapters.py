#!/usr/bin/env python3
"""Slice pipeline/work/<slug>/clean.md into chapter files by an agent-authored map.

Usage: split_chapters.py <slug>
Reads pipeline/work/<slug>/chapters.yml:

    chapters:
      - {n: 0,  slug: front-matter, title: Front Matter,        start_line: 1}
      - {n: 1,  slug: give-me-a-lever, title: "Give Me a Lever...", start_line: 610}
      ...

start_line = 1-based line number in clean.md where the chapter begins.
Each chapter runs to the next entry's start_line - 1. Last runs to EOF.
Writes pipeline/work/<slug>/chapters/NN-slug.md
"""
import sys
from pathlib import Path

import yaml

WORK = Path(__file__).resolve().parents[2] / "pipeline" / "work"

def main():
    slug = sys.argv[1]
    book = WORK / slug
    lines = (book / "clean.md").read_text(encoding="utf-8").splitlines()
    chapters = yaml.safe_load((book / "chapters.yml").read_text())["chapters"]
    chapters = sorted(chapters, key=lambda c: c["start_line"])
    assert chapters[0]["start_line"] >= 1
    assert chapters[-1]["start_line"] <= len(lines), "start_line beyond EOF"

    outdir = book / "chapters"
    outdir.mkdir(exist_ok=True)
    for cur, nxt in zip(chapters, chapters[1:] + [None]):
        end = (nxt["start_line"] - 1) if nxt else len(lines)
        body = "\n".join(lines[cur["start_line"] - 1 : end]).strip()
        dest = outdir / f"{cur['n']:02d}-{cur['slug']}.md"
        dest.write_text(f"# {cur['title']}\n\n{body}\n", encoding="utf-8")
        print(f"{dest.name}: {len(body.split())} words")

if __name__ == "__main__":
    main()
