---
type: Concept
title: Testing Only Pays If It Can Change a Decision
description: Testing produces information, and information is worthless unless someone will act differently depending on what it says — otherwise, don't bother.
book: perfect-software
chapters: [1, 2]
tags: [decision-making, information-value, risk, testing, incentives]
created: 2026-07-12
---

# Testing Only Pays If It Can Change a Decision

## Definition

Testing is fundamentally an information-gathering activity, not a quality-producing or risk-eliminating one — "testing is not fixing." Its entire value depends on whether the resulting information will actually change a decision someone is prepared to make differently. If a decision-maker will ship, cancel, or continue a project regardless of what testing reveals, then testing that question is worthless no matter how rigorous it is; conversely, sometimes not knowing is organizationally or legally safer than knowing.

## In the Book

Weinberg opens with an executive under pressure from a company president, Benito, who wants a logistics system shipped; the only reliable way to reduce the risk of that decision is to gather information about what the system actually does when used — one form of testing. He walks through why testing information doesn't automatically reduce risk: it costs time and money, it can trigger project-delaying rework, and it can create legal exposure (a known, unfixed bug found in testing is worse in a lawsuit than a bug nobody ever found — "sometimes, ignorance really is (legal) bliss"). He also shows testing being paid for but not used, as when testers can't even install the software after six weeks of trying, and the manager still fails to interpret that as critical information. The chapter closes with a checklist for whether a product is even ready for test: Is there a question testing can answer? Do you want to know the answer? Will any possible outcome change your decision? If not, "why would you want to know the outcome, let alone pay for it?"

## Why It Matters

This reframes testing (and measurement generally) as decision support rather than virtue or due diligence for its own sake. It gives you a concrete filter for cutting wasted verification effort anywhere: before collecting more data, ask whether any possible result would actually change what you do next — and if the honest answer is no, the activity is theater, not information.
