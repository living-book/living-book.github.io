---
type: Concept
title: "Revelation Principle"
description: "Any mechanism or allocation rule achievable through complex message spaces and indirect communication can be implemented using a simple direct mechanism where agents truthfully report their private information."
book: theory-of-incentives
chapters: [2, 6, 7]
tags: [mechanism-design, implementation, truthfulness, communication, simplification]
created: 2026-07-15
---

# Revelation Principle

## Definition

The Revelation Principle states that without loss of generality, analysis of incentive problems can be restricted to direct revelation mechanisms where informed agents simply report their private information truthfully to a planner, who then assigns allocations based on those reports. Any allocation rule that could be achieved through a complex mechanism with arbitrary message spaces can be equivalently implemented through a simple truth-telling mechanism. This is not because truth-telling is always optimal—agents must be given the right incentives through the transfer schedule—but because the principal can design transfers to make truth-telling optimal.

## In the Book

Chapter 2 (section 2.9) presents the Revelation Principle formally as Proposition 2.2. The proof is elegant: given any general mechanism with message space M and outcome function g̃(m), if the agent with type θ optimally chooses message m*(θ), the principal can construct a direct mechanism that simply asks the agent to report their type, then provides the allocation g(θ) = g̃(m*(θ)). Since m*(θ) was a best response in the original mechanism, reporting truthfully in the direct mechanism achieves the same allocation and payoffs.

The book notes that this principle emerged historically through the work of multiple authors (Gibbard 1973, Green and Laffont 1977, Dasgupta, Hammond, and Maskin 1979, Myerson 1979) and provided the "appropriate framework for the normative analysis of economies with asymmetric information and contracts that can be written on all observable variables" (Ch. 1.10). It simplified mechanism design from studying arbitrary message spaces to studying just transfer schedules for truthful reports.

Importantly, the principle does not require agents to be honest or altruistic. The transfers must be set so that reporting truthfully is each agent's best response. In adverse selection, this means paying efficient types a rent so they don't mimic inefficient types. In moral hazard, this means making pay depend on performance so effort is incentivized.

The book shows the principle at work across many settings: regulation (Ch. 2.15.1), pricing and discrimination (Ch. 2.15.2-3), financial contracting (Ch. 2.15.4), and labor contracting (Ch. 2.15.5). Each application uses the simplification the Revelation Principle provides to focus on what transfers are needed to implement desired allocations.

## Why It Matters

The Revelation Principle is foundational to modern mechanism design and contract theory. It transforms analysis from studying baroque incentive games to studying simple transfer schedules. It shows that the principal doesn't need to construct complex games or hidden-message spaces to achieve their goals—direct truth-telling suffices if incentivized correctly. This principle underlies auction design, regulation, taxation, and organizational mechanism design. It also provides a clear interpretation of any mechanism: you can always think of it as equivalent to agents truthfully reporting their information to a benevolent planner who assigns allocations based on those reports.

