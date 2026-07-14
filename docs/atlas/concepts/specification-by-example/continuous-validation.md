---
type: Concept
title: Continuous Validation
description: Running executable specifications on every change, the way continuous integration runs builds, catches drift from the right product while it is still small and cheap to fix.
book: specification-by-example
chapters: [10]
tags: [feedback-loops, testing, reliability, continuous-integration, drift]
created: 2026-07-12
---

# Continuous Validation

## Definition

A team that builds the right product once has no guarantee it stays right — code changes, and nothing catches drift unless something is actively watching for it. Continuous validation extends continuous integration's build-and-unit-test loop to executable specifications: a build server frequently re-runs the full set of specifications so that any divergence from agreed business behavior is caught within hours, not discovered months later during a demo or a customer complaint. Because functional specifications often depend on databases, external services, or a deployed environment, keeping this loop fast and reliable takes more deliberate engineering than plain continuous integration does.

## In the Book

Chapter 10 opens with Dr. Elbert Dysart Botts, who solved California's fading-lane-marker problem not with better paint but with raised, tactile "Botts' Dots" that make drivers physically feel it the instant they drift — the direct inspiration, Adzic notes, for continuous integration as an Extreme Programming practice: cheap, immediate feedback the moment something goes off course. He then documents the three problems specific to validating executable specifications continuously (as opposed to unit tests): environmental unreliability, slower feedback (acceptance packs that must run for hours), and the discipline of managing failing tests rather than ignoring them. Clare McLennan's team illustrates the fix for unreliability: developers wouldn't trust unstable tests, so she worked through problems one at a time — slow test data processing, then stale-data race conditions, then HTTP cookie expiry (fixed by introducing a controllable "business time") — following her own rule to "find the most annoying thing, fix it, and repeat" rather than attempting one large rewrite.

## Why It Matters

Any system that can silently drift from a known-good state — code from its spec, a process from its policy, a physical system from its calibration — benefits from a cheap, frequent, automatic check rather than periodic manual inspection, because the cost of catching drift rises with how long it's gone unnoticed. The reliability engineering this requires (isolating environmental noise, making feedback fast enough to act on, deciding what happens when a check fails) is itself a transferable discipline, and McLennan's "fix the most annoying thing and repeat" is a general strategy for stabilizing any large, entangled system incrementally rather than through one big rewrite.
