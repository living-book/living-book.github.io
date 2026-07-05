# Living Books — Spec v2

**Date**: 2026-07-05
**Status**: Active — supersedes the May 25 "Learning From Books Phase 1" spec
**Site**: https://sanjaygupta-professional.github.io/living-books/
**Repo**: https://github.com/sanjaygupta-professional/living-books

---

## 1. What this is

Book companions that improve with reader feedback. Each book gets a full study companion — chapter summaries, study guides, infographics, audio — produced by an **owned, fully scriptable AI pipeline** and refined by what readers send back.

The v1 spec (May 25) designed this around NotebookLM as the generation engine, with manual work first and automation later. Two things changed:

1. **Ambition**: this is a product pattern for many books, not a one-off companion — so the pipeline is the core artifact, agent-driven from day one.
2. **Engine**: NotebookLM browser automation proved fragile (source upload broken, unfixed). Every generation step now uses tools we own and can script.

## 2. What already shipped (Phase A — done)

- Public repo + MkDocs Material site, live on GitHub Pages
- Seed book: *The Laws of Human Nature* — 18 chapters, 18 study guides, Law 01 infographics
- Feedback intake via plus-addressed email
- Deploy: `mkdocs gh-deploy` from local clone (CI deferred — token lacks `workflow` scope)

## 3. The owned pipeline

Book in → companion out. Five stages, each independently scriptable, so a Claude Code agent can run the whole chain or any single stage.

| Stage | Produces | Tool | Proven? |
|---|---|---|---|
| 1. Ingest | Per-chapter markdown (10-section template) | Claude agents (parallel, ~6 chapters/agent) | ✅ Laws (18 chapters) |
| 2. Study guides | One study guide per chapter | Claude agents | ✅ Laws (18 guides) |
| 3. Infographics | 2 PNGs per chapter (START = concept map, END = takeaways) + cover | Nano Banana (`genimage.py`) | ✅ Law 01 |
| 4. Audio | Per-chapter overview, ~90s, user's cloned voice | Chatterbox (`~/chatterbox/./voice`) — script written by Claude, synthesized locally | ✅ pipeline proven on dba-kb explainer |
| 5. Assemble | Book folder in `docs/books/<slug>/`, index row, strict build, deploy | Bash + mkdocs | ✅ Laws migration |

Design rule: **no stage may depend on browser automation of a third-party UI.** NotebookLM remains available as an optional manual step per book (Deep Dive podcast is genuinely good) — linked, never automated, never blocking.

### Pipeline invocation

No orchestrator daemon. The pipeline is a **runbook** (`PIPELINE.md`, to be written in Phase B) executed by a Claude Code session, with deterministic parts as scripts. A "run" = "add book X" or "backfill stage 3 for book Y".

<!-- ponytail: runbook + scripts, not a framework. Build an orchestrator only when runs exceed ~1/week. -->

### Chapter file template (unchanged from Laws seed)

10 H2 sections: Core Concept · Human Weakness/Problem · Case Study · Transformation · Practical Guide · Modern Application · Warning Signs · Key Quotes · Reflection Questions · Connections. Adapt section names to the book's genre; keep the count and intent.

## 4. The loop

Three signals, all human-readable, no analytics:

| Signal | Channel | Route |
|---|---|---|
| Explicit feedback | `sanjaygupta.professional+living-books@gmail.com`, subject `[<book-slug>]` | Improve that book's artifact |
| Questions | Same address, subject `[question] <book-slug>` | Answer by email; recurring questions become an FAQ section in the chapter |
| Book requests | Same address, subject `[request]` | Queue for pipeline |

