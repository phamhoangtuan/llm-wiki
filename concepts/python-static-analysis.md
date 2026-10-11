---
title: "Python Static Analysis"
type: concept
tags: [python, static-analysis, code-quality]
created: 2026-06-12
updated: 2026-06-12
sources: [intuitive-python]
aliases: [Black, Flake8, Mypy, Python Quality Trifecta]
---

# Python Static Analysis

Automated tools that inspect source code without executing it, catching errors, inconsistencies, and structural problems before they reach runtime or code review. The Python ecosystem's "quality trifecta" of formatter, linter, and type checker forms the foundation of professional Python development.

## The Three Tools

| Tool | Category | Philosophy |
|---|---|---|
| **Black** | Formatter | "Uncompromising" — zero configuration. Like Henry Ford: "Any color, as long as it's black." Ends all stylistic debates. |
| **Flake8** | Linter | Scans for logic errors, structural smells, and anti-patterns. Configurable per-project. |
| **Mypy** | Type Checker | Gradual typing with **optimistic** inference. Add annotations incrementally; catch type errors before execution. |

These tools should be integrated into CI pipelines — not as gates that block progress, but as automated reviewers that flag issues immediately.

## Critical Flake8 Error Codes

Understanding error codes prevents silent failures:

| Code | Name | Severity | What Happens |
|---|---|---|---|
| **F821** | Undefined Name | Crash | Variable used but never defined — guaranteed crash |
| **F403** | Wildcard Import | Namespace pollution | `from module import *` makes variable tracking impossible |
| **F601** | Duplicate Dict Keys | Silent override | Later value silently overwrites earlier one |
| **F811** | Redefinition | Test skip | Reusing the same name (e.g., two tests with same function name) — second silently replaces first |
| **B006** | Mutable Default Argument | Shared state | Using `[]` or `{}` as default argument creates a single object shared across all function calls — the classic Python trap |

## CI Integration Pattern

```yaml
# pre-commit hooks or CI pipeline
- black --check .
- flake8 .
- mypy .
```

The goal is not zero-config — it's **consistent config** that the team agrees on once, then automates. Black handles formatting; the team focuses energy on logic and architecture review.

## Gradual Typing with Mypy

Unlike languages with mandatory type systems (Go, Rust, Java), Python allows adding type annotations incrementally:

```python
# Untyped (still valid Python)
def calculate(x, y):
    return x + y

# Gradually typed
def calculate(x: int, y: int) -> int:
    return x + y
```

Type annotations serve dual purpose: static error detection AND living documentation for future maintainers.

---

- Core to [[python-professional-practices]] — part of the quality foundation
- Related to [[fail-fast]] — catches errors before they reach runtime
- Related to [[testing-strategy]] — complements testing with automated gates
- Related to [[code-quality-pillars]] — static analysis as automated quality enforcement
- Covered by [[sources/intuitive-python]] — David Muller's guide to the Black + Flake8 + Mypy trifecta
