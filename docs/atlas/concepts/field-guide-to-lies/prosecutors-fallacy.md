---
type: Concept
title: The Prosecutor's Fallacy
description: Confusing the probability of evidence given guilt with the probability of guilt given evidence — two conditional probabilities that are not interchangeable.
book: field-guide-to-lies
chapters: [3]
tags: [probability, conditional-probability, legal-reasoning, bayesian-reasoning, fallacy]
created: 2026-07-12
---

# The Prosecutor's Fallacy

## Definition

P(Evidence | Guilty) — the probability of seeing this evidence if the suspect is guilty — is a different quantity from P(Guilty | Evidence) — the probability the suspect is guilty given this evidence — and conflating the two, treating them as interchangeable, is so common in courtrooms it has its own name: the prosecutor's fallacy. Correctly computing the second quantity from the first requires also weighing the prior probability of guilt before any evidence is considered — a step the fallacy skips entirely.

## In the Book

Levitin builds a worked forensic example with a fourfold probability table: a suspect drawn from a pool where the prior odds of guilt are 1 in 50, and forensic evidence (a blood match) that occurs with probability .85 if the suspect is guilty. Naively, a jury might hear "85% blood match" and conclude 85% guilt — the fallacy. Properly combined with the low prior, the actual result is P(Guilty | Match) = .10, meaning the suspect is nine times more likely to be innocent than guilty despite the seemingly damning match; a second piece of evidence (a .95 hair match) then updates this to .68 guilty. Levitin names the fallacy explicitly after walking through it, and pairs it with the real case of Dennis Adams, convicted largely on a DNA match alone — a match that, absent his brother (who shared the DNA profile) being investigated as an alternative suspect, was treated as near-conclusive proof without ever computing the probability of innocence given the same evidence.

## Why It Matters

Naming this fallacy gives a precise diagnostic for a specific, recurring reasoning error: whenever someone reports "the probability of this evidence under hypothesis X," check whether they (or you) are silently treating that as "the probability of hypothesis X given this evidence." The two only coincide when the prior probabilities of the competing hypotheses are equal, which is rarely true. This matters anywhere weak or moderate evidence gets reported as a standalone probability — forensics, medical test results (a positive test is not the probability of having the disease), risk scoring — because skipping the base rate turns modest evidence into false certainty.
