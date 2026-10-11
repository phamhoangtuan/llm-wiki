---
title: "Query Optimization"
type: concept
tags: [data-engineering, query-optimization, sql, performance, data-warehouse]
created: 2026-10-11
updated: 2026-10-11
sources: [financial-data-engineering-khraisha, data-pipelines-pocket-reference-densmore]
aliases: [sql optimization, query performance, column pruning]
---

## Summary

**Query Optimization** is the practice of writing analytical queries that minimize compute cost and latency — by fetching less data, doing heavy work as late as possible, and structuring queries for the query planner. In financial-scale data engineering, Tamer Khraisha's rules are stark: replacing `SELECT *` with explicit columns can cut latency **30–70%**, and modularizing queries with CTEs/filter-before-join ordering makes cost drop exponentially as datasets grow (source: [[sources/financial-data-engineering-khraisha]]).

## Core Techniques

### 1. Fetch Only What You Need
- **Query only essential columns** — replace `SELECT *` with explicit fields (30–70% latency reduction)
- Push the same pruning into ingestion: standardize what lands in the warehouse

### 2. Order Operations for the Query Planner
- **Filter before joins/aggregations** — reduce dataset size as early as possible
- **Minimize dataset size early** — the biggest lever is how much data enters each stage
- **Delay expensive operations** — aggregations, window functions, and heavy joins last

### 3. Modularize & Simplify
- **Break complex logic into CTEs/temp tables** — one step per transformation, readable and debuggable
- **Avoid N+1 queries** — batch work; never loop-query per row/key
- **Choose simplicity over cleverness** — maintainable SQL outperforms opaque "smart" SQL over time (source: [[sources/data-pipelines-pocket-reference-densmore]])

## Why It Matters

| Practice | Impact |
| --- | --- |
| Column pruning | 30–70% latency cut; exponentially lower compute at scale |
| Filter-before-join | Massive reduction in join input size |
| Readable modular queries | Faster debugging, better governance of what runs |

Query optimization is the execution-side complement of [[data-lineage]] and [[semantic-layer]]: lean queries are also *auditable* queries — explicit columns and CTEs document exactly what a metric consumed (the "what data was used" of the context triad).

---

- Core to [[data-engineering-fundamentals]] — lean SQL is a foundational DE skill
- Extends [[data-quality-monitoring]] — column pruning supports validated, explicit schemas
- Complements [[semantic-layer]] — explicit queries reveal what metrics consumed
- Related to [[data-lineage]] — lean, explicit queries are traceable queries
- Related to [[vectorized-execution]] — engines push pruning down; queries should cooperate
- Related to [[materialized-views]] — precomputed results eliminate repeated expensive work
- Related to [[dataops]] — simplicity over cleverness is a DataOps principle
- Benchmark source: [[sources/financial-data-engineering-khraisha]] — Khraisha's financial-scale query rules
- Benchmark source: [[sources/data-pipelines-pocket-reference-densmore]] — Densmore's simplicity principle