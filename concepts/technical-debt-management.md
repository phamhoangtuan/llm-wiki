---
title: "Technical Debt Management"
type: concept
tags: [technical-debt, migrations, engineering-management, maintainability, architecture]
created: 2026-08-18
updated: 2026-09-30
sources: [an-elegant-puzzle, software-engineering-at-google, leading-effective-engineering-teams-osmani]
aliases: [technical debt, migration management]
---

## Summary

**Technical debt management** is the deliberate control of design and implementation choices whose future cost threatens delivery, reliability, or changeability. It is not a cleanup queue to attack whenever time appears; it is a capacity and migration problem.

## The Migration Playbook

A scalable migration has three phases:

1. **De-risk** — embed the change with a team that understands the old and new paths.
2. **Enable** — provide tooling, documentation, compatibility layers, and defaults that make adoption cheaper than staying put.
3. **Finish** — migrate remaining users, remove the old path, and stop new debt from accumulating.

Small changes, explicit dependency versions, automated large-scale changes, and predictable releases make debt reduction safer.

## Management Rules

- Diagnose whether debt is the actual constraint before hiring or adding process.
- Reduce work in progress when the team is treading water.
- Give debt repayment enough uninterrupted time for benefits to compound.
- Update broken policies instead of granting one-off exceptions.
- Use dashboards and directional metrics to find debt that affects users or delivery.

## The Career Tax (Osmani)

Osmani frames context-free code as a **"career tax"** (source: [[sources/leading-effective-engineering-teams-osmani]]): coding without understanding the *Why* produces technical debt that "steals" your future time — output that will have to be redone. The antidote ties debt back to [[output-vs-outcome]]: before writing code, ask what outcome it serves; if the answer is absent, the work is likely to become debt.

## Connections

- Operationalized by [[engineering-management]] through team-health diagnosis and migration leadership.
- Supported by [[continuous-delivery]] because small, reversible changes lower migration risk.
- Related to [[software-rot]] and [[refactoring-at-scale]].
- Related to [[output-vs-outcome]] — context-free, Why-less code becomes debt.
- Benchmark sources: [[sources/an-elegant-puzzle]] and [[sources/software-engineering-at-google]].
