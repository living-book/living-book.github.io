---
type: Concept
title: Recidivism Rate
description: The percentage of workflow steps where a task moves backward (reopened, sent back for rework), revealing process friction and hidden rework.
book: agile-metrics-in-action
chapters: [2, 3, 9]
tags: [measurement, workflow, quality, process, rework]
created: 2026-07-12
---

# Recidivism Rate

## Definition

In a task workflow (e.g., Dev Ready → In Development → QA Ready → In QA → Done), recidivism is the rate at which tasks move backward—sent back to development from QA, or moved back to definition from development because requirements were unclear. It's calculated as: (Backward Movements / (Forward Movements + Backward Movements)) × 100.

A low recidivism rate (under 10%) suggests work is well-understood and progresses cleanly. A high recidivism rate (over 50%) reveals that tasks are repeatedly rejected or sent back for rework, a sign that initial requirements are unclear, developers misunderstand the work, or QA is finding issues late.

## In the Book

Recidivism first appears in the Blastamo case study (Chapter 2). The team tracks it alongside velocity and bugs to measure both volume and quality of work. When they see spikes in recidivism, they know work is coming back — perhaps developers didn't understand the feature or QA is catching issues that should have been prevented earlier.

Chapter 3 breaks down how to calculate and interpret it. The formula is: (B / (F + B)) × 100, where B is backward movements and F is forward movements. If a task moves forward three times but backward once, that's one task with 25% recidivism. Across a sprint, you can aggregate this to team-level trends.

The book also shows recidivism as a red flag in estimation accuracy. Chapter 7 reveals that tasks with low estimates often have high recidivism — they move backward frequently because they were underestimated or poorly understood. When the team added "recidivism > 0" as a filter to their analysis, they discovered certain task types and certain team members consistently had rework spikes, leading to coaching and process changes.

## Why It Matters

Velocity can hide rework. A team completing 40 story points might actually do 30 points of new work and 10 points of rework on previously "done" tasks. Recidivism exposes this hidden drag. It also points to specific process problems: high recidivism from development to definition means requirements are unclear (fix: better definition meetings); from QA back to development means code quality is low or testing is late (fix: earlier testing or better code review); from done back to any stage means your definition of done is wrong (fix: tighten acceptance criteria). Unlike velocity or other metrics that measure output, recidivism measures process friction directly.
