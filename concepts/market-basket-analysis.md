---
title: "Market Basket Analysis"
type: concept
tags: [data-mining, algorithms, association-rules, mapreduce, spark, retail]
created: 2026-07-13
updated: 2026-07-13
sources: [data-algorithms]
aliases: [MBA, association-rule-mining, affinity-analysis]
---

## Summary

**Market Basket Analysis (MBA)** is a data mining technique that discovers co-occurrence patterns — items that frequently appear together in transactions. The output is a set of **association rules** of the form "if X → then Y" that power recommendation engines, store layout optimization, and cross-sell strategies.

## Core Metrics

| Metric | Formula | Meaning | Example |
|--------|---------|---------|---------|
| **Support** | `#txns containing {X, Y} / total txns` | How popular is this item combination? | 5% of all receipts have both Coke and Pizza |
| **Confidence** | `#txns containing {X, Y} / #txns containing {X}` | If they buy X, how likely are they to also buy Y? | 70% of pizza buyers also buy Coke |

> High Support + High Confidence = a strong, actionable rule. High Confidence but low Support may be statistically irrelevant.

## MapReduce Implementation

The canonical distributed MBA pipeline on MapReduce:

### Mapper Phase
```
Input:  One transaction = a set of items
Step 1: Sort items alphabetically (CRITICAL — prevents "coke,pizza" and "pizza,coke" from becoming different keys)
Step 2: Generate all item combinations (pairs, triples, ...)
Output: (combo, 1) for each combination
```

### Reducer Phase
```
Input:  (combo, [1, 1, 1, ...])
Output: (combo, total_count) — the frequency of each combination
```

> ⚠️ **Sorting is mandatory.** Without alphabetical sorting, identical itemsets in different orders become different keys, corrupting frequency counts.

## Spark vs Hadoop for MBA

| Framework | Capabilities | Best For |
|-----------|-------------|----------|
| **Hadoop/MapReduce** | Find frequent patterns (itemset counting) | Simple frequency counting |
| **Spark** | Full pipeline: patterns → association rules → confidence calculation | End-to-end MBA with rule generation |

Spark wins because in-memory processing enables multi-phase workflows (counting + rule generation + confidence computation) in a single unified pipeline without multiple MapReduce jobs.

## Applications Beyond Retail

| Industry | Application | Value |
|----------|------------|-------|
| E-commerce (Amazon, Shopee) | "Customers who bought this also bought..." | Cross-sell, user experience |
| Brick-and-mortar retail | Store layout — place correlated items near each other | Higher average order value |
| Finance / Credit cards | Transaction pattern analysis, anomaly detection | Fraud detection: broken patterns = stolen card |
| Health insurance | Claim fraud detection — services that should cluster appear in isolation | Cost savings |
| Telecom | Bundle design — which services are purchased together | Product packaging |

## Key Takeaways

1. MBA translates raw transaction data into actionable "if-then" business rules.
2. Support and Confidence are the two essential metrics for evaluating rule quality.
3. Always sort items in the Mapper — a small step that determines the entire pipeline's accuracy.
4. Spark is superior to Hadoop for MBA due to multi-phase in-memory processing.
5. Wherever transaction data exists (retail, finance, healthcare, telecom), MBA generates value.

---

- Runs on [[apache-spark]] — Spark is the preferred engine for end-to-end MBA pipelines with rule generation
- Related to [[data-engineer]] — MBA is a classic big-data problem that data engineers implement at scale
- Benchmark source: [[sources/data-algorithms]] — Parsian's 778-page guide to distributed algorithms including MBA
