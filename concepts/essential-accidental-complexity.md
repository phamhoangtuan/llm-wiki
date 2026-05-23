---
title: "Essential vs Accidental Complexity"
type: concept
tags: [architecture, complexity, design-principles]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
aliases: [essential complexity, accidental complexity, Fred Brooks]
---

## Summary

Fred Brooks distinguished two types of complexity in software. Understanding the difference is critical for knowing what to accept and what to eliminate.

## Two Types of Complexity

| Type | Definition | Example | Can Eliminate? |
|---|---|---|---|
| **Essential** | Inherent complexity of the real-world problem | Physics of landing a rover on Mars | ❌ No — must manage |
| **Accidental** | Complexity introduced by bad design/implementation | Mutable Date auto-correcting Nov 31 → Dec 1 | ✅ Yes — better design |

## Key Insight

Most codebase complexity is **accidental**, not essential. Good design eliminates accidental complexity so you can focus on the essential complexity of the domain.

## Sources of Accidental Complexity

- Mutable state that silently corrupts data
- Anemic domain models with logic scattered everywhere
- Implicit type conversions that hide semantic errors
- Poor naming that obscures intent
- Tight coupling that makes changes ripple

## Connections

- Managed by [[immutability]] — eliminates accidental complexity from mutable state
- Reduced by [[rich-domain-model]] — eliminates scattered logic
- Prevented by [[fail-fast]] — catches errors before they create accidental complexity
- Related to [[bijection]] — bijection violations create accidental complexity
