---
title: "Architecture Fitness Functions"
type: concept
tags: [software-architecture, quality, governance, testing]
created: 2026-07-14
updated: 2026-07-14
sources: [software-architecture-hard-parts]
---

# Architecture Fitness Functions

Executable specifications that perform objective integrity assessments of architecture characteristics. Introduced in *Software Architecture: The Hard Parts* as a governance mechanism.

## Purpose

While Architectural Decision Records (ADRs) document *why* a decision was made, fitness functions verify that the decision *still holds*. They prevent architecture drift — the gradual erosion of architectural intent as developers make local changes.

## How They Work

A fitness function is code that tests an architectural characteristic:

- **Scalability**: Does response time stay within SLA under load?
- **Modularity**: Are there unauthorized dependencies between modules?
- **Security**: Are all endpoints authenticated?
- **Performance**: Is query latency below threshold?

Run in CI/CD pipelines, fitness functions fail the build when architecture rules are violated.

## Relationship to Testing

Fitness functions are tests at the *architecture* level:

- Unit tests verify behavior
- Integration tests verify component interactions
- Fitness functions verify architectural integrity

## Governance Without Bureaucracy

Fitness functions shift architecture governance from manual review meetings to automated enforcement — the "governance through automation" principle.

---

## Connections

- [[architectural-decision-records]] — Document the decisions that fitness functions enforce
- [[architecture-hoisting]] — Shifting quality guarantees into structural constraints
- [[model-code-gap]] — Fitness functions close the gap between design intent and code reality
- [[shift-left-security]] — Security fitness functions embedded in CI/CD
