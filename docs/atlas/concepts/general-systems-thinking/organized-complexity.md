---
type: Concept
title: Organized Complexity
description: The region of systems too complex for equation-by-equation analysis and too structured for statistical averaging — neither mechanism nor mass will do.
book: general-systems-thinking
chapters: [1]
tags: [complexity, systems-thinking, reductionism, methodology, scale]
created: 2026-07-12
---

# Organized Complexity

## Definition

Weinberg divides the world into three regions by number of interacting parts and their randomness. "Organized simplicity" (few parts, tightly determined) is the domain of mechanics; "unorganized complexity" (huge numbers of near-identical, near-random parts) is the domain of statistics. Between them sits "organized complexity" — systems too tangled for equation-by-equation analysis and too structured for the Law of Large Numbers to average away. This middle zone, governed by what he calls the "Law of Medium Numbers," is where computers, cells, organizations, and forests actually live.

## In the Book

Weinberg builds the idea from two computational facts. First, the "Square Law of Computation": the work needed to solve a system of equations grows roughly with the square of the number of equations, which is why Newton could only solve the solar system by ignoring all but ten of its thousands of bodies and treating them pairwise (reducing ~1000 equations to about 45, then to about 10 by exploiting the sun's dominant mass). Second, the "Square Root of N Law," quoted from Schrödinger: statistical averages over N particles are only accurate to about 1/√N, which is why nineteenth-century physicists (Gibbs, Boltzmann, Maxwell) could treat a bottle of gas's 10^23 molecules by averaging pressure and temperature instead of tracking individual particles. Plotting complexity against randomness, Region I (organized simplicity, machines) sits in one corner and Region II (unorganized complexity, aggregates) in the other; Region III, "the yawning gap in the middle," is "the region of systems" — too complex for analysis, too organized for statistics. Weinberg folds this into the Law of Medium Numbers, whose folk version is Murphy's Law: for medium-number systems, "large fluctuations, irregularities, and discrepancy with any theory will occur more or less regularly."

## Why It Matters

Most interesting real systems — a codebase, a team, an ecosystem, a market — have "medium numbers" of interacting parts: too many to model exhaustively, too few and too structured for statistics to smooth over. Naming this middle zone explains why both engineering-style modeling and survey-style averaging routinely fail on the same problems, and reframes "irreducible messiness" not as a failure of method but as a predictable property of a size regime. It gives a diagnostic question to ask before reaching for a tool: is this problem small enough to solve exactly, large and random enough to average, or stuck in the gap where neither works?
