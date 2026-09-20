---
title: "Data Lineage"
type: concept
tags: [data-engineering, metadata, governance, lineage, data-quality]
created: 2026-09-20
updated: 2026-09-20
sources: [the-data-lakehouse-inmon]
aliases: [end-to-end lineage, data provenance, lineage tracking]
---

## Summary

**Data Lineage** is the documentation of where data came from and how it was transformed at every step of its journey — the traceability that makes analytical outputs trustworthy. Inmon's *The Data Lakehouse* states the requirement bluntly: lineage must cover **every single step**; documenting only one or two steps is insufficient (source: [[sources/the-data-lakehouse-inmon]]).

## The Every-Step Rule

- Lineage documentation must be **comprehensive and end-to-end** — from raw source through every transformation to the final consumer
- Partial lineage (field-level, pipeline-level, or dashboard-level alone) creates blind spots that silently invalidate downstream analysis
- Full lineage is what lets an analyst answer: *where did this number actually come from?*

## Context for Calculated Values

A final calculated value is meaningless without its **context triad**:

| Aspect | Question |
| --- | --- |
| **What** | What was calculated (the metric / definition)? |
| **Data** | What data was used (the source inputs)? |
| **How** | How was the calculation performed (the method / formula)? |

This is the lineage of *meaning* rather than just the lineage of *movement* — it connects metrics back to definitions (see [[semantic-layer]]).

## Why It Matters

- **Trust**: analysts make decisions on data they can verify (governance pillar)
- **Debugging**: when a number is wrong, end-to-end lineage locates the broken step
- **Compliance**: regulators (and quality standards) require traceability of sensitive data
- **Quality**: data quality work presupposes knowing which step produced the defect

---

- Core to [[metadata-management]] — lineage metadata is the operating system of data descriptions
- Required by [[data-governance]] — the lineage & metadata pillar of the governance framework
- Informs [[data-lakehouse]] — full lineage as a prerequisite for lakehouse analytics trust
- Related to [[semantic-layer]] — metric definitions give calculated values their context
- Related to [[data-quality-engineering]] — lineage locates where quality defects arise
- Related to [[data-observability]] — lineage is the "where did this come from" channel
- Benchmark source: [[sources/the-data-lakehouse-inmon]] — Inmon's every-step lineage requirement