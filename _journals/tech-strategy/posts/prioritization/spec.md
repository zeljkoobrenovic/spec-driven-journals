---
status: draft
revised: 2026-05-20
---

# Spec: Prioritization and Waves

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Provide a **five-dimension scoring method** for ranking simplification
candidates (delivery friction, stability risk, ownership confusion,
fragmentation impact, ease of action), with a guardrail against
ease-only prioritisation. Apply the method to candidates from
[[first-targets]] and produce an initial Wave 1, Wave 2, and
Investigation Queue. The score is a **decision aid, not a decision**.

## Audience

- **[[operate]] forum** running the wave reviews.
- **Strategy owner** validating prioritisation against [[policy]].
- **Engineering leadership** sequencing investment.
- **Domain owners** scoring candidates from their area.

## Success criteria

- [ ] Reader can score a new candidate using the five dimensions
      without ambiguity.
- [ ] Reader understands the **ease-only guardrail** and why it
      exists.
- [ ] Reader knows the Wave 1 focus (delivery path + ownership) and
      why Wave 2 (backend convergence) waits.
- [ ] Reader knows the score is **a decision aid**, not the
      decision.

## Non-goals

- Replacing judgement with a number.
- Defining candidate-specific actions (that's the blueprints).
- A fully formalised optimisation model.

## Open questions

- Whether the 1-5 scale per dimension needs anchoring examples to
  reduce scorer drift.
- How often to re-score waves as new evidence arrives.

## Decision log

- **2026-05-20** — Chose **five dimensions** for scoring. Considered
  more (cost, risk, stakeholder alignment); rejected because each
  extra dimension reduces the discriminatory power of the score.
- **2026-05-20** — Added the **ease-only guardrail**. Considered
  trusting the score; rejected because ease tends to dominate sums
  and produce wave plans that ship lots of low-value work.
- **2026-05-20** — Made the score **sum**, not weighted average.
  Considered weighting; rejected because weighting hides judgement
  inside the math and the [[operate]] forum should make weighting
  explicit.
- **2026-05-20** — Created an **Investigation Queue** for
  high-impact items needing more mapping. Considered forcing
  everything into waves; rejected because waving unscoped items
  produces hidden risk.

## Sources

- **Internal**
  - [[first-targets]] — what gets scored.
  - [[policy]] — what the score serves.
  - [[operate]] — runs the wave reviews.
- **External**
  - Lean prioritisation literature — informs the multi-dimension +
    guardrail framing.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
