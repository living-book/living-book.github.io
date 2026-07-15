---
type: Concept
title: Queueing Theory and the Waiting-Cost Trade-off
description: Model arrivals and service as probability distributions to predict wait times, then balance the cost of adding service capacity against the cost customers bear by waiting.
book: intro-to-management-science
chapters: [11]
tags: [probability, capacity, trade-offs, operations, modeling]
created: 2026-07-12
---

# Queueing Theory and the Waiting-Cost Trade-off

## Definition

A waiting line (queue) forms whenever arrivals to a service system are random
and can outpace the system's capacity to serve them at that moment, even if
average capacity is sufficient. Queueing models describe the arrival process
and the service process as probability distributions — commonly the Poisson
distribution for the number of arrivals in a period — and from those
distributions derive "operating characteristics" like the average number
waiting and the average time in line. Because adding service capacity reduces
waiting time but costs more, the design question is an explicit trade-off: the
total cost is "the sum of the waiting cost and the service cost," and the goal
is to choose the number of channels that minimizes that sum, not to eliminate
waiting altogether.

## In the Book

Chapter 11 develops the model through the Burger Dome fast-food restaurant, a
"single-channel waiting line" where every customer passes through one
order-taking station. The book models customer arrivals with the Poisson
probability function, working out that at an arrival rate of 45 customers per
hour there is a 0.4724 probability of zero arrivals, 0.3543 of one arrival,
and 0.1329 of two arrivals in any given minute — and uses this distribution,
paired with a service-time distribution, to derive Burger Dome's average wait
and queue length. The chapter then performs an economic analysis: it assigns
a waiting cost per customer per hour and a service cost per channel per hour
(estimated at $7/hour at Burger Dome), sums them across different numbers of
service channels, and shows that the total-cost curve is minimized at a
specific number of channels — more channels than that overspends on idle
service capacity, fewer starves customers with excessive waits.

## Why It Matters

Queueing theory replaces "add more capacity when things feel slow" with a
quantified trade-off between two costs that pull in opposite directions —
under-provisioning and letting the people or things waiting bear the cost, or
over-provisioning and paying for idle capacity. That same balance recurs
anywhere requests arrive unpredictably against a shared, limited server:
support agents, hospital beds, checkout lanes, or compute capacity, wherever
the honest question is not "how do we eliminate the wait" but "how much
capacity is the wait actually costing us to avoid."
