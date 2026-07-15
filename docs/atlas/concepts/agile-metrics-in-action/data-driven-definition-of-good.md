---
type: Concept
title: Data-Driven Definition of Good
description: Using historical patterns in team data to establish objective baselines for "good" performance, rather than relying on opinions or external benchmarks.
book: agile-metrics-in-action
chapters: [7]
tags: [measurement, data-analysis, objectivity, performance, baseline]
created: 2026-07-12
---

# Data-Driven Definition of Good

## Definition

Rather than debating what "good" performance looks like or adopting an external benchmark that may not fit your team's context, analyze your own historical data to discover what good actually looks like for you. Look at releases or time periods the team considers successful and reverse-engineer the metrics that made them successful, then use those as targets for future work. Conversely, examine periods when things went poorly and identify what those data signatures looked like — these become red flags to watch for.

## In the Book

Chapter 7 contrasts two releases from the same team. One release looked good during development — average task completion time was 1 day, which seemed excellent — but had a two-month support tail of bug fixes afterward. Another release had an average development time of 4 days (much longer) but shipped cleanly with only a brief, planned support phase.

By analyzing the data around both releases (development time, recidivism rate, number of tasks per release, support duration), the team discovered that faster development time wasn't actually good — it correlated with more bugs and rework. The four-day release was the model to replicate.

The chapter also shows this working in reverse: when developers saw flat-line estimates over time, the question isn't "are we estimating poorly?" but rather "what thresholds in the data separate good estimation from bad?" The team queried for all tasks estimated at 3 points but taking 5+ days to complete, found tags on those tasks, and discovered that estimates were low specifically for tasks that moved backward in the workflow — that backward movement was the data signature of a problem, so they added it to their dashboard.

## Why It Matters

External benchmarks ("industry standard lead time is X days") often don't account for your codebase complexity, team size, or deployment frequency. Asking managers what they think is good leads to subjective targets that teams game. By grounding "good" in your own data, targets become achievable and honest, improvement becomes measurable, and the team stops wasting energy on the metrics that actually predict success for their context — whatever that context is. It also surfaces the hidden trade-offs: you can't optimize for speed AND simplicity AND low bugs — the data will tell you which two matter most for your team.
