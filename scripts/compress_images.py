#!/usr/bin/env python3
"""Stage 3 post-step: compress infographic PNGs to 1600w JPEG q85 (~12x smaller).

Converts every .png under docs/books/*/infographics/ to .jpg, deletes the .png,
and rewrites references in the book's markdown. Idempotent.
Run from repo root: python3 scripts/compress_images.py
"""
from pathlib import Path
from PIL import Image

for png in sorted(Path("docs/books").glob("*/infographics/*.png")):
    img = Image.open(png).convert("RGB")
    if img.width > 1600:
        img = img.resize((1600, round(img.height * 1600 / img.width)), Image.LANCZOS)
    jpg = png.with_suffix(".jpg")
    img.save(jpg, quality=85)
    png.unlink()
    print(f"{png.name} -> {jpg.name} ({jpg.stat().st_size//1024}K)")

# rewrite references
for md in Path("docs").rglob("*.md"):
    t = md.read_text()
    if "infographics/" in t and ".png" in t:
        import re
        t2 = re.sub(r"(infographics/[\w.-]+)\.png", r"\1.jpg", t)
        if t2 != t:
            md.write_text(t2)
            print(f"refs updated: {md}")
