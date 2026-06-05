---
title: "Incremental View Maintenance"
type: concept
tags: [databases, incremental-computation, streaming]
created: 2026-05-24
updated: 2026-05-24
sources: [materialized-views-quick-insights]
---

## Summary

**Incremental View Maintenance (IVM)** is the technique of updating a [[materialized-views|materialized view]] by processing only the data that has changed, rather than recomputing the entire view from scratch. IVM is what makes frequent refreshes affordable — the cost per refresh is proportional to the size of the delta, not the size of the full dataset.

## The Problem

When source data changes, the simplest approach is to recompute the entire MV — a **full refresh**. This works but is expensive: you pay the full compute cost on every refresh, and the MV is stale between runs. For large datasets, full refresh becomes prohibitive.

IVM addresses this by asking: *"Can we refresh only the piece affected by the change?"*

## Three Theoretical Approaches

The article identifies three main modern IVM frameworks. Not all databases implement one of these; some maintain MVs in their own way. Cloud data warehouse internals (BigQuery, Snowflake, Redshift) are not publicly documented.

### 1. Timely Dataflow

Introduced in the **Naiad** paper. A **general computational model** where every message carries a logical timestamp. The key mechanism: a node can request a notification when timestamp *t* is complete — meaning no further messages for *t* can arrive. This notification guarantee tells the system when a given version of a computation is complete and safe to emit.

Designed for deeply nested iterative algorithms (e.g., graph processing). For MVs, the notification mechanism is what matters: it provides correctness guarantees about when a view version is finalized.

→ See [[timely-dataflow]]

### 2. Differential Dataflow

Built on top of Timely Dataflow. Tracks data states as **multiple versions** ordered by timestamps. Uses the TD notification guarantee to know when a version is complete, then computes the minimal diff between versions. Key insight: the system can reuse computations when updates arrive, because it knows exactly which versions have been finalized.

→ See [[differential-dataflow]]

### 3. DBSP (Database Stream Processor)

Takes a fundamentally different approach rooted in **Digital Signal Processing**. A database is a stream of snapshots; changes are a stream of deltas. DBSP formalizes this with four operators (`lift`, `delay`, and two for recursive programs) that are **functionally complete** for all SQL relational operations — any standard SQL query can be automatically converted into an incremental version.

→ See [[dbsp]]

## Practical Implications

- **Check your database**: ClickHouse, Databricks, BigQuery, and Snowflake support some form of incremental refresh, but each has SQL operation restrictions.
- **BigQuery limitation**: Incremental updates work when the MV query is a JOIN and the right side has new data — not all change patterns are supported.
- **Prioritize incremental**: When your use case supports it, incremental refresh makes frequent refreshes affordable.
---
- Related to [[materialized-views]] — IVM is the mechanism that keeps MVs fresh
- Foundation for [[timely-dataflow]] — timestamp notification model — one of three IVM approaches
- Foundation for [[differential-dataflow]] — versioned incremental computation on top of Timely Dataflow
- Foundation for [[dbsp]] — signal-processing formalism — functionally complete for SQL
- Related to [[sources/materialized-views-quick-insights]] — Vu Trinh's article covering IVM theory
