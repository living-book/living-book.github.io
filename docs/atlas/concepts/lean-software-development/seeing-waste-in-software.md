---
type: Concept
title: Seeing Waste in Software
description: Translating Toyota's seven manufacturing wastes into seven wastes of software development, so anything not analysis or coding becomes a candidate for elimination.
book: lean-software-development
chapters: [1]
tags: [waste, translation, analysis, software-development, lean]
created: 2026-07-12
---

# Seeing Waste in Software

## Definition

Waste is anything that does not directly add value as perceived by the customer, or anything you could do without. Before an organization can eliminate waste it first has to learn to see it — and most software waste is invisible because it looks like normal process, not obvious scrap. The Poppendiecks make it visible by mapping Shigeo Shingo's seven wastes of manufacturing onto software: Partially Done Work, Extra Processes, Extra Features, Task Switching, Waiting, Motion, and Defects.

## In the Book

Chapter 1 opens with Winston Royce's 1970 observation that only analysis and coding directly contribute to the final product — everything else in the waterfall process drives up cost without adding value, which the authors read as a working definition of waste. They then walk through each of the seven translated categories with concrete failure modes: partially-done work that carries financial risk because you don't know it works until it's integrated and in production; paperwork nobody is waiting for; "just in case" extra features that add permanent maintenance burden for a need that may never materialize; task switching between multiple projects, which — citing Goldratt's Critical Chain — turns two two-week projects into five weeks of elapsed time once switching overhead is added; and systemic waiting, which the book ties directly to the cost of delaying customer value. The chapter's discipline is asking of every activity: is there someone actually waiting for this, eager to use it?

## Why It Matters

Most process waste survives because it's mistaken for necessary structure rather than recognized as waste — nobody audits a status report or a sign-off the way they'd audit idle inventory on a factory floor. Having a named taxonomy, borrowed from a domain (manufacturing) where waste-hunting is a mature discipline, gives you a checklist to interrogate work that otherwise hides behind the appearance of diligence. It reframes "our process requires this" as a testable claim rather than a given.
