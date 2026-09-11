---
title: "Graph Engineering"
type: concept
tags: [ai-engineering, agents, knowledge-graph, agent-architecture]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: []
---

## Summary

**Graph Engineering** is the third stage in Karpathy's progression of AI-assisted development: vibe coding → agentic engineering → graph engineering. It is the discipline of building agent systems where agents share **durable state through typed, queryable graphs** of work and knowledge, rather than relying on context windows as working memory.

> "The bottleneck is often not the next model call. It is the placement of memory and evaluation."

## The Three-Stage Progression

| Stage | Memory | Evaluation | Agent Role |
| ------- | -------- | ------------ | ------------ |
| **Vibe Coding** | Prompt context only | "Looks like it works" | Code generator |
| **Agentic Engineering** | Transcript + harness state | Test suites, evals, rubrics | Junior engineer |
| **Graph Engineering** | Typed graphs (DAG + KG) | Graph-grounded evaluation | Research community |

## Core Insight: Externalize Bottlenecks

Each architecture pattern externalizes a different constraint from the context window into durable infrastructure:

- **Loop** → externalizes iteration and evaluation ([[autoresearch]])
- **Chain** → externalizes task order
- **Swarm** → externalizes parallel search and role specialization ([[agent-hub]])
- **Commit DAG** → externalizes experiment lineage
- **Knowledge Graph** → externalizes shared facts, provenance, and cross-session memory ([[knowledge-graph]])

## Two Complementary Graphs

Graph engineering uses two distinct graph structures that serve different purposes:

### Commit DAG (Work Graph)

- Answers: What changed? Which experiment is the parent? Which agent produced the change? Which lineages remain active?
- Nodes: commits, each carrying code diff, metric, agent ID, hypothesis, keep/discard status
- Edges: parent-child (experiment lineage)
- Query examples: "Which retained result has the best metric under a memory limit?" "Which leaves have no evaluation?"

### Knowledge Graph (Domain Graph)

- Answers: Which entities exist? How are they related? Which sources support which claims? Which claims conflict?
- Nodes: entities, claims, sources, artifacts, agent runs, evaluations
- Edges: MENTIONS, SUPPORTS, CONTRADICTS, DERIVED_FROM, PRODUCED, EVALUATES, SUPERSEDES
- Query examples: "Which sources claim X?" "Does evidence path exist from claim to source?"

## The Graph-Grounded Agent Task

A standard pattern from the paper:

1. Receive objective and constraints
2. Resolve task entities against the graph
3. Retrieve bounded subgraph with provenance
4. Create typed plan, validate dependencies
5. Assign independent steps to isolated workers
6. Require structured artifacts and evidence
7. Publish candidate graph updates
8. Validate schemas, permissions, provenance
9. Run deterministic tests
10. Run evaluator agents against rubrics
11. Resolve conflicts or escalate uncertainty
12. Publish versioned final artifact
13. Link to sources, graph paths, runs, evaluations
14. Record cost, latency, failures, open questions

## Production Architecture: Five Planes

A reliable graph-engineering system separates concerns across five planes:

1. **Control plane**: receives objectives, creates plans, allocates budgets, decides when to stop
2. **Execution plane**: runs tools, tests, training jobs, sub-agents in isolated environments
3. **Artifact plane**: stores immutable versions of plans, drafts, code changes, reports, metrics
4. **Graph plane**: stores entities, claims, relations, provenance, experiment lineage, task dependencies
5. **Evaluation plane**: runs deterministic checks, model evaluators, statistical scorers, human review

## Quality Invariant

> "Every important output can be traced to an objective, a plan, an artifact, a source, a graph path, an evaluator decision, and a bounded execution record."

When this is false, adding more agents increases opacity. When true, loops, swarms, DAGs, and knowledge graphs become composable engineering mechanisms.

## When Not to Use Graphs

A graph may be unnecessary when: tasks are independent, no cross-session state is required, answers depend on one document, relations are fixed and simple, a relational table answers every query, provenance is not needed, or extraction errors would outweigh traversal value.

---

- Builds on [[agentic-development-life-cycle]] — graph engineering is the next stage beyond ADLC
- Uses [[knowledge-graph]] — domain graph is one of two complementary structures
- Enabled by [[autoresearch]] — the loop that generates the commit DAG
- Scaled by [[agent-hub]] — the platform that makes DAG traversal the primary collaboration mode
- Uses [[dynamic-workflows]] — generated orchestration for swarm fan-out
- Depends on [[graph-grounding]] — constraining agent outputs with graph facts
- Source: [[sources/graph-engineering-karpathy]]
