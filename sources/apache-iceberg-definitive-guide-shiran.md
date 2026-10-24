---
title: "Apache Iceberg: The Definitive Guide — Tomer Shiran"
type: source
source_type: book
author: "Tomer Shiran"
url: ""
source_date: 2023
ingested: 2026-10-11
tags: [table-formats, iceberg, data-lakehouse, data-engineering, data-quality]
concepts: [apache-iceberg, data-lakehouse, elt, data-ingestion]
created: 2026-10-11
updated: 2026-10-11
---

## Summary

Tomer Shiran's *Apache Iceberg: The Definitive Guide* (580 pages) is the practical reference for building a reliable lakehouse on Iceberg. The reader's notes condense it into three clusters: **core implementation guidelines** (ACID, schema evolution, hidden partitioning), **performance & scalability** (batch+streaming unification, time travel, metadata pruning), and **operational best practices** (ecosystem integration, CDC automation, storage cost optimization).

## Core Implementation Guidelines

1. **Enforce ACID transactions for reliability** — Iceberg's atomic commits and snapshot isolation ensure data consistency during concurrent writes/reads, preventing partial updates
2. **Leverage schema evolution safely** — add/drop/rename columns without rewriting data or breaking pipelines; adapt to changing business needs
3. **Adopt hidden & evolving partitioning** — decouple partitioning from physical storage; dynamically optimize layouts without costly data reorganization

## Performance & Scalability

1. **Unify batch and streaming workloads** — process historical and real-time data efficiently using shared metadata, reducing pipeline complexity
2. **Optimize queries with time travel** — audit, debug, or roll back data using snapshots, e.g. `SELECT * FROM table TIMESTAMP AS OF '2025-05-01'`
3. **Scale to petabytes with minimal overhead** — metadata pruning (manifest files) accelerates queries on massive datasets

## Operational Best Practices

1. **Integrate with ecosystem tools** — Spark (ETL), Flink (streaming), Dremio (analytics), ML frameworks for end-to-end workflows
2. **Automate CDC and incremental processing** — capture data changes natively via `create_changelog_view` or Debezium/Kafka for real-time synchronization
3. **Optimize storage costs** — compact small files regularly, expire old snapshots, and use partition evolution to reduce storage overhead

## Key Outcomes

- **Solve Hive limitations** — replace fragile partitions and manual schema management with Iceberg's metadata-driven approach
- **Boost data quality** — ACID compliance ensures integrity; time travel simplifies testing and reproducibility
- **Real-world use cases** — BI dashboards, ML feature stores, CDC pipelines (e.g., Netflix's incremental processing)

## Connection to the Wiki

The guide is the book-length companion to [[apache-iceberg]] (already documented here via the 1.11.0 release notes), adding the *how-to-operate* layer: snapshot isolation and time travel connect to [[data-quality-engineering]] and testing; hidden partitioning extends [[liquid-clustering]] and layout work; batch+streaming unification connects to [[elt]] and [[data-ingestion]]; CDC automation ties into the [[change-data-capture|CDC]] concept; and the whole book sits inside [[data-lakehouse]] as the open table format foundation.

---

- Feeds [[apache-iceberg]] — the definitive practical reference behind the concept
- Supports [[data-lakehouse]] — Iceberg as the open table format foundation
- Extends [[elt]] — unified batch+stream with shared metadata reduces pipeline complexity
- Informs [[data-ingestion]] — CDC automation via changelog views and Debezium/Kafka
- Related to [[change-data-capture]] — native changelog views enable real-time sync
- Related to [[data-quality-engineering]] — ACID + time travel as testing/reproducibility tools
- Related to [[liquid-clustering]] — modern layout optimization on Iceberg tables