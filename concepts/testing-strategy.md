---
title: "Testing Strategy"
type: concept
tags: [python, testing, strategy, architecture, tdd]
created: 2026-05-23
updated: 2026-06-27
sources: [okken-python-testing-pytest, tdd-python-percival, good-code-bad-code, clean-code-principles-patterns-silen]
---

## Summary

A professional testing strategy focuses effort where it matters most — the API layer — while avoiding the brittleness of UI tests and the maintenance burden of database tests.

## The 4 Pillars

| Pillar | Description |
| --- | --- |
| **Simple** | Tests easy to write and read — serve as living documentation |
| **Rapid** | Start in seconds — minimize friction in dev cycle |
| **Effective** | Tight feedback loop — actionable failure info, reduce MTTR |
| **Scalable** | From single script to multi-layer enterprise system |

| Layer | Recommendation | Why |
| --- | --- | --- |
| UI/CLI Tests | ❌ Avoid | Brittle, slow, break on UI changes |
| API Tests | ✅ 70-80% effort | Validate core logic, stable interface, fast |
| DB Tests | ❌ Avoid | Implementation-specific, hard to maintain |
| Integration/E2E | ✅ 20-30% effort | Validate real-world flows |
---
- Informs [[pytest-basics]] — strategy guides what to test first
- Drives [[pytest-fixtures]] — usage — fixtures enable clean API testing
- Drives [[pytest-mocking]] — usage — mocking isolates API from external deps
- Drives [[pytest-plugins]] — usage — coverage and parallel execution for CI
- Enabled by [[dependency-injection]] — DI provides the loose coupling that makes testing practical
- Informed by [[tdd-methodology]] — TDD provides the Red-Green-Refactor discipline and Outside-In workflow
- Guided by [[functional-testing]] — functional tests form the outer verification loop for end-to-end correctness
- Related to [[harness-engineering]] — harness engineering's closed-loop verification applies rigorous testing to AI agents
- Informs [[code-quality-pillars]] — pillar 6 (testable) structures testing into 3 levels: unit, integration, E2E
- Benchmark source: [[sources/okken-python-testing-pytest]] — Okken's comprehensive pytest guide
- Benchmark source: [[sources/tdd-python-percival]] — Percival's TDD with Django and Selenium
- Benchmark source: [[sources/clean-code-principles-patterns-silen]] — Silén on testing pyramid, BDD with Gherkin, and non-functional testing (performance, stability, security)
