---
title: "Context Engineering"
type: concept
tags: [ai-engineering, agents, prompt-engineering, llm, knowledge-management]
created: 2026-06-15
updated: 2026-06-20
sources: [practical-guide-ai-native-engineer, agent-quality-token-optimization, new-sdlc-vibe-coding]
aliases: [context-curation, context-injection]
---

## Summary

**Context Engineering** is the systematic discipline of curating and injecting project-specific information into AI agent working memory to maximize output quality. It is the next evolution beyond prompt engineering — recognizing that the quality of AI-generated output is fundamentally bounded by the quality, relevance, and structure of the context the model receives.

> "The quality of AI output is bounded by the quality of context it receives." — Shah Rahman, Meta

## Context Engineering vs Prompt Engineering

| Prompt Engineering | Context Engineering |
|---|---|
| Crafting a single message to the model | Curating a persistent knowledge layer |
| One-off, ad-hoc instructions | Reusable, standardized, version-controlled artifacts |
| Focused on the *instruction* | Focused on the *environment* the instruction lands in |
| Easy to start, hard to scale | Requires upfront investment, compounds over time |

## Core Components

The context layer consists of reusable, standardized artifacts:

| Artifact | Role | Example |
|---|---|---|
| **AGENTS.md / CLAUDE.md** | Constitutional rules, constraints, conventions | Coding standards, banned patterns, workflow expectations |
| **Architectural diagrams** | System structure and component relationships | C4 diagrams, data flow maps |
| **Coding standards** | Style guides, naming conventions, patterns | Language-specific conventions, team preferences |
| **Business rules** | Domain logic, validation constraints | "A premium customer must have a valid payment method" |
| **Team conventions** | Shared practices and expectations | Branch naming, PR template, review checklist |
| **Development workflows** | Step-by-step processes | "Plan → Research → Implement → Verify" |

## Six Dimensions of Context

Beyond static files, context engineering addresses six dimensions that feed the agent's working memory:

1. **Instructions**: Role, mission objectives, operational guardrails
2. **Knowledge**: Architectural diagrams, technical debt logs, domain schemas
3. **Memory**: Short-term session logs + long-term project persistent state
4. **Examples**: Few-shot demonstrations, gold-standard reference patterns
5. **Tools**: Structured definitions for APIs, scripts, external service access
6. **Guardrails**: Formatting requirements, safety validations, hard-coded constraints

These six dimensions correspond to the Memory, Tools, and Orchestration components of the [[agent-components|agent architecture]]. Context engineering is the practice of curating and delivering the right information from each dimension.

## Static vs Dynamic Context

Context can be delivered in two modes — each with distinct trade-offs:

| Feature | Static Context | Dynamic Context |
|---|---|---|
| **Definition** | Always loaded (AGENTS.md rules) | Loaded on demand (RAG results, skills) |
| **Cost (Tokens)** | 🔴 High (paid in every interaction) | 🟢 Low (paid only when needed) |
| **Reliability** | ✅ Excellent: Agent never forgets | ⚠️ Variable: Subject to retrieval misses |
| **Use Case** | Core conventions, architectural rules | Task-specific knowledge, RAG retrieval |

**The balance**: Static context ensures the agent never violates foundational rules. Dynamic context keeps token costs manageable by loading specialized knowledge only when relevant. Overloading static context causes context rot; relying entirely on dynamic context risks retrieval misses on critical constraints.

## Agent Skills Pattern: Progressive Disclosure

The Agent Skills pattern implements dynamic context through progressive disclosure:

- ✅ Agent remains a **lightweight generalist** by default
- ✅ When a task matches a skill trigger → load **deep procedural knowledge**
- ✅ Optimizes token economics — prevents context rot from rarely-used instructions
- ✅ Prevents the "one giant instruction file" anti-pattern

This maps directly to the behavior files (AGENTS.md for static rules + skills loaded on demand for dynamic knowledge). The mental model: "What would a new team member need to know to contribute effectively, and how do I encode that knowledge in a form the AI can use?"

## Mechanics of Context Quality

Two well-documented biases govern how models utilize context:

### Lost in the Middle
Information in the middle of a long context window receives significantly less attention than information at the beginning or end. Critical instructions must be positioned strategically — near the beginning (system prompt) or near the end (most recent messages).

### Recency Bias / Context Rot
As context grows, earlier information loses influence. Stale context accumulates, diluting the signal-to-noise ratio and causing the agent to "forget" constraints established early in the session. Session compaction and scoping are essential countermeasures.

## MCP and Tool Integration

Anthropic's **Model Context Protocol (MCP)** — described as "USB-C for AI" — provides a universal standard for connecting agents to external tools and data sources. MCP extends context engineering from static files to dynamic, tool-mediated context retrieval.

## Shared Context Libraries

At the team level, shared context libraries become the core currency of AI-native development:
- Standardize context files, evaluation sets, and agent configurations across teams
- Package context through plugins, skills, and commands
- **Watch for uncontrolled proliferation** — teams competing for standardization rather than collaborating

## Impact

Teams practicing rigorous context engineering report **40-50% speed increases** and dramatically reduced alignment overhead in agent interactions.

---

- Foundational to [[ai-native-engineering]] — context engineering is the first and most important of the four core practices
- Related to [[agent-quality-optimization]] — agent quality optimization includes context strategy as a key dimension of ROI
- Implements principles from [[harness-engineering]] — the AGENTS.md file is a harness primitive that acts as a context engineering artifact
- Related to [[agent-components]] — the 6 dimensions of context map to Memory, Tools, and Orchestration components
- Contrasts with simple [[vibe-coding]] — vibe coders give one-off prompts; AI-native engineers build persistent context layers
- Benchmark source: [[sources/practical-guide-ai-native-engineer]] — ByteByteGo guide covering context engineering
- Benchmark source: [[sources/agent-quality-token-optimization]] — GitHub workshop on context strategy
- Benchmark source: [[sources/new-sdlc-vibe-coding]] — 6 dimensions, static vs dynamic context, agent skills pattern
