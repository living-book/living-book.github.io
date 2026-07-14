---
type: Concept
title: Distributed Representation (PDP)
description: A connectionist network can represent a concept not in one dedicated unit but as a pattern of activation spread across many simple units, each standing for a small microfeature.
book: mind-design-ii
chapters: [8]
tags: [connectionism, neural-networks, representation, parallelism, cognitive-architecture]
created: 2026-07-14
---

# Distributed Representation (PDP)

## Definition

In a parallel distributed processing (PDP) system, meaning lives in a pattern spread across many simple processing units — each unit standing for a "microfeature" — rather than in any single unit standing for a whole concept. Rumelhart contrasts this directly with a "localist" system, where one unit equals one concept: "we mean one in which the units represent small, featurelike entities we call microfeatures. In this case it is the pattern as a whole that is the meaningful level of analysis."

## In the Book

Rumelhart lays out the seven components of any connectionist system — processing units, activation states, output functions, a connectivity pattern, an activation rule, a learning rule, and an environment — and stresses that "there is no executive or other overseer": every unit does its own simple job (summing weighted inputs from neighbors, producing an output) and knowledge lives entirely in the pattern of connection weights, not in any stored symbolic expression. He shows how many connectionist networks can be understood as constraint-satisfaction systems that "relax" toward a solution satisfying many soft constraints simultaneously, and works through the classic case of why single-layer perceptrons cannot compute certain functions (e.g., exclusive-or) while multi-layer networks with learned "hidden" representations can — motivating why backpropagation-trained hidden layers became central to the connectionist program.

## Why It Matters

Distributed representation reframes what "storing information" or "having a concept" means: instead of one lookup-table entry, a piece of knowledge is a pattern spread across many units, tolerant of damage or noise (each unit contributes only a little) and capable of graceful generalization by similarity of pattern. This is the mechanism that later chapters in the book (and the field at large) argue about — whether such patterns can ever explain the structured, rule-like, systematic character of thought that symbolic architectures were built to capture.
