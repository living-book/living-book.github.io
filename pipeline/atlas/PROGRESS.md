# Concept Atlas — build progress (session tracker, not shipped)

## Extraction status (29 books)
Wave = relaunch group after session-limit kill. Update as notifications arrive.

- [x] W1 antifragile (7 concepts)
- [x] W1 master-and-emissary (6 concepts)
- [x] W1 general-systems-thinking (7 concepts)
- [x] W1 web-of-life (7 concepts)
- [x] W1 master-algorithm (8 concepts)
- [x] W1 second-machine-age (8 concepts)
- [x] W2 model-thinker (7 concepts)
- [x] W2 how-to-measure-anything (7 concepts)
- [x] W2 beginning-of-infinity (7 concepts, → docs/books/.../concepts/)
- [x] W2 innovators-dilemma (7 concepts)
- [x] W2 business-model-generation (7 concepts)
- [x] W2 theory-of-constraints (7 concepts)
- [x] W3 end-of-competitive-advantage (7 concepts)
- [x] W3 measure-what-matters (7 concepts)
- [x] W3 toyota-kata (7 concepts)
- [x] W3 kanban (8 concepts)
- [x] W3 project-to-product (7 concepts)
- [x] W3 user-story-mapping (6 concepts)
- [x] W4 leaders-eat-last (7 concepts)
- [x] W4 creativity-inc (6 concepts)
- [x] W4 principles (7 concepts)
- [x] W4 progress-principle (7 concepts)
- [x] W4 thinking-fast-and-slow (8 concepts)
- [x] W4 atomic-habits (8 concepts)
- [x] W5 make-it-stick (7 concepts)
- [x] W5 nudge (7 concepts)
- [x] W5 laws-of-human-nature (8 concepts)
- [x] W5 structure-of-scientific-revolutions (8 concepts)
- [x] W5 scientific-research-programmes (8 concepts)

## After extraction
- [~] Edge weaving: 7 lenses → pipeline/atlas/edges/*.yml (done: feedback 23, learning 25, strategy 24, attention 21, incentives 21, flow 19; running: technology)
- [ ] Update pipeline/concept-inventory.yml (regenerate namespaces from files)
- [ ] scripts/build_atlas.py run → docs/atlas/atlas.json (script already written)
- [ ] docs/atlas/index.html — intent-driven interface (Anthropic design system per user CLAUDE.md)
- [ ] mkdocs nav/index entry + strict build
- [ ] Commit, push concept-atlas branch, draft PR (base main; branch includes preview-pilot pilot work)
- [ ] Artifact preview + final report (incl. OKF assessment answer)

## Key paths
- Worktree: /home/sanjayg4/living-books/.claude/worktrees/concept-atlas
- Sources clone: $CLAUDE_JOB_DIR/tmp/sources (= /home/sanjayg4/.claude/jobs/213b014c/tmp/sources)
- Brief for extraction agents: pipeline/atlas/EXTRACTION-BRIEF.md (agent prompt = brief path + book/slug/source/outdir, model sonnet)
