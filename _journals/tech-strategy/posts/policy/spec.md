---
status: draft
revised: 2026-05-20
---

# Spec: Policy — Nine Core Policies, Five Decision Rules, Refusals

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Turn the [[diagnosis]] and [[implications]] into **explicit decision
rules** that engineers can apply at the point of choice. Three
components: nine core policies (direction), five decision rules
(application), and a refusal list (negative application when no
positive option fits). The post is the most directly applicable layer
of the strategy.

## Audience

- **Engineers and tech leads** making real architectural choices.
- **Strategy reviewers** at [[operate]] forum evaluating exceptions.
- **Architecture group** ratifying proposals against the policy.

## Success criteria

- [ ] Reader can name the nine core policies and what each commits
      to.
- [ ] Reader can apply the five decision rules to a real choice
      without ambiguity.
- [ ] Reader knows when to refuse an option (the refusal list is
      explicit).
- [ ] Reader can trace each policy back to a diagnosis theme and an
      implication.

## Non-goals

- Detailing how each policy is operationalised (that's in the
  blueprints — [[backend-convergence]], [[delivery-path]],
  [[aws-accounts]], [[ownership-clarification]]).
- Wishlist or aspirational policies — every policy is grounded in
  diagnosis.
- Defining the exception process (that's [[operate]]).

## Open questions

- Whether nine policies are too many to remember in practice; would
  a smaller set be more usable.
- How rigid the refusal list should be — when should refusals get
  reviewed for currency.

## Decision log

- **2026-05-20** — Structured the policy in **three components**
  (policies, decision rules, refusals). Considered a single long
  list; rejected because the three layers serve different needs
  (direction, application, negation).
- **2026-05-20** — Tied each policy to a **specific diagnosis
  theme**. Considered making the policies self-contained; rejected
  because traceability back to evidence is what makes the policies
  testable.
- **2026-05-20** — Wrote a **refusal list**, not just a default
  list. Considered allowing implicit refusal; rejected because
  explicit refusal is the only thing that works when no positive
  option fits.

## Sources

- **Internal**
  - [[diagnosis]] — the evidence base.
  - [[implications]] — the constraint layer.
  - [[strategy]] — the overall frame.
  - [[operate]] — handles policy exceptions.
- **External**
  - Rumelt, *Good Strategy / Bad Strategy* — informs the
    diagnosis-implications-policy structure.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
