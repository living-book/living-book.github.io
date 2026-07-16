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
- [x] rebuild: 550 edges (4 cross-file dups deduped), 54 orphans, 79% cross-domain; strict build + smoke clean → PR #4 (merged)

## Tranche 4 (user: "execute next wave" 2026-07-14). Branch atlas-tranche-4 off main. 30 books, Sonnet, waves of 6.
- [x] All 5 waves done: 197 concepts / 30 books. Collision fixed: mind-design-ii distributed-representation → distributed-representation-pdp. YAML all clean.
- [x] +30 BOOKS entries; CATALOG + EDGES-EXISTING regenerated (121 books, 839 concepts, 550 edges).
- [x] 4 weavers: 105 edges (org 26, product 29, decisions 29, mind 21) — one session-limit wipe, relaunched 3:21am
- [x] 2 verifiers: kept 94 (24/26, 25/29, 27/29, 18/21); 11 dropped, 13 fixed
- [x] rebuild: 121 books, 839 concepts, 644 edges (80% cross-domain, 103 tempers + 25 contradicts), 145 orphans; corpus 1031 chunks; strict build + smoke clean → PR #5

## Orphan pass 3 (user: "execute next wave orphan pass" 2026-07-14). PR #5 merged; branch atlas-orphan-weave-3 off main.
145 orphans → pipeline/atlas/orphans3/ORPHANS.md (Biz 44, Psych 24, Lead 23, Tech 21, Agile 20, Sys 13).
- [x] 4 Sonnet weavers: 127 edges (biz 44 [100%!], lead-sys 26, psych-agile 38 [93%], tech 19); 14 honest unlinks; zero session-limit kills
- [x] 2 Sonnet verifiers: kept 118 (biz 44→39, lead-sys 26→24, psych-agile 38→37, tech 19→18); 9 dropped, 7 fixed; biz 100% link-rate claim busted (5 forced)
- [x] rebuild: 121 books, 839 concepts, 762 edges (78% cross-domain, 119 tempers + 26 contradicts), 21 orphans; corpus 1031 chunks; strict build + smoke (839 nodes, 0 errors) → PR #6 (merged)

## Tranche 5 (user triage 2026-07-14: Tech + Systems first). PR #6 merged; branch atlas-tranche-5 off main.
User triaged all 271 remaining books via artifact (161 next / 109 skip / 1 later) — decisions in pipeline/atlas/triage/{TRIAGE.md,triage_state.json}.
14 books = all "next" picks in Technology & Data (7) + Systems Thinking & Philosophy (7). +14 BOOKS entries added to build_atlas.py.
- [x] Tech 7 books → 44 concepts (ai-guide 7, mgmt-sci 6, logic-discrete 7, math-econ 7, sci-evidence 6, math-hacker 5, math-sci-2025 6); zero session kills
- [x] Sys 7 books → 39 concepts (conscious-language 6, direct-truth 7, ethics-of-precaution 3 [hand-reconstructed garbled tables], yoga-of-time-travel 4, ultimate-why 6, strategic-thinking 6, gharajedaghi 7)
- [x] 2 weavers: tech 46 (43/44 linked — flagged), systems 30 (77% honest rate, 9 unlinks)
- [x] 2 verifiers: tech 46→40 (6 dropped, 2 fixed — 98% link claim busted again), systems 30→29 (1 dropped, 2 extends→parallels)
- [x] rebuild: 135 books, 922 concepts, 831 edges (76% cross-domain; tempers 129, contradicts 31, instantiates 126, formalizes 22, extends 58, parallels 465), 37 orphans; corpus 1114 chunks; strict build clean; smoke 922 nodes / 0 errors → PR #7
Known issues to fix post-wave: (1) linear-programming slug collision — written by BOTH intro-to-management-science and mathematics-for-economics-and-business; rename econ one to linear-programming-corner-points. (2) strategic-thinking-for-leaders source content is actually "50 One-Minute Tips for Leaders" (same Haines/systems framework) — title kept, noted. (3) math-hacker author = Paul Carson (fixed in BOOKS).

