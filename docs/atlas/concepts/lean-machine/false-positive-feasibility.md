---
type: Concept
title: False Positive Feasibility
description: Committing early to a single design and only later testing whether it truly works produces a false sense of confidence that is the leading cause of project failure.
book: lean-machine
chapters: [9, 10]
tags: [premature-commitment, testing, risk, decision-making, point-based-development]
created: 2026-07-12
---

# False Positive Feasibility

## Definition

In "point-based" development, a team commits to one design solution early, then runs a pass/fail test to verify it is feasible. When the test passes, the team believes the design is proven — but the test usually covers only a partial representation of real conditions, with no visibility into the margin by which it passed. As the design keeps evolving to meet new requirements, the early "pass" stops being true, and the gap surfaces late, when it is most expensive to fix. Oosterwal calls this false positive feasibility: the single biggest cause of project failure the book identifies.

## In the Book

Chapters 9–10 present this as the answer to a root-cause investigation: after ruling out "bad engineering" as the explanation for recurring late-stage design failures, Oosterwal and Ward apply a "five whys" (not a "five whos") to years of After Action Reviews and land on the same pattern every time — a team believed something was feasible, then learned late in development that it was not. The book explicitly contrasts this with set-based concurrent development, which Allen Ward advocated as the antidote: instead of committing to one point solution and testing it, carry multiple design options in parallel and let the winner emerge from real feedback, so no single premature "pass" can mislead the whole project. The Product Development Limit Curve is presented as the diagnostic that makes false positive feasibility visible after the fact — projects fail specifically when a redesign loop forced by a false positive discovery falls outside the timing the curve allows.

## Why It Matters

This names a decision-making failure mode that extends far past engineering: any pass/fail gate applied to a partial test of an early commitment can manufacture confidence that isn't earned — a hiring decision validated by one interview, a strategy "proven" by a pilot under unrepresentative conditions, a startup's business model "validated" by an early cohort. Recognizing false positive feasibility argues for either delaying commitment until tests are representative, or deliberately keeping options open (set-based) until the evidence is real.
