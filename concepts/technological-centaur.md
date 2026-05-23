---
title: "Technological Centaur"
type: concept
tags: [ai, architecture, developer-role]
created: 2026-05-23
updated: 2026-05-23
sources: [contieri-clean-code-cookbook]
aliases: [AI assistant, human-AI collaboration, centaur developer]
---

## Summary

The "Technological Centaur" is the model of human architect + AI coding assistant working together. AI does not make architects obsolete — it makes clean code more important than ever.

## Why AI Produces Anemic Code

- Trained on large amounts of public code — mostly anemic and procedural
- Good at generating boilerplate and standard algorithms
- Weak at high-level architectural integrity
- Does not understand "reality" — only pattern-matches syntax

## The Centaur Model

```
[Human Architect] ←supervises→ [AI Code Generator]
         ↓
"Does this generated code maintain bijection with reality?"
"Is this object rich or anemic?"
"Does this mutation violate immutability of essence?"
```

## New Developer Roles

| Role | Responsibility |
|---|---|
| **Supervisor** | Review and correct AI "hallucinations" |
| **Designer** | Provide strategic vision that AI cannot simulate |
| **Guardian of Reality** | Ensure code faithfully reflects the business domain |

## Key Insight

> AI is a powerful tool, but human oversight is an architectural necessity. Clean code is the common language for effective human-machine collaboration.

## Connections

- Relies on [[software-as-simulation]] — humans understand reality, AI does not
- Requires [[rich-domain-model]] knowledge to review AI output
- Depends on [[bijection]] awareness to catch semantic errors AI introduces
- Related to [[readability-vs-performance]] — clean code enables effective AI collaboration
