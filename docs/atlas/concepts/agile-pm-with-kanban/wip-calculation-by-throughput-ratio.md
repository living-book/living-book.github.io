---
type: Concept
title: "WIP Calculation by Throughput Ratio"
description: "A formula-based method for setting initial WIP limits by measuring how many items each step completes per unit time, then balancing limits so all steps match the slowest step's throughput."
book: agile-pm-with-kanban
chapters: [2, 3]
tags: [kanban, wip-limits, throughput, measurement]
created: 2026-07-15
---

# WIP Calculation by Throughput Ratio

## Definition

Rather than guessing WIP limits or using rules of thumb, Brechner provides a specific formula: measure the average throughput (items completed per unit time) for each workflow step, identify the slowest step, then set that step's WIP limit to the number of people on that step plus 50%, and use ratios to calculate limits for other steps so they all process the same number of items per unit time. This ensures work flows smoothly without queuing up at bottlenecks or starving downstream steps.

## In the Book

Brechner shows a concrete example from an Xbox team: analysts specify roughly six items per month, developers implement two items per month (the slowest step), and testers validate roughly three items per month. The slowest step is implementation at two items per month. With three developers implementing, the team's throughput is 2 × 3 = 6 items per month. To match that throughput: one analyst (6 items/month ÷ 6 items/month = 1), three developers (6 ÷ 2 = 3), and two testers (6 ÷ 3 = 2). Adding 50% as buffer: WIP limits become 2 for Specify, 5 for Implement, 3 for Validate.

The formula works because it answers: "How many people do we need at each step to match the output of the slowest step?" Then the WIP limit is that number plus a buffer. This creates steady flow—if implementers are maxed out (5 items active or done), you can't specify more items and should help implementation instead. The limits are starting values, tunable as conditions change, but they ground the initial setup in observable data rather than intuition.

## Why It Matters

WIP limits chosen by formula prevent the two opposing failure modes: limits too high, which let work pile up and hide problems, and limits too low, which starve downstream steps. By pegging limits to the actual capacity and speed of each step, you match supply to demand automatically. This means work flows continuously instead of arriving in destructive bursts. It also surfaces bottlenecks immediately—if implementation is the slowest step and it hits its WIP limit, the analyst naturally knows to go help implementation rather than specify more work that will just queue. The 50% buffer accounts for variability in work size and team composition without requiring constant tweaking.

---

*related concepts: wip-limits (CATALOG), queues-as-root-cause (CATALOG), batch-size-economics (CATALOG)*
