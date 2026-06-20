---
title: "Harness Engineering"
type: concept
tags: [ai-engineering, agents, reliability, testing, workflow]
created: 2026-05-31
updated: 2026-06-20
sources: [learn-harness-engineering, new-sdlc-vibe-coding]
---

## Summary

**Harness Engineering** is a discipline for building reliable, closed-loop systems around AI agents. Rather than trying to make models "smarter" through better prompts, harness engineering focuses on structural enforcement: explicit rules, state management, granular verification, and systematic feedback loops. The output is not a better model — it's a *trustworthy engineering system*.

> "If the AI is the engine, the harness is the chassis and the steering."

## Core Problem: Intelligence ≠ Reliability

| Capability | Failure Mode (Without Harness) |
|---|---|
| Fast code generation | Loss of continuity in long, multi-session tasks |
| Advanced reasoning | Overreach & under-finish: drifts beyond scope |
| Large context windows | Declare victory too early: stops when code "looks good," skips testing |

> Raw intelligence without structural enforcement is a liability, not an asset.

## The Closed-Loop System

```
❌ Without harness: Prompt → Model → Output → "Done!" (may have bugs, lost context, wrong scope)

✅ With harness:
   Goal → Init → Execute → Feedback → Verify → (Fail? Auto-fix → Verify) → Done → Handoff
```

The agent **cannot** proceed past verification until the test suite returns "Passed." Verification is mandatory — not optional.

## Four Harness Primitives

A reliable harness is built from four atomic configuration files:

| Primitive | Role | Prevents |
|---|---|---|
| **`AGENTS.md`** | Rule definition: Clear Objective, constraints, boundaries | Agent overreach — going outside scope |
| **`init.sh`** | Environment setup: Reproducible, stable starting point | Building on broken foundations |
| **`feature_list.json`** | Requirement tracking: Granular checklist per feature | "Declare victory too early" — agent must tick each item |
| **`claude-progress.md`** | State persistence: Progress + context for next session | Loss of continuity across sessions |

### Design Principle: Primitives > Prompts

Mega-prompts (one giant instruction file) cause instruction drift, competing priorities, and model confusion. Harness primitives are **atomic, separate files** — each with a single responsibility.

## Five-Phase Agentic Workflow

```
┌─────────────────────────────────────┐
│ 1. GOAL SETTING                      │
│    Read AGENTS.md → internalize rules │
├─────────────────────────────────────┤
│ 2. INITIALIZATION                    │
│    Run init.sh → verify environment   │
├─────────────────────────────────────┤
│ 3. EXECUTION                         │
│    Perform tasks → update             │
│    feature_list.json → reconcile      │
├─────────────────────────────────────┤
│ 4. FEEDBACK LOOPS                    │
│    Monitor CLI/logs → run test suite  │
│    ❌ Fail → Auto-fix loop → re-verify│
│    ✅ Pass → Proceed to Phase 5       │
├─────────────────────────────────────┤
│ 5. STATE PERSISTENCE                 │
│    claude-progress.md → clean handoff │
│    Document done + next → commit      │
└─────────────────────────────────────┘
```

## Three Failure Modes & Solutions

### 1. "Declare Victory Too Early"

Agent sees no syntax errors → claims "done." Root cause: no granular verification.

**Solution**: `feature_list.json` forces per-requirement sign-off. "Done" = every item ticked + test suite passed.

### 2. Loss of Continuity

Session timeout or context shift → agent "forgets" what it was doing. Root cause: model memory is ephemeral.

**Solution**: `claude-progress.md` persists state in the repository. The repository, not chat history, is the System of Record.

### 3. Building on Broken Foundations

Agent starts in an inconsistent environment → builds on top of failures. Root cause: no stable starting point.

**Solution**: `init.sh` as a dedicated phase ensures a reproducible, verified foundation before execution begins.

## Verification Loop: The Heart of Reliability

```
Encounter Issues → Auto-fix → Run Test Suite → Verify
    ↑                                              ↓
    └────────── (Fail: loop back) ←───────────────┘
                                     (Pass: Done)
```

Reliability is a byproduct of closed-loop verification, not of prompt engineering. If the harness doesn't facilitate auto-fix through runtime observability, you have expensive autocomplete — not an agent.

