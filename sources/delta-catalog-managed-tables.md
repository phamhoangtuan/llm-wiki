---
title: "The Next Evolution of Delta — Catalog-Managed Tables"
type: source
source_type: article
author: "Benjamin Mathew, Scott Sandre, Scott Haines"
url: "https://delta.io/blog/2026-02-02-delta-catalog-managed-tables/"
source_date: 2026-02-02
ingested: 2026-05-31
tags: [delta-lake, unity-catalog, catalog-managed-tables, lakehouse, data-governance]
concepts: [delta-lake, unity-catalog]
---

## Summary

With **Delta Lake 4.1.0** and **Unity Catalog 0.4.0**, Delta introduces **catalog-managed tables** — a fundamental shift where the catalog (not the filesystem) becomes the authority for table identity, discovery, authorization, and commit coordination. This moves Delta toward the catalog-managed model pioneered by Iceberg and creates a shared foundation for interoperable lakehouse tables.

## Before: Filesystem-Managed Delta (Legacy)

In the traditional model, the filesystem (`_delta_log/`) was the primary authority:

1. **Discovery**: Clients needed the exact filesystem path to the table
2. **Authorization**: Credentials managed directly by the storage system — coarse-grained access
3. **Commits**: Atomic writes via filesystem "PUT-if-absent" APIs — filesystem determines write winner
4. **Read planning**: Replay the Delta transaction log from the filesystem → 100+ ms latency per query

Challenges:
- **Brittle path-based access**: Table relocation broke pipelines
- **Risky coarse-grained authorization**: Fragmented governance across storage systems
- **Unsafe schema changes**: Path-based writes could modify schemas without validation
- **Bottlenecked performance**: Log replay added latency to every query

## After: Catalog-Managed Delta (Delta 4.1.0+)

### Table Discovery

Clients resolve tables by **name** (e.g., Unity Catalog's three-level namespace: `catalog.schema.table`), not by filesystem path. The catalog provides table identity, location, and access credentials before any storage interaction.

### Reads

1. Client calls `get_catalog_commits` API to retrieve the **latest ratified commits** from the catalog
2. If older history is needed, the client LISTs the filesystem for published commits and checkpoints
3. The client **merges** catalog-provided commits with filesystem-discovered commits to build a complete snapshot

This means the catalog always serves the most recent table state, while long-term commit storage remains in the filesystem.

### Writes (Catalog Commits)

1. Client **stages** commits in `_delta_log/_staged_commits/` directory (or sends inline)
2. Client requests **ratification** from the catalog
3. The catalog inspects commit contents, enforces constraints, and applies policies
4. The catalog ratifies (accepts) or rejects the commit
5. Ratified commits are periodically **published** to the filesystem `_delta_log/`

**Inline commits**: Commit contents can be sent directly to the catalog, skipping the 100ms+ filesystem write entirely — enabling sub-100ms commits.

### Authorization

The catalog becomes the single point of governance:
- Fine-grained access control per table/column
- Schema and constraint validation on every commit
- Catalog can distinguish between "write data" and "modify schema" permissions
- No more fragmented storage-level policies

## Enabling Catalog-Managed Tables

```sql
CREATE TABLE sanctuary.pets (...)
USING DELTA
TBLPROPERTIES ('delta.feature.catalogManaged' = 'supported');
```

The `delta.feature.catalogManaged` property opts the table into catalog-managed mode. Without it, Delta falls back to filesystem-based coordination.

## Convergence with Iceberg

Delta's catalog-managed design closely resembles Iceberg's catalog model. This convergence means:
- **Consistent governance** across Delta and Iceberg tables
- **Multi-engine interoperability** — any engine that speaks the catalog API can access either format
- **Single catalog** for discovery and authorization regardless of underlying table format

## Links

- [Delta Lake 4.1.0 release](https://github.com/delta-io/delta/releases/tag/v4.1.0)
- [Unity Catalog 0.4.0 release](https://github.com/unitycatalog/unitycatalog/releases/tag/v0.4.0)
- [Catalog-Managed Tables protocol (RFC)](https://github.com/delta-io/delta/blob/master/PROTOCOL.md#catalog-managed-tables)
- [Unity Catalog Playground (Docker)](https://github.com/newfront/unitycatalog-playground/)
