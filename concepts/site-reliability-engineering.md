---
title: "Site Reliability Engineering"
type: concept
tags: [reliability, SRE, operations, observability, SLO, distributed-systems]
created: 2026-08-18
updated: 2026-08-18
sources: [site-reliability-engineering, building-secure-and-reliable-systems]
aliases: [SRE, site reliability]
---

## Summary

**Site Reliability Engineering (SRE)** applies software engineering to production operations. It replaces heroics with measurable reliability targets, automation, failure containment, and learning after incidents. The practical goal is to scale human operations more slowly than system load.

## Reliability Contract

- **SLI** — a measurement of user-visible service behavior, such as latency, availability, or error rate.
- **SLO** — the target for an SLI over a defined period.
- **Error budget** — the allowed unreliability, commonly `1 - SLO`; it makes the pace-versus-stability trade-off explicit.

SLOs are useful only when connected to decisions: spend the budget on safe change, slow releases when the budget is exhausted, and choose indicators users actually experience.

## Failure Containment

Reliable systems assume components fail:

- Load shedding rejects work early when capacity is exhausted.
- Graceful degradation serves a reduced result instead of taking down the whole system.
- Exponential backoff with jitter prevents retry storms.
- Deadline propagation stops doomed work in downstream services.
- Failure domains, canaries, and rate-limited rollouts limit blast radius.
- Backups, soft deletion, and independent validation protect recoverability; replication alone is not a backup.

## Operational Practice

Measure services with metrics, logs, and traces; automate repetitive work; and keep toil below half of engineering time. Stress tests, canary tests, and documented negative results turn reliability into an empirical discipline. Blameless postmortems ask which system conditions made the incident possible rather than who deserves blame.

## Connections

- Supplies targets and incident practice for [[observability]].
- Extends [[scalable-architecture]] with failure containment and recoverability.
- Complements [[secure-system-design]] because security and reliability share boundaries, automation, and recovery controls.
- Uses [[deployment-strategies]] for canary and rate-limited rollout safety.
- Benchmark sources: [[sources/site-reliability-engineering]] and [[sources/building-secure-and-reliable-systems]].
