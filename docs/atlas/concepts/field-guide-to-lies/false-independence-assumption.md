---
type: Concept
title: The False Independence Assumption
description: Multiplying probabilities together to get a vanishingly small joint chance is only valid if the underlying events are actually independent — and they often are not.
book: field-guide-to-lies
chapters: [1]
tags: [probability, statistics, causation, legal-reasoning, correlation]
created: 2026-07-12
---

# The False Independence Assumption

## Definition

The multiplication rule for combining probabilities — multiply individual probabilities to get the joint probability of both events happening — only holds when the events don't influence one another. When events share a hidden common cause (genetics, environment, household conditions), treating them as independent and multiplying their probabilities together produces a number that is dramatically, misleadingly small, making a coincidence look astronomically improbable when it is not.

## In the Book

Levitin's central case is Sally Clark, convicted of murdering her second child after her first had died of SIDS. The prosecution's expert witness testified that since SIDS occurs in roughly 1 in 8,543 infant deaths, the odds of two SIDS deaths in one family were that figure squared — about 1 in 73 million — treating the two deaths as independent events. But siblings share a household (exposure to secondhand smoke, sleeping position) and 50% of their DNA, so whatever predisposed the first child to SIDS-like death plausibly predisposed the second one too; the events are correlated, not independent, and the "1 in 73 million" figure was fabricated by an invalid multiplication. Clark served three years in prison before her husband found hospital evidence of a microbiological cause of death and she was acquitted. Levitin contrasts this with legitimate uses of the multiplication rule, such as coin-and-card draws or website security questions, where the events genuinely are independent.

## Why It Matters

This concept is a specific, checkable test for a common statistical error: before multiplying probabilities, ask whether the events could share a cause. It matters most in exactly the high-stakes settings where this fallacy has historically done damage — forensic and legal reasoning, medical risk assessment, insurance and actuarial claims — because a fabricated tiny probability reads as near-certain proof when in fact it rests on an unjustified independence assumption. It is the mirror image of correlation-implies-causation: here, unjustifiably assumed non-correlation manufactures false certainty.
