---
type: Concept
title: Automating Below the UI
description: Drive automated checks through an API, HTTP layer, or controller instead of a browser wherever possible — the interface is usually the slowest, flakiest place to verify business logic.
book: specification-by-example
chapters: [9]
tags: [test-automation, architecture, reliability, feedback-loops, layering]
created: 2026-07-12
---

# Automating Below the UI

## Definition

Business logic can almost always be checked without driving it through a full user interface, and doing so is usually a mistake: UI automation is slow, brittle, and typically locks a machine to one test at a time. The pattern is to automate "below the skin of the application" — against the HTTP layer, an internal controller, or a service API — reserving true end-to-end UI automation only for the handful of workflow or session rules that genuinely can't be checked any other way, and for building initial trust with skeptics.

## In the Book

Chapter 9 gives two concrete implementations. Tim Andersen's team at Iowa Student Loan sent hash-maps that mirrored real HTTP requests directly to the application, bypassing the browser while still exercising real code paths and real object state — he separately describes deleting a third of their test code once they stopped faking state and used the real system to set it up. Christian Hassa went one layer deeper, binding most specifications directly to the MVC controller rather than the UI, reserving Selenium-driven UI binding for a limited set of cases, because "binding to the UI costs significantly more." The chapter also covers automating along system boundaries rather than end-to-end: Rob Park's team, integrating with a voice-to-data conversion system they didn't own, built a test page that fed in prepopulated data instead of running real voice input through every test, isolating their actual responsibility (what happens after conversion) from a component they didn't control — leaving full end-to-end confidence to separate, smaller technical integration tests.

## Why It Matters

The layer where you verify something and the layer where a user experiences it don't have to be the same layer — checking behavior closer to the logic that produces it is nearly always faster and more reliable than checking it through the full presentation stack, whether that stack is a browser, a physical interface, or a bureaucratic process. The same reasoning applies to drawing a boundary around what you're actually responsible for verifying: isolating a system you depend on but don't control turns an unreliable, unautomatable end-to-end check into a fast, reliable check of your own logic plus a much smaller integration test for the seam.
