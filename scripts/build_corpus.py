#!/usr/bin/env python3
"""Build docs/ask/corpus.json from all book chapter + study-guide markdown files.

Run before mkdocs build. Strips frontmatter, audio tags, image markdown.
Output: JSON array [{book, book_title, type, title, content, url}]
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
DOCS = ROOT / "docs" / "books"
OUT  = ROOT / "docs" / "ask" / "corpus.json"

STRIP_FRONTMATTER = re.compile(r'^---\n.*?\n---\n', re.DOTALL)
STRIP_AUDIO       = re.compile(r'<audio[^>]*>.*?</audio>', re.DOTALL | re.IGNORECASE)
STRIP_IMG         = re.compile(r'!\[.*?\]\(.*?\)')
STRIP_BLANK_LINES = re.compile(r'\n{3,}')

def clean(text: str) -> str:
    text = STRIP_FRONTMATTER.sub('', text)
    text = STRIP_AUDIO.sub('', text)
    text = STRIP_IMG.sub('', text)
    text = STRIP_BLANK_LINES.sub('\n\n', text)
    return text.strip()

def first_heading(text: str) -> str:
    m = re.search(r'^#\s+(.+)', text, re.MULTILINE)
    return m.group(1).strip() if m else ''

def book_title_from_index(path: Path) -> str:
    if not path.exists():
        return ''
    m = re.search(r'^#\s+(.+)', path.read_text(), re.MULTILINE)
    return m.group(1).strip() if m else ''

def main():
    OUT.parent.mkdir(exist_ok=True)
    chunks = []

    for book_dir in sorted(DOCS.iterdir()):
        if not book_dir.is_dir():
            continue
        slug = book_dir.name
        book_title = book_title_from_index(book_dir / 'index.md') or slug.replace('-', ' ').title()

        for section, type_label in [('chapters', 'chapter'), ('study-guides', 'study-guide'), ('concepts', 'concept')]:
            section_dir = book_dir / section
            if not section_dir.exists():
                continue
            for f in sorted(section_dir.glob('*.md')):
                if f.stem == 'index':
                    continue
                raw = f.read_text(encoding='utf-8')
                content = clean(raw)
                title = first_heading(content) or f.stem.replace('-', ' ').title()
                # Strip leading h1 from content (already captured as title)
                content_body = re.sub(r'^#\s+.+\n', '', content, count=1).strip()
                chunks.append({
                    'book': slug,
                    'book_title': book_title,
                    'type': type_label,
                    'title': title,
                    'content': content_body,
                    'url': f'/books/{slug}/{section}/{f.stem}/'
                })

    # atlas-only books (concepts live under docs/atlas/concepts/<book>/ until the
    # book gets a full companion) — pull display titles from atlas.json
    atlas_json = ROOT / 'docs' / 'atlas' / 'atlas.json'
    titles = {}
    if atlas_json.exists():
        titles = {b['slug']: b['title'] for b in json.loads(atlas_json.read_text())['books']}
    atlas_dir = ROOT / 'docs' / 'atlas' / 'concepts'
    if atlas_dir.is_dir():
        for book_dir in sorted(atlas_dir.iterdir()):
            if not book_dir.is_dir():
                continue
            slug = book_dir.name
            for f in sorted(book_dir.glob('*.md')):
                if f.stem == 'index':
                    continue
                content = clean(f.read_text(encoding='utf-8'))
                title = first_heading(content) or f.stem.replace('-', ' ').title()
                chunks.append({
                    'book': slug,
                    'book_title': titles.get(slug, slug.replace('-', ' ').title()),
                    'type': 'concept',
                    'title': title,
                    'content': re.sub(r'^#\s+.+\n', '', content, count=1).strip(),
                    'url': f'/atlas/#{f.stem}'
                })

    OUT.write_text(json.dumps(chunks, ensure_ascii=False, separators=(',', ':')))
    total_kb = OUT.stat().st_size // 1024
    print(f"corpus.json: {len(chunks)} chunks, {total_kb}KB → {OUT}")

if __name__ == '__main__':
    main()
