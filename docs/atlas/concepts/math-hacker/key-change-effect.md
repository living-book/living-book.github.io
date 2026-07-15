---
type: Concept
title: The Key Change Effect
description: The digit pattern produced by multiplying or dividing two numbers is invariant; decimal points and trailing zeroes are separate bookkeeping laid on top of it afterward.
book: math-hacker
chapters: [4]
tags: [invariance, arithmetic, decimals, scale, mental-models]
created: 2026-07-12
---

# The Key Change Effect

## Definition

`43 x 23`, `4.3 x 23`, `0.43 x 2.3`, and `430 x 230` all produce the same core
digit sequence, `989`, just written at different scales. Carson names this the
"Key Change Effect," after the musical device where a song is repeated in a
different key — different notes, same melody. The claim is that decimal
places and zeroes never change *what* the digits are, only *where the
decimal point or magnitude sits*; you can strip them out, do the multiplication
or division on the bare digits, and reattach the scale afterward as a separate,
mechanical accounting step.

## In the Book

The concept is introduced in the Decimals chapter by comparing `9.89` and
`0.0989` and pointing out that "989" survives in both — the reader is told
they already know how to multiply any two numbers, because the answer is
always the same underlying digits, with decimal-place bookkeeping layered on.
The book then extends this in "Reverse Situation" to trailing zeroes: `430 x
230` is worked as "989, plus 2 zeroes" giving `98,900`, and `14,000,000 x
210,000` as "294, plus 10 zeroes." A mixed case — decimals and zeroes together,
`0.43 x 230,000` — is handled by adding the zeroes first, then inserting the
decimal places. The book explicitly ties this to Standard Form and to division
of decimals, noting that division applies the same invariant-digits idea but
subtracts decimal places instead of adding them.

## Why It Matters

Separating "what the digits are" from "what scale they're at" turns a family
of operations that feel like they require memorizing separate rules (decimal
multiplication, decimal division, scientific notation, unit conversion) into
one operation (work the bare digits) plus one bookkeeping step (track the
scale). The same move generalizes to significant-figure arithmetic, unit
conversion, and floating-point representation — anywhere a value factors
cleanly into an invariant "shape" and a separate scale or reference frame that
can be tracked independently and reattached at the end.
