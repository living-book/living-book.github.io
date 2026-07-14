---
type: Concept
title: "\"Let It Crash\" Fault Tolerance"
description: Instead of defensively catching every possible error, let a faulty process die outright and have a separate supervising process restart it clean.
book: seven-languages-seven-weeks
chapters: [6]
tags: [fault-tolerance, error-handling, supervision, reliability, distributed-systems]
created: 2026-07-12
---

# "Let It Crash" Fault Tolerance

## Definition

Rather than wrapping every operation in defensive error-checking to keep a process alive no matter what, Erlang's philosophy is to let a process that hits an unexpected state simply die, and rely on a separate, simpler monitoring process to notice the death and start a fresh replacement. Tate calls it "the Erlang mantra," and quotes Erlang's creator Joe Armstrong on why it works: "the whole notion of 'nondefensive' programming and 'Let It Crash'... is completely the opposite of conventional practice, but it leads to really short and beautiful programs."

## In the Book

Tate builds this concept with a concrete worked example rather than stating it abstractly. He writes a `roulette` process that "dies" (stops responding) after receiving the message `3`, then shows how a plain `receive` loop with no error handling leaves the caller unable to detect or recover from the death — later messages simply vanish. He then builds a `coroner` process that calls `link(Process)` on the roulette process and traps `'EXIT'` messages, so when the monitored process dies it receives `{'EXIT', From, Reason}` and can log the death. The example is then extended one step further into a `doctor` process that does the same monitoring but also automatically re-spawns a fresh roulette process whenever the old one dies — turning a coroner into a resurrector. Tate connects this directly back to the reliability story from the chapter's introduction: production Erlang systems built this way, using OTP's more formal supervision trees, "run for years without ever coming down for maintenance," because a crashed process is treated as a routine, cheap, recoverable event rather than a catastrophe requiring exhaustive defensive code at every call site.

## Why It Matters

Trying to anticipate and defensively handle every possible failure mode inline makes code longer, harder to read, and — because you can never truly enumerate every failure mode — still incomplete. Separating "detect that something failed" from "decide what to do about it" into two different pieces of code (the worker and its supervisor) lets the worker stay simple and honest about what it actually does, while reliability becomes the supervisor's one job. The same structural move shows up as circuit breakers and process supervisors in other software architectures, as well as outside software entirely: an organization that treats a failed initiative as something to kill and restart cleanly, rather than propping up indefinitely with patches, is applying the same underlying principle.
