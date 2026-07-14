---
type: Concept
title: Meta-Testing
description: You can assess the quality of a process from indirect, incidental signals lying around it — without ever executing the thing it produces.
book: perfect-software
chapters: [5]
tags: [meta-information, diagnosis, organizational-behavior, observation, testing]
created: 2026-07-12
---

# Meta-Testing

## Definition

Meta-testing is gathering "meta-information" — information about the quality of an organization's information — from signals that are just lying around, unrelated to running the software itself. A manager's offhand remark, a document nobody can locate, or an emotionless report of an absurd metric often reveals more about whether a development process is trustworthy than the test results it produces.

## In the Book

Weinberg frames this with an analogy from his wife Dani's dog-training practice: a client complains her puppy poops on the rug, and only when asked about other behavior problems mentions, unprompted, that the dog also scratches and whines at the door — the two "separate" problems are one problem (he needs to go out) that she was too close to see. He then runs a set of parallel "Sheltie stories" from testing: a test manager who says they "have specs" but doesn't know where they are (and guesses a month to find them); a team whose bug database degrades above 14,000 open reports, discussed with no emotion, revealing a development process generating bugs faster than they're resolved; a tester who calls the three "best" components good because they have low bugs-per-line, when 70 percent of that code hadn't even been checked in yet; severity ratings on a bug report that had been white-correction-fluided to look less severe; a tester who won't log a bug because "it's not in my component"; a general manager who shipped a buggy product because "our tests proved it was correct." In each case, the diagnostic information isn't the bug count — it's the process failure or blind spot the anecdote exposes.

## Why It Matters

This gives you a way to audit any process — quality, financial, safety — without re-running it yourself: look for the offhand, unemotional, or absurd detail that the people inside the system don't flag as a problem, because that blindness is itself the signal. It's a cheap, fast alternative (or complement) to deep technical review whenever you're an outsider trying to size up whether to trust an insider's numbers.
