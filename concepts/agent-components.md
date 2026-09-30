---
title: "Agent Components"
type: concept
tags: [ai-engineering, agents, architecture, llm]
created: 2026-06-20
updated: 2026-06-20
sources: [new-sdlc-vibe-coding]
aliases: [agent-architecture, agent-pillars, 5-pillars-of-agents]
---

## Summary

An AI agent is built from **5 foundational components** — Model, Tools, Memory, Orchestration, and Deployment. These components are static by themselves; they only gain value when set in motion by the [[agent-loop]]. Together they form the complete architecture that transforms a raw reasoning engine into a production-grade autonomous system.

> "The static components only have value when set in motion by the dynamic loop they power."

## The 5 Pillars

| Component | Primary Function | Human Analogy | Real-World Examples |
|---|---|---|---|
| **Model** 🧠 | Reasoning engine — decides the next thought or tool call | The Brain: central logic and thinking processor | Claude, GPT-4, Gemini as "core reasoning" |
| **Tools** 🛠️ | APIs, scripts, MCP servers to interact with the world | The Hands: ability to execute tasks and manipulate objects | File system access, database queries, terminal commands |
| **Memory** 📚 | Retains session logs + project-specific rules (AGENTS.md) | The Experience: library of lessons from previous attempts | Conversation history, project conventions, past failures |
| **Orchestration** 🎭 | Logic that assembles context and dispatches tool results | The Nervous System: coordination connecting thought → action | Routing between sub-agents, managing hand-offs |
| **Deployment** 🌐 | Hosting + observability infrastructure | The Environment: stage/workspace where work happens | Cloud sandbox, monitoring dashboards, cost tracking |

### Model — The Reasoning Engine

The model is the core intelligence — it decides *what* to do next. But a raw model cannot "drive" a project alone. It needs the surrounding machinery (the harness) to translate reasoning into action. Model capability (GPT-4 vs Claude vs Gemini) matters far less than the quality of the harness around it. A well-configured harness with a mid-tier model outperforms a poorly-configured harness with a top-tier model.

### Tools — The Interface to Reality

Tools are what separate agents from chatbots. They give the model the ability to interact with external state: read/write files, query databases, execute commands, call APIs. The Model Context Protocol (MCP) standardizes this interface — described as "USB-C for AI." Tools need precise functional definitions with clear invocation parameters; ambiguous tool descriptions cause the model to misuse or avoid them.

### Memory — Persistent Knowledge

Memory operates at two levels:
- **Short-term**: Session logs, conversation history, recent actions
- **Long-term**: Project conventions (AGENTS.md), coding standards, architectural rules, past failures and lessons

Memory is what prevents agents from repeating mistakes and enables continuity across sessions. The repository — not chat history — is the System of Record for long-term memory.

### Orchestration — Coordination Logic

Orchestration governs how the agent assembles context, routes between sub-agents, manages hand-offs, and decides delegation strategies. It includes:
- Deterministic rules for delegation and sub-agent spawning
- Inter-agent communication protocols (A2A)
- Context assembly: what information goes to which agent
- Loop control: when to re-plan, when to stop

### Deployment — The Production Environment

Deployment provides the isolated, monitored workspace where agents operate:
- **Sandboxes**: Ephemeral, cloud-hosted runtimes with zero-trust scoped permissions
- **Observability**: Comprehensive telemetry, granular traces, cost metering
- **Guardrails**: Hard constraints enforced at the framework layer (never commit credentials)

## Components → System

The 5 components are necessary but not sufficient. What makes them a *system* is the [[agent-loop]] — the dynamic cycle that activates each component in sequence. Without the loop, you have expensive autocomplete. With the loop, you have an autonomous agent.

---

- Powered by [[agent-loop]] — the loop is what animates these static components into a functioning system
- Structured by [[harness-engineering]] — the harness organizes these components into a production-grade configuration
- Related to [[context-engineering]] — Memory and Instructions are context engineering artifacts; tool definitions are context
- Core to [[ai-native-engineering]] — AI-native engineers design systems by composing and configuring these components
- Related to [[agent-verification]] — Deployment includes observability that enables trajectory verification
- Benchmark source: [[sources/new-sdlc-vibe-coding]] — Part 2: "Defining the Agent — 5 Pillars of Intelligence"
