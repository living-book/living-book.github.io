---
type: Concept
title: Certainty Factors
description: A pragmatic alternative to Bayesian probability that attaches a single belief/disbelief number to each rule and combines them with simple algebra, not a full joint distribution.
book: ai-guide-to-intelligent-systems
chapters: [3]
tags: [uncertainty, expert-systems, heuristics, reasoning, probability]
created: 2026-07-12
---

# Certainty Factors

## Definition

Certainty factors theory attaches a number between −1.0 (definitely false) and +1.0 (definitely true) to each rule's conclusion, built from a measure of belief MB(H,E) and a measure of disbelief MD(H,E) that are combined into a single certainty factor cf. Unlike full Bayesian reasoning, it does not require prior and conditional probabilities for every hypothesis — it lets an expert state, in effect, "if the evidence holds, I believe the conclusion to degree 0.8" without committing to a coherent probability model underneath. Certainty factors propagate through a reasoning chain by simple multiplication (for a single antecedent) and a combination formula (for multiple rules converging on the same hypothesis), rather than by Bayes' rule.

## In the Book

Chapter 3 introduces certainty factors as the solution MYCIN's developers reached after discovering that medical experts diagnosing blood infections and meningitis expressed belief in terms that were "neither logical nor mathematically consistent," and that reliable statistical data for the domain didn't exist — so a classical probability approach was unusable. The book works a rule like "IF the sky is clear THEN the forecast is sunny {cf 0.8}" through the propagation arithmetic: if the current certainty that the sky is clear is 0.5, the net certainty of "sunny" is 0.5 × 0.8 = 0.4, read off a table that maps numeric ranges to phrases like "maybe" or "almost certainly." It also works a case with rule certainty factors of opposite sign to show how the combination formula produces a net certainty, and closes chapter 3 by comparing certainty factors against Bayesian reasoning directly: certainty factors are cheaper to elicit and more robust to inconsistent expert testimony, but lack Bayesian reasoning's theoretical grounding and can, in principle, produce a different answer depending on the arbitrary order in which rules are combined.

## Why It Matters

Certainty factors are what a rigorous formalism looks like once you accept that the people supplying the numbers cannot give you a coherent joint probability distribution and don't have the data to derive one anyway. That trade-off — a cheaper, locally-consistent scoring rule instead of a global model nobody can actually populate — shows up whenever a system has to aggregate expert judgment under time or data pressure: credit scoring rules-of-thumb before enough default data exists, medical triage checklists, or any weighted-scorecard decision process built from practitioners' rough confidence levels rather than a fitted statistical model.
