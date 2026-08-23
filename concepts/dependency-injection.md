---
title: "Dependency Injection"
type: concept
tags: [design-patterns, architecture, testing, di, solid]
created: 2026-05-31
updated: 2026-06-15
sources: [dependency-injection-principles-patterns]
aliases: [DI]
---

## Summary

**Dependency Injection (DI)** is a set of software design principles and patterns that enable **loose coupling** between components. Rather than a library or framework, DI is a discipline: classes declare their dependencies (typically via constructor parameters), and an external mechanism supplies them. The goal is not DI itself — it's **maintainability** through replaceable, testable components.

> "DI is the vehicle. Loose coupling is the destination."

## Core Idea: "Don't Call Us, We'll Call You"

```
❌ Control Freak: Class creates its own dependencies
   OrderService → new SqlDatabase() → tight coupling, hard to test

✅ Dependency Injection: Class declares what it needs
   OrderService → IDatabase (passed in) → loose coupling, easy to test
```

A class should **state a need**, not go fetch it. Infrastructure supplies what's required.

## Three Injection Patterns

### 1. Constructor Injection (Primary — for mandatory dependencies)

```csharp
public class OrderService
{
    private readonly IPaymentProcessor _payment;
    
    public OrderService(IPaymentProcessor payment)
    {
        _payment = payment ?? throw new ArgumentNullException(nameof(payment));
    }
}
```

**When**: The class cannot function without this dependency.
**Benefits**: Guarantees class invariant (object never exists invalid), protects encapsulation (readonly fields).

### 2. Method Injection (Contextual — for call-varying dependencies)

```csharp
public decimal Convert(decimal amount, string from, string to, IExchangeRateProvider rates)
{
    return amount * rates.GetRate(from, to);
}
```

**When**: The dependency changes per method call — not the same across all invocations.

### 3. Property Injection (Extensibility — for optional dependencies)

```csharp
public class ReportGenerator
{
    public IEmailSender EmailSender { get; set; }
    
    public void Generate(ReportData data)
    {
        EmailSender?.Send(data.Recipient, data.Content); // Safe null check
    }
}
```

**When**: The class works without it, but behavior can be extended. Also a **last resort** for breaking cyclic dependencies.

## Stable vs Volatile Dependencies

Not everything needs to be injected:

| Type | Characteristics | Handle |
|---|---|---|
| **Stable** | Standard library types, deterministic logic, value types (string, List, Math) | `new` internally |
| **Volatile** | Non-deterministic (DateTime, Random), infrastructure (DB, network, file I/O), not-yet-existing | **Must inject** |

> A dependency is volatile if it makes the class hard to test or hard to reuse.

## Object Lifetime Management

Lifetime management is the **sole responsibility of the [[composition-root|Composition Root]]**. Consumers never know or manage dependency lifetimes.

| Lifestyle | Scope | Best For |
|---|---|---|
| **Singleton** | One instance for entire app | Stateless services, caching, config |
| **Transient** | New instance per request | Stateful, short-lived operations |
| **Scoped** | Shared within a logical context (e.g., web request) | Unit of Work, Current User |

### Captive Dependency (Critical Anti-Pattern)

> **Never inject a Scoped or Transient dependency into a Singleton.**

```csharp
// ❌ FATAL: Scoped connection trapped in Singleton
public class CachedDataService // Singleton
{
    public CachedDataService(IDbConnection connection) // Scoped!
    { ... }
}
```

Consequences: stale data, memory leaks, concurrency bugs.

## Common Anti-Patterns

| Anti-Pattern | Problem | Fix |
|---|---|---|
| **Service Locator** | Class asks container `GetService<T>()` — obscures requirements, hard to test | Constructor injection — declare dependencies explicitly |
| **Ambient Context** | Global static access `Logger.Global.Log()` — hard to replace or intercept | Inject `ILogger` via constructor |
| **Control Freak** | Class does `new SqlDatabase()` — locks into implementation | Inject `IDatabase` abstraction |

→ See [[composition-root]] for how to centralize and avoid these.

## SOLID as Foundation

DI works because of [[solid-principles|SOLID principles]]:
- **S** — Single Responsibility: focused classes → focused dependencies
- **O** — Open/Closed: decoration (wrapping) without modifying original
- **L** — Liskov Substitution: any implementation works through the abstraction
- **I** — Interface Segregation: small interfaces → targeted injection
- **D** — Dependency Inversion: depend on abstractions, not concretions

## When to Use DI

| ✅ Use DI | ❌ Skip DI |
|---|---|
| Volatile dependencies (DB, API, file I/O) | Stable dependencies (string, List, Math) |
| Code that needs unit testing | One-off scripts, throwaway code |
| Multi-developer, long-lived projects | Single-developer prototypes |
| Cross-cutting concerns (logging, caching) | No extensibility needs |

## Adoption Path

1. Classify dependencies: Stable vs Volatile
2. Refactor volatile deps to constructor injection
3. Create a [[composition-root|Composition Root]] at the application entry point
4. Start with Pure DI (manual wiring); adopt a container only when necessary
5. Manage lifetimes carefully — avoid Captive Dependency
---
- Implemented via [[composition-root]] — all wiring centralized at the Composition Root
- Built on [[solid-principles]] — DI is enabled by SRP, OCP, LSP, ISP, DIP
- Related to [[fail-fast]] — guard clauses in constructors (`throw new ArgumentNullException`) enforce valid state
- Related to [[immutability]] — readonly fields in injected classes prevent accidental mutation
- Benchmark source: [[sources/dependency-injection-principles-patterns]] — van Deursen & Seemann's 643-page definitive guide
