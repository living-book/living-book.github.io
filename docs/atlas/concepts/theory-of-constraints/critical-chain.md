---
type: Concept
title: Critical Chain
description: A project-scheduling method that strips hidden safety time out of individual task estimates and pools it into shared buffers, defeating student syndrome, sandbagging, and bad multitasking.
book: theory-of-constraints
chapters: [2, 3, 4]
tags: [project-management, buffers, behavioral-incentives, scheduling, constraints]
created: 2026-07-12
---

# Critical Chain

## Definition

Critical Chain Project Management (CCPM) applies TOC to projects, where the constraint is not a resource but the longest chain of dependent tasks (including resource dependencies, not just technical precedence — hence "chain" rather than "critical path"). Its key move is to remove the safety time individuals bury inside their own task estimates and instead aggregate that safety into a project buffer (and feeding buffers where non-critical chains merge into the critical chain), then manage the project by watching buffer consumption rather than individual task due dates.

## In the Book

Chapter 2 diagnoses why traditional project management fails, and Chapter 3 names the specific behaviors CCPM is built to counter: student syndrome (people start a task at the last safe moment even when given extra time, named for students who only begin studying the night before an exam despite requesting an extension), sandbagging (finishing early but not reporting it, to protect future estimates or avoid extra work), and Parkinson's Law ("work expands to fill the time available," so a task finished early gets "polished" instead of handed off). Because task durations include large hidden safety margins yet those margins routinely get consumed by late starts and multitasking rather than genuine task variability, individual due dates are unreliable while the project as a whole is still overprotected. Chapter 3's worked example strips roughly half the "safe" time out of each task, reassembles the true Critical Chain via resource-leveling passes, and inserts a project buffer (about half the total safety removed) at the end plus feeding buffers wherever secondary chains merge in — then tracks execution with the same red/yellow/green buffer-penetration signal used in Drum-Buffer-Rope. Chapter 4's field report adds a further rule: limit the number of projects released into execution at once ("pipelining"), because bad multitasking across projects, not any single task's difficulty, is a major hidden cause of project delay.

## Why It Matters

Critical Chain reveals that a project's schedule risk is often mismanaged rather than irreducible: safety time hoarded locally, task by task, gets wasted by predictable human behavior (start late, don't report early finishes, polish instead of handing off), while the same amount of safety pooled at the system level actually protects the deadline. The underlying move — stop protecting every individual step and instead protect the aggregate outcome with a shared reserve — applies to any process where local slack is squandered by the incentives of the people holding it.
