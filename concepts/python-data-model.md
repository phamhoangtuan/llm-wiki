---
title: "Python Data Model"
type: concept
tags: [python, programming, object-model, protocols]
created: 2026-08-06
updated: 2026-08-06
sources: [fluent-python]
aliases: [python-object-model, dunder-methods, special-methods]
---

## Summary

The **Python Data Model** (also called the object model) is the unifying framework that formalizes interfaces for Python's building blocks — sequences, iterators, functions, classes, and context managers. It's implemented through **dunder methods** (double-underscore, aka "special methods" or "magic methods") that allow user-defined objects to interact seamlessly with Python's core language features.

> Understanding the data model is the key to writing "Pythonic" code — code that feels native to the language rather than translated from another.

## How It Works

When you write `len(obj)`, Python calls `obj.__len__()`. When you write `obj[key]`, Python calls `obj.__getitem__(key)`. When you iterate with `for x in obj`, Python calls `obj.__iter__()`. The language syntax is a thin skin over these protocol methods.

This means any class that implements the right dunder methods **becomes** a Pythonic citizen: your custom objects can be iterated, indexed, hashed, compared, context-managed, and more — just like built-in types.

## Key Dunder Methods by Category

| Category | Methods | Triggered By |
| ---------- | --------- | ------------- |
| String representation | `__repr__`, `__str__` | `repr()`, `str()`, f-strings |
| Collection | `__len__`, `__getitem__`, `__contains__` | `len()`, `obj[i]`, `x in obj` |
| Iteration | `__iter__`, `__next__` | `for` loops, comprehensions |
| Comparison | `__eq__`, `__lt__`, `__gt__`, `__hash__` | `==`, `<`, `>`, sets, dict keys |
| Arithmetic | `__add__`, `__mul__`, `__sub__` | `+`, `*`, `-` |
| Callable | `__call__` | `obj()` — makes instance callable |
| Context manager | `__enter__`, `__exit__` | `with` blocks |
| Attribute access | `__getattr__`, `__setattr__` | `obj.attr`, `obj.attr = val` |

## Protocols and Duck Typing

The data model defines **protocols** — informal interfaces defined by sets of dunder methods. A "sequence" is anything that implements `__len__` and `__getitem__`. A "mapping" implements `__getitem__`, `__len__`, `__contains__`, `__iter__`, and a few others. You don't need to inherit from a specific base class — you just implement the methods.

This is **duck typing**: "If it walks like a duck and quacks like a duck, it's a duck." The data model is the formal specification of what "walks like a duck" means for each protocol.

## "Goose Typing"

Coined by Alex Martelli, **goose typing** uses Abstract Base Classes (ABCs) from `collections.abc` to make protocols explicit while keeping duck typing flexibility. `isinstance(obj, Sequence)` checks whether `obj` implements the Sequence protocol — not whether it inherits from a specific class. This is duck typing with a type-checkable interface.

See [[pythonic-code]].

---

- Foundation of [[pythonic-code]] — understanding the data model is prerequisite to writing Pythonic code
- Enables the Python [[python-standard-library|standard library's]] consistency — all built-in types follow the same protocols
- Source: [[sources/fluent-python]] — Part 1: The Data Model
