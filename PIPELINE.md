# Living Books — Pipeline Runbook

Book in → companion out. Run any stage independently from a fresh Claude Code session.
Spec: `SPEC.md` §3. All output lands under `docs/books/<slug>/`.

## Conventions

- **slug**: kebab-case book title, e.g. `laws-of-human-nature`
- **chapter id**: `NN-short-name`, zero-padded, e.g. `law-07-defensiveness` (keep book's own naming if it has one)
- Local clone: `/home/sanjayg4/living-books` · venv: `.venv/bin/mkdocs`
- Secrets: `~/.config/living-books/.env` (AgentMail; never committed)

## Stage 1 — Ingest (book → chapter markdown)

Input: book text, notes, or user's knowledge of the book.
Output: `docs/books/<slug>/chapters/<chapter-id>.md`, one per chapter.

- Template: 10 H2 sections — Core Concept · Human Weakness/Problem · Case Study ·
  Transformation · Practical Guide · Modern Application · Warning Signs · Key Quotes ·
  Reflection Questions · Connections. Rename sections to fit genre; keep count + intent.
- Method: parallel Claude agents, ~6 chapters each. Frontmatter: `title`, `chapter`, `created`.
- Cross-link chapters with standard MD links (no wikilinks — MkDocs).
- Plus a book landing page `index.md`: chapter table, themes, how-to-use.

## Stage 2 — Study guides

Input: stage 1 chapters. Output: `study-guides/<chapter-id>-study-guide.md` + `study-guides/index.md`.
Same agent pattern. Structure: Core Concept · Key Terms · Case Study Summary ·
Application Checklist · Self-Test Questions.

## Stage 3 — Infographics (Nano Banana)

Tool: `python /home/sanjayg4/.claude/plugins/marketplaces/ibrahim-plugins/scripts/genimage.py`
Output: `infographics/<chapter-id>-start.png`, `<chapter-id>-end.png`, `cover.png`

- Always `--aspect-ratio 16:9 --resolution 2K` for chapter infographics (2K = Pro model,
  needed for legible text). Cover: `--aspect-ratio 2:3 --resolution 2K`.
- **Keep every text label ≤4 words** — long strings garble (see Law 01 END, pre-2K).
- START template (read before chapter): three editorial panels — the trap (visual metaphor
  + 2 labels), the historical figure (name + dates), the stakes (2 labels). Banner:
  chapter number + title. Footer arrow: the chapter's directive.
- END template (read after chapter): transformation arc (BEFORE→SHIFT→AFTER circles),
  case study card (figure, lesson ≤6 words, outcome ≤6 words), 6 strategy cards
  (icon + ≤3-word label), warning signs row (4 flags, ≤4 words each), action card.
- Style string (append to every prompt): "Editorial magazine infographic, navy #1a2f4a
  and gold #c9a227 on cream #f2efe6, clean flat illustration, generous whitespace,
  sans-serif headers."
- Review every image before commit; regenerate garbled ones individually.

## Stage 4 — Audio (Chatterbox, cloned voice)

Tool: `cd /home/sanjayg4/chatterbox && ./voice --text "..."` (locked config: English
model, natural ref, cfg 0.5, exag 0.5 — see chatterbox/VOICE.md for output flags)
Output: `audio/<chapter-id>.mp3`

- Script per chapter: ~200–230 words ≈ 90s. Structure: hook (1 line) → core idea
  (2–3 lines) → the case study in one breath → the single practice to try → closing line.
- Written for the ear: short sentences, no lists, no citations.
- Convert wav→mp3 96kbps: `ffmpeg -i in.wav -codec:a libmp3lame -b:a 96k out.mp3`
- Embed in chapter page (top, after title):
  `<audio controls src="../audio/<chapter-id>.mp3"></audio>`

## Stage 5 — Assemble + deploy

1. Infographics into chapter pages: START image after the audio block, END image before
   Reflection Questions.
2. Book row in `docs/index.md` library table (hand-edit until book #2 exists).
3. `feedback-log.md` in book folder, seeded with creation entry.
4. Verify: `.venv/bin/mkdocs build --strict` — must be green.
5. Deploy: `.venv/bin/mkdocs gh-deploy --force` (until CI restored).
6. Spot-check live: https://living-book.github.io/ — 3 chapters, phone viewport.
7. Commit + push main.

## Feedback handling (until Phase D automation)

Inbox: `visual-book-feedback-action@agentmail.to`. Intent table: SPEC.md §4.
Act → log row in book's `feedback-log.md` → deploy → reply with live URL.
