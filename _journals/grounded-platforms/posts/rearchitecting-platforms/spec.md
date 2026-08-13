---
status: accepted
revised: 2026-08-13
---

# Spec: Rearchitecting Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the discipline I hold every major platform rearchitecture to: it is a
business investment, not a technical adventure. A rearchitecture happens
only when incremental improvement genuinely cannot solve the constraint; it
is planned on a 3–5-year horizon but pays for itself with a valuable
deliverable in production within every 12 months; migration costs are
counted honestly before commitment; security is built in by design and by
default; and the work is stopped or reshaped when evidence no longer
supports the original hypothesis. The post turns the "Rearchitecting
Platforms" chapter of Fournier and Nowland's *Platform Engineering* into an
operating principle. The load-bearing ideas: prefer incremental
rearchitecture over a separate "v2"; use the three levels of success
(audacious, valuable fallback, production proof); and secure leadership
commitment that survives reorganizations before starting.

## Audience

Platform engineering leads and architects proposing or running a
rearchitecture in my organization; the executives I ask to fund and protect
multi-year architectural work; consumer-team leads whose migration effort
is part of the true cost. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that rearchitecture is a
      business investment justified by a real constraint, paid for by
      12-month wins in production, costed including migration, and stopped
      when the evidence turns.
- [x] **The go/no-go discipline survives** — genuine architectural
      constraint on features/reliability/security/efficiency, incremental
      preferred over "v2", maturity and mindset match
      (scrappy/scalable/robust; pioneer/settler/town planner), and the
      final go/no-go review.
- [x] **The delivery discipline survives** — 3–5-year target, 12-month wins
      with the three levels of success (audacious / valuable fallback /
      production proof), guardrails on compatibility, testing, lower
      environments, and rollout.
- [x] **The cost and people side survives** — honest migration-cost
      calculation, organizational support that protects the work through
      reorgs and layoffs, staffing that keeps historical context involved
      rather than handing the rewrite to new hires, and pioneer work
      without shadow platforms.
- [x] **Security-by-design survives** — security as a core platform
      capability, protections that do not depend on human behavior, and
      paved paths that make the safest option the easiest option.
- [x] **Credit is explicit** — References name Fournier and Nowland's
      *Platform Engineering* and the "Rearchitecting Platforms" chapter.

## Non-goals

- Not [[planning-and-delivery]] — that record governs ordinary planning
  cycles and long projects generally; this one adds the extra guardrails a
  foundational rewrite demands. The milestone and migration discipline is
  inherited from there.
- Not [[four-pillars]] — the pillars say what a platform is; this record
  says how to rebuild one that exists.
- Not a technology-selection guide — the record constrains how OSS/vendor
  bets are evaluated, not which technologies to pick.
- Not an application-rewrite playbook — the scope is platforms with a broad
  developer base and migration obligations, not a single product's codebase.

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

- **2026-08-12** — Grounded in the "Rearchitecting Platforms" chapter of
  Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
  Technical, Product, and People Leaders* (O'Reilly, 2024), via its chapter
  checklist — read through a practitioner-executive lens, as with every
  record in this journal.
- **2026-08-12** — Framed as an investment discipline rather than a
  technical method: the chapter's distinctive claim is that rearchitectures
  fail organizationally (no 12-month value, uncounted migration costs,
  unprotected funding) more often than technically, so the record commits
  to the go/no-go and annual-review gates.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Rearchitecting
    Platforms.pdf` — the chapter checklist; reproduced, adapted, in the
    Checklist tab (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the
    "Rearchitecting Platforms" chapter.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
