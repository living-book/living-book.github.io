---
type: Concept
title: Operations as Compressed Repetition
description: Multiplication and division are not separate primitive operations to memorize but shorthand for repeating a simpler operation — addition or subtraction — until you stop.
book: math-hacker
chapters: [1, 2]
tags: [arithmetic, mental-models, decomposition, pedagogy, mechanism]
created: 2026-07-12
---

# Operations as Compressed Repetition

## Definition

Multiplication is repeated addition: `3 x 5` means "add 5, three times." Division
is repeated subtraction: `6 / 2` means "how many times can I subtract 2 from 6
before I hit zero." Carson calls these the First and Second Rules of Maths and
treats them as covering roughly 80% of arithmetic between them — not as two
unrelated operations with their own rulebooks, but as one operation (adding to
a pile, or taking away from a pile) applied repeatedly.

## In the Book

Chapter 1 opens by forbidding the reader from defining multiplication using the
words "multiply," "times," "product," or "by" — forcing them to discover that
`3 x 5 = 5 + 5 + 5` themselves. From this the book derives a practical
consequence: since order doesn't change the answer (`3 x 5 = 5 x 3`), you should
always add the *smaller* number the *larger* number of times, e.g. turn
`14 x 7` into `7 x 14` because seven additions beat fourteen. The same move is
made for division: the book demonstrates how a five-year-old sharing six coins
between two people ("one for you, one for me...") is doing subtraction —
`6 - 2 = 4`, `4 - 2 = 2`, `2 - 2 = 0` — three subtractions, hence `6 / 2 = 3`. It
stops at zero because division is also sharing: the pile runs out. The book
explicitly states this repeated-subtraction/repeated-addition pair, plus the
reversibility rule covered separately, accounts for the great majority of what
"doing maths" actually is.

## Why It Matters

Once an operation is understood as a compressed version of a simpler one, you
no longer need to memorize it as an independent fact table — you can always
fall back to the primitive (add repeatedly, subtract repeatedly) to check or
derive an answer, and you can optimize the compression itself (fewest additions,
stopping condition) once you see what it's actually doing. The general move —
find the primitive repeated operation hiding inside a compound one — applies
anywhere a "black box" procedure can be unpacked into a loop over something
simpler: it turns "memorize the rule" into "derive the rule whenever needed."
