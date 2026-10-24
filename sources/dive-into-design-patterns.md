---
title: "Dive Into Design Patterns"
type: source
source_type: book
author: "Alexander Shvets"
url: ""
source_date: 2019-01-01
ingested: 2026-07-13
tags: [design-patterns, oop, solid, software-design]
concepts: [design-patterns, solid-principles, object-oriented-design]
---

# Dive Into Design Patterns

Alexander Shvets' 410-page practical, language-agnostic guide to the 22 classic Gang of Four design patterns. Uses pseudocode, UML diagrams, and progressive structure.

## OOP Foundations

The four pillars: Abstraction, Encapsulation, Inheritance, Polymorphism. Prefer **composition over inheritance** — more flexible, less fragile.

Object relationships (weak → strong): Dependency → Association → Aggregation → Composition.

## Design Principles (The Rules of the Road)

- **Encapsulate What Varies** — Isolate changing logic so it doesn't ripple through the system
- **Program to an Interface** — Depend on abstractions, not concrete implementations
- **Favor Composition Over Inheritance** — Build behavior by combining objects, not deep class trees

Plus [[solid-principles|SOLID]]: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion.

## The 22 Patterns (3 Categories)

### Creational (Object Creation)

Factory Method, Abstract Factory, Builder, Prototype, Singleton

### Structural (Assembling Components)

Adapter, Bridge, Composite, Decorator, Facade, Flyweight, Proxy

### Behavioral (Algorithms & Responsibilities)

Chain of Responsibility, Command, Iterator, Mediator, Memento, Observer, State, Strategy, Template Method, Visitor

## Learning Path

Week 1-2: Strategy + Observer → Week 3-4: Factory + Builder → Week 5-6: Adapter + Decorator → Week 7+: Revisit SOLID, refactor old code with pattern-aware eyes.

> Design patterns don't make you a better coder. They make you a better thinker.

---

- Comprehensive reference for [[design-patterns]] — all 22 GoF patterns in 3 categories
- Grounded in [[solid-principles]] — SOLID as the compass for pattern-aware design
- Extends [[object-oriented-design]] — composition over inheritance, messages over methods
