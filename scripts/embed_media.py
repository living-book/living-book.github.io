#!/usr/bin/env python3
"""Stage 5: embed audio player + START/END infographics into chapter pages.

Usage: python3 scripts/embed_media.py [book-slug]   (default: all books)
Run AFTER compress_images.py (references .jpg). Idempotent; embeds only existing assets.
"""
import re
import sys
from pathlib import Path

books = [Path("docs/books") / sys.argv[1]] if len(sys.argv) > 1 else sorted(Path("docs/books").iterdir())

for book in books:
    chapters = book / "chapters"
    if not chapters.is_dir():
        continue
    for ch in sorted(chapters.glob("*.md")):
        slug = ch.stem
        text = ch.read_text()
        if "<audio" in text or "-start." in text:
            print(f"skip {slug}")
            continue
        audio = book / "audio" / f"{slug}.mp3"
        start = book / "infographics" / f"{slug}-start.jpg"
        end = book / "infographics" / f"{slug}-end.jpg"

        header = ""
        if audio.exists():
            header += f'\n<audio controls preload="none" style="width:100%" src="../../audio/{slug}.mp3"></audio>\n'
        if start.exists():
            header += f"\n![{slug} overview infographic](../infographics/{slug}-start.jpg)\n"
        if header:
            text = re.sub(r"(^# .+$)", r"\1\n" + header, text, count=1, flags=re.M)
        if end.exists():
            block = f"![{slug} transformation infographic](../infographics/{slug}-end.jpg)\n\n"
            if "## Reflection Questions" in text:
                text = text.replace("## Reflection Questions", block + "## Reflection Questions", 1)
            else:
                text += "\n" + block
        ch.write_text(text)
        print(f"ok   {slug} audio={audio.exists()} start={start.exists()} end={end.exists()}")
