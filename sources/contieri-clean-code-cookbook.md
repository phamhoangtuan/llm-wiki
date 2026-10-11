---
title: "Clean Code Cookbook (Maximiliano Contieri)"
type: source
tags: [clean-code, architecture, design-principles, oop]
created: 2026-05-24
updated: 2026-06-15
author: "Maximiliano Contieri"
source_type: book
source_date: 2026-05-18
ingested: 2026-05-23
url: ""
concepts: [software-as-simulation, mapper-principles, bijection, rich-domain-model, tell-dont-ask, immutability, fail-fast, technological-centaur, readability-vs-performance]
---

## Summary

Personal notes on **Clean Code Cookbook** by Maximiliano Contieri — a 374-page book that reframes software as a "simulator of reality." The core thesis: code must faithfully mirror the real-world domain it serves, and when it stops doing so, it becomes fragile, incomprehensible, and dangerous.

## Key Takeaways

- **Software = Simulation**: Code is not a list of commands for a computer — it's a theory/model of how the real world works
- **MAPPER**: 6 principles defining the simulation philosophy — Model, Abstract, Partial, Programmable, Explaining, Reality
- **Bijection**: The one-and-only design principle — 1 real-world entity ↔ 1 code object. Violations led to the $125M Mars Climate Orbiter disaster
- **Rich > Anemic**: Objects must encapsulate both data and behavior. "Tell, Don't Ask" protects encapsulation
- **Immutability of essence**: Essential attributes should never change — create new objects instead to avoid ripple effects
- **Fail Fast**: Stop execution immediately on error — don't let errors propagate silently
- **Technological Centaur**: Human architect + AI assistant is the strongest combo, but human must remain supervisor
- **Readability before Performance**: Clean code makes it easier to identify true bottlenecks; premature optimization causes more harm than good

## Case Study: Mars Climate Orbiter (1999)

Ground control used English units (pound-force), spacecraft expected metric units (Newtons). Both sides used `double force = 10.5;` — a bare number with no semantic meaning. The spacecraft deviated from orbit and burned up in Mars' atmosphere. A semantic error, not a syntax error.

## Quotes

> "To program is to build theory and models" — Peter Naur

> "If the language you use shapes your perception of the world, what is your current codebase telling you about the reality you're trying to build?"

---
- Core to [[software-as-simulation]] — the foundational thesis
- Related to [[mapper-principles]] — the 6 principles that define the approach
- Related to [[bijection]] — the golden design rule
- Related to [[rich-domain-model]] — the alternative to anemic data holders
- Related to [[tell-dont-ask]] — the behavioral encapsulation principle
- Related to [[immutability]] — protecting essential attributes
- Related to [[fail-fast]] — error handling philosophy
- Related to [[technological-centaur]] — AI + human architect collaboration
- Related to [[readability-vs-performance]] — prioritization strategy
