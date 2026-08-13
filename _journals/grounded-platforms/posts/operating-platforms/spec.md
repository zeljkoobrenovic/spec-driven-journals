---
status: accepted
revised: 2026-08-12
---

# Spec: Operating Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I expect platform teams to operate what they build: operational
work as a core, ongoing part of platform engineering — not an interruption
to it. The post turns the "Operating Platforms" chapter of Camille Fournier
and Ian Nowland's *Platform Engineering* into an operating principle:
platform teams own three core practices — on-call, user support, and
operational feedback — in a merged DevOps model with sustainable,
measurable load limits; support is structured by levels and separated from
critical on-call; and operational signals (SLOs, change management,
synthetic monitoring, operational reviews) close the loop back into
engineering priorities. The load-bearing idea: the engineers who build the
platform operate it, and operational load is a managed quantity with
explicit numbers, not background noise.

## Audience

Platform team leads and engineering managers in my organization (so they
know the operational bar and the load limits I hold them to); platform
engineers who need to see why on-call and support are part of their job;
peer executives comparing platform operating models. First-person
declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the three core practices
      (on-call, support, operational feedback), the merged DevOps model,
      that operational load is measured and bounded, and that operational
      work is core platform engineering.
- [x] **The on-call side survives** — 24×7 coverage where the business
      needs it, merged rotation with platform expertise, the load limits
      (1 week in 4, ideally 1 in 6–8; fewer than five meaningful pages per
      engineer per week), alert quality, secondary on-call, and
      compensation fairness.
- [x] **The support side survives** — engineers participate in support,
      request categorization and support levels, critical-incident
      definition, separating noncritical support from on-call, support
      specialists, far-flung time zones, and scaling with an engineering
      support organization.
- [x] **The feedback side survives** — few meaningful customer-facing SLOs
      vs broader internal ones, change management, synthetic monitoring,
      weekly and organization-level operational reviews, and closing the
      loop into engineering priorities.
- [x] **Credit is explicit** — References name Camille Fournier and Ian
      Nowland's *Platform Engineering* and the "Operating Platforms"
      chapter.

## Non-goals

- Not [[platform-as-a-product]] — that record treats reliability as part of
  the product experience; this one carries the operational machinery behind
  that promise.
- Not [[building-platform-teams]] — support-specialist hiring appears here
  only as an operational scaling move; the full staffing model lives there.
- Not [[planning-and-delivery]] — this record feeds operational signals
  into priorities; the planning mechanics that absorb them live there.
- Not an incident-management runbook or a tooling guide — the record sets
  the operating practices and limits, not the pager vendor.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-12** — Grounded in the "Operating Platforms" chapter of Camille
  Fournier and Ian Nowland, *Platform Engineering: A Guide for Technical,
  Product, and People Leaders* (O'Reilly, 2024), via its chapter checklist
  — read through a practitioner-executive lens, as with every record in
  this journal.
- **2026-08-12** — Framed around "operational work is core platform
  engineering, with explicit load limits" rather than a generic SRE primer:
  the chapter's distinctive claims are the merged DevOps rotation, the
  concrete on-call numbers, and the support/on-call separation.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Operating
    Platforms.pdf` — the chapter checklist; reproduced, adapted, in the
    Checklist tab (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the
    "Operating Platforms" chapter.

## Changelog

- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
