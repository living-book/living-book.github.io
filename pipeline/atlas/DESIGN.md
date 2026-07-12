# Concept Atlas — design note

**Date**: 2026-07-12
**Status**: shipped with the `concept-atlas` branch
**Question answered**: should the Living Books library adopt Google's Open Knowledge
Format (OKF), and what does an intent-driven, cross-domain interface over it look like?

## 1. The OKF verdict

**Yes — and the repo had already adopted it de facto.** The Connected-Books concept
files (`docs/books/<slug>/concepts/*.md`) are OKF-conformant: markdown + YAML
frontmatter, one required `type` field, links as edges, broken links legal. Full
conversion of the library *into* OKF is therefore not a migration, it is a naming:
the `docs/` tree **is** a Knowledge Bundle.

What OKF gives this library:
- **Zero-tooling durability** — concepts are plain markdown; readable in 20 years,
  greppable, git-mergeable, publishable as-is by MkDocs.
- **Incremental growth is legal** — the spec blesses broken links and partial
  coverage, which matches a library that adds books over time.
- **A ready consumer ecosystem** — the OKF viz.html pattern, enrichment agent
  (`--output_format=okf`), and eval harness in ~/okf-knowledge all consume this
  format unchanged.

What OKF deliberately does NOT give (and how the atlas fills it):
- **Typed relations.** OKF links are untyped; the *kind* of connection is what makes
  cross-domain learning work. Solution (kept from the Connected-Books pilot): a fixed
  6-verb vocabulary — `extends, contradicts, instantiates, formalizes, parallels,
  tempers` — carried in `## Connections` sections and `pipeline/atlas/edges.yml`.
  OKF consumers still see plain links; our own consumer sees types. Spec-legal
  (arbitrary keys/prose allowed).
- **Inference.** OKF has no mechanism to *discover* connections. The prior research
  (graphify_vs_okf_comparison.md) already decided the pattern: OKF is the canonical
  destination; an analysis pass (here: LLM edge-weaving agents; later: graphify or
  embeddings) produces inferred edges that are written back.

## 2. Architecture

```
sources (private, gitignored)          417 book conversions, 6 domains
   │  extraction agents (1/book, grounded in source text, 5-8 concepts each)
   ▼
concept files (OKF)                    docs/books/<slug>/concepts/*.md   (published books)
                                       docs/atlas/concepts/<slug>/*.md   (atlas-only books)
   │  edge-weaving agents (thematic lenses over the whole catalog)
   ▼
pipeline/atlas/edges.yml               typed cross-book edges + rationale
   │  scripts/build_atlas.py
   ▼
docs/atlas/atlas.json                  compiled graph (books, concepts, edges)
   ▼
docs/atlas/index.html                  the interface (self-contained, no deps)
```

Concepts for books not yet in the library live under `docs/atlas/concepts/<book>/`;
when a book gets a full companion, its concept dir moves to
`docs/books/<slug>/concepts/` unchanged (same format). `build_atlas.py` reads both.

Runtime cost of "connections built in": zero — everything is precomputed at build
time; the interface is a static page over a static JSON.

## 3. The interface ("express intent, get cross-domain concepts")

- **Intent box** — free-text question, scored client-side against title/tags/
  description/body; results grouped by domain so the cross-domain spread of an
  idea is the first thing you see ("this question spans 4 domains").
- **Map** — force-layout constellation, one color per domain, edges drawn as ink
  routes; selecting a concept lights its routes (dashed = contradicts/tempers).
- **Concept card** — definition / in-the-book / why-it-matters + typed connections,
  cross-domain ones sorted first, each with its rationale sentence.
- **Trails** — one-click walk from any concept that greedily prefers changing
  domain each hop: a 4-hop multidisciplinary reading path with the connecting
  logic spelled out at each step.

## 4. Scale-up path (rest of the 375-book corpus)

The pilot tranche is ~30 books / ~200 concepts chosen for cross-domain gravity.
Scaling is mechanical: same extraction brief per book (~1 agent), re-run weaving
for new concepts (weavers take the compiled catalog, not the books), rebuild.
Practical batch: one domain folder at a time; dedupe titles first
(~25-30 duplicate files in sources). The interface needs no changes until
~1,000 concepts, at which point search should precompute an index and the map
should cluster by domain with expand-on-zoom.

<!-- ponytail: lexical search, no embeddings. Add an embedding index only when
     intent queries visibly miss synonymous concepts. -->
