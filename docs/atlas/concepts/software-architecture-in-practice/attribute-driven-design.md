---
type: Concept
title: Attribute-Driven Design
description: An iterative design method that recursively picks a system part, marshals its architecturally significant requirements, then generates and tests a design against them.
book: software-architecture-in-practice
chapters: [17]
tags: [design-method, iteration, decomposition, quality-attributes, generate-and-test]
created: 2026-07-12
---

# Attribute-Driven Design

## Definition

Attribute-Driven Design (ADD) is a recursive design loop: pick a part of the system still needing design, gather the architecturally significant requirements that apply to that part, generate a design hypothesis for it (from a pattern, a framework, a domain decomposition, or a checklist), and test that hypothesis against the ASRs, quality attribute checklists, and formal analysis. Repeat on the next part until either the ASRs are satisfied or the design budget runs out. The output is never a fully detailed architecture — it's an architecture whose major approaches have been chosen and vetted, workable enough to hand to implementation teams while refinement continues.

## In the Book

Chapter 17 frames the "generate and test" loop as the core engine beneath ADD, borrowed explicitly from decision-making under uncertainty: form a hypothesis, apply the cheapest available tests (the design checklists from Chapters 5–11, the analysis techniques of Chapter 14, and the ASRs themselves), and only then decide whether to accept the hypothesis or generate a better one. The chapter is candid about non-convergence: if a satisfactory design isn't found within budget, the architect either proceeds with the best hypothesis and relaxes the unmet ASRs, argues for more design budget, or — if all unmet ASRs are critical — recommends the project not proceed. ADD deliberately does not wait for complete requirements before starting, because requirements keep arriving throughout a project; it only requires a known set of ASRs to begin the first iteration, with the caveat that later ASR changes can force rework "under any design method, not just ADD."

## Why It Matters

ADD is a template for how to make committed, structural decisions under requirements that are known to be incomplete — decompose into a manageable part, gather only the constraints that actually bind that part, generate a candidate, test it against the cheapest checks available, and move on. It also names the honest failure mode most planning methods dodge: sometimes the tests keep failing within the available budget, and the right move is to relax the requirement, not to keep iterating indefinitely or to pretend the design succeeded. That combination — recursive scoping plus an explicit stopping rule that can end in "this can't be built as specified" — generalizes past software to any design process working against a fixed budget and a growing requirements set.
