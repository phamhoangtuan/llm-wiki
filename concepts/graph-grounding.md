---
title: "Graph Grounding"
type: concept
tags: [ai-engineering, knowledge-graph, verification, agents]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: [graph-grounded-evaluation, graph-constrained-generation]
---

## Summary

**Graph Grounding** is the practice of constraining agent generation with facts retrieved from a knowledge graph, and evaluating claims against graph edges with provenance. Instead of agents reasoning from memory or unanchored context, they cite specific graph paths. An evaluator can check whether a claim has a supported path through the graph, returning structured, actionable feedback rather than free-form critique.

## Three Roles of the Graph for Agents

### 1. Shared Memory

Workers write findings as structured graph updates. A synthesizer traverses the graph to combine findings even if no single worker saw all source documents. This prevents context-window amnesia — the graph persists across sessions.

### 2. Grounding Layer

An evaluator checks claims against evidence. Example:

Claim: "Vendor X supplied the component involved in Incident Y."

The evaluator checks for edges:

- `(Vendor X, supplied, Component Z)`
- `(Component Z, involved_in, Incident Y)`

When an edge is missing, it returns structured feedback:

```json
{
  "decision": "revise",
  "claim": "Vendor X supplied the component in Y",
  "reason": "No supported path from Vendor X to Y",
  "required_evidence": [
    "A source-backed supplied relation",
    "A source-backed involved_in relation"
  ]
}
```

This is more actionable than "looks wrong" — it tells the agent exactly which edges are missing.

### 3. Persistent World Model
>
> "The agent forgets, the graph does not."

Persistence enables: long-running investigations, cross-session planning, incremental document ingestion, contradiction tracking, temporal facts, versioned decisions, audit trails, handoff between different models, and recovery after a failed run.

## Context Construction From a Graph

The graph should not become context dumping. A context builder:

1. Resolves entities mentioned in the task
2. Expands one or two hops over allowed edge types
3. Includes current artifact versions
4. Prioritizes recent verified claims
5. Includes conflicts and uncertainty
6. Serializes within a token budget
7. Attaches stable edge identifiers for citation

## Graph Write Invariants

Every graph write must satisfy:

1. Every claim has a source or is marked as inference
2. Every artifact has an authoring run and version
3. Every evaluation identifies a rubric
4. Every superseded object remains addressable

---

- Core mechanism in [[graph-engineering]] — the evaluation and memory layer
- Depends on [[knowledge-graph]] — the graph being queried and updated
- Complements [[agent-verification]] — graph grounding is structured verification against persistent facts
- Related to [[autoresearch]] — the evaluation step in the ratchet loop is a simple form of grounding
- Source: [[sources/graph-engineering-karpathy]]
