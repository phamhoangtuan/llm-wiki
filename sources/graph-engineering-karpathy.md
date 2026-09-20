---
title: "Graph Engineering: The Karpathy Loop, Improved 1000x by Itself"
type: source
source_type: article
author: "Independent Synthesis (based on Karpathy, Anthropic)"
url: "https://github.com/karpathy/autoresearch"
source_date: 2026-05-01
ingested: 2026-08-06
tags: [ai-engineering, agents, knowledge-graph, agent-architecture, workflows]
concepts: [graph-engineering, autoresearch, agent-hub, dynamic-workflows, graph-grounding, software-3, agent-loop, knowledge-graph, vibe-coding]
---

## Summary

A comprehensive synthesis mapping Andrej Karpathy's progression from **autoresearch** (autonomous ML experimentation) to **AgentHub** (agent-first collaboration platform) onto **Anthropic's workflow infrastructure** (five patterns, Dynamic Workflows, Knowledge Graph Construction Cookbook). The central thesis: the bottleneck in agent systems is not the next model call — it's the **placement of memory and evaluation**. Loops, DAGs, and knowledge graphs externalize state from context windows into durable, queryable structures.

## Key Claims

1. **Three-stage progression**: Vibe coding → Agentic engineering → **Graph engineering** (agents share durable state through typed, queryable graphs of work and knowledge)

2. **Each architecture externalizes a different bottleneck**:
   - Loop → iteration and evaluation
   - Chain → task order
   - Swarm → parallel search and role specialization
   - DAG (commit graph) → experiment lineage
   - Knowledge graph → shared facts, provenance, cross-session memory

3. **Autoresearch works because of four conditions**: verifiable output (measurable metric), reversible action (git reset), short horizon (~5 min runs), bounded environment (narrow repository)

4. **The ratchet loop** is a reusable template: inspect → propose → apply → evaluate → keep/revert. Only metric improvements survive.

5. **AgentHub inverts human Git assumptions**: thousands of agents explore simultaneously, most results never merged, failed experiments contain useful evidence, collaboration via graph traversal not merge requests

6. **Dynamic Workflows** shift orchestration from developer-written static scripts to Claude-generated JavaScript that spawns up to 1,000 sub-agents with fresh contexts

7. **Knowledge graphs serve three roles for agents**: shared memory (workers write structured updates), grounding layer (evaluator checks claims against edges), persistent world model (the agent forgets, the graph does not)

8. **The commit DAG and knowledge graph are complementary, not redundant**: DAG answers "what changed/who/when," KG answers "which entities exist, how are they related, which sources support which claims"

9. **entity-resolution** is framed as a reasoning task: surface forms (including zero-overlap aliases like "Edwin Aldrin" → "Buzz Aldrin") are mapped to canonical entities via model arbitration, with reversible decisions

10. **Practical build path** (incremental): Day 1 loop → Day 2 tools → Week 1 planning → Week 2 multi-agent → Month 1 graph → Month 2 swarm

## Architecture Patterns Covered

- **Karpathy's autoresearch**: agent edits `train.py`, runs ~5min training, metric-gated keep/revert
- **AgentHub**: bare Git repo + SQLite + HTTP API + CLI + message board; `ah children`, `ah leaves`, `ah lineage` commands
- **Anthropic's 5 workflow patterns**: Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer
- **Dynamic Workflows**: generated JavaScript orchestration, up to 1,000 sub-agents, fresh context per worker
- **Knowledge Graph Construction**: Haiku extraction → Sonnet resolution → NetworkX assembly → Sonnet querying with edge citations
- **Production architecture**: 5-plane separation (Control, Execution, Artifact, Graph, Evaluation)

## Key Terminology

| Term | Definition |
| ------ | ----------- |
| Autoresearch | Autonomous experimentation: agent edits code, evaluates, keeps or reverts based on metric |
| AgentHub | Agent-first collaboration platform: bare Git repo as experiment DAG |
| program.md | Natural-language control specification for the autoresearch loop |
| Ratchet loop | Iterative process retaining only metric improvements |
| Dynamic Workflows | Generated scripts that spawn and gather sub-agent tasks |
| Graph grounding | Constraining generation with facts retrieved from a graph |
| Commit DAG | Directed acyclic graph where commits are nodes and parent links are edges |
| Software 3.0 | Context and prompts become a programmable interface |

## Decision Framework

Six questions to choose architecture level:

1. Can success be verified? (If not, don't begin with autonomy)
2. Are steps stable? (Yes → chain; No → planning/orchestrator)
3. Are subtasks independent? (Yes → parallelize)
4. Must alternative lineages remain available? (Yes → DAG)
5. Must facts survive the run? (Yes → persist artifacts + graph)
6. Can the organization afford the cost and latency?

## Limitations Noted

- Autoresearch works on small single-GPU setups; doesn't prove safe self-modification of production training platforms
- Metrics can be gamed (improving validation loss while degrading other properties)
- AgentHub is explicitly a sketch, not production software
- Dynamic Workflows are expensive (1,000 sub-agents can cost tens of dollars)
- Fragmentation can reduce quality for tasks requiring coherent context
- Entity resolution false merges can catastrophically contaminate downstream queries
- The graph amplifies builder judgment — wrong ontology or source policy scales errors
