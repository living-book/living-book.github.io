---
type: Concept
title: "Performance Informativeness"
description: "The more an observable signal (like output or profit) reveals the agent's true type or effort, the less the principal needs to distort contracts or pay information rents."
book: theory-of-incentives
chapters: [2, 4, 5]
tags: [measurement, signals, monitoring, information-structure, inference]
created: 2026-07-15
---

# Performance Informativeness

## Definition

Performance informativeness measures how much an observable signal (like output, profit, or any measurable outcome) reveals the principal's uncertainty about the agent's private information or effort. A signal is more informative if observing it allows the principal to better infer whether the agent is a high-cost type, a high-effort agent, or facing favorable conditions. The higher the informativeness of performance signals, the less the principal needs to distort the agent's actions or pay large information rents to extract information. This is formalized through likelihood ratios and Bayesian updating: signals that make it more likely the agent is a desired type reduce the information problem.

## In the Book

Chapter 2 (section 2.14) studies how informative signals improve contracting. The book shows that ex post verifiable signals—observed after the agent chooses production and correlated with the agent's type—can dramatically reduce the principal's information problem. In the baseline adverse selection model, the inefficient agent's output is distorted downward to separate types. But if the principal observes a signal that indicates the agent is likely to be efficient, the principal can offer a contract with less distortion, knowing the signal will confirm efficiency with high probability.

Specifically, section 2.14.2 formalizes the informativeness through a likelihood ratio. If a signal ξ is more likely when the agent is efficient, the principal updates their belief using Bayes' law: Pr(efficient | ξ) increases. Using Theorem 2.1 (the Monotone Likelihood Ratio Property), the principal can condition contract distortions on the signal. If the signal confirms efficiency, contracts are less distorted; if it confirms inefficiency, distortion increases. Formally: S'(q̄^SB(ξ)) = c̄ + (θ̂(ξ)/(1-θ̂(ξ))) Δc, where θ̂(ξ) is the updated probability of efficiency. When θ̂(ξ) is high, distortion is low.

The book also discusses (Ch. 2.14.1) ex post verifiable signals that perfectly reveal the state of nature. When the principal, agent, and court all observe the same signal, incentive and participation constraints can be written as a system of linear equations in the agent's rents. When this system has full rank (which holds generically), the principal can find transfers that make all constraints binding simultaneously, allowing any output profile to be implemented with zero rent to the agent—even the first-best outcome. The quality of performance measurement is the key: more informative signals permit more efficient contracting.

The concept also underlies the discussion of yardstick competition (Ch. 1, cited works) and monitoring structures: observing the performance of similar agents under similar conditions provides a signal about whether outcomes reflect the agent's effort or external factors.

## Why It Matters

Performance informativeness explains why organizations invest in measurement and monitoring systems. It shows that better accounting, clearer metrics, and comparative benchmarking (comparing one agent's performance to peers) all have value beyond transparency—they improve incentive contracting by making it easier to infer effort and ability. This justifies the costs of auditing, performance appraisals, and yardstick competition. It also highlights a trade-off: measuring performance is costly, and the principal must balance the cost of better measurement against the savings from reduced information rents and distortions. This framework applies to personnel evaluation, firm regulation, and any context where contracts depend on observed outcomes.

