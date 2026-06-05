---
title: "DuckDB"
type: concept
tags: [databases, olap, analytics, python, data-engineering]
created: 2026-05-24
updated: 2026-05-28
sources: [duckdb-up-and-running, benchmarking-vortex-file-format, delta-grows-up-writes-unity-catalog]
---

## Summary

**DuckDB** is an open-source (MIT), in-process OLAP database management system — often described as "SQLite for analytics." It runs as an embedded library inside your application (Python, R, Node.js, C++, etc.), requiring zero server setup. Its performance comes from four architectural pillars: **columnar storage**, [[vectorized-execution|vectorized execution]], **parallel execution**, and **late materialization**.

## Identity: "SQLite for Analytics"

| Aspect | SQLite | DuckDB |
| --- | --- | --- |
| Workload | OLTP (transactions) | OLAP (analytics) |
| Storage | Row-based | Columnar |
| Execution | Row-at-a-time | Vectorized (chunk-at-a-time) |
| Embedding | Yes (in-process) | Yes (in-process) |
| License | Public domain | MIT |

## Architectural Pillars

### 1. Columnar Storage

Data is stored by column, not by row. Analytical queries typically need only a few columns across many rows — DuckDB reads only what's needed, dramatically reducing I/O.

### 2. Vectorized Execution

Processes data in "vectors" (chunks of 1K–64K rows) instead of row-by-row. Reduces CPU instruction overhead, improves cache efficiency, and leverages SIMD instructions. → See [[vectorized-execution]]

### 3. Parallel Execution

Automatically splits queries across available CPU cores. No configuration required — a laptop can achieve throughput that previously required distributed clusters.

### 4. Late Materialization

Postpones fetching full row data until absolutely necessary. Works with column indices and metadata first, minimizing data movement in memory.

## Key Capabilities

- **Query data in place**: Run SQL directly on CSV, Parquet, JSON, Excel files without loading them first. `SELECT AVG(price) FROM read_csv_auto('data.csv')`
- **Zero-copy DataFrame integration**: Run SQL on pandas/Polars DataFrames without copying data.
- **Larger-than-memory**: Streams data in chunks; 5.8M-row flight dataset uses ~280MB vs. pandas' 4.2GB.
- **Remote file access**: Query files over HTTP/S, S3, GitHub, Hugging Face via the `httpfs` extension.
- **Full SQL**: Standard analytical SQL including window functions, advanced aggregations, CTEs.
- **Python UDFs**: Define custom functions in Python and call them from SQL.

## Getting Started

```
# Install
pip install duckdb

# In Python
import duckdb

# Query a CSV directly — no loading needed
result = duckdb.query("""
    SELECT category, AVG(price) as avg_price
    FROM read_csv_auto('products.csv')
    GROUP BY category
    ORDER BY avg_price DESC
""")

# Convert to pandas DataFrame
print(result.df())

```

## When to Use / When Not to Use

| ✅ Use DuckDB | ❌ Don't Use DuckDB |
| --- | --- |
| Exploratory analysis on CSV/Parquet | High-volume OLTP (use PostgreSQL/MySQL) |
| Prototyping analytics pipelines | Multi-user concurrent writes (single-writer) |
| Embedding SQL in Python/R apps | Real-time streaming ingestion (use Kafka + Flink) |
| Local dev and testing of data workflows | Need full client-server multi-tenancy |
| "Larger-than-memory" datasets on a laptop | Fastest raw CSV parsing ([[apache-datafusion|DataFusion]] ~5× faster on CSV, but DuckDB wins on Parquet) |

## Ecosystem & Extensions

| Extension | Purpose |
| --- | --- |
| `httpfs` | Query remote files over HTTP/S (S3, GitHub, Hugging Face) |
| `spatial` | Geospatial data types and functions |
| `json` | Advanced JSON parsing and querying |
| `icu` | Unicode and locale-aware string operations |
| `iceberg` | Read/write [[apache-iceberg|Apache Iceberg]] tables with time travel (✅ stable, 2026-06) |
| `vortex` | Read/write [[vortex-file-format|Vortex]] files (⚠️ early-stage, reported OOM crashes on multi-file reads as of 2026-05) |
| `delta` | Read/write [[delta-lake|Delta Lake]] tables with time travel (✅ stable, 2026-05) |
| `unity_catalog` | Query and write through [[unity-catalog|Unity Catalog]] — governed lakehouse access (✅ stable, 2026-05) |

**Languages**: Python, R, Julia, C/C++, Java, Go, Rust, Node.js.

**MotherDuck**: A managed SaaS platform built around DuckDB that enables hybrid queries — joining local data with cloud tables in a single SQL statement.
---
- Powered by [[vectorized-execution]] — one of DuckDB's four architectural pillars
- Implements [[in-process-olap]] — DuckDB is the canonical example of in-process OLAP
- Related to [[sources/duckdb-up-and-running]] — Wei-Meng Lee's practical guide
- Related to [[sources/benchmarking-vortex-file-format]] — benchmark against Vortex, Polars, DataFusion (Backblaze dataset)
- Competes with [[polars]] — both target Python data engineering; DuckDB uses SQL, Polars uses DataFrame API
- Integrates with [[delta-lake]] — DuckDB's Delta extension supports reads, writes, and time travel (stable)
- Integrates with [[unity-catalog]] — DuckDB's UC extension queries and writes through governed catalogs (stable)
