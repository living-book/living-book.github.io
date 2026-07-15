---
type: Concept
title: "Sustained Engineering with Kanban"
description: "Applying Kanban to post-release bug fixing and maintenance using separate swim lanes for escalations and bugs, with triage, quick-solve meetings, and clear support tier definitions."
book: agile-pm-with-kanban
chapters: [8]
tags: [kanban, operations, bugs, support]
created: 2026-07-15
---

# Sustained Engineering with Kanban

## Definition

After a product ships, a dedicated team (or set of team members) handles customer-reported issues, bugs, and escalations. Brechner's approach is to apply Kanban to this work with two swim lanes: one for escalations (customer support issues that may not require code changes) and one for bugs (code fixes and technical work). Each swim lane has its own Specify, Implement, Validate steps and done rules. Incoming escalations are triaged to minimize distractions, "quick-solve" meetings resolve support issues without code changes, and the team uses test-driven development for bug fixes to prevent regressions.

## In the Book

Chapter 8 describes a sustained-engineering (SE) team: "Most teams that release a product or service to customers perform software maintenance after release." The team has customer support, product management, and core engineering collaborating. Escalations arrive from customer support; the SE team triages them on the first swim lane, quickly resolving what doesn't need code. Bugs land on the second swim lane after triage. Done rules for SE bugs include testing (especially test-driven: write a test that fails, fix the code, test passes) and root-cause analysis to prevent similar bugs in future releases.

Key mechanisms: Support tiers clarify handoffs (Tier 1 support handles common issues, Tier 2 SE engineers handle technical issues, Tier 3 core engineering handles architecture changes). A "parking lot" holds low-priority work that's not in the active swim lanes. The Kanban board makes SE team contribution visible—leadership sees how many escalations were resolved and bugs fixed, not just time spent. Because the team is measured on sustained engineering and given similar respect as feature development, morale stays high.

## Why It Matters

Post-release support is often invisible or treated as overhead. Applying Kanban makes it a flow that can be measured and improved. The two swim lanes prevent escalations (often quick context-switching problems) from burying bug fixes (which need sustained focus). Triage and quick-solve meetings prevent support from consuming all capacity; the SE team can then focus on root causes. Test-driven bug fixing builds up a regression test suite over time, reducing future defects. By making SE work visible on the Kanban board (not hidden in a support ticket system), the entire organization sees its value and the team doesn't feel marginalized. This is distinct from traditional post-release support models where SE is reactive and low-status; here it's a valued, measured workflow.

---

*related concepts: kaizen-culture (CATALOG), failure-demand (CATALOG), help-chains (CATALOG)*
