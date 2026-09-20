---
title: "Software 3.0"
type: concept
tags: [ai-engineering, programming-paradigm, karpathy]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: [software-3]
---

## Summary

**Software 3.0** is Andrej Karpathy's framing of a new programming paradigm where **context and prompts become a programmable interface** for AI systems. It extends the progression:

- **Software 1.0**: developer writes explicit instructions (traditional code)
- **Software 2.0**: developer shapes behavior through data and training (ML)
- **Software 3.0**: developer shapes behavior through context, prompts, and natural-language control specifications

## Programming the Program

The key insight is that natural-language instructions can configure autonomous behavior. In [[autoresearch]], `program.md` serves as the control specification — it establishes mutable files, metrics, budgets, crash handling, and autonomy policy. The agent reads it as its constitution.

This pattern generalizes: AGENTS.md files, system prompts, project instructions, and evaluation rubrics are all Software 3.0 artifacts. They "program" the agent's behavior without traditional code.

## Relationship to Graph Engineering

Software 3.0 is the paradigm that makes [[graph-engineering]] possible. When prompts and context become the interface, the engineering challenge shifts from writing code to designing durable, queryable state (graphs) that agents can read and write. The `program.md` pattern extends into typed schemas, graph schemas, evaluation rubrics, and workflow specifications.

---

- Foundation for [[autoresearch]] — `program.md` is the canonical Software 3.0 artifact
- Enables [[graph-engineering]] — graph schemas and control specs are Software 3.0 interfaces
- Related to [[vibe-coding]] — vibe coding uses Software 3.0 without engineering discipline
- Source: [[sources/graph-engineering-karpathy]]
