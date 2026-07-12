---
type: Concept
title: Overfitting
description: A learner mistakes noise or coincidence in its data for a real pattern, producing a model that fits what it has seen but fails on everything new.
book: master-algorithm
chapters: [3]
tags: [machine-learning, pattern-recognition, error, generalization]
created: 2026-07-12
---

# Overfitting

## Definition

Overfitting occurs when a learner finds a pattern in its data that is not actually true of the world it's trying to model — "the central problem in machine learning," per Domingos, and the subject of more research papers than any other ML topic. It arises because learners face too many candidate hypotheses relative to the data available to distinguish among them, and is worsened by noise (errors or unpredictable randomness in the data), since a learner will otherwise contort itself to explain away what is really just noise.

## In the Book

Domingos frames overfitting as a universal hazard for "every powerful learner, whether symbolist, connectionist, or any other." He deliberately extends the concept beyond computers to human cognition: a child who blurts "Look, a baby maid!" on seeing a Latina infant has overfit her small sample of encountered Latina women to a general rule, and Aristotle overfit when he inferred from everyday friction-laden experience that objects need continuous force to keep moving (Galileo's insight — that undisturbed objects keep moving — required overriding that overfit intuition). He cites John von Neumann's line "with four parameters I can fit an elephant, and with five I can make him wiggle his trunk," and the Bible Code controversy — where skeptics showed the same letter-skipping method that supposedly found hidden biblical prophecies also "finds" predictions in Moby Dick — as illustrations that with enough search capacity, spurious patterns are guaranteed to turn up. He formalizes it: for a simple conjunctive learner, the number of possible hypotheses grows exponentially with the number of attributes, so without enough data, many hypotheses fit the training set equally well and most of them are wrong.

## Why It Matters

Overfitting generalizes to any situation where an agent — human or algorithmic — has enough flexibility to explain a limited set of observations and mistakes that flexibility for insight: small-sample stereotyping, over-fit business narratives built from a handful of anecdotes, backtest-optimized trading strategies, or a theory that perfectly explains everything that already happened and predicts nothing new. The tell is the same everywhere: a story so good at explaining the past that it costs you nothing to abandon your priors, built on too little independent evidence to have earned that confidence.
