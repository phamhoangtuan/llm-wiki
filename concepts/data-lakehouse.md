---
title: "Data Lakehouse"
type: concept
tags: [databricks, data-engineering, architecture, lakehouse]
created: 2026-06-23
updated: 2026-06-23
sources: [databricks-dea-study-guide]
aliases: [Lakehouse architecture]
---

Data Lakehouse is a modern data architecture that combines the economics and scalability of data lakes with the governance and performance of data warehouses into a single unified platform.

## Warehouse vs Lake vs Lakehouse

| Paradigm | Metaphor | Strengths | Weaknesses |
|----------|----------|-----------|------------|
| Data Warehouse | Organized library | Fast, reliable SQL, structured | Rigid, expensive, struggles with unstructured data |
| Data Lake | Disordered storage shelf | Low cost, massive scale, format flexibility | Poor governance, "data swamps", hard to find data |
| Lakehouse | Smart, adaptable library | Best of both: cheap storage + ACID + governance | Requires modern open table formats (Delta, Iceberg) |

The problem with two separate systems: silos → frequent data transfers → increased complexity → slowed innovation.

## Five Core Benefits

| Benefit | Description |
|---------|-------------|
| Openness & Scalability | Low-cost cloud storage, vendor-neutral open formats, handles structured + unstructured |
| Reliability & Governance | Centralized security, ACID transactions, audit-ready compliance |
| Cost-Efficiency | Consolidate workloads, eliminate redundant data movement between systems |
| Unified Platform | Data engineers, scientists, analysts work on same data — one platform for BI + ML |
| Performance | Optimized for high-speed analytics across all data types |

## Key Enabling Technologies

- **Open table formats**: [[delta-lake|Delta Lake]], [[apache-iceberg|Apache Iceberg]] — provide ACID transactions on data lakes
- **Compute engine**: [[apache-spark]] — high-performance distributed processing
- **Governance**: [[unity-catalog]] — centralized security and access control
- **Abstraction**: [[dbfs]] — cloud storage feels like a local filesystem

> A lakehouse represents a smart, adaptable library that combines the best of both worlds.

---
- Foundation for [[databricks-platform]] — Databricks is the leading commercial Lakehouse implementation
- Foundation for [[delta-lake]] — Delta Lake provides the transactional layer enabling Lakehouse
- Builds on [[apache-spark]] — Spark provides the compute engine for Lakehouse analytics
- Related to [[lambda-architecture]] — lakehouses reduce the need for separate batch/speed storage paths
- Related to [[kappa-architecture]] — unified lakehouse storage supports single-path streaming replay
- Related to [[snowflake-data-cloud]] — Snowflake is a proprietary lakehouse platform with separated storage/compute