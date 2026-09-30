---
title: "Agent Hub"
type: concept
tags: [ai-engineering, agents, collaboration, git, dag]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: [agenthub, agent-collaboration-platform]
---

## Summary

**AgentHub** is Karpathy's sketch of an agent-first collaboration platform. Its central slogan: "GitHub is for humans. AgentHub is for agents." It combines a bare Git repository, a SQLite database, an HTTP service, a thin CLI, and a message board to enable thousands of agents to explore simultaneously through a **commit DAG** rather than a single main branch.

## How It Inverts Human Git

Agent research inverts human Git assumptions:

| Human Git (GitHub) | Agent Git (AgentHub) |
| --------------------- | ---------------------- |
| Few developers, serial review | Thousands of agents exploring simultaneously |
| Goal is merge to main | Most results never merged |
| Failed work is discarded | Failed experiments contain useful evidence |
| Pull requests, merge queue | Graph traversal as primary operation |
| One canonical leaf (main) | Frontier of leaves, no assumption of canonicity |

AgentHub removes convergence abstractions: no required main branch, no pull requests, no merge queue, no assumption that one leaf is canonical.

## Minimal Architecture

A compact implementation: one Go server binary, one SQLite database, one bare Git repository on disk, one API key per agent, rate limiting, bundle-size limits, and a thin `ah` CLI.

The design deliberately separates **mechanism from culture**. AgentHub does not know whether agents optimize validation loss, fix tests, search for vulnerabilities, or design APIs. The prompts and project instructions define behavior.

## The CLI as a Graph Interface

```bash
ah push                    # Push HEAD commit to hub
ah fetch <hash>            # Fetch any commit
ah log [-agent X]          # Show recent commits
ah children <hash>         # What was tried above this?
ah leaves                  # Frontier: no children (unexplored)
ah lineage <hash>          # Ancestry path to root
ah diff <hash-a> <hash-b>  # Compare any two commits
```

These commands encode a different unit of collaboration:

- `children` → which ideas were tried on top of a result
- `leaves` → the unexplored frontier
- `lineage` → the path that produced an outcome

## The DAG Is the Graph

Commits are nodes. Parent links are directed edges. Each commit node carries: parent commit, agent ID, hypothesis, code diff, metric, runtime, memory usage, environment, keep/discard status, links to discussion posts, and links to related experiments.

Graph traversals answer questions awkward in conventional branch models:

- Which retained result has the best metric under a memory limit?
- Which experiments descend from the batch-size change?
- Which agents independently rediscovered the same optimization?
- Which leaves have no evaluation?
- Which lineages improve quickly and then stagnate?

## Collaboration Without Shared Context

The message board provides the social layer. Agents post hypotheses, failures, summaries, and coordination notes. A discarded change may still teach other agents that an idea fails under one condition.

The system reduces context copying: an agent doesn't need every prior transcript. It queries relevant lineages, reads a few summaries, fetches a commit, and continues. This is **graph-grounded context construction** — retrieve the connected state needed for the current decision rather than replaying the entire history.

## Status: A Sketch

The repository explicitly warns: "Work in progress. Just a sketch. Thinking..." Missing concerns include: distributed storage, repository compaction, trust among agents, malicious bundles, experiment reproducibility, semantic duplicate detection, compute scheduling, and long-term graph indexing.

The limitation strengthens the architectural lesson: the repository identifies which conventional abstractions fail first when agents become numerous — single main branch, human-paced review, transcript-based memory, and merge-centered collaboration.

---

- Scales [[autoresearch]] — from one loop to thousands of concurrent explorers
- Implements the commit DAG in [[graph-engineering]] — the work graph
- Complementary to [[knowledge-graph]] — DAG for work lineage, KG for domain facts
- Inverts [[agentic-development-life-cycle]] assumptions — no main branch, no single canonical result
- Source: [[sources/graph-engineering-karpathy]]
