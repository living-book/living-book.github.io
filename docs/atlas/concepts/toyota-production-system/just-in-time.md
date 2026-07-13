---
type: Concept
title: Just-in-Time
description: Each process receives the exact part, in the exact quantity, at the exact time needed, by having later processes pull from earlier ones instead of being pushed to.
book: toyota-production-system
chapters: [1]
tags: [pull-systems, flow, inventory, waste, synchronization]
created: 2026-07-12
---

# Just-in-Time

## Definition

Just-in-time means the right parts reach the assembly line at the moment they are needed and only in the amount needed, so a fully realized flow approaches zero inventory. Ohno achieves this not by scheduling every process forward from raw material to finished car, but by reversing the direction of information: a later process goes to an earlier process and withdraws only what it needs, when it needs it, and the earlier process makes only enough to replace what was withdrawn.

## In the Book

Ohno introduces just-in-time as one of the "two pillars" of the Toyota production system in Chapter 1, alongside autonomation. He describes arriving at the idea by inverting the conventional material flow: instead of parts pushing forward from an early process toward final assembly according to a central plan, he imagined the assembly line pulling parts backward from each preceding process, one step at a time. This reversal is what produced kanban — the signboard that tells an earlier process what was withdrawn and how much to replace — but the book is explicit that kanban is only "the means" or "tool" for realizing just-in-time, not the idea itself. Ohno also uses a baseball analogy (Chapter 2): just-in-time is the practiced teamwork of players executing a coordinated play, while autonomation is the individual skill of each player. He is candid that applying just-in-time to a product built of thousands of parts across countless processes is "extremely difficult," and that conventional management methods do not work for it — the whole system had to be redesigned around synchronized withdrawal rather than forecasted push.

## Why It Matters

Just-in-time reframes a coordination problem: instead of every upstream station guessing correct output levels from a forecast and pushing on faith, the coordination signal comes from the one place that actually knows demand — the point of consumption — and propagates backward through the chain. This collapses the need for large buffers between steps, but it also removes the safety margin those buffers used to hide: any variability, defect, or breakdown anywhere in the chain now surfaces immediately instead of being absorbed by inventory. The concept generalizes to any multi-stage system (staffing, software delivery, supply chains) where pulling from real downstream demand, rather than pushing from an upstream forecast, trades buffer-based slack for tighter synchronization and faster exposure of problems.
