---
type: Concept
title: Representation, Evaluation, Optimization
description: Every learning algorithm, whatever its tribe, decomposes into three parts — what forms its hypotheses can take, how it scores them, and how it searches for the best one.
book: master-algorithm
chapters: [2, 9, 10]
tags: [machine-learning, mechanism, decomposition, search]
created: 2026-07-12
---

# Representation, Evaluation, Optimization

## Definition

Domingos argues that despite their surface diversity, all learning algorithms — symbolist, connectionist, evolutionary, Bayesian, or analogical — reduce to the same three components: a **representation** (the formal language the learner uses to express hypotheses, which determines what it's even possible for it to learn), an **evaluation function** (a score, such as accuracy or likelihood, that distinguishes good hypotheses from bad ones), and an **optimizer** (a search procedure that finds the highest-scoring hypothesis the representation allows). "Hundreds of new learning algorithms are invented every year, but they're all based on the same few basic ideas."

## In the Book

This decomposition is introduced early and used as an organizing lens for comparing the five tribes' algorithms across the book, then made explicit near the end of Chapter 9 and used directly in Chapter 10 for Domingos's argument that AI systems pose no autonomy risk: "the learner's representation circumscribes what it can learn... the optimizer then does everything in its power to maximize the evaluation function — no more and no less — and the evaluation function is determined by us." Because every learner, however powerful, is only as capable as this triple lets it be, and the evaluation function is human-set, Domingos concludes a learning system can't autonomously adopt goals outside what it was built to optimize — "a robot whose programmed goal is 'make a good dinner' ... can't decide to murder its owner any more than a car can decide to fly away."

## Why It Matters

This is a general-purpose way to dissect any optimizing or search-based system, not just ML: ask what space of solutions it can even represent, what it's being scored against, and how it searches that space — and most disagreements about a system's behavior trace back to one of those three, not the others. It's also the concrete mechanism behind a recurring debate about autonomous AI risk: whether a system's goals can drift depends on whether its evaluation function is truly fixed by its designers or can itself become a target of optimization — a question this decomposition makes precise enough to argue about.
