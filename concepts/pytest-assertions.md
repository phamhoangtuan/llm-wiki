---
title: "pytest Assertions"
type: concept
tags: [python, testing, pytest, assertions]
created: 2026-05-23
updated: 2026-05-23
sources: [okken-python-testing-pytest]
aliases: [assert rewriting, assertion introspection]
---

## Summary

Assert rewriting is pytest's secret weapon — it intercepts `assert` statements at runtime, analyzes the expression, and generates rich diffs when assertions fail. You get framework-specific assertion quality without learning new syntax.

## How It Works

```python
# Plain Python assert — no framework methods needed
assert actual_result == expected_result
```

When it fails:

```
E       assert (3, 2, 1) == (1, 2, 3)
E         Full diff:
E         - (3, 2, 1)
E         ?  ^     ^
E         + (1, 2, 3)
E         ?  ^     ^
```

Carets point to exact failure indices. Side-by-side diff shows what changed.

## Comparison with unittest

```python
# unittest: verbose, hard to read
self.assertEqual(actual_result, expected_result, "Error message")

# pytest: clean, natural Python
assert actual_result == expected_result
```

## Connections

- Core to [[pytest-basics]] — the foundation of pytest's simplicity
- Related to [[pytest-test-results]] — assertion failures produce FAILED results
