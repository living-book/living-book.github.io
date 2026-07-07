# Stage 3+4 — Write & Connect one book

You are running the Connected Books pipeline (see `pipeline/SKILL.md`) for ONE
book. The user tells you the slug (e.g. `superintelligence`). You are in a git
worktree on branch `book-<slug>`. Work only on this branch. Never push.

## Inputs (read these first)

1. `sources/manifest.yml` entry for your slug — title/author/year — read it at
   `/home/sanjayg4/living-books/sources/manifest.yml` (main checkout; sources/
   and pipeline/work/ are gitignored so they exist ONLY in the main checkout).
2. Chapter map: `/home/sanjayg4/living-books/pipeline/work/<slug>/chapters.yml`
3. Chapter texts: `/home/sanjayg4/living-books/pipeline/work/<slug>/chapters/*.md`
   — full book text. Expect residual OCR noise (broken caps like "SP IRIT",
   stray hyphens); read through it, never quote noise verbatim.
4. Concept namespace: `pipeline/concept-inventory.yml` (in the worktree).
5. Voice reference: `docs/books/beginning-of-infinity/chapters/ch-01-*.md` and
   one study guide next to it. Match that quality bar: analytical, dense,
   specific episodes from the text, zero filler. Section headings may adapt to
   the material — the study-guide section set is fixed, chapter sections are not.

## Outputs (all under `docs/books/<slug>/` in the worktree)

Skip front-matter (n=0) and back-matter (n=99) work files. Very short chapters
(<500 words) still get files, proportionally short.

**`chapters/ch-NN-<short-slug>.md`** — one per real chapter:

```markdown
---
title: "Chapter N: <Title>"
chapter: N
book: "<Book Title>"
author: "<Author>"
created: 2026-07-07
---

# Chapter N — <Title>

## Core Thesis
...4-8 sections total, adapted to the chapter (e.g. The Problem It Solves /
Key Episode / The Mechanism / The Shift / Critiques & Rivals). 400-800 words.
Cite concrete examples, numbers, named cases FROM THE TEXT...
```

No `<audio>` tags, no image embeds — stage 5 injects media later.

**`study-guides/ch-NN-<short-slug>-study-guide.md`** — one per chapter, fixed
sections: Core Idea / Key Terms / Case Summary / Application Checklist /
Self-Test (same shape as the Beginning of Infinity guides).

**`concepts/<concept-slug>.md`** — exactly the slugs listed for your book in
`concept-inventory.yml` (rename only if the text plainly demands it; note any
rename in your final report):

```markdown
---
type: Concept
title: <Name>
description: <one sentence>
book: <slug>
chapters: [7, 8]
tags: [<2-4 tags>]
created: 2026-07-07
---

# <Name>

## Definition
Tight, faithful to the author's own formulation.

## In the Book
Where it appears, how the argument builds, chapter references.

## Why It Matters
Stakes, in and beyond the book.

## Connections
- **<edge>** [<Target Name>](/books/<other-book>/concepts/<target-slug>.md) — one sentence WHY, citing your book's chapter.
```

Connection rules — this is the product, treat as the hardest part:
- Edge vocabulary: extends | contradicts | instantiates | formalizes | parallels | tempers (definitions in concept-inventory.yml).
- Target slugs MUST come from the inventory namespace (any book, including provisional ones). Links to not-yet-written files are fine.
- Every edge needs a one-sentence justification grounded in YOUR book's text. "Both discuss X" = failure. A reader should think "hadn't seen that" — verify seed_edges against the text, keep only what holds, find better ones.
- 2-5 cross-book edges per concept. Within-book edges also welcome.

**`index.md`** — book landing page: title, author, one-paragraph overview,
chapter table (linked), concept list (linked, one-line descriptions). Mirror an
existing book's index for tone, minus media references.

**`feedback-log.md`** — stub: `# Feedback Log\n\nNo feedback yet.`

## Discipline

- Commit every ~5 chapters: `git add docs/books/<slug> && git commit -m "..."`.
- Do NOT touch mkdocs.yml, build_corpus.py, other books, or anything outside `docs/books/<slug>/`.
- Do NOT push. Do NOT run media scripts.
- Finish with a report: files written, word counts, concept renames, your 3 strongest cross-book edges.
