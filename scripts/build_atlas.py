#!/usr/bin/env python3
"""Compile OKF concept files + woven edges into docs/atlas/atlas.json.

Sources:
  docs/books/<book>/concepts/*.md   (published books)
  docs/atlas/concepts/<book>/*.md   (atlas-only books, not yet in library)
  ## Connections sections inside concept files (hand-authored edges)
  pipeline/atlas/edges.yml          (woven edges from the synthesis pass)

Run: python3 scripts/build_atlas.py
"""
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent

# slug -> (title, author, domain, status). status: published = has a book page.
BOOKS = {
    "fifth-discipline": ("The Fifth Discipline", "Peter Senge", "Systems Thinking & Philosophy", "published"),
    "antifragile": ("Antifragile", "Nassim Nicholas Taleb", "Systems Thinking & Philosophy", "atlas"),
    "master-and-emissary": ("The Master and His Emissary", "Iain McGilchrist", "Systems Thinking & Philosophy", "atlas"),
    "general-systems-thinking": ("An Introduction to General Systems Thinking", "Gerald Weinberg", "Systems Thinking & Philosophy", "atlas"),
    "web-of-life": ("The Web of Life", "Fritjof Capra", "Systems Thinking & Philosophy", "atlas"),
    "structure-of-scientific-revolutions": ("The Structure of Scientific Revolutions", "Thomas Kuhn", "Systems Thinking & Philosophy", "published"),
    "scientific-research-programmes": ("The Methodology of Scientific Research Programmes", "Imre Lakatos", "Systems Thinking & Philosophy", "published"),
    "superintelligence": ("Superintelligence", "Nick Bostrom", "Technology & Data", "published"),
    "beginning-of-infinity": ("The Beginning of Infinity", "David Deutsch", "Technology & Data", "published"),
    "master-algorithm": ("The Master Algorithm", "Pedro Domingos", "Technology & Data", "atlas"),
    "second-machine-age": ("The Second Machine Age", "Brynjolfsson & McAfee", "Technology & Data", "atlas"),
    "model-thinker": ("The Model Thinker", "Scott E. Page", "Technology & Data", "atlas"),
    "how-to-measure-anything": ("How to Measure Anything", "Douglas Hubbard", "Technology & Data", "atlas"),
    "innovators-dilemma": ("The Innovator's Dilemma", "Clayton Christensen", "Business & Management", "atlas"),
    "business-model-generation": ("Business Model Generation", "Osterwalder & Pigneur", "Business & Management", "atlas"),
    "theory-of-constraints": ("Theory of Constraints", "Eliyahu Goldratt", "Business & Management", "atlas"),
    "end-of-competitive-advantage": ("The End of Competitive Advantage", "Rita Gunther McGrath", "Business & Management", "atlas"),
    "measure-what-matters": ("Measure What Matters", "John Doerr", "Business & Management", "atlas"),
    "toyota-kata": ("Toyota Kata", "Mike Rother", "Agile & Software Delivery", "atlas"),
    "kanban": ("Kanban", "David J. Anderson", "Agile & Software Delivery", "atlas"),
    "project-to-product": ("Project to Product", "Mik Kersten", "Agile & Software Delivery", "atlas"),
    "user-story-mapping": ("User Story Mapping", "Jeff Patton", "Agile & Software Delivery", "atlas"),
    "leaders-eat-last": ("Leaders Eat Last", "Simon Sinek", "Leadership & Coaching", "atlas"),
    "creativity-inc": ("Creativity, Inc.", "Ed Catmull", "Leadership & Coaching", "atlas"),
    "principles": ("Principles: Life and Work", "Ray Dalio", "Leadership & Coaching", "atlas"),
    "progress-principle": ("The Progress Principle", "Amabile & Kramer", "Leadership & Coaching", "atlas"),
    "thinking-fast-and-slow": ("Thinking, Fast and Slow", "Daniel Kahneman", "Psychology & Self-Development", "atlas"),
    "atomic-habits": ("Atomic Habits", "James Clear", "Psychology & Self-Development", "atlas"),
    "make-it-stick": ("Make It Stick", "Brown, Roediger & McDaniel", "Psychology & Self-Development", "atlas"),
    "nudge": ("Nudge", "Thaler & Sunstein", "Psychology & Self-Development", "atlas"),
    "laws-of-human-nature": ("The Laws of Human Nature", "Robert Greene", "Psychology & Self-Development", "published"),
    # tranche 2 (2026-07-13)
    "deep-simplicity": ("Deep Simplicity", "John Gribbin", "Systems Thinking & Philosophy", "atlas"),
    "simple-rules": ("Simple Rules", "Sull & Eisenhardt", "Systems Thinking & Philosophy", "atlas"),
    "art-of-problem-solving": ("The Art of Problem Solving", "Russell L. Ackoff", "Systems Thinking & Philosophy", "atlas"),
    "on-the-shortness-of-life": ("On the Shortness of Life", "Seneca", "Systems Thinking & Philosophy", "atlas"),
    "ai-superpowers": ("AI Superpowers", "Kai-Fu Lee", "Technology & Data", "atlas"),
    "the-inevitable": ("The Inevitable", "Kevin Kelly", "Technology & Data", "atlas"),
    "fabric-of-reality": ("The Fabric of Reality", "David Deutsch", "Technology & Data", "atlas"),
    "field-guide-to-lies": ("A Field Guide to Lies and Statistics", "Daniel Levitin", "Technology & Data", "atlas"),
    "design-of-everyday-things": ("The Design of Everyday Things", "Don Norman", "Business & Management", "atlas"),
    "inspired": ("INSPIRED", "Marty Cagan", "Business & Management", "atlas"),
    "running-lean": ("Running Lean", "Ash Maurya", "Business & Management", "atlas"),
    "four-steps-to-the-epiphany": ("The Four Steps to the Epiphany", "Steve Blank", "Business & Management", "atlas"),
    "zone-to-win": ("Zone to Win", "Geoffrey Moore", "Business & Management", "atlas"),
    "jobs-to-be-done": ("Jobs to Be Done", "Wunker, Wattman & Farber", "Business & Management", "atlas"),
    "intelligent-investor": ("The Intelligent Investor", "Benjamin Graham", "Business & Management", "atlas"),
    "the-advantage": ("The Advantage", "Patrick Lencioni", "Business & Management", "atlas"),
    "product-development-flow": ("The Principles of Product Development Flow", "Donald G. Reinertsen", "Agile & Software Delivery", "atlas"),
    "toyota-production-system": ("Toyota Production System", "Taiichi Ohno", "Agile & Software Delivery", "atlas"),
    "lean-software-development": ("Lean Software Development", "Mary & Tom Poppendieck", "Agile & Software Delivery", "atlas"),
    "making-work-visible": ("Making Work Visible", "Dominica DeGrandis", "Agile & Software Delivery", "atlas"),
    "essential-drucker": ("The Essential Drucker", "Peter Drucker", "Leadership & Coaching", "atlas"),
    "five-dysfunctions-of-a-team": ("The Five Dysfunctions of a Team", "Patrick Lencioni", "Leadership & Coaching", "atlas"),
    "act-like-a-leader": ("Act Like a Leader, Think Like a Leader", "Herminia Ibarra", "Leadership & Coaching", "atlas"),
    "why-great-leaders-dont-take-yes": ("Why Great Leaders Don't Take Yes for an Answer", "Michael Roberto", "Leadership & Coaching", "atlas"),
    "power-of-habit": ("The Power of Habit", "Charles Duhigg", "Psychology & Self-Development", "atlas"),
    "mastery": ("Mastery", "Robert Greene", "Psychology & Self-Development", "atlas"),
    "checklist-manifesto": ("The Checklist Manifesto", "Atul Gawande", "Psychology & Self-Development", "atlas"),
    "six-thinking-hats": ("Six Thinking Hats", "Edward de Bono", "Psychology & Self-Development", "atlas"),
    "art-of-learning": ("The Art of Learning", "Josh Waitzkin", "Psychology & Self-Development", "atlas"),
    "digital-minimalism": ("Digital Minimalism", "Cal Newport", "Psychology & Self-Development", "atlas"),
}

