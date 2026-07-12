---
type: Concept
title: Flow Efficiency
description: The ratio of time work spends being actively worked on versus waiting — a hidden-waste metric that rises as work-in-progress grows, independent of how fast any single step runs.
book: project-to-product
chapters: [4]
tags: [queuing, work-in-progress, waste, measurement, throughput]
created: 2026-07-12
---

# Flow Efficiency

## Definition

Flow Efficiency is the proportion of a flow item's total elapsed time (from
acceptance into the value stream to delivery) that it was actually being worked on,
as opposed to sitting in a wait state. It is built from two other metrics: **Flow
Time** (customer-centric wall-clock duration from acceptance to done, distinguished
from Lean manufacturing's "lead time" and "cycle time") and **Flow Load** (the count
of flow items actively in progress at once — the value stream's work-in-progress,
or WIP). The mechanism connecting them is queuing behavior: as Flow Load rises,
items spend more time waiting for a free resource, Flow Efficiency drops, and — per
Reinertsen's and Goldratt's work on overutilization — pushing a resource toward 100%
utilization is exactly what causes queue times, and therefore Flow Time, to blow up.

## In the Book

Kersten distinguishes Flow Time sharply from the DevOps-community habit of using
"lead time" loosely (e.g., "code commit to deploy") — that is actually cycle time,
a developer-centric measure of one stage, not the customer-centric, wall-clock
measure the Flow Framework requires. Flow Time is derived from four MECE flow
states (new, waiting, active, done) built to generalize across the fifty-five
different Agile/DevOps/issue-tracking tools observed in the 308-organization
toolchain study, and it lets flow items skip stages entirely — a high-severity
incident can be fast-tracked straight to a development backlog, bypassing design and
prioritization, something a physical production line cannot do. The book then builds
Flow Load explicitly as "work in a pipe": the number of items between acceptance and
completion, a leading indicator that predicts future degradation in Flow Time and
Flow Velocity before it happens. Flow Efficiency is the payoff metric: low efficiency
means a value stream is mostly generating queue time, not delivery time, and because
it's based on Flow Time (not cycle time) it captures waiting both upstream and
downstream of development — for example, a feature stalled because designers are
tied up elsewhere shows up as reduced flow efficiency even though no developer is
"blocked" in the conventional sense.

## Why It Matters

This gives a way to detect waste that is invisible if you only measure how fast
individual steps run — a system can have every station performing quickly and still
be dominated by waiting, because the waiting happens *between* stations, in the
handoffs and queues that per-step metrics don't see. It's the software-delivery
instance of a general queuing-theory result (utilization near capacity causes queue
times to explode) that shows up identically in hospital emergency rooms, call
centers, and highway traffic — anywhere multiple items compete for a shared,
finite-capacity resource, driving that resource toward full utilization is the thing
that destroys throughput, not the thing that maximizes it.
