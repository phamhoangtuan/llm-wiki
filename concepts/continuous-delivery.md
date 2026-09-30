---
title: "Continuous Delivery"
type: concept
tags: [ci-cd, software-engineering, deployment, release-management, testing]
created: 2026-08-18
updated: 2026-08-18
sources: [software-engineering-at-google, the-accidental-cto]
aliases: [CD, continuous delivery, trunk-based development]
---

## Summary

**Continuous delivery** keeps software in a releasable state by integrating, testing, and deploying small changes through an automated path. It is not simply frequent deployment; it is a system that makes each change observable, constrained, and reversible.

## Practices

- Integrate on a shared trunk instead of maintaining long-lived branches.
- Run formatters, linters, tests, and static analysis before human review.
- Keep changes small so review and rollback remain cheap.
- Use feature flags to separate code deployment from feature activation.
- Release on a predictable train; missed work waits rather than triggering a risky rush.
- Build immutable, reproducible artifacts with explicit dependencies.
- Use containers and GitOps to reduce environment drift.
- Roll out with canaries, rate limits, and fast rollback paths.

## Safety Condition

"Faster is safer" only when the delivery system has feedback and control. Continuous delivery without reliable tests, observability, or rollback merely automates failure.

## Connections

- Implements risk controls from [[deployment-strategies]] and [[concepts/site-reliability-engineering]].
- Supports [[technical-debt-management]] by making migrations incremental.
- Builds on [[containerization]] and [[kubernetes-architecture]].
- Benchmark sources: [[sources/software-engineering-at-google]] and [[sources/the-accidental-cto]].
