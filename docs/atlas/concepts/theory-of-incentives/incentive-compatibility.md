---
type: Concept
title: "Incentive Compatibility"
description: "A contract is incentive-compatible when agents prefer to truthfully reveal their information and take the actions the principal wants, rather than lying or deviating."
book: theory-of-incentives
chapters: [2, 3, 4, 5, 6]
tags: [truthfulness, constraints, contracts, mechanism-design, self-selection]
created: 2026-07-15
---

# Incentive Compatibility

## Definition

A contract or mechanism is incentive-compatible when it is in each agent's self-interest to behave as the principal desires. For an agent with private information, this means truthfully revealing that information rather than misrepresenting it. For an agent making hidden actions, it means exerting the desired level of effort or care. An incentive-compatible contract aligns the agent's incentives with the principal's preferences without requiring external enforcement or monitoring—the agent wants to do what the principal wants because it maximizes the agent's own payoff given the contract terms.

## In the Book

Chapter 2 (section 2.3) introduces incentive compatibility in the context of adverse selection. The principal offers a menu of contracts and wants each type of agent to choose the contract designated for that type. An incentive-compatible menu requires that each contract be weakly preferred by its intended type to all other contracts in the menu. Formally, an efficient agent receiving contract (t, q) must get higher utility from (t, q) than from the contract (t̄, q̄) designed for the inefficient type: t - cq ≥ t̄ - cq̄.

These constraints are not morality or honor codes; they are revealed preference statements. By observing which contract an agent chooses, the principal learns the agent's type. If incentive constraints are violated, pooling occurs—the efficient agent imitates the inefficient one, defeating the screening mechanism.

The book shows that incentive-compatible allocations must satisfy a monotonicity condition (Ch. 2.3.3): output allocated to an inefficient agent cannot exceed that allocated to an efficient agent, or the contracts fail to separate. This is an implementability requirement that has no counterpart under complete information.

In moral hazard settings (Ch. 4), incentive compatibility requires that the agent's optimal choice of effort matches the principal's desired effort level. With hidden action, the principal cannot directly verify effort, so the contract must make truthful effort-taking a best response. This typically involves performance pay that increases the agent's payoff when outcomes are better.

The book emphasizes (Ch. 2.9, Revelation Principle) that without loss of generality, one can restrict attention to direct revelation mechanisms where agents simply report their type and the principal responds with an allocation. This dramatically simplifies analysis: any allocation achievable through complex mechanisms can be achieved through simple truth-telling under the right transfer schedule.

## Why It Matters

Incentive compatibility is the binding constraint on what is achievable under asymmetric information. First-best outcomes are often infeasible because they violate incentive constraints. The concept shows that getting people to behave well requires structuring payoffs appropriately, not just threatening punishment or appealing to honesty. It explains why simple fixed-wage contracts often fail for managers (they don't incentivize hard work), why insurance requires deductibles and copays (they deter false claims), and why regulation uses menus of contracts rather than trying to dictate terms. Incentive compatibility converts the abstract problem of asymmetric information into specific mathematical constraints on feasible contracts.

