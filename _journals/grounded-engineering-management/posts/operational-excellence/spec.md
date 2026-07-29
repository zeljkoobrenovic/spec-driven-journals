---
status: accepted
revised: 2026-07-28
---

# Spec: Operational Excellence

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the operational bar I hold software teams to: a system is not done
when it ships, it is done when it can be launched, monitored, paged on,
recovered, and improved without heroics. The post distills Kate
Matsudaira's article "Software Managers' Guide to Operational Excellence"
(the source PDF names her article explicitly) into an operating principle:
five keys — invest in quality assurance, automate repetitive tasks,
standardize and improve engineering processes, measure and track
performance data, foster continuous improvement — made concrete across
seven areas: launch readiness, incident management, on-call management,
operational data and system health, customer issue tracking, failover and
recovery, and CI/CD, testing, and automation. The load-bearing idea:
operational excellence is a management responsibility with a checkable bar,
not an infrastructure team's hobby — the manager owns whether the answers
to these questions are yes.

## Audience

Engineering managers and tech leads on my teams (so they know the bar their
services are held to); senior leaders and peers (so they know what
"operationally ready" means when I say it); AI tools using this journal as
context. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — the highlight states that operational
      excellence is a management responsibility with a checkable bar, and
      that a system is done when it can be run, not when it ships.
- [x] **The five keys survive** — quality assurance, automation of
      repetitive tasks, standardized and improving processes, measured
      performance data, and a culture of continuous improvement.
- [x] **All seven areas survive** — launch readiness, incident management,
      on-call management, operational data and system health, customer
      issue tracking, failover and recovery, and CI/CD, testing, and
      automation each appear in the article and map to a checklist section.
- [x] **The humane on-call stance survives** — on-call pain is measured
      and minimized, rotations are fair, and expectations about feature
      work during on-call are explicit.
- [x] **The recovery stance survives** — disaster recovery documented and
      tested, graceful degradation, time to full recovery measured, and
      rollback/failover to a known good instance always possible.
- [x] **Credit is explicit** — References name Kate Matsudaira and her
      article "Software Managers' Guide to Operational Excellence" as the
      source, as the PDF itself does.

## Non-goals

- Not [[senior-leadership]] — that record carries the True North
  commitment to protect quality, readiness, and operational standards;
  this one is the concrete bar behind that commitment.
- Not [[managing-a-team]] — that record covers team health and dynamics;
  this one covers system health and the operational practices around it.
- Not an SRE handbook — the record sets the bar managers are accountable
  for; the engineering craft of meeting it (observability stacks, DR
  tooling, deployment pipelines) lives with the teams.

## Modalities

The working checklist ships as the checklist modality (`checklist.md`,
rendered as the Checklist tab).

- [x] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [x] `comics.md` — explainer comic

## Open questions

- None.

## Decision log

- **2026-07-28** — Grounded in the "Software Managers' Operational
  Excellence Checklist" PDF, which states it is based on Kate Matsudaira's
  article "Software Managers' Guide to Operational Excellence"; credited to Matsudaira accordingly — this is
  the one record in this journal's Manager's Path section not drawn from
  Camille Fournier's book.
- **2026-07-28** — Framed as "the bar I hold teams to" rather than a
  how-to: the seven areas are stated as conditions that must hold and be
  checkable, with the manager accountable for asking, not for personally
  operating the systems.

## Sources

- **Internal**
  - `sources/engineering-manager-path/Checklist_ Software Managers’ Guide
    to Operational Excellence.pdf` — the source checklist; reproduced,
    adapted, in the Checklist tab (`checklist.md`).
- **External**
  - Kate Matsudaira, "Software Managers' Guide to Operational Excellence" — the article the checklist
    and this record distill.

## Changelog

- **2026-07-29** — Post-review fixes applied (majors and cross-cutting sweeps); see REVIEW.md. *(Željko, AI-mediated session)*
- **2026-07-28** — Comics modality added (comics.md, Comic tab, shared
  VERA/ARLO cast); 3 inline figures generated in the article. *(Željko,
  AI-mediated session)*
- **2026-07-28** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
