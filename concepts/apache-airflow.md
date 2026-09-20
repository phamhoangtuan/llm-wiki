---
title: "Apache Airflow"
type: concept
tags: [data-engineering, orchestration, workflow, python, dag]
created: 2026-07-11
updated: 2026-07-11
sources: [data-engineering-with-python]
aliases: [airflow, workflow-orchestration]
---

## Summary

**Apache Airflow** is an open-source platform for programmatically authoring, scheduling, and monitoring data pipelines. It represents workflows as **Directed Acyclic Graphs (DAGs)** written in Python, enabling data engineers to define complex task dependencies, retry logic, and monitoring in code rather than through GUI configurations.

## Core Concepts

| Concept | Description |
|---------|-------------|
| **DAG** | Directed Acyclic Graph — a collection of tasks with explicit dependencies and no cycles |
| **Task** | A unit of work (e.g., run a SQL query, execute a Python script, transfer a file) |
| **Operator** | A template for a task type (e.g., `PythonOperator`, `BashOperator`, `SnowflakeOperator`) |
| **Scheduler** | Parses DAGs, determines execution order, and triggers tasks based on schedule |
| **Executor** | Runs the tasks (e.g., LocalExecutor, CeleryExecutor, KubernetesExecutor) |
| **Web UI** | Visualizes DAG runs, task status, logs, and historical performance |

## Why Airflow Became Standard

1. **Python-native** — pipelines are code, not XML or YAML; integrates with pandas, SQLAlchemy, boto3
2. **Dependency as code** — `task_a >> task_b >> task_c` explicitly encodes execution order
3. **Backfill and catchup** — automatically run missed schedules when a DAG is paused and resumed
4. **Extensible** — 500+ community operators for databases, cloud services, ML platforms
5. **Observability** — built-in logging, SLA alerting, and retry with exponential backoff

## Example DAG

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def extract(): ...
def transform(): ...
def load(): ...

with DAG('etl_pipeline', start_date=datetime(2024, 1, 1), schedule='@daily') as dag:
    extract_task = PythonOperator(task_id='extract', python_callable=extract)
    transform_task = PythonOperator(task_id='transform', python_callable=transform)
    load_task = PythonOperator(task_id='load', python_callable=load)

    extract_task >> transform_task >> load_task
```

## Alternatives and When to Choose Them

| Tool | Strength | Best For |
|------|----------|----------|
| **Airflow** | Mature, Python-native, vast operator library | General data pipelines, ETL/ELT |
| **Prefect** | Modern API, hybrid cloud/on-prem | Teams wanting simpler local development |
| **Dagster** | Asset-oriented, strong testing | Data-aware pipelines with unit testing |
| **Luigi** | Lightweight, Spotify origin | Simple dependency graphs |
| **Temporal** | Durable execution, long-running | Business process workflows, microservice orchestration |

## Key Takeaways

1. Airflow is the de facto standard for data pipeline orchestration in Python ecosystems.
2. DAGs-as-code make pipelines versionable, testable, and reviewable.
3. Backfill, retry, and SLA monitoring are built-in production features.
4. For modern stacks, evaluate Dagster (asset-centric) and Prefect (simpler API) as alternatives.

---

- Core tool for [[data-engineer]] — orchestration is one of the four pillars of data engineering
- Expands [[dataops]] — Airflow embodies the DataOps principle of treating pipelines as software
- Related to [[cicd-data-pipelines]] — DAGs should be linted, tested, and deployed via CI/CD
- Related to [[apache-spark]] — Spark jobs are commonly triggered from Airflow DAGs
- Related to [[elt]] — Airflow orchestrates the extraction and load steps; dbt handles transformation
- Related to [[dbt]] — dbt + Airflow is the canonical modern data stack combination
- Benchmark source: [[sources/data-engineering-with-python]] — Crickard's guide covers Airflow DAG construction
