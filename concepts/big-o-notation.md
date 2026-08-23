---
title: "Big O Notation"
type: concept
tags: [algorithms, complexity, performance, asymptotic-analysis]
created: 2026-08-23
updated: 2026-08-23
sources: [learning-algorithms-heineman]
aliases: [asymptotic analysis, big-O, complexity classes]
---

Big O notation is the standard vocabulary for describing how an algorithm's resource consumption grows as input size (N) increases. It abstracts away hardware, language, and constants to focus on the **growth pattern**.

## Performance Classes

| Class | Notation | Growth on N doubling | Example |
| ------- | ---------- | --------------------- | --------- |
| Constant | O(1) | No change | Array access `A[i]` |
| Logarithmic | O(log N) | +1 step | Binary search |
| Linear | O(N) | Work doubles | Single scan for max |
| Linear-log | O(N log N) | Slightly more than double | Merge sort, quicksort |
| Quadratic | O(N²) | Work quadruples | Bubble sort, nested comparisons |

## Why It Matters

At N = 1,000, O(N²) means 1,000,000 operations — manageable. At N = 1,000,000, it means 1,000,000,000,000 — catastrophic. The growth pattern, not the absolute speed, determines whether code survives contact with real data.

## The "Slower Computer" Paradox

An efficient algorithm (O(N log N)) on a slow machine will eventually outperform an inefficient algorithm (O(N²)) on a supercomputer. No amount of hardware can compensate for asymptotic inferiority at scale. (source: [[learning-algorithms-heineman]])

## Relationship to Other Concepts

- **Operation counting** is the method; Big O is the classification. Count key operations, observe the doubling pattern, then classify. See [[algorithm-analysis]].
- Big O describes [[time-space-tradeoff|time complexity]] specifically; space complexity uses the same notation for memory growth.
- Distinct from [[complexity-metrics]] like Halstead or Cyclomatic complexity, which measure code structure rather than algorithmic growth.
- System-level scaling ([[scalable-architecture]]) addresses different problems than algorithm-level scaling (Big O), but both matter for production systems.
