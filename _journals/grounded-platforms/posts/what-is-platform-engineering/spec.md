---
status: accepted
revised: 2026-08-13
---

# Spec: What Is Platform Engineering

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State why I invest in platform engineering at all: as the way an organization
manages the complexity it has already accumulated. The post turns the
introductory chapter of Fournier and Nowland's *Platform Engineering* into an
operating principle: modern engineering organizations sink into an
"over-general swamp" of duplicated OSS, cloud services, and per-application
glue, and the way out is a platform treated as an internal product — curated,
self-service, with clear boundaries — built and operated by a dedicated team.
The load-bearing idea: a platform earns its keep when a small platform team
makes a much larger engineering organization measurably more productive, and
adoption grows because developers find it useful, not because it was mandated.

## Audience

Platform and infrastructure leaders in my organization (so they know what I
mean when I say "platform" and what I hold platform investment accountable
to); application-team leads deciding whether to adopt the platform path; peer
executives weighing platform investment against feature work. First-person
declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that platform engineering
      exists to manage accumulated complexity, that the platform is an
      internal product with clear boundaries, and that its test is leverage:
      a small platform team making a much larger organization more productive.
- [x] **The swamp diagnosis survives** — the over-general swamp: inventoried
      duplication, per-application glue, expensive migrations, and the move to
      curated abstractions that hide implementation complexity.
- [x] **The product stance survives** — interviewing developers, prioritizing
      user experience over infrastructure-team convenience, curated
      capabilities, incremental delivery, adoption and satisfaction tracked,
      no adoption by mandate alone.
- [x] **The operating stance survives** — "you build it, you run it" enabled
      by resilient platform abstractions; platform operational responsibility
      stays with the platform team for shared infrastructure; migrations
      managed centrally with tooling that minimizes application-team work.
- [x] **Innovation stays possible** — common paths easy, experiments allowed,
      a path for experiments to graduate into the platform, shadow platforms
      read as signals of unmet need.
- [x] **The checklist's full breadth survives** — including the glue-reduction
      section (shared IaC components, no "Terraform writing service") and the
      team-composition section (infrastructure, DevTools, DevOps, and SRE
      expertise in balance), the latter anchored in the article by a Related
      Records pointer to [[building-platform-teams]].
- [x] **Credit is explicit** — References name Fournier and Nowland's
      *Platform Engineering* and its introductory chapter.

## Non-goals

- Not [[four-pillars]] — that record defines what a real platform is made of
  (the four pillars); this one argues why platform engineering exists and
  when it earns its keep.
- Not [[getting-started]] — that record covers how and when to start; this
  one is the case for the discipline itself.
- Not [[platform-as-a-product]] — that record carries the full product
  operating mechanics; this one only states the product stance as part of
  the definition.
- Not a tooling catalogue — no positions on specific IaC, portal, or
  orchestration products.

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

- **2026-08-12** — Grounded in the introductory chapter of Camille Fournier
  and Ian Nowland, *Platform Engineering: A Guide for Technical, Product, and
  People Leaders* (O'Reilly, 2024), via its chapter checklist — read through
  a practitioner-executive lens, as with every record in this journal.
- **2026-08-12** — Framed around managing complexity rather than around
  tooling: the chapter's distinctive claim is that platforms exist to drain
  the over-general swamp, so the record leads with the swamp and holds the
  platform to a leverage test, not a feature list.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Introduction.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the
    introductory chapter, "Why Platform Engineering".

## Changelog

- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
