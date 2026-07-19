---
title: "Game Theory"
type: concept
created: 2026-07-13
updated: 2026-07-13
tags: [game-theory, strategy, economics, decision-making, mathematics]
sources: [game-theory-bonanno]
---

# Game Theory

The mathematical study of strategic interaction among rational decision-makers — where each player's outcome depends on the actions of others. Focus on **non-cooperative game theory**: each player optimizes their own payoff.

## The Spectrum: Ordinal → Cardinal → Beliefs → Refinements → Incomplete Information

### Strategic Form Games (Simultaneous Moves)

All players choose actions at the same time. Core solution concepts:

- **Dominance**: A strategy that's always better regardless of what others do
- **IDSDS**: Iteratively remove dominated strategies until only rational choices remain
- [[nash-equilibrium|Nash Equilibrium]]: A state where no player wants to unilaterally deviate

### Dynamic Games (Sequential Moves)

Players move in sequence; later players observe earlier moves:

- **Backward Induction**: Solve from the end backward — think ahead to decide now
- **Information Sets**: Model what a player knows (or doesn't) about prior moves
- **Subgame-Perfect Equilibrium (SPE)**: Nash that holds in every subgame — eliminates non-credible threats

### Expected Utility & Mixed Strategies

When outcomes involve risk:

- **Expected Utility (vNM)** : Rank probabilistic outcomes (lotteries) by expected value
- **Mixed Strategies**: Randomize choices to keep opponents indifferent — essential when no pure equilibrium exists

## Common Knowledge

A fact is *common knowledge* when everyone knows it, everyone knows everyone knows it, ad infinitum. Traffic lights are common knowledge; private information isn't. Common Knowledge of Rationality (CKR) implies players won't choose dominated strategies.

## Equilibrium Refinements

Nash equilibrium often produces too many outcomes — including unreasonable ones. Refinements (Sequential Equilibrium, Perfect Bayesian Equilibrium) add plausibility constraints to filter out non-credible threats.

## Incomplete Information

The Harsanyi Transformation converts "unknown opponent types" into imperfect information by adding a "Nature" move. Bayesian Nash Equilibrium: each player optimizes based on probabilistic beliefs about opponent types.

## Applications

Beyond economics: evolutionary biology, political science, computer science (algorithmic game theory, mechanism design), AI (multi-agent systems, adversarial training).

---

- Defines [[nash-equilibrium]] — the foundational solution concept
- Uses backward induction — sequential reasoning from end to start
- Connects to [[essential-accidental-complexity]] — strategic interaction as a form of essential complexity
