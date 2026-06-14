---
title: "Intuitive Python"
type: source
source_type: book
author: "David Muller"
url: ""
source_date: 2024-01-01
ingested: 2026-06-12
created: 2026-06-12
updated: 2026-06-12
tags: [python, software-engineering, static-analysis, debugging, concurrency]
concepts: [python-static-analysis, python-debugging-pdb, python-standard-library, python-concurrency, python-repl, python-professional-practices]
---

# Intuitive Python — David Muller (137 pages)

A practical guide to moving from "code that runs" to "production-grade Python" by leveraging Python's batteries-included ecosystem. The core thesis: becoming professional isn't about learning more syntax — it's about replacing guessing with **grounded intuition** through the right tools.

## The Trifecta: Black + Flake8 + Mypy

Professional code is consistent, not error-free. The three static analysis tools form the quality foundation:

| Tool | Role | Philosophy |
|---|---|---|
| **Black** | Formatter | Uncompromising — zero config. Ends tabs-vs-spaces debates. |
| **Flake8** | Linter | Catches logic errors and structural smells before they reach runtime |
| **Mypy** | Type Checker | Gradual typing via annotations to catch errors statically |

Key Flake8 error codes: F821 (undefined name → crash), F403 (wildcard import → namespace pollution), F601 (duplicate dict keys → silent override), F811 (redefinition → test skip silently), B006 (mutable default argument → shared state trap).

All three should be integrated into CI as a "friend looking over your shoulder."

## Debugging: breakpoint() over print()

From Python 3.7+, `breakpoint()` replaces `import pdb; pdb.set_trace()`. The contrast:

| | print() | breakpoint()/pdb |
|---|---|---|
| **Proactive** | Must know what to print in advance | Explore state without knowing |
| **Interactive** | None | Query variables, test expressions live |
| **Efficiency** | Restart code each time | Pause at exact line |

Essential PDB commands: `next` (n) — execute current line, `step` (s) — step into function, `pp` — pretty-print nested data with indentation, `where` (w) — full stack trace.

## Standard Library: Batteries Included

Don't rewrite what Python already gives you.

- **`collections.defaultdict`**: Eliminates `if key not in dict` checks. Auto-creates values for missing keys.
- **`collections.namedtuple`**: Replaces simple classes with immutable, readable data structures. `User(id=1, name='David')` instead of `<object at 0x7f3...>`.
- **`sqlite3`**: Every Python install has it. Use `:memory:` for ultra-fast ephemeral databases — perfect for testing and data processing without a DB server.

## Concurrency: Safety Over Speed

The race condition trap: two processes reading $8 simultaneously, each subtracting independently, leading to $13 withdrawn from an $8 account.

| Paradigm | Shared Memory | GIL Bound | Best For |
|---|---|---|---|
| **Threads** | Yes | Yes | I/O-bound (API calls, file reads, network) |
| **Processes** | No | No | CPU-bound (heavy computation, large data) |

Senior developers prioritize safety over perceived speed. Only use concurrency when truly necessary.

## The REPL: Living Laboratory

The Python console is a zero-cost sandbox for exploration:

- **`print(obj)`** → user-friendly string (may hide type). **`obj` + Enter** → `repr(obj)` → developer representation with exact type info.
- **`help()`**: Detailed docs with argument expectations.
- **`__doc__`**: Quick docstring access.
- **`dir()`**: List all attributes and methods — discover what an object can do.
- **`__mro__`**: Method Resolution Order in complex inheritance hierarchies.

Use `ipython` for better tab-completion and multi-line editing.

## Professional Development Policy

Three pillars for sustainable code:
1. **Readability**: Code is communication between humans.
2. **Accessibility**: Easy onboarding for non-specialists.
3. **Batteries-Included**: Leverage standard library to reduce error-prone boilerplate.

Dockerize environments to eliminate "works on my machine": `docker run --rm -v $(pwd):/usr/src/code -w /usr/src/code python:3.8.8 /bin/bash`

## 4-Week Upgrade Path

- **Week 1**: Install Black, Flake8, Mypy; configure pre-commit hooks; learn F821, F403, B006
- **Week 2**: Replace all `print()` debug with `breakpoint()`; practice `next`, `step`, `pp`, `where`; explore an unfamiliar library with `dir()` and `help()`
- **Week 3**: Refactor dicts to `defaultdict`; replace simple classes with `namedtuple`; use `sqlite3 :memory:` for temporary data processing
- **Week 4**: Dockerize current project; write Docker run documentation; find and fix mutable default arguments
