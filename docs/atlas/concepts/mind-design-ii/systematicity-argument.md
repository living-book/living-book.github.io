---
type: Concept
title: The Systematicity Argument
description: Cognitive capacities come in structurally related clusters — whoever can think "John loves Mary" can think "Mary loves John" — a pattern only combinatorial syntax can explain, not stipulate.
book: mind-design-ii
chapters: [12]
tags: [cognitive-architecture, connectionism, syntax, explanation, philosophy-of-mind]
created: 2026-07-14
---

# The Systematicity Argument

## Definition

Fodor and Pylyshyn observe that human cognitive abilities are never "punctate" — nobody can think one thought without being able to think structurally related ones: anyone who can infer *John and Mary went to the store* from *John and Mary and Susan went to the store* can also infer *John went to the store* from *John and Mary went to the store*, and so on across countless parallel cases. They argue only an architecture with combinatorial syntax and semantics — a classical symbol system — can explain why this pattern is a near-truism rather than an accident, because a connectionist network can be built to exhibit it but has no internal mechanism that forces it to.

## In the Book

The chapter's core move is to show that "connectionist architecture tolerates gaps in cognitive capacities" — since connectionist representations are, structurally, just a list of causally-connected nodes, and "lists, qua lists, have no structure; any collection of items is a possible list." A network could in principle have a node for aRb without one for bRa, producing a mind that could think one relational thought but not its systematic partner — yet no such minds are found. Fodor and Pylyshyn anticipate the reply that a connectionist could simply build networks that happen to respect systematicity, and reject it: stipulating the pattern isn't explaining it; you need a mechanism that enforces it, and "the only mechanism that is known to be able to produce pervasive systematicity is classical architecture," which requires exactly the internally-structured, syntactically-combinable representations that connectionism, by its own principles, forgoes. The chapter also surveys and rebuts the standard pro-connectionist arguments (the "hundred-step constraint" on neural speed, graceful degradation under damage, and difficulty explaining tacit/nonverbal skill) as motivating parallelism at the implementation level without undermining classical symbolic structure at the level of cognitive architecture.

## Why It Matters

The systematicity argument gives a general test for any proposed cognitive or computational architecture: does it merely permit an observed regularity, or does its structure actually force that regularity to hold? A model that can be tuned to fit a pattern after the fact explains less than one whose architecture makes the pattern unavoidable — a distinction useful whenever you're evaluating whether a proposed mechanism is doing real explanatory work or just being retrofitted to match the data.
