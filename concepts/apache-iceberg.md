---
title: "Apache Iceberg"
type: concept
tags: [table-formats, data-lake, iceberg, data-engineering, lakehouse]
created: 2026-05-26
updated: 2026-06-05
sources: [hugo-data-ingestion-platform-flink, delta-grows-up-writes-unity-catalog, debunking-data-layout-myths-liquid-clustering, apache-iceberg-1.11.0-release]
---

## Summary

**Apache Iceberg** is an open-source table format for large analytic datasets, designed to bring ACID transactions, schema evolution, and time travel to data lakes. As of the **1.11.0 release (May 2026)**, Iceberg has stabilized its V3 specification with deletion vectors, variant types, built-in encryption, and a pluggable file format API — marking its evolution from a foundational format to a full-featured lakehouse platform.

## Core Features

- **ACID transactions** — serializable isolation for concurrent reads and writes
- **Schema evolution** — add, drop, rename, reorder columns without rewriting data
- **Partition evolution** — change partition scheme without rewriting existing data (unique among table formats)
- **Time travel** — query data as it existed at any point in time
- **Hidden partitioning** — partition values derived automatically; no need for users to specify partition columns in queries
- **Engine-agnostic** — works with Spark, Flink, Trino, Presto, Hive, Impala, DuckDB

## V3 Specification (Stabilized in 1.11.0)

The V3 spec focuses on optimized read paths, secured metadata, and complex data types:

| Feature | Description |
|---|---|
| **Deletion Vectors** | Roaring bitmaps replace positional delete files; faster row-level deletes without new files per update |
| **Variant type** | Semi-structured JSON data with predicate pushdown; Trino maps native JSON → Iceberg Variant |
| **Geospatial types** | Bounding box types with intersects checking |
| **Nanosecond timestamps** | Precision beyond milliseconds (`TimestampNTZ`) |
| **Manifest list encryption** | GCM stream cipher on manifest lists; prevents metadata inference attacks |

V3 requires explicit table upgrade from V2. Java 17 is the new minimum runtime (Java 11 dropped).

## 1.11.0 Major New Capabilities

### Built-in Table Encryption

Envelope encryption with three-tier key hierarchy:

```
KMS (Master Key, never touches storage)
  └─ wraps → Key Encryption Keys (KEKs, stored in table metadata)
       └─ wraps → Data Encryption Keys (DEKs, unique per file)
```

- **Zero-trust storage** — data unreadable even with direct bucket access
- **Total index protection** — manifest lists encrypted too; statistics cannot be inferred
- **Tamper-proof** — authentication tags on encrypted data
- **Auto key rotation** — no data rewrite needed; satisfies compliance mandates

KMS support: AWS KMS, Azure Key Vault, Google Cloud KMS.

### Pluggable File Format API

Decouples Iceberg metadata from physical storage layouts:
- **FormatModel** — standardized interface for reader/writer per format (Parquet, ORC, Avro)
- **FormatModelRegistry** — engines fetch builders from a central directory
- Enables third-party format plugins (Vortex, Lance) without core Iceberg changes
- Foundation for **Column Families** — vertical partitioning for isolated column rewrites
- Lays groundwork for **V4 manifest specification** — format-agnostic, scales to millions of files

### Server-Side Scan Planning (REST Catalog)

Shifts metadata traversal from engine to catalog:

| Scan Size | Mode | Mechanism |
|---|---|---|
| Small | Immediate | Single `POST …/plan` → `FileScanTask` objects |
| Large | Polling | `POST …/plan` → `plan-id` → poll for results |
| Massive | Parallel | `POST …/plan` → `plan-id` → `POST …/tasks` for parallel retrieval |

Reduces client-side manifest list/manifest file traversal overhead significantly.

### SQL UDF Specification

- Versioned JSON metadata files in object store
- Parameters map to Iceberg Type JSON (nested structs, maps, Variant)
- Atomic rollback to previous versions on buggy UDF deployments
- Engine-specific function implementations per UDF

## Engine Support (1.11.0)

| Engine | Status |
|---|---|
| **Spark 4.1** | Default build target; `MERGE INTO` with `WITH SCHEMA EVOLUTION`; async micro-batch planner |
| **Spark 4.0, 3.5, 3.4** | Backports: `AvailableNow` trigger, partition stats |
| **Flink 2.1** | Default build target; DynamicIcebergSink, post-commit maintenance |
| **Flink 1.20** | Active support |
| **Flink 1.19** | **Deprecated** |
| **Spark 3.4** | **Deprecated** |

## Comparison with Other Table Formats

| Feature | Iceberg | Hive | Delta Lake | Hudi |
|---|---|---|---|---|
| ACID | ✅ | ❌ | ✅ | ✅ |
| Schema evolution | ✅ | ❌ (manual) | ✅ | ✅ |
| Partition evolution | ✅ | ❌ | ❌ | ❌ |
| Time travel | ✅ | ❌ (manual snapshots) | ✅ | ✅ |
| Hidden partitioning | ✅ | ❌ | ❌ | ❌ |
| Table-level encryption | ✅ (1.11.0) | ❌ | ❌ | ❌ |
| Deletion Vectors | ✅ (V3) | ❌ | ❌ (file rewriting) | ❌ |
| Pluggable file formats | ✅ (1.11.0) | ❌ | ❌ | ❌ |
| Engine support | Broad (5+ engines) | Broad | Spark-primary | Spark-primary |

## Hugo Use Case (Grab)

Hugo currently writes to Hive tables (with Spark compaction). Iceberg would address:
- **SLA improvements** — ACID transactions prevent inconsistent reads during compaction
- **Cost reduction** — hidden partitioning eliminates expensive full-table scans caused by incorrect partition filters
- **Schema evolution** — current Hive schema changes require manual intervention; Iceberg supports online, non-blocking schema changes

→ See [[data-ingestion]] for Hugo's current architecture and [[apache-flink]] for Flink's Iceberg sink connector (including DynamicIcebergSink in 1.11.0).

## Liquid Clustering Support

On Databricks, Iceberg tables in Unity Catalog support **[[liquid-clustering|Liquid Clustering]]** — the same modern data layout available for Delta tables. Liquid Clustering is a write-side optimization that produces standard Parquet files with min/max statistics, so any Iceberg-compatible reader benefits from data skipping regardless of whether it runs on Databricks.

## Performance (1.11.0)

- **GCS Analytics Core** — footer prefetching, vectored I/O, small-object caching for Google Cloud Storage
- **Deletion Vector pruning** — manifest partition pruning during DV validation
- **Overwrite-aware table registration** — idempotent catalog operations
- **Scheduled credential refresh** — for S3FileIO and GCSFileIO, eliminating auth expiration failures in long-running jobs
- **Async micro-batch planner** (Spark) — faster Structured Streaming execution
---
- Related to [[data-ingestion]] — Iceberg is the planned next-gen table format for Hugo's data lake
- Integrates with [[apache-flink]] — Flink 2.1 is the default build target; DynamicIcebergSink enables multi-table routing and auto-schema evolution
- Competes with [[delta-lake]] — both dominate the open table format landscape; Iceberg has partition evolution, built-in encryption (1.11.0), and broader engine support; Delta has deeper Databricks integration
- Optimized by [[liquid-clustering]] — modern data layout available for Iceberg tables on Databricks; write-side optimization
- Reference: [[sources/apache-iceberg-1.11.0-release]] — 1.11.0 release blog post with full feature list
