---
title: "pytest Parametrization"
type: concept
tags: [python, testing, pytest, data-driven]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
aliases: [parametrize, data-driven testing]
---

## Summary

Parametrization allows running the same test function with multiple input data sets, eliminating copy-paste test methods.

## How It Works

```python
@pytest.mark.parametrize("input,expected", [
    (2, 4),
    (3, 9),
    (-1, 1),
])
def test_square(input, expected):
    assert input ** 2 == expected
```

Each tuple generates a separate test case. pytest reports each individually in the output.

## Multiple Parameters

```python
@pytest.mark.parametrize("name,age,expected", [
    ("Alice", 30, True),
    ("Bob", 17, False),
])
def test_is_adult(name, age, expected):
    assert is_adult(age) == expected
```

## Connections

- Builds on [[pytest-basics]] — extends plain test functions
- Complements [[pytest-fixtures]] — indirect parametrization offloads setup to fixtures
- Related to [[testing-strategy]] — enables thorough API testing with minimal code
