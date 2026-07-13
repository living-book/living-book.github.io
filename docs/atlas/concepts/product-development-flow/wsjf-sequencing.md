---
type: Concept
title: Weighted Shortest Job First
description: Sequence work by dividing each job's cost of delay by its duration, not by FIFO, ROI, or the longest/shortest job alone — the mathematically optimal rule when both vary.
book: product-development-flow
chapters: [7]
tags: [scheduling, prioritization, cost-of-delay, queueing]
created: 2026-07-12
---

# Weighted Shortest Job First

## Definition

When jobs differ in both duration and cost of delay, Reinertsen shows the economically
optimal sequencing rule is to prioritize by cost of delay divided by duration — weighted
shortest job first (WSJF). This generalizes two simpler special cases: when delay costs are
equal across jobs, do the shortest job first (SJF) to avoid the "convoy effect" where one slow
job delays a queue of fast ones behind it; when durations are equal but delay costs differ, do
the highest cost-of-delay job first (HDCF).

## In the Book

Chapter 7 builds WSJF through three principles (F15–F17), each illustrated with a
cumulative delay-cost diagram: processing jobs in a 1–2–3 order (shortest first) produces
a smaller total shaded "delay cost" area than a 3–2–1 order, because delaying many short
jobs behind one long one compounds their collective wait. The chapter names this the
convoy effect, comparing it to one slow car on a narrow road delaying every car behind it.
F17 combines both factors into the single WSJF priority score and calls it "the most complex
situation and the most common one" in real product development, where jobs vary in both
dimensions simultaneously. Reinertsen then contrasts WSJF against the sequencing rules
companies actually use: prioritizing by ROI alone (which ignores how sequence changes
delay costs — the book notes overall portfolio ROI adjusted for delay cost matters more than
any single project's ROI), plain FIFO (dangerous once delay costs differ, likened to an
emergency room that ignores triage), and Critical Chain.

## Why It Matters

WSJF converts "how should we sequence this backlog" from a debate about competing
priorities into an arithmetic sort — divide cost of delay by duration, rank descending — that
any team with the two inputs can run without escalating to management. It later became
the standard prioritization formula in the SAFe agile framework, but the underlying insight
generalizes past software backlogs to any queue where items differ in both how expensive
delay is and how long they take to clear: triage, scheduling, and portfolio sequencing all
reduce to the same rule once you accept that both variables matter and interact.
