#!/usr/bin/env python3
"""QA gate for extracted concept dirs: python3 scripts/qa_concepts.py <slug> [<slug>...]
Checks: YAML frontmatter parses + required keys, required sections, description length,
slug collisions vs CATALOG.md and across the given dirs."""
import sys, os, re, yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CATALOG = os.path.join(ROOT, 'pipeline/atlas/CATALOG.md')
REQ_KEYS = {'type', 'title', 'description', 'book', 'tags'}
REQ_SECTIONS = ['## Definition', '## In the Book', '## Why It Matters']

owned = set(re.findall(r'^- `([a-z0-9-]+)`', open(CATALOG).read(), re.M)) if os.path.exists(CATALOG) else set()
# fallback: any backticked kebab token at line start
if not owned:
    owned = set(re.findall(r'`([a-z0-9][a-z0-9-]+)`', open(CATALOG).read()))

seen = {}
fails = 0
for slug in sys.argv[1:]:
    d = os.path.join(ROOT, 'docs/atlas/concepts', slug)
    if not os.path.isdir(d):
        print(f"FAIL {slug}: dir missing"); fails += 1; continue
    files = sorted(f for f in os.listdir(d) if f.endswith('.md'))
    print(f"{slug}: {len(files)} concepts")
    for f in files:
        p = os.path.join(d, f)
        cslug = f[:-3]
        txt = open(p).read()
        m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
        errs = []
        if not m:
            errs.append("no frontmatter")
        else:
            try:
                fm = yaml.safe_load(m.group(1))
                missing = REQ_KEYS - set(fm or {})
                if missing: errs.append(f"missing keys {sorted(missing)}")
                desc = str((fm or {}).get('description', ''))
                if len(desc.split()) > 35: errs.append(f"description {len(desc.split())} words")
                if (fm or {}).get('book') != slug: errs.append(f"book={fm.get('book')} != {slug}")
            except yaml.YAMLError as e:
                errs.append(f"yaml: {str(e).splitlines()[0]}")
        for s in REQ_SECTIONS:
            if s not in txt: errs.append(f"missing '{s}'")
        if '## Connections' in txt: errs.append("has forbidden Connections section")
        if cslug in owned: errs.append("COLLISION vs CATALOG")
        if cslug in seen: errs.append(f"COLLISION in-tranche vs {seen[cslug]}")
        seen[cslug] = slug
        if errs:
            fails += 1
            print(f"  FAIL {f}: {'; '.join(errs)}")
print(f"\n{'GATE FAIL: ' + str(fails) + ' problems' if fails else 'GATE PASS'}")
sys.exit(1 if fails else 0)
