---
title: "Data Engineering with dbt"
type: source
source_type: book
author: "Roberto Zagni"
source_date: 2023-01-01
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-08
url: ""
tags: [dbt, data-engineering, analytics, elt, dataops]
concepts: [dataops, dbt, analytics-engineer]
---

## Summary

A 603-page deep dive into dbt as the core of the Modern Data Stack. Goes beyond tool tutorials to cover the strategic transformation from siloed data operations to collaborative DataOps: the analytics engineer role, Jinja-powered declarative SQL, the 3-tier modeling journey (Conceptual → Logical → Physical), soft boundaries in cloud warehousing, and the pragmatic path to production-grade data platforms.

## Core Message

> dbt is not just a tool — it's a mindset shift: transforming data engineering into software engineering, analysts into analytics engineers, and data pipelines into trusted information refineries.

## Key Takeaways

1. **Analytics Engineer is the keystone role**: Bridge between data plumbing and business storytelling; owns the transformation layer
2. **SQL + Jinja = Superpower**: Declarative logic describes "what"; dbt handles "how" — DRY macros, `ref()` for DAGs
3. **DataOps is mandatory**: Version control + automated testing + modularity = maintainable, scalable data platforms
4. **Soft boundaries > Strong boundaries**: Cloud warehouse + dbt enables flexible data organization without rigid database constraints
5. **Modeling is a 3-tier journey**: Conceptual → Logical → Physical ensures technical implementation aligns with business goals
6. **"Copy and paste kills your future self"**: Maintainability is the only success metric — don't trade short-term speed for long-term technical debt

## Companion Concepts

→ [[dataops]] — the DataOps practice framework
→ [[dbt|dbt]] — the tool itself
→ [[analytics-engineer]] — the role dbt enables
