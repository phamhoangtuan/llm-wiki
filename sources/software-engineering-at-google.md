---
title: "Software Engineering at Google"
type: source
source_type: book
author: "Titus Winters, Tom Manshreck, and Hyrum Wright"
url: "https://abseil.io/resources/swe-book"
source_date: 2020
ingested: 2026-08-18
tags: [software-engineering, code-review, testing, CI-CD, build-systems, culture]
concepts: [software-construction, continuous-delivery, testing-strategy, technical-debt-management, staff-engineering]
---

## Summary

*Software Engineering at Google* frames software engineering as programming plus time: practices that keep a codebase useful as requirements, teams, and dependencies change. The notes emphasize review, testing, integration, build infrastructure, large-scale change, and a culture that makes knowledge transferable.

## Core Ideas

### Review for Correctness and Comprehension

Every change should receive human review, with mechanical checks running first. Small changes are easier to understand and safer to integrate. Review asks whether the code is correct, comprehensible, and consistent with local standards; questions about readability are valid correctness signals because unreadable code cannot be maintained reliably.

### Test Behavior Through Stable Interfaces

Prefer fast, deterministic unit tests and tests that use public APIs. State-based assertions usually survive refactoring better than interaction tests. High-fidelity fakes isolate complex dependencies, while flaky tests are defects that erode trust. Test code may favor DAMP (Descriptive And Meaningful Phrases) over aggressive deduplication.

### Integrate and Release in Small Batches

Trunk-based development, continuous integration, continuous delivery, feature flags, and predictable release trains reduce the risk of change. Faster is safer when each change is small, verified, and independently reversible.

### Make Builds and Large Changes Boring

Artifact-based builds, fine-grained modules, explicit dependency versions, and cacheable execution make large codebases tractable. Automated large-scale changes prevent migrations and refactors from becoming permanent bottlenecks.

### Build a Learning Organization

Psychological safety, servant leadership, deliberate delegation, canonical information sources, and rewards for knowledge sharing create self-sufficient teams. The goal is to avoid single points of failure in both systems and human knowledge.

## Connections

- Defines [[software-construction]] as the time-aware discipline of maintaining changeability.
- Defines [[concepts/continuous-delivery]] through small changes, trunk-based development, CI, flags, and release trains.
- Extends [[testing-strategy]] with public-API, state-based, fake-backed, deterministic tests.
- Connects [[concepts/technical-debt-management]] to automated large-scale changes and explicit dependencies.
