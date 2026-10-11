---
title: "Data Product"
type: concept
tags: [dataops, data-engineering, product-thinking, data-mesh]
created: 2026-07-14
updated: 2026-07-14
sources: [practical-dataops]
aliases: [data-as-product, analytics-product]
---

## Summary

A **Data Product** is the output of treating data not as a one-off project deliverable but as a continuously produced, monitored, and iteratively improved asset — analogous to a software product. This is the core goal of [[dataops|DataOps]]: moving from "bespoke hand-crafted" data science to a high-velocity, factory-like operation (source: [[sources/practical-dataops]]).

## Project vs Product

| Aspect | Data Project | Data Product |
| -------- | ------------- | -------------- |
| **Lifetime** | Finite — ends at delivery | Continuous — runs in production |
| **Ownership** | Project team disbands after completion | Cross-functional team maintains and improves |
| **Quality** | Tested once before handoff | Monitored continuously with alerts |
| **Improvement** | Fixed scope; change = new project | Iterative based on user feedback and experimentation |
| **User trust** | "Here's the report" | "The dashboard is always accurate" |

## Characteristics of a Data Product

1. **In continuous production** — not a one-time analysis or static dashboard
2. **Monitored and measured** — SLIs/SLOs for freshness, accuracy, uptime
3. **Self-service** — users can discover, access, and trust it without gatekeepers
4. **Versioned and governed** — schema changes are managed, not breaking
5. **Iteratively improved** — feedback drives the backlog, not a frozen requirements doc

## The DataOps Factory

The "factory" metaphor means:

- **Standardized inputs** — data sources with known schemas, SLAs
- **Automated pipelines** — no manual CSV exports, no email attachments
- **Quality gates** — automated testing at each stage (like CI/CD for software)
- **Repeatable outcomes** — same input → same output, no "it worked on my machine"

## Minimum Viable Data Product

Start with a **single thin slice** — an end-to-end delivery of one data product — to prove value before scaling. Choose a high-value use case with a supportive stakeholder. Learn, then expand.

---

- Core to [[dataops]] — the product mindset is what distinguishes DataOps from ad-hoc data work
- Related to [[data-quality-monitoring]] — continuous monitoring is a prerequisite for treating data as a product
- Related to [[data-governance]] — governed data products build user trust
- Related to [[semantic-layer]] — the semantic layer makes data products discoverable and consistent
- Benchmark source: [[sources/practical-dataops]] — Atwal on the DataOps factory
