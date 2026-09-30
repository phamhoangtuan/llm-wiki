---
title: "Practical Object-Oriented Design, 2nd Edition"
type: source
source_type: book
author: "Sandi Metz"
source_date: 2018-01-01
ingested: 2026-06-08
created: 2026-06-08
updated: 2026-06-15
url: ""
tags: [oop, design-principles, ruby, maintainability, agile]
concepts: [object-oriented-design, solid-principles]
---

## Summary

A 334-page field guide to practical object-oriented design. Rejects big-up-front-design in favor of design-as-discovery, introduces the TRUE standard (Transparent, Reasonable, Usable, Exemplary) for measuring design quality, and roots OOP in message-passing between objects rather than class hierarchies. SRP is treated as the foundational principle — classes should do the smallest possible useful thing.

## Core Message

> Design is not a luxury for perfect projects. It's a survival requirement for managing change — the one thing guaranteed to happen over a software system's lifetime. The purpose of design is to allow you to do design later.

## Key Takeaways

1. **Change is King**: Design exists to manage change, not to achieve upfront perfection
2. **TRUE Standard**: Code should be Transparent (consequences clear), Reasonable (cost proportional), Usable (reusable), Exemplary (encourages others to follow)
3. **No BUFD**: Big Up Front Design is an illusion — design is continuous discovery alongside coding
4. **Technical Debt**: Choosing speed over design borrows time from the future — you pay with interest
5. **Messages > Methods**: OOP is about objects sending messages, not calling functions — think communication, not execution
6. **SRP as Foundation**: Smallest possible useful thing — isolate change by giving each class one reason to change

## Companion Concepts

→ [[object-oriented-design]] — the TRUE framework and design philosophy
→ [[solid-principles]] — SRP, OCP, LSP, ISP, DIP — the formal foundation POOD builds on
