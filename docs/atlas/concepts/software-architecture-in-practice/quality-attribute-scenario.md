---
type: Concept
title: The Quality Attribute Scenario
description: A six-part template — source, stimulus, environment, artifact, response, response measure — that turns a vague quality goal into a testable requirement.
book: software-architecture-in-practice
chapters: [4]
tags: [requirements, measurement, specification, quality-attributes, testability]
created: 2026-07-12
---

# The Quality Attribute Scenario

## Definition

"Be fast" or "be secure" cannot be verified because they are not testable statements. A quality attribute scenario forces the claim into six parts: a source of stimulus, the stimulus itself, the environment/mode the system is in, the artifact being stimulated, the required response, and a response measure that makes the response checkable. Omitting a part is common early on, but naming all six as a checklist forces the architect to at least consider whether each is relevant.

## In the Book

Chapter 4 introduces the six-part form as the common structure used for every quality attribute discussed in the book, from availability to usability. It distinguishes general scenarios — system-independent templates that could apply to any system ("a fault occurs; the system must detect it, recover, and remain available X% of the time") — from concrete scenarios, which instantiate the template for a specific system. Figure 4.2 works through availability as an example: source (internal or external fault), stimulus (omission, crash, incorrect timing), environment (normal operation, startup, degraded mode), artifact (processors, communication channels, storage), response (detect, recover, log, notify), and response measure (availability percentage, time to detect, time to repair). Chapters 5–11 then apply the identical six-part structure to interoperability, modifiability, performance, security, testability, and usability, which is what lets the book claim these otherwise very different concerns are commensurable.

## Why It Matters

The scenario form is a discipline for converting adjectives into obligations. Any domain that talks about desirable properties in unfalsifiable terms — "reliable," "user-friendly," "resilient," "fair" — can use the same move: name who or what triggers the property, under what conditions, on what part of the system, what the required response is, and how you would measure whether it happened. It also exposes when a stated requirement is actually silent on the part that matters most, usually the response measure, which is the part people skip because it's the part that commits them to being provably wrong.
