---
title: "DataOps"
type: concept
tags: [data-engineering, devops, dbt, analytics, methodology]
created: 2026-06-08
updated: 2026-06-15
sources: [data-engineering-with-dbt]
aliases: [data-operations, data-devops]
---

## Summary

DataOps applies software engineering best practices — version control, automated testing, modularity, CI/CD — to data pipelines and transformations. It represents the shift from ad-hoc data wrangling to disciplined, collaborative data platform engineering, with dbt serving as the canonical transformation-layer catalyst.

## The Mindset Shift

| Old Way | DataOps Way |
|---|---|
| Data silos: engineers and analysts work separately | [[analytics-engineer|Analytics Engineer]] bridges both worlds |
| Business logic hidden in spreadsheets, stored procedures | Logic transparent in version-controlled SQL + YAML |
| Brittle pipelines, manual testing, tribal knowledge | Automated tests, documented lineage, reusable models |
| Reactive firefighting when dashboards break | Proactive quality gates catch issues before stakeholders see them |

> "Copy and paste kills your future self." — The DataOps philosophy: maintainability is the only success metric.

## Three Pillars of DataOps with dbt

| Pillar | Practice | Benefit |
|---|---|---|
| **Version Control** 📦 | Every model, test, and config in Git (PRs, code review) | Track changes, collaborate, roll back confidently |
| **Quality Assurance** 🧪 | Automated tests: `unique`, `not_null`, `relationships`, custom SQL tests | Catch data issues at the source, not in dashboards |
| **Modularity** 🧱 | Break monolithic scripts into reusable models + macros | Reduce technical debt, easier onboarding, faster iteration |

## The 3-Tier Modeling Journey

Zagni's Pragmatic Data Platform (PDP) framework ensures technical implementation aligns with business reality:

```
1. Conceptual Model → "What are the business entities?"
   (Customer, Order, Product, Revenue)

2. Logical Model → "How do they relate?"
   (Customer 1→N Orders, Order N→M Products)

3. Physical Model → "How to implement in the warehouse?"
   (dim_customers, fct_orders, bridge_order_products)
```

| Skip This | Consequence |
|---|---|
| Conceptual | Misalignment between tech and business → rework |
| Logical | Vague relationships → incorrect analytics |
| Jump straight to Physical | Technically correct model nobody understands or uses |

## Soft Boundaries in Cloud Warehousing

Cloud data platforms enable a fundamental reorganization:

| Old (On-Prem PostgreSQL) | New (Cloud + dbt) |
|---|---|
| Database = rigid "strong boundary" | Database/schema = flexible "soft folders" |
| Manual security, complex access management | dbt automation + hierarchical RBAC |
| Vertical scaling only | Horizontal scaling on-demand |

**Project structure reflects business domains**, not database constraints:
```
models/
├── staging/       # Raw → cleaned (soft boundary: staging schema)
├── intermediate/  # Business logic (soft boundary: intermediate schema)
└── marts/         # Business-ready (soft boundary: analytics schema)
    ├── finance/
    ├── marketing/
    └── product/
```

## The Modern Data Stack Ecosystem

dbt is the core of a larger ecosystem:
```
Ingestion (Fivetran, Airbyte) → Storage (Snowflake, BigQuery) → Transformation (dbt)
→ Orchestration (Airflow, Dagster) → BI (Looker, Metabase)
```

DataOps ensures each layer is versioned, tested, and maintainable.

---

- Formalized by [[dbt]] — dbt is the canonical tool that makes DataOps practical for SQL transformations
- Defines [[analytics-engineer]] — the role that practices DataOps daily
- Related to [[elt]] — DataOps governs the transformation (T) step with engineering discipline
- Related to [[data-ingestion]] — ingested data flows into DataOps-managed transformation pipelines
- Informs [[code-quality-pillars]] — DataOps applies the same modularity, testing, and reuse principles to data
- Operationalized by [[cicd-data-pipelines]] — CI/CD is the practical implementation of DataOps in the deployment pipeline (Ruff, SQLFluff, SQLMesh, Great Expectations)
- Related to [[data-engineering-fundamentals]] — DataOps applies software engineering rigor to the fundamental DE skills
- Benchmark source: [[sources/data-engineering-with-dbt]] — Roberto Zagni's 603-page guide
