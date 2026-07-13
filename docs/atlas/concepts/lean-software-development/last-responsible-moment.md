---
type: Concept
title: The Last Responsible Moment
description: Delay a commitment until the point where failing to decide would eliminate an important alternative — any later is procrastination, any earlier is a guess.
book: lean-software-development
chapters: [3]
tags: [decision-making, timing, commitment, concurrent-development, uncertainty]
created: 2026-07-12
---

# The Last Responsible Moment

## Definition

The last responsible moment (a term the book credits to the Lean Construction Institute) is the point at which not making a decision starts to eliminate an option you'd otherwise still have. Delaying past that point means the decision gets made by default rather than deliberately — which the book treats as a bad outcome, not a virtue of patience. Reaching that moment deliberately, rather than either committing early or drifting past it, is hard, active work, not procrastination.

## In the Book

Chapter 3 makes concurrent development the enabling mechanism: teams start work with only partial requirements and use short iterations to let the system emerge, which is what makes late commitment survivable rather than reckless. The chapter lays out concrete tactics for actually operating this way — releasing partial design information instead of waiting for completeness, organizing direct worker-to-worker collaboration so refinement can happen as understanding grows, and a long list of design techniques borrowed from object-oriented practice (modules, interfaces, parameters, abstraction, avoiding custom-tool investment, DRY/OAOO, YAGNI, encapsulating what's likely to change) that the authors read collectively as commitment-deferral tools, following Harold Thimbleby's "Delaying Commitment." It also names the failure mode on the other side: "a bias toward late commitment must not degenerate into a bias toward no commitment" — some things (usability architecture, layering, component packaging) are best decided early precisely because they enable everything downstream to emerge safely. The chapter closes by noting that response speed sets how late you can decide: Dell can decide what to build a week before shipping because it can assemble a computer in under a week, so quick-response capability is itself what buys you a later last responsible moment.

## Why It Matters

"Decide as late as possible" is easy to hear as an excuse for indecision; this concept supplies the missing discipline — there is a specific, identifiable moment tied to which alternatives you'd lose, not a vague preference for lateness. It converts a vague slogan into an operational test you can apply to any pending decision: what do we actually still learn by waiting, and what do we lose if we wait one beat longer than that?
