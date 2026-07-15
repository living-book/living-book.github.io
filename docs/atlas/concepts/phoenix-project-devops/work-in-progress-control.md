---
type: Concept
title: "Work-in-Progress Control: Visual Management for IT Operations"
description: Controlling how much work starts before previous work finishes, using visual kanban boards and WIP limits to expose bottlenecks and stabilize flow in IT operations.
book: phoenix-project-devops
chapters: [7, 15]
tags: [wip, kanban, visual-management, flow-control]
created: 2026-07-12
---

# Work-in-Progress Control: Visual Management for IT Operations

## Definition

Work-in-progress (WIP) is the amount of work that has started but not finished. Controlling WIP means setting explicit limits on how much work can be active at each stage of IT Operations (changes, deployments, incident handling, project work). Visible WIP limits expose bottlenecks immediately: when a stage hits its limit, new work cannot start, forcing the organization to finish what it began before starting something new. This is the mechanical implementation of flow control and is the foundation for predictable, stable IT operations.

## In the Book

Bill Palmer and his team introduce a simple change management board using index cards representing each change. This visual management tool allows the team to see WIP directly: which changes are in planning, which are in testing, which are waiting for deployment. When the change board shows zero completions in a week—every single card stuck in progress—the problem becomes undeniable in a way no report could make it. This is WIP transparency: the system cannot hide that work is starting faster than it finishes.

Erik Reid references David J. Anderson's work on kanban for IT operations: "David J. Anderson developed techniques of using a kanban board to release work and control WIP for Development and IT Operations." He advises Bill to set work release by the tempo of the constraint's consumption rate, not by the speed at which work arrives: "You must figure out how to set the tempo of work according to Brent" so that work flows through the system at a predictable pace. The goal is to move from "we start too much work" to "we release only as much work as we can finish."

## Why It Matters

WIP limits are one of the few mechanisms that automatically exposes system-level problems without waiting for a crisis. High WIP creates long lead times, context-switching overhead, and delays in feedback. By making WIP visible and then capping it, an organization forces itself to finish before starting, which reveals the real bottlenecks and makes improvement concrete and measurable. It also explains why adding more resources to "busy" teams does not always help—if WIP is uncontrolled, adding people often increases WIP and makes things worse. Finally, it provides a mechanical lever for the First Way (flow): you cannot have fast flow without WIP control.
