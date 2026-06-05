---
title: "Vortex File Format"
type: concept
tags: [file-formats, columnar, rust, data-engineering]
created: 2026-05-26
updated: 2026-05-26
sources: [benchmarking-vortex-file-format]
---

## Summary

**Vortex** is a next-generation columnar file format and toolkit written in Rust, designed for high-performance data processing on object storage (S3, GCS, etc.). It claims significant speed improvements over [[apache-parquet|Apache Parquet]]: 100× faster random access, 10–20× faster scans, 5× faster writes, with similar compression ratios.

## Design & Architecture

- **Written in Rust** — performance-first language with memory safety
- **Zero-copy compatibility with Apache Arrow** — can interoperate with the Arrow ecosystem without data copying
- **Modeled after Apache DataFusion's extensible approach** — modular, pluggable design
- **Supports major engines**: Arrow, DataFusion, DuckDB, Spark, Pandas, [[polars|Polars]]
- **Filter pushdown** — predicates pushed to scan level, minimizing data read

## Performance Claims (from Vortex team)

| Claim | vs Parquet |
|---|---|
| Random access | 100× faster |
| Scan | 10–20× faster |
| Writes | 5× faster |
| Compression | Similar |

## Benchmarked Reality (2026-05)

Daniel Beach's independent benchmarks using Backblaze hard drive data (~24 GB, 184 CSV files) found more modest gains:

| Scenario | Best Time | Engine |
|---|---|---|
| CSV (baseline) | 25.465s | DuckDB |
| Parquet | 0.125s | DuckDB |
| Vortex (native scan) | 0.111s | Vortex pure |
| Vortex (via bridge) | 0.114s | Polars via PyArrow |

The jump from CSV to any columnar format (~200×) dwarfs Vortex's marginal advantage over Parquet (~11%). The claimed 10–20× scan advantage was **not observed** at this data scale (~24 GB).

## Python Ecosystem Maturity (2026-05)

The Python integration story is immature:

| Integration | Status |
|---|---|
| **DuckDB vortex extension** | OOM crashes on multi-file reads; requires PyArrow bridge workaround |
| **Polars** | Per-file loading only (no globbing); converts to PyArrow immediately |
| **DataFusion** | Works via PyArrow bridge |
| **Pure Vortex** | Fastest, but limited ecosystem support |

Most practical usage requires converting to PyArrow first — losing any potential zero-copy benefits.

## Positioning

Vortex appears to be competing directly with [[apache-parquet|Apache Parquet]] as the dominant columnar format for data lakes and object-storage-based analytics. It also positions itself as an alternative to [[apache-arrow|Apache Arrow]], with claims of faster processing. However, as of mid-2026, it remains **early-stage** with immature Python integrations and unproven claims at production scale.

## When to Watch

Promising but not yet production-ready for Python-heavy data engineering workflows. Worth revisiting as integrations mature, especially for:
- Rust-native data pipelines
- High-performance object-storage analytics
- Workloads bottlenecked on Parquet scan/random-access performance at petabyte scale
---
- Competes with [[apache-parquet]] — Vortex positions itself as a Parquet alternative for object storage
- Related to [[polars]] — Vortex provides a Polars bridge via `to_polars()` LazyFrame
- Related to [[duckdb]] — DuckDB has a vortex extension (currently buggy) and a PyArrow bridge workaround
- Related to [[apache-datafusion]] — Vortex modeled after DataFusion's extensible approach
- Competes with [[lance-file-format]] — both are next-gen columnar formats targeting Parquet's dominance
- Benchmark source: [[sources/benchmarking-vortex-file-format]] — Daniel Beach's independent performance evaluation
