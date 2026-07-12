---
type: Concept
title: Expected Value of Information
description: The economic worth of reducing uncertainty before a decision equals the reduction in expected opportunity loss — which tells you what, and how much, to measure.
book: how-to-measure-anything
chapters: [7]
tags: [decision-analysis, value-of-information, risk, opportunity-cost]
created: 2026-07-12
---

# Expected Value of Information

## Definition

Expected Opportunity Loss (EOL) is the chance of making the wrong decision times the cost of being wrong. The Expected Value of Information (EVI) of a measurement is the reduction in EOL it would produce: EVI = EOL(before) − EOL(after). The easiest bound to compute is the Expected Value of Perfect Information (EVPI) — what you'd gain if uncertainty were eliminated entirely, which is simply the EOL of whatever you'd otherwise default to doing. Since EVPI caps how much any measurement could possibly be worth, it tells you immediately which uncertain variables are worth measuring at all, and which aren't.

## In the Book

Chapter 7 builds the calculation from a simple binary case: an ad campaign that nets $40 million if it works and loses $5 million (the campaign cost) if it fails, with a calibrated 40% chance of failure. Approving it has an EOL of $5m × 40% = $2 million; rejecting it has an EOL of $40m × 60% = $24 million — so the most you could ever gain by eliminating uncertainty about this campaign's success is $2 million (the EVPI of the "approve" default). Hubbard then extends this to continuous ranges: a calibrated marketer is 90% certain the campaign will sell between 150,000 and 300,000 units, the firm needs 200,000 to break even at $25 margin per unit, and a "loss function" (zero above breakeven, proportional below it) lets him slice the probability distribution into thousands of segments, multiply each segment's opportunity loss by its probability, and sum to get an EVPI of about $200,000. He generalizes the finding from many client projects: the vast majority of variables in a typical decision model turn out to have negligible information value and don't need measuring further, while a small number of surprising variables carry almost all the value — which is what lets an analyst target measurement effort instead of trying to reduce uncertainty everywhere at once.

## Why It Matters

This turns "what should we measure?" from a guess into a calculation: instead of assuming more data is always better, you can rank every uncertain variable in a decision by how much resolving it is actually worth, and stop measuring once the cost of more precision exceeds its expected payoff. That logic applies wherever information gathering competes for a limited budget — research, due diligence, testing, surveys — because it prices uncertainty reduction in the same currency as everything else in the decision.
