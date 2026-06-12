---
title: "Python REPL"
type: concept
tags: [python, repl, exploration]
created: 2026-06-12
updated: 2026-06-12
sources: [intuitive-python]
aliases: [Python interactive console, Python shell]
---

# Python REPL

The Read-Eval-Print Loop (REPL) is Python's interactive console — a zero-cost sandbox for exploring code, inspecting objects, and testing ideas without creating files. Professional developers treat the REPL as a **living laboratory** for discovery.

## repr vs print: The Developer's Secret Language

The most important REPL distinction:

| Action | Returns | Target Audience |
|---|---|---|
| `print(obj)` | `str(obj)` — user-friendly, may hide type info | End users |
| `obj` + Enter | `repr(obj)` — developer representation with exact type | Developers |

```python
>>> import datetime
>>> t = datetime.time(8, 12)
>>> print(t)
08:12:00                    # Looks like a string
>>> t
datetime.time(8, 12)        # Shows exact type and constructor
```

`repr` reveals the object's true nature — critical when debugging unexpected behavior or exploring unfamiliar libraries.

## Four X-Ray Vision Tools

When encountering an unfamiliar object, these tools reveal its internal structure:

| Tool | Purpose | Example |
|---|---|---|
| **`help(obj)`** | Full documentation with argument details | `help(str.upper)` |
| **`obj.__doc__`** | Quick docstring access | `print(str.upper.__doc__)` |
| **`dir(obj)`** | List all attributes and methods | `dir([])` → all list methods |
| **`obj.__mro__`** | Method Resolution Order — inheritance hierarchy | `bool.__mro__` → `(bool, int, object)` |

## REPL as Discovery Tool

The REPL isn't just for running commands — it's for **exploration**:

```python
>>> import requests  # Unfamiliar library
>>> dir(requests)     # What can it do?
>>> help(requests.get) # How do I use get()?
>>> resp = requests.get('https://api.example.com')
>>> type(resp)        # What did I get back?
>>> dir(resp)         # What methods does the response have?
>>> resp.__dict__     # What's inside?
```

This exploration loop — `dir()` → `help()` → `type()` → `__dict__` — lets you understand any object or library without reading full documentation.

## Pro Tips

- Use **`ipython`** instead of the default console for tab-autocompletion, better multi-line editing, and magic commands (`%timeit`, `%debug`)
- When you see the `...` prompt, the REPL is waiting for you to complete multi-line logic (like a function definition or loop)
- For production code, use the `inspect` module instead of REPL exploration tools
- The REPL's zero-cost-of-failure makes it ideal for testing ideas before committing them to files

---

- Related to [[python-debugging-pdb]] — shares the interactive exploration mindset
- Related to [[python-professional-practices]] — professional exploration workflow
- Related to [[python-standard-library]] — the `inspect` module is the production equivalent of REPL exploration
