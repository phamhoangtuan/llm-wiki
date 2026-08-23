---
title: "Learning Algorithms: A Programmer's Guide to Writing Better Code"
type: source
source_type: book
author: "George T. Heineman"
url: ""
source_date: 2021-01-01
ingested: 2026-08-23
tags: [algorithms, complexity, big-o, performance, data-structures]
concepts: [big-o-notation, algorithm-analysis, time-space-tradeoff, complexity-metrics]
---

## Summary

Heineman's 281-page guide bridges the gap between "code that works" and "code that scales." The central thesis: performance is not a hardware problem — it's a problem of logical structure. An efficient algorithm on old hardware will outperform an inefficient algorithm on a supercomputer when N is large enough.

The book is structured around progressively deeper layers of understanding, from primitive types through data structures, abstract data types, and finally algorithms themselves.

## Key Claims

### Timing Is Unreliable

Clock-based measurement is a trap. Timing varies by platform, language implementation, and — critically — by the data itself. `max()` on ascending values is always slower than on descending values. The lesson: **timing tells you WHAT happened; operation counting tells you WHY**.

### Count Key Operations

Instead of seconds, count the single most important action an algorithm performs — its "heartbeat." For finding the largest element in an array, that's the less-than (`<`) comparison. This gives a machine-independent, predictable metric.

### The Doubling Effect

When you double N, does the work double (linear, O(N)), quadruple (quadratic, O(N²)), or stay the same (constant, O(1))? This is the real test of an algorithm's scalability.

### Time-Space Trade-off

Mathematical efficiency ≠ practical efficiency. The tournament algorithm finds the two largest values with N + log N − 2 comparisons (vs. 2N − 3 for a standard scan) — but is the *slowest* in practice because it requires extra arrays (`winners[]`, `losers[]`, `prior[]`). Memory allocation overhead wipes out the comparison savings.

### Built-ins "Cheat"

Python's `max()` always outperforms a custom `largest()` because built-ins are implemented in C, bypassing interpreter overhead. Know when to use built-ins vs. custom logic.

### The 4 Layers of CS

1. **Primitives** — int, long, float, double (raw atoms)
2. **Data Structures** — Arrays, Linked Lists, Heaps, Trees (physical layout)
3. **Abstract Data Types** — Stack, Queue, Symbol Table, Priority Queue, Graph (logical blueprints)
4. **Algorithms** — Strategies of execution built on the layers below

### Karatsuba Multiplication

Grade-school multiplication is O(N²), but Python's Bignum uses Karatsuba (~N^1.585), bending the curve downward. Even "solved problems" can have better algorithms.

## Notable Examples

| Algorithm | Key Ops | Big O | Behavior when N doubles |
| ----------- | --------- | ------- | ------------------------ |
| `largest()` | N − 1 comparisons | O(N) | Work doubles |
| `alternate()` | (N² + 3N − 2)/2 | O(N²) | Work quadruples |
| `tournament_two()` | N + log N − 2 | O(N) | Fewer ops but more memory |
| Binary search | log N | O(log N) | +1 step per doubling |

## Connections

- Relates to [[complexity-metrics]] — Halstead and Cyclomatic complexity measure code structure; Big O measures algorithmic growth. Complementary lenses.
- Contrasts with [[readability-vs-performance]] — Heineman focuses purely on performance; the readability-first school says optimize bottlenecks *after* profiling.
- Extends [[scalable-architecture]] — system-level scaling (load balancers, sharding) matters, but algorithm-level scaling (O(N) vs O(N²)) matters more when N is large.
- Connects to [[essential-accidental-complexity]] — algorithmic inefficiency is essential complexity; platform overhead is accidental.
