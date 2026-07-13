---
name: add-book
description: Connected Books pipeline — turn a source book (PDF/markdown in sources/) into a published living-book companion with chapters, study guides, OKF concept layer, media, and cross-book links. Trigger: "add book: <slug>".
---

# Connected Books Pipeline

Turns one book into a published companion. Interface: drop source in `sources/`
(private repo), add a `shelf:` entry to `sources/manifest.yml`, then say
**"add book: <slug>"**.

Copyright rule: `sources/` and `pipeline/work/` are gitignored. Full book text
NEVER enters the public repo — only transformative outputs (summaries, guides,
concepts, media) publish.

## Stages

| # | Stage | Who | Tool |
|---|-------|-----|------|
| 1 | Ingest — clean + chapter-split | script + agent map | `scripts/clean_source.py <slug>` → agent authors `work/<slug>/chapters.yml` from TOC/heading grep → `scripts/split_chapters.py <slug>` |
| 2 | Dossier — source coverage grade | agent | PDF/MD present = pass. Absent = research mode: gather legit sources (publisher excerpts, author essays/talks, reviews), grade coverage. Below bar → chapters-only, no concept extraction |
| 3 | Write — chapter summaries + study guides | agent | One session per book (worktree for parallel batches). Read `work/<slug>/chapters/*.md`, write `docs/books/<slug>/chapters/` + `study-guides/` |
| 4 | Connect — OKF concept layer | agent | Extract 5-10 concepts per book → `docs/books/<slug>/concepts/*.md` with OKF frontmatter (`type: Concept`). Cross-book links against the shared concept inventory (pre-agreed slugs; broken links legal per OKF). Every cross-book edge: typed relationship (extends/contradicts/instantiates/formalizes) + one-sentence justification citing chapters |
| 5 | Media — infographics + audio | scripts | Existing `gen_infographics.py`, `gen_audio.sh`, `embed_media.py`. Serial (GPU/quota shared) — batch after text phase across books |
| 6 | Publish | script + CI | `build_corpus.py` (includes concepts), graph data, mkdocs nav, push → Pages deploy |

## Stage 1 details (proven on fifth-discipline)

1. `python3 pipeline/scripts/clean_source.py <slug>` — strips page stamps,
   flattens fake layout tables. New artifact patterns → extend rules in script.
2. Find chapter boundaries: chapter starts often = standalone number line then
   caps title (`grep -n -E "^[12]?[0-9]$"` + inspect). Endnotes re-list chapter
   titles — don't confuse with body. Verify against the book's real TOC.
3. Author `work/<slug>/chapters.yml` (see fifth-discipline example: n, slug,
   title, start_line). Attach part-title pages to their first chapter.
4. `python3 pipeline/scripts/split_chapters.py <slug>` — sanity-check word
   counts against known chapter lengths.

## Quality gates

- **Dossier gate**: weak sources → book ships chapters-only.
- **Connection gate**: user rates sample cross-book connections after pilot
  wave before scaling. Generic topic-overlap edges = fail; typed, justified,
  chapter-cited edges = pass.
