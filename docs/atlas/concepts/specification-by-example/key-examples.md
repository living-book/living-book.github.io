---
type: Concept
title: Key Examples
description: Concrete, realistic examples expose ambiguity and missing rules that abstract requirement statements hide, and refining them (not automating them) is what turns them into a specification.
book: specification-by-example
chapters: [2, 7, 8]
tags: [requirements, examples, ambiguity, specification, precision]
created: 2026-07-12
---

# Key Examples

## Definition

Abstract requirement statements ("make sure all correct products are displayed") create an illusion of shared understanding that concrete examples immediately break. A key example is a specific, realistic scenario — actual data, not a class of inputs — chosen to pin down one rule or edge case; a small set of them, discussed collaboratively, surfaces gaps and disagreements a paragraph of prose would hide. Raw examples from a discussion are only the starting material, though — Adzic compares them to uncut diamonds — and must be refined (given a title, stripped of yes/no answers and abstract equivalence classes, freed of implementation detail) before they count as a specification.

## In the Book

Chapter 7 walks through a running example at the fictional ACME OnlineShop: a "free delivery" rule that seems simple until the team — Barbara (analyst), David (developer), Tessa (tester) — works through concrete cases (a Manning book alone, a non-Manning book, two Manning books, a Manning book plus a fridge) and discovers a real business gap (delivery cost on bulky non-book items) that the original one-line requirement never surfaced. The chapter also reports a workshop Adzic ran with 50 people illustrating ambiguous blackjack rules from a website: six of seven teams converged on identical edge-case answers once they worked through examples, versus none beforehand. Chapter 8 then shows the refinement step on a deliberately bad payroll specification, cutting workflow narration and renaming an invented "Paycheck Inspector" concept down to a short, self-explanatory table of inputs and expected outputs — the same free-delivery rule reappears here polished into a clean example table (VIP customer, 5 books, cart contents, delivery outcome).

## Why It Matters

Any two people can agree on a vague statement while disagreeing about what it means in a specific case — abstraction is where disagreement hides. Forcing a claim, rule, or requirement down to a concrete instance ("what happens when X buys a fridge with the book?") is a cheap, fast way to discover missing rules before they become expensive rework, and it works whether the claim under test is a business rule, a policy, or a scientific hypothesis. The added lesson — that raw examples still need refining into something self-explanatory — generalizes to any brainstormed artifact: the discussion that produces material is a different activity from the editing that makes it usable later.
