---
type: Concept
title: The Multiplicative Counting Principle
description: Count the outcomes of a multi-step process by multiplying the number of choices at each step, even when later choices depend on earlier ones.
book: logic-and-discrete-mathematics
chapters: [6]
tags: [combinatorics, counting, decomposition, decision-trees]
created: 2026-07-12
---

# The Multiplicative Counting Principle

## Definition

If a process breaks into a sequence of steps E₁,...,Eₘ where E₁ can occur n₁ ways, and once
E₁,...,Eₖ₋₁ have occurred Eₖ can occur nₖ ways, then the whole sequence can occur in
n₁×n₂×···×nₘ ways. The book calls this "the entire sequence of events E₁,E₂,E₃,…,Eₘ can
occur in n₁×n₂×n₃×···×nₘ different ways," and stresses that each nⱼ is counted *given* that
the prior steps already happened — the step counts don't need to be independent of each
other, only well-defined at the moment each step is reached. When the counts genuinely
don't depend on prior choices, the events are called "commuting" and the principle reduces
to a simple product.

## In the Book

Section 6.1 introduces the principle with routes between towns: five roads from A to B and
three roads from B to C combine, via ordered pairs (i,j), into 5×3=15 total routes. It then
works two contrasting examples that show the principle handles both independent and
dependent step-counts: counting four-digit numbers using only odd digits gives
5×5×5×5=5⁴, because each of the four digit positions independently has 5 choices; counting
arrangements of the five letters a,b,c,d,e gives 5×4×3×2×1=5!=120, because each position's
choice count shrinks depending on which letters were already used in earlier positions.
The book builds essentially all of Chapter 6's combinatorics — permutations, combinations,
the binomial theorem, and Sudoku-solution counts — as applications or refinements of this
one principle, alongside its counterpart, the addition principle, for counting a set by
partitioning it into disjoint cases.

## Why It Matters

This principle is the mechanism behind "how many possibilities are there," which is the
first question in cryptography (keyspace size), probability (sample space size), and
combinatorial search (branching factor). Its real teaching point is the discipline of
decomposing a complex choice into an ordered sequence of simpler choices and tracking how
each step's option count depends on what came before — the same decomposition habit used
to bound a search tree, size a password space, or estimate the states a system can reach.
