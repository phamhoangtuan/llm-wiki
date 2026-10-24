---
title: "Secure System Design"
type: concept
tags: [security, reliability, architecture, least-privilege, supply-chain, devsecops]
created: 2026-08-18
updated: 2026-08-18
sources: [building-secure-and-reliable-systems]
aliases: [secure-by-design, security architecture]
---

## Summary

**Secure system design** makes security a property of architecture, code, delivery, and operations rather than a late review. It reduces the damage that a compromised component, bad configuration, or human mistake can cause.

## Design Rules

1. **Make boundaries explicit.** Treat every service interface as a security boundary; authenticate internal callers and keep the trusted computing base understandable.
2. **Partition failure domains.** Separate components and regions so one root cause cannot compromise the entire service.
3. **Use least privilege.** Give identities narrow, task-specific APIs instead of ambient authority or broad shell access. Prefer zero-touch, auditable automation for production changes.
4. **Prevent misuse by construction.** Use strong types for sensitive data, hardened frameworks for common controls, and established cryptographic libraries instead of custom crypto.
5. **Prove what runs.** Mandatory review, signed build provenance, dependency metadata, and admission controls connect source intent to deployable artifacts.
6. **Recover safely.** Fail closed where appropriate, shed load, rate-limit rollouts, and prevent rollback to known-vulnerable versions.

## Operating Model

Security is shared by developers, SREs, and managers. Hermetic tests, fuzzing, static and dynamic analysis, audit logs, and blameless postmortems make security a continuous feedback loop. See [[shift-left-security]] for lifecycle placement and [[concepts/site-reliability-engineering]] for the reliability counterpart.

## Connections

- Extends [[shift-left-security]] from early scanning to architecture, provenance, and recovery.
- Complements [[kubernetes-security]] through least-privilege RBAC, signed images, and admission enforcement.
- Uses [[testing-strategy]] for hermetic testing and fuzzing.
- Relates to [[microservices]] through service boundaries and failure isolation.
- Benchmark source: [[sources/building-secure-and-reliable-systems]].
