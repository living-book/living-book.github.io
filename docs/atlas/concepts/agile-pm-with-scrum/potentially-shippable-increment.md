---
type: Concept
title: Potentially Shippable Product Increment
description: "Each sprint must produce complete, tested, integrated, documented code that could be released to production immediately—a strict definition of 'done'."
book: agile-pm-with-scrum
chapters: [1, 6]
tags: [quality, definition-of-done, testing, integration]
created: 2026-07-15
---

# Potentially Shippable Product Increment

## Definition

At the end of every sprint, Scrum requires teams to deliver an increment of product functionality that is potentially shippable: code that is thoroughly analyzed, designed, coded, unit-tested, integrated, and acceptance-tested. It is built into an executable and user-documented (either in help files or user guides). This is what "done" means—not "mostly done" or "ready for QA" but genuinely complete and releasable to production.

## In the Book

Schwaber emphasizes that this definition of "done" is not ceremonial—it directly shapes project outcomes. In the MegaBank cash application case study, the team initially estimated the project would take five months. But when Schwaber asked what "done" meant, the conversation revealed that the team's estimate didn't include unit testing, code reviews, refactoring, or even decisions about which testing framework (JUnit) to use.

Once the Product Owner, Julie, understood that "done" meant tested, maintainable code that could be released immediately if needed, she asked the team to re-estimate. The new estimate was seven months—two additional months. This was not because the team was slack; it was because a loose definition of "done" had masked the real scope of work.

Schwaber notes that this definition prevents two pathologies common in waterfall: (1) declaring partial work complete and losing sight of technical debt, and (2) discovering late in a project that code is unmaintainable, poorly tested, or tightly coupled, requiring massive rework.

The principle extends to regulated environments. For FDA-regulated medical devices, Scrum's definition of "done" for each increment must include the traceability, documentation, and quality checks the FDA requires—so that each sprint's output is not only functionally complete but also compliant.

## Why It Matters

This concept prevents teams from mortgaging quality for schedule. By requiring complete, shippable work every sprint, it forces honest estimation and prevents the accumulation of technical debt. It also enables the business to release frequently if desired, rather than waiting for a "final integration" that discovers all the problems at once. The daily integration (implicit in "done") also reduces the risk and cost of merging large bodies of work.
