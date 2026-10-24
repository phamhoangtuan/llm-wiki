---
title: "Python Concurrency"
type: concept
tags: [python, concurrency, gil]
created: 2026-06-12
updated: 2026-06-15
sources: [intuitive-python]
aliases: [GIL, Python threading, Python multiprocessing]
---

# Python Concurrency

Python's concurrency model, constrained by the Global Interpreter Lock (GIL), offers two distinct paradigms — threads and processes — each suited to different workloads. The professional instinct is to **prioritize safety over perceived speed**.

## The Race Condition Trap

Classic illustration of why concurrency is dangerous without proper synchronization:

```
Account balance: $8. Two processes run simultaneously:
1. Process A reads balance: $8
2. Process B reads balance: $8
3. A withdraws $6 → writes $2
4. B withdraws $7 → had read $8, allows transaction → writes $1
→ Result: $13 withdrawn from an $8 account
```

Race conditions are **non-deterministic** — they may pass tests 99% of the time and fail in production under specific timing conditions.

## Threads vs Processes

| Dimension | Threads (`threading`) | Processes (`multiprocessing`) |
|---|---|---|
| **Shared Memory** | Yes — all threads share the same memory space | No — each process has independent memory |
| **GIL Bound** | Yes — only one thread executes Python at a time | No — each process has its own GIL |
| **Overhead** | Low — lightweight, quick to spawn | High — separate interpreter per process, serialization cost |
| **Data Sharing** | Easy — shared variables (but needs locks) | Hard — must serialize via `Queue` or `Pipe` |
| **Best For** | **I/O-bound** work: API calls, file reads, network requests | **CPU-bound** work: heavy computation, large data processing |

## When to Use Concurrency

The senior developer's decision tree:

1. **Can this be solved without concurrency?** — Single-threaded code is always simpler, safer, and easier to debug
2. **Is it I/O-bound?** — Threads (`threading` or `asyncio`) let other work proceed while waiting
3. **Is it CPU-bound?** — Processes (`multiprocessing`) bypass the GIL for true parallelism
4. **Must it be fast AND correct?** — Only then introduce concurrency, with rigorous testing

## Python-Specific Considerations

The **GIL** (Global Interpreter Lock) prevents true parallel execution of Python bytecode within a single process. This means:
- Threads are **not** suitable for CPU-heavy work (no speed gain)
- Threads **are** suitable for I/O work (the GIL is released during I/O operations)
- For CPU-bound parallelism, use `multiprocessing` or external libraries (NumPy, C extensions)

---

- Core to [[python-professional-practices]] — professional judgment on when to use concurrency
- Related to [[readability-vs-performance]] — safety over premature optimization
- Related to [[fail-fast]] — race conditions as silent, intermittent failures
- Covered by [[sources/intuitive-python]] — David Muller's guide to Python concurrency (threads, processes, GIL)
