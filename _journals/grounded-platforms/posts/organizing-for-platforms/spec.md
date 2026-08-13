---
status: accepted
revised: 2026-08-13
---

# Spec: Organizing for Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I organize people around a platform: as a small product company
inside the organization, not as an IT project or a ticket queue. The post
turns the "Platform Team Organization" chapter checklist of Gregor Hohpe's
*Platform Strategy* into an operating principle: a cross-functional platform
team with an accountable leader and named ownership of technology strategy,
roadmap, delivery, marketing, and support — roles that can share heads but
never go unowned; east–west alignment so infrastructure silos never ship in
the platform experience; north–south alignment so adoption is an ongoing
relationship, not a rollout; an engagement model balanced across
self-service, consulting, community, and co-creation; and the discipline to
first confirm a platform is needed at all. The load-bearing idea: platforms
fail organizationally before they fail technically.

## Audience

Platform leaders and the executives who staff them; infrastructure and
operations managers whose teams sit behind the platform; development-team
leads deciding whether and how to adopt it; peer executives comparing
operating models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight commits to the platform team as
      a small product company: accountable leadership, named role ownership,
      east–west and north–south alignment, and value-earned adoption.
- [x] **The roles survive** — accountable platform leader plus ownership of
      technology strategy, product roadmap, engineering delivery, marketing
      and adoption, and support — with the note that roles can share people
      but responsibilities must be revisited and split as the team grows.
- [x] **Both alignment axes survive** — east–west (breaking silos across
      infrastructure functions, no org chart in the platform experience,
      fix/wrap/work-around for impossible dependencies) and north–south
      (builders and consumers, speed vs. stability, no us-versus-them).
- [x] **The customer machinery survives** — needs before solutions, personas
      (developers, administrators, operators, end users), and the engagement
      model balanced across self-service, setup, consulting, community, and
      co-creation.
- [x] **The restraint survives** — the decide-whether-you-need-a-platform
      gate, Thinnest Viable Platform, enablement as an alternative, and
      skills/cognitive-load development alongside the platform.
- [x] **Credit is explicit** — References name Gregor Hohpe's *Platform
      Strategy* and the platform-team-organization chapter.

## Non-goals

- Not [[building-platform-teams]] — that record covers hiring and growing
  platform engineers as individuals; this one covers the team's shape, roles,
  and relationships to the rest of the organization.
- Not [[platform-as-a-product]] — the full product-management discipline for
  platforms lives there; here "platform as a product" appears as the founding
  organizational stance.
- Not [[managing-stakeholders]] — stakeholder tactics for platform leaders
  are that record's subject; this one sets up the org structure those tactics
  operate in.
- Not a headcount or org-chart template — no prescriptions for team sizes or
  reporting lines.

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

- **2026-08-12** — Grounded in the "Platform Team Organization" chapter
  checklist of Gregor Hohpe, *Platform Strategy: Innovation Through
  Harmonization* (Leanpub, 2024) — read through a practitioner-executive
  lens, as with every record in this journal.
- **2026-08-12** — Framed around the small-product-company metaphor and the
  two alignment axes (east–west, north–south) rather than a role catalog:
  the chapter's distinctive claim is that platform success is organizational
  before it is technical, so the record commits to the relationships, not
  just the boxes.

## Sources

- **Internal**
  - `sources/checklists/platform-strategy/Checklist_ PS _ Organizing for
    Platforms.pdf` — the chapter checklist; reproduced, adapted, in the
    Checklist tab (`checklist.md`). The reproduction keeps the chapter's
    recruiting-and-retention section for source fidelity, even though hiring
    and growing platform engineers is fenced to [[building-platform-teams]].
- **External**
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024) — the platform-team-organization chapter.

## Changelog

- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
