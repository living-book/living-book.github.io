---
type: Concept
title: "adVANTAGE: A Contract Model for Agile Client-Contractor Partnerships"
description: "A commercial framework that enables fair agile delivery by distributing risk and reward equally, using two daily rates and feature-based budgeting instead of fixed-price or time-and-materials."
book: tamed-agility
chapters: [11, 12, 13, 14, 15, 16, 17]
tags: [contracting, risk-sharing, commercial-models, agile-delivery, incentive-alignment]
created: 2026-07-15
---

# adVANTAGE: A Contract Model for Agile Client-Contractor Partnerships

## Definition

adVANTAGE (agile development advantage) is a contract and pricing model for software projects delivered by external contractors under agile conditions. It combines three elements: a price structure using two daily rates (a "normal" rate for work within estimated effort, and a "painful" rate for overruns that do not generate profit for either party), a contract framework establishing mutual obligations, and project procedures (sprint planning, billing, sprint inspection) embedded in the Interaction Room workflow. The model distributes price risk equally between client and contractor, creating aligned incentives: neither party profits from scope creep, both suffer from delays, so both focus on delivering lean software efficiently.

## In the Book

Traditional contracts (fixed-price, time-and-materials, pay-per-use) each assign risk to one party: fixed-price puts cost risk on the contractor (incentivizing underbidding), T&M puts it on the client (incentivizing scope creep), and pay-per-use requires the contractor to predict usage. None fit agile uncertainty well.

adVANTAGE uses a base rate (BR)—a fixed fee per sprint covering planning, scrum master, meetings, warranty—plus dynamic billing on actual development effort. At the start, the team estimates effort for each feature in person-days. These estimates are *never retouched* unless entirely new features arise; they are understood to be uncertain guesses. Two daily rates are negotiated: DR₁ (market rate with profit margin, applied to estimated work) and DR₂ (deliberately set to "painful" level, near cost of production, applied only to overruns). At each sprint's end, effort up to the estimate is billed at DR₁; overages are billed at DR₂. The contractor shares pain: overruns don't generate profit. The client shares benefit: can negotiate a gain-share clause where cost savings from finishing under budget are split (e.g., 50-50).

The book describes procedures: initial requirements collection via Interaction Room to create feature list and estimates, sprint planning workshops with the client, daily billing rules with no debate about whether slippage was "the client's fault" (pain is shared, so blame is irrelevant), and a risk map that surfaces uncertainties early. The Cura case study shows this in practice: a complex insurance benefit system was scoped in an Interaction Room, sprints were planned and monitored using the same collaborative model, and the adVANTAGE pricing ensured both sides stayed focused on lean delivery.

## Why It Matters

adVANTAGE matters because it makes agile sustainable in commercial relationships. Pure agile doctrine says "embrace change" and "trust the team," but a client who has signed a contract for $500k has a legitimate need to understand cost exposure; a contractor bearing all downside risk will underbid or refuse the work. adVANTAGE solves this by acknowledging that neither party controls all variables (client doesn't fully know requirements in advance, contractor doesn't control team productivity), so splitting the risk is fairer than assigning it whole. The two-rate mechanism is elegant: it removes arguments about blame (both share the pain) while creating incentives (the contractor avoids DR₂ through efficiency; the client avoids DR₂ through clear specifications). It is a structural solution to the principal-agent problem in software outsourcing.
