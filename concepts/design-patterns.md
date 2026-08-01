---
title: "Design Patterns"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [software-design, patterns, oop, gang-of-four]
sources: [dive-into-design-patterns, architecture-of-open-source-applications-vol2]
---

# Design Patterns

Reusable, customizable blueprints for solving recurring software design problems — not copy-paste code, but architectural templates. The 22 classic Gang of Four (GoF) patterns are organized into three categories by intent: Creational, Structural, and Behavioral.

## Principles Before Patterns

Patterns rest on foundational principles. Master these first:

- **Encapsulate What Varies** — Isolate changing logic
- **Program to an Interface** — Depend on abstractions
- **Favor Composition Over Inheritance** — Flexible object assembly over rigid hierarchies
- [[solid-principles|SOLID]] — The gold standard of object-oriented design

## Creational Patterns (5)

Solve object creation with flexibility and decoupling:

| Pattern | Intent | Key Use Case |
| --------- | -------- | ------------- |
| **Factory Method** | Delegate creation to subclasses | When a class can't anticipate what objects it must create |
| **Abstract Factory** | Create families of related objects | UI widget kits for different platforms (Windows/macOS) |
| **Builder** | Construct complex objects step-by-step | Multi-part reports, SQL query builders |
| **Prototype** | Clone existing instances | When object creation is costly (database lookups) |
| **Singleton** | Ensure exactly one instance | Configuration managers, connection pools |

## Structural Patterns (7)

Assemble larger structures from smaller parts without tight coupling:

| Pattern | Intent | Key Use Case |
| --------- | -------- | ------------- |
| **Adapter** | Make incompatible interfaces collaborate | Integrating legacy APIs with new systems |
| **Bridge** | Separate abstraction from implementation | When both need to vary independently |
| **Composite** | Treat individual objects and groups uniformly | File systems, UI component trees |
| **Decorator** | Add responsibilities dynamically | Logging, compression, encryption wrappers |
| **Facade** | Simplify access to complex subsystems | Home theater systems, library wrappers |
| **Flyweight** | Share state to reduce memory | Text editor character rendering |
| **Proxy** | Control access to an object | Lazy loading, security checks, remote proxies |

## Behavioral Patterns (10)

Define how objects communicate and delegate responsibilities:

| Pattern | Intent | Key Use Case |
| --------- | -------- | ------------- |
| **Chain of Responsibility** | Pass requests along handler chain | Logging levels, middleware pipelines |
| **Command** | Turn actions into first-class objects | Undo/redo, macro recording, job queues |
| **Iterator** | Traverse collections without exposing internals | Uniform access to lists, trees, graphs |
| **Mediator** | Centralize chaotic many-to-many dependencies | Chat rooms, air traffic control |
| **Memento** | Capture and restore object state | Undo/redo, game save states |
| **Observer** | Notify dependents of state changes | Event listeners, pub-sub systems |
| **State** | Change behavior with internal state | Order workflows, vending machines |
| **Strategy** | Interchangeable algorithms | Payment methods, sorting strategies, compression |
| **Template Method** | Algorithm skeleton with customizable steps | Build pipelines, data processing frameworks |
| **Visitor** | Add operations without modifying classes | AST traversal, report generation |

## Pattern Selection Heuristic

Start with the *problem*, not the pattern. Ask "What's hurting in my design?" then match symptoms to patterns. Master 3–5 patterns deeply before expanding.

---

- Grounded in [[solid-principles]] — SOLID is the compass for knowing when and how to apply patterns
- Extends [[object-oriented-design]] — patterns embody composition over inheritance, messages over methods
- Enables [[dependency-injection]] — Strategy, Factory, and Decorator are DI's closest allies
