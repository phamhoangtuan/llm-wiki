---
title: "Semantic Layer"
type: concept
tags: [data-engineering, analytics, ai, dbt, metrics]
created: 2026-06-08
updated: 2026-06-08
sources: [semantic-layers-for-ai]
aliases: [context-layer, metrics-layer, semantic-context]
---

## Summary

A semantic layer is a unified context layer that standardizes metric definitions, business logic, and data relationships across an organization's data stack. Originally built for human stakeholders (who largely ignored it), the semantic layer has found a new and critical user: **AI agents**. Without a semantic layer, AI agents guess metric definitions inconsistently — pulling from scattered sources across dbt, BI tools, documentation, and tribal knowledge.

## Why AI Changes Everything

| Old World (for humans) | New World (for AI agents) |
|---|---|
| Built for stakeholders who promised to use it | Built for AI agents that **must** use it to function |
| High effort, low actual adoption | High effort, but adoption is guaranteed — AI can't work without it |
| Standardized metrics for dashboards | Standardized context for accurate SQL generation and business answers |

> **Anthropic's benchmark**: 95% accuracy on self-service analytics by combining strong data foundations + sources of truth (semantic layer) + validation.

## What a Semantic Layer Unifies

| Source | Context Provided |
|---|---|
| **dbt models** | Data lineage, model definitions, column descriptions, tests |
| **BI tools** (Looker, Tableau) | Metric definitions — the "official" business logic |
| **Query history** | Which tables are joined, common filters, query patterns |
| **Documentation** (Notion, Confluence) | Business context, feature specs, process docs |
| **Communication** (Slack, Teams) | Tribal knowledge, historical decisions, edge cases |

**Without unification**: AI sees fragmented information and guesses. **With unification**: AI has a single source of truth for what a metric means and how to compute it.

## The Gap: dbt Alone Is Not Enough

dbt documents models and columns, but critical context lives elsewhere:
- **Query patterns**: Two models frequently joined in BI, but no join context in dbt — the AI needs to know `fact_sessions` JOINs `dim_commerce_type` on `commerce_id`
- **Common filters**: Everyone filters by `commerce_type = 'web'` for web sessions, but this isn't in dbt docs
- **Business rationale**: A Notion doc explains *why* a feature exists and how it should be measured — dbt has the *how* but not the *why*

## The Semantic Layer Stack

Current tools in the space:

| Tool | Approach |
|---|---|
| **dbt Semantic Layer** | YAML-defined metrics, compiles to SQL — powerful but high-friction |
| **Snowflake Semantic Views** | Low-lift, warehouse-native — but doesn't incorporate BI definitions |
| **Cube** | YAML-based, mature — but restricted to YAML files |
| **ktx** (open-source) | Pulls context from dbt, query history, Notion, Slack, BI tools — Git-versioned |

> The next generation of semantic layers doesn't just define metrics in YAML — it **gathers** context from where the business already lives.

---

- Related to [[dbt]] — dbt provides the data models and docs that feed the semantic layer
- Informs [[analytics-engineer]] — Analytics Engineers are the natural builders and maintainers of semantic layers
- Enables [[dataops]] — semantic layers are a DataOps practice: version-controlled, testable, CI/CD-ready context
- Related to [[harness-engineering]] — semantic layers are the "source of truth" harness that AI agents need for reliable answers
- Benchmark source: [[sources/semantic-layers-for-ai]] — Madison Mae on why semantic layers are now for AI
