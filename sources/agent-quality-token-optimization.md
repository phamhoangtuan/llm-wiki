---
title: "Agent Quality & Token Optimization — GitHub Workshop"
type: source
source_type: article
author: "Felix Gozali, Lakshya Tyagi (GitHub)"
url: "https://staticassets.goldcast.io/public_images/organization/4bbeac0f-e176-4d6f-85a7-ac3397470d44/lsQlOCxTfKqVMqgFOVUA_Agent_Quality_and_Token_Optimization_(customer-facing_workshop).pdf"
source_date: 2026-06-08
ingested: 2026-06-14
created: 2026-06-14
updated: 2026-06-14
tags: [ai-engineering, agents, token-optimization, agent-quality, llm, context-window, prompt-engineering]
concepts: [agent-quality-optimization, harness-engineering]
---

## Summary

A 30-slide workshop by GitHub's Felix Gozali and Lakshya Tyagi on maximizing agent quality while minimizing token costs. The workshop frames agent quality not as a prompt engineering problem but as an ROI optimization challenge — balancing output value against token expenditure. Covers compound error in multi-step agent workflows, the Lost in the Middle and Recency Bias effects in context windows, model selection strategies, deterministic guardrails (unit tests, linters, CI/CD), and a Research → Plan → Implement workflow pattern. Includes practical configuration guidance for AGENTS.md, custom agents, skills, MCPs, subagents, and scoped instructions.

## Core Message

> Agent quality is an ROI equation, not a prompt engineering problem. Value comes from compound reliability — even 99% per-step accuracy degrades to 60% after 50 steps. Quality amplifies value across dimensions (speed, autonomy, correctness); tokens only affect cost. Stop counting tokens. Start engineering quality.

## Key Takeaways

1. **Agent ROI = Value of Output − Token Cost**: Quality amplifies value across speed, autonomy, and correctness; tokens only affect one variable (cost)
2. **Compound error destroys reliability**: At 95% accuracy per step, only 36% reliability remains after 10 steps and just 8% after 50 steps. Even at 99% per step, only 60% survives 50 steps
3. **Context window is not unlimited**: Two biases degrade long-context performance — Lost in the Middle (information in the middle of context is poorly attended to) and Recency Bias / Context Rot (stale earlier context loses influence). Compact sessions and use `/clear` for new tasks
4. **Model selection is a strategy, not a default**: Use reasoning models (o3, Sonnet thinking) for synchronous planning and debugging; mid-tier models (Sonnet, 4o) for async implementation; low-tier models (Haiku, 4o-mini) for simple refactors. "Auto" mode is a lazy default to avoid
5. **Three-phase workflow reduces errors**: Research (/research finds relevant files), Plan (/plan with reasoning model creates spec), Implement (/fleet executes precise tasks) — prevents compounding errors from blind execution
6. **Deterministic guardrails catch agent mistakes**: Unit tests, linters, and CI/CD serve as quality gates that catch errors before they compound. With tests → failing test → correction → pass. Without → buggy change → buggy change → wasted cycles
7. **Agent configuration is engineering infrastructure**: AGENTS.md and copilot-instructions.md define non-negotiable rules; custom agents, skills, MCPs, subagents, and scoped instructions compose a configurable, maintainable agentic system
8. **Think in code, not conversation**: Power users think in scripts, compare CLI vs MCP trade-offs, reduce shell output, use chronicle analysis, and apply model-specific optimizations
9. **Long-term traits matter more than prompt tricks**: Strong analytical skills over raw coding ability; good architecture (DDD, hexagonal) for agent discoverability; iterate prompts like you iterate code
10. **Five things to start today**: Explore models manually, secure API access, install GitHub Copilot, use `--cache` and `--resume` flags, and use `--thinking` flags to close the feedback loop

## Companion Concept

→ [[agent-quality-optimization]]
