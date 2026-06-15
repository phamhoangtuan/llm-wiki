---
title: "Seriously Good Software"
type: source
source_type: book
author: "Marco Faella"
source_date: 2020-01-01
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-15
url: ""
tags: [design-principles, architecture, engineering, optimization]
concepts: [software-quality-dimensions]
---

## Summary

A 330-page exploration of software quality as a multi-dimensional optimization problem. Introduces the 2D quality spectrum (Internal/External × Functional/Non-functional), formalizes four core trade-offs (Time/Space, Efficiency/Readability, Robustness/Efficiency, Dev Time/Quality), and demonstrates these concepts through a case study of a water container system with multiple implementations at different quality points.

## Core Message

> There is no "perfect" implementation in a vacuum. Every line of code is a trade-off. The best code is the one optimized correctly for the specific context — balancing machine performance against developer sanity.

## Key Takeaways

1. **2D Quality Spectrum**: Quality isn't binary — it spans Internal/External and Functional/Non-functional axes
2. **No "Internal Functional"**: If software "does something," its effects are ultimately visible to users
3. **Four Trade-offs**: Time vs Space, Efficiency vs Readability, Robustness vs Efficiency, Development Time vs Quality
4. **YAGNI**: Don't add features or store data "just in case" — every unnecessary field is technical debt from birth
5. **Analyzability > Readability**: Code must be analyzable for maintenance — meaningful naming is rule #1
6. **Abstractions have costs**: A `HashSet` in a JVM costs ~108 bytes per object. Calculate memory footprints at scale.
7. **Context is King**: The right implementation depends on whether you prioritize machine speed or developer sanity

## Companion Concept

→ [[software-quality-dimensions]]
