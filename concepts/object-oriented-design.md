---
title: "Object-Oriented Design"
type: concept
tags: [oop, design-principles, maintainability, agile]
created: 2026-06-08
updated: 2026-06-15
sources: [practical-object-oriented-design]
aliases: [pood, oo-design, practical-design]
---

## Summary

Object-oriented design is the practice of arranging code to minimize the cost of change — the one thing guaranteed over a software system's lifetime. It is not a separate phase before coding but a continuous process of discovery. The TRUE standard provides a practical quality metric, while the message-passing model reorients thinking from "calling functions" to "objects communicating."

## What Design Is (and Isn't)

| Old View | Practical View (POOD) |
|---|---|
| Design is creating perfection upfront | Design is arranging code to reduce the cost of change |
| Design is a separate phase before coding | Design is part of continuous discovery |
| Goal: follow rigid principles | Goal: preserve changeability |

> "The purpose of design is to allow you to do design later." — Sandi Metz

## The TRUE Standard

A practical checklist for measuring design quality — not abstract metrics, but questions anyone can ask:

| Letter | Meaning | Question |
|---|---|---|
| **T — Transparent** | Consequences of change are obvious | "If I change this, do I know exactly what will be affected?" |
| **R — Reasonable** | Cost of change is proportional to benefit | "Is this change worth the effort, or disproportionately complex?" |
| **U — Usable** | Code is reusable in new contexts | "Can I use this code for another feature without major rewrites?" |
| **E — Exemplary** | Code encourages others to follow | "Would a new team member naturally write code in the same style?" |

> **Ultimate metric**: Cost per Feature over Time — not lines of code or cyclomatic complexity.

## Design as Discovery (No BUFD)

Big Up Front Design (BUFD) assumes requirements are known and stable — an illusion:

| BUFD ❌ | Design as Discovery ✅ |
|---|---|
| Assumes we can predict all requirements | Accepts that customers discover needs through working software |
| Creates adversarial relationship with stakeholders | Iterative feedback loop builds trust |
| Produces "beautiful" architectures that don't fit reality | Produces code that evolves with understanding |

**Three ways design fails:**
1. **Lack of Design** — successful app without design carries seeds of self-destruction
2. **Overdesign** — rigid application of principles creates beautiful but unusable code castles
3. **Separation from Practice** — design by isolated "experts" without coding feedback loops

## Messages: The Heart of OOP

OOP is fundamentally about objects communicating via messages, not calling functions:

| Procedural | Object-Oriented |
|---|---|
| Data and behavior separated by a "chasm" | Data + behavior combined in objects |
| Functions execute predefined logic | Objects send messages requesting behavior |
| Extensibility limited to built-in types | Infinite extensibility — programmers create new types |

```
// ❌ Procedural thinking: call a function
calculate_tax(order)

// ✅ OOP thinking: send a message
order.tax()  → TaxCalculator receives message, responds with result
```

> **Mindset shift**: Don't think about executing logic. Think about sending messages that request objects to perform their behavior.

## SRP: Smallest Possible Useful Thing

The Single Responsibility Principle is the foundation. A class should do the smallest possible thing while still being useful:

```
// ❌ SRP violation: one class, three responsibilities
class Order {
  calculate_total()  // Business logic
  save_to_database() // Persistence
  send_confirmation() // Notification
}

// ✅ SRP compliance: each class, one responsibility
class Order { calculate_total() }
class OrderRepository { save(order) }
class OrderNotifier { send_confirmation(order) }
```

**Why it matters**: When each class has one reason to change, impact is localized. Changing persistence doesn't touch business logic.

## Technical Debt as Borrowed Time

Choosing speed over design borrows time from the future — and you pay with interest:

- Small apps survive poor design because one person holds the mental model
- Large apps become "tar pits" — the harder you struggle to change, the deeper you sink
- Agile needs **more** design, not less — frequent iterations demand code that bends without breaking

---

- Builds on [[solid-principles]] — SRP is the foundation; OCP, LSP, ISP, DIP enable practical design
- Related to [[tell-dont-ask]] — both center on objects owning their behavior; messages replace data queries
- Informed by [[code-quality-pillars]] — TRUE (Transparent) aligns with readability; TRUE (Reasonable) with modularity
- Complements [[software-quality-dimensions]] — design as discovery acknowledges the trade-off between upfront planning and adaptability
- Related to [[bijection]] — good OO design maps objects 1:1 to real-world entities
- Related to [[rich-domain-model]] — objects encapsulate both data and behavior via message-passing
- Related to [[dependency-injection]] — DI supplies objects their collaborators so they can send messages
- Benchmark source: [[sources/practical-object-oriented-design]] — Sandi Metz's 334-page guide
