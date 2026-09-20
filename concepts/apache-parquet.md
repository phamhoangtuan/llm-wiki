---
title: "Apache Parquet"
type: concept
tags: [file-formats, columnar, big-data, data-engineering, delta-lake]
created: 2026-05-26
updated: 2026-06-15
sources: [benchmarking-vortex-file-format, integrating-rust-delta-kernel-clickhouse, debunking-data-layout-myths-liquid-clustering]
---

## Summary

**Apache Parquet** is the dominant open-source columnar storage format for the big data ecosystem. It stores data column-by-column (rather than row-by-row like CSV), enabling highly efficient compression and selective column reads. It is the de facto standard for data lakes, supported by virtually every analytics engine: [[duckdb|DuckDB]], [[polars|Polars]], [[apache-datafusion|Apache DataFusion]], Apache Spark, Presto/Trino, and more.

## Why Columnar?

| Aspect | Row-based (CSV, JSON) | Columnar (Parquet) |
|---|---|---|
| Storage | Row by row | Column by column |
| Compressibility | Low (mixed types per row) | High (same-type values together) |
| Read pattern | Must read all columns | Read only needed columns |
| Analytics suitability | Poor | Excellent |

In Daniel Beach's benchmarks, switching from CSV to Parquet yielded a **~200× speed improvement** (25.5s → 0.125s with DuckDB) — a larger gain than any difference between columnar formats.

## Key Features

- **Columnar storage** — values of the same column stored contiguously, enabling high compression (run-length, dictionary, delta encoding)
- **Predicate pushdown** — filter conditions pushed to storage layer; only matching row groups are read
- **File-level statistics** — each Parquet file stores per-column min/max values and row counts, enabling engines to skip entire files without reading them (data skipping). This is the foundation for partition pruning and statistics-based pruning in [[delta-lake|Delta Lake]] and [[apache-iceberg|Iceberg]].
- **Schema evolution** — add/remove columns without rewriting entire datasets
- **Nested data** — supports complex types (structs, lists, maps)
- **Splittable** — files can be split for parallel processing across distributed workers

## Performance Benchmarks (2026-05)

Independent benchmarks by Daniel Beach (Backblaze hard drive data, ~24 GB):

| Engine | Parquet Runtime | vs CSV (same engine) |
|---|---|---|
| DuckDB | 0.125s | ~200× faster |
| DataFusion | 0.370s | ~14× faster |
| Polars | 0.193s | N/A (OOM on CSV) |

## Competing Formats

Parquet faces competition from newer columnar formats aiming to improve on its design:

- **[[vortex-file-format|Vortex]]** — Rust-native, claims 10–20× faster scans; benchmarks show marginal improvement (0.111s vs 0.125s Parquet)
- **[[lance-file-format|Lance]]** — Columnar format optimized for ML/AI workloads, random access, and versioning
- **Apache ORC** — Similar to Parquet, historically preferred in the Hive ecosystem

Despite challengers, Parquet remains the **incumbent standard** with the broadest ecosystem support and proven production reliability.
---
- Used by [[duckdb]] — DuckDB reads/writes Parquet natively with excellent performance
- Used by [[polars]] — Polars supports Parquet via `read_parquet()` / `scan_parquet()`
- Used by [[apache-datafusion]] — DataFusion reads Parquet natively (0.370s benchmark)
- Used by [[clickhouse]] — ClickHouse writes Parquet for Delta Lake tables (Kernel handles metadata)
- Competes with [[vortex-file-format]] — Vortex aims to replace Parquet as the columnar standard
- Related to [[vectorized-execution]] — columnar storage enables vectorized query execution
- Foundation for [[delta-lake]] — Delta tables store data as Parquet files with min/max stats for data skipping
- Foundation for [[liquid-clustering]] — Liquid produces standard Parquet files with statistics, enabling reader-agnostic pruning
- Benchmark source: [[sources/benchmarking-vortex-file-format]] — 0.125s DuckDB-on-Parquet, the baseline to beat
- Foundation for [[apache-iceberg]] — Iceberg tables store data as Parquet files with file-level statistics for data skipping
- Competes with [[lance-file-format]] — Lance is a next-gen columnar format optimized for ML/AI workloads and random access
