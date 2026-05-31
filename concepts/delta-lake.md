---
title: "Delta Lake"
type: concept
tags: [table-formats, data-lake, delta-lake, lakehouse, duckdb, data-engineering]
created: 2026-05-28
updated: 2026-05-31
sources: [delta-grows-up-writes-unity-catalog, delta-catalog-managed-tables]
aliases: [Delta]
---

## Summary

**Delta Lake** is an open-source storage framework that brings ACID transactions, time travel, and schema enforcement to data lakes. It is one of the three major open table formats (alongside [[apache-iceberg|Apache Iceberg]] and Apache Hudi) for building lakehouse architectures. Delta Lake stores data as [[apache-parquet|Parquet]] files with a transaction log (`_delta_log/`) that tracks every change — enabling versioning, rollback, and concurrent read/write coordination.

## Core Features

| Feature | Description |
|---|---|
| **ACID transactions** | Serializable isolation for concurrent reads and writes |
| **Time travel** | Query data as it existed at any historical version (`VERSION AS OF`) |
| **Schema enforcement** | Rejects writes with mismatched schema; schema evolution via explicit DDL |
| **Schema evolution** | Add, rename, reorder columns; automatic for compatible changes |
| **Compaction (OPTIMIZE)** | Merge small files into larger ones for better query performance |
| **File skipping** | Statistics in the transaction log let engines skip irrelevant files via filter pushdown |
| **Z-ordering** | Multi-dimensional clustering for faster queries on multiple columns |

## Architecture

A Delta table is a directory of Parquet files plus a transaction log:

```
my_table/
├── _delta_log/
│   ├── 00000000000000000000.json   # Version 0
│   ├── 00000000000000000001.json   # Version 1
│   └── 00000000000000000002.json   # Version 2
├── part-00000-xxx.parquet
├── part-00001-xxx.parquet
└── ...
```

Each JSON log entry records which files were added/removed in that version, plus statistics (min/max per column, row count) for file skipping.

## Time Travel

Delta's transaction log enables querying historical snapshots. In [[duckdb|DuckDB]]'s Delta extension:

```sql
-- Query specific version
SELECT count() FROM my_table AT (VERSION => 0);

-- Attach pinned to a specific version (stable, ignores future writes)
ATTACH './my_table' AS my_table_v1 (TYPE delta, VERSION 1);

-- Attach pinned to latest at attach time
ATTACH './my_table' AS my_table_snapped (TYPE delta, PIN_SNAPSHOT);
```

Incremental snapshot loading (DuckDB nightly, → v1.5.3) reuses cached log metadata across nearby versions, making time travel fast even in lakes with millions of snapshots.

## DuckDB Delta Extension

As of 2026-05, DuckDB's Delta extension is **stable** (no longer experimental):

| Capability | Status |
|---|---|
| Read Delta tables | ✅ Stable |
| INSERT (append writes) | ✅ Stable |
| Time travel | ✅ Stable |
| UPDATE, MERGE, DELETE | 🔮 Future |
| Multi-table atomic writes | 🔮 Future |

Multiple INSERTs in a `BEGIN`/`COMMIT` block create a single atomic Delta version.

## Delta vs Iceberg vs Hudi

| Feature | Delta Lake | Apache Iceberg | Apache Hudi |
|---|---|---|---|
| ACID | ✅ | ✅ | ✅ |
| Time travel | ✅ (via version) | ✅ (via snapshot) | ✅ (via commit time) |
| Schema evolution | ✅ | ✅ | ✅ |
| Partition evolution | ❌ (static) | ✅ (dynamic) | ❌ (static) |
| Hidden partitioning | ❌ | ✅ | ❌ |
| Compaction | OPTIMIZE | Rewrite data files | Clustering + compaction |
| Catalog integration | Unity Catalog (native) | Multiple catalogs | Hive Metastore |
| DuckDB support | ✅ (read + write) | ✅ (via Iceberg ext) | ❌ |

→ See [[apache-iceberg]] for the Iceberg comparison perspective.

## Catalog-Managed Tables (Delta 4.1.0+)

Delta 4.1.0 introduces **catalog-managed tables** — a fundamental architectural shift where the catalog (not the filesystem) becomes the authority for table identity, discovery, authorization, and commit coordination.

