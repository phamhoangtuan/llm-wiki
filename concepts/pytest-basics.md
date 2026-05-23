---
title: "pytest Basics"
type: concept
tags: [python, testing, pytest, fundamentals]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
aliases: [pytest fundamentals, test discovery]
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
|---|---|---|---|
| File | `test_*.py` or `*_test.py` | `test_user.py` | `user.py` |
| Function | starts with `test_` | `test_login()` | `check_login()` |
| Class | starts with `Test` | `TestUserAPI` | `UserTests` |

Warning: Non-compliant names are silently skipped — a dangerous silent failure.

## Running Tests

```bash
pytest                    # run all tests
pytest -v                 # verbose mode
pytest --tb=no            # hide tracebacks
pytest test_file.py::test_function  # run specific test
pytest -m smoke           # run tests with "smoke" marker
```

## Connections

- Foundation for [[pytest-fixtures]], [[pytest-parametrization]], [[pytest-markers]]
- Contrasts with [[unittest]] — no boilerplate classes needed
- Related to [[pytest-assertions]] — the assert rewriting mechanism
