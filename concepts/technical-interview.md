---
title: "Technical Interview"
type: concept
tags: [interview, algorithms, problem-solving, career]
created: 2026-06-08
updated: 2026-06-15
sources: [cracking-the-coding-interview, de-coding-technical-interview]
aliases: [coding-interview, technical-interview-philosophy]
---

## Summary

Technical interviews are not knowledge tests — they assess problem-solving ability under pressure. The interviewer evaluates relative performance (comparing against their "mental database" of past candidates) using a risk-averse decision model where false positives (hiring the wrong person) are far worse than false negatives (rejecting the right person).

## The Evaluation Model

### Relative Evaluation

Interviewers don't grade on an absolute scale. They compare you against everyone previously interviewed with the same question. Their mental database: "Alex took 30 minutes, Bella took 50, Ellie took 10 and presented a solution even the interviewer hadn't considered."

**Lesson**: Don't panic on hard problems. If you survive where others failed, you win.

### False Positives vs False Negatives

| Outcome | Definition | Company Attitude |
|---|---|---|
| **False Positive** | Hiring someone underqualified | Extremely dangerous — costly, damages culture |
| **False Negative** | Rejecting a qualified candidate | Acceptable — better safe than sorry |

> **Consequence**: You are a liability until proven otherwise. If you're "on the fence," you get a No-hire.

## Company-Specific Cultures

Each Big Tech company has distinct interview DNA:

| Company | Focus | Unique Element |
|---|---|---|
| **Amazon** | Scalability & OOD | **Bar Raiser** — independent interviewer with veto power to maintain hiring standards |
| **Google** | Algorithms & analytics | **Hiring Committee** — interviewers submit feedback, a separate committee decides |
| **Facebook** | "Build fast" startup spirit | **Jedi** (behavioral) / **Ninja** (coding) / **Pirate** (system design) roles |
| **Microsoft** | Tech passion, office interviews | **As App** — final interview with Hiring Manager is a strong positive signal |
| **Apple** | Product fanatics | 2-on-1 format, often includes Director/VP |
| **Palantir** | Extremely hard algorithm questions | HackerRank tests to filter algorithmic performance |

### Bar Raiser (Amazon)

An interviewer from a different team with veto power. Their job is not to defeat you — it's to ensure you're better than 50% of people currently in the role. If one interview feels significantly harder than others, it might be the Bar Raiser — don't panic.

### Hiring Committee (Google/Facebook)

Interviewers don't decide whether you're hired. They submit feedback packets. An independent committee reviews all packets and makes the final decision. This means: **give interviewers data they can defend in committee**.

## The BUD Optimization Technique

After finding a working solution, optimize it by examining three lenses:

| Lens | Question |
|---|---|
| **Bottlenecks** | Where is the program slowest? |
| **Unnecessary Work** | Which steps aren't actually needed? |
| **Duplicated Work** | What's being recomputed that could be cached? |

BUD ensures you don't stop at the first solution — you demonstrate the analytical thinking interviewers crave.

## Talk Aloud Rule

The whiteboard has no compiler — it's a communication tool. If you're silent, the interviewer has no data to defend you to the Hiring Committee. Explain your logic as you write code. If stuck, verbalize your thought process — interviewers may give hints that rescue you.

## Whiteboarding: Friend, Not Enemy

Whiteboarding isn't "unrealistic." It's a deliberate abstraction that:
- Forces focus on algorithmic logic (the "meaty parts"), not syntax
- Encourages communication instead of staring at a screen
- Protects you — minor syntax errors are irrelevant; analytical depth is what matters

## Patterns Over Memorization

- **Wrong**: Memorizing solutions to 500 LeetCode problems
- **Right**: Learning problem-solving patterns (templates of thought)
- When a familiar problem appears with a twist, pattern-understanders adapt — rote memorizers fail.

---

- Complementary to [[system-design-interview]] — technical interviews test algorithms/PoC, system design tests architecture/scale
- Contrasted with [[case-interview]] — technical interviews test coding and algorithms; case interviews test business judgment and structured thinking
- Benchmark source: [[sources/cracking-the-coding-interview]] — McDowell's 708-page guide
- Benchmark source: [[sources/de-coding-technical-interview]] — Bostian's 138-page guide with 5-step problem-solving cycle
