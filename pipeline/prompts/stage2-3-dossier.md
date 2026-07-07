# Stage 2+3+4 — Dossier mode: book WITHOUT source text

For books whose `source:` is null in `sources/manifest.yml`. You build the
companion from **web research + model knowledge** instead of full text. The
user tells you the slug. You are in a worktree on branch `book-<slug>`. Never
push.

## Stage 2 — Research dossier (do this FIRST, write it down)

Build `/home/sanjayg4/living-books/pipeline/work/<slug>/dossier.md` (main
checkout path — pipeline/work/ is gitignored, exists only there):

1. **Verify the real table of contents.** Publisher page, Google Books
   preview, detailed reviews. NEVER invent chapter titles. If the true TOC
   cannot be verified, organize the companion by verified themes instead and
   say so in the book's index.md.
2. **Gather legitimate sources**: author essays/newsletters (e.g. Choudary's
   platform writings for reshuffle), talks and interview transcripts,
   publisher excerpts, long-form reviews (2+ independent ones), academic
   citations. Record each source URL + what it covers.
3. **Grade coverage** per chapter/theme: strong / partial / weak. Note it in
   the dossier.
4. Useful fetch trick for JS-heavy pages: `curl -s https://r.jina.ai/<url>`.

Recency warning: deep-utopia (2024), singularity-is-nearer (2024), reshuffle
(2025) have THIN model-knowledge coverage. For claims about these, prefer the
dossier over memory; if neither supports a claim, leave it out.

## Stage 3 — Write (same outputs as pipeline/prompts/stage3.md, differences below)

Follow `pipeline/prompts/stage3.md` for file formats, voice, study guides,
index, feedback-log — with these overrides:

- Add `source: dossier` to every chapter/guide/concept frontmatter.
- Book `index.md` includes one honest line: *"This companion was built from
  published research about the book (author essays, talks, reviews) and
  general knowledge — not from the full text. Chapters graded weak in
  coverage are marked."*
- Chapters with weak coverage: shorter file + a `> Coverage: partial` note
  rather than confident padding. Never fabricate specific numbers, named
  case studies, or quotes.
- Concepts: use your book's slugs from `pipeline/concept-inventory.yml`
  (status: provisional). If research shows a provisional slug is wrong,
  use the corrected slug in your files and REPORT the rename — do NOT edit
  concept-inventory.yml (merge conflicts; orchestrator reconciles).
- Connection edges: same rules and vocabulary as stage3.md. Ground each edge
  in a dossier source or well-established knowledge of your book.

## Discipline

Same as stage3.md: commit every ~5 files, touch only `docs/books/<slug>/`
(plus the dossier in main-checkout work/), no push, no media, final report
with sources used, coverage grades, renames, 3 strongest edges.
