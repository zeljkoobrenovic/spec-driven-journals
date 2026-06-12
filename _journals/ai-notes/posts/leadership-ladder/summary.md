---
timetoread: 2 min
---

Better prompts are not the real transition. As AI moves from small tasks toward agentic workflows — architecture reviews, delivery planning, multi-step code changes — the leadership skill shifts from giving better commands to expressing clearer **intent**: purpose, context, constraints, review boundaries, and accountability. David Marquet's Intent-Based Leadership supplies the language; the post adapts it as an analogy, not a claim that AI is a person or moral agent.

The core mechanism is a seven-level **Human-AI Leadership Ladder**: command → prompt → critique → recommendation → intent → bounded delegation → monitored autonomy. Lower levels are not bad — they are right for narrow, low-risk, verifiable tasks. Most leadership failures happen when people use **high-autonomy tools with low-maturity language**.

**What changes**

- Interaction language carries the leadership structure: "I intend to achieve X under constraints Y; ask clarifying questions before recommending" instead of "write a strategy."
- AI's role splits cleanly from the leader's: AI generates options, drafts plans, compares trade-offs, finds risks; leaders decide what matters here, choose the accountable path, and own consequences. **False delegation** — treating generated artifacts as if they contain judgment — is the central risk.
- A spec becomes the written boundary between human intent and AI execution ([[spec-driven-authoring]]): intent, success criteria, non-goals, and review expectations made inspectable *before* the AI acts.
- Autonomy is earned through three gates: intent is clear, competence is demonstrated, control is bounded. Any "no" → stay lower on the ladder.

**What it costs**

- Guardrails that scale with autonomy: scope, competence evidence, observability, review checkpoints, stop conditions, rollback, named ownership. *Autonomy without observability is not delegation; it is drift.*
- More upfront clarity from the leader — intent statements and lightweight specs take more effort than commands, deliberately: they slow the work down before confidence outruns clarity.

**What we are not doing**

- Not a Marquet book summary, a generic prompt-engineering guide, or an AI-agent governance policy.
- Not claiming AI has intent, ownership, or moral agency — and not endorsing broad autonomy without competence evidence, auditability, and human override.

The Article tab has the full ladder table, two worked examples (architecture trade-off review, delivery-risk review), the guardrail tests, and a this-week practice template. Companion post: [[prepare-for-ai-future]].
