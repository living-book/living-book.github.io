---
type: Concept
title: "Task Size Consistency in Breakdown"
description: "Breaking down large work items into similarly-sized small tasks (ideally 1-5 days each) so that cycle time becomes predictable and WIP limits can be tuned to actual capacity."
book: agile-pm-with-kanban
chapters: [2, 3]
tags: [kanban, task-breakdown, batch-size, predictability]
created: 2026-07-15
---

# Task Size Consistency in Breakdown

## Definition

The first step in Brechner's workflow is called "Specify" or "Breakdown"—its job is to take large, variable-sized backlog items and decompose them into smaller, consistently-sized tasks, each of which can be finished in one to five days. This is done with the team's input as items enter the Specify step, not upfront for the whole backlog. The consistency of task size is more important than the exact size—if all tasks are 3-5 days, the completion rate becomes predictable; if they range from a few hours to three weeks, forecasting and WIP tuning become impossible.

## In the Book

Brechner illustrates with an example: a large feature like "Visiting Disneyland" gets broken into tasks like "See Adventureland," "See Frontierland," "See Fantasyland," "See Tomorrowland"—each a similar scope and duration. The Specify done rule explicitly requires: "All items broken down into tasks that can be finished in less than a week each." When estimating with the team later, they estimate task breakdown (how many tasks does this feature need), not hours, because tasks are the unit of work that flows through the process.

A key subtlety: the WIP limit for the Specify step applies to the original backlog items (e.g., 2 features being specified), not the breakdown tasks created from them. So one backlog item might be broken into four tasks, but the Specify step still shows 2 items active with the task cards grouped visually beneath. Once the tasks leave Specify, each task counts individually toward Implementation's WIP limit. This accounting ensures consistency—the team doesn't face a sudden explosion of work items.

## Why It Matters

Consistent task size is the foundation of predictability. If tasks range wildly, a task completion rate of "5 per day" is meaningless—five small tasks are not the same as five large ones. But with consistent sizing, 5 tasks per day is stable and defensible to leadership. It also enables WIP limits to work properly; a limit of 5 for Implementation only makes sense if you know what a unit is. Small, consistent tasks also reduce the risk of individual items getting lost or stuck—if a 3-day task disappears from the board, it's noticed immediately; a 3-week task might sit stuck for days without visible urgency. The breakdown happens incrementally as items enter the workflow, so the team doesn't face a planning nightmare of sizing the entire backlog upfront, only what's immediately needed.

---

*related concepts: batch-size-economics (CATALOG), wip-limits (CATALOG), last-responsible-moment (CATALOG)*
