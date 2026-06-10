---
title: "Learn Harness Engineering"
type: source
source_type: book
author: "walkinglabs"
url: "https://walkinglabs.github.io/learn-harness-engineering/en/"
source_date: 2025-01-01
ingested: 2026-05-31
created: 2026-05-31
updated: 2026-05-31
tags: [ai-engineering, agents, harness, verification, reliability]
concepts: [harness-engineering]
---

## Summary

An open guide to **Harness Engineering** — a discipline for building reliable, closed-loop systems that constrain and verify AI agent behavior. Rather than trying to make models "smarter," harness engineering focuses on structural enforcement: explicit rules, state management, granular verification, and systematic feedback loops that turn intelligent-but-unpredictable agents into trustworthy engineering collaborators.

## Core Message

> Raw intelligence without structural enforcement is a liability, not an asset. The harness doesn't make the model smarter — it establishes a closed-loop working system where the model can succeed reliably.

## The Problem: Intelligence ≠ Reliability

| Model Capability | Systemic Failure (Without Harness) |
|---|---|
| Fast code generation | Loss of continuity in long, multi-session tasks |
| Advanced reasoning | Overreach & under-finish: drifts beyond scope, doesn't complete |
| Large context windows | Declare victory too early: stops when code "looks good," skips testing |

## Four Harness Primitives

| Artifact | Role | Core Benefit |
|---|---|---|
| `AGENTS.md` | **Rules**: Clear Objective + constraints + boundaries | Prevents overreach — agent stays in scope |
| `init.sh` | **Environment Setup**: Reproducible starting point | Prevents building on broken foundations |
| `feature_list.json` | **Requirement Tracking**: Granular checklist | Prevents "declare victory too early" — must tick each item |
| `claude-progress.md` | **State Persistence**: Progress + context for next session | Resolves loss of continuity — repo, not model memory, is System of Record |

## Five-Phase Agentic Workflow

```
1. GOAL SETTING → Agent reads AGENTS.md, internalizes rules
2. INITIALIZATION → Execute init.sh, verify environment stability
3. EXECUTION → Perform tasks, update feature_list.json, reconcile state
4. FEEDBACK → Monitor CLI/logs, run test suite
   ❌ Failed? → Auto-fix loop → re-verify
   ✅ Passed? → Proceed
5. STATE PERSISTENCE → Document in claude-progress.md for clean handoff
```

Agent cannot proceed to Phase 5 until test suite returns "Passed." Verification is mandatory.

## Three Failure Modes Addressed

| Failure | Root Cause | Harness Solution |
|---|---|---|
| **Declares "done" too early** | No granular verification | `feature_list.json` forces per-requirement sign-off |
| **Loss of continuity** | Model memory is ephemeral | `claude-progress.md` persists state in repo |
| **Builds on broken foundation** | No stable starting point | `init.sh` ensures consistent, verified environment |

## Five Key Insights

1. **Harness doesn't make the model smarter** — it provides structure for the model to succeed reliably
2. **"One giant instruction file" is a fatal flaw** — mega-prompts cause instruction drift; use atomic primitives
3. **Observability is for the agent, not just humans** — agent needs CLI outputs, logs, test results to self-correct
4. **Repository = System of Record, not chat history** — state must live in files, not in conversation memory
5. **Verification loop is the heart of reliability** — `Encounter Issues → Auto-fix → Verify → (Pass? Done : Loop)`

## The Role Shift

From "Prompt Whisperer" to "Environment Designer." The engineer's job is not to craft better prompts — it's to design better systems.
