---
title: "The New SDLC With Vibe Coding: From ad-hoc prompting to Agentic Engineering"
type: source
source_type: book
author: "Addy Osmani, Shubham Saboo & Sokratis Kartakis"
url: ""
source_date: 2026-06-20
ingested: 2026-06-20
tags: [ai-engineering, agents, sdlc, vibe-coding, agentic-engineering, context-engineering, harness-engineering]
concepts: [agent-loop, agent-components, agent-verification, vibe-coding, harness-engineering, context-engineering, ai-native-engineering, agent-quality-optimization, agentic-development-life-cycle, specification-driven-development]
created: 2026-06-20
updated: 2026-06-20
---

A 51-page ebook mapping the transformation of software engineering from manual coding to agentic orchestration. Written by three Google/engineering leaders, it traces the 5-stage evolution of AI coding tools (autocomplete → autonomous agents), defines the core agent architecture (5 pillars + Perceive-Plan-Act-Observe loop), and establishes the economic and engineering case for systematic harness design over ad-hoc prompting.

## Key Claims

1. **Model is only 10% of the system.** A LangChain study found that fixing the model while tuning harness configuration (system prompt, tools, middleware) improved benchmark scores by +13.7 points — more than swapping to a larger model. Harness configuration is the primary driver of performance.

2. **The Agent Loop is the heartbeat of autonomy.** The Perceive-Plan-Act-Observe cycle with self-correction distinguishes agents from chatbots. Agents don't guess answers — they work through problems step-by-step, using failure as fuel for the next iteration.

3. **Context Engineering supersedes Prompt Engineering.** Rather than clever wording, success comes from providing structured information: instructions, knowledge, memory, examples, tools, and guardrails — 6 dimensions of context. Static context (AGENTS.md rules) ensures reliability; dynamic context (skills, RAG) optimizes token economics.

4. **Vibe Coding has a hidden interest rate.** Low upfront cost (CapEx) but high ongoing cost (OpEx) from trial-and-error loops, maintenance tax, and token burn. Agentic Engineering has higher CapEx (system design, test suites) but sustainable low OpEx — a 3-10x cost crossover in favor of engineering discipline over time.

5. **Your output is no longer code — it's the Harness.** The new craft is verification, judgment, and direction. "Generation is solved. Verification, judgment, and direction are the new craft."

6. **Verification must cover trajectory, not just output.** For non-deterministic agents, unit testing is insufficient. Production harnesses must verify both the artifact (code, config) and the reasoning + tool sequence used to reach it.

## Notable Quotes

> "The most profound shift in software engineering isn't a new language, framework, or cloud service. It's the transition from writing code to expressing intent."

> "If the AI model is a genius brain with no hands, Harness Engineering is building the body, tools, and environment for that brain to actually work in the real world."

> "Generation is solved. Verification, judgment, and direction are the new craft."

## Implementation Roadmap

The book provides a 4-phase, 7-week roadmap from zero to production agentic engineering:

| Phase | Timeline | Focus |
|---|---|---|
| Foundation | Week 1-2 | Create AGENTS.md, setup basic harness (sandbox, guardrails, observability), automate 1 workflow |
| Context Engineering | Week 3-4 | Static context (conventions, rules), dynamic context (RAG, skills), write evals first |
| Orchestration Mode | Week 5-6 | Decomposition practice, multi-agent workflows, deterministic hooks |
| Scale & Optimize | Week 7+ | Token economics monitoring, benchmark performance, harness iteration |

## Critical Standards Identified

- **Google's Agents CLI & ADK** — Scaffold, evaluate, manage agent lifecycle
- **Model Context Protocol (MCP)** — Standardize tool access, ensure interoperability
- **Agent-to-Agent (A2A) Protocol** — Cross-agent delegation and collaborative workflows
- **Configuration files (AGENTS.md)** — Versioned rule files as constitutional constraints

## 5-Stage Evolution of AI Coding

| Stage | Era | Capability |
|---|---|---|
| Autocomplete | ~2021 | Predict next token |
| Inline Code Suggestions | ~2022 | Complete functions from signatures |
| Chat-Based Generation | ~2023 | Natural language as interface |
| Coding Agents | ~2024-25 | Tool invocation, self-correction, test-execute loop |
| Autonomous Agents | ~2025-26 | Clone repo, plan architecture, execute in sandbox, submit PR |

## Connections

- Core to [[agent-loop]] — defines the Perceive-Plan-Act-Observe cycle as the heartbeat of agent autonomy
- Core to [[agent-components]] — establishes the 5 pillars (Model, Tools, Memory, Orchestration, Deployment) as the agent architecture
- Core to [[agent-verification]] — argues verification must cover both output and trajectory; introduces deterministic hooks
- Updates [[vibe-coding]] — provides the Vibe Coding vs Agentic Engineering spectrum with economics comparison
- Updates [[harness-engineering]] — adds the 90% rule and 6-component production anatomy
- Updates [[context-engineering]] — adds 6 dimensions of context, static vs dynamic, agent skills pattern
- Updates [[ai-native-engineering]] — adds Conductor vs Orchestrator mode, 4 orchestrator skills
- Updates [[agent-quality-optimization]] — adds token economics (CapEx vs OpEx), vibe coding's hidden costs
- Updates [[agentic-development-life-cycle]] — adds 4-phase implementation roadmap
- Grounded in [[specification-driven-development]] — spec-first development as the antidote to random prompting
