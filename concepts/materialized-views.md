---
title: "Materialized Views"
type: concept
tags: [databases, data-engineering, streaming, caching]
created: 2026-05-24
updated: 2026-05-24
sources: [materialized-views-quick-insights]
---

## Summary

A **materialized view (MV)** is a pre-computed query result stored as a physical table. It combines the "awareness" of a view (it knows the query that defines it) with the storage of a table (the result is persisted on disk). MVs trade write-time compute for read-time speed — essentially acting as a cache layer on top of your base tables.

## Table vs. View vs. Materialized View

| Entity | Stores Data? | Knows Query? | Refreshed? |
| --- | --- | --- | --- |
| **Table** | Yes — on disk | No | Manual INSERT/UPDATE/DELETE |
| **View** | No — recomputed every query | Yes | N/A — always fresh |
| **Materialized View** | Yes — on disk | Yes | Yes — on schedule or on change |

## The Cache Analogy

An MV is semantically a **cache**: it holds a computed subset of data so queries avoid recomputing from source tables. Like any cache, the fundamental challenge is **freshness** — keeping the MV in sync with its source data without paying prohibitive compute costs.

## Freshness vs. Cost Trade-Off

Every MV decision comes down to two questions:

- **How fresh does your data need to be?** — A fraud detection system needs near-real-time freshness; an hourly report dashboard tolerates minutes of staleness.
- **What are you willing to pay for it?** — Moving computation from read-time to write/refresh-time is not free. Higher freshness = higher compute cost.

### Refresh Strategies

| Strategy | How | Pros | Cons |
| --- | --- | --- | --- |
| **Full refresh** | Recompute everything on schedule | Simple, predictable | Stale between runs; expensive for large datasets |
| **Incremental refresh** | Process only changed data ([[incremental-view-maintenance|IVM]]) | Efficient; enables frequent refreshes | Not all SQL ops supported; complexity |

## MVs in Stream Processing

MVs are not just a batch/database concept — they are a first-class primitive in stream processing:

- **Flink Dynamic Tables**: A continuous SQL query on a dynamic table is semantically equivalent to an MV with eager view updating.
- **RisingWave**: A streaming OLAP database built entirely around MV principles — views are maintained incrementally via dataflow graphs.
- **ClickHouse**: Treats incremental MVs as stream processors for real-time analytics — a trigger inserts new data, merges incrementally.

## Practical Guidance

- Always check if your database supports [[incremental-view-maintenance|incremental refresh]] (ClickHouse, Databricks, BigQuery, Snowflake).
- Prioritize incremental refresh when possible — it makes frequent refreshes affordable.
- Be aware of SQL operation limitations on incremental MVs (e.g., BigQuery restricts which JOINs can be incrementally maintained).
- When MV can't serve your use case (e.g., missing JOIN change capture), consider dedicated stream processors like Apache Flink.
---
- Maintained by [[incremental-view-maintenance]] — the mechanism that keeps MVs fresh without full recompute
- Foundation for [[timely-dataflow]] — timestamp-based notification model underlying IVM
- Foundation for [[differential-dataflow]] — versioned incremental computation built on Timely Dataflow
- Foundation for [[dbsp]] — signal-processing formalism for incremental computation
- Related to [[materialized-views-quick-insights]] — Vu Trinh's article on MVs, IVM, and streaming
