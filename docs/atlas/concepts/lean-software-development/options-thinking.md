---
type: Concept
title: Options Thinking
description: Treat the right (not obligation) to act later as something worth paying for, because it limits downside while preserving upside when the future is uncertain.
book: lean-software-development
chapters: [3]
tags: [uncertainty, decision-making, risk, optionality, delayed-commitment]
created: 2026-07-12
---

# Options Thinking

## Definition

An option is the right, but not the obligation, to do something in the future — like a satisfaction-guaranteed return policy, a hotel reservation, or a financial options contract. Options cost something to hold, but they let you commit to action only once uncertainty resolves in your favor, capping the loss from a bad outcome to the option's price while leaving the upside of a good outcome open. Delaying an irreversible decision has real economic value precisely because it lets more information arrive before the decision must be locked in.

## In the Book

The chapter's central case is Hewlett-Packard, which used to configure printers for local electrical outlets at the factory and chronically mismatched supply to demand across countries; moving that configuration step to the warehouse — after the order arrived — cost more per unit but saved $3 million a month by always shipping the right product. Economist Enrico Zaninotto's framing (cited from an XP2002 keynote) contrasts this "just-in-time" strategy of keeping options open with Fordist mass production's strategy of eliminating options ("any color as long as it's black"), and argues the option-preserving system wins in complex, dynamic markets. The book then widens the lens to Microsoft's 1988 strategy of hedging simultaneously across DOS, Windows, OS/2, and Unix rather than betting on one platform, and to Harold Thimbleby's 1988 paper "Delaying Commitment," which the authors use to distinguish amateurs (who commit early and get it wrong) from experts (who delay commitments deliberately and use the extra time to learn). The chapter's punchline for software: agile processes are best understood as a way of creating options — deferring detailed requirements and technical framework decisions until customer needs and technology have had time to clarify — while cautioning that options aren't free and holding the wrong ones (as IBM did, ceding software options to Microsoft) is itself a cost.

## Why It Matters

Most planning language treats uncertainty as something to eliminate by deciding early and firmly. Options thinking reframes it as something to price: an unresolved uncertainty has a value if you can structure your commitment so you only pay it once the answer favors you. This turns "we don't know yet" from an excuse for indecision into a design constraint — build the capability to delay commitment cheaply, rather than either guessing now or refusing to decide at all.
