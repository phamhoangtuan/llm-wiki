---
title: "High Performance Spark"
type: source
source_type: book
author: "Holden Karau & Rachel Warren"
source_date: 2017-01-01
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-08
url: ""
tags: [apache-spark, data-engineering, performance, optimization, big-data]
concepts: [apache-spark]
---

## Summary

A 356-page deep dive into Apache Spark performance optimization. Covers Spark internals (lazy evaluation, DAG scheduler, RDD immutability), the Catalyst optimizer and Tungsten engine, narrow vs wide dependencies (shuffle costs), join strategies (broadcast hash join), groupByKey vs reduceByKey, data skew mitigation, caching and checkpointing, Scala vs Python trade-offs, Spark ML vs MLlib, Structured Streaming, and automated testing with spark-testing-base.

## Core Message

> Writing Spark code that runs is easy. Writing Spark code that runs 100× faster requires understanding internals — how data is distributed and processed across the cluster.

## Key Takeaways

1. **Spark SQL is king**: Use DataFrames/Datasets to leverage Catalyst optimizer and Tungsten engine
2. **Avoid shuffle**: Wide dependencies (groupByKey, sort) are the biggest bottleneck — minimize them
3. **Broadcast joins**: For small tables, broadcast to all workers to avoid shuffle entirely
4. **reduceByKey > groupByKey**: Map-side reduction before shuffle dramatically reduces network I/O
5. **Handle data skew**: Add "junk" to keys to spread data evenly, avoid straggler tasks
6. **Cache strategically**: Persist reused datasets, but don't cache everything — memory is finite
7. **Test your optimizations**: Use spark-testing-base to ensure performance improvements don't break logic

## Companion Concept

→ [[apache-spark]]
