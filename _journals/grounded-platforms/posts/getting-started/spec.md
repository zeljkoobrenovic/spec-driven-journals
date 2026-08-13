---
status: accepted
revised: 2026-08-13
---

# Spec: Getting Started with Platform Engineering

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State when I introduce platform engineering and what I build first. The post
turns the "Getting Started" chapter of Camille Fournier and Ian Nowland's
*Platform Engineering* into an operating rule: stay lightweight while informal
cooperation still works, introduce structure as coordination costs rise, form
a formal platform team only when centralizing a capability creates real
leverage — and have that team start by fixing today's most painful problems,
not by designing an architecture for a scale we do not have. The load-bearing
idea: platform engineering is a product and cultural discipline, and readiness
is measured in coordination cost, not company size or technology fashion.

## Audience

Engineering leaders deciding whether and when to invest in platform
engineering; founders and CTOs of growing startups tempted to form a platform
team early; leaders of traditional infrastructure organizations facing a
platform transformation; peer executives comparing operating models.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that structure follows
      coordination cost: shared responsibility early, explicit ownership when
      "everyone owns it" has become "nobody owns it", and a first team that
      solves today's pain.
- [x] **The stage guidance survives** — early-stage: source control, fast
      feedback, off-the-shelf tooling, no Kubernetes before it is needed,
      outsource non-differentiators; growing: standardized local development,
      testing and deployment automation, observability, infrastructure
      automation, and a lightweight decision process (RFCs/ADRs).
- [x] **The team-formation test survives** — the friction signals (unclear
      ownership, recurring tooling friction, reinvented capabilities) and the
      centralization questions (value for many teams, one implementation
      without per-team customization, leverage vs. coordination cost).
- [x] **The first-team guidance survives** — explicit ownership boundaries,
      engineers-as-customers framing, start with problems not architecture,
      hire for the current organization's scale, add product managers before
      project managers and both only when genuinely needed.
- [x] **The transformation guidance survives** — treating an infrastructure
      org's move to platform engineering as a culture transformation: where to
      start, product thinking, support, hiring, incentives, owning migrations,
      and time spent with customers.
- [x] **Credit is explicit** — References name Camille Fournier and Ian
      Nowland's *Platform Engineering* and the Getting Started chapter.

## Non-goals

- Not [[building-platform-teams]] — that record covers staffing and shaping a
  great platform team in depth; this one covers only the hiring cautions that
  matter at formation time.
- Not [[four-pillars]] — that record defines what a real platform is; this one
  covers how and when to start building toward it.
- Not [[platform-as-a-product]] — that record is the full product operating
  mode; this one only establishes the customer framing at formation.
- Not a technology-selection guide — specific tooling choices stay with the
  teams that live with them.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab). The checklist additionally carries the chapter's
shared/integration-platform section (§6 — platform mandate, earlier PM
involvement, internal discoverability, alignment across platform layers);
that material is checklist-only by design and the article deliberately does
not summarize it. The comic compresses to eight panels and omits the
infrastructure-org transformation beat; the article (Rationale, Figure 3)
and checklist §7 carry it.

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-12** — Grounded in the "Getting Started" chapter of Camille
  Fournier and Ian Nowland, *Platform Engineering: A Guide for Technical,
  Product, and People Leaders* (O'Reilly, 2024), via its chapter checklist —
  read through a practitioner-executive lens, as with every record in this
  journal.
- **2026-08-12** — Framed around coordination cost as the readiness signal
  rather than around company stages alone: the chapter's distinctive claim is
  that structure should arrive when informal cooperation stops scaling, so the
  record commits to that trigger explicitly.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Getting Started (1).pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the "Getting
    Started" chapter.

## Changelog

- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
