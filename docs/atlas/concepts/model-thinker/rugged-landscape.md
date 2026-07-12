---
type: Concept
title: Rugged Landscape
description: When attributes of a design interact, the space of possible solutions has multiple peaks, so which local optimum a search finds depends on where it starts and what heuristic it uses.
book: model-thinker
chapters: [28]
tags: [optimization, search, innovation, complexity, path-dependence]
created: 2026-07-12
---

# Rugged Landscape

## Definition

A rugged landscape is a solution space with multiple local peaks (optima) rather than one, created when the attributes of a design interact — improving one attribute's contribution depends on the setting of another. On such a landscape, a hill-climbing search (a "gradient heuristic") reliably gets stuck on whichever peak lies within its starting point's "basin of attraction," and the global peak, having the smallest basin, is often the *least* likely one to be found by chance.

## In the Book

Page introduces the model with the "Mount Fuji" case first: a single-peaked landscape, illustrated by a coyote's tail length trading off balance against signaling, or the pan size of a coal shovel (formalized historically by Frederick Taylor's scientific-management studies, which Page notes optimized for efficiency while neglecting worker well-being). Ruggedness — multiple peaks — appears once attributes interact: designing a couch where the ideal arm width depends on cushion thickness produces two distinct good designs (thick-thick or thin-thin) rather than one. He formalizes this with the NK model, where an object is a binary string of N attributes and K controls how many other bits each bit's value depends on: K=0 gives a smooth, single-peaked (linear) landscape, while K=N−1 makes the landscape maximally rugged and effectively random. Page shows that different search heuristics (e.g., "climb the steepest gradient" versus "go to the right") applied to the identical rugged landscape locate the same set of peaks but with different basins of attraction, and that harder, more interdependent problems benefit more from running multiple diverse heuristics or starting points in parallel and keeping the best result found.

## Why It Matters

Wherever a design or strategy problem has attributes that interact — product design, organizational structure, R&D — the reason a "good enough" outcome persists instead of the truly best one is not stupidity but topology: search got trapped in a local peak's basin of attraction. This reframes stuck-ness as a structural property of the problem you can address by diversifying starting points or search heuristics, rather than a failure of intelligence or effort, and it explains why the same problem can have several equally sensible but mutually incompatible "best practices."
