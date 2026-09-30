---
title: "Compound AI Systems"
type: concept
tags: [machine-learning, ai-engineering, orchestration, systems-design]
created: 2026-07-13
updated: 2026-07-13
sources: [introduction-to-machine-learning-systems]
aliases: [compound-ai, ai-ensembles, multi-agent-ai]
---

## Summary

**Compound AI Systems** are the paradigm shift from single monolithic models to orchestrated ensembles of specialized components — retrievers, reasoners, verifiers, tools, and agents working together. The future of AI isn't one bigger model; it's many models and tools that compose into a system smarter than any individual piece.

## Why Compound Systems

Single-model approaches hit diminishing returns (see [[ai-scaling-laws]]). Compound systems achieve more by:

- **Division of labor**: Each component specializes — a retriever finds context, a reasoner generates answers, a verifier checks correctness
- **Composability**: Swap components independently — upgrade the retriever without touching the reasoner
- **Tool use**: Models call APIs, query databases, run code — extending capability beyond what's encoded in weights
- **Safety through structure**: Verification layers catch hallucinations before they reach users

## Architecture Patterns

| Pattern | Components | Example |
| --- | --- | --- |
| **RAG** | Retriever + Generator | Search docs, feed context to LLM for grounded answers |
| **Agent with Tools** | Planner + Executor + Verifier | ReAct loop: plan, use tools, verify, iterate |
| **Ensemble** | Multiple models + Router | Route simple queries to small model, complex to large model |
| **Guardrails** | Input filter + Model + Output validator | Detect PII before inference, verify outputs before delivery |

## The Frontier

As AI systems become more autonomous, engineering value shifts from tweaking individual models to mastering integration, orchestration, and reliability of compound systems. The bottleneck is no longer "Can we build a smarter model?" but "Can we build a scalable, sustainable, safe system around it?"

---

- Part of [[machine-learning-systems]] — compound systems are the frontier (Part VI of the ML Systems framework)
- Related to [[retrieval-augmented-generation]] — RAG is the most widely deployed compound AI pattern
- Related to [[agent-components]] — agents are compound systems of model + tools + memory + orchestration
- Related to [[harness-engineering]] — compound systems need verification and guardrail infrastructure
- Benchmark source: [[sources/introduction-to-machine-learning-systems]] — Reddi covers compound AI as the future paradigm
