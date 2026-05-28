---
title: "Delta Grows Up: Writes, Unity Catalog and Time Travel"
type: source
source_type: article
author: "Ben Fleis (DuckDB Labs)"
url: "https://delta.io/blog/2026-05-06-delta-grows-up-writes-time-travel-and-unity-catalog/"
source_date: 2026-05-06
ingested: 2026-05-28
tags: [delta-lake, unity-catalog, duckdb, time-travel, data-lake, lakehouse]
concepts: [delta-lake, unity-catalog, duckdb, apache-iceberg]
---

## Summary

DuckDB's Delta and Unity Catalog extensions have graduated from experimental status. The blog (republished from DuckDB's own blog) announces three major capabilities: **write support** (INSERT into Delta tables), **time travel** (query Delta tables at any historical version), and **Unity Catalog integration** including **Catalog Managed Tables** with concurrent write coordination.

## Key Announcements

### 1. Delta Writes (INSERT)

DuckDB can now write to Delta tables — not just read them:

```sql
ATTACH './path/to/my_table' AS my_table (TYPE delta);
INSERT INTO my_table VALUES ('Question 2', 2), ('The Answer', 42);
INSERT INTO my_table FROM (SELECT text || ' (copy)', code + 100 FROM my_table);
```

Multiple INSERTs within a `BEGIN`/`COMMIT` block are stored as a single Delta version (atomic commit). UPDATE, MERGE, and DELETE are on the roadmap but not yet supported.

### 2. Time Travel

Query Delta tables at any historical version:

```sql
-- Query specific version inline
SELECT count() FROM my_table AT (VERSION => 0);  -- v0

-- Attach pinned to a version (stable reference, ignores future writes)
ATTACH './path/to/my_table' AS my_table_v1 (TYPE delta, VERSION 1);

-- Pin to latest at attach time
ATTACH './path/to/my_table' AS my_table_pinned (TYPE delta, PIN_SNAPSHOT);
```

**Incremental snapshot loading** (nightly builds, coming in v1.5.3): when querying nearby versions, DuckDB reuses cached metadata rather than reloading the full Delta log. This provides big wins in lakes with thousands/millions of snapshots.

### 3. Unity Catalog Support

Unity Catalog (UC) is an open standard for governing data and AI assets. DuckDB's UC extension connects to both OSS Unity Catalog (self-hosted) and Databricks Unity Catalog (managed):

```sql
LOAD unity_catalog;
CREATE SECRET (TYPE unity_catalog, TOKEN '...', ENDPOINT 'http://...');
ATTACH 'unity' AS my_catalog (TYPE unity_catalog, DEFAULT_SCHEMA 'my_schema');
SELECT * FROM my_catalog.pets;
INSERT INTO my_catalog.pets ...;  -- Writes through UC!
```

### 4. Catalog Managed Tables & Catalog Commits

**Catalog Managed Tables (CMT)** enable **Catalog Commits (CC)**: every write is staged and registered through UC before becoming visible. UC acts as the commit arbiter:

- First writer wins the version
- Later writers get a conflict error (not silent data loss)
- UC's metadata, audit trail, and statistics stay in sync

In a concurrency test with 20 parallel DuckDB writers (8 at a time), 5 committed successfully and 15 received clear conflict signals — exactly the semantics expected from coordinated concurrent writes.

## Technical Details

| Feature | Status |
|---|---|
| Read Delta tables | ✅ Stable |
| INSERT (writes) | ✅ Stable |
| Time travel (VERSION, PIN_SNAPSHOT) | ✅ Stable |
| Incremental snapshot loading | 🧪 Nightly (→ v1.5.3) |
| Unity Catalog reads | ✅ Stable |
| Unity Catalog writes (CMT) | ✅ Stable |
| UPDATE, MERGE, DELETE | 🔮 Future |
| DDL (CREATE TABLE via UC) | 🔮 Future |
| Multi-table atomic writes | 🔮 Future |

## Stack Implications

The combination of **Delta** (open storage), **Unity Catalog** (governance + coordination), and **DuckDB** (fast analytical queries) forms a production-ready lakehouse stack. Previously, DuckDB could only read Delta tables — now it's a full participant in the Delta ecosystem.

## Links

- [DuckDB Delta Extension docs](https://duckdb.org/docs/current/core_extensions/delta.html)
- [DuckDB Unity Catalog Extension docs](https://duckdb.org/docs/current/core_extensions/unity_catalog.html)
- [Playground Docker image](https://github.com/benfleis/duckdb-unitycatalog-playground/)
- [OSS Unity Catalog](https://unitycatalog.io/)
- [Delta Lake](https://delta.io/)
