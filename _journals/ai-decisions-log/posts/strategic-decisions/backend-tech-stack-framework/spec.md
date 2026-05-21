---
status: draft
revised: 2026-05-20
---

# Spec: Backend Services Platform — Standardize on .NET with C#

> Filled in during the second pass over backfilled specs. Status `draft`;
> keep this spec current with substantive post changes.

## Intent

State that .NET with C# is the default platform for Organization backend
services, name the narrow exceptions (small BFFs, simple API aggregation
in Node.js/TypeScript), and make the skills-investment cost explicit so
nobody is surprised by it later.

## Audience

- **Backend engineers** choosing a stack for a new service.
- **Tech leads** mentoring engineers stronger in TypeScript than C#.
- **Hiring managers** sizing the skills the platform requires.
- **Architecture group** evaluating exception requests for other
  languages.

## Success criteria

- [ ] Reader can pick the right platform for a new service without
      asking.
- [ ] Reader can identify when Node.js/TypeScript is acceptable (BFF,
      aggregation) and when it isn't (core, Kafka-driven, business
      logic).
- [ ] Reader sees the skills-investment cost as part of the decision,
      not a hidden surprise.
- [ ] Reader can trace the dependencies on
      [[infra-tech-stack-compute]] and [[infra-tech-stack-messaging]].
- [ ] The post stays focused as an ADR and does not absorb service-template,
      training-plan, or implementation-guide content.
- [ ] Vocabulary appears only as appendix reference material and does not
      interrupt the decision flow.

## Non-goals

- Picking specific .NET libraries, frameworks, or NuGet packages.
- Defining the service template contents.
- Replacing other language choices for non-core uses (data pipelines,
  ML tooling, ops scripts).
- Deciding the timeline for migrating existing services.

## Open questions

- What counts as a "narrow edge use case" in practice — concrete
  examples vs ambiguous ones.
- Skills-investment plan: training budget, mentoring pairs, timeline.

## Decision log

- **2026-05-20** — Kept vocabulary, but moved it to an appendix so the
  main ADR stays focused on the decision and consequences.
- **2026-05-20** — Trimmed the post from a long educational guide into a
  focused ADR. Kept the decision, exception boundary, rationale,
  consequences, team expectations, and revisit triggers; removed detailed
  code skeletons, lifecycle checklists, and learning-path content that
  belongs in platform documentation.
- **2026-05-20** — Chose **.NET with C#** as the default. Node.js with
  TypeScript was considered as the default; rejected because the
  target backend shape is business-logic-heavy, Kafka-driven, and
  long-running, which fits .NET's strong-typing + hosting model better.
- **2026-05-20** — Accepted **Node.js/TypeScript** for narrow edge
  cases (BFFs, simple aggregation). Considered banning it outright;
  rejected because frontend-adjacent glue is a legitimate use case
  and forcing it onto C# would slow UI work for no platform benefit.
- **2026-05-20** — Did **not** include Java, Kotlin, Go, Python as
  default options. Considered Kotlin given mobile alignment; rejected
  because mixing JVM languages in core backend would re-create the
  diversity this decision exists to remove.

## Sources

- **Internal**
  - [[infra-tech-aws]] — the cloud target this builds on.
  - [[infra-tech-stack-compute]] — the runtime target (ECS Fargate).
  - [[infra-tech-stack-messaging]] — the Kafka target on MSK.
- **External**
  - .NET LTS release schedule — informs the runtime baseline.
  - Node.js LTS schedule — informs when edge-case Node services need
    upgrade attention.

## Changelog

- **2026-05-20** — Refocused `index.md` into a shorter ADR and updated this
  spec with the scope-control criterion. Status remains `draft` pending
  human review. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Added vocabulary back as an end appendix rather than
  inline explanatory material. *(Zeljko, AI-mediated session)*
- **2026-05-20** — Filled in during second-pass spec rewrite. Status
  kept `draft`; updated during the focus and spec cleanup passes. *(Zeljko,
  AI-mediated session)*
- **2026-05-20** — Initial spec created as part of journal-wide spec-driven
  rollout. *(automated backfill)*
