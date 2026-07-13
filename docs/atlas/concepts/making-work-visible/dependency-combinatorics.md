---
type: Concept
title: Dependency Combinatorics
description: Each additional hard dependency a delivery requires doesn't add risk linearly — it halves the probability of on-time delivery.
book: making-work-visible
chapters: [1.2]
tags: [dependencies, probability, risk, coordination, systems-thinking]
created: 2026-07-12
---

# Dependency Combinatorics

## Definition

When a deliverable requires N independent things to all go right (all inputs on time, all people available, all upstream teams done), the probability everything lines up is roughly 1/2^N — not some gentler linear decay. Removing a single dependency doesn't shave a little risk off; it doubles the odds of delivering on time. Dependencies are asymmetrical in their impact: a small number of them can make on-time delivery ce­rtain to fail.

## In the Book

Section 1.2, "Unknown Dependencies," opens with a case of a $23 billion company where Team X shipped a change that broke Team Y's product, costing Team Y's customers a combined $15 million and a public-relations disaster — because "Team Y had zero visibility into Team X's decision." DeGrandis defines three dependency types: architecture (a change in one area breaks another), expertise (needing a specific person's know-how), and activity (progress blocked until something else finishes).

She then grounds the mathematical claim in Troy Magennis's Agile 2015 talk: with binary (on-time/late) inputs, the number of possible outcome combinations is 2^N, and only one combination has everything arrive on time. With two inputs there's a 1-in-4 chance; with four dependencies (illustrated as four dinner guests traveling independently to a restaurant that won't seat the party until everyone arrives), there are sixteen possible outcomes and only one where the whole party is on time — a 93% chance someone is late. The book also uses "two-pizza teams" (five to seven people) to show that shrinking team size to move fast just relocates the dependency problem: cross-team coordination costs rise even as each small team individually accelerates, so organization-wide throughput can still suffer.

## Why It Matters

This turns a vague worry ("there are a lot of moving parts") into an argument for aggressively counting and removing hard dependencies rather than merely tracking them — because the payoff of removing one is nonlinear and large. It also explains a common organizational paradox: an org can make every individual team faster (smaller, more autonomous) while making the whole system slower, because autonomy just multiplies the number of independent dependency-inputs a joint outcome now requires.
