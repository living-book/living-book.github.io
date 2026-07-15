---
type: Concept
title: "Stable Trunk for Multi-Team Development"
description: Keep the main code branch always ready for system test through disciplined team branches, daily merge-downs, and feature-level validation before integration.
book: lean-from-the-trenches
chapters: [14]
tags: [version-control, integration, coordination, technical-excellence]
created: 2026-07-15
---

# Stable Trunk for Multi-Team Development

## Definition

In a multi-team environment, maintain a mainline (trunk) branch that is always stable and deployable, never broken. Each team has a team branch for daily development (looser rules: code must compile, unit tests pass, but features don't have to be complete). Teams merge down from trunk to their branch daily to stay in sync. When a feature is complete and feature-tested, the team merges up to trunk only after ensuring the merge is clean and the feature still works. Broken trunks are discovered immediately by continuous integration and fixed at once. System test branches are spawned from the trunk for testing, isolated from ongoing development.

## In the Book

PUST suffered from serious version control problems as it scaled. At one point, the trunk was broken for extended periods, branches diverged badly, and teams wasted days on merge conflicts and integration thrash. They implemented the stable trunk model: the trunk must be ready for system test at all times; teams have permissive team branches where developers check in unfinished work daily; every morning, team leads merge trunk changes down to the team branch; when a feature is done, teams thoroughly feature-test it, merge down from trunk one last time, then merge up. The CI system immediately builds and tests the trunk after every merge. If something breaks, everyone stops to fix it (or rolls back). This discipline meant the trunk was always in a state where you could branch off for system testing without waiting, and bug fixes on system test branches merged back up to trunk so all teams got the fix immediately.

## Why It Matters

This pattern inverts the pain of multi-team development. Rather than each team suffering the cost of integrating other teams' work, the cost is distributed: every team pays a small daily cost (merge-down, merge conflict resolution) to stay in sync, and the overhead of feature-level validation before integrating upward. The result is no big integration bang, no late-cycle surprises. Changes ripple through the organization in days, not weeks. This is foundational for any scaling scenario where multiple groups must ship one product—hardware, infrastructure, large software systems.
