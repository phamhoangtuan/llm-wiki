---
title: "Polars"
type: concept
tags: [dataframes, query-engines, rust, python, data-engineering]
created: 2026-05-26
updated: 2026-05-26
sources: [benchmarking-vortex-file-format]
---

## Summary

**Polars** is an open-source DataFrame library written in Rust with Python bindings, designed for high-performance data manipulation. It uses a lazy execution model (queries are optimized before execution) and Apache Arrow as its memory model. It competes with pandas, [[duckdb|DuckDB]], and [[apache-datafusion|Apache DataFusion]].

## Key Characteristics

- **Written in Rust** — memory-safe, near-C performance
- **Lazy Evaluation** — queries are built, optimized, then executed; avoids unnecessary intermediate results
- **Apache Arrow memory model** — zero-copy interop with other Arrow-based tools
- **Expression-based API** — composable operations (`.filter()`, `.group_by()`, `.agg()`)
- **Multi-threaded by default** — no Python GIL bottleneck (Rust core runs in native threads)

## OOM Issues and Reliability Concerns

Daniel Beach (Data Engineering Central) has publicly criticized Polars for **unpredictable out-of-memory (OOM) failures** on workloads that other tools handle without issue. In his benchmarking:

- **24 GB CSV dataset** → Polars crashed with memory errors, while DuckDB (25.5s) and DataFusion (5.1s) succeeded on the same hardware.
- Author claims to have "ripped Polars out of production" citing "simply unpredictable and unreliable in an unacceptable way, for tasks that other tools handle with ease."
- He references widespread OOM issues documented across Polars GitHub and Google search results.

> "You can only hide the pea for so long." — Daniel Beach on Polars' OOM problems

However, it's worth noting that Polars performed fine on Parquet (0.193s) and Vortex (0.114s via bridge) — the OOM was specific to raw CSV ingestion of large files.

## Polars vs DuckDB

| Aspect | Polars | DuckDB |
|---|---|---|
| Paradigm | DataFrame API (expression-based) | SQL |
| Execution | Lazy (optimized plan) | Eager (immediate) |
| Core language | Rust | C++ |
| Memory model | Apache Arrow | Custom columnar |
| CSV robustness | Reported OOM issues | Handled 24 GB CSV reliably |
| Parquet performance | 0.193s (benchmark) | 0.125s (benchmark) |
| Best for | DataFrame-centric workflows | SQL-centric analytics |

## Python Integration

Polars provides first-class Python bindings:

```python
import polars as pl

# Lazy — builds query plan, optimizes, then executes
df = (
    pl.scan_csv("data/*.csv")
    .filter(pl.col("failure") == 1)
    .group_by("date")
    .agg(pl.count())
    .collect()
)

# Eager — immediate execution
df = pl.read_parquet("data.parquet")
```

## Vortex Integration

Polars can read Vortex files via the Arrow bridge (`VortexFile.to_polars()`) — but only file-by-file, with no globbing/pattern support as of May 2026. The workflow requires converting to PyArrow first, then to Polars LazyFrame, negating zero-copy potential.
---
- Competes with [[duckdb]] — both target data engineering workloads with Python APIs; DuckDB uses SQL, Polars uses DataFrame API
- Competes with [[apache-datafusion]] — both are Rust-based Arrow-native query engines, but DataFusion accepts SQL
- Related to [[vortex-file-format]] — Polars can read Vortex files via PyArrow bridge (0.114s benchmark)
- Related to [[apache-parquet]] — Polars reads Parquet natively with strong performance (0.193s)
- Benchmark source: [[sources/benchmarking-vortex-file-format]] — independent performance evaluation showing OOM on CSV
