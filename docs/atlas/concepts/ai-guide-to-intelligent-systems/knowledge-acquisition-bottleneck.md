---
type: Concept
title: The Knowledge Acquisition Bottleneck
description: Extracting an expert's know-how into a usable form is the hardest, slowest step in building an intelligent system, because experts are often unaware of the knowledge they actually use.
book: ai-guide-to-intelligent-systems
chapters: [9]
tags: [knowledge-engineering, expert-systems, tacit-knowledge, elicitation, process]
created: 2026-07-12
---

# The Knowledge Acquisition Bottleneck

## Definition

Knowledge acquisition — collecting and analyzing the domain data and expert knowledge needed to build an intelligent system — is an inherently iterative process of reviewing documents, then interviewing the domain expert, then studying and re-interviewing. The book calls it "the knowledge acquisition bottleneck" because it is routinely the slowest and most error-prone phase of the six-phase knowledge engineering process (problem assessment, data and knowledge acquisition, prototype, complete system, evaluation, integration/maintenance): experts are frequently unaware of what knowledge they have or the strategy they actually use to solve a problem, and even when aware, may be unable to verbalize it, or may supply irrelevant, incomplete, or inconsistent information.

## In the Book

Chapter 9 grounds the bottleneck in a case from Donald Michie (1982): a cheese factory's experienced tester, nearing retirement, tested cheese by sticking a finger into a sample and judging whether it "felt right." The factory assumed this meant surface tension, and built a machine to measure surface tension — the machine was useless. It turned out the tester was subconsciously judging the cheese by smell, and used the finger only to break the crust and release the aroma; the stated explanation of his own expertise was simply wrong. The chapter frames this as the general risk of knowledge engineering: experts describe their reasoning through introspection, and introspection is not a reliable readout of the actual decision process, which is why the standard elicitation method — asking an expert to walk through four or five typical cases and "think out loud" — is treated as necessary but insufficient, requiring iteration and cross-checking against real cases rather than trusting the expert's self-report on the first pass.

## Why It Matters

The bottleneck is really a general fact about expertise: skilled performance and the ability to accurately narrate that performance are two different capacities, and the gap between them is exactly where any attempt to codify, teach, or automate someone's judgment gets stuck. It shows up whenever an organization tries to turn a person's tacit skill into a repeatable process — writing a runbook from a senior engineer's on-call instincts, onboarding documentation that misses the "smell" a veteran salesperson actually uses, or an AI system trained on stated rules that misses the real signal an expert relied on. The corrective in every case is the same: don't just ask what someone thinks they do, watch what they actually respond to.
