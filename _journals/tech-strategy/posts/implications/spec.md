---
status: draft
revised: 2026-05-20
---

# Spec: Strategic Implications

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Bridge [[diagnosis]] and [[policy]]: turn the diagnosis into **eight
load-bearing implications** that narrow the space of acceptable policy
choices. The post should sit between description and prescription —
neither evidence nor decision rules, but the constraints the rules must
respect. If a future policy contradicts an implication, either the
implication or the diagnosis needs to change.

## Audience

- **Policy authors** writing or revising the policy document.
- **Tech leads** evaluating whether a specific proposal respects the
  strategy.
- **Strategy reviewers** at the [[operate]] forum testing proposals
  against the implications.

## Success criteria

- [ ] Reader can list the eight implications and what each constrains.
- [ ] Reader knows each implication is paired with a downstream
      policy.
- [ ] Reader can use the implications to test whether a proposal
      respects the strategy.
- [ ] Reader understands the implications are **not yet policy** —
      they narrow the space, not define the rules.

## Non-goals

- Writing the policy itself (that's [[policy]]).
- Listing every consequence of the diagnosis — only the load-bearing
  ones.
- Quantifying the implications.

## Open questions

- Should "strong defaults beat broad optionality" be elevated to a
  policy of its own.
- Whether the eight count is right, or whether some should merge.

## Decision log

- **2026-05-20** — Chose **eight implications**. Considered fewer
  (three or four) for sharpness; rejected because each of the eight
  is genuinely load-bearing and merging them would obscure the
  trade-offs.
- **2026-05-20** — Inserted the **implications layer** between
  diagnosis and policy. Considered going straight from diagnosis to
  policy; rejected because the policy needs a constraint surface to
  be tested against, and the diagnosis alone is too descriptive to
  do that.
- **2026-05-20** — Made each implication **pair with a downstream
  policy**. Considered keeping them abstract; rejected because the
  pairing makes the implications testable against the policy text.

## Sources

- **Internal**
  - [[diagnosis]] — what these implications respond to.
  - [[policy]] — what these implications constrain.
  - [[strategy]] — the overall frame.
- **External**
  - Rumelt, *Good Strategy / Bad Strategy* — informs the
    diagnosis/implications/policy separation.

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
