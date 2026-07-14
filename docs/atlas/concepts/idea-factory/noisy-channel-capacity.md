---
type: Concept
title: Information as Resolved Uncertainty
description: A message carries information in proportion to how unpredictable it is, and any channel has a hard capacity limit on how many such bits it can carry reliably.
book: idea-factory
chapters: [7]
tags: [information-theory, communication, measurement, uncertainty, limits]
created: 2026-07-14
---

# Information as Resolved Uncertainty

## Definition

Claude Shannon's "A Mathematical Theory of Communication" (1948) defined
information not by meaning but by surprise: "we take the essence of information
as the irreducible, fundamental underlying uncertainty that is removed by its
receipt." The less predictable a message, the more information it carries; a
predictable message (English text is 75-80% redundant, by Shannon's
calculation) can be compressed without losing content. He named the unit the
"bit," and proved that any channel has a maximum capacity — a hard ceiling on
information rate, exactly as a pipe caps a flow of water — beyond which
transmission quality degrades no matter how cleverly you encode.

## In the Book

Chapter Seven traces the theory from Shannon's wartime cryptography work,
where he found that reducing redundancy compresses a message (his own
example: "FCTSSTRNGRTHNFCTN" is still legible as "fact is stranger than
fiction"), to his 1948 communication paper, which generalized this into a single
framework covering any channel — lunchroom conversation, phone call, radio
signal — as an information source facing a noisy channel. Its most startling
claim, which "seemed impossible to many at the time," was the noisy-channel
coding theorem: any digital message can be sent with virtual perfection even
over the noisiest wire, as long as you add error-correcting bits, up to the
channel's capacity. The book frames this as the abstract, mathematical
counterpart to the transistor's physical breakthrough — the transistor gave Bell
Labs a device that could switch billions of times a second; Shannon's theory
gave engineers "a yardstick" for how much information any system could
actually move.

## Why It Matters

It separates the *quantity* of information a message carries from its *meaning*,
which is what makes "information" measurable and comparable across totally
different media — voice, text, video, DNA. It also hands you a diagnostic for
any communication problem: is the bottleneck a lack of signal (compress
smarter) or channel noise (add redundancy), and is the channel already running
at its ceiling, in which case no amount of engineering cleverness helps.
