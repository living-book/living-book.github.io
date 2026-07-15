---
type: Concept
title: "Track Column for Blocked Items"
description: "A special column within a workflow step that holds items waiting on external dependencies or approvals, visible to the team but not counting toward WIP limits, enabling continuous progress on other work."
book: agile-pm-with-kanban
chapters: [2, 7]
tags: [kanban, dependencies, blocking, flow]
created: 2026-07-15
---

# Track Column for Blocked Items

## Definition

When a work item cannot advance because it's waiting for something outside the team's control—an external review, a dependency from another team, a decision from leadership—instead of keeping it in the Active column where it consumes WIP capacity and misleads the team, it moves to a special "Track" column within the same step. Items in the Track column are discussed in every daily standup to monitor progress, but they don't count toward that step's WIP limit. When the blocking condition is resolved, the item moves back to Active, taking one of the freed WIP slots.

## In the Book

Brechner describes adding a Track column to the middle of the Implement step: "Items are moved to the Track column whenever they are blocked awaiting external input." The team talks about their status daily until they're unblocked. "When a tracked item is unblocked, it moves back to the Active column as soon as a slot becomes available. The logic is that any item already in Implement has higher priority than the next item from Specify."

He also notes a "parking lot"—a special area for items blocked indefinitely, checked on every few weeks rather than daily. This prevents the team from "forgetting" items and makes it visible that something needs escalation or a decision. For critical-path items in large projects, the team might create fakes or shims to unblock themselves while waiting for the real dependency, with a task card to remove the fake once the real work arrives.

## Why It Matters

Without a Track column, blocked items waste WIP limits—you can't pull new work because a slot is consumed by something you can't progress. This forces idle capacity or overstaffing of other steps. The Track column decouples waiting from doing; the team keeps steady on items it controls while visibility on blocked work rises to whoever can unblock it (another team, a manager, a customer). The daily mention of tracked items in standup ensures they're not silently forgotten and creates social pressure to unblock them. It also makes scope clear—leadership sees which high-value work is stuck and for how long, driving real decisions instead of assumptions.

---

*related concepts: kanban-pull-system (CATALOG), integration-points (CATALOG), help-chains (CATALOG)*
