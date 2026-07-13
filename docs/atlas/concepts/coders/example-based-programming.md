---
type: Concept
title: From Writing Rules to Teaching by Example
description: Deep learning replaced hand-written logic rules with models trained on data, changing the programmer's job from author of instructions to curator of examples.
book: coders
chapters: [9]
tags: [machine-learning, programming-paradigms, deep-learning, expertise]
created: 2026-07-12
---

# From Writing Rules to Teaching by Example

## Definition

Traditional programming is an act of authorship: the coder writes explicit if-then rules that fully specify the intended behavior. Deep learning inverts this — the coder instead assembles a large set of labeled examples and lets a neural network infer its own internal rules by pattern-fitting the data, producing a system whose behavior even its own creator cannot fully explain or trace. The programmer's core skill shifts from writing correct logic to curating the training data and iterating on results.

## In the Book

Chapter 9 pairs two illustrations of this shift. First, AlphaGo: Thompson explains that earlier Go-playing programs tried to "develop search algorithms that would rank and pick the best possible future moves," but this rule-based approach failed against Go's astronomical branching factor ("more possible Go games than there are atoms in the universe"). AlphaGo instead used deep learning to analyze 30 million human game positions and build an internal model "so dense and convoluted the creators themselves could not tell you precisely how it works" — producing move 37 against Lee Sedol, a play so alien that Go experts first thought it was a mistake before recognizing it as brilliant.

Second, and more concretely, Makoto Koike, a Japanese engineer who returned to his family's cucumber farm, used Google's newly released TensorFlow to build a cucumber-sorting robot: rather than writing rules distinguishing "good" from "bad" cucumbers, he photographed thousands of cucumbers and let a neural net learn the distinction on its own, reaching 80 percent accuracy through iterative retraining rather than rule refinement. Thompson frames the whole chapter's arc with: "For years, coders have been programming computers to do our repetitive actions. Now they're automating our repetitive thoughts" — and contrasts this with the brittleness of rule-based chatbots, which fail the instant a user's phrasing falls outside the rules anyone thought to write ("boiling the ocean," per AI researcher Dave Ferrucci).

## Why It Matters

This distinguishes two fundamentally different relationships an expert can have to their own tool's behavior: full authorship and traceability (rules) versus statistical fit with irreducible opacity (learned models) — a distinction that matters wherever people are deciding whether to trust, audit, or regulate an automated system, since the two approaches fail differently and require different kinds of oversight. It generalizes beyond software to any expertise transitioning from codified procedure to pattern-matched judgment trained on cases.
