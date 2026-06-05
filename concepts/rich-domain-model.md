---
title: "Rich Domain Model"
type: concept
tags: [oop, architecture, domain-driven-design]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
---

## Summary

Rich domain models encapsulate both data and behavior within objects. The alternative — **Anemic Domain Model** — is a data holder with only getters/setters, which is procedural programming in disguise.

## Anemic Model (Anti-pattern)

```
// ❌ Object is just a data bag
public class Order {
    private double amount;
    private String status;
    public double getAmount() { return amount; }
    public void setAmount(double amount) { this.amount = amount; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}

// Logic lives outside → procedural programming
if (order.getAmount() > 100) {
    order.setStatus("PREMIUM");
}
```
**Problems**: Violates encapsulation, logic scattered across codebase, object has no responsibility.

## Rich Model (Correct)

```
// ✅ Object encapsulates data AND behavior
public class Order {
    private final Money amount;       // Value Object, immutable
    private OrderStatus status;

    public void applyPremiumDiscount() {
        if (amount.isGreaterThan(Money.of(100))) {
            this.status = OrderStatus.PREMIUM;
            this.amount = this.amount.multiply(0.9);
        }
    }
}
```
## Key Benefits

- Change localization: when business rules change, fix one place (inside the class)
- Encapsulation: internal state is protected
- Objects have responsibility — they are active behavioral entities

---
- Enforced by [[bijection]] — anemic objects are a bijection violation
- Supported by [[tell-dont-ask]] — the behavioral principle
- Related to [[immutability]] — rich objects protect essential attributes
- Benchmark source: [[sources/contieri-clean-code-cookbook]] — Contieri's Clean Code Cookbook
