---
title: "Liquid Clustering"
type: concept
tags: [data-layout, liquid-clustering, delta-lake, iceberg, partitioning, databricks, data-engineering]
created: 2026-06-02
updated: 2026-06-02
sources: [debunking-data-layout-myths-liquid-clustering]
aliases: [Liquid]
---

## Summary

**Liquid Clustering** is Databricks' modern data layout technique for open table formats ([[delta-lake|Delta Lake]] and [[apache-iceberg|Apache Iceberg]]). Unlike Hive-style partitioning — which forces users to commit to a fixed physical directory structure at table creation — Liquid treats clustering keys as flexible input hints. The engine uses these hints to organize data into optimally sized files, and keys can be changed at any time without rewriting the table. It became Generally Available in 2024.

## How It Differs from Partitioning

| Aspect | Hive-Style Partitioning | Liquid Clustering |
|---|---|---|
| **File structure** | Fixed directory hierarchy (`date=2026/hour=12/`) | Flat directory of clustered files |
| **Key changes** | Requires full table rewrite | Change keys anytime without rewrite |
| **Cardinality constraints** | High-cardinality → billions of tiny files | No cardinality constraints |
| **Multi-dimensional** | Single partition hierarchy | Clusters on multiple columns simultaneously |
| **Write amplification** | New data may require rewriting many partitions | Incremental clustering at write time |
| **Concurrency** | File-level (partition-based boundaries) | Row-level concurrency |

## Key Features

### Incremental Clustering
Liquid clusters data incrementally, including at write time, so the layout stays optimal without periodic full rewrites. This contrasts with Z-Ordering, which requires rerunning `OPTIMIZE ZORDER BY` periodically — each run rewriting large amounts of already-clustered data.

### Low-Cardinality Optimization
Liquid automatically detects low-cardinality clustering columns and applies special optimizations. For example, clustering by `(date, user_id)`:
- Each file contains rows from a single date (low-cardinality optimization)
- `user_id` used for finer-grained sorting within each date's files
- Benchmarks: 35% faster clustering, 22% faster queries

### Row-Level Concurrency
Unlike partitioning (file-level concurrency), Liquid provides row-level concurrency. Two writers updating different rows don't conflict even if those rows live in the same file. This eliminates the historical need to partition tables for concurrent ETL write boundaries.

### Metadata-Only Operations
Liquid supports computing results from file-level metadata without scanning data:
- **DELETEs** aligned with clustering keys: ~90% faster than full rewrites
- **Aggregate queries** (COUNT, DISTINCT, GROUP BY): up to 27× speedup

### Reader-Agnostic
Liquid is a **write-side optimization**. Output is standard [[apache-parquet|Parquet]] files with min/max statistics. Any compatible reader (open-source Apache Spark, [[duckdb|DuckDB]], Trino, etc.) benefits from data skipping — no Databricks lock-in.

## Comparison with Z-Ordering

Z-Ordering (`OPTIMIZE ZORDER BY`) is an older clustering technique that Liquid supersedes:

| Aspect | Z-Ordering | Liquid Clustering |
|---|---|---|
| **Clustering quality** | Poor — values spread across many files | High — tight per-file value ranges |
| **Maintenance** | Periodic full rewrites required | Incremental, at write time |
| **Rewrite cost** | Grows with table size | Proportional to new data only |
| **Column support** | Multi-column | Multi-column with low-cardinality optimization |

## Production Scale

Dozens of Databricks customers run PB-scale Liquid Clustered tables in production. OPTIMIZE on a 10 PB table previously took 12 hours for planning; now takes 23 minutes. Execution phase got 5× faster.

### Customer Results

| Team | Scale | Improvements |
|---|---|---|
| **Arctic Wolf** | 3.8 PB security telemetry | 7.7× query speedup (51s → 6.6s), files 4M → 2M |
| **Bolt** | TB-scale CDC table | 138% write throughput, 63% max read reduction |
| **Databricks internal** | 1.1 PB | 5.9× query speedup, 86% fewer bytes, 27% smaller table |

## Co-Clustered Joins (Private Preview)

Joining two Liquid tables on their clustering columns previously required a full shuffle. Co-clustered joins remove that shuffle: **51% faster** (28m → 14m) with **87% less data shuffled** (1.2 TiB → 150 GiB).

## Conversion from Partitioning

Databricks is introducing a new `ALTER TABLE ... REPLACE PARTITIONED BY WITH CLUSTER BY` command (Private Preview) for in-place conversion with minimal downtime, avoiding full table rewrites.

## When to Use

| ✅ Use Liquid Clustering | ❌ Stick with Partitioning |
|---|---|
| High-cardinality columns needed for filtering | Legacy systems that ONLY support directory-based pruning |
| Multi-dimensional query patterns | Extremely static query patterns with few columns |
| Frequent schema/key evolution | N/A — Liquid handles this better too |
| Concurrent ETL workloads | N/A — row-level concurrency is superior |
---
- Built for [[delta-lake]] — Liquid is the recommended data layout for Delta Lake tables on Databricks
- Supports [[apache-iceberg]] — Liquid Clustering also works on Iceberg tables in Unity Catalog
- Produces [[apache-parquet]] — output files are standard Parquet with min/max statistics
- Compatible with [[duckdb]] — any Parquet reader benefits from Liquid's file-level statistics
- Related to [[change-data-capture]] — row-level concurrency enables high-throughput CDC pipelines
- Benchmark source: [[debunking-data-layout-myths-liquid-clustering]] — 8 myths debunked, success stories at scale
