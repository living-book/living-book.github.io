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

## Tranche 3 (user: "merged, continue" 2026-07-13). Branch atlas-orphan-weave merged; now on atlas-tranche-3 off main.
30 books, Sonnet, waves of 6. Sources: $CLAUDE_JOB_DIR/tmp/sources. Output: docs/atlas/concepts/<slug>/.
After extraction: +30 BOOKS entries in scripts/build_atlas.py, regen CATALOG, weave (4 Sonnet anchored on new books), verify (2 Sonnet), rebuild atlas+corpus, strict build, smoke, PR #3.

- [~] A thinking-for-a-change ✓7, simplexity (Kluger, Systems), whats-it-all-about ✓6, what-to-do-when-machines-do-everything ✓7, perfect-software ✓8, coders ✓8 — rest RUNNING
- [ ] B reinventing-organizations ✓7, reframing-organizations ✓7, sprint (Knapp, Business/BMI "Sprint ( PDFDrive.com ).md"), lean-product-playbook ✓6, secrets-of-consulting ✓7, are-your-lights-on ✓8
- [ ] C tao-of-charlie-munger ✓6, the-ultimate-question ✓7, strategy-beyond-the-hockey-stick ✓6, coaching-agile-teams ✓7, specification-by-example (Adzic, Agile/Lean), personal-kanban (Benson&Barry, Agile/Scrum&Kanban)
- [ ] D value-stream-mapping ✓7, learning-agile (Stellman&Greene, Agile/Scrum&Kanban), leadership-challenge ✓7, simple-habits-for-complex-times ✓6, secret-language-of-leadership ✓8, gamestorming ✓7
- [ ] E clean-language ✓7, pragmatic-thinking-and-learning ✓7, when-perfect-timing ✓7, decision-quality ✓8, daring-greatly ✓6, the-antidote (Oliver Burkeman, Psych/Mindfulness)
t3 weave: systems-decisions ✓23, people-psyche ✓27; all 4 ✓ (98); verify: flow 23→22, psyche 27→24; batch1 running. Then 2 verifiers, rebuild, PR #3.

## Orphan pass 2 (user: "next wave, optimize tokens" 2026-07-13). PR #3 merged; branch atlas-orphan-weave-2 off main.
145 orphans → pipeline/atlas/orphans2/ORPHANS.md (Biz 43, Lead 24, Psych 21, Agile 21, Tech 20, Sys 16).
- [x] 4 Sonnet weavers: 112 edges (biz 27, lead-sys 32, psych-agile 37, tech 16); 30 honest unlinks
- [x] 2 Sonnet verifiers: kept 88 (24/27, 26/32, 26/37, 12/16); 24 dropped, 10 fixed
- [x] rebuild: 550 edges (4 cross-file dups deduped), 54 orphans, 79% cross-domain; strict build + smoke clean → PR #4
