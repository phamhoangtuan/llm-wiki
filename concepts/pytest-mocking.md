---
title: "pytest Mocking"
type: concept
tags: [python, testing, pytest, mocking, isolation]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
---

## Summary

Mocking isolates tests from external dependencies (APIs, databases, files). pytest provides two approaches: the built-in `monkeypatch` fixture and the `pytest-mock` plugin wrapping `unittest.mock`.

## monkeypatch (Built-in)

```
def test_env_var(monkeypatch):
    monkeypatch.setenv("DATABASE_URL", "sqlite:///test.db")
    assert get_db_url() == "sqlite:///test.db"
```
Safely modifies objects and environment variables — automatically restored after test.

## pytest-mock Plugin

```
def test_api_call(mocker):
    mock_response = mocker.patch("requests.get")
    mock_response.return_value.json.return_value = {"id": 1}
    result = fetch_user(1)
    assert result["id"] == 1
```
## autospec — Defense in Depth

```
from unittest.mock import create_autospec

# Mock must match real signature — errors if interface changes
mock_db = create_autospec(Database, instance=True)
mock_db.get_user.return_value = {"id": 1}
```
Prevents "green tests that mask real bugs" — a major risk when refactoring large systems.

---
- Complements [[pytest-fixtures]] — mocks are often provided as fixture return values
- Related to [[testing-strategy]] — essential for API layer isolation
- Benchmark source: [[sources/okken-python-testing-pytest]] — Okken's comprehensive pytest guide
