---
title: "Tell, Don't Ask"
type: concept
tags: [oop, design-principles, encapsulation]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
aliases: [tell dont ask, behavioral encapsulation]
---

## Summary

"Don't ask an object for data to process logic outside it. Tell the object to perform its behavior." This principle protects encapsulation and localizes change.

## The Principle

| Old Way (Ask) | New Way (Tell) |
|---|---|
| `if (order.getAmount() > 100) { order.setStatus("PREMIUM"); }` | `order.applyPremiumDiscount();` |
| Logic outside object | Logic inside object |
| Ripple effect on requirement changes | Change localized in object |

## Why It Matters

When business rules change:
- **Ask approach**: Find and fix logic scattered across the entire codebase
- **Tell approach**: Fix one method inside the class

## Connections

- Enforces [[rich-domain-model]] — objects must have behavior, not just data
- Protects [[bijection]] — the object represents the real entity's behavior
- Related to [[immutability]] — telling an object to act is safer than mutating its state from outside
