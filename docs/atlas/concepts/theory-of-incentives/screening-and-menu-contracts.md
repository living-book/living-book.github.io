---
type: Concept
title: "Screening and Menu Contracts"
description: "The principal offers a menu of different contract options, each designed to appeal to agents with different private types, allowing the principal to infer and screen agent types through their choices."
book: theory-of-incentives
chapters: [2, 3, 7]
tags: [menu, screening, separation, bunching, contract-design]
created: 2026-07-15
---

# Screening and Menu Contracts

## Definition

Screening is the principal's strategy to indirectly learn agents' private information by offering a menu of contracts, each with different terms. Each contract is designed to be most attractive to agents of a particular type (low-cost, high-productivity, low-risk, etc.). By observing which contract each agent chooses, the principal learns the agent's type through the agent's self-selection. The principal screens by making the contracts different enough that misrepresentation is costly: a low-cost agent preferring the high-cost agent's contract would forgo valuable gains. This is in contrast to pooling contracts, where all agents receive the same terms regardless of type.

## In the Book

Chapter 2 (section 2.3) introduces screening through menus of two contracts: one for an efficient type and one for an inefficient type. The principal must ensure the menu is incentive-compatible: the efficient agent weakly prefers their contract to the inefficient agent's contract, and vice versa. This is achieved by distorting the inefficient agent's output downward. Under complete information, both types would receive their first-best output. Under asymmetric information, the inefficient type's output is reduced so that the efficient type no longer wants to mimic them.

The book formalizes this: the incentive-compatible menu requires t - cq ≥ t̄ - cq̄ for the efficient type and t̄ - c̄q̄ ≥ t - c̄q for the inefficient type. These constraints define the set of feasible allocations. The monotonicity constraint q ≥ q̄ emerges necessarily: if the inefficient agent were allocated higher output, even with lower transfer, the efficient agent would want to switch contracts.

Chapter 3 extends screening to more than two types. When there is a continuum of types, the optimal contract becomes a nonlinear pricing or tariff schedule where output/quality varies smoothly with the agent's type. Historically (Ch. 1.8), this appears in Dupuit's discussion of pricing infrastructure: charge different prices or qualities to different consumers based on their willingness to pay, forcing self-selection.

Special cases of screening include:
- **Pooling**: All agents get the same contract (extreme case where screening is zero)
- **Shutdown**: The principal offers a contract only to the efficient type and excludes the inefficient type entirely (extreme separation)
- **Bunching**: Multiple types receive the same contract (partial pooling)

The book shows (Ch. 2.14) that with informative performance signals, the principal can shift between separation and pooling: a favorable signal may warrant reduced output distortion or even pooling.

## Why It Matters

Screening menus explain real-world contract structures: loan applications with different terms for different risk profiles, insurance policies with different coverage levels and deductibles, pricing tiers for services, and employment contracts with different performance requirements. The design of these menus reflects the trade-off between giving agents the flexibility to self-select and maintaining incentive compatibility. It also shows why simple uniform contracts often fail: if one contract cannot separate types, it must pool them, leaving information rents on the table. Screening theory reveals how institutions sort heterogeneous agents into different arrangements that reveal and separate their types.

