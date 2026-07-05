#!/usr/bin/env python3
"""Stage 5: embed audio player + START/END infographics into chapter pages.

Idempotent — skips chapters already embedded. Only embeds assets that exist.
Run from repo root: python3 scripts/embed_media.py
"""
import re
from pathlib import Path

BOOK = Path("docs/books/laws-of-human-nature")
CHAPTERS = BOOK / "chapters"

for ch in sorted(CHAPTERS.glob("law-*.md")):
    if ch.name.endswith("-study-guide.md"):
        continue
    slug = ch.stem
    text = ch.read_text()
    if "<audio" in text or "-start.png" in text:
        print(f"skip {slug}")
        continue
    audio = BOOK / "audio" / f"{slug}.mp3"
    start = BOOK / "infographics" / f"{slug}-start.png"
    end = BOOK / "infographics" / f"{slug}-end.png"

    header = ""
    if audio.exists():
        header += f'\n<audio controls preload="none" style="width:100%" src="../../audio/{slug}.mp3"></audio>\n'
    if start.exists():
        header += f"\n![{slug} overview infographic](../infographics/{slug}-start.png)\n"
    if header:
        # insert after the H1 line
        text = re.sub(r"(^# .+$)", r"\1\n" + header, text, count=1, flags=re.M)
    if end.exists():
        block = f"![{slug} transformation infographic](../infographics/{slug}-end.png)\n\n"
        if "## Reflection Questions" in text:
            text = text.replace("## Reflection Questions", block + "## Reflection Questions", 1)
        else:
            text += "\n" + block
    ch.write_text(text)
    print(f"ok   {slug} audio={audio.exists()} start={start.exists()} end={end.exists()}")
