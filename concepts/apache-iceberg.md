---
title: "Apache Iceberg"
type: concept
tags: [table-formats, data-lake, iceberg, data-engineering, lakehouse]
created: 2026-05-26
updated: 2026-05-31
sources: [hugo-data-ingestion-platform-flink, delta-grows-up-writes-unity-catalog]
---

## Summary

**Apache Iceberg** is an open-source table format for large analytic datasets, designed to bring ACID transactions, schema evolution, and time travel to data lakes. It is Grab's planned future table format for Hugo's data lake, replacing Hive tables to improve pipeline SLAs and reduce costs.

## Key Features

- **ACID transactions** — serializable isolation for concurrent reads and writes
- **Schema evolution** — add, drop, rename, reorder columns without rewriting data
- **Partition evolution** — change partition scheme without rewriting existing data
- **Time travel** — query data as it existed at any point in time
- **Hidden partitioning** — partition values derived automatically; no need for users to specify partition columns in queries
- **Engine-agnostic** — works with Spark, Flink, Trino, Presto, Hive, Impala, DuckDB

## Comparison with Other Table Formats

| Feature | Iceberg | Hive | Delta Lake | Hudi |
|---|---|---|---|---|
| ACID | ✅ | ❌ | ✅ | ✅ |
| Schema evolution | ✅ | ❌ (manual) | ✅ | ✅ |
| Partition evolution | ✅ | ❌ | ❌ | ❌ |
| Time travel | ✅ | ❌ (manual snapshots) | ✅ | ✅ |
| Hidden partitioning | ✅ | ❌ | ❌ | ❌ |
| Engine support | Broad (5+ engines) | Broad | Spark-primary | Spark-primary |

## Why Grab is Considering Iceberg

Hugo currently writes to Hive tables (with Spark compaction). Iceberg would address:
- **SLA improvements** — ACID transactions prevent inconsistent reads during compaction
- **Cost reduction** — hidden partitioning eliminates expensive full-table scans caused by incorrect partition filters
- **Schema evolution** — current Hive schema changes require manual intervention; Iceberg supports online, non-blocking schema changes

→ See [[data-ingestion]] for Hugo's current architecture and [[apache-flink]] for Flink's Iceberg sink connector.

> **Note**: This page is a stub — Iceberg was mentioned as a future direction in the Hugo article but not evaluated in depth. A dedicated source would add substance.
---
- Related to [[data-ingestion]] — Iceberg is the planned next-gen table format for Hugo's data lake
- Integrates with [[apache-flink]] — Flink has an Iceberg sink connector for writing streaming data to Iceberg tables
- Reference: [[hugo-data-ingestion-platform-flink]] — mentioned as Hugo's future table format to replace Hive
- Competes with [[delta-lake]] — Iceberg and Delta are the two dominant open table formats; Iceberg has partition evolution, Delta has deeper Databricks integration
