---
title: "Delta Live Tables (DLT)"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [data-engineering, databricks, etl, data-quality]
sources: [big-book-data-engineering]
---

# Delta Live Tables (DLT)

Declarative ETL framework on Databricks that lets you define *what* data transformations to perform, not *how* to execute them. DLT automatically handles cluster management, monitoring, and data quality enforcement.

## Declarative vs. Imperative

Traditional ETL requires specifying execution details (cluster size, retry logic, error handling). DLT flips this: declare the desired state of your data, and the framework handles execution.

## DLT Expectations (Data Quality Guardrails)

Expectations are declarative quality rules applied at each pipeline step:

```sql
-- Example: Silver layer must have valid customer IDs
CONSTRAINT valid_customer_id EXPECT (customer_id IS NOT NULL)
```

When violated, DLT can: warn and continue, drop invalid rows, or halt the pipeline — configurable per rule.

## How DLT Fits Medallion

DLT is purpose-built for [[medallion-architecture]]:

- **Bronze → Silver**: Clean, deduplicate, enforce basic constraints
- **Silver → Gold**: Aggregate, join, produce business-ready tables

Each transition is a DLT pipeline stage with its own expectations.

## Key Benefits

- **No infrastructure management**: DLT provisions and scales clusters automatically
- **Incremental processing**: Only processes new/changed data
- **Built-in monitoring**: Visual pipeline DAG, data quality metrics
- **Auto-retry**: Failed pipeline steps retry automatically

---

- Implements [[medallion-architecture]] — declarative Bronze → Silver → Gold pipelines
- Runs on [[databricks-platform]] — native to Databricks Data Intelligence Platform
- Uses [[delta-lake]] — underlying storage with ACID, time travel
- Quality-gated by [[data-quality-monitoring]] — expectations as automated guardrails
