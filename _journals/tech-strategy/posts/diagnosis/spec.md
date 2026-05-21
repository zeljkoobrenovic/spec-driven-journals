---
status: draft
revised: 2026-05-20
---

# Spec: Diagnosis — Inherited Complexity, Three Eras, Structural Fragmentation

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

Describe the **evidence base** that the rest of the [[strategy]]
responds to. Identify the mismatch between Organization Germany's inherited
estate and its actual business reality, name the three eras of layered
legacy, and concentrate the fragmentation evidence in backend, devex,
and the AWS account estate. Deliberately a **description, not a
prescription** — the prescription is in [[implications]] and [[policy]].

## Audience

- **Strategy authors** sanity-checking that policy responds to the
  right problem.
- **Tech leads** wanting to know why fragmentation is the headline
  concern.
- **Engineering leadership** evaluating whether the diagnosis still
  fits a year from now.
- **New joiners** asking why parts of the estate look the way they
  do.

## Success criteria

- [ ] Reader can state the diagnosis in one sentence:
      fragmentation, not technical sophistication.
- [ ] Reader can name the three eras and what each contributed.
- [ ] Reader knows the three strongest fragmentation areas: backend,
      devex, AWS account estate.
- [ ] Reader can use the diagnosis to challenge proposed policies
      that solve a different problem.

## Non-goals

- Prescribing what to do about the diagnosis (that's [[policy]]).
- Listing every fragmentation symptom — only the load-bearing ones.
- Naming specific teams or attributing the layering to individuals.
- Defining the target steady state.

## Open questions

- How to keep the diagnosis fresh as the estate evolves — when does
  it need re-validating.
- Whether to add quantitative evidence (account counts, service
  counts) to the qualitative description.

## Decision log

- **2026-05-20** — Made the diagnosis **descriptive, not
  prescriptive**. Considered folding diagnosis and policy into one
  document; rejected because separating evidence from response lets
  each be re-evaluated independently.
- **2026-05-20** — Concentrated evidence in **three load-bearing
  areas** (backend, devex, AWS accounts). Considered enumerating all
  fragmentation symptoms; rejected because a long list dilutes the
  strongest signals.
- **2026-05-20** — Framed the problem as **fragmentation**, not "lack
  of modern technology". Considered the modernisation framing;
  rejected because it leads to "buy/build more" responses that worsen
  fragmentation rather than fix it.

## Sources

- **Internal**
  - [[strategy]] — depends on this diagnosis being right.
  - [[implications]] — turns the diagnosis into strategic
    implications.
  - [[policy]] — responds to the diagnosis.
- **External**
  - Richard Rumelt, *Good Strategy / Bad Strategy* — informs the
    diagnosis/policy separation.
  - Documentation of AVIV White-Label era platform ambitions
    (internal).

## Changelog

- **2026-05-20** — Filled in during second-pass spec rewrite.
  *(Zeljko, AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide rollout.
  *(automated backfill)*
