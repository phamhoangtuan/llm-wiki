---
title: "Vibe Coding"
type: concept
tags: [ai-engineering, coding, methodology, terminology]
created: 2026-06-15
updated: 2026-06-15
sources: [practical-guide-ai-native-engineer]
aliases: [vibe-coding]
---

## Summary

**Vibe Coding** is a term coined by Andrej Karpathy in early 2025 to describe the practice of non-engineers building functional software by describing what they want to AI agents — without understanding the underlying code. It represents the democratization of software creation, but it is categorically different from professional [[ai-native-engineering]].

## Vibe Coding vs AI-Native Engineering

| Dimension | Vibe Coding | AI-Native Engineering |
|---|---|---|
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

---

- Contrasts with [[ai-native-engineering]] — AI-native engineering is the professional discipline; vibe coding is the democratized subset
- Related to [[technological-centaur]] — vibe coding is pure AI reliance; the centaur model requires human expertise directing AI
- Risk factor for [[code-overload]] — when professional teams adopt vibe coding practices, code overload follows
- Benchmark source: [[sources/practical-guide-ai-native-engineer]] — ByteByteGo article placing vibe coding in context
