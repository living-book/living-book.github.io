---
type: Concept
title: "Modular Decomposition"
description: Breaking systems into smaller, independent modules simplifies each unit but requires careful design of interfaces to avoid new coordination complexity.
book: simplicity-de-bono
chapters: [1, 3]
tags: [systems-design, modularity, decentralization, interfaces, complexity]
created: 2026-07-15
---

# Modular Decomposition

## Definition

One approach to simplification is to break large systems into smaller modules, each with its own simpler internal organization. This works well when modules can operate independently and integrate cleanly. However, the trade-off is that the interfaces between modules can become complex, and coordination overhead can negate the gains.

## In the Book

De Bono discusses modular design as a fundamental simplification strategy: "There is the modular approach to simplicity. In setting things up a few standard modules are coupled together. Different standard modules may be put together to give a variety of products."

He cites General Motors' alleged approach to car production and Dell's custom computer business: using standard modules that can be recombined to create variety. The advantage is clear: "The organization of a smaller unit is obviously simpler than the organization of a large unit." Modular design also simplifies diagnosis and repair: "The modular approach makes diagnosis and repair easier. You check each module and repair the one that is faulty."

However, De Bono emphasizes the critical caveat: "Breaking things down into smaller units, decentralization and modular design are all approaches to simplicity—so long as the unity of the overall purpose is not lost." He warns against over-modularization: "Modularization, chunking and creating units is one of the basic approaches to simplification—but it can be overdone."

The book also warns that decentralization can introduce chaos: "When every decision and every order has to come from a central command and filter down through other layers of command, the system becomes complex. When local leaders have the ability to make their own decisions within clearly defined frameworks and with clearly defined general objectives, then the system is simpler and more responsive. The emphasis has to be on the 'defined' framework."

## Why It Matters

This concept clarifies that modularity is not a panacea. The hidden cost of modular design is the interface complexity and coordination overhead. Effective modular design requires strong, clear standards and frameworks that allow modules to integrate without constant negotiation. This applies to software architecture (microservices simplify individual services but complicate deployment and data consistency), organizational structure (decentralization simplifies decision-making at local levels but complicates overall coordination), and physical systems (standardized parts simplify assembly but require careful interface design).
