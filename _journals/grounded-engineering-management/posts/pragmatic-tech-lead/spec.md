---
status: accepted
revised: 2026-07-28
---

# Spec: The Pragmatic Tech Lead

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the project-leadership expectations I hold an engineer to when they
step into the tech-lead role — grounded in the Pragmatic Tech Lead chapters
of Gergely Orosz's *The Software Engineer's Guidebook*. The load-bearing
idea: a tech lead is neither a junior manager nor a superior engineer, but
the person accountable for a project succeeding while staying hands-on —
which means clarifying the role's mandate before exercising it, starting
projects with real kickoffs and written scope, breaking work into small
shippable milestones with estimates as forecasts, respecting the physics
binding scope, timeline, and people, mitigating risk through prototypes and
engineer-to-engineer conversation, matching the release process to the
product's risk with safety nets, keeping stakeholders unsurprised, tending
team structure and dynamics, and closing projects properly — all while
empowering the team rather than making it dependent on the lead.

## Audience

Engineers stepping into or holding a tech-lead role (the bar, in their own
checklist); the managers those tech leads pair with, so both sides know the
split; peer executives comparing operating models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the role definition (not
      a junior manager, not a superior engineer; accountable and hands-on),
      the project disciplines, and the closing test: make the team succeed,
      not dependent.
- [x] **Role clarity survives** — title vs. informal role vs. project
      responsibility; explicit manager expectations; the build/strategy/
      people time split; hands-on quality bar; not a manager unless
      explicit; never the bottleneck.
- [x] **Project mechanics survive** — kickoff with circulated proposal and
      aligned stakeholders, engineering kickoff with written decisions,
      small shippable milestones, estimates as forecasts, no dates locked
      before planning, explicit tradeoffs when the business needs a fixed
      date, and proper project closure (final update, recognition,
      learnings).
- [x] **Software project physics survive** — scope/timeline/people move
      together; added people cost before they pay; changes communicated,
      never hidden into crises.
- [x] **Risk, release, and stakeholder disciplines survive** — prototypes
      and spikes for technology risk; direct engineer-to-engineer contact
      before escalation for dependencies; release approach chosen on the
      YOLO-to-regulated spectrum; verification and safety nets (flags,
      canaries, staged rollouts, rollback); conscious pragmatic risk;
      stakeholders identified broadly and never surprised late.
- [x] **Credit is explicit** — References name Gergely Orosz, *The Software
      Engineer's Guidebook* (2023), and the chapters distilled.

## Non-goals

- Not [[tech-lead]] — that record is the same rung seen from the management
  ladder (*The Manager's Path*); this one is the engineer-side
  project-leadership bar. The two deliberately coexist and crosslink.
- Not [[managing-a-team]] — people management, performance, and team
  building are the manager's records; this role leads projects, not people.
- Not [[well-rounded-senior-engineer]] — individual senior scope and craft
  are assumed here, not restated.
- Not [[operational-excellence]] — the standing operational bar (monitoring,
  on-call, incident practice) lives there; this record only touches it at
  the release boundary.

## Modalities

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-28** — Grounded in the "Pragmatic Tech Lead" checklist distilled
  from Gergely Orosz's *The Software Engineer's Guidebook* (2023): role
  clarity, project leadership, scope/timeline/people physics, day-to-day
  project management, risks and dependencies, wrapping up, shipping to
  production, stakeholder management, team structure, and team dynamics.
- **2026-07-28** — Framed per the journal's Guidebook convention, with one
  deliberate structural choice: this record and [[tech-lead]] cover the same
  rung from opposite sides (engineer-side project leadership vs. the
  management-ladder step) and crosslink rather than merge.

## Sources

- **Internal**
  - `sources/software-engineering-guidebook/Checklist_ TSEG _ Pragmatic Tech Lead (1).pdf`
    — reproduced, lightly condensed, in the Checklist tab (`checklist.md`).
- **External**
  - Gergely Orosz, *The Software Engineer's Guidebook* (self-published,
    2023) — the Pragmatic Tech Lead chapters this record distills.

## Changelog

- **2026-07-28** — Comics modality added (comics.md, Comic tab, shared
  VERA/ARLO cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-07-28** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
