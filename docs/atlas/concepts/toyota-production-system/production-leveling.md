---
type: Concept
title: Production Leveling
description: Smoothing output at the final process so upstream demand arrives evenly rather than in spikes — because a pull system transmits every downstream fluctuation straight upstream, amplified.
book: toyota-production-system
chapters: [1, 2]
tags: [variability, flow, scheduling, synchronization, capacity]
created: 2026-07-12
---

# Production Leveling

## Definition

Production leveling (also called load smoothing) means deliberately lowering the peaks and raising the valleys of output at the final assembly line — "mountains should be low and valleys should be shallow" — so that every process feeding it experiences steady, predictable demand instead of erratic spikes. Ohno treats it as a necessary precondition for kanban to work at all, not an optional refinement.

## In the Book

Ohno explains in Chapter 2 why leveling matters mechanically: under the kanban system, the earlier process must keep enough manpower and equipment on hand to satisfy whatever the later process withdraws. If the later process's withdrawals fluctuate wildly in time and quantity, the earlier process needs proportionally more excess capacity just to keep up — and because Toyota's kanban chain runs through outside cooperating firms as well as internal processes, any fluctuation at the final assembly line propagates backward and is felt by every supplier in the chain. He traces the origin of the idea to a Five Whys chain: asking "why can't we make this part using just-in-time?" surfaced the answer that an earlier process made parts so fast no one could tell how many were made per minute — from which "the idea of production leveling developed." The book also documents that leveling gets harder as product variety increases: with Toyota producing well over 200,000 cars a month across near-infinite combinations of body type, engine, transmission, and color, achieving zero fluctuation at final assembly is acknowledged as extremely difficult, requiring finer leveling (mixing sedans and other models within the same line) to hold the ideal.

## Why It Matters

A pull system's efficiency depends on treating variability as a first-class problem, not an inconvenience to absorb with buffers: any spike at the point of final demand doesn't stay local, it ripples backward through every linked process, each of which must carry extra capacity just to survive the swings. Leveling attacks this at the source by smoothing the signal itself, rather than asking every upstream link to individually absorb noise it didn't create. The same dynamic recurs in any pull-based or just-in-time-coupled system — staffing rosters, service capacity, distributed software pipelines — where an unsmoothed spike at the front of a chain gets amplified, not dampened, as it travels backward through dependent stages.
