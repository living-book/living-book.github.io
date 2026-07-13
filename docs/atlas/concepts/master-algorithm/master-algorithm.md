---
type: Concept
title: The Master Algorithm
description: The hypothesis that a single, general-purpose learning algorithm could in principle derive all knowledge in the world from data.
book: master-algorithm
chapters: [1, 2]
tags: [machine-learning, unification, induction, ai]
created: 2026-07-12
---

# The Master Algorithm

## Definition

The Master Algorithm is Domingos's name for a hypothetical universal learner: one algorithm, fed enough data, that could discover any pattern and derive any knowledge that exists to be derived, in any domain. He compares its role for machine learning to the Standard Model in particle physics or the Central Dogma in molecular biology — "a unified theory that makes sense of everything we know to date."

## In the Book

Domingos frames the whole book as a quest, not a settled answer: he argues from convergent evidence — the existence of the scientific method, the universality of Turing machines, the physical Church-Turing thesis, and the fact that the brain uses (roughly) one algorithm across cortical regions — that a master algorithm likely exists, then spends the book trying to build the closest approximation anyone has assembled. Each of the five schools of machine learning (symbolists, connectionists, evolutionaries, Bayesians, analogizers) already has its own candidate master algorithm — inverse deduction, backpropagation, genetic programming, Bayesian inference, and the support vector machine, respectively — but each is "good for some things but not others." The book's running worked example is curing cancer: no single doctor, and no single learning paradigm, can integrate genomics, drug interactions, and a patient's full medical history, but a unified learner in principle could. By the end (Chapter 9), Domingos assembles Markov logic networks as his best current answer, explicitly calling it "not yet the Master Algorithm... but the closest anyone has come."

## Why It Matters

The idea reframes a technical field as a live scientific quest with a falsifiable-ish endpoint, which is what makes it exportable: it is a template for asking, of any fragmented discipline, "do these competing schools of thought share a deep structure that a single unifying framework could capture?" It also usefully separates the aspiration (one algorithm to learn anything) from the current reality (five incompatible partial solutions), a distinction worth holding onto whenever a field's "grand unified theory" is invoked rhetorically before it exists.
