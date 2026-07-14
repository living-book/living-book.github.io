---
type: Concept
title: Percent Complete and Accurate
description: A quality metric attributed to the process that produced flawed work, not the one that caught it — and one that compounds multiplicatively across a value stream.
book: value-stream-mapping
chapters: [3, 4]
tags: [quality, measurement, root-cause, metrics, waste]
created: 2026-07-12
---

# Percent Complete and Accurate

## Definition

Percent complete and accurate (%C&A) is obtained by asking each downstream customer what percentage of the time they receive work that's "usable as is" — no corrections, no missing information, no clarification needed. If a department reports having to fix or clarify incoming work 30 percent of the time, the *upstream* process gets scored at 70 percent, because the metric is written on the Post-it of whoever produced the defect, not whoever caught it. Multiplying the %C&A of every process block in sequence yields the "Rolled %C&A" — the true odds that a unit of work makes it through the entire value stream without anyone anywhere needing to touch it up.

## In the Book

Chapter 3 calls %C&A "the most transformational metric we've encountered," because unlike lead time or process time it exposes invisible rework. The book gives a worked example (Figure 3.7): Process 4's output is reworked 25 percent of the time by downstream Process 5 (so 75 percent %C&A) and 50 percent of the time by a different downstream Process 7, who catches a different set of defects that Process 5 missed — multiplying (0.75 × 0.50) × 100 gives Process 4's true output quality as 37.5 percent, far worse than either downstream report alone suggested. Rolled across a whole value stream — (%C&A)₁ × (%C&A)₂ × (%C&A)₃ × ... — the book reports this number is routinely 1 to 10 percent in office and service value streams, meaning 90 to 99 percent of work gets reworked somewhere along the line before it reaches the customer. The authors call this discovery, like the Activity Ratio (process time divided by lead time), "sobering" — and deliberately so: assessing %C&A for each process is uncomfortable for the people doing the work, but attributing the defect to its source rather than its symptom is what lets the team target root causes with countermeasures instead of applying a Band-Aid at the point where the error was merely discovered.

## Why It Matters

Most quality complaints surface at the point of discovery, which is rarely the point of origin — so organizations chronically fix the wrong step. Scoring quality against the producer rather than the discoverer, and then multiplying that score across every hop in a chain, turns a vague sense that "things get reworked a lot" into a specific number that reveals how much of a system's apparent capacity is secretly consumed by invisible correction loops.