Personal Gmail plus-addressing is deliberate while the audience is friend + self. A dedicated account (v1 spec's `learningfrombooks.feedback@`) returns to scope only if/when the site goes public-facing.

### Feedback intents → pipeline stage

| Intent | Example | Action |
|---|---|---|
| `infographic` | "Infographic for Law 7" | Stage 3, single chapter |
| `rephrase` | "Chapter 2 summary too dense" | Stage 1/2 re-edit |
| `audio` | "Audio for chapter 4" / "redo, too fast" | Stage 4, single chapter |
| `error` | "Typo in Law 5" | Direct MD fix |
| `question` | "How does Law 3 apply at work?" | Email reply; FAQ if recurring |
| `request` | "Do Thinking, Fast and Slow" | Book queue |
| `general` | freeform | Judgment |

Every acted-on item gets a row in `docs/books/<slug>/feedback-log.md` (published — the improving-in-public trail *is* the product story):

```markdown
## 2026-07-12 — law-07 infographic added
- Intent: infographic · From: (initials) · Commit: <sha>
```

## 5. Repository layout (current + target)

```
living-books/
├── SPEC.md                      # this file
├── PIPELINE.md                  # runbook (Phase B)
├── mkdocs.yml
├── docs/
│   ├── index.md                 # library grid — hand-edited until book #2
│   └── books/<slug>/
│       ├── index.md             # book landing
│       ├── chapters/            # stage 1 output
│       ├── study-guides/        # stage 2 output
│       ├── infographics/        # stage 3 output (PNG)
│       ├── audio/               # stage 4 output (mp3)
│       └── feedback-log.md
└── scripts/                     # deterministic pipeline pieces, added as they stabilize
```

Deferred until book #2 exists (YAGNI until then): `book.yaml` metadata schema, index generator script, `new_book.py` scaffolder, awesome-pages nav config.

Audio lives in-repo as mp3 (~96kbps, ≤2 min/chapter ≈ ≤25 MB/book).
<!-- ponytail: in-repo audio; move to GitHub Releases per-book when repo passes ~300 MB. -->

## 6. Phases v2

| Phase | Scope | Status |
|---|---|---|
| **A · Ship** | Repo, site, seed book, feedback email | ✅ Done 2026-07-05 |
| **B · Pipeline + backfill** | Write `PIPELINE.md`; prove stages 3–4 by backfilling Laws: cover + infographics 02–18 (34 PNGs), audio 01–18; restore CI | Next |
| **C · Second book** | Full pipeline run on a new book, end to end. Then (and only then) add book.yaml + index generator + scaffolder | Queued |
| **D · Loop automation** | Poll inbox → classify intent (Gemini free tier) → dispatch pipeline stage → auto-commit → reply | Deferred until feedback volume justifies it |
| **E · Q&A on site** | ask-tutor-style agent over book corpus (pattern proven on dba-kb) | Deferred |

Phase D's economics from v1 still hold (Gemini 2.5 Flash free tier, GitHub Actions cron, $0/month) — only the dispatch targets changed from NotebookLM calls to owned-pipeline stages.

## 7. Phase B acceptance criteria

- [ ] `PIPELINE.md` runbook committed — each stage runnable from a fresh session with no context
- [ ] Cover image for Laws (Nano Banana) renders on library grid
- [ ] Infographics for Laws 02–18 generated (34 PNGs), embedded in chapter pages
- [ ] Audio overviews for chapters 01–18 (user's cloned voice), playable on chapter pages
- [ ] `mkdocs build --strict` green; site redeployed; spot-check 3 chapters on a phone
- [ ] CI restored: `gh auth refresh -s workflow`, deploy.yml re-added, Pages source switched to Actions
- [ ] Feedback-log started for Laws with the backfill entries

## 8. Risks

| Risk | Sev | Mitigation |
|---|---|---|
| Nano Banana output quality drifts across 34 images | Med | Reuse Law 01 prompt template verbatim; batch-review before commit |
| Chatterbox audio at 18-chapter scale (tone drift, artifacts) | Med | Locked config (natural ref, cfg 0.5, exag 0.5); regenerate outliers individually |
| Repo weight from audio/PNGs | Low | Ceilings noted above; Releases fallback |
| MkDocs 2.0 breaking Material plugins | Low | Pin versions in requirements.txt when CI lands |
| Book content copyright | Med | Companions are transformative summaries/commentary of books user owns; no book text reproduced at length; PDFs never committed |

## 9. Carried over from v1 unchanged

Lean storage strategy · plus-addressing routing mechanics · feedback-log format · MkDocs Material choice · $0/month operating target · Phase D free-tier LLM choice (Gemini Flash).

## 10. Explicitly dropped from v1

- NotebookLM as automated engine (all of: source upload, slide generation, flashcards, audio via automation)
- Google Slides iframe embeds per chapter (owned infographics + audio replace them)
- Dedicated feedback Gmail account (personal plus-address until public)
- Separate migration script (migration already done by hand)
- dba-site wiki stub replacement (wiki copy stays for now; revisit if dual-maintenance hurts)
