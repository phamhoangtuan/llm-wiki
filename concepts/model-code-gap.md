---
title: "Model-Code Gap"
type: concept
tags: [software-architecture, design-intent, code-quality]
created: 2026-06-26
updated: 2026-06-26
sources: [just-enough-software-architecture-fairbanks]
aliases: [architecturally-evident-coding, design-intent]
---

The Model-Code Gap is the disconnect between **design intent** (what the architect intended) and **code reality** (what the code actually does). Code alone cannot express *why* a decision was made — it can only show *what* was implemented.

## Why It Matters

> "Code is the truth, but not the whole truth."

A developer reading code sees variables, loops, and function calls — the **phenomena**. An architect sees thread-safe locking policies, event-driven architecture, fault isolation boundaries — the **strategy**. The gap between these two perspectives is the source of architectural drift: as code evolves without awareness of design intent, it silently violates the architecture.

## Point of View Is Worth 80 IQ Points

Alan Kay's insight applies directly to software:

| Rookie Perspective | Coach (Architect) Perspective |
|---|---|
| Sees raw phenomena: variables, loops, function calls | Sees strategy: concurrency policies, communication patterns, isolation boundaries |
| "This function calls that function" | "This is an event-driven architecture with async message passing" |
| Fixes symptoms | Addresses root structural causes |

The right **point of view** — the architectural lens — transforms how you read and write code.

## Architecturally-Evident Coding

The antidote to the model-code gap: write code so that **architectural structure is visible** in the codebase itself.

**Principle**: If architecture requires fault isolation via separate processes, organize modules and packages to reflect that boundary. Make it impossible for a new developer to accidentally create cross-process dependencies that violate the architecture.

**Examples**:
- Separate packages for each bounded context (DDD alignment)
- Directory structure that mirrors architectural layers (presentation, domain, data)
- Explicit interfaces at module boundaries that enforce architectural rules
- Build system constraints that prevent forbidden dependencies

## Chain of Intentionality

The Rackspace case study demonstrates the chain: a deliberate architectural choice (accept 15-minute stale data) traces directly to a higher-level goal (scalability to handle terabytes). Without architectural documentation, this trade-off looks like a bug. With it, it's an **intentional, reasoned decision**.

This chain must be preserved across the model-code gap. Every "weird" implementation detail should have a traceable architectural rationale.

## Bridging the Gap

Strategies to minimize the model-code gap:

1. **Architecturally-evident coding** — structure reflects intent
2. **Architecture Decision Records (ADRs)** — document the *why* of key decisions
3. **"Just enough" modeling** — lightweight diagrams that explain strategy without BDUF overhead
4. **Code reviews with architectural lens** — reviewers check not just correctness but alignment with design intent
5. **Architecture Hoisting** — encode guarantees in structure so code *can't* violate them

---

## Connections

- [[architecture-hoisting|Architecture Hoisting]] — The strongest bridge: guarantees encoded in structure so code can't drift
- [[risk-driven-architecture|Risk-Driven Architecture]] — The meta-framework that determines how much modeling is "just enough"
- [[software-rot|Software Rot]] — Unchecked model-code gap accelerates code degradation
- [[code-archaeology|Code Archaeology]] — Recovering lost design intent from code alone
- [[software-as-simulation|Software as Simulation]] — Software models reality; the gap is between the model and its implementation
- [[domain-driven-design|Domain-Driven Design]] — Bounded Contexts and Ubiquitous Language as bridges between model and code
- [[solid-principles|SOLID Principles]] — Principles that keep code aligned with design intent
