---
title: "Data Algorithms"
type: source
source_type: book
author: "Mahmoud Parsian"
url: ""
source_date: 2026-04-14
ingested: 2026-07-13
tags: [data-engineering, big-data, algorithms, mapreduce, spark, machine-learning]
concepts: [market-basket-analysis, apache-spark]
---

## Summary

"Data Algorithms" by Mahmoud Parsian (778 pages) is a comprehensive guide to designing and implementing data-intensive algorithms at scale using MapReduce and Spark. The book covers pattern mining, graph algorithms, statistical analysis, and time-series processing — all with a strong emphasis on distributed implementations.

## Key Topics

- **Market Basket Analysis (MBA)** — Finding association rules between items in transaction datasets using MapReduce. The canonical "customers who bought X also bought Y" problem. Support and Confidence metrics for evaluating rule quality.
- **Distributed Count & Sort** — Secondary sort patterns, top-N algorithms, and frequency counting at scale
- **Graph Algorithms** — PageRank, shortest paths, connected components on MapReduce
- **MapReduce Design Patterns** — Combiners, partitioners, key design, and shuffle optimization
- **Spark vs Hadoop** — When to use each framework; Spark's advantages for multi-phase MBA pipelines with in-memory processing

## Key Insight

The book emphasizes that distributed algorithms require fundamentally different thinking from their single-machine counterparts. The sorted-items-before-counting pattern in MBA is a prime example: without alphabetically sorting items in the Mapper, "coke, pizza" and "pizza, coke" would be treated as two different keys, destroying accuracy.
