---
type: Concept
title: Code as Unplanned Social Engineering
description: Small code changes reshape how millions of people relate to each other, but the engineers who ship them rarely foresee the social consequences.
book: coders
chapters: [1, 10]
tags: [unintended-consequences, product-design, scale, social-behavior]
created: 2026-07-12
---

# Code as Unplanned Social Engineering

## Definition

A programmer can rewrite the norms of human relationships — what counts as private, how attention is allocated, how conflict spreads — by changing a few thousand lines of code. The change looks like a technical tweak from the inside (a new feed algorithm, an open messaging default) but functions as social engineering from the outside, and the people writing it are trained to reason about systems, not about the second-order behavior of crowds.

## In the Book

Chapter 1 opens with Ruchi Sanghvi's team at Facebook building the News Feed in 2006: a "single page" reconstructing "how people paid attention to one another." The team spent nine months debating technical weighting rules — how much to weight a friendship, a photo — without anticipating that surfacing information users had to previously seek out would feel like surveillance. The launch triggered "Students against Facebook News Feed," a group with 250,000 members within a day, because users had relied on the old system's inefficiency for "a small, pleasant measure of secrecy."

Chapter 10 makes the same mechanism explicit at greater scale through Twitter cofounders Biz Stone and Jack Dorsey, interviewed by Thompson in Twitter's early days. They accurately foresaw Twitter enabling new "ad hoc coordination" — real-time crowd awareness, later realized in #blacklivesmatter and #metoo — but never discussed, in Thompson's words, "the enormous potential of the service for flat-out evil": Gamergate, Russian troll factories, Trump wielding the platform against individual critics. Thompson calls the conversation, in hindsight, "strikingly naive," and frames it as a general feature of software: it "changes, inexorably, the way society works — including in ways the creators struggle to foresee."

## Why It Matters

Any system-builder — not just coders — can ship a mechanism whose local logic is sound while its aggregate, population-scale effect is unpredictable and irreversible once adopted. It reframes "unintended consequences" as a structural property of tools that operate on human attention and coordination at scale, not a moral failing to be prevented by better intentions alone. It suggests that the discipline needed to anticipate these effects (social science, ethics, adversarial thinking) is different from the discipline that builds the system (engineering), and organizations that only staff for the latter will keep being surprised by the former.
