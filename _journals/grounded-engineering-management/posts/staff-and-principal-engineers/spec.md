---
status: accepted
revised: 2026-07-28
---

# Spec: Staff and Principal Engineers

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the expectations I hold staff and principal engineers to, and how I
coach senior engineers toward them. The post turns the "Role-Model Staff and
Principal Engineers" checklist from Gergely Orosz's *The Software Engineer's
Guidebook* into an operating principle seen from the manager's side: staff+
is a change of axis, not a bigger senior role. The load-bearing idea: beyond
senior, I stop grading craft alone and start grading five things together —
business understanding, constructive influence, engineering execution across
teams, end-to-end reliability ownership, and architecture judgment scaled to
blast radius — all of it anchored by staying hands-on enough to make
grounded decisions.

## Audience

Staff and principal engineers on my teams (so they know the bar and that it
is not "senior, but more"); senior engineers aiming at staff+ (so they see
the axis change coming); the managers who partner with staff+ engineers.
First-person declarative, manager's voice.

## Success criteria

- [x] **Principle is quotable** — highlight states that staff+ is a change
      of axis, not degree, and names the five dimensions I grade together.
- [x] **The five dimensions survive** — business understanding (North Stars,
      KPIs, customers, how the company makes money), collaboration and
      influence (trust capital, visibility, sponsorship), engineering
      execution (coding with impact, processes, CI/CD, codebase structure,
      compliance and security), reliability end to end (logging, monitoring,
      alerting, on-call, incidents, resilience), and architecture judgment
      (simplicity, one-way/two-way doors, blast radius, business-justified
      scalability).
- [x] **The hands-on anchor is explicit** — staff+ engineers keep enough
      connection to the work to make practical decisions; the ivory-tower
      architect is named as the failure mode.
- [x] **The partnership framing survives** — staff+ work is a partnership
      with EMs, PMs, business stakeholders, and senior engineers, with
      clarified responsibilities, not a solo authority role.
- [x] **Credit is explicit** — References name Gergely Orosz's *The Software
      Engineer's Guidebook* and the staff/principal chapter this distills.

## Non-goals

- Not [[well-rounded-senior-engineer]] — that record covers the senior bar
  this one builds beyond; this record is about what changes *after* senior.
- Not [[pragmatic-tech-lead]] — project leadership of one team is the tech
  lead record; staff+ scope spans teams and the org.
- Not [[engineering-career-paths]] — whether to pursue staff+ at all, and
  which track, lives there; this record assumes the role and states its bar.
- Not an operations runbook — the reliability section states ownership and
  scope; the operational bar itself is [[operational-excellence]].

## Modalities

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-28** — Grounded in the "Role-Model Staff and Principal
  Engineers" checklist distilled from Gergely Orosz, *The Software
  Engineer's Guidebook* (2023); the article is my manager-side statement of
  that bar, the Checklist tab is the checklist I hand the engineer.
- **2026-07-28** — Framed the record around the "change of axis" idea: the
  five dimensions are graded together, and hands-on groundedness is the
  anchor that keeps all five honest — rather than presenting staff+ as a
  larger quantity of senior work.

## Sources

- **Internal**
  - `sources/software-engineering-guidebook/Checklist_ TSEG _ Role-Model
    Staff _ Principal Engineers (1).pdf` — reproduced, adapted, in the
    Checklist tab (`checklist.md`).
- **External**
  - Gergely Orosz, *The Software Engineer's Guidebook* (Pragmatic Engineer,
    2023) — the staff and principal engineer chapters this record distills.

## Changelog

- **2026-07-28** — Comics modality added (comics.md, Comic tab, shared
  VERA/ARLO cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-07-28** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
