---
type: Concept
title: "Done Rules: Enforcing Quality Upstream"
description: "Step-specific done rules that define completion criteria and prevent incomplete work from advancing, driving quality checks into earlier stages."
book: agile-pm-with-kanban
chapters: [2, 5, 8]
tags: [kanban, quality, workflow, done-criteria]
created: 2026-07-15
---

# Done Rules: Enforcing Quality Upstream

## Definition

A "done rule" is a set of step-specific criteria that must be met before a work item can be moved from one workflow step to the next. Each step in the Kanban board has its own rule, team-defined and publicly posted, that governs when that step's work is genuinely complete. The defining feature is the two-column structure within each step—an Active column and a Done column—where items must pass the done rule before moving to the Done column, creating a hard stop before advancing.

## In the Book

Brechner emphasizes that the two-column structure "may seem excessive, but it makes all the difference." His Xbox team defined specific done rules for Specify, Implement, and Validate steps. For example: the Specify done rule required all items be broken down into tasks finishable in less than a week each with quick specs completed; the Implement rule required code review, unit tests, static analysis clean, checked in, acceptance tests passing, and customer documentation complete; the Validate rule required deployment to production and real customer testing with all issues resolved.

The core mechanism is that done rules are not prescribed by management or consultants—the team defines them together, committing to follow them. This prevents lazy or careless team members from moving incomplete work downstream and hiding its true state. When someone tries to move a card, peers ask questions: "How many customers tried this?" "Where's the code review?" The rules stay posted at the bottom of the signboard as a constant, visible standard that the team holds each other accountable to.

Brechner notes this is distinct from just having a Definition of Done (a single list); instead, each step has its own context-specific criteria, and the two-column structure makes the check explicit and mandatory. Because items in the Done column still count toward WIP limits (except the final step), a team that's overwhelmed at the next step naturally can't pull more work forward even if the prior step has its done column full.

## Why It Matters

Without step-specific done rules, quality slides downstream where it's most expensive to fix—late in validation or post-release. Because the rules are publicly visible and team-defined, they make quality a team responsibility, not an inspector's job. The two-column structure prevents the common mistake of moving an item to the next step the moment it's done with the current step, which masks whether the next step is ready to receive it and obscures the distinction between "finished here" and "ready for there." By putting quality gates at every step, teams catch defects days or weeks earlier, when they're still in the developer's mind and cheap to fix.

---

*related concepts: wip-limits (CATALOG), kaizen-culture (CATALOG), done-done (Learning Agile)*
