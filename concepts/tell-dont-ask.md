---
title: "Tell, Don't Ask"
type: concept
tags: [oop, design-principles, encapsulation]
created: 2026-05-23
updated: 2026-06-15
sources: [contieri-clean-code-cookbook, practical-object-oriented-design]
---

## Summary

"Don't ask an object for data to process logic outside it. Tell the object to perform its behavior." This principle protects encapsulation and localizes change.

## The Principle

| Old Way (Ask) | New Way (Tell) |
| --- | --- |
| `if (order.getAmount() > 100) { order.setStatus("PREMIUM"); }` | `order.applyPremiumDiscount();` |
| Logic outside object | Logic inside object |
| Ripple effect on requirement changes | Change localized in object |
---
- Protects [[bijection]] — the object represents the real entity's behavior
- Related to [[immutability]] — telling an object to act is safer than mutating its state from outside
- Central to [[object-oriented-design]] — telling objects via messages, not asking for data, is the essence of OOP
- Benchmark source: [[sources/contieri-clean-code-cookbook]] — Contieri's Clean Code Cookbook
