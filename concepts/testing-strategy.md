---
title: "Testing Strategy"
type: concept
tags: [python, testing, strategy, architecture]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
aliases: [test pyramid, API-first testing]
---

## Summary

A professional testing strategy focuses effort where it matters most — the API layer — while avoiding the brittleness of UI tests and the maintenance burden of database tests.

## The 4 Pillars

| Pillar | Description |
|---|---|
| **Simple** | Tests easy to write and read — serve as living documentation |
| **Rapid** | Start in seconds — minimize friction in dev cycle |
| **Effective** | Tight feedback loop — actionable failure info, reduce MTTR |
| **Scalable** | From single script to multi-layer enterprise system |

## API Layer: The Sweet Spot

| Layer | Recommendation | Why |
|---|---|---|
| UI/CLI Tests | ❌ Avoid | Brittle, slow, break on UI changes |
| API Tests | ✅ 70-80% effort | Validate core logic, stable interface, fast |
| DB Tests | ❌ Avoid | Implementation-specific, hard to maintain |
| Integration/E2E | ✅ 20-30% effort | Validate real-world flows |

## Key Principles

- Test the API layer first — it validates core logic without UI brittleness
- Use fixtures for setup, not copy-paste in each test
- Mock external dependencies with `autospec=True` to prevent stale interface bugs
- Integrate with CI: `tox` for multi-version, `pytest-cov` for coverage, GitHub Actions for automation

## Connections

- Informs [[pytest-basics]] — strategy guides what to test first
- Drives [[pytest-fixtures]] usage — fixtures enable clean API testing
- Drives [[pytest-mocking]] usage — mocking isolates API from external deps
- Drives [[pytest-plugins]] usage — coverage and parallel execution for CI
