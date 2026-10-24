---
title: "Batch Processing"
type: concept
tags: [data-engineering, batch, etl, hadoop, spark, traditional]
created: 2026-07-11
updated: 2026-07-11
sources: [building-real-time-analytics-systems]
aliases: [batch]
---

## Summary

**Batch Processing** is the traditional paradigm of collecting data over a period of time and processing it all at once in a scheduled job. Unlike [[stream-processing|stream processing]] which handles events incrementally, batch processing operates on **bounded datasets** with defined start and end points.

## Characteristics

| Aspect | Batch | Stream |
|--------|-------|--------|
| Data boundary | Bounded (finite) | Unbounded (infinite) |
| Trigger | Schedule (cron, clock) | Event-driven |
| Latency | Minutes to hours | Milliseconds to seconds |
| Throughput | Very high (full dataset at once) | Sustained (record-by-record) |
| Fault recovery | Restart entire job | Checkpoint and resume |

## When Batch Is Still the Right Choice

- **Historical reporting** — monthly/quarterly financial reports
- **Data reconciliation** — end-of-day settlement, accounting
- **Large-scale transformations** — full-table repartitioning, historical backfills
- **Cost optimization** — batch is cheaper than streaming for non-time-sensitive work
- **Complex analytics** — large joins, graph algorithms that streaming engines can't handle efficiently

## Batch in the Modern Stack

Even in streaming-first architectures, batch hasn't disappeared — it has been unified:

- **Micro-batching** — [[apache-spark|Spark Streaming]] processes data in small batches (e.g., 1-second windows)
- **Unified engines** — [[apache-flink|Flink]] treats batch as a bounded stream: same API, different data source
- **Lakehouse batch** — [[delta-lake|Delta Lake]] and [[apache-iceberg|Iceberg]] tables are queried by both batch and streaming jobs

## Batch Tools

| Tool | Era | Role |
|------|-----|------|
| **Hadoop MapReduce** | 2000s | Original distributed batch processing |
| **Apache Spark** | 2010s | In-memory batch + micro-batch streaming |
| **dbt** | 2020s | SQL-based batch transformation in data warehouses |
| **Airflow** | 2020s | Batch workflow orchestration and scheduling |

## Key Takeaways

1. Batch processing is not dead — it remains the right choice for historical reporting, reconciliation, and cost-sensitive workloads.
2. Modern architectures unify batch and stream: the same data and often the same engine handles both.
3. The [[lambda-architecture|Lambda Architecture]] was built because batch and stream required separate systems; modern engines have made this obsolete.

---

- Contrasts with [[stream-processing]] — the fundamental paradigm difference in data processing
- Contrasts with [[real-time-analytics]] — RTA replaces batch for time-sensitive decision-making
- Related to [[apache-spark]] — Spark is the dominant modern batch processing engine
- Related to [[dbt]] — dbt is the standard batch transformation tool in cloud warehouses
- Related to [[apache-airflow]] — Airflow orchestrates batch pipeline schedules
- Benchmark source: [[sources/building-real-time-analytics-systems]] — Needham contrasts batch with real-time analytics
