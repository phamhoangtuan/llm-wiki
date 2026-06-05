---
title: "Unity Catalog"
type: concept
tags: [data-governance, catalog, unity-catalog, delta-lake, lakehouse, duckdb]
created: 2026-05-28
updated: 2026-05-31
sources: [delta-grows-up-writes-unity-catalog, delta-catalog-managed-tables]
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

With Delta Lake 4.1.0 and Unity Catalog 0.4.0, catalog-managed tables represent a fundamental architectural shift: the catalog (not the filesystem) becomes the **authority** for table state.

### How the Protocol Works

#### Table Discovery

Clients resolve tables by **logical name** (`catalog.schema.table`) through the catalog — not by filesystem path. The catalog provides identity, location, and access credentials.

#### Reads (Catalog-Mediated)

```
1. Client → get_catalog_commits API → latest ratified commits (0ms to catalog, skip storage)
2. If older history needed → LIST filesystem for published commits + checkpoints
3. Merge catalog commits + filesystem commits → complete snapshot
```

This eliminates the 100ms+ filesystem round-trip for metadata resolution on every query.

#### Writes (Catalog-Ratified)

```
1. Client stages commit → _delta_log/_staged_commits/ (or sends inline to catalog)
2. Client requests ratification from UC
3. UC inspects commit contents, enforces constraints, applies policies
4. UC ratifies or rejects the commit
5. Ratified commits periodically published to the filesystem _delta_log/
```

**Inline commits**: Commit payload is sent directly to the catalog, skipping filesystem write entirely → sub-100ms commit latency.

### Filesystem-Managed (Legacy) vs Catalog-Managed

| Aspect | Without Catalog Commits | With Catalog Commits |
|---|---|---|
| **Discovery** | Clients need exact filesystem path | Clients resolve by name through catalog |
| **Authorization** | Coarse-grained storage credentials | Fine-grained catalog-level access control |
| **Writes** | Filesystem "PUT-if-absent" determines winner | Catalog ratifies; inspects content, enforces constraints |
| **Schema changes** | Unvalidated — incompatible changes can break pipelines | Catalog validates before accepting commits |
| **Metadata latency** | Replay `_delta_log` from filesystem (100ms+) | `get_catalog_commits` direct from catalog |

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

## Convergence with Iceberg

Delta's catalog-managed design closely resembles [[apache-iceberg|Iceberg]]'s catalog model. Since Unity Catalog can govern both formats, this convergence enables:
- **Consistent governance** across Delta and Iceberg from a single catalog
- **Multi-engine interoperability** — any engine speaking UC's API can access either format
- **Simplified operations** — no format-specific access patterns to manage

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
- Benchmark source: [[sources/delta-grows-up-writes-unity-catalog]] — DuckDB Labs announces stable UC extension with Catalog Commits
- Benchmark source: [[sources/delta-catalog-managed-tables]] — architectural shift: filesystem-managed → catalog-managed (Delta 4.1.0 + UC 0.4.0)
