---
title: "Goodhart's Law"
type: concept
tags: [metrics, measurement, statistics, organizational-behavior]
created: 2026-08-06
updated: 2026-08-06
sources: [tyranny-of-metrics]
aliases: [goodharts-law, campbells-law]
---

## Summary

**Goodhart's Law** states: "When a measure becomes a target, it ceases to be a good measure." Originally formulated by economist Charles Goodhart about monetary policy, it has become a universal principle of measurement dysfunction — applying to business KPIs, academic metrics, software engineering metrics, and any domain where numbers are used to drive behavior.

## The Mechanism

A metric has two roles:

1. **Descriptive**: It reflects some underlying reality (e.g., lines of code roughly correlates with project size)
2. **Incentive**: When people know they're evaluated on it, they optimize for the metric rather than the reality

The moment a metric becomes a target (incentive role), the descriptive signal is corrupted. People find the shortest path to make the number look good — which is rarely the same as doing good work.

## Examples

| Domain | Metric | Gaming |
| -------- | -------- | -------- |
| Software | Lines of code | Verbose, redundant code; no refactoring |
| Software | Bug count closed | Closing trivial bugs, ignoring hard ones |
| Medicine | Surgical success rate | Surgeons rejecting high-risk patients |
| Policing | Crime statistics | Downgrading felonies to misdemeanors |
| Education | Test scores | Teaching to the test, neglecting untested subjects |
| Academia | Citation count | Citation rings, self-citation, salami slicing |

## Related Formulations

- **Campbell's Law**: "The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures and the more apt it will be to distort and corrupt the social processes it is intended to monitor."
- **Cobra effect**: Named for a British colonial policy in India that offered bounties for dead cobras — people started breeding cobras to collect bounties. When the policy was scrapped, breeders released their cobras, making the problem worse.

## Mitigation

- Use metrics for **diagnostic monitoring**, not external judgment (see [[metric-fixation]])
- Combine quantitative metrics with qualitative judgment
- Rotate metrics regularly — don't let one number dominate for years
- Measure multiple dimensions — a single KPI is trivially gameable
- Trust professional ethos and intrinsic motivation where it exists

---

- Underpins [[metric-fixation]] — Goodhart's Law is the mechanism; metric fixation is the organizational pathology
- Related to [[complexity-metrics]] — quantitative code metrics are subject to the same gaming
- Source: [[sources/tyranny-of-metrics]]
