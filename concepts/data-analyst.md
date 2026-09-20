---
title: "Data Analyst"
type: concept
tags: [data-analytics, roles, career, bi, sql, ai]
created: 2026-06-27
updated: 2026-06-27
sources: [how-ai-changes-4-core-data-roles]
aliases: [da, business-analyst]
---

## Summary

A **Data Analyst** works closely with business stakeholders to define metrics and dimensions, creating dashboards, reports, and ad-hoc queries to answer business questions. They typically focus on a specific domain — product, growth, finance, or marketing — and their superpower is **making the most of available data to get insights fast**.

## Role Positioning

| Role | Focus | Primary Tools |
|---|---|---|
| **Data Engineer** | Infrastructure, pipeline orchestration | Airflow, Kafka, Python |
| **Analytics Engineer** | Transformation layer, data modeling | dbt, SQL, Git |
| **Data Analyst** ✅ | Business insights, reporting, ad-hoc analysis | Looker, Tableau, Power BI, Excel, SQL |
| **Data Scientist** | Predictive models, ML, statistical patterns | Python, R, ScikitLearn |

Data analysts don't build pipelines or manage infrastructure — they work with the data already available to them. They are the closest data role to business stakeholders.

## Core Skills

| Skill | Importance | Role in Daily Work |
|---|---|---|
| **SQL** | 5/5 | Primary language for ad-hoc queries and data exploration |
| **Excel** | 4/5 | Quick analysis, pivot tables, stakeholder-friendly output |
| **BI Tools** (Looker, Tableau, Power BI) | 4/5 | Dashboard creation, visualization, self-service enablement |
| **A/B Testing** | 3/5 | Experimentation design and statistical interpretation |
| **Statistics** | 3/5 | Understanding significance, distributions, correlation |

## How AI Is Changing the Role

The data analyst role faces the **biggest disruption** from AI among all data roles (source: [[sources/how-ai-changes-4-core-data-roles]]):

1. **Dashboards becoming dataset sources**: Stakeholders increasingly use dashboards to download filtered datasets that they feed directly to Claude/AI. *How data is displayed* and *how metrics are calculated* matter less than having a clean dataset.

2. **Self-service analytics threat**: AI-powered self-service tools can answer business questions without analyst intermediaries. The role shifts from *answering questions* to *building the clean models that AI queries*.

3. **Data modeling becomes essential**: Analysts must learn [[data-modeling]] — the core skill of [[analytics-engineer|analytics engineering]] — to remain valuable. Building clean, documented, governed data models is the new analyst superpower.

4. **Upskilling imperative**: Without learning dbt and data modeling, analysts risk being replaced by [[self-service-analytics]]. The path forward is analyst-to-analytics-engineer.

## Analyst vs Analytics Engineer

| Capability | Data Analyst | Analytics Engineer |
|---|---|---|
| Dashboard creation | Primary focus | Secondary |
| Data modeling | Limited | Primary focus |
| SQL complexity | Moderate (queries) | High (CTEs, window functions, modular models) |
| Business proximity | Very high | Medium-high |
| Technical depth | Moderate | High |
| Pipeline ownership | None | Transformation layer |

---

- Complements [[analytics-engineer]] — Analytics Engineers build the models Analysts query; the boundary is blurring
- Informed by [[data-modeling]] — the critical upskill for analysts in the AI era
- Consumed by [[self-service-analytics]] — the AI-powered trend that analysts must adapt to or be replaced by
- Related to [[data-engineer]] — Analysts consume the infrastructure DEs build
- Benchmark source: [[sources/how-ai-changes-4-core-data-roles]] — Madison Mae on AI's impact on data roles
