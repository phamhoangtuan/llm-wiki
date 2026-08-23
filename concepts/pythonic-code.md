---
title: "Pythonic Code"
type: concept
tags: [python, programming, idioms, code-quality]
created: 2026-08-06
updated: 2026-08-06
sources: [fluent-python]
aliases: [pythonic, python-idioms]
---

## Summary

**Pythonic code** is code that uses Python's language idioms to be consistent, expressive, and effective — not just code that happens to run in Python. It's the difference between writing Python with a Java/C++ "accent" and writing code that feels native to the language. The concept is central to Luciano Ramalho's Fluent Python.

## Pythonic vs Non-Pythonic

| Non-Pythonic (translated) | Pythonic (native) |
| --- | --- |
| Manual index loops | `for item in collection` |
| `if len(lst) == 0` | `if not lst` |
| `if x in d.keys()` | `if x in d` |
| `list(map(f, data))` | `[f(x) for x in data]` |
| Building your own iterator class | Generator function with `yield` |
| Manually closing resources | `with` statement (context manager) |

## Core Principles

1. **Use what's available**: Reach for built-ins (`collections`, `functools`, `itertools`) and standard library before building custom solutions. Python has "batteries included."

2. **Follow the data model**: Implement dunder methods so your objects behave like Python natives. If your class is a container, implement `__getitem__` — suddenly it works with `for`, `in`, slicing, and `len()`. See [[python-data-model]].

3. **Embrace duck typing**: Code against what objects do (their methods), not what they are (their type). Check behavior at interfaces, not inheritance hierarchies.

4. **Prefer simple over clever**: Pythonic code is readable first. `import this` in your REPL for the Zen of Python.

## Goose Typing

A refinement of duck typing. Use Abstract Base Classes from `collections.abc` (`Sequence`, `Mapping`, `Iterable`) to make protocols explicit while keeping flexibility:

```python
from collections.abc import Sequence

def process(items: Sequence):
    # Accepts list, tuple, str, or anything sequence-like
    return items[0]
```

This is more precise than bare duck typing but less rigid than class inheritance — "if it implements the Sequence protocol, it's a Sequence."

## Why It Matters

Pythonic code is more than aesthetics. It leverages Python's C-level optimizations (e.g., `len()` on a list is O(1) because it reads a cached field via `__len__`, not by counting). It's more readable to other Python programmers who expect the idioms. And it composes better — data model protocols like `__iter__` chain together naturally.

---

- Built on [[python-data-model]] — dunder methods and protocols are the mechanism behind Pythonic behavior
- Leverages [[python-standard-library]] — "batteries included" means reaching for stdlib before custom code
- Source: [[sources/fluent-python]] — the definitive guide to Pythonic programming
