---
title: "AI Psychosis"
type: concept
tags: [ai, engineering-culture, leadership, organizational-behavior, risk]
created: 2026-06-17
updated: 2026-06-17
sources: [meta-destroying-engineering-org-orosz]
aliases: [AI Obsession, AI Delusion, AI Hype Disorder]
---

**AI Psychosis** is an organizational pathology where leadership becomes so fixated on AI — building it, adopting it, or optimizing for it — that they systematically destroy the engineering culture, operational reliability, and human capital that made their company successful (source: [[sources/meta-destroying-engineering-org-orosz]]).

Coined by Mitchell Hashimoto (founder of HashiCorp, creator of Ghostty), the term describes leaders who operate under an "almost absolute MTTR-is-all-you-need mentality" — believing AI agents will fix bugs so quickly and at such scale that traditional safeguards (testing, code review, resilient architecture) become obsolete.

## Symptoms

Organizations suffering from AI psychosis exhibit a recognizable pattern:

1. **Forced AI adoption metrics** — measuring and rewarding AI usage (token count, AI-generated commits) in performance reviews, incentivizing performative AI use over genuine engineering
2. **Core engineering treated as cost center** — reallocating the best engineers from business-critical systems to AI training/data labeling, signaling that shipping product matters less than training models
3. **Gutted safety teams** — cutting security, infra, and trust & safety headcount while pushing AI-generated code with AI-only review
4. **Surveillance for training data** — invasive monitoring (keystrokes, mouse clicks) of engineers to generate RLHF training data, with no opt-out
5. **Catastrophic failures become normalized** — outages caused by unreviewed AI-generated code are accepted as the cost of speed
6. **Talent exodus** — tenured engineers who built the company's systems leave en masse, replaced by those willing to optimize for token metrics

## The Meta Case Study

In 2026, Meta became the canonical example of AI psychosis in action:

| Action | Consequence |
|---|---|
| 30-50% of core engineers reassigned to data labeling | Infra/security teams gutted; institutional knowledge lost |
| Keystroke/mouse tracking deployed with no opt-out | Employee backlash; partial rollback after weeks of protest |
| Token count measured in PSC (performance review) | Engineers tokenmaxx — generate AI code for metrics, not quality |
| Trust & Safety team cut 50% | Instagram zero-auth password reset outage; CISO resignation |
| 10% layoffs announced with month-long waiting period | Fear-based paralysis; everyone optimizing exit strategy |

The result: Instagram suffered a zero-auth account takeover where an AI-powered support system handed password resets to any email address — a failure described as "the most unserious, 'almost too stupid to be true' security breach." The code was AI-generated and AI-reviewed with no human input. Meta's CISO resigned the next day.

## The Infrastructure Lesson: MTBF vs MTTR

Hashimoto draws a parallel to the infrastructure industry's cloud transition, where similar debates played out:

- **MTBF** (Mean Time Between Failures): Invest in preventing failures — resilient architecture, testing, redundancy
- **MTTR** (Mean Time To Recovery): Invest in recovering quickly from failures — automation, rollback, monitoring

The infrastructure industry learned that you "can automate yourself into a very resilient catastrophe machine" — systems appear healthy by local metrics while globally becoming incomprehensible. Bug reports go down while latent risk explodes. Test coverage rises while semantic understanding falls. Changes happen so fast that nobody notices architecture decaying.

AI psychosis repeats this mistake at the software development level, but with higher stakes — because AI agents can generate and ship bad code at unprecedented scale.

## Engineering as Profit Center vs Cost Center

A key dynamic in AI psychosis is leadership reclassifying engineering from **profit center** (builds products that generate revenue) to **cost center** (an expense to be optimized or repurposed for AI training).

Meta's shift was visible in:
- Engineers moved from building products used by 2B+ people to repetitive data labeling
- The clear signal: "the next AI model matters more than you do"
- Retention equity packages offered to key engineers — but seen as golden handcuffs, not appreciation

When engineers feel like cost centers, they optimize for personal metrics (token count) rather than business outcomes — a rational response to irrational incentives.

## "It's Not Just Meta"

Hashimoto notes he's seeing similar behavior across the industry: "There are entire companies right now under heavy AI psychosis and it's impossible to have rational conversations about it with them."

The pattern extends beyond Meta:
- Founders over-index on AI's capabilities and under-index on its failure modes
- "It's fine to ship bugs because agents will fix them" becomes the operating assumption
- Traditional engineering values (testing, review, documentation) are dismissed as obsolete
- Engineers who raise concerns are labeled "not getting it" or "afraid of change"

## How to Recognize and Resist

**For leaders**: Before making drastic org changes for AI-related reasons, examine Meta's outcome. Ask:
- Are we measuring AI usage in ways that incentivize performative behavior?
- Have we cut safety/security teams while increasing AI-generated code volume?
- Are our best engineers building products or training models?
- Would an AI-generated, AI-reviewed code change survive our outage postmortem?

**For engineers**: If your organization shows symptoms:
- Document concerns with specific examples, not abstract fears
- Frame arguments in terms of business risk, not engineering values
- Forward the Meta case study as additional context for leadership
- Build an exit strategy — the talent market rewards engineers who resisted AI psychosis

---

## Connections

- [[ai-native-engineering]] — Healthy AI-native engineering contrasts with AI psychosis: augmentation vs replacement, quality gates vs tokenmaxxing
- [[vibe-coding]] — Vibe coding (non-engineer AI-assisted coding) shares the "ship it, AI will fix it" mentality; AI psychosis applies this at the organizational level
- [[code-overload]] — AI psychosis accelerates code overload: more AI-generated code, less human review, compounding technical debt
- [[agentic-development-life-cycle]] — ADLC provides the structured framework that AI psychosis destroys: Plan→Build→Test→Review, not Generate→Ship→Pray
- [[staff-engineering]] — Staff engineers are often the first to leave when AI psychosis hits; their role is expanding surface area, which becomes impossible when surface area is being destroyed
- [[software-rot]] — AI psychosis accelerates software rot by removing the human review and intentional architecture that prevents decay