### Filesystem-Managed (Legacy) vs Catalog-Managed

| Aspect | Filesystem-Managed (Legacy) | Catalog-Managed (4.1.0+) |
|---|---|---|
| **Discovery** | Clients know exact filesystem path | Clients resolve by name (`catalog.schema.table`) |
| **Authorization** | Coarse-grained storage credentials | Fine-grained catalog-level access control |
| **Reads** | Replay `_delta_log` from filesystem (100ms+ latency) | `get_catalog_commits` API → direct metadata, skip storage |
| **Writes** | Filesystem "PUT-if-absent" determines winner | Catalog ratifies commits; can inspect/enforce/reject |
| **Schema changes** | Unvalidated — incompatible changes possible | Catalog validates before accepting commits |

### Reads (Catalog-Mediated)

1. Client calls `get_catalog_commits` API → retrieves **latest ratified commits** directly from catalog
2. If older history is needed, LIST the filesystem for published commits and checkpoints
3. Merge catalog + filesystem commits to build complete snapshot

The catalog always serves the most recent table state; long-term storage stays in the filesystem.

### Writes (Catalog Commits)

1. Client **stages** commit to `_delta_log/_staged_commits/` (or sends **inline**)
2. Client requests **ratification** from the catalog
3. Catalog inspects commit contents, enforces constraints, applies policies
4. Catalog **ratifies** (accepts) or **rejects** the commit
5. Ratified commits are periodically **published** to the filesystem `_delta_log/`

**Inline commits**: Commit payload sent directly to catalog — skips the 100ms+ filesystem write. Enables sub-100ms commits for latency-sensitive workloads.

### Enabling Catalog-Managed Mode

```sql
CREATE TABLE catalog.schema.table (...)
USING DELTA
TBLPROPERTIES ('delta.feature.catalogManaged' = 'supported');
```

Without this property, Delta falls back to standard filesystem-based coordination.

### Convergence with Iceberg

Delta's catalog-managed design closely resembles [[apache-iceberg|Iceberg]]'s catalog model. This shared foundation enables:
- **Consistent governance** across formats from a single catalog
- **Multi-engine interoperability** — any engine speaking the catalog API can access either format
- **Simplified operations** — no need to manage format-specific access patterns

## Unity Catalog Integration

[[unity-catalog|Unity Catalog]] 0.4.0+ is the first open lakehouse catalog to support catalog-managed Delta tables. The UC integration provides:

| Feature | Mechanism |
|---|---|
| **Table discovery** | Three-level namespace (`catalog.schema.table`) |
| **Authorization** | Fine-grained access control per table/column |
| **Commit coordination** | UC ratifies commits; validates constraints before accepting |
| **Inline commits** | Commit metadata sent directly to UC (sub-100ms latency) |
| **Audit trail** | All ratified commits tracked by UC |

→ See [[unity-catalog]] for UC's catalog commit protocol details.

## When to Use Delta

| ✅ Use Delta | ❌ Use Something Else |
|---|---|
| Databricks/Spark-centric ecosystem | Iceberg-native engines (Trino, Flink prefer Iceberg) |
| Need Unity Catalog governance | Using AWS Glue Catalog (→ Iceberg) |
| DuckDB reads + writes to lakehouse | Read-only DuckDB analytics (either works) |
| Can tolerate static partitioning | Need partition evolution (→ Iceberg) |
---
- Competes with [[apache-iceberg]] — both are open table formats for lakehouse architectures; Iceberg has partition evolution, Delta has deeper Databricks integration
- Stores data as [[apache-parquet]] — Delta tables are Parquet files + transaction log
- Integrates with [[duckdb]] — DuckDB's Delta extension supports reads, writes, and time travel (stable as of 2026-05)
- governed by [[unity-catalog]] — UC provides catalog management and concurrent write coordination for Delta tables
- Benchmark source: [[delta-grows-up-writes-unity-catalog]] — DuckDB Labs announces stable Delta writes, time travel, and UC support
- Powered by [[delta-catalog-managed-tables]] — architectural shift from filesystem-managed to catalog-managed tables (Delta 4.1.0)
