---
title: "Apache Spark"
type: concept
tags: [apache-spark, data-engineering, big-data, performance, optimization]
created: 2026-06-08
updated: 2026-06-15
sources: [high-performance-spark]
aliases: [spark, spark-optimization]
---

## Summary

Apache Spark is a distributed data processing engine designed for large-scale analytics. While Spark's high-level APIs (DataFrames, Spark SQL) make it accessible, writing high-performance Spark requires understanding its internals — lazy evaluation, the DAG scheduler, shuffle mechanics, and memory management. A well-optimized Spark job can run 100× faster than a naive implementation.

## Core Internals

| Concept | What It Means | Why It Matters |
|---|---|---|
| **Lazy Evaluation** | Transformations (map, filter) don't execute until an action (collect, save) triggers them | Allows the DAG Scheduler to optimize the execution plan, combining operations and minimizing data scans |
| **RDD** | Resilient Distributed Dataset — immutable, partitioned collection with lineage tracking | Immutability + lineage = built-in fault tolerance: lost partitions can be recomputed |
| **Catalyst Optimizer** | Spark SQL's query optimizer — rewrites logical plans into optimized physical plans | Automatic optimization: predicate pushdown, constant folding, join reordering |
| **Tungsten** | Memory management at byte level + code generation | Eliminates JVM overhead — significantly faster than RDD-based processing |

## Shuffles: The #1 Bottleneck

Shuffles occur when data must be redistributed across partitions — the most expensive operation in Spark:

| Dependency Type | Examples | Shuffle? | Cost |
|---|---|---|---|
| **Narrow** | `map`, `filter`, `flatMap`, `mapPartitions` | No | Low |
| **Wide** | `groupByKey`, `sort`, `join` (non-broadcast), `repartition` | Yes | High (network + disk I/O) |

> **Rule**: Minimize wide dependencies. Every shuffle doubles the I/O cost.

## Join Optimization

| Strategy | When to Use | Benefit |
|---|---|---|
| **Broadcast Hash Join** | One table is small (< 10MB default) | No shuffle — small table sent to all workers |
| **Shuffled Hash Join** | Both tables large | Full shuffle — most expensive |
| **Sort Merge Join** | Both tables large, pre-sorted on join key | Efficient for sorted data |

```python
from pyspark.sql.functions import broadcast
df_large.join(broadcast(df_small), "key")  # Forces broadcast join
```

## groupByKey vs reduceByKey

| Operation | Behavior | Risk |
|---|---|---|
| **groupByKey** | Collects ALL values for a key on one executor | High OOM risk — no pre-aggregation |
| **reduceByKey** | Reduces values locally (map-side) before shuffle | Dramatically less data transferred |

> **Always prefer reduceByKey / aggregateByKey over groupByKey.**

## Data Skew

When some keys have disproportionately more data, causing straggler tasks:

- **Symptom**: One task takes 10× longer than others
- **Fix**: Add random "salt" (junk) to skewed keys to spread data across partitions, then aggregate back

## Caching & Checkpointing

| Strategy | What It Does | When to Use |
|---|---|---|
| **persist() / cache()** | Keeps dataset in memory for reuse | Repeated access to same dataset (multiple actions) |
| **checkpoint()** | Writes to stable storage, truncates lineage | Long lineage chains (stack overflow risk), failure recovery |

> Cache only what you reuse. Unnecessary caching wastes memory and can degrade performance.

## Scala vs Python (PySpark)

| Aspect | Scala | Python (PySpark) |
|---|---|---|
| **Performance** | Native JVM — fastest | JVM↔Python bridge overhead |
| **Spark SQL parity** | Identical | Identical (data stays in JVM for SQL operations) |
| **UDF overhead** | Minimal | Higher — data must cross JVM↔Python boundary |
| **Ecosystem** | Full Spark API | Full Spark API via PySpark |

> For most workloads, the gap is negligible due to Spark SQL's dominance. Use whatever language your team knows best.

---

- Related to [[data-engineer]] — Spark is the workhorse of distributed batch processing in modern DE stacks
- Related to [[apache-flink]] — Flink handles streaming where Spark handles batch; both are distributed processing engines
- Related to [[apache-iceberg]] — Spark is a primary engine for reading/writing Iceberg tables
- Related to [[change-data-capture]] — Spark Streaming can consume CDC feeds
- Benchmark source: [[sources/high-performance-spark]] — Karau & Warren's 356-page optimization guide
