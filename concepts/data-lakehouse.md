---
title: "Data Lakehouse"
type: concept
tags: [databricks, data-engineering, architecture, lakehouse]
created: 2026-06-23
updated: 2026-09-20
sources: [databricks-dea-study-guide, big-book-data-engineering, the-data-lakehouse-inmon]
aliases: [Lakehouse architecture]
---

Data Lakehouse is a modern data architecture that combines the economics and scalability of data lakes with the governance and performance of data warehouses into a single unified platform.

## Warehouse vs Lake vs Lakehouse

| Paradigm | Metaphor | Strengths | Weaknesses |
| ---------- | ---------- | ----------- | ------------ |
| Data Warehouse | Organized library | Fast, reliable SQL, structured | Rigid, expensive, struggles with unstructured data |
| Data Lake | Disordered storage shelf | Low cost, massive scale, format flexibility | Poor governance, "data swamps", hard to find data |
| Lakehouse | Smart, adaptable library | Best of both: cheap storage + ACID + governance | Requires modern open table formats (Delta, Iceberg) |

The problem with two separate systems: silos → frequent data transfers → increased complexity → slowed innovation.

## Five Core Benefits

| Benefit | Description |
| --------- | ------------- |
| Openness & Scalability | Low-cost cloud storage, vendor-neutral open formats, handles structured + unstructured |
| Reliability & Governance | Centralized security, ACID transactions, audit-ready compliance |
| Cost-Efficiency | Consolidate workloads, eliminate redundant data movement between systems |
| Unified Platform | Data engineers, scientists, analysts work on same data — one platform for BI + ML |
| Performance | Optimized for high-speed analytics across all data types |

## Medallion Architecture

The canonical data organization pattern within a lakehouse: [[medallion-architecture]] (Bronze → Silver → Gold). Raw data lands in Bronze, gets cleaned in Silver, and becomes business-ready in Gold. Each transition quality-gated by [[delta-live-tables|DLT expectations]].

## Key Enabling Technologies

- **Open table formats**: [[delta-lake|Delta Lake]], [[apache-iceberg|Apache Iceberg]] — provide ACID transactions on data lakes
- **Compute engine**: [[apache-spark]] — high-performance distributed processing
- **Governance**: [[unity-catalog]] — centralized security and access control
- **Abstraction**: [[dbfs]] — cloud storage feels like a local filesystem

## Data Types in the Lakehouse (Inmon)

Inmon's treatment (source: [[sources/the-data-lakehouse-inmon]]) adds practical storage guidance:

- **Avoid storing raw text** in the lakehouse unless explicitly required — prefer structured database storage so text can be analyzed with standard analytical tools
- **Structured data** is best for known, predefined queries; **other unstructured data** is best for exploratory, unknown queries; **textual data** uniquely supports *both* known and unknown analytics
- **Calculated values need context**: a final value is meaningless without knowing *what* was calculated (the definition), *what data* was used (the inputs), and *how* it was computed (the method) — see [[semantic-layer]] and [[data-lineage]]
- **Comprehensive lineage** is mandatory: documentation must cover *every step* of the data's journey, not just one or two — see [[data-lineage]]

> A lakehouse represents a smart, adaptable library that combines the best of both worlds.

---

- Foundation for [[databricks-platform]] — Databricks is the leading commercial Lakehouse implementation
- Foundation for [[delta-lake]] — Delta Lake provides the transactional layer enabling Lakehouse
- Builds on [[apache-spark]] — Spark provides the compute engine for Lakehouse analytics
- Related to [[lambda-architecture]] — lakehouses reduce the need for separate batch/speed storage paths
- Related to [[kappa-architecture]] — unified lakehouse storage supports single-path streaming replay
- Uses [[medallion-architecture]] — the canonical data organization pattern for lakehouse platforms
- Related to [[snowflake-data-cloud]] — Snowflake is a proprietary lakehouse platform with separated storage/compute
- Informed by [[the-data-lakehouse-inmon]] — data-type suitability, text storage, calculated-value context, full lineage
- Feeds [[data-lineage]] — every-step lineage as a lakehouse trust requirement