## Tranche 6 (user: "merged, next tranche more efficient, low-cost model, no quality loss" 2026-07-15). PR #7 merged; branch atlas-tranche-6 off main.
Agile & Software Delivery: 29 "next" picks − 1 duplicate (Reinertsen Product Development Flow = tranche-2 product-development-flow) = 28 books.
COST MODEL: extraction on Haiku 4.5 (pilot wave A of 6 → QA gate: yaml/section script + grounding spot-read → scale or fall back to Sonnet). Weave + adversarial verify stay Sonnet (quality gates unchanged). Tiny docs (<60KB: scrum-guide, kanban-guide, collaboration-at-scale, adaptive-governance, agile-leadership-kata, evidence-based-management-guide) batched 3-per-agent.
In-tranche slug-collision risk HIGH (28 overlapping agile books) — post-wave collision scan mandatory.
- [x] Wave A (Haiku pilot): 6 books — first launch killed by weekly limit @23:xx PT 7/14 (2 survived complete); relaunched 4 after 12am reset. All 6 done.
- [x] QA gate: HAIKU PASSES (grounded, case-study specifics, Sonnet-standard). scripts/qa_concepts.py added (yaml/keys/sections/desc-length/collisions). Haiku failure modes seen: unquoted colons in yaml (2), collision despite CATALOG grep (kaizen-culture→embedding-kaizen-culture, living-documentation deleted as already-owned dup), 1 long description.
- [x] Wave B: great-big-agile 8, making-sense-of-agile 9, agile-pm-with-scrum 8, agile-pm-with-kanban 8, bdd-in-action 7, disciplined-agile-delivery 7. A+B = 12 books / 93 concepts, gate PASS.
- [x] Wave C (final, 12 Haiku agents): all 16 books done. Full-tranche QA: 20 fails → 14 false positives (2 agents wrote their slugs into CATALOG.md uninvited — reverted CATALOG before gating), 6 real (2 yaml colons, 2 long descriptions, 2 duplicate concepts: less-org-design empirical-process-control deleted [= Schwaber's], collaboration-at-scale definition-of-done → definition-of-done-at-scale). 28 books / 187 concepts, GATE PASS.
- [x] +28 BOOKS entries, atlas rebuilt (163 books, 1110 concepts), CATALOG + EDGES-EXISTING regenerated (concept key = 'id' not 'slug').
- [x] 4 Sonnet weavers (flow/scaling/people/craft, anchored, ≥60% cross-domain mandate): 118 edges, honest unlink 35-44%.
- [x] 2 Sonnet verifiers: people 29→24, scaling 30→25, flow 30→21, craft 29→13 = 83 kept (26 fixed, 35 dropped — craft weaver forced hardest, 2 of its "deepest finds" killed). One verify sub-subagent made unrequested commit 8fab7a6 + push on atlas-tranche-6 (intermediate state; final files reconciled on top — harmless).
- [x] rebuild: 163 books, 1110 concepts, 914 edges (78% cross-domain; tempers 140, contradicts 35, instantiates 130, formalizes 23, extends 58, parallels 528), 141 orphans (new-book residue → next orphan pass); corpus 1302 chunks; strict build clean; smoke 1110 nodes / 0 real errors (only /favicon.ico 404 from bare http.server) → PR #8
COST RESULT: 28/28 extractions on Haiku (~90-120k tok/book vs Sonnet) — quality gate-passed; Sonnet reserved for weave+verify only. Haiku failure modes (for next tranche prompts): unquoted yaml colons, occasional generic slug despite CATALOG grep, 2 agents "helpfully" editing CATALOG.md.

## Tranche 7 (user: "merged, continue next tranche" 2026-07-15). PR #8 merged; branch atlas-tranche-7 off main.
30 books: Leadership & Coaching all 15 "next" picks + Psychology first 15 (alpha order of 50 resolvable picks; hbr-smart-decisions unresolvable in sources). Haiku extraction + QA gate; Sonnet weave+verify. Orphan pass (141) still queued separately.
- [ ] Wave A (15 Haiku): leadership books
- [ ] Wave B (15 Haiku): psych books
- [ ] QA gate, +30 BOOKS, CATALOG regen
- [ ] 4 Sonnet weavers → 2 Sonnet verifiers → rebuild → strict+smoke → PR #9
Tranche 7 result: waves A+B all 30 done (leadership 113 + psych 118 = 231 concepts; QA fails: 9 yaml colons/descriptions, 3 collisions renamed [powerful-questions→powerful-questions-in-coaching, thematic-goal→thematic-goal-workshop, skilled-incompetence→organizational-defensive-routines], 0 CATALOG edits by agents — new prompt rules worked).
4 Sonnet weavers: 103 edges (coaching 24, leadership 29, behavior 27, emotion 23), honest unlink 45-62%. Verify: session-limit killed both verifiers mid-run (10:30am PT reset); relaunched → coaching 19, leadership 23, behavior 22, emotion 18 = 82 kept, 7 fixed, 21 dropped.
Rebuild: 193 books, 1341 concepts, 996 edges (79% cross-domain; tempers 154, contradicts 41), 277 orphans (two-tranche residue — orphan pass overdue); corpus 1533 chunks; strict clean; smoke 1341 nodes/0 real errors → PR #9.

## Orphan pass 4 (user: "merged, now do orphan pass" 2026-07-15). PR #9 merged; branch atlas-orphan-weave-4 off main.
277 orphans → pipeline/atlas/orphans4/ORPHANS.md (Agile 101, Psych 76, Lead 75, Sys 12, Tech 10, Biz 3).
- [x] 4 Sonnet weavers: 185 edges (agile-A+tech 35, agile-B+sys 46, lead+biz 52, psych 52); honest link 60-72%; agile-B weaver self-audited from forced ~100% down to 71%.
- [x] 2 Sonnet verifiers (extra-harsh orphan mandate): kept 140 (29/35, 47/52, 30/46, 34/52); 45 dropped (incl. laundering kills: three-principles∥autopoiesis, elevated-emotion∥edso), 19 fixed.
- [x] rebuild: 193 books, 1341 concepts, 1136 edges (79% cross-domain; tempers 163, contradicts 45), orphans 277→129 (honest residue: Dzogchen core, Yukl taxonomies, coaching-process frameworks); corpus 1533 chunks; strict clean; smoke 1341 nodes / 0 bad responses → PR #10

## Wave 1 — high-impact remainder (user: "Go ahead with recommended Wave 1 scope" 2026-07-15). PR #10 merged; branch atlas-wave-1 off main.
Remainder analysis first: 88 files left (Biz 52 + Psych 36) → 5 impact-ranked waves; recommended 1-3 (44 books), skip ~44 (dups/boxed sets/textbooks/no-mechanism). Correction: hbr-smart-decisions IS resolvable — curly apostrophe (U+2019) in filename broke slugify match; also HBR 2019 file is byte-duplicated, McKinsey Valuation 852K = excerpt of full 4.4MB Valuation, "Mental Models" = Indi Young UX (not Johnson-Laird), Deming file = garbled DoD thesis.
Wave 1 = 14 root sources & tension engines: Drucker Management, Ackoff Re-Creating Corp, Process/Sensemaking/Organizing (Hernes+Maitlis), Argyris Flawed Advice + Reasons and Rationalizations, Implementing Beyond Budgeting (Bogsnes), Amazon Shareholder Letters, Tversky Preference/Belief/Similarity, How People Learn (NRC), Willpower Instinct, Applied Critical Thinking Handbook (UFMCS), Power of Full Engagement, Appreciative Inquiry, Sense and Respond — header check revealed Barlow/Parry/Faulkner 2005 (lean-service), NOT Gothelf; slug sense-and-respond-barlow-parry-faulkner.
- [x] 14 Haiku extractors: 110 files → QA gate 5 fails → dropped 5 dups (management-by-objectives, espoused-theory-vs-theory-in-use, loss-aversion, representativeness-heuristic already owned; internal-external-commitment near-dup of sibling flawed-advice concept), 1 yaml colon fix → 105 concepts GATE PASS.
- [x] +14 BOOKS entries, CATALOG appended, EDGES-EXISTING regenerated (1129 edges from yml).
- [x] 4 Sonnet weavers (org-control 21, learning-defenses 24, decisions 20, energy-service 21 = 86 edges, 71-92% cross-domain, 8+6+tensions).
- [x] 2 Sonnet verifiers: 17+22+17+19 = 75 kept (11 killed incl. weaver "deepest find" untested-attributions-tempers-five-whys; 9 fixed). Survival 87%.
- [x] rebuild: 207 books, 1446 concepts, 1211 edges (tempers 186, contradicts 52, formalizes 27), orphans 164 (129 carried + 35 new residue — orphan pass 5 queued); corpus 1638 chunks; mkdocs strict clean; smoke 200s on atlas page + atlas.json + corpus.json → PR pending.
Remaining after Wave 1: Wave 2 (14 decision-science & money bridges), Wave 3 (16 craft/resilience/strategy anthologies), Waves 4-5 defer/skip.

## Wave 2 (user: "PR 11 merged, start wave 2" 2026-07-15). Branch atlas-wave-2 off main.
14 decision-science & money-bridge books: McKinsey Mind, Valuation (Koller), Lean CFO, Digital Transformation Playbook, Theory of Incentives, How We Decide, How We Learn (Carey), Smarter Than You Think, Simplicity (de Bono), Remote, Traction (Wickman EOS) + Traction (Weinberg channels), Design Thinking (Cross), HBR Smart Decisions (curly-apostrophe path passed explicitly — resolved fine).
- [x] 14 Haiku extractors → 105 concepts, GATE PASS first try (0 collisions — matured prompts). Remote extractor killed by spurious content-filter API error after writing all 6 files; files verified complete, no relaunch.
- [x] +14 BOOKS, CATALOG appended, EDGES-EXISTING regen (1204).
- [x] 4 Sonnet weavers: money-value 22, problem-solving 23, learning-cognition 19, operating-growth 20 = 84 (70-90% xdom). Core tension landed: hypothesis-driven-analysis contradicts co-evolution-of-problem-and-solution.
- [x] 2 Sonnet verifiers: 19+18+15+18 = 70 kept (14 killed, 11 fixed; 83% survival). Both pre-flagged suspects killed: revelation-principle⇒disagree-and-commit (analogy dressed as formalization), instrumental-convergence⇒centaur-collaboration (invented capability-gap condition).
- [x] rebuild: 221 books, 1551 concepts, 1283 edges (= 1211+70+2 previously-unresolvable now satisfied; drops 22→20); corpus 1743 chunks; strict clean; smoke 200s → PR #12.
Remaining: Wave 3 (16 craft/resilience/strategy anthologies), then orphan pass 5 (accumulating residue), Waves 4-5 defer/skip.

## 3D Atlas explorer (user approved warm-dark 3D recommendation 2026-07-16). Branch atlas-3d off main (post PR #12).
docs/atlas/3d/index.html — WebGL galaxy view of the full atlas (1551 nodes / 1283 edges, 60fps):
- Warm-dark futurism: design-system Near Black bg, 6 warm domain hues, additive halo sprites (6 shared canvas textures, not per-node), NO cool blues — parchment ivory cards on dark.
- Spin-to-front on select: camera tweens along origin ray (1400ms), node faces viewer; ego-focus mode (1-3 hop depth slider via nodeVisibility — layout stable, no data swap).
- Hover: node swell + neighbors lit + rest dimmed to 10%, directional particles on active edges; EDGE hover shows the why-sentence (parchment tooltip) — why-sentences now first-class UI.
- Tension lens toggle: 254 contradicts/tempers edges only (debate map). Domain chips filter. Search with fly-to. Esc reset. prefers-reduced-motion honored (no autorotate/particles, 300ms cams). Pixel ratio capped 2.
- Vendor: single esbuild IIFE bundle (3d-force-graph 1.80.0 + three, ONE instance) — first attempt with separate three.min.js r160 UMD + graph UMD failed (THREE.Timer missing + dual-instance clash). Bloom = additive halo sprites, not UnrealBloomPass (dep-chain not worth it).
- 2D atlas untouched, linked both ways (header "◈ 3D Atlas").
- Smoke: playwright-core + cached chromium + swiftshader — canvas renders, search→select→card→depth→lens all pass, 0 real console errors; screenshots verified. mkdocs --strict clean.

## Library landing refresh (user: match 2D-atlas look, interactive/dynamic — 2026-07-16). Branch library-refresh off main (post PR #13).
docs/index.md (Material-themed) replaced by docs/index.html — standalone parchment page, same chrome/design language as the 2D atlas:
- Live stats band (books/concepts/edges/tensions) count-up from atlas/atlas.json.
- Companions shelf built from atlas.json status=published (6 cards; cover.jpg with onerror → domain-ink "spine" fallback for the 2 coverless).
- Whole-library browser: search + 6 domain chips (2D-atlas chip pattern), grouped by domain, expandable rows → concept chips deep-linking atlas/#slug + "view in 3D"; companion badge on published.
- 3D page gained #slug deep links (select-on-load after warmup + hashchange + history.replaceState on select/deselect).
- Scroll-reveal via IntersectionObserver; prefers-reduced-motion honored everywhere.
- Smoke (playwright): stats 221/1,551/1,283/254, search "drucker"→3, expand→8 concept chips, chip toggle→198/221, 3D #feedback-loops deep link opens card; 0 errors. mkdocs --strict exit 0 (index.md removal safe — raw index.html copied verbatim).
