---
type: Concept
title: "Task Completion Rate Forecasting"
description: "Using measured task completion rate, task add rate, and current task estimate to forecast project completion dates via Little's Law, updating estimates as conditions change."
book: agile-pm-with-kanban
chapters: [3]
tags: [kanban, forecasting, measurement, estimation]
created: 2026-07-15
---

# Task Completion Rate Forecasting

## Definition

Instead of upfront estimates made at the start, Brechner measures three running metrics after the team is working: Task Completion Rate (tasks completed per day), Task Add Rate (new tasks added minus removed per day), and Current Task Estimate (pending tasks plus active tasks). The forecast formula is CTE ÷ (TCR – TAR). This derives from Little's Law and updates regularly as the team's actual productivity and backlog churn become known.

## In the Book

Brechner provides an example spreadsheet tracking two to four weeks of data. Say the team completes 5 tasks per day on average and adds 1 new task per day due to change requests. With 30 tasks still pending or active, the formula is 30 ÷ (5 – 1) = 7.5 days remaining. As time passes, these numbers change—if the team hits a bottleneck, TCR drops; if scope creeps, TAR rises; if work gets clearer, items break down differently. By recalculating monthly or weekly, the forecast stays current without requiring constant re-estimation of individual items.

The key insight is that task completion rate is more stable than individual item estimates because it averages across many tasks. A team that averages 3-day tasks, when spread across multiple people and processes, produces a fairly consistent completion rate. This rate, combined with the add rate, tells you instantly whether you're ahead or behind—if TAR exceeds TCR, you're never finishing; if they're equal, you're treading water; if TCR exceeds TAR, you're making progress. The burndown chart (a cumulative flow diagram) visualizes this: pending and active task curves going down means you're winning.

## Why It Matters

This approach replaces guessing with observation. No need for Planning Poker estimates of every item if the completion rate is known; leadership gets a forecast that updates as reality unfolds rather than a fixed plan that drifts. It also makes the cost of scope change immediately visible—leadership sees that adding 5 new tasks per day pushes completion out by weeks, which clarifies trade-offs. The forecast is honest about variability and dependencies, since it's based on what the team actually achieved, not optimistic assumptions. This builds trust with stakeholders because estimates are defensible and improve over time.

---

*related concepts: cost-of-delay (CATALOG), batch-size-economics (CATALOG), last-responsible-moment (CATALOG)*
