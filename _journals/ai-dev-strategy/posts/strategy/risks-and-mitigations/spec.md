---
status: draft
revised: 2026-05-20
---

# Spec: Risks and Mitigations

> Filled in during the second pass over backfilled specs. Status `draft`.

## Intent

Enumerate **explicit risks** for agentic coding (vendor concentration,
hallucinated changes, stale instructions, secret exposure, prompt and
tool injection, over-automation, cost growth, architectural drift)
and pair each with a **named mitigation**.

## Audience

- **Architecture group** evaluating risk exposure.
- **Security and compliance** owning specific mitigations.
- **AI Engineering Enablement** implementing mitigations.

## Success criteria

- [ ] Reader can name the eight risks.
- [ ] Reader can identify the mitigation for each.
- [ ] Reader knows risk is **named and owned**, not implicit.

## Non-goals

- Eliminating risk (only reducing/owning it).
- Specifying mitigation rollout dates.

## Open questions

- How to detect architectural drift early.

## Decision log

- **2026-05-20** — Made risks **explicit and paired with
  mitigations**. Considered implicit risk acknowledgement; rejected
  because unnamed risks remain unmitigated.

## Sources

- **Internal**
  - [[ai-policy]] — the policy that handles many of these.
  - [[operating-model]] — owns incident response.
- **External**
  - OWASP LLM Top 10 — informs the injection risks.
  - Vendor concentration risk literature.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
- **2026-05-20** — Initial spec created.
