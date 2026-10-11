---
title: "DuckDB: Up and Running"
type: source
tags: [duckdb, olap, analytics, python, data-engineering]
created: 2026-05-24
updated: 2026-06-15
author: "Wei-Meng Lee"
source_type: book
source_date: 2024-05-24
ingested: 2026-05-24
url: ""
concepts: [vectorized-execution, duckdb, in-process-olap]
---

## Summary

A practical guide to **DuckDB** — the open-source, in-process OLAP database often described as "SQLite for analytics." The book covers DuckDB's architecture (columnar storage, vectorized execution, parallel execution, late materialization), performance vs. pandas, seamless data format integration (CSV, Parquet, pandas DataFrames), extensions (httpfs, spatial), and the MotherDuck cloud platform.

## Key Takeaways

- **In-process, zero setup**: DuckDB runs inside your application as a library — no server, no config, no network latency. `pip install duckdb` and go.
- **Four architectural pillars**: [[vectorized-execution|Vectorized execution]], columnar storage, parallel execution, and late materialization deliver fast analytics on standard hardware.
- **Query data in place**: No need to load CSV/Parquet/pandas into a database first — query files and DataFrames directly with zero-copy overhead.
- **Memory efficient**: Processes data in streaming chunks; handles datasets larger than RAM. 5.8M-row flight dataset: 280MB memory vs. pandas' 4.2GB.
- **Extension ecosystem**: httpfs (remote files via HTTP/S, S3, Hugging Face), spatial (geospatial), json, icu (locale-aware strings).
- **Cloud via MotherDuck**: Hybrid queries — join local data with cloud tables in a single SQL statement.

## Architectural Pillars

| Pillar | Mechanism | Benefit |
| --- | --- | --- |
| **Columnar storage** | Data stored by column, not row | Read only needed columns → less I/O |
| **Vectorized execution** | Process data in chunks (vectors), not row-by-row | Reduced CPU overhead, SIMD, better cache use |
| **Parallel execution** | Auto-split queries across CPU cores | No configuration; automatic throughput scaling |
| **Late materialization** | Postpone full row fetch; work with indices first | Minimized data movement → lower memory, faster filtering |

## Performance vs. pandas (5.8M-row flight dataset)

| Metric | pandas | DuckDB |
| --- | --- | --- |
| Execution Time | ~7.5s | ~0.5s |
| Peak Memory | ~4.2 GB | ~280 MB |
| Loading | Must load entire file into RAM | Streams data; processes in chunks |

## Supported Formats & Sources

| Type | Examples |
| --- | --- |
| Flat Files | CSV, JSON, Excel |
| Columnar | Parquet (recommended for performance) |
| In-Memory | pandas/Polars DataFrames (zero-copy) |
| Databases | MySQL, PostgreSQL (via extensions) |
| Remote | HTTP/S URLs, S3, GitHub, Hugging Face (via httpfs) |

## When to Use / When Not to Use

| ✅ Ideal For | ❌ Less Suitable For |
| --- | --- |
| Exploratory analysis on large CSV/Parquet files | High-volume transactional workloads (use PostgreSQL/MySQL) |
| Prototyping analytics pipelines | Multi-user concurrent writes (DuckDB is single-writer) |
| Embedding analytical SQL in Python/R apps | Real-time streaming ingestion (use Kafka + Flink/Spark) |
| Local dev and testing of data workflows |  |
| "Larger-than-memory" datasets on standard hardware |  |

## Quotes

> "DuckDB removes the 'infrastructure tax' — you focus on analysis, not database administration."

> "DuckDB proves that you don't need a massive cluster to do serious analytics. With the right architecture, a single laptop can become a powerful analytical engine."

> "DuckDB isn't meant to replace your cloud data warehouse — it's meant to accelerate the work that happens before and after."

---
- Core to [[duckdb]] — the in-process OLAP database — "SQLite for analytics"
- Foundation for [[vectorized-execution]] — processing data in chunks, not row-by-row
- Foundation for [[in-process-olap]] — analytical database running as an embedded library
