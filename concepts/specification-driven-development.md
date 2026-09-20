---
title: "Specification-Driven Development"
type: concept
tags: [ai-engineering, software-engineering, methodology, requirements]
created: 2026-06-15
updated: 2026-06-15
sources: [practical-guide-ai-native-engineer]
aliases: [spec-driven-development, spec-first-development]
---

## Summary

**Specification-Driven Development** is the discipline of defining what you want *before* asking AI (or humans) to build it. In the AI-native era, it's the antidote to random prompting and vibe coding — AI agents get stuck in circular reasoning without clear, well-defined specifications. The principle: define success criteria, break problems into discrete milestones, execute incrementally, and validate at each checkpoint.

## Core Principles

- **Define before build**: Write specs before generating code. The quality of AI-generated code matches the quality of input specifications.
- **Discrete milestones**: Break problems into contained, well-defined chunks with clear success criteria.
- **Incremental execution**: Build and validate one milestone at a time. Never let agents run off with assumptions.
- **Checkpoint validation**: At each milestone, verify the output matches the spec before proceeding.

## In the ADLC

Within the [[agentic-development-life-cycle]], specification-driven development is the foundation of the Planning phase. Planning agents synthesize specifications from codebase exploration; building agents execute against those specs. The spec acts as a contract — implementation either matches or it doesn't, making verification binary rather than judgment-based.

---

- Core practice within [[ai-native-engineering]] — one of the four practices that separate AI-native engineers from vibe coders
- Foundation of the Planning phase in [[agentic-development-life-cycle]]
- Contrasts with [[vibe-coding]] — vibe coding is specification-free; spec-driven development is the professional alternative
- Related to [[context-engineering]] — specifications are a key component of the context layer fed to agents
- Benchmark source: [[sources/practical-guide-ai-native-engineer]] — Shah Rahman's guide on ByteByteGo
