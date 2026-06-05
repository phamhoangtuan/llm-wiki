---
title: "pytest Markers"
type: concept
tags: [python, testing, pytest, test-selection]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
---

## Summary

Markers categorize tests and control which ones run. Built-in markers handle common scenarios; custom markers enable project-specific test selection.

## Built-in Markers

| Marker | Purpose |
| --- | --- |
| `@pytest.mark.skip()` | Unconditionally skip a test |
| `@pytest.mark.skipif(condition)` | Skip if condition is true |
| `@pytest.mark.xfail()` | Expected failure — for known issues |
| Symbol | Meaning |
| `PASSED` | Test succeeded |
| `FAILED` | AssertionError |
| `SKIPPED` | Intentionally skipped |
| `XFAIL` | Expected failure, failed as predicted |
| `XPASS` | Expected failure, unexpectedly passed |
| `ERROR` | Exception outside test function (fixture/hook) |
---
- Extends [[pytest-basics]] — adds selective execution to discovery
- Related to [[testing-strategy]] — enables fast feedback loops in CI
- Benchmark source: [[sources/okken-python-testing-pytest]] — Okken's comprehensive pytest guide
