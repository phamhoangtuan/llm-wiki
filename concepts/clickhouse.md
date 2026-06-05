---
title: "ClickHouse"
type: concept
tags: [olap, databases, columnar, clickhouse, data-engineering, delta-lake]
created: 2026-06-02
updated: 2026-06-02
sources: [integrating-rust-delta-kernel-clickhouse]
aliases: []
---

## Summary

**ClickHouse** is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP). It processes billions to trillions of rows in milliseconds, making it one of the fastest analytical databases available. In 2026, ClickHouse became "data lake ready" — supporting [[delta-lake|Delta Lake]] and [[apache-iceberg|Apache Iceberg]] as first-class table formats through its `deltaLake()` and `iceberg()` table functions.

## Architecture Highlights

- **Column-oriented** — data stored column-by-column, enabling [[vectorized-execution]] and high compression
- **No external dependencies** — single binary with vendored dependencies; only links libc
- **C++ core with Rust extensions** — introduced Rust for select functionality (BLAKE3, PRQL, skim, delta-kernel-rs)
- **Sanitizer-hardened** — every commit tested with ASAN, MSAN, TSAN, UBSAN

## Delta Lake Integration

ClickHouse's Delta Lake support evolved through two phases:

| Phase | Approach | Trade-offs |
|---|---|---|
| **Native implementation** | Direct Delta protocol implementation | Full control, high maintenance burden, slow feature coverage |
| **Delta Kernel** | Rust-based `delta-kernel-rs` via FFI | Shared protocol handling, faster features, Rust build complexity |

The [[delta-kernel|Delta Kernel]] integration gives ClickHouse:
- **Writes** — transactional writes to Delta tables (Parquet written by ClickHouse, metadata by Kernel)
- **Schema evolution** — reconciles file-level schemas with current table definition
- **Time travel** — query historical snapshots via versioned access
- **Partition pruning** — skip irrelevant files using Delta metadata
- **Statistics-based pruning** — file-level min/max stats for data skipping
- **Change Data Feed (CDF)** — row-level change visibility between versions

```sql
-- Query Delta Lake directly
SELECT cityHash64(URL), count() AS cnt
FROM deltaLake('https://datasets-documentation.s3.amazonaws.com/lake_formats/delta_lake/')
GROUP BY cityHash64(URL) ORDER BY cnt DESC LIMIT 5

-- Change Data Feed (ClickHouse 25.12+)
SELECT *
FROM deltaLake('s3://path/to/table')
SETTINGS delta_lake_snapshot_start_version = 5, delta_lake_snapshot_end_version = 10
```

## Rust Integration Challenges

Integrating `delta-kernel-rs` into ClickHouse's C++ build system required:
- **Nightly Rust** — required for sanitizer support (unstable compiler features)
- **Full crate vendoring** — all dependencies vendored into a submodule to avoid network fetches during build
- **Corrosion** — Rust-C++ CMake bridge for build integration
- **Static OpenSSL** — linking against ClickHouse's own statically built OpenSSL (since `ring`/rustls alternatives failed)
- **Cross-compilation fixes** — restricting to `staticlib` crate type only

Key quote from the ClickHouse team: *"We've spent easily 20 to 50 times more effort debugging and setting up Rust builds than reading Rust code."*

## ClickPipes

ClickPipes is ClickHouse's managed CDC ingestion tool. The CDF support in the Delta Kernel integration provides the foundation for CDC-oriented workflows — allowing ClickPipes to consume row-level changes from Delta tables for incremental pipeline processing.

## Related Databases

| Database | Type | Comparison |
|---|---|---|
| **ClickHouse** | Distributed OLAP | Fastest for large-scale aggregations; columnar, vectorized |
| [[duckdb|DuckDB]] | [[in-process-olap|In-process OLAP]] | Embedded; simpler deployment; ClickHouse is faster at extreme scale |
| **Snowflake** | Cloud data warehouse | Managed; ClickHouse is self-hosted or ClickHouse Cloud |
| **BigQuery** | Serverless data warehouse | Fully managed; ClickHouse gives more control over performance |
---
- Integrates with [[delta-kernel]] — Rust abstraction layer that provides Delta Lake protocol support via FFI
- Supports [[delta-lake]] — `deltaLake()` table function for reading/writing Delta tables natively
- Related to [[duckdb]] — both are columnar analytical databases; DuckDB is embedded, ClickHouse is distributed
- Powered by [[vectorized-execution]] — columnar architecture enables SIMD-based query processing
- Uses [[apache-parquet]] — underlying file format for Delta table storage
- Benchmark source: [[sources/integrating-rust-delta-kernel-clickhouse]] — detailed FFI integration and feature coverage
