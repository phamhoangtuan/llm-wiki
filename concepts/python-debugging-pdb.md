---
title: "Python Debugging with PDB"
type: concept
tags: [python, debugging, pdb]
created: 2026-06-12
updated: 2026-06-12
sources: [intuitive-python]
aliases: [breakpoint, PDB, Python debugger]
---

# Python Debugging with PDB

Interactive debugging using Python's built-in debugger (PDB) as a surgical tool, replacing the reactive and limited `print()`-based debugging approach. The debugger transforms debugging from guessing to **systematic state exploration**.

## breakpoint() vs print()

From Python 3.7+, `breakpoint()` is the standard entry point (replaces `import pdb; pdb.set_trace()`):

| Dimension | print() | breakpoint()/PDB |
|---|---|---|
| **Proactivity** | Must predict what to inspect in advance | Explore any state without knowing in advance |
| **Interaction** | None — fire and read output | Full interactive session: query variables, test expressions, modify state |
| **Efficiency** | Add prints → restart → remove prints → restart | Pause execution at exact line, inspect, then continue |
| **Nested Data** | Unreadable for dicts/lists | `pp` (pretty print) with indentation and sorted keys |

## Essential PDB Commands

Once inside a PDB session, these commands enable surgical navigation:

| Command | Short | Effect |
|---|---|---|
| `next` | `n` | Execute current line, stop at next line in same function (don't enter called functions) |
| `step` | `s` | Step **into** the called function to inspect internal logic |
| `pp` | — | **Pretty-print** — game-changer for nested dicts/lists with proper indentation and sorted keys |
| `where` | `w` | Print full stack trace showing the exact call path that led to this point |
| `continue` | `c` | Resume normal execution until next breakpoint |
| `list` | `l` | Show source code around current line |
| `args` | `a` | Print arguments of the current function |

## Workflow Pattern

Instead of:
```python
# ❌ Reactive print debugging
print(user_data)
print(type(user_data))
print(user_data.keys())
```

Use:
```python
# ✅ Proactive interactive debugging
breakpoint()
# In PDB: pp user_data
# In PDB: type(user_data)
# In PDB: dir(user_data)
```

The debugger lets you inspect **without knowing what to ask in advance** — you explore the actual runtime state interactively.

## Advanced: Post-Mortem Debugging

PDB can also inspect crashes after they happen:

```python
import pdb; pdb.pm()  # Post-mortem: inspect the last traceback
```

This is useful for understanding unexpected crashes in production-like scenarios without reproducing them.

---

- Core to [[python-professional-practices]] — professional debugging workflow
- Related to [[fail-fast]] — interactive inspection of failure states
- Related to [[python-repl]] — REPL shares the interactive exploration mindset
- Related to [[testing-strategy]] — debugging tests that fail unexpectedly
