---
title: "MAPPER Principles"
type: concept
tags: [architecture, design-principles, clean-code]
created: 2026-05-23
updated: 2026-06-15
sources: [contieri-clean-code-cookbook]
---

## Summary

MAPPER is an acronym for 6 principles that define the "software as simulation" philosophy. Each letter represents a guideline for building faithful computational models of reality.

## The 6 Principles

| Letter | Principle | Meaning | Example |
| --- | --- | --- | --- |
| **M** | Model | Code is a "theory" about how the world works | `BankAccount` class simulates a real bank account |
| **A** | Abstract | Focus on contracts & behavior, not implementation details | `PaymentProcessor` interface with `process()` — doesn't matter if it's Stripe or PayPal |
| **P** | Partial | Only simulate what's relevant — not the entire reality | `User` class needs email and name, not shoe size (unless it's a shoe store) |
| **P** | Programmable | The model must be executable to observe its evolution and response | Code must compile and run, not just be theory on paper |
| **E** | Explaining | Code should reveal "why" not just "what" — declarative naming | `isPremiumUser` is clearer than `flag1` |
| **R** | Reality | The observable world is the ultimate source of truth | Units must be explicit: Newtons vs. pound-force — never ambiguous |
---
- Operationalizes [[software-as-simulation]] — turns philosophy into actionable guidelines
- Enforced by [[bijection]] — the 1-1 mapping is the concrete implementation of Model + Reality
- Supports [[rich-domain-model]] — Abstract + Explaining encourage behavioral objects
- Related to [[tell-dont-ask]] — Explaining principle guides naming and behavior revelation
- Benchmark source: [[sources/contieri-clean-code-cookbook]] — Contieri's Clean Code Cookbook
