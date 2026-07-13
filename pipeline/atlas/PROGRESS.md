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
- [x] Edge weaving: 7 lenses, 155 edges woven
- [~] Edge verification (Sonnet, adversarial): done incentives/flow/technology (61→55) + strategy/attention (45→39); running feedback/learning
- [ ] Update pipeline/concept-inventory.yml (regenerate namespaces from files)
- [ ] scripts/build_atlas.py run → docs/atlas/atlas.json (script already written)
- [ ] docs/atlas/index.html — intent-driven interface (Anthropic design system per user CLAUDE.md)
- [ ] mkdocs nav/index entry + strict build
- [ ] Commit, push concept-atlas branch, draft PR (base main; branch includes preview-pilot pilot work)
- [ ] Artifact preview + final report (incl. OKF assessment answer)

## Tranche 2 (user-approved: steps 1 PR ✓, 2 corpus ✓, 3 = this). 30 books, Sonnet, waves of 6.
Sources root: $CLAUDE_JOB_DIR/tmp/sources. All output dirs: docs/atlas/concepts/<slug>/.
After extraction: add 30 entries to BOOKS in scripts/build_atlas.py, regenerate CATALOG.md,
Orphan pass: woven 162; verify batch2 done (psych-agile 48→43, systems-tech 44→41); batch1 (business, leadership) running. Then rebuild, PR #2.

- [~] A deep-simplicity (Gribbin, Systems), simple-rules ✓7, art-of-problem-solving ✓8, on-the-shortness-of-life ✓5, ai-superpowers ✓6, the-inevitable ✓7 — others RUNNING
- [ ] B fabric-of-reality (Deutsch, Tech: "The fabric of reality...WeLib.org .md" in Tech/AI), field-guide-to-lies ✓7, design-of-everyday-things ✓8, inspired ✓7, running-lean ✓7, four-steps-to-the-epiphany ✓8
- [ ] C zone-to-win ✓6, jobs-to-be-done (Business/BMI), intelligent-investor ✓7, the-advantage (Lencioni, Business/OrgDesign "The advantage _ why..."), product-development-flow ✓7, toyota-production-system ✓7
- [ ] D lean-software-development ✓7, making-work-visible ✓7, essential-drucker ✓8, five-dysfunctions-of-a-team ✓6, act-like-a-leader ✓7, why-great-leaders-dont-take-yes (Roberto, Leadership/LeadDev "Why Great Leaders Don't Take Yes for an Answer Managing for  ( PDFDrive.com ).md")
- [ ] E power-of-habit ✓7, mastery ✓7, checklist-manifesto ✓6, six-thinking-hats ✓6, art-of-learning ✓7, digital-minimalism (Newport, Psych/Mindfulness)

## Key paths
- Worktree: /home/sanjayg4/living-books/.claude/worktrees/concept-atlas
- Sources clone: $CLAUDE_JOB_DIR/tmp/sources (= /home/sanjayg4/.claude/jobs/213b014c/tmp/sources)
- Brief for extraction agents: pipeline/atlas/EXTRACTION-BRIEF.md (agent prompt = brief path + book/slug/source/outdir, model sonnet)
