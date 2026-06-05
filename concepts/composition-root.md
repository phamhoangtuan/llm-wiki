---
title: "Composition Root"
type: concept
tags: [design-patterns, architecture, di, composition-root]
created: 2026-05-31
updated: 2026-05-31
sources: [dependency-injection-principles-patterns]
---

## Summary

The **Composition Root** is the single, centralized location in an application where the entire object graph is wired together — where all [[dependency-injection|Dependency Injection]] composition happens. Everything outside the Composition Root focuses purely on business logic, never on creating or wiring dependencies.

## Why Centralize?

Without a Composition Root, dependency creation is scattered across the codebase:

```
❌ Scattered: Every class "news up" its own dependencies
   → Hard to change wiring, hard to see the full picture

✅ Centralized: One place creates the entire object graph
   → Single point of change, full visibility, pure business logic elsewhere
```

## Location by Application Type

| Application Type | Composition Root |
|---|---|
| Console App | `Main()` method |
| ASP.NET Core | `Startup.ConfigureServices()` + controller activators |
| Desktop (WPF/UWP) | `OnLaunched()` or startup logic |
| Lambda / Serverless | Function entry point |

## Pure DI vs DI Containers

The Composition Root can be implemented two ways:

### Pure DI (Manual Wiring)

```csharp
// Composition Root: Main()
var payment = new StripePaymentProcessor();
var logger = new FileLogger("/var/log/app.log");
var service = new OrderService(payment, logger);
```

### DI Container (Auto-Wiring)

```csharp
// Composition Root: Startup.ConfigureServices()
services.AddTransient<IPaymentProcessor, StripePaymentProcessor>();
services.AddSingleton<ILogger, FileLogger>();
services.AddTransient<OrderService>();
```

| Aspect | Pure DI | DI Container |
|---|---|---|
| **Feedback** | Compile-time errors | Runtime errors |
| **Transparency** | Explicit, traceable | "Magic" auto-wiring |
| **Scale** | Burdensome for large graphs | Auto-wiring saves effort |
| **Risk** | None (no third-party lib) | Container-specific bugs |
| **Learning** | Essential for fundamentals | Convenience layer on top |

> Start with Pure DI. Adopt a container only when manual wiring becomes too costly — not sooner.

## Rules of the Composition Root

1. **Only ONE** Composition Root per application — no scattered wiring
2. **Only the Composition Root** references the DI container (if using one)
3. **Everything else** is container-ignorant — pure business logic
4. **Lifetime decisions** live here: which services are Singleton, Transient, Scoped
5. **No business logic** in the Composition Root — it's purely infrastructure

## Object Lifetime Management

The Composition Root owns all lifetime decisions:

```csharp
// Composition Root decides:
services.AddSingleton<IConfiguration, AppConfig>();         // One for all
services.AddScoped<IUnitOfWork, EfUnitOfWork>();            // Per request
services.AddTransient<IEmailSender, SmtpEmailSender>();     // New each time
```

The critical rule: **never inject a shorter-lived dependency into a longer-lived one** (Captive Dependency).

→ See [[dependency-injection]] for lifetime details.

## Common Mistakes

| Mistake | Why It's Wrong |
|---|---|
| Multiple Composition Roots | Wiring scattered; no single source of truth |
| Business logic in Composition Root | Mixes infrastructure with domain; untestable |
| Service Locator outside Composition Root | Defeats the purpose; classes become container-aware |
| Premature container adoption | Hide complexity behind "magic"; developers skip learning fundamentals |
---
- Implements [[dependency-injection]] — the Composition Root is where all DI wiring happens
- Related to [[solid-principles]] — SRP applied to infrastructure: one place, one responsibility
- Benchmark source: [[sources/dependency-injection-principles-patterns]] — van Deursen & Seemann's 643-page definitive guide
