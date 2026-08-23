---
title: "Algorithm Analysis"
type: concept
tags: [algorithms, performance, operation-counting, doubling-effect]
created: 2026-08-23
updated: 2026-08-23
sources: [learning-algorithms-heineman]
aliases: [operation counting, key operations, doubling effect]
---

Algorithm analysis is the discipline of predicting how an algorithm behaves as input grows, without running it. The core method: **count key operations, not clock time**.

## Why Not Timing?

Clock-based measurement is unreliable for three reasons:

1. **Platform variation** — same code runs at different speeds on different hardware
2. **Language variation** — same logic in C vs Python differs by orders of magnitude
3. **Data sensitivity** — `max()` on ascending data is slower than on descending data

> "Timing tells you WHAT happened. Operation counting tells you WHY it happened." (source: [[learning-algorithms-heineman]])

## The Method

1. **Identify the key operation** — the single most important action the algorithm performs (e.g., `<` comparison for finding the maximum)
2. **Count it as a function of N** — express the count mathematically: C(N) = N − 1
3. **Test the doubling effect** — double N and observe: does work double (linear), quadruple (quadratic), or stay constant?
4. **Classify with [[big-o-notation]]** — map the growth pattern to a performance class

## Best Case vs Worst Case

An algorithm's work depends on data arrangement:

- **Best case**: input requiring least work (e.g., first element is the maximum → N ops)
- **Worst case**: input demanding most work (e.g., ascending order → O(N²) ops)

Always analyze the worst case. An algorithm must work for ALL problem instances, not just convenient ones.

## The 4 Layers of Computer Science

Understanding algorithms requires understanding what they're built on:

| Layer | What | Examples |
| ------- | ------ | ---------- |
| 1. Primitives | Raw data atoms | int, long, float, double |
| 2. Data Structures | Physical memory layout | Arrays, linked lists, heaps, trees |
| 3. Abstract Data Types | Logical operation blueprints | Stack, Queue, Symbol Table, Graph |
| 4. Algorithms | Execution strategies | largest(), binary search, merge sort |

Each layer constrains the one above. Physical layout choices (contiguous array vs linked list) dictate the cost of find/add/delete operations, which in shape the algorithms that can be built on top.

## Connections

- Produces [[big-o-notation]] classifications as output
- Must account for [[time-space-tradeoff|space complexity]] alongside time
- Complements [[complexity-metrics]] — structural metrics measure the code itself; algorithm analysis measures the logic's growth
- Informs [[readability-vs-performance]] — analyze first, optimize bottlenecks, don't premature-optimize
