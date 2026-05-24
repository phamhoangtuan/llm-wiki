---
title: "Vectorized Execution"
type: concept
tags: [olap, query-optimization, database-engines]
created: 2026-05-24
updated: 2026-05-24
sources: [duckdb-up-and-running]
---

## Summary

**Vectorized execution** is a query execution model where the database engine processes data in **vectors** — chunks of rows (typically 1K–64K rows at a time) — instead of processing one row at a time (the "Volcano" iterator model). This is a key architectural pillar of modern OLAP databases like [[duckdb|DuckDB]], ClickHouse, and Velox (Meta).

## How It Works

- **Traditional (row-at-a-time)**: The engine calls `next()` on each operator for every single row. One function call per row, per operator → high CPU instruction overhead.
- **Vectorized (chunk-at-a-time)**: The engine processes a block of rows at once. One function call per *vector* of rows → dramatically fewer function calls per operation.

## Why It's Faster

| Factor | Mechanism | Impact |
| --- | --- | --- |
| **Reduced instruction overhead** | One function call per vector instead of per row | 10–100x fewer virtual function dispatches |
| **Cache efficiency** | Data is processed in contiguous blocks that fit CPU cache lines | Fewer cache misses per row processed |
| **SIMD utilization** | Modern CPUs can apply one instruction to multiple data elements simultaneously (AVX, AVX-512) | Up to 8–16 operations per instruction vs. 1 |
| **Branch predictability** | Loop-based processing over arrays has predictable branches | CPU branch predictor accuracy → fewer pipeline stalls |

## Relationship to Other Execution Models

| Model | Granularity | Strengths | Used By |
| --- | --- | --- | --- |
| **Volcano (Iterator)** | Row-at-a-time | Simple, composable, low memory | MySQL, PostgreSQL, SQLite |
| **Vectorized** | Column-chunks (vectors) | High throughput on analytical queries | DuckDB, ClickHouse, Velox, DataFusion |
| **JIT-compiled** | Query-at-a-time | Lowest overhead for complex expressions | HyPer, SingleStore |

## Vectorized Execution in DuckDB

In DuckDB, the vectorized engine works hand-in-hand with **columnar storage**: data is already laid out column-by-column on disk, so reading a column produces a contiguous array ready for vectorized operations. Together with **parallel execution** (splitting work across CPU cores) and **late materialization** (postponing full row assembly), this creates a highly efficient analytical pipeline.

## Limitations

- Vectorized engines are optimized for **analytical (OLAP)** queries with large scans and aggregations — not row-level lookups (OLTP).
- Vector size must be tuned: too small → not enough amortization; too large → doesn't fit in CPU cache.
- Some operations (e.g., correlated subqueries with row-dependent logic) don't vectorize cleanly.
---
- Used by [[duckdb]] — one of four architectural pillars of DuckDB's performance
- Supports [[in-process-olap]] — vectorized execution makes laptop-scale analytics practical
- Related to [[duckdb-up-and-running]] — Wei-Meng Lee's guide on DuckDB architecture
