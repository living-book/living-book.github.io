---
type: Concept
title: "Technical Debt and Operability: Design for Operations"
description: Systems accumulate technical debt when built for features only, generating unplanned work in operations; operability must be designed in from the start—not retrofitted.
book: phoenix-project-devops
chapters: [15]
tags: [technical-debt, operability, architecture, dev-ops-integration]
created: 2026-07-12
---

# Technical Debt and Operability: Design for Operations

## Definition

Technical debt in IT operations is the gap between a system as developed (optimized for features and speed-to-market) and a system as operationally viable (designed for stability, security, scalability, manageability, and continuity). The more features are piled on without building in operability, the greater the unplanned work burden Operations inherits. Operability cannot be retrofitted after the toothpaste is out of the tube; it must be a first-class design priority from the start.

## In the Book

When Bill complains that unplanned work in Operations is being caused by the Phoenix project itself, Erik responds: "Of course Phoenix is causing all the problems. You get what you design for. Chester, your peer in Development, is spending all his cycles on features, instead of stability, security, scalability, manageability, operability, continuity, and all those other beautiful other 'itties." Erik then points out that the one person who understands technical debt best is too busy firefighting: "the person who knows the most about where your technical debt is and how to actually build code that is designed for Operations is too busy. You know who that person is, don't you?" Bill responds: "Brent."

The systemic problem is that Development optimizes for delivery speed and feature count, while Operations suffers the consequences of systems not designed for production reality. Erik insists: "You need to design these things, what some call 'non-functional requirements,' into the product" from the start, not try to bolt them on later during operations. Without Brent's involvement in architecture meetings, Development builds systems that Operations cannot operate efficiently, creating a vicious cycle of technical debt.

## Why It Matters

This concept exposes a hidden organizational dependency: the developer who understands operations best is the same person who is drowning in firefighting, so they cannot prevent the next crisis. It reframes technical debt not as a code cleanliness issue but as a production-readiness issue that directly converts to unplanned operational work. It explains why operations teams feel powerless—they are solving a design problem at runtime, which is nearly impossible. Finally, it makes the case for integrating operations thinking into development from the design phase, not the deployment phase.
