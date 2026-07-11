---
title: "Data Engineering with Python"
type: source
source_type: book
author: "Paul Crickard"
url: ""
source_date: ""
ingested: 2026-07-11
tags: [data-engineering, python, etl, airflow, spark, postgres, elasticsearch, great-expectations]
concepts: [data-engineer, data-engineering-fundamentals, python-professional-practices, apache-airflow, apache-spark, data-quality-monitoring, database-isolation, dataops]
---

# Data Engineering with Python

**Author:** Paul Crickard  
**Type:** Ebook (299 pages)  
**Finished:** 2026-04-22  
**Ingested:** 2026-07-11

---

## Core Thesis

Data Engineering is the art of building, operating, and maintaining data infrastructure — pipelines, databases, and platforms — that transform raw data into production-quality information accessible to end users.

> If data is water, the data engineer designs the pipes, filtration plants, and reservoirs to ensure clean water flows to the right place at the right time.

## Python as the Lingua Franca

| Reason | Explanation | Example |
|--------|-------------|---------|
| **Ecosystem** | Thousands of libraries for every data task | pandas for manipulation, SQLAlchemy for databases |
| **Community** | Large community, abundant documentation | "pandas merge" → millions of search results instantly |
| **Cross-platform** | Runs on Windows, Mac, Linux, cloud, containers | Write once, deploy anywhere |
| **Readability** | Syntax close to English, low cognitive load | `df[df['age'] > 30].groupby('city').mean()` reads like a sentence |

## Essential Python Tooling

### Data Manipulation & Analysis

- **pandas** — Read from CSV, JSON, SQL; transform with chainable operations; group, aggregate, filter.

### Scientific & Machine Learning

| Library | Purpose | Use Case |
|---------|---------|----------|
| numpy | High-performance multi-dimensional array computation | Large-scale numeric preprocessing |
| scipy | Scientific algorithms: optimization, statistics | A/B testing, statistical modeling |
| scikit-learn | Classical machine learning | Classification, regression, clustering |
| tensorflow/pytorch | Deep learning | NLP, computer vision, recommendations |

### File & API Handling

- **json, csv, requests** — Standard library modules for API calls and file I/O.

## Building Data Pipelines with Python Frameworks

### Apache Airflow: Pure Python Orchestrator

- **Concept:** Directed Acyclic Graphs (DAGs) describe tasks and dependencies as code.
- **When to use:** Schedule, monitor, and retry complex jobs.
- Pattern: `extract_task >> transform_task >> load_task`

### Apache Spark (PySpark): Distributed Big Data Processing

- **Concept:** Distributed computing — split data, process in parallel across a cluster.
- **When to use:** Datasets too large for single-machine processing (TB/PB scale).

### Apache NiFi + Jython: GUI-Based with Custom Logic

- **Concept:** Drag-and-drop data flow design with Jython (Python on JVM) for custom processors.
- **When to use:** Teams need visual pipeline design but want Python flexibility for complex logic.

## Database Interaction

### Relational (PostgreSQL Example)

- **psycopg2** — Connect, execute SQL, bulk insert with `execute_batch` for high performance.

### NoSQL (Elasticsearch Example)

- **elasticsearch** Python client — Index documents, bulk indexing, query with DSL.

## Production-Ready Data Engineering Principles

### 1. Idempotent

Rerunning a pipeline must produce the same outcome without duplicating records.

- Bad: Always `INSERT` new rows → duplicates on retry.
- Good: `UPSERT` (`INSERT ... ON CONFLICT`) → same result every time.

### 2. Atomic

If part of a transaction fails, the entire operation rolls back to avoid partial/dirty data.

- Use database transactions and context managers.

### 3. Validated

Ensure data quality before production via rules and automated checks.

- **Great Expectations** — Python library for human-readable data validation rules.
  - `expect_column_values_to_not_be_null('order_id')`
  - `expect_column_values_to_be_between('amount', 0, 10000)`
  - `expect_column_values_to_match_regex('email', r'^[\w\.-]+@[\w\.-]+\.\w+$')`

## Key Takeaways

1. Python is the default language thanks to its rich ecosystem, readability, and cross-platform support.
2. Pipelines are the heart of data engineering — choose the right framework (Airflow, Spark, NiFi) for the problem.
3. Database interaction requires specialized libraries (psycopg2, elasticsearch) for performance and reliability.
4. Clearly separate roles: Engineer builds the foundation; Scientist extracts insights — tight collaboration required.
5. Production-ready code must be **Idempotent + Atomic + Validated** — no exceptions.
6. Great Expectations is essential for automating data quality checks.

---

- Expands [[data-engineer]] — the role and responsibilities of building data infrastructure with Python
- Expands [[data-engineering-fundamentals]] — Python, SQL, and pipeline patterns as enduring DE skills
- Expands [[python-professional-practices]] — production-grade Python for data pipelines
- Foundation for [[apache-airflow]] — Python-native DAG orchestrator for complex workflows
- Expands [[apache-spark]] — PySpark for distributed big data processing in Python
- Expands [[data-quality-monitoring]] — Great Expectations as a Python data validation tool
- Expands [[database-isolation]] — atomic transactions as a production pipeline principle
- Expands [[dataops]] — applying software engineering practices (CI/CD, testing) to Python pipelines
