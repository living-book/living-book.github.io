# Edge-weaving brief (read fully)

You are weaving typed edges between concepts extracted from 31 books across 6 domains.
These edges ARE the product: they are what lets a reader ask one question and see
answers from systems theory, psychology, business, and epistemology at once.

## Inputs (read all three)

1. `pipeline/atlas/CATALOG.md` — all 224 concepts (slug, title, one-liner, tags), grouped by book/domain
2. `pipeline/atlas/EDGES-EXISTING.md` — edges that already exist; do not duplicate
3. Your lens, given in the task prompt — weave only edges that belong to your lens

## Edge vocabulary (exactly these, direction matters: FROM does VERB to TO)

- `extends` — FROM builds on TO, adds scope or mechanism
- `contradicts` — FROM argues against TO
- `instantiates` — FROM is a concrete case of TO
- `formalizes` — FROM gives TO rigorous/measurable form
- `parallels` — same deep structure in a different domain
- `tempers` — FROM limits TO, names conditions where TO fails

## Quality bar (this is what separates insight from noise)

- The `why` sentence must name the SHARED MECHANISM, not the shared vibe.
  Good: "both describe a reinforcing loop whose delay shrinks each cycle, so the
  window for intervention closes before the signal arrives."
  Bad: "both are about feedback and change."
- CROSS-BOOK is required; CROSS-DOMAIN is strongly preferred (≥70% of your edges
  should connect different domains — that is the atlas's purpose).
- contradicts/tempers edges are the most valuable and the rarest — actively hunt
  for genuine tensions (e.g. a book that argues planning works vs one that argues
  it can't). Aim for at least 3-5 of them.
- If you are not sure the connection is real, drop it. 15 strong edges beat 30 weak ones.
- Consult the underlying concept files when unsure what a concept actually claims:
  `docs/atlas/concepts/<book>/<slug>.md` or `docs/books/<book>/concepts/<slug>.md`.

## Output

Write a YAML file at the path given in your task. Format (list of maps, nothing else):

```yaml
- from: <slug>
  verb: <verb>
  to: <slug>
  why: >-
    <one sentence, the shared mechanism, ≤45 words>
```

15-25 edges. Only slugs that appear in CATALOG.md. Final message: count + the 3 edges
you consider the deepest finds (one line each).
