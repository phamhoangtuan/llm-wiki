---
title: "Quick Insights on Materialized Views"
type: source
tags: [materialized-views, streaming, databases, data-engineering]
created: 2026-05-24
author: "Vu Trinh"
source_type: article
source_date: 2026-05-21
ingested: 2026-05-24
url: "https://vutr.substack.com/p/quick-insights-on-materialized-views"
concepts: [timely-dataflow, differential-dataflow, dbsp, materialized-views, incremental-view-maintenance]
---

## Summary

A practical exploration of **materialized views** (MVs) — the hybrid of tables and views that stores pre-computed query results. The article covers what MVs are, how Incremental View Maintenance (IVM) works through three theoretical frameworks (Timely Dataflow, Differential Dataflow, DBSP), the freshness vs. cost trade-off, and MVs' emerging role in real-time/stream processing as an alternative to dedicated stream processors.

## Key Takeaways

- **MV = table × view hybrid**: A pre-computed query result stored physically. It is "aware" of the query (like a view) but stores data (like a table). Refreshed when source data changes.
- **MV as cache**: Semantically, an MV is a cache — it holds computed results so queries avoid accessing the "original location" (source tables). The core challenge is keeping the cache fresh.
- **Three IVM approaches**: [[timely-dataflow|Timely Dataflow]] (timestamp-based notification), [[differential-dataflow|Differential Dataflow]] (versioned state on TD), and [[dbsp|DBSP]] (signal-processing formalism with 4 operators).
- **Freshness vs. cost trade-off**: Higher freshness = more frequent refreshes = higher compute cost. Full refresh is simple but expensive; incremental refresh is efficient but doesn't support all SQL operations.
- **MVs in stream processing**: Flink Dynamic Tables, RisingWave, and ClickHouse incremental MVs all use MV semantics for real-time analytics —MV is a first-class concept in streaming.
- **Practical rule**: Check if your database supports incremental refresh (ClickHouse, Databricks, BigQuery, Snowflake). If your use case can leverage it, prioritize incremental refresh. When MV can't serve your use case (e.g., missing JOIN change capture), then move to Flink.

## Freshness vs. Cost Spectrum

| Strategy | How It Works | Pros | Cons |
| --- | --- | --- | --- |
| **Full refresh** | Recompute everything on schedule | Simple, predictable | Stale between runs, expensive for large data |
| **Incremental refresh** | Process only what changed | Efficient, enables frequent refreshes | Not all SQL ops supported; complexity |

## Real-World Implementations

- **Flink Dynamic Tables**: A dynamic table changes over time as its stream evolves. A continuous SQL query on a dynamic table is semantically equivalent to an MV with eager view updating.
- **RisingWave**: A streaming OLAP database built around MV principles. MVs are maintained incrementally via dataflow graphs.
- **ClickHouse**: Treats incremental MV as a stream processor — a trigger that runs a query on new data as it arrives, merging results incrementally.

## Quotes

> "A materialized view can be considered a cache, as it helps queries run faster by accessing computed data and avoiding access to the data's original location."

> "The higher the freshness, the more frequently the MV is refreshed. Which means you pay a higher cost for more frequent refreshes."

---
- Core to [[materialized-views]] — the hybrid of tables and views — pre-computed, stored, refreshable
- Foundation for [[incremental-view-maintenance]] — how databases keep MVs fresh without full recompute
- Foundation for [[timely-dataflow]] — timestamp-based notification model for distributed computation
- Foundation for [[differential-dataflow]] — versioned incremental computation built on Timely Dataflow
- Foundation for [[dbsp]] — signal-processing formalism for incremental view computation
