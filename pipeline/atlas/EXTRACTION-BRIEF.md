# Concept Atlas — extraction brief (read fully before extracting)

You are extracting the load-bearing concepts from ONE book into OKF concept files.
These join a shared cross-book namespace used to connect ideas across domains.

## Output

Write 5–8 concept files (one per concept) into the output directory given in your task.
File name: `<concept-slug>.md` (kebab-case, short, timeless — name the IDEA, not the book's chapter title).

## File format (exactly this shape)

```markdown
---
type: Concept
title: <Concept Title>
description: <one sentence, ≤30 words, self-contained — used in search/index>
book: <book-slug given in your task>
chapters: [<chapter numbers where this concept lives, if identifiable>]
tags: [<3-5 lowercase tags>]
created: 2026-07-12
---

# <Concept Title>

## Definition

<2-5 sentences. The idea in plain words, in OUR words. May include ONE short
quote (<25 words) from the book if it is genuinely the best formulation.>

## In the Book

<Where and how the book develops it: the argument, the central example/case,
the mechanism. 1-2 paragraphs. Must be grounded in the actual text you read —
name the specific examples the book uses.>

## Why It Matters

<1 paragraph: what this concept lets you see or do that you couldn't before.
Write it domain-neutral where honest — this is what makes cross-domain
connection possible.>
```

Do NOT write a `## Connections` section — typed cross-book edges are woven in a
separate pass by agents that can see the whole catalog.

## Grounding rules

- READ the source markdown before writing. It is large: skim strategically —
  table of contents / first 200 lines, then openings of the chapters that carry
  the core ideas. 8–15 targeted Reads, not the whole file.
- Every "In the Book" section must cite examples that actually appear in the text.
  You know these famous books from training — that is NOT grounding. Verify against the file.
- Conversion artifacts (page headers, garbled OCR) are normal; read around them.

## Choosing the 5–8 concepts

- Pick the concepts the book would be cited FOR — its exportable ideas,
  not its chapter list. Prefer mechanisms over slogans.
- Prefer concepts likely to connect across domains (feedback, incentives,
  constraints, learning, emergence, measurement, coordination...) but do not
  force it; a book's idiosyncratic core idea belongs here too.

## Existing namespace (avoid slug collisions; do not re-own these)

The full list of owned slugs is `pipeline/atlas/CATALOG.md` (one line per concept,
grouped by book) — grep it for your candidate slugs before writing.

If your book's core concept is already owned (e.g. another systems book and
`feedback-loops`), extract the book's DISTINCT angle under a distinct slug
(e.g. `via-negativa`, not `antifragility-feedback`). The edge-weaving pass will
connect them.

## Final message format

Return (as plain text, no file dumps): the book slug, then one line per concept:
`<slug> | <title> | <one-line description>`. Note any concept where source
grounding was weak (conversion too garbled) — do not fabricate grounding.
