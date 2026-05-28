---
title: "Unity Catalog"
type: concept
tags: [data-governance, catalog, unity-catalog, delta-lake, lakehouse, duckdb]
created: 2026-05-28
updated: 2026-05-28
sources: [delta-grows-up-writes-unity-catalog]
aliases: [UC]
---

## Summary

**Unity Catalog (UC)** is an open standard (and open-source implementation) for governing data and AI assets — tables, volumes, models, and functions — across engines and clouds. It provides a single place to discover, audit, and control access to data, turning a data lake into a governed lakehouse. DuckDB's Unity Catalog extension graduated from experimental status in 2026-05, supporting both reads and writes through UC.

## What Unity Catalog Provides

| Capability | Description |
|---|---|
| **Discovery** | Single catalog of all data assets across engines and storage locations |
| **Access control** | Fine-grained permissions on tables, schemas, catalogs |
| **Audit trail** | Who accessed what, when — unified across engines |
| **Metadata sync** | Table schemas, statistics, and lineage kept in sync |
| **Write coordination** | Catalog Commits arbitrate concurrent writes to Delta tables |

## Two Implementations

| Aspect | OSS Unity Catalog | Databricks Unity Catalog |
|---|---|---|
| **Deployment** | Self-hosted (Docker, K8s) | Managed SaaS (Databricks) |
| **Cost** | Free (open source) | Part of Databricks platform |
| **API** | UC Open API | UC Open API + Databricks extensions |
| **Best for** | Custom lakehouse stacks, experimentation | Databricks-centric organizations |

OSS Unity Catalog can be Docker-ified in minutes — DuckDB Labs provides a [playground image](https://github.com/benfleis/duckdb-unitycatalog-playground/) bundling UC + DuckDB.

## DuckDB Integration

Connecting DuckDB to Unity Catalog:

```sql
LOAD unity_catalog;

CREATE SECRET (
    TYPE     unity_catalog,
    TOKEN    'your-token',
    ENDPOINT 'https://your-workspace.cloud.databricks.com'
);

ATTACH 'unity' AS my_catalog
    (TYPE unity_catalog, DEFAULT_SCHEMA 'my_schema');

-- Read through UC
SELECT * FROM my_catalog.pets;

-- Write through UC (INSERT, Delta tables)
INSERT INTO my_catalog.pets (name, age) VALUES ('Luna', 3);
```

## Catalog Managed Tables & Catalog Commits

The key feature for production usage is **Catalog Managed Tables (CMT)** with **Catalog Commits (CC)**:

### Without Catalog Commits (the problem)

```
DuckDB --writes--> Delta log directly
                    ↓
              UC metadata out of sync
              UC audit trail incomplete
              Other engines see stale state
```

Writes go directly to the Delta transaction log, bypassing UC entirely. UC's metadata, audit trail, and statistics fall out of sync with actual table state.

### With Catalog Commits (the solution)

```
DuckDB --stages commit--> _staged_commits/
           ↓
        UC registers commit
           ↓
    UC arbitrates (first writer wins)
           ↓
    UC metadata stays in sync
    UC audit trail is complete
    All engines see consistent state
```

Every write is staged and registered through UC before becoming visible. UC preserves the first writer's commit and sends conflict errors to later writers — no silent data loss.

### Concurrency Test (20 writers, 8 parallel)

In DuckDB Labs' test:
- 5 writers committed successfully
- 15 received clear conflict signals (not silent failures)
- In a real workload, conflicted writers would retry

```
[worker 6] OK - inserted 5 rows
[worker 5] CONFLICT - another writer won this version, retry needed
[worker 2] CONFLICT - another writer won this version, retry needed
...
```

Catalog Commits coordinate **per table** — no cross-table atomicity. Two tables in the same `BEGIN`/`COMMIT` block commit independently.

## Enabling Catalog Managed Tables

Set the table property at creation time (via Spark or UC CLI; DuckDB's `CREATE TABLE` DDL via UC is on the roadmap):

```sql
-- Via Spark
CREATE TABLE my_catalog.my_schema.concurrent_tbl (...)
TBLPROPERTIES ('delta.feature.catalogManaged' = 'supported');
```

Once enabled, DuckDB INSERTs automatically route through UC's commit staging.

## When to Use Unity Catalog

| ✅ Use Unity Catalog | ❌ Skip Unity Catalog |
|---|---|
| Multi-engine lakehouse (DuckDB + Spark + Trino) | Single-engine setup |
| Need governance (access control, audit) | No regulatory/compliance requirements |
| Concurrent writers to same Delta table | Single-writer pipelines |
| Databricks shop wanting open standards | Custom metadata store already in place |
---
- Governs [[delta-lake]] — UC is the native catalog for Delta tables; Catalog Commits coordinate concurrent writes
- Integrates with [[duckdb]] — DuckDB's UC extension (stable) supports reads and writes through UC-managed catalogs
- Related to [[apache-iceberg]] — UC can catalog Iceberg tables too; Iceberg also has its own catalog ecosystem (REST catalog, Hive, Glue)
- Benchmark source: [[delta-grows-up-writes-unity-catalog]] — DuckDB Labs announces stable UC extension with Catalog Commits
