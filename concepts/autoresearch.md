---
title: "Autoresearch"
type: concept
tags: [ai-engineering, agents, ml-experimentation, autonomy, loop]
created: 2026-08-06
updated: 2026-08-06
sources: [graph-engineering-karpathy]
aliases: [karpathy-loop, autonomous-research, ratchet-loop]
---

## Summary

**Autoresearch** is Andrej Karpathy's autonomous ML experimentation system. An agent is placed inside an executable research harness with a mutable training program, a fixed evaluation metric, a time budget, and a Git history. The agent proposes one change at a time, runs a short experiment, and keeps only metric improvements — a **ratchet loop** that converts hypotheses, failures, and parameter interactions into a machine-readable experiment lineage.

~86,000 GitHub stars, ~12,500 forks. ~700 experiments in two days, ~20 retained optimizations from a ~630-line codebase.

## The Ratchet Loop

```
LOOP FOREVER:
1. Read current train.py and recent history
2. Propose one motivated change (guided by program.md)
3. Commit the candidate change
4. Run training for ~5 minutes
5. Measure val_bpb and peak memory
6. If crash: inspect, fix if mechanical, else revert
7. If val_bpb improves: keep commit
   Else: reset to previous retained commit
8. Record result and continue without asking human
```

Pseudocode:

```python
def ratchet_loop(inspect, propose, apply, evaluate,
                 keep, revert, better, baseline):
    history, current = [], baseline
    while True:
        state = inspect()
        change = propose(state)
        commit = apply(change)
        try:
            score = evaluate()
        except Exception as exc:
            revert(commit)
            history.append(Trial(commit, change, None, "crash", str(exc)))
            continue
        if better(score, current):
            keep(commit); current = score
            history.append(Trial(commit, change, score, "kept", ""))
        else:
            revert(commit)
            history.append(Trial(commit, change, score, "reverted", ""))
```

## Three Central Files

1. **`prepare.py`** — fixed data preparation and evaluation utilities. Not modified by the agent.
2. **`train.py`** — the model, optimizer, hyperparameters, training loop. The experimental surface.
3. **`program.md`** — describes the research process, constraints, metric, logging rules, and autonomy policy.

## Why It Works: Four Conditions

The system is unusually compatible with autonomous agents because:

1. **Verifiable output** — training produces a measurable validation result
2. **Reversible action** — `git reset` returns to the last retained state
3. **Short horizon** — ~5 minute runs create frequent feedback
4. **Bounded environment** — the narrow repository limits the action space

These four conditions form a reusable template for any autonomous agent loop.

## Programming the Program

`program.md` is **"programming the program"** — a natural-language control specification that configures an autonomous organization. It establishes: mutable and protected files, the metric and direction, experiment budget, run command, output parsing, crash handling, commit/revert rules, logging, human escalation policy, and exhaustion criteria.

This extends Karpathy's Software 3.0 concept: context and prompts become a programmable interface, and `program.md` adds a layer where natural language instructions configure autonomous behavior.

## Reported Results

~700 experiments over two days. 20 retained optimizations including: QK normalization scaling, value-embedding regularization, AdamW parameter tuning, batch-size changes, depth changes, embedding learning rate, RoPE base frequency, targeted weight decay, initialization scale, and warmdown settings.

The **architectural lesson** is more reliable than any one optimization: the loop converts human working memory (hypotheses, failures, parameter interactions) into a machine-readable, traversable history with parent state, code diff, metric, and keep/discard for every experiment.

## Relationship to Graph Engineering

Autoresearch is the entry point to [[graph-engineering]]. The loop generates a commit DAG — each experiment is a node with parent links forming a directed acyclic graph. When scaled to multiple agents exploring concurrently, this becomes the foundation for [[agent-hub]].

Karpathy calls recursive model improvement "the final boss battle" and says frontier labs will pursue it.

---

- Concrete implementation of [[agent-loop]] — the generic perceive-plan-act-observe cycle specialized for ML experimentation
- Foundation for [[agent-hub]] — scales the single loop to concurrent multi-agent exploration
- Entry point to [[graph-engineering]] — the loop generates the commit DAG
- Extends [[software-3]] — `program.md` as natural-language programming of autonomous behavior
- Source: [[sources/graph-engineering-karpathy]]
