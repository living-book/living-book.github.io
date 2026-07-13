---
type: Concept
title: Testing Is Sampling, Never Exhaustive
description: The number of possible tests for any real program is effectively infinite, so every test suite is a sample — and a sample's adequacy is a judgment call, not a fact.
book: perfect-software
chapters: [3]
tags: [sampling, combinatorics, measurement, epistemology, testing]
created: 2026-07-12
---

# Testing Is Sampling, Never Exhaustive

## Definition

"Testing can be exhausting, but it can never be exhaustive." Because inputs, sequences, configurations, timing, and internal state combine combinatorially, the set of possible tests for even a trivial program is effectively infinite, so any real test suite is a sample of that space, not a survey of it. Whether a given sample is "good enough" is not a technical fact about the tests but a psychological and organizational judgment about what was worth looking for.

## In the Book

Weinberg takes the simplest imaginable program — one that prints "Hello Dolly!" when you hit the space bar — and asks how many test cases you'd need to bet your life you'd covered every possibility; he then shows a real case where a programmer, Wanda Marilyn Jones, built a password backdoor triggered only by an obscure 170-plus-keystroke sequence, which a "highly sophisticated test plan" missed for three years and only a code review found. He piles on multiplicative factors — ten CPUs times ten memory sizes times ten disk sizes, ten-factorial orderings of ten functions, program memory that changes results on repeat runs, true hardware-timing randomness — to argue the space is not just large but unbounded, quoting Dijkstra that testing can reveal bugs but never their absence. He then reframes any real test effort as sampling, illustrated by a story about a rain gauge that badly under- or over-reports a New Mexico downpour of huge, widely spaced drops (his own beard, he notes, was a better rain gauge that day) — the same size sample can wildly mis-measure depending on what the underlying "storm" looks like.

## Why It Matters

This kills the fantasy of "complete coverage" in any complex system — testing, auditing, monitoring, or research — and replaces it with the sharper, answerable question a sampling frame forces you to ask: what does this particular sample represent, and for whom is that representative enough? It converts an impossible goal (total certainty) into a manageable one (a defensible sampling strategy).
