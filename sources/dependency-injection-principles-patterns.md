---
title: "Dependency Injection Principles, Practices, and Patterns"
type: source
source_type: book
author: "Steven van Deursen & Mark Seemann"
source_date: 2019-01-01
ingested: 2026-05-31
created: 2026-05-31
updated: 2026-06-15
url: ""
tags: [dependency-injection, design-patterns, solid, architecture, testing]
concepts: [dependency-injection, composition-root, solid-principles]
---

## Summary

A 643-page definitive guide to Dependency Injection (DI) — not as a library or framework, but as a **discipline of software design** that enables loosely coupled, maintainable, and testable systems. Covers the three injection patterns, Composition Root, object lifetime management, anti-patterns, and SOLID principles as the foundation for effective DI.

## Core Message

> DI is not the destination — it's the vehicle to achieve maintainability through loose coupling, where components can be replaced, intercepted, or extended without causing a "domino effect" across the system.

## Three Injection Patterns

### 1. Constructor Injection (Primary Pattern)

For **mandatory dependencies** — things the class cannot function without.

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

Benefits: ensures class invariant (object never exists in invalid state), preserves encapsulation (dependencies are readonly, protected from external mutation).

### 2. Method Injection (Contextual Pattern)

For dependencies that **vary per call** — not the same across all method invocations.

```csharp
public decimal Convert(decimal amount, string from, string to, IExchangeRateProvider rateProvider)
{
    var rate = rateProvider.GetRate(from, to);
    return amount * rate;
}
```

### 3. Property Injection (Extensibility Pattern)

For **optional dependencies** — the class still works without them, but can extend behavior.

```csharp
public class ReportGenerator
{
    public IEmailSender EmailSender { get; set; } // Optional
    
    public void GenerateReport(ReportData data)
    {
        // Only send email if configured
        EmailSender?.Send(data.Recipient, data.Content);
    }
}
```

Also used as a last resort to break cyclic dependencies.

## Stable vs Volatile Dependencies

| Type | Characteristics | Management |
|---|---|---|
| **Stable** | Available in runtime (stdlib), deterministic logic, value types | New up internally — no DI needed |
| **Volatile** | Non-deterministic (DateTime.Now, Random), infrastructure (DB, file system, API), doesn't exist at code-writing time | Must inject for testability |

> Rule of thumb: If a dependency makes the class hard to test or reuse, it's volatile → inject it.

## Composition Root

The single, centralized location in the application where the entire object graph is wired together. Everything outside the Composition Root focuses purely on business logic, never on wiring.

### Pure DI vs DI Containers

| Aspect | Pure DI (Manual) | DI Container (Autofac, etc.) |
|---|---|---|
| Feedback | Compile-time errors (type-safe) | Runtime errors (harder to debug) |
| Transparency | Clear, traceable object graph | "Magic" auto-wiring |
| Complexity | Manual wiring burdensome at scale | Auto-wiring saves time |
| Risk | No third-party dependency | Leaky abstractions, container-specific bugs |

> Start with Pure DI to learn fundamentals. Switch to a container only when manual wiring becomes too costly.

## Object Lifetime Management

| Lifestyle | Definition | Use Case |
|---|---|---|
| **Singleton** | Single instance for entire app lifetime | Stateless services, caching, config |
| **Transient** | New instance per request | Stateful services, short-lived ops |
| **Scoped** | Shared instance within a logical context (e.g., web request) | Unit of Work, current user |

### Captive Dependency (Critical Bug)

Never inject a Scoped or Transient dependency into a Singleton. Consequences: stale data, memory leaks, concurrency bugs.

## Anti-Patterns

1. **Service Locator** — Class asks the container for dependencies instead of declaring them. Obscures requirements, hard to test.
2. **Ambient Context** — Global static access point (e.g., `Logger.Global.Log()`). Hard to replace for testing.
3. **Control Freak** — Class instantiates its own volatile dependencies (`new SqlDatabase()`). Locks into implementation.

## SOLID as Foundation

DI works because of SOLID principles:
- **S** (Single Responsibility) — class has one reason to change; focused dependencies
- **O** (Open/Closed) — open for extension via decoration/interception
- **L** (Liskov Substitution) — any implementation can replace the abstraction
- **I** (Interface Segregation) — small, focused interfaces
- **D** (Dependency Inversion) — both high and low-level modules depend on abstractions

→ See [[solid-principles]]

## Adoption Roadmap

1. **Foundation** (weeks 1-2): Classify dependencies, refactor to constructor injection, create Composition Root
2. **Best Practices** (weeks 3-4): Apply SOLID, manage lifetimes, write unit tests with mocks
3. **Advanced** (weeks 5-6): Decorator pattern for cross-cutting concerns, handle cyclic dependencies
4. **Scale** (weeks 7+): Document dependency graph, CI/CD for DI bugs, team training
