---
type: Concept
title: Compounding and Discounting
description: Money grows geometrically when interest is paid on interest, and that same geometric relationship run backwards converts any future sum into its present value.
book: mathematics-for-economics-and-business
chapters: [3]
tags: [finance, geometric-growth, time-value, decision-making, measurement]
created: 2026-07-14
---

# Compounding and Discounting

## Definition

Under compound interest, a principal P invested at rate r% for n periods grows to a future value S = P(1 + r/100)ⁿ, because each period's interest is earned on the previous period's total, not just the original principal — "interest on the interest." Discounting reverses this: given a known future value S, the present value P = S(1 + r/100)⁻ⁿ (or P = Se^(−rt/100) under continuous compounding) is the amount that must be invested today to reach S. Net present value (NPV) — the present value of a project's returns minus the present value of its costs — is positive exactly when a project is worth undertaking.

## In the Book

Section 3.2 builds compound interest from a concrete case: $500 invested at 10% annually earns $50 in year one (raising the total to $550), then $55 in year two — 10% of $550, not $500 — because interest is now earned on the earlier interest, reaching $665.50 after three years versus what simple interest would give. The book generalises this via the "scale factor" 1.1, showing S = P(1.1)ⁿ, then S = P(1 + r/100)ⁿ in general. Section 3.4 inverts the formula to define discounting and present value, working a direct example — the present value of $1000 in four years at a 10% discount rate is $676.84 compounded semi-annually versus $670.32 compounded continuously, illustrating that continuous compounding always yields a higher return (so a smaller present value is needed to hit the same target). The section then applies this to a $600-outlay venture returning $1000 in five years, computing NPV = $676.84 − $600 = $76.84 to show the venture is profitable, and extends the machinery to annuities by summing a geometric series of individually discounted payments.

## Why It Matters

The core insight — that a fixed proportional growth rate compounds geometrically rather than additively — is exactly why money now is worth more than the same money later, and it is the same mathematics that governs population growth, radioactive decay, and any process where the rate of change is proportional to the current amount. Discounting supplies the general answer to "how do I compare a benefit received later against a cost paid now?": convert everything to a common point in time by inverting the growth formula, a move that generalises far beyond finance to any decision that trades a present cost for a delayed, larger payoff.
