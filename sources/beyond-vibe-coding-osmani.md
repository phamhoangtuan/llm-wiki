---
title: "Beyond Vibe Coding"
type: source
source_type: book
author: "Addy Osmani"
url: ""
source_date: 2025-12-07
ingested: 2026-08-24
tags: [ai-engineering, coding, qa, security, methodology]
concepts: [vibe-coding, ai-native-engineering, code-overload, specification-driven-development, context-engineering, harness-engineering]
---

## Summary

Addy Osmani's 387-page guide distills the core principles for professional engineers using AI coding assistants effectively. The central thesis: the future developer is an **Architect, Orchestrator, and Reviewer** — leveraging AI's speed while applying human judgment to the critical 30% of engineering work that AI cannot handle.

## Key Ideas

### The 70% Problem

AI generates the majority of functional code, but the final 30% — edge cases, security, architecture, maintainability — demands deep human expertise. "Trust but verify": treat all AI output as a draft from an "eager junior developer."

### The Engineering Spectrum

Use [[vibe-coding]] for rapid prototyping and boilerplate (zero-to-one). Switch to AI-Assisted Engineering (Plan-First) for production code where sustained reliability is paramount. The key insight: **never stop learning** — use AI as a tutor, not a crutch.

### Five Disciplines

1. **Adopt the Engineering Mindset** — anchor in quality and discipline; acknowledge the 70% problem
2. **Master Programming with Intent** — be specific, focus on intent (what not how), iterate conversationally, leverage autonomous agents for delegation
3. **Implement Quality Assurance** — validate against intent, test immediately, debug yourself first, refactor continuously, isolate AI changes in separate commits
4. **Ensure Security and Ethics** — audit for vulnerabilities (SQL injection, hardcoded secrets), scan with SAST tools (Bandit, CodeQL, Snyk), protect sensitive data in prompts, comply with IP, mitigate bias
5. **Evolve Your Developer Role** — shift from routine coding to architecture, orchestration, systems thinking, curation, and domain expertise

### Role Evolution

| From | To |
| --- | --- |
| Writing routine boilerplate | Architect & Planner |
| Implementing simple features | Orchestrator & Integrator |
| Fixing straightforward bugs | Systems Thinker & Debugger |
| Remembering syntax details | Curator & Reviewer |
| Pure coding skills | Domain Expert & Communicator |

### Security Imperative

Never expose proprietary data, client PII, or real secrets in prompts. Treat AI-generated code as having ambiguous IP license. Integrate SAST scanners into IDE and CI.

---

- Related to [[vibe-coding]] — Osmani extends Karpathy's framing with practical engineering discipline
- Related to [[ai-native-engineering]] — both describe the orchestrator model; Osmani adds the 5-discipline framework
- Related to [[code-overload]] — the NYT term appears in both Osmani and ByteByteGo sources
- Related to [[harness-engineering]] — Osmani's QA discipline maps to harness engineering's verification-first approach
- Related to [[specification-driven-development]] — "focus on intent" is specification-driven development in practice
- Related to [[context-engineering]] — "be specific and clear" is context engineering at the prompt level
- Benchmark source: [[sources/new-sdlc-vibe-coding]] — complementary framing from Osmani, Saboo & Kartakis
- Benchmark source: [[sources/practical-guide-ai-native-engineer]] — ByteByteGo's AI-native engineering guide
