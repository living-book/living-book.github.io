---
type: Concept
title: Testing the Parts Isn't Testing the Whole (and Vice Versa)
description: Testing every module doesn't test how they interact, and testing the whole system doesn't exercise every path inside its parts — each direction misses what the other catches.
book: perfect-software
chapters: [9]
tags: [emergence, composition, systems-thinking, testing, fallacies]
created: 2026-07-12
---

# Testing the Parts Isn't Testing the Whole (and Vice Versa)

## Definition

The Decomposition Fallacy assumes "test the parts and you've tested the whole" — but module-level testing only produces information about the modules, not about how they interact once assembled. Its mirror image, the Composition Fallacy, assumes "test the whole and you've automatically tested the parts" — but a system test only touches each module's interface, not every internal path, so integration testing can pass while badly broken internal logic in a component goes unexercised.

## In the Book

Weinberg dramatizes this through a workplace argument: a developer, Barry, orders a tester, Suzy, to test individual modules instead of "the interface," insisting "if you test the modules and the modules make up the system, then you've done your job" — the Decomposition Fallacy. New test manager Rose intervenes, explaining that testing modules gives information about the modules, not about how they work together, so it's correct for Suzy to test the system as a system. Suzy then swings to the opposite error — "testing the system will automatically test the parts" — which Rose also corrects: system tests touch the modules but don't reach all the paths inside them, the same way merely touching a system's outer interface wouldn't count as having tested it thoroughly.

## Why It Matters

This names a symmetric blind spot that shows up anywhere a whole is built from parts: unit-level verification and integration-level verification are not substitutes for each other, they answer different questions, and skipping either one leaves a specific, predictable category of failure uncaught — interaction failures in one direction, buried internal-path failures in the other.
