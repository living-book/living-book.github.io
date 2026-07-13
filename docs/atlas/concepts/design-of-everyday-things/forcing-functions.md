---
type: Concept
title: Forcing Functions
description: A physical or procedural constraint that makes an error impossible by preventing the next step until a required condition is met, trading convenience for safety.
book: design-of-everyday-things
chapters: [4]
tags: [constraints, safety, error-prevention, mechanism-design, poka-yoke]
created: 2026-07-12
---

# Forcing Functions

## Definition

A forcing function is the extreme case of a physical constraint: a situation engineered so that failure at one stage physically prevents the next stage from happening, making a particular error impossible rather than merely discouraged. Norman names three specialized varieties from safety engineering: an interlock, which forces steps to occur in the correct sequence; a lock-in, which keeps an operation active until it is properly completed or exited; and a lockout, which prevents entry into a dangerous state or space altogether.

## In the Book

Chapter 4's running example is the car ignition key: a car cannot be driven without a physical token proving authorization, whether an old-style key or a modern proximity fob — "because the vehicle won't start without the authentication proved by possession of the key, it is a forcing function." Interlocks are illustrated by microwave ovens that cut power the instant the door opens, automatic transmissions that require the brake pedal depressed before leaving Park, and "dead man's switches" on trains, lawn mowers, and chainsaws that stop the machine if the operator's grip releases. Lock-ins appear as the "save before exit" prompt on computer applications — a mechanism Norman says he now deliberately exploits as his standard way of exiting a program, since it guarantees his work is saved. Lockouts appear as the gate that blocks stairwell access from the ground floor into a building's basement, preventing people fleeing a fire from getting trapped below grade, and as the pin on a fire extinguisher preventing accidental discharge. Norman notes the tradeoff explicitly: forcing functions are often experienced as a nuisance in normal use, which is why people frequently disable them, defeating the very protection they were designed to provide.

## Why It Matters

Forcing functions replace "remember to do X" with "you physically cannot proceed without doing X" — moving reliability out of human vigilance and into the structure of the system itself, which is a much stronger guarantee against the errors that recur even among careful, well-trained people. The concept generalizes to any process where a costly mistake is possible: required fields that block form submission, financial controls that require two approvals before a transfer executes, checklists that won't let a pilot advance without completing the prior item. The explicit cost is friction in the normal case, so the design judgment is always about which errors are catastrophic enough to justify making everyone pay a small tax on every use.
