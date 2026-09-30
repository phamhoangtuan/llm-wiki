---
title: "Building Secure and Reliable Systems"
type: source
source_type: book
author: "Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, and Adam Stubblefield"
url: "https://sre.google/books/building-secure-and-reliable-systems/"
source_date: 2020
ingested: 2026-08-18
tags: [security, reliability, secure-by-design, least-privilege, supply-chain, testing]
concepts: [secure-system-design, site-reliability-engineering, shift-left-security, testing-strategy, kubernetes-security]
---

## Summary

*Building Secure and Reliable Systems* treats security and reliability as emergent properties of architecture, implementation, and operations. They cannot be bolted on after launch. The book translates Google's practices into a lifecycle that begins with understandable system boundaries and continues through automated change, testing, recovery, and blameless learning.

## Core Ideas

### Make Boundaries and Failure Domains Explicit

Decomposition can shrink the trusted computing base, but every interface remains a security boundary. Internal callers are not automatically trusted. Mutual authentication, narrow APIs, and independent failure domains reduce the blast radius of both compromise and operational mistakes.

### Remove Ambient Authority

Use least privilege and small functional APIs instead of broad administrative access. Zero Touch Production moves changes from direct human interaction toward automation, while risk classification and multi-party authorization protect high-impact operations.

### Prevent Classes of Bugs by Construction

Strong types for sensitive values, hardened application frameworks, and misuse-resistant cryptographic libraries are safer than relying on every caller to remember the right escape, validation, or cryptographic detail. The guidance is explicit: use established primitives and do not roll your own cryptography.

### Verify the Software You Ship

Hermetic unit and integration tests, fuzzing, static analysis, dynamic sanitizers, mandatory review, signed build provenance, and admission controls create a chain of evidence from source to production. This is [[secure-system-design]] applied to the software supply chain.

### Fail Safely and Recover Deliberately

Systems should fail closed where security is at stake, shed load under pressure, and degrade gracefully when lower-quality service is preferable to total failure. Fast rollouts still need rate limits, and minimum acceptable security versions prevent malicious rollback to vulnerable artifacts.

### Security Is Shared Work

Blameless postmortems and shared ownership prevent security from becoming a specialist-only gate. Developers, SREs, and managers all participate in creating secure and reliable systems.

## Connections

- Defines [[secure-system-design]] as an architectural and operational discipline.
- Extends [[shift-left-security]] with provenance, fuzzing, typed security, and admission controls.
- Complements [[concepts/site-reliability-engineering]] through shared failure, recovery, and postmortem practices.
- Reinforces [[testing-strategy]] with hermetic testing, fuzzing, and runtime analysis.
