---
title: "Architectural Decision Records (ADRs)"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [software-architecture, documentation, decision-making, adr]
sources: [head-first-software-architecture, architecture-of-open-source-applications-vol2]
---

# Architectural Decision Records (ADRs)

Lightweight documents that capture the context, rationale, and consequences of significant architectural decisions. ADRs are institutional memory — "Why" preserved long after the "How" (code) has been refactored.

## Structure of an ADR

Each ADR typically contains:

1. **Title**: Short, descriptive name (e.g., "ADR-001: Use PostgreSQL as Primary Database")
2. **Context**: What problem are we solving? What constraints exist?
3. **Decision**: What did we choose?
4. **Consequences**: What are the trade-offs? What becomes easier? What becomes harder?
5. **Alternatives Considered**: What else did we evaluate and why was it rejected?

## Why ADRs Matter

> "Why is more important than how." — Second Law of Architecture (source: [[sources/head-first-software-architecture|Head First Software Architecture]])

Code changes; the reasoning behind decisions keeps teams aligned. ADRs:

- Prevent "why did they do this?" archaeology months later
- Help new team members understand architectural rationale
- Record trade-offs explicitly — no revisionist history
- Enable [[architecture-in-agile|agile architecture]] by capturing decisions as they emerge

## When to Write an ADR

Write an ADR when a decision is:

- **Strategic** (long-term impact, not a tactical fix)
- **Hard to change** (expensive to reverse)
- **Involves significant trade-offs** (e.g., consistency vs. availability)

## ADR Lifecycle

Proposed → Accepted → Deprecated → Superseded. ADRs are never deleted — superseded ones explain why the old decision was replaced.

---

- Core practice of [[risk-driven-architecture]] — ADRs record why specific risks were prioritized
- Documents [[architectural-characteristics]] — each ADR explains which -ilities drove the decision
- Enables [[architecture-in-agile]] — lightweight, incremental architectural documentation
- Embodies [[architecture-hoisting]] — ADRs are structural constraints encoded as institutional knowledge
