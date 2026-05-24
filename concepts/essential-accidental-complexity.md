---
title: "Essential vs Accidental Complexity"
type: concept
tags: [architecture, complexity, design-principles]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
---

## Summary

Fred Brooks distinguished two types of complexity in software. Understanding the difference is critical for knowing what to accept and what to eliminate.

## Two Types of Complexity

| Type | Definition | Example | Can Eliminate? |
| --- | --- | --- | --- |
| **Essential** | Inherent complexity of the real-world problem | Physics of landing a rover on Mars | ❌ No — must manage |
| **Accidental** | Complexity introduced by bad design/implementation | Mutable Date auto-correcting Nov 31 → Dec 1 | ✅ Yes — better design |
---
- Managed by [[immutability]] — eliminates accidental complexity from mutable state
- Reduced by [[rich-domain-model]] — eliminates scattered logic
- Related to [[bijection]] — bijection violations create accidental complexity
