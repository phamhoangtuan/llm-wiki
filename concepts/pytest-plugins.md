---
title: "pytest Plugins"
type: concept
tags: [python, testing, pytest, ecosystem]
created: 2026-05-23
updated: 2026-06-15
sources: [okken-python-testing-pytest]
---

## Summary

pytest has a rich plugin ecosystem (1000+ plugins on PyPI). Essential plugins extend pytest for production use.

## Essential Plugins

| Plugin | Purpose | Usage |
| --- | --- | --- |
| `pytest-cov` | Coverage reporting | `pytest --cov=src` |
| `pytest-xdist` | Parallel execution | `pytest -n auto` |
| `pytest-randomly` | Randomize test order | Detects hidden state dependencies |
| `pytest-mock` | Cleaner mocking API | `mocker` fixture |
| `pytest-asyncio` | Async test support | `@pytest.mark.asyncio` |
---
- Extends [[pytest-basics]] — plugins add capabilities to the core framework
- Related to [[pytest-configuration]] — plugins are configured in `pyproject.toml`
- Related to [[testing-strategy]] — coverage and parallel execution enable CI quality gates
