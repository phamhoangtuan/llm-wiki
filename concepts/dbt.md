---
title: "dbt (data build tool)"
type: concept
tags: [dbt, data-engineering, analytics, elt, sql, data-modeling]
created: 2026-05-28
updated: 2026-05-28
sources: [unlocking-dbt-design-deploy-transformations]
aliases: [data-build-tool]
---

## Summary

**dbt** (data build tool) is an open-source data transformation framework that brings software engineering best practices to SQL. It handles the "T" in [[elt|ELT]] (Extract-Load-Transform) — running transformations inside your cloud data warehouse rather than on external servers. dbt compiles SQL + Jinja templates into executable queries, manages dependencies between models, and provides built-in testing and documentation generation.

## Core Identity

> dbt is not a database. Not an ETL tool. It's a **transformation framework** that applies version control, testing, and collaboration to SQL workflows.

dbt has **no compute engine of its own** — it sends compiled SQL to your data warehouse (Snowflake, BigQuery, Redshift, Databricks) for execution. This compute-neutral architecture means you leverage the warehouse's scale without moving data.

## Three Architectural Pillars

### 1. Compute-Neutral: Orchestrates, Doesn't Execute

```
[dbt project] --(compiled SQL)--> [Snowflake/BigQuery] --(results)--> [Tables/Views]
```

dbt manages the **lifecycle** of data transformations: compilation, dependency resolution, materialization, testing, and documentation — but all computation happens in the warehouse.

### 2. Declarative: Write SELECT, Not DDL

Traditional SQL requires imperative DDL/DML:

```sql
-- Traditional: you say HOW
CREATE TABLE analytics.customers AS
SELECT id, name, email FROM raw.users WHERE active = true;
```

With dbt, you write only SELECT — dbt handles the materialization:

```sql
-- dbt models/customers.sql: you say WHAT
SELECT id, name, email
FROM {{ ref('raw_users') }}
WHERE active = true
```

dbt automatically manages: `CREATE TABLE`, `CREATE VIEW`, `MERGE` (incremental), dependency ordering via `{{ ref() }}`.

### 3. Automated Object Management

- **Materializations**: table, view, incremental, ephemeral, materialized view
- **Dependencies**: `{{ ref('model') }}` builds a DAG; dbt runs models in correct order
- **Schema changes**: `on_schema_change` config handles column additions/removals

## 3-Tier Modeling Pattern

The recommended project structure follows a layered approach:

```
Raw Tables
  ↓
[stg_] Staging — Clean, rename columns, basic type casting
  ↓
[int_] Intermediate — Business logic, joins, aggregations
  ↓
[fct_/dim_] Marts — Business-ready fact and dimension tables for BI/ML
```

This modular design improves maintainability, allows reuse across projects, and makes testing targeted.

## Project Structure

```
my_dbt_project/
├── dbt_project.yml          # Project configuration
├── models/                  # Transform logic (the heart)
│   ├── staging/             # stg_ models: raw → cleaned
│   ├── intermediate/        # int_ models: business logic
│   └── marts/               # fct_/dim_ models: business-ready
├── seeds/                   # CSV lookup tables (mapping, config)
├── snapshots/               # SCD Type 2: track historical changes
├── tests/                   # Custom data quality tests
├── macros/                  # Reusable Jinja code blocks
├── analyses/                # Ad-hoc queries (not models)
└── dbt_packages/            # External dependencies (dbt hub)
```

## Built-in Testing

Data quality testing is a **first-class feature**, configured via YAML:

```yaml
# models/schema.yml
version: 2
models:
  - name: customers
    columns:
      - name: customer_id
        tests:
          - unique          # No duplicates
          - not_null        # No null values
      - name: email
        tests:
          - relationships:   # Foreign key validation
              to: ref('raw_users')
              field: user_id
```

- **Generic tests**: `unique`, `not_null`, `accepted_values`, `relationships`
- **Singular tests**: Custom SQL queries for complex assertions
- **Test execution**: `dbt test` runs all tests; integrable into CI/CD

## Auto-Generated Documentation

`dbt docs generate` produces a static website with:
- Model and column descriptions from YAML
- **Lineage graph** (DAG) showing dependencies visually
- Column-level metadata, test status, source table info

Documentation stays in sync with code — no more outdated wikis.

## dbt Core vs dbt Cloud

| Aspect | dbt Core (OSS) | dbt Cloud (Managed) |
|---|---|---|
| Cost | Free | Per-user/month |
| Deployment | CLI, self-managed infra | Browser IDE, auto-scheduling |
| Adapters | Broadest (community + vendor) | Official only |
| Scheduling | Manual / external (Airflow) | Built-in job scheduler |
| Best for | Teams with DevOps capacity | Teams wanting reduced ops |

> Start with Core to learn fundamentals. Move to Cloud when you need collaboration, scheduling, or want to reduce operational overhead.

## Platform Support

dbt uses an **adapter** plugin system:

| Tier | Examples |
|---|---|
| dbt Labs supported | Snowflake, BigQuery, Redshift, Postgres, Spark |
| Vendor supported | Databricks, Oracle, ClickHouse, Teradata |
| Community supported | MySQL, SQL Server, [[duckdb|DuckDB]], SQLite |
| Custom | Any SQL engine via custom adapter |

If your platform "speaks SQL", there's almost certainly a dbt adapter.

## When to Use dbt

| ✅ Use dbt | ❌ Don't Use dbt |
|---|---|
| Data transformations in cloud warehouses | Data extraction/loading (use Fivetran, Airbyte) |
| Applying software engineering to SQL | Pipeline orchestration (use Airflow, Dagster — or pair with dbt) |
| Building tested, documented data models | Real-time streaming transforms (use [[apache-flink|Flink]], Spark Streaming) |
| Teams with SQL skills wanting version control | No-code/low-code workflows |

## Key Skills for dbt

| Skill | Importance (1-5) |
|---|---|
| SQL (SELECT, CTEs, window functions) | 4 |
| Jinja templating | 2 |
| YAML configuration | 2 |
| Git / version control | 2 |
| Data modeling (dimensional, Data Vault) | 1-4 (role-dependent) |
| Python (custom macros, hooks) | 1 |
---
- Implements [[elt]] — dbt is the canonical "T" (Transform) tool in the ELT paradigm
- Defines [[analytics-engineer]] — dbt formalized the Analytics Engineer role in data teams
- Related to [[data-ingestion]] — dbt handles the transform step; ingestion tools handle extract/load
- Related to [[materialized-views]] — dbt supports materialized views as a materialization strategy
- Integrates with [[duckdb]] — DuckDB has a community dbt adapter for local development
- Benchmark source: [[unlocking-dbt-design-deploy-transformations]] — Cameron Cyr & Dustin Dorsey's 351-page guide
