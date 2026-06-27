---
title: "Architecture in Agile"
type: concept
tags: [software-architecture, agile, project-management, methodology]
created: 2026-06-26
updated: 2026-06-26
sources: [just-enough-software-architecture-fairbanks]
aliases: [iteration-zero]
---

Architecture in Agile reconciles the perceived tension between upfront design and iterative development. Architecture is not Agile's enemy — it's the **skeleton that makes agility possible**. Without architectural bones, iterative development collapses into a Big Ball of Mud.

## The False Dichotomy

| Misconception | Reality |
|---|---|
| "Agile means no architecture" | Agile needs *just enough* architecture to guide iterations |
| "Architecture means BDUF" | Architecture can be risk-driven, incremental, and adaptive |
| "Architects slow down teams" | Architects reduce the risk of building the wrong thing |

## Three Integration Strategies

### 1. Iteration Zero

Reserve the first iteration (or portion of it) for **architecture drivers** — the requirements that shape the system's structure. This is not BDUF: you design only what's needed to establish the skeleton, not every detail.

Activities in Iteration Zero:
- Identify architecture drivers (top 3-5 risks)
- Set up development environment and CI/CD
- Establish architectural conventions and constraints
- Create lightweight architecture decision records (ADRs)

### 2. Feature & Risk Backlog

The Product Backlog must contain both **user features** and **risk mitigation tasks**. Educate the Product Owner that technical risk reduction deserves equal priority to user-visible functionality.

| Traditional Backlog | Risk-Aware Backlog |
|---|---|
| "User login page" | "User login page" |
| "Search functionality" | "Authenticate against OAuth provider" |
| "Shopping cart" | **"Benchmark query performance under 10K concurrent users"** |
| | **"Implement circuit breaker for payment service"** |

Risk mitigation tasks are **not optional** — they are the architecture work that prevents catastrophic failure.

### 3. Model-Code Gap Management

Iterative development amplifies the [[model-code-gap]] because code changes rapidly while design intent drifts. Counter-strategies:
- **"Just enough" modeling** — lightweight diagrams updated alongside code, not massive upfront specs
- **Architecturally-evident coding** — code structure reflects architectural intent
- **Architecture reviews as part of Definition of Done** — not a separate phase

## Architecture as Skeleton, Not Straitjacket

Good architecture in Agile:
- Provides **guide rails** that reduce needless creativity on solved problems
- Enables **parallel work** by defining clear module boundaries
- Makes **refactoring safer** by establishing invariants
- Does **not** dictate implementation details that should be discovered iteratively

## Success Metrics

> "Architecture is not about drawing diagrams; it is about reducing the chance of failure so you can get back to the truth of the code."

In Agile terms: architecture work is successful when it **reduces the risk** of future sprints being derailed by structural problems.

---

## Connections

- [[risk-driven-architecture|Risk-Driven Architecture]] — The decision framework for what architecture to do and when
- [[model-code-gap|Model-Code Gap]] — The gap that Agile iterations amplify without architectural discipline
- [[architecture-hoisting|Architecture Hoisting]] — Structural guarantees that persist across iterations
- [[software-rot|Software Rot]] — What happens when Agile proceeds without architecture
- [[refactoring-at-scale|Refactoring at Scale]] — Correcting architectural drift in Agile codebases
- [[domain-driven-design|Domain-Driven Design]] — Bounded Contexts provide the skeleton for Agile teams
- [[agentic-development-life-cycle|Agentic Development Life Cycle (ADLC)]] — AI-era evolution of SDLC with architectural considerations
