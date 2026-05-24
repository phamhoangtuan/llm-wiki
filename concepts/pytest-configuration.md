---
title: "pytest Configuration"
type: concept
tags: [python, testing, pytest, configuration]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
---

## Summary

pytest configuration unifies flags and settings across a team. Modern pytest supports native TOML configuration in `pyproject.toml`.

## pyproject.toml Configuration

```
[tool.pytest.ini_options]
addopts = "-v --tb=short"
testpaths = ["tests"]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests requiring external services",
]
```
## pytest.ini (Legacy)

```
[pytest]
addopts = -v --tb=short
markers =
    slow: marks tests as slow
    integration: marks tests requiring external services
```
## Common Settings

| Setting | Purpose |
| --- | --- |
| `addopts` | Default command-line flags |
| `testpaths` | Directories to search for tests |
| `markers` | Register custom markers |
| `filterwarnings` | Control warning behavior |
---
- Extends [[pytest-basics]] — configuration affects discovery and execution
- Related to [[pytest-plugins]] — plugins are configured here
- Related to [[pytest-markers]] — custom markers must be registered
