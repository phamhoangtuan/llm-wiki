---
title: "Software Architecture: The Hard Parts"
type: source
source_type: book
author: "Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani"
url: ""
source_date: 
ingested: 2026-01-28
tags: [software-architecture, distributed-systems, trade-offs, microservices, data]
concepts: [architecture-quantum, static-vs-dynamic-coupling, architecture-fitness-functions, architectural-decision-records, data-mesh, saga-pattern, decomposition-patterns, data-sovereignty, orchestration-vs-choreography]
---

# Software Architecture: The Hard Parts

**Authors:** Neal Ford, Mark Richards, Pramod Sadalage, Zhamak Dehghani | **Type:** Ebook | **Pages:** 906

## Summary

A comprehensive guide on modern trade-off analysis for distributed architectures. The core thesis: "best practices" do not exist in modern architecture — every organization is a unique "snowflake" of constraints. The architect's real job is to find the "least worst" combination of trade-offs.

## Core Concepts

### Architecture Quantum

An independently deployable artifact with high functional cohesion, high static coupling, and synchronous dynamic coupling. The fundamental unit of architectural analysis.

### Static vs Dynamic Coupling

- **Static Coupling**: How parts are wired together (dependencies, frameworks, OS)
- **Dynamic Coupling**: How parts communicate at runtime (sync/async, consistency, coordination)

### Two-Phase Structure

**Part I: Pulling Things Apart** — Decomposition patterns for monoliths:

- Tactical Forking (unstructured codebases)
- Component-Based Decomposition (structured codebases)
- Service granularity and operational data challenges

**Part II: Putting Things Back Together** — Communication patterns:

- Transactional sagas
- Contracts
- Data access patterns (replicated caching, interservice communication)

### Data as First-Class Concern

Data sovereignty and transactionality move within the service boundary. Distinction between:

- **Operational Data**: Day-to-day business (OLTP)
- **Analytical Data**: Strategic intelligence, often via Data Mesh

### Governance Mechanisms

- **Architectural Decision Records (ADRs)**: Capture context, decision, consequences — the "why" over the "how"
- **Architecture Fitness Functions**: Executable integrity assessments of architecture characteristics

### Sysops Squad Saga

A running fictional case study following a team at Penultimate Electronics refactoring a failing monolithic ticketing system, demonstrating each pattern in context.
