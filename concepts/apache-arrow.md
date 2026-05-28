---
title: "Apache Arrow"
type: concept
tags: [data-engineering, columnar, apache, in-memory]
created: 2026-05-28
updated: 2026-05-28
sources: [benchmarking-vortex-file-format]
---

## Summary

**Apache Arrow** is an open-source, language-agnostic columnar in-memory format designed for efficient data interchange between systems. It provides zero-copy data sharing across languages (Python, C++, Java, Rust) and serves as the memory model for many modern data tools including [[polars|Polars]], [[apache-datafusion|Apache DataFusion]], and [[vortex-file-format|Vortex]].

## Key Features

- **Columnar in-memory format** — data stored column-by-column for vectorized processing
- **Zero-copy interop** — pass data between Python, R, C++, Java without serialization
- **Language-agnostic** — native implementations in 12+ languages
- **SIMD-optimized** — leverages modern CPU instructions for analytics

## Role in the Ecosystem

Arrow serves as the universal memory representation that enables fast data interchange between compute engines:

```
Source → Arrow (in-memory) → DuckDB / Polars / DataFusion / Vortex
```

Tools that use Arrow as their memory model:
- [[polars|Polars]] — Rust DataFrame library
- [[apache-datafusion|Apache DataFusion]] — Rust query engine
- [[vortex-file-format|Vortex]] — integrates via zero-copy Arrow compatibility
- PySpark — pandas UDFs use Arrow for data transfer
- [[duckdb|DuckDB]] — can export to Arrow tables

> **Note**: This page is a stub. Arrow is referenced by multiple wiki pages (vortex-file-format, polars, duckdb) but was not the subject of any single ingested source.
---
- Used by [[polars]] — Polars uses Apache Arrow as its in-memory columnar format
- Used by [[apache-datafusion]] — DataFusion is Arrow-native for zero-copy interop
- Integrates with [[vortex-file-format]] — Vortex claims zero-copy compatibility with Arrow
- Related to [[apache-parquet]] — Arrow is the in-memory format; Parquet is the on-disk format
