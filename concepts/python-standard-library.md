---
title: "Python Standard Library"
type: concept
tags: [python, standard-library]
created: 2026-06-12
updated: 2026-06-12
sources: [intuitive-python]
aliases: []
---

# Python Standard Library

Python's "batteries-included" philosophy: a rich set of built-in modules that solve common problems without external dependencies. Professional Python developers reach for standard library tools before writing custom code or pulling in third-party packages.

## collections: Cleaner Data Structures

### defaultdict — Eliminate Key Checks

The classic pattern of checking whether a key exists before appending is error-prone boilerplate:

```python
# ❌ Manual key checking
if key not in data:
    data[key] = []
data[key].append(value)

# ✅ defaultdict: auto-creates missing keys
from collections import defaultdict
data = defaultdict(list)
data[key].append(value)  # No KeyError, ever
```

`defaultdict` accepts any callable as factory: `defaultdict(int)` for counters, `defaultdict(set)` for unique collections, `defaultdict(lambda: "default")` for custom defaults.

### namedtuple — Immutable Lightweight Objects

Replace simple data-holder classes with `namedtuple`:

```python
from collections import namedtuple
User = namedtuple('User', ['id', 'name', 'email'])
u = User(id=1, name='David', email='david@example.com')
```

Benefits over regular classes:
- **Immutability** — fields cannot be reassigned (prevents `config.timeout = "oops"` bugs)
- **Readable repr** — `User(id=1, name='David')` instead of `<__main__.User object at 0x7f3...>`
- **Memory efficient** — lighter than full classes
- **Tuple-compatible** — can unpack: `uid, name, email = u`

## sqlite3: The Database You Already Have

Every Python installation includes `sqlite3`. Don't spin up a database server for every need:

- **Memory efficiency**: Store hundreds of thousands of lat/lon pairs in SQLite instead of Python lists to reduce RAM pressure
- **Transactional integrity**: `COMMIT` and `ROLLBACK` — safer than manual file writes
- **`:memory:` mode**: Ultra-fast ephemeral databases that exist only for the process lifetime — perfect for testing and temporary data processing

```python
import sqlite3
conn = sqlite3.connect(':memory:')  # Zero setup, zero cleanup
```

## Philosophy: Don't Rewrite

The professional Python developer's first question: **"Does the standard library already have this?"** This instinct reduces bugs, improves readability (everyone knows `defaultdict`), and keeps dependencies minimal.

---

- Core to [[python-professional-practices]] — batteries-included philosophy
- Related to [[immutability]] — namedtuple provides immutable data structures
- Related to [[code-quality-pillars]] — standard library reduces error-prone patterns
