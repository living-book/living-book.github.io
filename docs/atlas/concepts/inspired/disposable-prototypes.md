---
type: Concept
title: Disposable Prototypes
description: Fake, throwaway simulations built at the lowest fidelity that will still answer the question, used to learn before committing to real engineering.
book: inspired
chapters: [44, 45, 46, 47]
tags: [prototyping, experimentation, feedback, risk-reduction, iteration]
created: 2026-07-12
---

# Disposable Prototypes

## Definition

A prototype, in Cagan's usage, is anything built to learn something at an order of magnitude less time and effort than building the real product — and it is explicitly not meant to survive. A user prototype is "smoke and mirrors... there is nothing behind the curtain": entering a credit card on a prototype e-commerce checkout does not actually charge anyone. A feasibility prototype is deliberately quick-and-dirty throwaway code, written by an engineer to answer one narrow technical question, with no user interface or error handling. In both cases the prototype's fidelity — how realistic it looks or behaves — is chosen to match the specific risk being tested, never maximized for its own sake.

## In the Book

Chapter 45 ("Principles of Prototypes") states the core rule: every form of prototype should take at least an order of magnitude less time than the eventual product, and its purpose is to tackle one or more of the four risks — value, usability, feasibility, or business viability — during discovery. Chapter 46 works through the feasibility prototype in detail: engineers write throwaway code, typically in a day or two, purely to determine whether a technical approach (an unfamiliar algorithm, a legacy system, a new third-party dependency) will actually work, and this is explicitly discovery work, not delivery work, done before any commitment to build. Chapter 47 covers the user prototype, describing low-fidelity interactive wireframes at one end of the spectrum and high-fidelity simulations that are "very real" but not live at the other — for example, a mountain-bike search prototype that always returns the same canned results, which is useless for testing search relevance but perfectly adequate for testing the overall shopping experience.

A recurring lesson-learned throughout these chapters is that novice product people go wrong by either skipping the prototype and skipping straight to building, or by over-investing in fidelity the test didn't actually need.

## Why It Matters

The value of a prototype comes entirely from how cheap it is to throw away — a prototype that took real engineering effort to build creates sunk-cost pressure to ship it regardless of what it teaches you. Matching fidelity to the specific question being asked, rather than to how "finished" the artifact looks, is what keeps the cost of learning low enough that a team can afford to be wrong most of the time. This is a general answer to the problem of testing an idea before committing real resources to it: build only enough of the thing to falsify or confirm the one question you're actually asking, and build it in a form nobody will feel obligated to keep.
