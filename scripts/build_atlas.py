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
    # tranche 3 (2026-07-13)
    "thinking-for-a-change": ("Thinking for a Change", "Lisa Scheinkopf", "Systems Thinking & Philosophy", "atlas"),
    "simplexity": ("Simplexity", "Jeffrey Kluger", "Systems Thinking & Philosophy", "atlas"),
    "whats-it-all-about": ("What's It All About?", "Julian Baggini", "Systems Thinking & Philosophy", "atlas"),
    "what-to-do-when-machines-do-everything": ("What to Do When Machines Do Everything", "Frank, Roehrig & Pring", "Technology & Data", "atlas"),
    "perfect-software": ("Perfect Software", "Gerald Weinberg", "Technology & Data", "atlas"),
    "coders": ("Coders", "Clive Thompson", "Technology & Data", "atlas"),
    "reinventing-organizations": ("Reinventing Organizations", "Frederic Laloux", "Business & Management", "atlas"),
    "reframing-organizations": ("Reframing Organizations", "Bolman & Deal", "Business & Management", "atlas"),
    "sprint": ("Sprint", "Jake Knapp", "Business & Management", "atlas"),
    "lean-product-playbook": ("The Lean Product Playbook", "Dan Olsen", "Business & Management", "atlas"),
    "secrets-of-consulting": ("The Secrets of Consulting", "Gerald Weinberg", "Business & Management", "atlas"),
    "are-your-lights-on": ("Are Your Lights On?", "Gause & Weinberg", "Business & Management", "atlas"),
    "tao-of-charlie-munger": ("Tao of Charlie Munger", "David Clark", "Business & Management", "atlas"),
    "the-ultimate-question": ("The Ultimate Question 2.0", "Fred Reichheld", "Business & Management", "atlas"),
    "strategy-beyond-the-hockey-stick": ("Strategy Beyond the Hockey Stick", "Bradley, Hirt & Smit", "Business & Management", "atlas"),
    "coaching-agile-teams": ("Coaching Agile Teams", "Lyssa Adkins", "Agile & Software Delivery", "atlas"),
    "specification-by-example": ("Specification by Example", "Gojko Adzic", "Agile & Software Delivery", "atlas"),
    "personal-kanban": ("Personal Kanban", "Benson & DeMaria Barry", "Agile & Software Delivery", "atlas"),
    "value-stream-mapping": ("Value Stream Mapping", "Martin & Osterling", "Agile & Software Delivery", "atlas"),
    "learning-agile": ("Learning Agile", "Stellman & Greene", "Agile & Software Delivery", "atlas"),
    "leadership-challenge": ("The Leadership Challenge", "Kouzes & Posner", "Leadership & Coaching", "atlas"),
    "simple-habits-for-complex-times": ("Simple Habits for Complex Times", "Berger & Johnston", "Leadership & Coaching", "atlas"),
    "secret-language-of-leadership": ("The Secret Language of Leadership", "Stephen Denning", "Leadership & Coaching", "atlas"),
    "gamestorming": ("Gamestorming", "Gray, Brown & Macanufo", "Leadership & Coaching", "atlas"),
    "clean-language": ("Clean Language", "Sullivan & Rees", "Leadership & Coaching", "atlas"),
    "pragmatic-thinking-and-learning": ("Pragmatic Thinking and Learning", "Andy Hunt", "Psychology & Self-Development", "atlas"),
    "when-perfect-timing": ("When", "Daniel Pink", "Psychology & Self-Development", "atlas"),
    "decision-quality": ("Decision Quality", "Spetzler, Winter & Meyer", "Psychology & Self-Development", "atlas"),
    "daring-greatly": ("Daring Greatly", "Brené Brown", "Psychology & Self-Development", "atlas"),
    "the-antidote": ("The Antidote", "Oliver Burkeman", "Psychology & Self-Development", "atlas"),
    # Tranche 4
    "team-topologies": ("Team Topologies", "Skelton & Pais", "Agile & Software Delivery", "atlas"),
    "beyond-budgeting": ("Beyond Budgeting", "Hope & Fraser", "Agile & Software Delivery", "atlas"),
    "lean-machine": ("The Lean Machine", "Dantar Oosterwal", "Agile & Software Delivery", "atlas"),
    "agile-product-management-scrum": ("Agile Product Management with Scrum", "Roman Pichler", "Agile & Software Delivery", "atlas"),
    "fifty-quick-ideas-user-stories": ("Fifty Quick Ideas to Improve Your User Stories", "Adzic & Evans", "Agile & Software Delivery", "atlas"),
    "competing-against-luck": ("Competing Against Luck", "Clayton Christensen et al.", "Business & Management", "atlas"),
    "rework": ("Rework", "Fried & Heinemeier Hansson", "Business & Management", "atlas"),
    "idea-factory": ("The Idea Factory", "Jon Gertner", "Business & Management", "atlas"),
    "flawless-consulting": ("Flawless Consulting", "Peter Block", "Business & Management", "atlas"),
    "our-iceberg-is-melting": ("Our Iceberg Is Melting", "Kotter & Rathgeber", "Business & Management", "atlas"),
    "organizational-traps": ("Organizational Traps", "Chris Argyris", "Business & Management", "atlas"),
    "communities-of-practice": ("Cultivating Communities of Practice", "Wenger, McDermott & Snyder", "Business & Management", "atlas"),
    "berkshire-letters": ("Berkshire Hathaway Letters to Shareholders", "Warren Buffett", "Business & Management", "atlas"),
    "skilled-facilitator": ("The Skilled Facilitator", "Roger Schwarz", "Leadership & Coaching", "atlas"),
    "open-space-technology": ("Open Space Technology", "Harrison Owen", "Leadership & Coaching", "atlas"),
    "coaching-questions": ("Coaching Questions", "Tony Stoltzfus", "Leadership & Coaching", "atlas"),
    "motivational-interviewing": ("Building Motivational Interviewing Skills", "David Rosengren", "Leadership & Coaching", "atlas"),
    "smart-trust": ("Smart Trust", "Covey & Link", "Leadership & Coaching", "atlas"),
    "choices-values-frames": ("Choices, Values, and Frames", "Kahneman & Tversky (eds.)", "Psychology & Self-Development", "atlas"),
    "punished-by-rewards": ("Punished by Rewards", "Alfie Kohn", "Psychology & Self-Development", "atlas"),
    "how-learning-works": ("How Learning Works", "Susan Ambrose et al.", "Psychology & Self-Development", "atlas"),
    "talent-code": ("The Talent Code", "Daniel Coyle", "Psychology & Self-Development", "atlas"),
    "david-and-goliath": ("David and Goliath", "Malcolm Gladwell", "Psychology & Self-Development", "atlas"),
    "whole-new-mind": ("A Whole New Mind", "Daniel Pink", "Psychology & Self-Development", "atlas"),
    "nature-fix": ("The Nature Fix", "Florence Williams", "Psychology & Self-Development", "atlas"),
    "architecture-of-happiness": ("The Architecture of Happiness", "Alain de Botton", "Systems Thinking & Philosophy", "atlas"),
    "mind-design-ii": ("Mind Design II", "John Haugeland (ed.)", "Systems Thinking & Philosophy", "atlas"),
    "deep-learning": ("Deep Learning", "Goodfellow, Bengio & Courville", "Technology & Data", "atlas"),
    "software-architecture-in-practice": ("Software Architecture in Practice", "Bass, Clements & Kazman", "Technology & Data", "atlas"),
    "seven-languages-seven-weeks": ("Seven Languages in Seven Weeks", "Bruce Tate", "Technology & Data", "atlas"),
    # Tranche 5 (user triage: Tech + Systems first)
    "ai-guide-to-intelligent-systems": ("Artificial Intelligence: A Guide to Intelligent Systems", "Michael Negnevitsky", "Technology & Data", "atlas"),
    "intro-to-management-science": ("An Introduction to Management Science", "Anderson, Sweeney & Williams", "Technology & Data", "atlas"),
    "logic-and-discrete-mathematics": ("Logic and Discrete Mathematics", "Conradie & Goranko", "Technology & Data", "atlas"),
    "mathematics-for-economics-and-business": ("Mathematics for Economics and Business", "Ian Jacques", "Technology & Data", "atlas"),
    "reference-manual-scientific-evidence": ("Reference Manual on Scientific Evidence", "Federal Judicial Center", "Technology & Data", "atlas"),
    "math-hacker": ("The Math-Hacker Book", "Paul Carson", "Technology & Data", "atlas"),
    "mathematical-sciences-2025": ("The Mathematical Sciences in 2025", "National Research Council", "Technology & Data", "atlas"),
    "conscious-language": ("Conscious Language: The Logos of Now", "Robert Tennyson Stevens", "Systems Thinking & Philosophy", "atlas"),
    "direct-truth": ("Direct Truth", "Kapil Gupta", "Systems Thinking & Philosophy", "atlas"),
    "ethics-of-precaution": ("Ethics of Precaution: Individual and Systemic Risk", "Joseph Norman & Nassim Taleb", "Systems Thinking & Philosophy", "atlas"),
    "yoga-of-time-travel": ("The Yoga of Time Travel", "Fred Alan Wolf", "Systems Thinking & Philosophy", "atlas"),
    "ultimate-why-question": ("The Ultimate Why Question", "John F. Wippel (ed.)", "Systems Thinking & Philosophy", "atlas"),
    "strategic-thinking-for-leaders": ("Strategic Thinking for Leaders", "Stephen Haines", "Systems Thinking & Philosophy", "atlas"),
    "systems-thinking-managing-chaos": ("Systems Thinking: Managing Chaos and Complexity", "Jamshid Gharajedaghi", "Systems Thinking & Philosophy", "atlas"),
    "agile-metrics-in-action": ("Agile Metrics in Action", "Christopher W. H. Davis", "Agile & Software Delivery", "atlas"),
    "kanban-change-leadership": ("Kanban Change Leadership", "Klaus Leopold & Siegfried Kaltenecker", "Agile & Software Delivery", "atlas"),
    "liftoff": ("Liftoff: Start and Sustain Successful Agile Teams", "Diana Larsen & Ainsley Nies", "Agile & Software Delivery", "atlas"),
    "scrum-mastery": ("Scrum Mastery: From Good to Great Servant-Leadership", "Geoff Watts", "Agile & Software Delivery", "atlas"),
    "lean-from-the-trenches": ("Lean from the Trenches", "Henrik Kniberg", "Agile & Software Delivery", "atlas"),
    "phoenix-project-devops": ("The Phoenix Project (excerpt)", "Gene Kim, Kevin Behr & George Spafford", "Agile & Software Delivery", "atlas"),
    "great-big-agile": ("Great Big Agile: An OS for Agile Leaders", "Jeff Dalton", "Agile & Software Delivery", "atlas"),
    "making-sense-of-agile": ("Making Sense of Agile Project Management", "Charles G. Cobb", "Agile & Software Delivery", "atlas"),
    "agile-pm-with-scrum": ("Agile Project Management with Scrum", "Ken Schwaber", "Agile & Software Delivery", "atlas"),
    "agile-pm-with-kanban": ("Agile Project Management with Kanban", "Eric Brechner", "Agile & Software Delivery", "atlas"),
    "bdd-in-action": ("BDD in Action", "John Ferguson Smart", "Agile & Software Delivery", "atlas"),
    "disciplined-agile-delivery": ("Disciplined Agile Delivery", "Scott Ambler & Mark Lines", "Agile & Software Delivery", "atlas"),
    "agile-lean-program-management": ("Agile and Lean Program Management", "Johanna Rothman", "Agile & Software Delivery", "atlas"),
    "agility-across-time-and-space": ("Agility Across Time and Space", "Šmite, Moe & Ågerfalk (eds.)", "Agile & Software Delivery", "atlas"),
    "building-the-agile-enterprise": ("Building the Agile Enterprise", "Fred A. Cummins", "Agile & Software Delivery", "atlas"),
    "lean-architecture": ("Lean Architecture for Agile Software Development", "James Coplien & Gertrud Bjørnvig", "Agile & Software Delivery", "atlas"),
    "lean-six-sigma-a3": ("Lean Six Sigma A3 Thinking Workbook", "(workbook)", "Agile & Software Delivery", "atlas"),
    "performance-management-agile-orgs": ("Performance Management for Agile Organizations", "Tim Baker", "Agile & Software Delivery", "atlas"),
    "tamed-agility": ("Tamed Agility: Pragmatic Contracting and Collaboration", "Book, Gruhn & Striemer", "Agile & Software Delivery", "atlas"),
    "agility-mindset": ("The Agility Mindset", "Fiona Cannon", "Agile & Software Delivery", "atlas"),
    "scrumban-revolution": ("The Scrumban [R]Evolution", "Ajay Reddy", "Agile & Software Delivery", "atlas"),
    "less-org-design": ("Org Design & Large-Scale Scrum (LeSS) [slides]", "Craig Larman", "Agile & Software Delivery", "atlas"),
    "scrum-guide": ("The 2020 Scrum Guide", "Ken Schwaber & Jeff Sutherland", "Agile & Software Delivery", "atlas"),
    "kanban-guide": ("The Official Kanban Guide", "Kanban University", "Agile & Software Delivery", "atlas"),
    "evidence-based-management-guide": ("The Evidence-Based Management Guide", "Scrum.org", "Agile & Software Delivery", "atlas"),
    "collaboration-at-scale": ("Collaboration at Scale", "Scrum.org / Age of Product", "Agile & Software Delivery", "atlas"),
    "adaptive-governance": ("Scaling Agile Through Adaptive Governance", "Sanjiv Augustine", "Agile & Software Delivery", "atlas"),
    "agile-leadership-kata": ("The Agile Leadership Kata", "(article)", "Agile & Software Delivery", "atlas"),
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
