---
title: "The Data Lakehouse — Bill Inmon, Ranjeet Srivastava & Mary Levins"
type: source
source_type: book
author: "Bill Inmon, Ranjeet Srivastava, Mary Levins"
url: ""
source_date: 2021
ingested: 2026-09-20
tags: [data-engineering, lakehouse, lineage, metadata, analytics]
concepts: [data-lakehouse, data-lineage, metadata-management, data-governance]
created: 2026-09-20
updated: 2026-09-20
---

## Summary

*The Data Lakehouse* (256 pages), by data-warehousing pioneer Bill Inmon with Ranjeet Srivastava and Mary Levins, frames the lakehouse as the convergence of the data lake and the data warehouse. The user's notes condense the book into four practical rules about how data types behave inside a lakehouse and what makes lakehouse analytics trustworthy.

## Key Takeaways

### 1. Text Storage in the Lakehouse
- **Avoid storing raw text in a data lakehouse unless explicitly required**
- Prefer storing text in a **structured database format** so it can be analyzed with standard analytical tools

### 2. Data Type Suitability
Different data types within a lakehouse support different kinds of analysis:

| Data Type | Best For |
| --- | --- |
| **Structured Data** | Known, predefined queries and analyses |
| **Other Unstructured Data** | Exploratory, unknown queries and analyses |
| **Textual Data** | **Both** known and unknown types of analytics |

### 3. Context for Calculated Values
A final calculated value is meaningless without context. To be useful you must know:
- **What** was calculated (the metric/definition)
- **What data** was used (the source inputs)
- **How** the calculation was performed (the method/formula)

### 4. Comprehensive Lineage
- Data lineage documentation is **essential** and must cover **every single step** in the data's journey
- Documenting only one or two steps is insufficient — **full end-to-end lineage** is required

## Connection to the Wiki

The book's architecture material builds directly on [[data-lakehouse]] (economics of a lake + governance of a warehouse). Its lineage mandate extends [[data-lineage]] and [[metadata-management]] (operational/lineage metadata), and the "context for calculated values" rule ties into [[data-governance]] and the metrics-definition work of the [[semantic-layer]] — a metric means nothing without its definition, inputs, and method.

---

- Extends [[data-lakehouse]] — the Inmon framing of lakehouse data types and storage rules
- Feeds [[data-lineage]] — every-step, end-to-end lineage as a hard requirement
- Supports [[metadata-management]] — lineage and definition metadata as the operating system of trust
- Informs [[data-governance]] — calculated values are meaningless without documented context
- Related to [[semantic-layer]] — metric definitions (what/how/inputs) standardize meaning
- Related to [[data-quality-engineering]] — context and lineage are prerequisites for data quality