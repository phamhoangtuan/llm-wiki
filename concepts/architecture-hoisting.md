---
title: "Architecture Hoisting"
type: concept
tags: [software-architecture, quality-attributes, design-patterns]
created: 2026-06-26
updated: 2026-06-26
sources: [just-enough-software-architecture-fairbanks]
aliases: []
---

Architecture Hoisting is the strategy of **shifting quality attribute guarantees from manual developer discipline to structural system constraints**. Instead of relying on every developer to follow rules correctly every time, hoisting bakes the guarantee into the architecture itself.

## The Analogy: Seatbelt vs. Airbag

| Approach | Example | Developer Role |
|---|---|---|
| Architecture-Focused | Seatbelt | System provides support, but developer must remember to "buckle up" (follow the rule) |
| Architecture Hoisting | Airbag | System handles it automatically. Developer neither needs to think about it nor can interfere |

Hoisting is the **airbag** — automatic, non-negotiable, always on.

## Tyranny for Liberation

> Constraints that restrict what you can do simultaneously free you from entire categories of bugs.

Hoisting creates **strict constraints** (tyranny), but those constraints **liberate** developers from worrying about low-level correctness:

| Problem Domain | Manual (Fragile) | Hoisted (Guaranteed) |
|---|---|---|
| Memory Management | Developer calls `free()` on every allocation — risk of leaks, double-free | Garbage Collection — system handles all memory lifecycle |
| Concurrency | Developer manages threads, locks, synchronization — risk of race conditions, deadlocks | App Server (EJB) — server manages instance pooling and thread safety |
| Fault Isolation | Code reviews enforce separation rules — easily violated | Separate processes — crash in one cannot affect another |
| Security | Access checks scattered throughout code — easy to miss | Structural isolation at architectural boundary — enforced by design |

## Constraints as Guide Rails

Hoisting imposes constraints that reduce **needless creativity**. When developers can't express certain patterns (e.g., EJB forbids direct thread creation), they're guided toward the safe path by default. This is not about limiting innovation — it's about preventing known failure modes so creativity can focus on the actual business problem.

## When to Hoist

Consider hoisting when:
- A quality attribute is **critical** to system success (safety, security, data integrity)
- Manual enforcement has **failed repeatedly** (code review catch rate is low)
- The failure mode has **catastrophic consequences** (patient monitoring, financial transactions)
- The constraint's **cost** (reduced flexibility) is acceptable given the risk reduction

## The Cost

Hoisting isn't free. You trade flexibility for safety:
- **EJB example**: Can't write custom threading — must work within container's model
- **GC example**: Less control over memory layout and deallocation timing
- **Structural isolation**: Can't share memory for performance — must serialize across boundaries

The risk-driven framework answers whether this trade-off is worth it: if the risk of manual enforcement justifies the loss of flexibility, hoist.

---

## Connections

- [[risk-driven-architecture|Risk-Driven Architecture]] — The meta-framework that determines when hoisting is warranted
- [[model-code-gap|Model-Code Gap]] — Hoisting bridges the gap by encoding intent in structure, not just code
- [[software-quality-dimensions|Software Quality Dimensions]] — Hoisting targets specific quality attributes (security, reliability, safety)
- [[immutability|Immutability]] — A form of hoisting: structural guarantee against mutation
- [[fail-fast|Fail Fast]] — Hoisting enforces fail-fast at architectural boundaries
- [[dependency-injection|Dependency Injection]] — Structural enforcement of loose coupling
