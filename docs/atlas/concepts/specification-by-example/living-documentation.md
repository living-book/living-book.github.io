---
type: Concept
title: Living Documentation
description: Documentation built from executable specifications that stays automatically in sync with the system, because a failing test reveals drift immediately.
book: specification-by-example
chapters: [2, 3, 11]
tags: [documentation, feedback-loops, maintenance, trust, knowledge-management]
created: 2026-07-12
---

# Living Documentation

## Definition

Living documentation is a body of knowledge about what a system does, built from executable specifications that are validated automatically and continuously. Unlike prose documentation, it cannot silently go stale: if the specification and the system diverge, a test fails and the divergence is caught immediately. Adzic frames it as the long-term payoff of Specification by Example, distinct from the shorter-term benefit of catching regressions — "if specifications with examples were pages, the living documentation system would be the book."

## In the Book

Chapter 3 contrasts two ways of framing the practice: the acceptance-testing-centric model (ATDD), which values catching functional regressions, and the documentation-centric model, which Adzic argues delivers the deeper long-term value. He grounds this in interviews with teams five-plus years into the practice: Tim Andersen at Iowa Student Loan says he trusts only documentation that "is exercised" — i.e., automatically validated; Andrew Jackman describes the Sierra team at BNP Paribas answering support questions by sending a link to a test result instead of a Word document; Lisa Crispin at ePlan Services describes debugging a loan-interest discrepancy by reading the FitNesse test rather than a requirements doc. Adzic contrasts this with "system archeology" — Christian Hassa's term for reverse-engineering business rules out of legacy source code when no one remembers why the system does what it does. Chapter 11 covers how this documentation stays usable over time: organizing specifications by business process or functional area rather than by story, evolving a shared domain language, and merging new specifications into the existing hierarchy as features are built (illustrated with the running "free delivery" example being merged into the broader delivery-rules documentation).

## Why It Matters

Most organizational knowledge decays because nothing forces it to be checked against reality — a wiki page or requirements doc can be wrong for years without anyone noticing. Living documentation inverts the incentive: staying wrong is expensive (a failing build) and staying current is nearly free (an automated check). The pattern generalizes past software to any domain where you'd otherwise rely on a document that "isn't entirely correct" — the fix is to attach an automatic, frequent check to the artifact you want people to trust, rather than trusting people to keep it updated.
