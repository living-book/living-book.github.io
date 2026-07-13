---
type: Concept
title: Trust-Based Contracts
description: A contract engineered to prevent either party from exploiting the other produces worse outcomes than a relationship built on earned trust, backed by a target-cost rather than fixed-price structure.
book: lean-software-development
chapters: [7]
tags: [contracts, trust, incentives, supplier-relationships, incompleteness]
created: 2026-07-12
---

# Trust-Based Contracts

## Definition

The conventional view treats a contract as a substitute for trust: spell out every eventuality so neither party can take advantage of the other. The book argues this produces worse results than building genuine inter-firm trust and pairing it with a target-cost contract structure — where both parties share the risk of overruns and both have an incentive to solve problems together — rather than a fixed-price contract, where change requests become the vendor's main profit opportunity and change-approval bureaucracy becomes the customer's main defense.

## In the Book

The chapter's evidence is Toyota's supplier relationships, documented in Jeffrey Dyer's Collaborative Advantage: by 1998 Toyota was rated the most trusted automaker by its suppliers, twice as trusted as GM, because suppliers had confidence in the fairness of Toyota's routines and processes — not in any individual buyer — reflected in Toyota doing repeat business with a supplier 90% of the time versus 50% for GM, and suppliers sharing proprietary information and letting Toyota's own experts into their plants without fear of exploitation. The parallel case is stamping-die development: U.S. automakers used fixed-price contracts awarded to the lowest bidder, so toolmakers padded profit through change orders (30-50% of die cost), backed by rigorous change-approval processes that mirror common software change-control practices; Toyota used target-cost contracts where changes were budgeted in from the start (typically adding 10-20%) and cost overruns were negotiated jointly, with Toyota absorbing the larger share — and Toyota's dies came in at roughly half the cost and half the time, with higher quality. The book explicitly draws the software parallel: a fixed-price contract combined with a rigorous change-approval mechanism, its own version of the American die-shop pattern, tends to double cost and time while lowering quality.

## Why It Matters

Contract design is usually treated as risk allocation between adversaries; this concept reframes it as an incentive structure that either rewards genuine collaboration or rewards gaming the letter of the agreement. It gives you a diagnostic for any cross-firm arrangement — including ones far from manufacturing — for whether the payment structure quietly incentivizes the exact adversarial behavior the contract was meant to prevent.
