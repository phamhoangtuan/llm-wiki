---
title: "In-Process OLAP"
type: concept
tags: [database-architecture, olap, analytics, embedded-database]
created: 2026-05-24
updated: 2026-05-24
sources: [duckdb-up-and-running]
---

## Summary

**In-process OLAP** is an architectural pattern where an analytical database runs as an **embedded library** inside the application process — no separate server, no network communication, no infrastructure overhead. It is the OLAP analog of SQLite for OLTP. [[duckdb|DuckDB]] is the canonical implementation.

## In-Process vs. Client-Server

| Aspect | In-Process OLAP (DuckDB) | Client-Server OLAP (Snowflake, BigQuery) |
| --- | --- | --- |
| **Setup** | `pip install duckdb` | Provision cluster, configure networking |
| **Communication** | Direct function calls | Network (TCP/TLS, driver protocol) |
| **Latency** | Zero — no network hop | Network latency per query (ms) |
| **Data locality** | Data can be local files (CSV, Parquet) | Data must be loaded into warehouse storage |
| **Multi-user** | Single-writer (embedded) | Multi-user, concurrent reads/writes |
| **Scaling** | Vertical (one machine's cores) | Horizontal (add more nodes) |
| **Cost** | Free (open-source, runs on your hardware) | Pay per query / storage / compute |

## Why In-Process Matters for Analytics

- **Zero "infrastructure tax"**: No server config, no permission management, no networking setup. Focus on analysis, not administration.
- **Query data in place**: Run SQL directly on local CSV, Parquet, or pandas DataFrames. Skip the traditional ELT "Load" step — just point and query.
- **Development velocity**: Fast iteration loop — prototype locally with real SQL, then scale to cloud warehouses when collaboration demands it.
- **Hybrid workflows**: With [MotherDuck](https://motherduck.com), join local data with cloud tables in a single query, keeping sensitive data local.

## The Pattern: Local → Cloud Gradient

```
Local Exploration (In-Process OLAP)
    ↓
    Fast iteration on laptop
    DuckDB: query CSV/Parquet/pandas directly
    
Cloud Warehousing (Client-Server OLAP)
    ↓
    Scale for team/enterprise
    Snowflake/BigQuery: shared data, concurrent access
    
Production Deployment
    ↓
    Embed analytics in apps
    DuckDB: ship analytical SQL inside your application

```

## Related Patterns

- **In-process OLTP**: SQLite — the same embedded-library approach but for transactional (row-based) workloads.
- **Embedded analytical engines**: Apache DataFusion (Rust), Velox (C++, Meta) — in-process query engines without a full database.
- **Hybrid cloud**: MotherDuck, TileDB — keep local data local, share aggregated results in the cloud.

## Limitations

- **Single-writer**: Not designed for concurrent write transactions (use client-server for that).
- **Vertical scaling only**: Limited to one machine's CPU cores and memory — can't horizontally scale across nodes.
- **Process lifecycle**: Database lives and dies with the application process (or is persisted to disk).
---
- Core to [[duckdb]] — "SQLite for analytics" — the reference implementation
- Enabled by [[vectorized-execution]] — makes in-process analytical performance practical
- Related to [[sources/duckdb-up-and-running]] — Wei-Meng Lee's guide covers the in-process architecture
