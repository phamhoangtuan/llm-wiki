---
title: "Apache DataFusion"
type: concept
tags: [query-engines, rust, apache, sql, data-engineering]
created: 2026-05-26
updated: 2026-05-26
sources: [benchmarking-vortex-file-format]
---

## Summary

**Apache DataFusion** is an extensible, Rust-native query engine that provides SQL and DataFrame APIs for building high-performance data systems. It is designed to be embedded into other applications (similar to [[duckdb|DuckDB]]) rather than being a standalone database. Its architecture — particularly its extensibility — served as the design model for the [[vortex-file-format|Vortex file format]].

## Key Characteristics

- **Written in Rust** — zero-cost abstractions, memory safety, near-C performance
- **SQL + DataFrame APIs** — supports both paradigms
- **Apache Arrow native** — in-memory columnar format, zero-copy interop
- **Extensible design** — composable components (planner, optimizer, execution engine) that can be mixed and matched
- **Used as a foundation** — powers InfluxDB IOx, HoraeDB, GreptimeDB, and other databases
- **[[vectorized-execution|Vectorized execution]]** — columnar batch-at-a-time processing

## Benchmarks (Backblaze Dataset, 2026-05)

DataFusion stood out in Daniel Beach's benchmarks as the **fastest engine on raw CSV** by a wide margin:

| Format | Engine | Runtime |
|---|---|---|
| CSV | DuckDB | 25.465s |
| CSV | Polars | OOM (crashed) |
| **CSV** | **DataFusion** | **5.106s** |
| Parquet | DuckDB | 0.125s |
| Parquet | DataFusion | 0.370s |

DataFusion was nearly **5× faster than DuckDB** on raw CSV, demonstrating exceptional CSV parsing performance. On Parquet, DataFusion (0.370s) was slower than DuckDB (0.125s) — likely because DuckDB's C++ Parquet reader is more mature than DataFusion's Rust one.

## Python Integration

DataFusion provides Python bindings via `datafusion` package:

```python
import datafusion

ctx = datafusion.SessionContext()
ctx.register_parquet("drive_data", "data/*.parquet")
result = ctx.sql("""
    SELECT date, COUNT(*) as failure_count
    FROM drive_data
    WHERE failure = 1
    GROUP BY date
    ORDER BY failure_count DESC
""")
print(result)
```

## Position in the Ecosystem

DataFusion sits between DuckDB (batteries-included database) and Apache Spark (distributed cluster framework). It's a **library** for building data systems rather than a ready-to-use tool — developers compose DataFusion's optimizer, planner, and execution engine into custom database or query products.
---
- Competes with [[duckdb]] — both are embeddable query engines with SQL support; DuckDB is C++, DataFusion is Rust
- Related to [[vortex-file-format]] — Vortex's architecture was modeled after DataFusion's extensible approach
- Utilizes [[vectorized-execution]] — columnar batch processing for analytical queries
- Related to [[apache-parquet]] — DataFusion reads Parquet natively (0.370s in benchmarks)
- Benchmark source: [[benchmarking-vortex-file-format]] — 5.106s CSV scan, best-in-class for raw CSV
