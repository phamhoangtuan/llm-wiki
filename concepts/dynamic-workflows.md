---
title: "Dynamic Workflows"
type: concept
tags: [ai-engineering, agents, orchestration, anthropic, parallelism]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: []
---

## Summary

**Dynamic Workflows** is an Anthropic feature (2026) where Claude generates a JavaScript orchestration program for the current task, rather than requiring the developer to write a static fan-out script. The generated script spawns sub-agents with fresh contexts, gathers results, filters, re-dispatches, and synthesizes — collapsing what was previously a developer task into a single model call that produces the workflow itself.

## How It Works

Instead of writing orchestration code, the developer triggers workflow generation. Claude writes JavaScript that:

```javascript
const files = await tools.glob("src/**/*.ts");
const audits = await gather(
  files.map((file) =>
    spawn("auditor", {
      file,
      instructions: "Inspect for race conditions. Return JSON."
    })
  ),
  { concurrency: 16 }
);
const suspicious = audits.filter((r) => r.confidence >= 0.70);
const reviews = await gather(
  suspicious.map((r) =>
    spawn("reviewer", {
      report: r,
      instructions: "Try to refute this finding."
    })
  ),
  { concurrency: 16 }
);
return await spawn("synthesizer", {
  audits, reviews,
  instructions: "Produce one cited report."
});
```

## Key Specifications

- Up to 16 concurrent sub-agents
- Hard cap of 1,000 sub-agents per workflow
- Fresh context for each sub-agent (no shared transcript pollution)
- Intermediate state held in script variables
- Triggered via the word "workflow" or ultracode mode

## From "You Build" to "Claude Builds"

The 2024 guidance says engineers should build simple workflows. The 2026 feature says Claude can build a workflow on the fly. This changes the abstraction boundary but does **not** remove engineering responsibility. The human still defines:

- The objective
- Files in scope
- Output contract
- Permissions
- Verification policy
- Concurrency and token budget
- Rollback rule
- Evidence required for synthesis

## Cost Consideration

Large fan-out consumes tokens quickly. A 1,000-sub-agent run can cost tens of dollars. Parallel workers also create correlated errors — a verification wave helps only if reviewers have a different prompt, evidence set, or role.

## Bun Runtime Port

A notable demonstration: approximately 750,000 lines of Zig ported to Rust in 11 days using Dynamic Workflows, with 99.8% tests passing. The workflow decomposed the port into parallelizable units, dispatched sub-agents for each, and synthesized results.

---

- Implements the swarm pattern in [[graph-engineering]] — generated orchestration for parallel exploration
- Related to [[agent-hub]] — both enable concurrent agent work, but Dynamic Workflows generate the orchestration script dynamically
- Contrasts with static [[agent-loop]] — the loop is fixed; dynamic workflows adapt orchestration per task
- Source: [[sources/graph-engineering-karpathy]]