EDGE_VERBS = {"extends", "contradicts", "instantiates", "formalizes", "parallels", "tempers"}

FM_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
# - **verb** [title](path) — rationale
CONN_RE = re.compile(r"^-\s+\*\*(\w+)\*\*\s+\[([^\]]+)\]\(([^)]+)\)\s*[—–-]?\s*(.*)$")


def parse_concept(path: Path, book: str):
    text = path.read_text(encoding="utf-8")
    m = FM_RE.match(text)
    if not m:
        print(f"  SKIP (no frontmatter): {path}", file=sys.stderr)
        return None, []
    fm = yaml.safe_load(m.group(1))
    body = text[m.end():]

    sections = {}
    cur = None
    conn_lines = []
    for line in body.splitlines():
        h = re.match(r"^##\s+(.*)$", line)
        if h:
            cur = h.group(1).strip().lower()
            continue
        if cur == "connections":
            conn_lines.append(line)
        elif cur:
            sections.setdefault(cur, []).append(line)

    slug = path.stem
    concept = {
        "id": slug,
        "title": fm.get("title", slug),
        "description": fm.get("description", ""),
        "book": book,
        "chapters": fm.get("chapters", []),
        "tags": fm.get("tags", []),
        "definition": "\n".join(sections.get("definition", [])).strip(),
        "inBook": "\n".join(sections.get("in the book", [])).strip(),
        "whyItMatters": "\n".join(sections.get("why it matters", [])).strip(),
    }

    edges = []
    for line in conn_lines:
        cm = CONN_RE.match(line.strip())
        if not cm:
            continue
        verb, _title, target_path, why = cm.groups()
        if verb not in EDGE_VERBS:
            print(f"  WARN unknown verb '{verb}' in {path}", file=sys.stderr)
            continue
        target = Path(target_path).stem
        edges.append({"from": slug, "verb": verb, "to": target, "why": why.strip(), "source": "authored"})
    return concept, edges


