---
title: "Vibe Coding"
type: concept
tags: [ai-engineering, coding, methodology, terminology]
created: 2026-06-15
updated: 2026-08-06
sources: [practical-guide-ai-native-engineer, new-sdlc-vibe-coding, graph-engineering-karpathy]
aliases: [vibe-coding]
---

## Summary

**Vibe Coding** is a term coined by Andrej Karpathy in early 2025 to describe the practice of non-engineers building functional software by describing what they want to AI agents — without understanding the underlying code. It represents the democratization of software creation, but it is categorically different from professional [[ai-native-engineering]].

## Vibe Coding vs AI-Native Engineering

| Dimension | Vibe Coding | AI-Native Engineering |
| --- | --- | --- |
| **Who** | Non-engineers, domain experts | Professional software engineers |
| **Requirement** | Ability to describe desired behavior | Deep coding knowledge + orchestration skills |
| **Code understanding** | Not required | Essential — for verification, debugging, integration |
| **Verification** | "Looks like it works" | Rigorous testing, security review, performance validation |
| **Context** | One-off prompts | Persistent, curated context layers |
| **Specifications** | Ad-hoc descriptions | Structured, milestone-based specs |
| **Failure mode** | Produces working demo that breaks at scale | Produces production-grade, maintainable systems |

> "Vibe coding has its place, but it's not engineering."

## Where Vibe Coding Adds Value

- **Prototyping**: Non-technical founders can validate ideas before hiring engineers
- **Internal tools**: Domain experts can build simple automation without involving engineering teams
- **Learning**: Beginners can explore programming concepts through experimentation

## Where Vibe Coding Fails

- **Production systems**: Security, performance, and reliability require engineering rigor
- **Scale**: Vibe-coded apps break under real load or edge cases
- **Maintainability**: Without code understanding, bugs compound and technical debt becomes irreversible
- **Team collaboration**: No shared standards, no version control discipline, no review process

## The "Code Overload" Connection

When professional engineers operate in vibe coding mode — generating code through AI without the four core practices of [[ai-native-engineering]] — the result is [[code-overload]]: more code velocity, more bugs, more incidents, more technical debt. Vibe coding is not wrong; it's wrong for production engineering.

## The Agentic Engineering Spectrum

Software development now exists on a spectrum of discipline between two poles:

| Dimension | Vibe Coding 🌊 | Agentic Engineering 🏗️ |
| --- | --- | --- |
| **Intent Specification** | Casual natural language prompts | Formal specs, architecture docs, memory files |
| **Verification** | Manual "Does it seem to work?" checks | Automated test suites + LM Judges/Evals |
| **Error Handling** | Reactive copy-paste error messages | Autonomous self-diagnosis within bounds |
| **Risk Profile** | 🔴 High (fine for prototypes/hackathons) | 🟢 Low (systematic verification for production) |
| **Token Economics** | ❌ High burn from trial-and-error loops | ✅ Optimized via high-signal context payloads |

**Applied rule**: "The higher the stakes, the tighter the harness." A weekend hackathon can be pure vibe coding. A production system handling financial transactions requires [[harness-engineering|agentic engineering]].

## Token Economics: The Hidden Interest Rate

Vibe coding appears cheap upfront but carries a "hidden interest rate" — the maintenance tax from trial-and-error loops, token burn, and accumulating technical debt:

| Approach | CapEx (Upfront) | OpEx (Ongoing) | Long-Term Viability |
| --- | --- | --- | --- |
| Vibe Coding 🌊 | 🟢 Low (just subscription) | 🔴 High ("Maintenance Tax" + token burn) | ❌ 3-10x cost crossover point |
| Agentic Engineering 🏗️ | 🔴 High (system design, test suites) | 🟢 Low (sustainable marginal costs) | ✅ Scalable economic model |

The financial insight: **high-signal context payloads (precise AGENTS.md) prevent trial-and-error loops that drive up API costs.** Investing in context engineering upfront pays for itself in reduced token burn and fewer wasted iterations.

> "Vibe coding's low CapEx is a teaser rate. The real cost is in the OpEx."

## Karpathy's Three-Stage Progression

Vibe coding is stage one of a three-stage progression described in [[graph-engineering]]:

1. **Vibe coding**: the human expresses intent and the model writes. No systematic verification, no durable state.
2. **Agentic engineering**: the human specifies, orchestrates, verifies, and remains responsible for quality. Loops, harnesses, evals.
3. **Graph engineering**: agents share durable state through typed, queryable graphs of work and knowledge. Memory and evaluation live outside context windows.

Each stage addresses a limitation of the previous: vibe coding lacks verification → agentic engineering adds it → graph engineering externalizes state from context windows into persistent structures.

---

- Contrasts with [[ai-native-engineering]] — AI-native engineering is the professional discipline; vibe coding is the democratized subset
- Contrasts with [[agent-loop]] — vibe coding skips the Perceive-Plan-Act-Observe cycle; agentic engineering runs it systematically
- Contrasts with [[agent-verification]] — vibe coding relies on "seems to work"; agentic engineering verifies both output and trajectory
- Related to [[technological-centaur]] — vibe coding is pure AI reliance; the centaur model requires human expertise directing AI
- Risk factor for [[code-overload]] — when professional teams adopt vibe coding practices, code overload follows
- Related to [[agent-quality-optimization]] — token economics reveal vibe coding's hidden OpEx costs
- Benchmark source: [[sources/practical-guide-ai-native-engineer]] — ByteByteGo article placing vibe coding in context
- Benchmark source: [[sources/new-sdlc-vibe-coding]] — spectrum comparison and token economics framework
- Stage one of [[graph-engineering]] — Karpathy's three-stage progression (vibe → agentic → graph)
- Source: [[sources/graph-engineering-karpathy]] — the three-stage framing
