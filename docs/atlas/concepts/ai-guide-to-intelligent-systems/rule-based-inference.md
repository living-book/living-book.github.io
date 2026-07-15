---
type: Concept
title: Rule-Based Inference (Forward and Backward Chaining)
description: An inference engine matches IF-THEN rules against known facts, either gathering forward from data or working backward from a hypothesis to prove it.
book: ai-guide-to-intelligent-systems
chapters: [2]
tags: [expert-systems, inference, reasoning, knowledge-representation, symbolic-ai]
created: 2026-07-12
---

# Rule-Based Inference (Forward and Backward Chaining)

## Definition

A rule-based expert system represents domain knowledge as a set of IF-THEN production rules and represents the current situation as a set of facts in a database, keeping the two strictly separate. An inference engine drives reasoning through a match-fire cycle: it compares rule conditions against known facts and executes ("fires") any rule whose IF part matches, which may add new facts. There are two ways to run this cycle — forward chaining, which is data-driven and starts from known facts to see what can be inferred, and backward chaining, which is goal-driven and starts from a hypothesis, searching for rules and sub-goals that would prove it.

## In the Book

Chapter 2 builds the mechanism from a five-rule toy example (facts A–E; rules like `X & B & E → Y`) and traces it twice. In forward chaining, the engine fires every rule whose conditions are satisfied each cycle regardless of relevance to any particular goal — in the book's example, four of five rules fire, including one (`C → L`) that has nothing to do with the target fact Z. In backward chaining, the engine starts from the goal (fact Z), finds the rule that concludes it, "stacks" the rule, and recursively sets up sub-goals for its unproven conditions until it bottoms out in facts already in the database — only three rules fire to reach the same conclusion. The book uses this efficiency contrast to give a concrete selection rule: choose forward chaining when an expert first gathers information and then infers whatever follows (its example is DENDRAL, which infers molecular structure from mass spectral data), and choose backward chaining for diagnostic tasks that start from a hypothesis and hunt for supporting evidence (its example is MYCIN, diagnosing blood infections). The chapter then builds MEDIA ADVISOR, a demonstration expert system in the Leonardo shell that recommends a training-delivery medium from a trainee's job profile, to show the technique end to end, including how the fired-rule trace doubles as an explanation facility.

## Why It Matters

The forward/backward distinction is really about where the leverage is in a chain of "if this then that": run the chain forward when you have your inputs and want to know everything they entail, run it backward when you have a specific claim to check and don't want to compute anything irrelevant to that claim. The pattern recurs anywhere a system reasons over conditional rules — tax software choosing whether to accumulate deductions or trace back from a target deduction, a debugger working forward from a stack trace versus backward from a suspected root cause, or a build system deciding whether to rebuild everything reachable from a changed file versus everything needed to produce one target artifact.
