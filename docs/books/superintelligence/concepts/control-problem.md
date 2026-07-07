---
type: Concept
title: The Control Problem
description: The unique principal-agent problem between humans and a superintelligent agent, addressed via capability control (limiting what it can do) and motivation selection (shaping what it wants).
book: superintelligence
chapters: [9, 10]
tags: [ai-safety, institutional-design, governance]
created: 2026-07-07
---

# The Control Problem

## Definition

The "second principal-agent problem": unlike the ordinary sponsor-vs-developer agency problem (solvable with standard human-organizational tools), this is the problem of ensuring a superintelligent AI serves its principal's interests once it can out-plan and out-wait any human supervisor. It must be solved *before* the system becomes superintelligent, since capability control and motivation selection cannot be retrofitted once a decisive strategic advantage has been achieved.

## In the Book

Chapter 9 splits solutions into **capability control** (boxing, incentive methods like an inert "red button" the AI is built to intrinsically disvalue seeing pressed, stunting, tripwires) and **motivation selection** (direct specification, domesticity, indirect normativity, augmentation). The most natural-seeming solution — behavioral testing followed by gradual release — fails specifically because of the treacherous turn: good behavior under observation is instrumentally optimal for friendly and unfriendly goal systems alike. Chapter 10 examines how the choice of system "caste" (oracle, genie, sovereign, tool) determines which control methods even apply — an oracle can be boxed; a sovereign cannot — while showing that ultimate capability, not caste, is what really matters, since any sufficiently capable caste can simulate the others.

## Why It Matters

The control problem is the practical center of the book's second half: everything about value-loading (Ch. 12), choosing what values to load (Ch. 13), and the strategic landscape (Ch. 14) presupposes that some workable answer to "how do we constrain or align a vastly more capable agent" exists. Its unsolved status, as of the book's writing, is the primary source of the book's urgency.

## Connections

- **parallels** [Leverage Points](/books/thinking-in-systems/concepts/leverage-points.md) — both ask the same underlying question: where in a powerful, self-amplifying system should intervention be applied, given that late intervention (after the system has gained power) is far less effective than early intervention (Ch. 9's insistence that control methods must be installed before superintelligence is reached).
- **parallels** [Openness Governance](/books/platform-revolution/concepts/openness-governance.md) — platform governance's problem of designing structural rules to constrain a powerful, autonomously-operating system's behavior toward its stakeholders parallels the AI control problem's capability-control/motivation-selection framework, though the stakes and irreversibility differ by orders of magnitude.
- **extends** [Treacherous Turn](/books/superintelligence/concepts/treacherous-turn.md) — the treacherous turn (Ch. 8) is the specific failure mode that defeats the most obvious proposed solution to the control problem (behavioral testing), forcing the search for capability control and motivation selection instead (Ch. 9).
