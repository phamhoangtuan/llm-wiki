---
title: "Agentic Development Life Cycle"
type: concept
tags: [ai-engineering, agents, sdlc, methodology, process]
created: 2026-06-15
updated: 2026-06-15
sources: [practical-guide-ai-native-engineer]
aliases: [ADLC, agentic-sdlc]
---

## Summary

The **Agentic Development Life Cycle (ADLC)** is a redefinition of the traditional Software Development Life Cycle for environments where AI agents collaborate with humans to produce software. Traditional SDLC — even extreme agile — falls short because it was designed for human-only development. ADLC reimagines each phase for agent-human collaboration.

## The Five Phases

```
Planning → Building → Testing → Review → Documentation
    ↑                                            │
    └──────── Codify ADLC (continuous) ←────────┘
```

### 1. Planning
The most critical phase. Uses deep research and planning modes with multiple agents for parallel exploration. Agents explore the codebase, flag ambiguities, decompose tasks, estimate difficulty, and create roadmaps with version milestones. A planning agent synthesizes findings from multiple exploration agents into a coherent implementation strategy.

### 2. Building
AI agents handle end-to-end feature implementation at a junior-to-mid-level engineer capacity. The human acts as tech lead, orchestrating multiple agents rather than coding directly. Sequential or parallel execution models depend on the roadmap. Tools: Claude Code, Cursor Composer, GitHub Copilot Agent Mode, OpenAI Codex.

### 3. Testing
TDD reincarnated for the agentic era. Agents write test plans first, then implement code. All tests should fail at the beginning and incrementally pass. Three levels: unit (atomic), integration (cross-feature), end-to-end (cross-system). Critical insight: **don't overindex on unit testing at the expense of integration or system testing**.

### 4. Review
Agent swarms specialize in distinct review dimensions: functionality, quality, scalability, performance, reliability, security, privacy. Agents take the first pass and produce reports; humans review each report. When one agent discovers an issue (e.g., injection vulnerability), apply the **generalization principle**: if one instance exists, others likely do too.

**Pro pattern**: Separate planning, building, testing, and review agents. Each swarm develops a distinct perspective on the codebase. Planning agents challenge building agents who take shortcuts; testing agents catch coverage gaps; review agents catch incorrect implementations that appear correct.

### 5. Documentation
Shift from post-facto documentation to continuous generation. AI agents generate summaries, key design decisions, architectural diagrams, and changelogs in real time. This feeds into API documentation, feature collateral, and customer-facing content — finally solving the stale documentation problem.

### Codify ADLC
Encode Layer-1 (individual) and Layer-2 (team) practices into maintained, self-evolving context files, skills libraries, and MCP tools. This ensures ADLC adoption scales across the organization rather than remaining tribal knowledge.

## Why Traditional SDLC Falls Short

| Traditional SDLC | ADLC |
|---|---|
| Human writes code, human reviews | Agent writes code, agent + human review |
| One developer per feature | Multiple specialized agents per feature |
| Documentation as afterthought | Documentation as continuous byproduct |
| Review bottlenecked by human bandwidth | Agent first pass → human final review |
| Planning by lead engineer | Planning by agent swarm with human oversight |

## The Learning Loop

AI compresses the build step dramatically, but compression value depends on execution quality throughout the remaining cycle. Faster building without robust user observation and scope discipline produces faster divergence from product goals.

---

- Core process for [[ai-native-engineering]] — ADLC is the operational framework that AI-native engineers execute
- Depends on [[context-engineering]] — each ADLC phase shares a curated context layer
- Enforced by [[harness-engineering]] — harness primitives (AGENTS.md, feature_list.json) provide structural enforcement within ADLC
- Implements [[specification-driven-development]] — the Planning phase is specification-driven development at scale
- Related to [[tdd-methodology]] — ADLC's Testing phase is TDD adapted for agentic workflows
- Benchmark source: [[sources/practical-guide-ai-native-engineer]] — Shah Rahman's ADLC framework
