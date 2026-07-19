---
title: "Medallion Architecture"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [data-engineering, lakehouse, databricks, data-quality]
sources: [big-book-data-engineering]
---

# Medallion Architecture

A data organization pattern that organizes data into three progressive quality tiers: Bronze (raw), Silver (cleaned), and Gold (business-ready). Like water flowing through filtration, data moves from raw → filtered → pure.

## The Three Layers

| Layer | Purpose | Characteristics |
| ------- | --------- | ---------------- |
| **Bronze** 🥉 | Raw ingestion | Append-only, preserves original data, no data loss, schema-as-read |
| **Silver** 🥈 | Cleaned & augmented | Deduplicated, normalized, enriched with reference data, quality-checked |
| **Gold** 🥇 | Business aggregates | Aggregated, ready for dashboards, reports, ML models |

## Why Medallion?

- **Progressive refinement**: Each layer adds value without destroying raw source
- **Reprocessing**: Bronze preserves original — can always rebuild downstream layers
- **Data quality**: Quality checks at each transition gate (Bronze→Silver, Silver→Gold)
- **Access control**: Different consumers access different layers (data scientists need Silver; BI needs Gold)

## Relationship to Lakehouse

Medallion architecture is the canonical data organization pattern within a [[data-lakehouse]]. Open table formats ([[delta-lake|Delta Lake]], [[apache-iceberg|Apache Iceberg]]) provide the ACID guarantees and time travel that make each layer reliable.

## DLT Expectations as Quality Gates

[[delta-live-tables|Delta Live Tables]] implements Medallion with declarative quality expectations at each transition — e.g., "Silver must have no nulls in column X."

---

- Foundation of [[data-lakehouse]] — canonical data organization pattern for lakehouse
- Quality-gated by [[delta-live-tables]] — declarative expectations at each layer transition
- Powered by [[delta-lake]] — ACID transactions and time travel across layers
- Part of [[data-ingestion]] — the Transform pillar of the Data Engineering framework
