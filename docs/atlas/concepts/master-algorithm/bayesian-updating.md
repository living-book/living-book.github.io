---
type: Concept
title: Bayesian Updating
description: Belief should be treated as a probability that shifts in a mathematically precise way as new evidence arrives, weighted by how likely that evidence is under each hypothesis.
book: master-algorithm
chapters: [6]
tags: [probability, inference, evidence, belief-revision]
created: 2026-07-12
---

# Bayesian Updating

## Definition

Bayes' theorem states that the probability of a cause given an observed effect equals the cause's prior probability, times the probability of the effect given the cause, divided by the effect's overall (unconditional) probability: P(cause | effect) = P(cause) × P(effect | cause) / P(effect). Domingos calls it "a machine that turns data into knowledge" and, for the Bayesian tribe of machine learning, the closest thing to a master algorithm, since in principle it applies with whole models standing in for hypotheses and datasets standing in for evidence.

## In the Book

Chapter 6 builds the theorem from a "waking on a strange planet" thought experiment: your prior probability that the sun will rise (based on general knowledge that planets tend to orbit stars) gets revised into a posterior probability as evidence accumulates — the sky lightening is stronger evidence of sunrise than stars fading, because fading stars could also be explained by fog. Domingos then derives the theorem cleanly from a medical example: of 100 patients, 14 had the flu, 20 had a fever, 11 had both, and simple counting shows the two ways of computing P(flu, fever) must be equal, which rearranges directly into Bayes' theorem. He uses the classic HIV-test example to show how neglecting the prior leads people astray: even with a test that's 99% accurate, testing positive in a population where HIV prevalence is only 0.3% raises your true probability of having HIV only to about 30%, not 99%, because the rarity of the condition (the prior) matters as much as the test's accuracy. The chapter goes on to build this pairwise updating into full Bayesian networks that combine many uncertain causes and effects.

## Why It Matters

Bayesian updating is a portable check on inference in any domain: it explains precisely why a rare-event test with high accuracy can still be mostly wrong when it fires (ignoring the base rate is the single most common statistical reasoning error, in medicine, forensics, hiring, and fraud detection alike), and it gives a disciplined alternative to updating beliefs by gut feel — start from a stated prior, weight new evidence by how surprising it would be under competing hypotheses, and only then revise.