def main():
    concepts, edges = [], []
    seen = {}

    def ingest(concept_dir: Path, book: str):
        for f in sorted(concept_dir.glob("*.md")):
            if f.name in ("index.md", "log.md"):
                continue
            c, e = parse_concept(f, book)
            if not c:
                continue
            if c["id"] in seen:
                print(f"  WARN duplicate slug {c['id']} ({book} vs {seen[c['id']]}) — keeping first", file=sys.stderr)
                continue
            seen[c["id"]] = book
            concepts.append(c)
            edges.extend(e)

    for slug in BOOKS:
        for base in (ROOT / "docs/books" / slug / "concepts", ROOT / "docs/atlas/concepts" / slug):
            if base.is_dir():
                ingest(base, slug)

    for woven in sorted((ROOT / "pipeline/atlas").glob("edges*.yml")) + \
                 sorted((ROOT / "pipeline/atlas/edges").glob("*.yml") if (ROOT / "pipeline/atlas/edges").is_dir() else []):
        for e in yaml.safe_load(woven.read_text()) or []:
            if e["verb"] not in EDGE_VERBS:
                print(f"  WARN unknown verb in {woven.name}: {e}", file=sys.stderr)
                continue
            e.setdefault("source", "woven")
            edges.append(e)

    # drop edges pointing at unknown concepts (OKF: broken links legal, but the
    # interface only renders resolvable ones), dedupe on (from, verb, to)
    ids = {c["id"] for c in concepts}
    uniq = {}
    dropped = 0
    for e in edges:
        if e["from"] not in ids or e["to"] not in ids:
            dropped += 1
            continue
        # parallels is symmetric — collapse A->B / B->A into one edge
        key = (frozenset((e["from"], e["to"])), e["verb"]) if e["verb"] == "parallels" \
              else (e["from"], e["verb"], e["to"])
        uniq.setdefault(key, e)
    edges = list(uniq.values())

    books = [
        {"slug": s, "title": t, "author": a, "domain": d, "status": st,
         "concepts": [c["id"] for c in concepts if c["book"] == s]}
        for s, (t, a, d, st) in BOOKS.items()
    ]
    books = [b for b in books if b["concepts"]]

    out = ROOT / "docs/atlas/atlas.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"books": books, "concepts": concepts, "edges": edges},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"atlas.json: {len(books)} books, {len(concepts)} concepts, {len(edges)} edges "
          f"({dropped} unresolvable edges dropped)")


if __name__ == "__main__":
    main()
