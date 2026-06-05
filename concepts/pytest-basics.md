---
title: "pytest Basics"
type: concept
tags: [python, testing, pytest, fundamentals]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
---

## Summary

pytest is a command-line testing framework for Python that automatically discovers, runs, and reports test results. Its core philosophy is simplicity and readability — "Tests are easy to read" (stated twice by the author for emphasis).

## Key Ideas

- **Convention over configuration**: Follow naming rules and pytest finds tests automatically

  - Files: `test_*.py` or `*_test.py`

  - Functions: `test_*()`

  - Classes: `Test*` (no `__init__`)

- **Plain assert**: Use Python's built-in `assert` — no `assertEqual()`, `assertTrue()`, etc.
- **Virtual environment**: Always use `venv` to avoid dependency conflicts
- **Auto-discovery**: pytest searches current directory and subdirectories for test files

## Test Discovery Rules

| Type | Rule | Valid | Invalid |
| --- | --- | --- | --- |
| File | `test_*.py` or `*_test.py` | `test_user.py` | `user.py` |
| Function | starts with `test_` | `test_login()` | `check_login()` |
| Class | starts with `Test` | `TestUserAPI` | `UserTests` |
---
- Foundation for [[pytest-fixtures]] — reusable setup/teardown via dependency injection
- Foundation for [[pytest-parametrization]] — run one test with multiple data sets
- Foundation for [[pytest-markers]] — tag tests for selective execution
- Related to [[pytest-assertions]] — the assert rewriting mechanism
- Related to [[pytest-configuration]] — pyproject.toml and pytest.ini setup
- Related to [[pytest-test-results]] — result symbols: PASSED, FAILED, SKIPPED, XFAIL, XPASS, ERROR
- Benchmark source: [[sources/okken-python-testing-pytest]] — Okken's comprehensive pytest guide
