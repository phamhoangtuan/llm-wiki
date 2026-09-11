---
title: "Data Modeling"
type: concept
tags: [data-engineering, data-modeling, sql, database-design]
created: 2026-06-15
updated: 2026-06-15
sources: [data-fundamentals-matter-2026, data-engineering-handbook]
aliases: [data-modelling, dimensional-modeling]
---

## Summary

**Data Modeling** is the practice of designing the structure, relationships, and constraints of data within a storage system. It determines whether queries are fast or impossible, whether analytics are accurate or misleading, and whether data systems are maintainable or a tangled mess. In the 2026 AI era, data modeling remains one of the most critical and enduring [[data-engineering-fundamentals|data engineering fundamentals]] — AI can suggest schemas but cannot understand business semantics.

## Why Data Modeling Matters

- **Query performance**: A well-modeled schema can be 100x faster than a poorly modeled one
- **Business accuracy**: Models encode business rules and semantics — without them, "revenue" means different things to different teams
- **Maintainability**: Good models evolve gracefully as requirements change; bad models require rewrites
- **AI consumption**: AI agents querying data need clean, well-modeled structures — raw, unmodeled data drives token costs through the roof

## Key Approaches

| Approach | Description | Use Case |
|---|---|---|
| **Dimensional Modeling** | Star/snowflake schemas with fact and dimension tables | Analytics, BI, data warehouses |
| **Normalized Modeling** | 3NF/BCNF — minimal redundancy, maximum integrity | OLTP systems, operational data stores |
| **Data Vault** | Hub-Link-Satellite pattern for auditable, scalable integration | Enterprise data warehouses with many sources |
| **Wide Tables / One Big Table** | Denormalized for query speed | Analytics on columnar stores, ML feature stores |

## The Schema-on-Read Trap

The idea of "skip modeling and let AI figure it out later" (schema on read) was tried in 2010 and failed. It produces inconsistent results, explodes token costs, and guarantees that no two queries agree on what "customer" means. Modeling upfront is an investment that compounds.

---

- Core component of [[data-engineering-fundamentals]] — alongside SQL and Python, data modeling is one of the three enduring DE skills
- Practiced by [[analytics-engineer|Analytics Engineers]] — they own the transformation layer where dimensional models are built
- Implemented via [[dbt]] — dbt models are the physical realization of data modeling decisions
- Related to [[data-governance]] — data models encode governance rules (naming conventions, entity definitions)
- Benchmark source: [[sources/data-fundamentals-matter-2026]] — SeattleDataGuy on fundamentals
- Benchmark source: [[sources/data-engineering-handbook]] — DE Handbook discipline overview
