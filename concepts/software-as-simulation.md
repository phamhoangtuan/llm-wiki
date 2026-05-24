---
title: "Software as Simulation"
type: concept
tags: [architecture, philosophy, domain-modeling]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
---

## Summary

Software is not a list of commands for a computer. It is a **simulator of reality** — a computational model that must faithfully mirror the real-world domain it serves. When code stops reflecting reality accurately, it becomes fragile, incomprehensible, and dangerous.

## Core Thesis

> "To program is to build theory and models" — Peter Naur

Code does not just run — it **explains** the business domain. A well-designed codebase is a living theory of how the world works, executable on a machine.

## Key Implications

- Code must be a faithful mirror of the business domain
- Semantic errors (wrong model) are more dangerous than syntax errors (code doesn't compile)
- The real world is the ultimate source of truth for the simulation
- Language shapes thought — choosing the right types and patterns encourages rich modeling

---
- Foundation for [[mapper-principles]] — the 6 principles that operationalize this philosophy
