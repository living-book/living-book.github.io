---
type: Concept
title: "Continuous System Test"
description: Testing the integrated system repeatedly throughout development rather than once at the end, reducing the critical path spent on bug-fixing after major integration.
book: lean-from-the-trenches
chapters: [9]
tags: [testing, quality, flow, lean-waste]
created: 2026-07-15
---

# Continuous System Test

## Definition

Instead of saving system testing for the end of a release cycle, run partial or full system tests at regular intervals as features complete. Each test cycle discovers bugs while the code is still fresh in developers' minds and before large amounts of untested work pile up. The testing timeline extends (more test runs happen), but the bug-fixing timeline shrinks far more, compressing the total time dramatically.

## In the Book

The PUST team was skeptical at first. Their testers resisted running system tests more than once per release cycle, since system test takes time and felt inefficient to run often. But when Kniberg graphed the math, it was clear: testing once at the end produces one long bug-fixing tail after you've finally integrated everything. Testing continuously means bugs are found when only a few new features have been added since the last test run, so developers still understand the code and fixes are fast. Bugs found at the end are harder to debug because developers have moved on; bugs found early are fixed immediately. By doing continuous system testing, the PUST team reduced the chaotic end-of-release crunch and made the entire release predictable.

## Why It Matters

This concept inverts the assumption that testing is a final gate. It shows that the cost of a testing activity isn't the time spent testing—it's the time spent fixing bugs found by that test. Moving testing earlier in the cycle front-loads learning and spreads the cost of integration across the whole development window instead of compressing it into a panic at the end. This applies beyond software: any domain where integrating parts late is expensive benefits from validating subsystems as they're completed rather than waiting for one catastrophic assembly.
