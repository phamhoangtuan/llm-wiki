---
title: "Bijection"
type: concept
tags: [architecture, design-principles, domain-modeling]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
---

## Summary

Bijection is the golden design rule: **each domain object must be represented by a single object in the computable model and vice versa.** A one-to-one mapping between reality and code.

## The Rule

```
Reality: [Bank Account #123]  ↔  Code: [new BankAccount(id="123")]
Reality: [10 meters]          ↔  Code: [new Length(10, Unit.METERS)]
```
## When Bijection Fails: Mars Climate Orbiter (1999)

- **Reality**: Ground control used English units (pound-force), spacecraft expected metric (Newtons)
- **Code flaw**: Both sides used `double force = 10.5;` — a bare number with no semantic meaning
- **Result**: Spacecraft deviated from orbit, burned up in Mars' atmosphere — $125M loss

> A semantic error is more dangerous than a syntax error. Code that "runs" is not code that is "correct."

## 4 Common Bijection Violations

| Violation | Description | Consequence |
| --- | --- | --- |
| Many entities, one object | Using `int` for both "10 meters" and "10 inches" | Unit mismatch → wrong calculations |
| One entity, many objects | `Person` appears as separate `Athlete` and `Judge` objects | Data inconsistency, sync nightmare |
| Anemic representation | Object is just a "data holder" with getters/setters | Logic leaks outside, violates encapsulation |
| Implicit transformations | Language "auto-corrects" invalid data (Nov 31 → Dec 1) | Hides errors, violates [[fail-fast]] |
---
- Prevents [[rich-domain-model]] — violations — anemic objects are a bijection failure
- Enforced by [[immutability]] — mutable essence attributes break the 1-1 mapping
- Related to [[mapper-principles]] — Model and Reality principles
- Benchmark source: [[sources/contieri-clean-code-cookbook]] — Contieri's Clean Code Cookbook
