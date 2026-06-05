---
title: "SOLID Principles"
type: concept
tags: [design-principles, architecture, solid, oop, clean-code]
created: 2026-05-31
updated: 2026-05-31
sources: [dependency-injection-principles-patterns, contieri-clean-code-cookbook]
---

## Summary

**SOLID** is an acronym for five object-oriented design principles that together enable maintainable, extensible, and testable software. They form the theoretical foundation for [[dependency-injection|Dependency Injection]] — DI only works well when SOLID principles are followed. The principles were introduced by Robert C. Martin ("Uncle Bob").

## The Five Principles

### S — Single Responsibility Principle (SRP)

> A class should have only one reason to change.

| ❌ Violation | ✅ Compliance |
|---|---|
| `OrderService` handles orders AND sends emails AND logs | `OrderService` → only order logic; `IEmailSender` and `ILogger` injected |

Each class has one focused responsibility → dependencies stay small and targeted.

### O — Open/Closed Principle (OCP)

> Open for extension, closed for modification.

You should be able to add new behavior without changing existing code. In DI, this enables the **Decorator pattern**:

```csharp
// Wrap IPaymentProcessor with caching — no changes to original
public class CachingPaymentProcessor : IPaymentProcessor
{
    private readonly IPaymentProcessor _inner;
    public CachingPaymentProcessor(IPaymentProcessor inner) => _inner = inner;
    
    public PaymentResult Charge(PaymentRequest req)
        => _cache.GetOrCreate(req.Key, () => _inner.Charge(req));
}
```

### L — Liskov Substitution Principle (LSP)

> Subtypes must be substitutable for their base types.

Any implementation of an abstraction must behave correctly when used through that abstraction. In DI: you can swap `StripePaymentProcessor` for `PayPalPaymentProcessor` without changing any consumer code — as long as both correctly implement `IPaymentProcessor`.

### I — Interface Segregation Principle (ISP)

> Many client-specific interfaces are better than one general-purpose interface.

| ❌ Fat Interface | ✅ Segregated Interfaces |
|---|---|
| `IRepository { Read(); Write(); Delete(); Archive(); ... }` | `IReadableRepository`, `IWritableRepository`, `IArchivableRepository` |

Small interfaces → consumers only depend on what they actually need → easier to mock in tests, easier to swap implementations.

### D — Dependency Inversion Principle (DIP)

> Depend on abstractions, not concretions.

Both high-level modules (business logic) and low-level modules (database, network) should depend on abstractions:

```
❌ OrderService → SqlDatabase (high depends on low = fragile)
✅ OrderService → IDatabase ← SqlDatabase (both depend on abstraction)
```

This is the **direct enabler** of DI: if everything depends on interfaces, you can wire any implementation at the [[composition-root|Composition Root]].

## SOLID in Practice with DI

| Principle | DI Impact |
|---|---|
| **SRP** | Focused classes → focused constructors (fewer parameters) |
| **OCP** | Decoration pattern — wrap services without touching originals |
| **LSP** | Any implementation works through the abstraction — swap freely |
| **ISP** | Small interfaces → only inject what's needed → no "fat mock" problem |
| **DIP** | Constructor injection with interfaces — the mechanism itself |

## Relationship to Other Principles

SOLID is not the only design framework. Complementary concepts in the wiki:

- **[[mapper-principles|MAPPER]]** — Maximiliano Contieri's 6 principles (Model, Abstract, Partial, Programmable, Explaining, Reality) — an alternative lens on software design
- **[[tell-dont-ask|Tell, Don't Ask]]** — Aligns with SRP: tell objects to act, don't ask for data
- **[[rich-domain-model|Rich Domain Model]]** — Objects encapsulate data + behavior; DI supplies their dependencies
- **[[immutability]]** — Readonly fields in constructors preserve valid state
- **[[fail-fast]]** — Guard clauses in constructors (`throw new ArgumentNullException`) enforce invariants

## When Principles Conflict

SOLID is guidance, not dogma:

- SRP can lead to too many tiny classes → use judgment
- OCP via decoration adds indirection → only when needed
- ISP can over-fragment interfaces → balance with cohesion
- DIP requires abstractions → don't abstract stable dependencies (`string`, `List<T>`)
---
- Enables [[dependency-injection]] — DI works because of SRP, OCP, LSP, ISP, and DIP
- Implements [[composition-root]] — Composition Root uses DIP to wire abstractions to concretions
- Complements [[mapper-principles]] — different framework, same goal: maintainable software
- Related to [[tell-dont-ask]] — aligned with SRP: focused objects with clear responsibilities
- Related to [[rich-domain-model]] — SOLID enables rich domain objects with injected dependencies
- Related to [[fail-fast]] — guard clauses in constructors enforce valid state at creation time
- Related to [[immutability]] — readonly fields prevent accidental mutation of injected dependencies
- Benchmark source: [[sources/dependency-injection-principles-patterns]] — van Deursen & Seemann's definitive guide
