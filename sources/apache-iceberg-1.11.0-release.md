---
title: "Apache Iceberg 1.11.0 Release"
type: source
source_type: article
author: "Apache Iceberg PMC"
url: "https://iceberg.apache.org/blog/apache-iceberg-1.11.0-release/"
source_date: 2026-05-19
ingested: 2026-06-05
created: 2026-06-05
updated: 2026-06-15
tags: [iceberg, table-formats, data-lake, release-notes]
concepts: [apache-iceberg, apache-flink, apache-parquet]
---

## Summary

Apache Iceberg 1.11.0, released May 19, 2026, is a major milestone that moves beyond incremental enhancements to deliver fundamental architectural changes. This release stabilizes the **V3 specification**, introduces **built-in table encryption**, a **pluggable File Format API**, **server-side scan planning**, and a **SQL UDF specification**. It also upgrades engine support to Spark 4.1 and Flink 2.1.

## Key Features

### V3 Specification Stabilization

The V3 spec reaches production maturity, focusing on optimized read paths, secured metadata, and standardized complex data types:
- **Deletion Vectors** — Roaring bitmaps replacing positional delete files for improved row-level delete performance
- **Variant type** — Semi-structured JSON-like data with predicate pushdown (Trino maps native `JSON` to Iceberg Variant)
- **Geospatial types** — Bounding box types with intersects checking
- **Nanosecond timestamps** — Precision beyond milliseconds

Format version 3 is required for all these features; V2 tables need explicit upgrade.

### Built-in Table Encryption

Envelope encryption with a three-tier key hierarchy:
1. **Table master key** — stored securely in KMS (AWS/Azure/GCP), never touches Iceberg storage
2. **Key-encryption keys (KEKs)** — wrapped by master key, stored in table metadata
3. **Per-file data-encryption keys (DEKs)** — wrapped by KEKs, unique per file

Manifest lists are encrypted using Galois/Counter Mode (GCM) stream cipher, preventing metadata inference attacks. Supports automatic key rotation for compliance.

### Server-Side Scan Planning (REST Catalog)

Shifts metadata traversal from the query engine to the catalog:
- Engine submits `POST …/plan` with scan details
- REST catalog returns optimized `FileScanTask` objects
- Supports three modes: immediate (small scans), polling via `plan-id` (large scans), parallel `plan-tasks` via `POST …/tasks` (massive datasets)

Eliminates expensive manifest list/manifest file traversal on the client side.

### Pluggable File Format API

Decouples Iceberg core metadata management from physical storage layouts:
- **FormatModel** — standardized interface for reader/writer construction
- **FormatModelRegistry** — central directory for engines to fetch builders
- Enables integration of next-generation formats (Vortex, Lance) without modifying core Iceberg
- Supports **Column Families** — vertical partitioning for isolated column rewrites (e.g., recalculating embeddings without touching other columns)

Foundations for V4 manifest specification laid in this API.

### SQL UDF Specification

New metadata format for scalar and table functions:
- Self-contained, versioned JSON files in object store
- Atomic rollback to previous versions on buggy deployments
- Parameters map to Iceberg Type JSON representations (nested structs, maps, Variant)
- Engine-specific function implementations per UDF

### Engine Upgrades

- **Spark 4.1** — new default build target; `MERGE INTO` with automatic schema evolution (`WITH SCHEMA EVOLUTION` clause); async micro-batch planner for Structured Streaming; DSv2 API modernization
- **Flink 2.1** — new default build target; **DynamicIcebergSink** (experimental): single sink routes records to tables at runtime, auto-creates tables, evolves schemas on the fly, drops unused columns
- **Flink post-commit maintenance** — arbitrary tasks attachable to `IcebergSink` builder; branch compaction support in `RewriteDataFiles`
- **Spark 4.0, 3.5, 3.4** — backported features: `AvailableNow` trigger, partition statistics files
- **Java 17 required** — Java 11 support dropped; Spark 3.4 and Flink 1.19 deprecated

### Google Cloud Storage Performance

Embedded GCS Analytics Core library into `GCSFileIO`:
- Footer Prefetching — caches Parquet object suffixes to eliminate network overhead
- Threaded VectoredIO — concurrent multi-range operations
- Small object caching — for files under 1MB

### Other Notable Changes

- **Overwrite-aware table registration** — idempotent catalog registration
- **Scheduled credential lifecycle refresh** — for S3FileIO and GCSFileIO
- **Deletion Vector pruning** — manifest partition pruning during DV validation in `MergingSnapshotProducer`
- **Dependency bumps**: Parquet 1.17.1, ORC 1.9.8, Hadoop 3.4.2, Jackson 2.20.0, AWS SDK 2.33.4, Netty 4.2.5, Guava 33.5.0, Nessie 0.105.3

## Key Takeaways

1. **V3 is production-ready** — deletion vectors, Variant, geospatial, nanosecond timestamps are stable defaults
2. **Security is now first-class** — table-level encryption with KMS-backed envelope encryption; no more reliance on bucket-level security alone
3. **Scan planning moves server-side** — significant reduction in client-side metadata overhead for large tables
4. **Format API opens the ecosystem** — Vortex, Lance, and future formats can plug in without core changes
5. **Streaming matures** — DynamicIcebergSink and post-commit maintenance make Flink a first-class streaming writer for Iceberg
