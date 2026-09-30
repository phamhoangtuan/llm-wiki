---
title: "Nash Equilibrium"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [game-theory, strategy, equilibrium, economics]
sources: [game-theory-bonanno]
---

# Nash Equilibrium

The foundational solution concept in non-cooperative [[game-theory|game theory]]: a strategy profile where no player can improve their payoff by *unilaterally* changing their strategy, given what everyone else is doing.

## Intuition

A Nash equilibrium is a "resting point" — once reached, no individual has an incentive to deviate. It's not necessarily the *best* outcome; it's the *stable* one.

## Pure vs. Mixed Strategies

- **Pure Strategy**: A single deterministic choice (always play Rock)
- **Mixed Strategy**: A probability distribution over choices (play Rock 1/3, Paper 1/3, Scissors 1/3)
- Every finite game has at least one Nash equilibrium — but it may require mixed strategies

## Types of Nash Equilibria

| Type | Context | Key Property |
| ------ | --------- | ------------- |
| Nash Equilibrium | Simultaneous-move games | No unilateral deviation |
| Subgame-Perfect Equilibrium (SPE) | Dynamic games | Nash in every subgame — eliminates non-credible threats |
| Bayesian Nash Equilibrium | Incomplete information | Optimize given probabilistic beliefs about opponent types |

## Limitations

- **Multiplicity**: Many games have multiple equilibria — which one will players coordinate on?
- **Unreasonable equilibria**: Some Nash equilibria rely on threats that wouldn't be carried out (refined by SPE, PBE)
- **Rationality assumption**: Players must be perfectly rational — real humans often aren't

## Examples

> **Prisoner's Dilemma**: Both confessing is Nash (neither can improve by staying silent alone), but mutual silence is collectively better.

> **Coordination Game**: Driving on the left vs. right — two Nash equilibria; social convention picks one.

---

- Central to [[game-theory]] — the core solution concept for strategic interaction
- Refined by subgame-perfect equilibrium (SPE) and Perfect Bayesian Equilibrium (PBE)
- Applied in economics, political science, evolutionary biology, and AI multi-agent systems
