---
type: Concept
title: Proof by Refutation
description: To prove a claim, assume its negation and mechanically decompose it into simpler pieces until every branch collapses into a direct contradiction.
book: logic-and-discrete-mathematics
chapters: [3, 4]
tags: [proof-technique, formal-methods, contradiction, deduction]
created: 2026-07-12
---

# Proof by Refutation

## Definition

To prove that B logically follows from premises A₁,...,Aₙ, instead of directly reasoning
forward, assume the premises true and the conclusion B false, and try to derive a
contradiction. The book's semantic tableaux method formalizes this as a systematic search:
"the method of semantic tableaux attempts to show that there is no truth assignment that
falsifies it, which is equivalent to showing that the formulae A₁,...,Aₙ and ¬B cannot be
satisfied simultaneously." Every connective has decomposition rules — some non-branching
(A∧B true forces both A and B true), some branching (A∨B true forces a split into A-true
or B-true) — that break a formula down into its parts until either every branch closes
(hits an outright contradiction, proving the claim) or a branch survives (yielding a
counterexample).

## In the Book

Section 3.2.2's Example 3.2.3 shows the method in miniature before it's formalized: to
show p→r and q→r logically imply (p∨q)→r, the book supposes the opposite — that (p∨q)→r
is false while both premises are true — and derives that p∨q is true and r is false, then
splits into "p is true" (forcing p→r false, a contradiction) or "q is true" (forcing q→r
false, also a contradiction); since both cases collapse, no falsifying assignment exists.
Section 3.4 formalizes this into the full semantic tableaux system, attributed to Beth,
Hintikka, and later Smullyan and Fitting, with an explicit rule table for each connective
(¬, ∧, ∨, →, ↔) showing exactly how a formula's truth or falsity forces its subformulae's
truth or falsity. Chapter 4 extends the same refutation-tree method to first-order logic,
adding quantifier rules, and Section 3.6 develops clausal resolution as a related
refutation-based derivation system.

## Why It Matters

Refutation reframes "prove X" as "show ¬X is impossible" — a shift that trades an open-
ended search for a supporting argument for a closed, mechanical decomposition that
terminates in success (contradiction on every branch) or failure (a surviving branch,
which is a counterexample handed to you for free). This is the shape behind proof by
contradiction generally, behind SAT/SMT solvers and automated theorem provers, and behind
any debugging or diagnostic process that assumes "it works" and hunts for the branch where
that assumption breaks — the counterexample the search finds is often more informative
than a bare "yes, it's true" would have been.
