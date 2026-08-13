---
status: accepted
revised: 2026-08-13
---

# Spec: The Four Pillars of Platform Engineering

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the structural test I apply before I call anything in my organization a
platform. The post turns the four-pillars chapter of Fournier and Nowland's
*Platform Engineering* into an operating principle: a real platform is (1) a
curated product with paved paths, (2) built on software abstractions that
genuinely manage complexity, (3) consumable self-service by a broad base of
application developers, and (4) operated as a reliable foundation for the
business. Miss a pillar and what you have is tooling, provisioning, or
infrastructure enablement wearing a platform badge. The load-bearing idea:
the running test is whether the platform actually manages complexity for
application developers or merely moves it somewhere else.

## Audience

Platform leads and teams in my organization (so they know the bar their
offering is held to); infrastructure and DevTools leaders deciding what to
call a platform and fund as one; peer executives assessing platform maturity.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight names all four pillars and the
      key test: managing complexity for application developers versus merely
      relocating it.
- [x] **Pillar 1 survives** — curated product: identified customers,
      customer-driven priorities, explicit scope opinion, paved paths that
      cover most recurring needs, developers can leave the path, "railway"
      platforms for common gaps, success measured by customer outcomes.
- [x] **Pillar 2 survives** — software-based abstractions: real software
      built by platform engineers, APIs over underlying systems, no hiding
      without genuine productivity gain, thick clients with a lifecycle plan,
      OSS customized when needed, metadata (ownership, usage, access, cost,
      dependencies, migration impact) collected automatically.
- [x] **Pillar 3 survives** — broad developer base: many teams, varied skill
      levels, self-service onboarding and provisioning, multiple interfaces
      (UI/CLI/API/SDK/config-as-code), user observability, guardrails with
      safe defaults, deliberate multitenancy so the platform gets cheaper as
      adoption grows.
- [x] **Pillar 4 survives** — operated as a foundation: platform team owns
      the operational experience of the complete offering including cloud,
      OSS, and vendor layers; incident ownership, SLOs, capacity, runbooks,
      on-call; support treated as product feedback.
- [x] **The scorecard survives** — the quick four-pillar scorecard (0/1/2
      per pillar) with its interpretation bands is reproduced in the
      checklist; the source's "Development" pillar label is glossed as
      software abstractions to match the record's pillar names.
- [x] **Supporting quality dimensions survive** — the checklist reproduces
      the chapter's dimensions beyond the four pillars: architecture quality,
      developer experience, IDP only if needed, cost/security/governance, and
      AI/ML platform considerations (checklist §5–§9), acknowledged in the
      article's How to Read This.
- [x] **Credit is explicit** — References name Fournier and Nowland's
      *Platform Engineering* and the four-pillars chapter.

## Non-goals

- Not [[what-is-platform-engineering]] — that record argues why platform
  engineering exists; this one defines what qualifies as a platform once you
  build it.
- Not [[platform-as-a-product]] — that record carries the full product
  operating mechanics; pillar 1 here only states the curated-product bar.
- Not [[operating-platforms]] — that record covers operating discipline in
  depth; pillar 4 here only states the foundation bar.
- Not [[building-platform-teams]] — staffing and team-shape mechanics live
  there, even though pillar 2 implies the skills mix.

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

- **2026-08-12** — Grounded in the four-pillars chapter of Camille Fournier
  and Ian Nowland, *Platform Engineering: A Guide for Technical, Product, and
  People Leaders* (O'Reilly, 2024), via its chapter checklist — read through
  a practitioner-executive lens, as with every record in this journal.
- **2026-08-12** — Framed as a qualification test rather than a maturity
  ladder: the chapter's distinctive claim is that all four pillars must hold
  or the offering is tooling rather than a platform, so the record commits to
  the conjunction and keeps the scorecard as the fast assessment.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Four Pillars.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`), including the quick four-pillar scorecard.
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the
    four-pillars chapter.

## Changelog

- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
