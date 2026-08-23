---
title: "pytest Fixtures"
type: concept
tags: [python, testing, pytest, dependency-injection]
created: 2026-05-23
updated: 2026-06-15
sources: [okken-python-testing-pytest]
---

## Summary

Fixtures are pytest's killer feature — reusable setup/teardown logic via dependency injection. They replace `setUp()`/`tearDown()` from unittest with a more flexible, composable system.

## How It Works

A fixture is any function decorated with `@pytest.fixture`. Tests receive fixtures as function arguments — dependencies are declared explicitly.

```
@pytest.fixture
def db_connection():
    conn = create_connection()
    yield conn
    conn.close()  # teardown after test

def test_query(db_connection):
    result = db_connection.execute("SELECT 1")
    assert result == 1
```
## Fixture Scopes

| Scope | Lifecycle | Use Case |
| --- | --- | --- |
| `function` (default) | Runs for each test | Isolated test data |
| `class` | Once per test class | Shared class setup |
| `module` | Once per module | Module-level resources |
| `session` | Once per entire run | Database connections, config |
---
- Extends [[pytest-basics]] — the next level after plain tests
- Complements [[pytest-parametrization]] — fixtures can be parametrized
- Used by [[pytest-mocking]] — mock objects often provided as fixtures
- Related to [[testing-strategy]] — fixtures enable clean API layer testing
- Implements [[dependency-injection]] — pytest's fixture system is DI applied to test setup and teardown
- Benchmark source: [[sources/okken-python-testing-pytest]] — Okken's comprehensive pytest guide