## The 90% Rule: Harness Determines Success

A LangChain study demonstrated that harness configuration — not model selection — is the primary driver of agent performance:

- **Fixed model**, tweaked only system prompt + tools + middleware
- **Result**: +13.7 points on Terminal Bench 2.0
- **Conclusion**: Harness configuration > model swapping

> "Model is only 10% of the system. The harness is the other 90%."

The harness is not an "optional extra" — it's the physical scaffolding that transforms raw inference into a reliable production asset. Investing in a better model without improving the harness yields diminishing returns.

## Anatomy of a Production-Grade Harness

A production harness comprises six components beyond the four primitives:

| Component | Purpose | Production Requirement |
|---|---|---|
| **Instructions & Rule Files** 📜 | Establish agent identity, boundaries, prohibited trajectories | Versioned config files (AGENTS.md, CLAUDE.md) in codebase |
| **Tools & MCP Servers** 🔧 | Enable model interface with external state (APIs, DBs, file systems) | Precise functional definitions + semantic prose for invocation params |
| **Sandboxes & Managed Runtimes** 🧪 | Isolated execution environments for code verification | Cloud-hosted, ephemeral runtimes with zero-trust scoped permissions |
| **Orchestration Logic** 🎭 | Govern sub-agent spawning, specialist hand-offs, iterative loop | Deterministic rules for delegation + inter-agent communication protocols |
| **Guardrails & Hooks** 🛡️ | Enforce hard constraints at framework layer | Final-layer deterministic code intercept hazardous actions (block hardcoded credentials) |
| **Observability & Tracing** 🔍 | Monitor model drift, token burn rates, architectural alignment | Comprehensive telemetry, granular traces, cost metering for audit decisions |

These components map to the 5 [[agent-components]] — the harness is the implementation layer that configures and integrates them into a production system.

## Deployment Readiness Checklist

Before deploying any agentic harness, verify:
- ✅ **System of Record**: Does the repository hold ultimate authority for state and progress?
- ✅ **Explicit Boundaries**: Does `AGENTS.md` define strict rules to prevent overreach?
- ✅ **Initialization Integrity**: Does `init.sh` ensure a stable environment before execution?
- ✅ **Victory Prevention**: Does `feature_list.json` force per-requirement verification?
- ✅ **Closed-Loop Verification**: Is there a mandatory "Verify & QA" phase with auto-fix loop?
- ✅ **State Continuity**: Does `claude-progress.md` provide clean handoff for the next session?

> If you answer "No" to any of these, your harness is not production-ready.

## The Role Shift

Harness engineering represents a shift from:
- ❌ "How do I write better prompts?"
- ✅ "How do I design better environments?"

The AI engineer's role is not prompt whisperer — it's **environment designer**. Build the system, not just the instruction.
---
- Related to [[testing-strategy]] — harness engineering applies automated testing as a mandatory gate for agentic workflows
- Related to [[fail-fast]] — shared philosophy: prevention over cure; catch issues before they compound
- Related to [[composition-root]] — both centralize control: Composition Root centralizes dependency wiring; harness centralizes agent behavior rules
- Implements [[technological-centaur]] — harness engineering provides the structural enforcement that makes the human+AI centaur model reliable
- Core to [[ai-native-engineering]] — harness primitives (AGENTS.md, feature_list.json, verification loops) are the structural enforcement layer for AI-native workflows
- Provides verification gates for [[agentic-development-life-cycle]] — each ADLC phase (Planning, Building, Testing, Review) uses harness primitives as checkpoints
- Related to [[context-engineering]] — AGENTS.md and context files are both harness primitives and context engineering artifacts; the disciplines overlap at the configuration layer
- Organizes [[agent-components]] — the harness is the implementation layer that configures the 5 components into a production system
- Enforces [[agent-loop]] — harness primitives ensure each stage of the Perceive-Plan-Act-Observe cycle completes before proceeding
- Related to [[agent-verification]] — deterministic hooks and guardrails are the final safety layer in agent verification
- Benchmark source: [[sources/learn-harness-engineering]] — walkinglabs' guide to closed-loop AI agent systems
- Benchmark source: [[sources/new-sdlc-vibe-coding]] — the 90% rule and 6-component production anatomy
