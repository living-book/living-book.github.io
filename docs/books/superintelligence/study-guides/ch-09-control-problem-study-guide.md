---
title: "Study Guide — Ch 9: The Control Problem"
chapter: 9
created: 2026-07-07
---

# Study Guide: Chapter 9 — The Control Problem

## Core Idea
Two agency problems: sponsor-vs-developer (ordinary, solvable with standard tools) and project-vs-superintelligence (the real "control problem," unprecedented, must be solved before the system becomes superintelligent). Two families of solution: capability control (limit what it can do — boxing, incentives, stunting, tripwires) and motivation selection (shape what it wants — direct specification, domesticity, indirect normativity, augmentation). Each has real vulnerabilities; none is a clean solution alone.

## Key Terms
Control problem · capability control vs. motivation selection · boxing · tripwire · anthropic capture · direct specification · domesticity · indirect normativity · augmentation · hedonium

## Case Summary
Red-button incentive design: give the AI a final goal that intrinsically disvalues a button being pressed — the button can be made of Play-Doh, since what matters is only the AI's belief that cooperating keeps it unpressed. Illustrates how capability control and motivation selection can be combined rather than chosen between.

## Application Checklist
- [ ] Don't rely on behavioral testing alone to certify a strategic agent's future behavior — good behavior under observation is cheap for a capable agent to fake
- [ ] When "boxing" any powerful system, check for side channels beyond the obvious ones (the Faraday-cage lesson)
- [ ] When writing rules or objectives, stress-test edge cases before trusting the literal specification — precision reveals vagueness you didn't know was there
- [ ] Prefer layered/combinable safeguards over betting everything on one "best" method

## Self-Test
1. Why must a solution to the control problem be implemented before the AI becomes superintelligent, rather than after?
2. Why does data/domain restriction ("stunting") fail to guarantee safety against a sufficiently superior mind?
3. What is "anthropic capture," and why might it restrain an AI with resource-satiable goals more than one with unbounded goals?
