---
title: "Lindy Effect"
type: concept
tags: [technology-selection, architecture, heuristics, data-engineering]
created: 2026-07-13
updated: 2026-07-13
sources: [fundamentals-of-data-engineering]
aliases: [lindy-law, lindy-rule]
---

## Summary

The **Lindy Effect** is a heuristic for technology selection: **the longer a technology has been around, the longer it's likely to stay around.** Future life expectancy is proportional to current age — not because old is always better, but because technologies that have survived decades have proven their value across diverse use cases, economic cycles, and paradigm shifts.

## Application to Data Engineering

In data architecture, Lindy guides tool selection:

| Lindy (Build On) | Non-Lindy (Be Cautious) |
| --- | --- |
| SQL (50+ years) | New query engines without track records |
| Object storage / Unix semantics | Proprietary storage formats with single-vendor lock-in |
| Python, C, Java | Niche languages with small communities |
| Relational algebra, normalization | New data modeling paradigms without proven stability |

The principle doesn't mean "never adopt new tech." It means: **build your foundation on Lindy technologies; experiment with transitory tools at the edges.** When a new tool fails (or is abandoned by its vendor), the Lindy foundation keeps your system operational.

## Broader Applications

The Lindy Effect applies beyond technology: books that have been in print for decades, mathematical theorems, and engineering principles all gain credibility with age. It's a defense against hype cycles — the next shiny framework may be gone in two years, but SQL will still be here.

---

- Foundation for [[data-engineering-fundamentals]] — SQL, Python, and data modeling endure because they've proven Lindy
- Related to [[risk-driven-architecture]] — Lindy is a risk-reduction heuristic for architectural decisions
- Connected to [[essential-accidental-complexity]] — Lindy technologies tend to capture essential complexity well
- Benchmark source: [[sources/fundamentals-of-data-engineering]] — Reis & Housley advocate Lindy in architecture and tool selection
