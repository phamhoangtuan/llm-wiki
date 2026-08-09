---
title: "Agent Loop"
type: concept
tags: [ai-engineering, agents, autonomy, llm]
created: 2026-06-20
updated: 2026-08-06
sources: [new-sdlc-vibe-coding, graph-engineering-karpathy]
aliases: [perceive-plan-act-observe, agentic-loop, agent-cycle]
---

## Summary

The **Agent Loop** is the iterative cycle that powers autonomous AI agents — the mechanism that distinguishes agents from chatbots. Rather than guessing an answer from a single prompt, an agent works through problems step-by-step: perceiving the goal, planning actions, executing them via tools, observing results, and iterating until the mission is complete. The loop is the "heartbeat" of agent autonomy.

> AI Agent = A software system that perceives a goal → plans steps → takes action using tools → observes results → iterates until mission complete.

## The 4-Stage Cycle

```
1. PERCEIVE GOAL
   • Scan the "scene": user prompt, files, environment state
   • Understand mission state and current progress
   • Identify constraints and boundaries

        ↓

2. PLAN STEPS
   • Model reasons through the logic of the problem
   • Decide which actions to take and in what order
   • Order actions specifically to achieve the intent

        ↓

3. ACT
   • Utilize tools: write files, search databases, execute terminal commands
   • Take concrete action in the world
   • Each action changes state — moves the needle

        ↓

4. OBSERVE RESULTS
   • Evaluate outcome: Did tests pass? Does output match spec? Any errors?
   • If FAIL → error becomes new information → re-plan (back to stage 2)
   • If PASS → mission complete or next goal
```

## Self-Correction: Failure as Data

The loop's power comes from treating failure as input, not failure:

```
Test fails or error thrown
    ↓
Agent uses error message as new information
    ↓
Update strategy → Try again
    ↓
Loop continues until goal met OR stopping condition reached
```

Agents don't "fear failure" — they use failure as fuel for the next iteration. Each failed attempt provides diagnostic data that narrows the solution space.

## Agent vs Chatbot

| Chatbot | Agent |
| --- | --- |
| Single prompt → single response | Iterative loop → multi-step execution |
| Stateless (or limited context) | Stateful — tracks progress across steps |
| No tool access | Invokes tools to interact with the world |
| No self-correction | Failure triggers re-planning |
| "What's the answer?" | "How do I work through this?" |

The agent loop is what transforms a reasoning model from a passive question-answerer into an active problem-solver.

## Relationship to Harness Engineering

The [[harness-engineering]] discipline structures and enforces this loop. Without a harness:

- The agent may skip verification (declare victory too early)
- The loop may not close (loss of continuity)
- Self-correction may go unbounded (overreach)

The harness provides the scaffolding that ensures each stage of the loop completes before proceeding — making the loop a reliable production mechanism, not just an ad-hoc pattern.

## Concrete Implementation: Karpathy's Autoresearch

[[autoresearch]] is the canonical concrete implementation of the agent loop for ML experimentation. It specializes the generic perceive-plan-act-observe cycle into a **ratchet loop**:

1. **Inspect** (perceive): read current `train.py` and recent history
2. **Propose** (plan): one motivated change guided by `program.md`
3. **Apply** (act): commit the candidate change, run ~5min training
4. **Evaluate** (observe): measure `val_bpb` and peak memory
5. **Keep or revert**: if metric improves → keep; else → `git reset`

The key insight: every experiment becomes a node in a commit DAG with parent state, code diff, metric, and keep/discard decision. The loop converts human working memory into a machine-readable experiment lineage — the foundation of [[graph-engineering]].

Karpathy's loop works because of four conditions: **verifiable output** (measurable metric), **reversible action** (git reset), **short horizon** (~5 min runs), and **bounded environment** (narrow repository). These form a reusable template for any autonomous agent loop.

---

- Core to [[agent-components]] — the 5 components (Model, Tools, Memory, Orchestration, Deployment) are static; the loop is what animates them
- Structured by [[harness-engineering]] — harness primitives enforce each stage of the loop as mandatory gates
- Distinct from [[vibe-coding]] — vibe coding skips the loop (prompt → output → done); agentic engineering runs it systematically
- Implements [[agentic-development-life-cycle]] — ADLC adapts the loop for collaborative human-agent development
- Related to [[fail-fast]] — self-correction catches failures early, preventing compound errors
- Specialized by [[autoresearch]] — Karpathy's ratchet loop for ML experimentation
- Foundation for [[graph-engineering]] — the loop generates the commit DAG
- Benchmark source: [[sources/new-sdlc-vibe-coding]] — Part 3: "The Beating Heart — The Perceive-Plan-Act-Observe Loop"
- Extended source: [[sources/graph-engineering-karpathy]] — Autoresearch as concrete loop implementation
