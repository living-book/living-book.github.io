---
type: Concept
title: Set-Based Development
description: Communicate constraints instead of proposed choices, and carry multiple design options forward in parallel until the best one becomes evident from real feedback.
book: lean-software-development
chapters: [2]
tags: [design, constraints, parallelism, uncertainty, communication]
created: 2026-07-12
---

# Set-Based Development

## Definition

Point-based development picks one solution early and iterates it toward acceptability, a process that can loop indefinitely because each party is reacting to a specific proposed choice. Set-based development instead has each party communicate their constraints up front, and a solution is selected — or emerges — from the intersection of everyone's constraints. Communicating constraints instead of choices requires less back-and-forth and converges faster, because it conveys far more information per exchange.

## In the Book

The chapter opens with the scheduling-a-meeting analogy — proposing one time and haggling (point-based) versus everyone stating their availability constraints so a workable slot falls out immediately (set-based) — then grounds the pattern in Durward Sobek's 1997 dissertation comparing Toyota and Chrysler product development. Toyota's engineers maintain and exchange checklists of manufacturability constraints (e.g., how sharply a body panel can be stamped) rather than sending finished style proposals back and forth; a styling engineer designs directly against a graph of known limits instead of waiting for after-the-fact rejection. Toyota also runs literal set-based development on vehicle programs: exploring far more concepts, prototypes, and clay models at once than competitors, and fixing final specs to suppliers much later than the industry norm — a practice Ward, Liker, Cristiano, and Sobek call "the second Toyota paradox," where delaying decisions produces cars faster. The book then translates this to software through three sidebar cases: a medical-device manager who runs a half-dozen prototype options through one iteration before narrowing, an enterprise team that built on three candidate technical platforms simultaneously until the right one became obvious near the end, and a web-design consultant who resolves usability disputes the same way.

## Why It Matters

When you don't yet know enough to choose correctly, forcing an early single choice doesn't create certainty — it just hides the uncertainty inside a commitment that's expensive to undo. Set-based development gives you a concrete alternative: keep several live options and let real information (constraints, prototypes, feedback) narrow the field, rather than debating hypothetical merits of options nobody has tested. It works precisely because it changes what's communicated — constraints compress into a shared representation everyone can check against, where competing point proposals just multiply.
