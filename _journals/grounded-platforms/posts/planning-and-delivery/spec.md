---
status: accepted
revised: 2026-08-13
---

# Spec: Planning and Delivery

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I plan and deliver platform work: no long-running project starts
without a written proposal that nails the problem, the options, and what
"done" looks like; adoption and migration are project work, not launch-day
afterthoughts; long projects are broken into milestones that deliver value,
not just technical completion. The post turns the "Planning & Delivery"
chapter of Fournier and Nowland's *Platform Engineering* into an operating
principle: the roadmap is built bottom-up from all four consumers of
capacity — features, KTLO, mandates, and system improvements — with KTLO
capped near 40% and mandates costed explicitly, and delivery is communicated
through biweekly wins and challenges written for the audience that reads
them. The load-bearing idea: a plan that only lists features is a plan to
disappoint, and launch is not the finish line — adoption is.

## Audience

Platform engineering leads and managers who plan and deliver platform work
in my organization; product managers on platform teams; peer executives who
consume our plans and updates and need to know what they can trust in them.
First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that planning is honest
      capacity accounting across all four work categories, that adoption is
      part of the project, and that delivery is narrated in wins and
      challenges rather than story points.
- [x] **The proposal discipline survives** — problem before solution,
      options with trade-offs, constraints, definition of done, measurable
      success criteria, and buy-in before implementation.
- [x] **The capacity model survives** — bottom-up roadmap from features,
      KTLO, mandates, and system improvements; KTLO near or under 40%;
      mandates listed and costed separately; explicit trade-offs; slack for
      the unplanned.
- [x] **The delivery mechanics survive** — value-bearing milestones (monthly
      in year one), adoption planned as project work, the 70/20/10 and
      three-developer-month heuristics, caution on innersourcing, and the
      biweekly wins-and-challenges cadence with situation–action–result
      framing.
- [x] **Credit is explicit** — References name Fournier and Nowland's
      *Platform Engineering* and the "Planning & Delivery" chapter.

## Non-goals

- Not [[platform-as-a-product]] — that record covers discovering what to
  build and running the platform as a product; this one covers planning and
  delivering the work once direction exists.
- Not [[operating-platforms]] — KTLO appears here only as a capacity line in
  the plan; the operating model behind it (on-call, support, incident
  response) lives there.
- Not [[rearchitecting-platforms]] — major architectural rewrites get their
  own record; this one governs ordinary planning cycles and long projects
  generally.
- Not a project-management methodology — no sprint mechanics, estimation
  poker, or tooling prescriptions.

## Modalities

The working tool ships as the checklist modality (`checklist.md`, rendered
as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [x] `summary.md` — management summary
- [x] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-08-12** — Grounded in the "Planning & Delivery" chapter of Camille
  Fournier and Ian Nowland, *Platform Engineering: A Guide for Technical,
  Product, and People Leaders* (O'Reilly, 2024), via its chapter checklist —
  read through a practitioner-executive lens, as with every record in this
  journal.
- **2026-08-12** — Framed around honest capacity accounting rather than
  process: the chapter's distinctive claim is that platform plans fail by
  pretending features are the only work and launch is the end, so the record
  commits to the four-category roadmap and adoption-as-project-work.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Planning &
    Delivery.pdf` — the chapter checklist; reproduced, adapted, in the
    Checklist tab (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the
    "Planning & Delivery" chapter.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
