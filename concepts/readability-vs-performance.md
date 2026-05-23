---
title: "Readability vs Performance"
type: concept
tags: [design-principles, optimization, clean-code]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
aliases: [premature optimization, pareto performance]
---

## Summary

Many teams fall into the trap of premature optimization — sacrificing readability to chase performance gains that aren't significant. The correct priority: clean, readable code first, then measure and optimize bottlenecks.

## The Pareto Strategy

1. Write clean, readable code first
2. Cover with tests to ensure correctness
3. Measure actual performance (profiling)
4. Apply Pareto: optimize the 20% of bottlenecks causing 80% of problems

## Why This Works

> Clean code makes it easier to identify true bottlenecks. Code that's a tangled mess is hard to profile even if you try.

## Linguistic Relativity in Code (Sapir-Whorf Hypothesis)

> "The language you use shapes how you perceive the world."

- If your language only has `int` and `String`, you'll think of domain objects as "data holders"
- If your language supports value objects, immutability, type safety, you'll naturally build rich behavioral models

## Connections

- Supports [[software-as-simulation]] — readable code is a better simulation
- Enabled by [[rich-domain-model]] — rich objects are more readable than scattered procedural logic
- Related to [[technological-centaur]] — clean code enables effective human-AI collaboration
- Related to [[essential-accidental-complexity]] — premature optimization adds accidental complexity
