---
title: "pytest Markers"
type: concept
tags: [python, testing, pytest, test-selection]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
aliases: [pytest marks, test tags]
---

## Summary

Markers categorize tests and control which ones run. Built-in markers handle common scenarios; custom markers enable project-specific test selection.

## Built-in Markers

| Marker | Purpose |
|---|---|
| `@pytest.mark.skip()` | Unconditionally skip a test |
| `@pytest.mark.skipif(condition)` | Skip if condition is true |
| `@pytest.mark.xfail()` | Expected failure — for known issues |

## Test Result Symbols

| Symbol | Meaning |
|---|---|
| `PASSED` | Test succeeded |
| `FAILED` | AssertionError |
| `SKIPPED` | Intentionally skipped |
| `XFAIL` | Expected failure, failed as predicted |
| `XPASS` | Expected failure, unexpectedly passed |
| `ERROR` | Exception outside test function (fixture/hook) |

## Custom Markers

```python
@pytest.mark.slow
def test_large_dataset():
    ...

@pytest.mark.integration
def test_api_call():
    ...
```

Register in `pyproject.toml` or `pytest.ini` to avoid warnings:

```toml
[tool.pytest.ini_options]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests requiring external services",
]
```

Run specific subsets: `pytest -m "not slow"`, `pytest -m integration`.

## Connections

- Extends [[pytest-basics]] — adds selective execution to discovery
- Related to [[testing-strategy]] — enables fast feedback loops in CI
