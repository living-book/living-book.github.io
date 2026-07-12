---
type: Concept
title: Work-in-Progress Limits
description: Capping how many items each stage of a workflow can hold at once, tuned empirically rather than calculated, to expose problems and stabilize flow.
book: kanban
chapters: [2, 10]
tags: [constraints, flow, empiricism, capacity]
created: 2026-07-12
---

# Work-in-Progress Limits

## Definition

A WIP limit is an agreed cap on how many items can occupy a given stage of a workflow (or be assigned to a given person, pair, or team) at one time. It is one of the five core properties of the Kanban Method, alongside visualizing workflow, measuring flow, making policies explicit, and using models to find improvement opportunities. There is no formula for the "correct" number — Anderson insists limits are chosen, observed, and adjusted, not derived: "Choose something! Choose to make progress with imperfect information and then observe and adjust. Kanban is an empirical process."

## In the Book

Chapter 10 works through concrete examples: at Microsoft's XIT team, developers and testers were limited to one item at a time (a WIP limit of three, matching headcount), following the team's existing Personal Software Process discipline. At Corbis, major-project work allowed two or three people per item with some overflow — ten people at roughly two-per-item yielded a limit around eight. Queue and buffer sizes are tuned the same empirical way: the XIT input queue was set to five (one week's throughput) under weekly prioritization, but when the team switched to on-demand prioritization, Anderson admits he should have shrunk it to one and didn't — "a reflection of my inexperience at the time." The chapter also contrasts kanban's WIP-limited-at-every-station design with Goldratt's Drum-Buffer-Rope, where only the bottleneck station is constrained and everything downstream runs unlimited (illustrated with a patrol of scouts roped together at different points). A closing warning — "Don't Stress Your Organization" — cautions that setting limits too tight in a lower-maturity organization will surface more impediments than the team can absorb, and recommends starting looser and tightening over time.

## Why It Matters

A WIP limit converts an invisible overload (everyone quietly juggling too much) into a visible, forcing constraint: when the limit is hit, the team cannot start new work and must instead resolve whatever is blocking existing work. This makes WIP limits a general lever for surfacing and prioritizing bottlenecks in any system where more starts than finishes is the default failure mode — and the book's insistence on empirical tuning over calculation is itself a transferable stance toward any policy that governs behavior under uncertainty.
