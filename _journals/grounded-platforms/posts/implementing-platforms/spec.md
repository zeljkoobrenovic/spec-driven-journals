---
status: accepted
revised: 2026-08-13
---

# Spec: Implementing Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the operating model I hold platform implementations to: an internal
platform is built as three planes — a self-service management plane that
developers touch, a control plane that continuously reconciles desired and
actual state, and a services plane that does the actual work — and every
abstraction it introduces is judged by two tests: does it genuinely reduce
cognitive load, and can a failure be traced back through it. The post turns
the "Implementing (Internal) Platforms" chapter of Gregor Hohpe's *Platform
Strategy* into an operating principle: reconciliation is the engine, not a
feature; ownership between platform and application teams is explicit;
tenancy and isolation are conscious architecture decisions tested at scale,
not defaults inherited from the first prototype. The load-bearing idea: a
platform that hides complexity without a troubleshooting path has not
reduced cognitive load — it has deferred it to the worst possible moment.

## Audience

Platform leads and architects building or rearchitecting our internal
developer platform (so they know the anatomy and the readiness bar I hold
them to); application-team leads negotiating the ownership boundary; peer
executives comparing platform operating models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states the three-plane anatomy,
      reconciliation as the engine, the cognitive-load and traceability
      tests, and tenancy as a conscious decision.
- [x] **The anatomy survives** — management plane (portal, CLI, API,
      automation language; user journeys over CRUD; no ClickOps at scale),
      control plane (desired state, reconciliation, multi-tenancy, catalog,
      orchestration), services plane (base, third-party, custom, and
      user-contributed services; SDLC capabilities).
- [x] **The control-loop and orchestration ideas survive** — Observe →
      Analyze → Act, drift detection and resolution, translate/deploy
      orchestration, templates versus higher-level orchestration, the
      cognitive-load test for abstractions.
- [x] **Traceability and ownership survive** — errors traceable to the
      platform specification that produced them; explicit platform-team and
      application-team responsibilities; configuration control with
      guardrails instead of ticket friction.
- [x] **Tenancy and scale survive** — what a tenant is, the three tenancy
      approaches, isolation levels (logical / namespace / resource),
      noisy-neighbor fairness, and testing the control plane for
      reconciliation bursts and scale.
- [x] **Credit is explicit** — References name Gregor Hohpe's *Platform
      Strategy* and the "Implementing (Internal) Platforms" chapter.

## Non-goals

- Not [[designing-platforms]] — that record covers what to design into the
  platform and where to draw its boundaries; this one is how the design
  becomes a running system.
- Not [[operating-platforms]] — that record covers running platforms in
  production (reliability, on-call, support); this one covers building the
  machinery that will be operated.
- Not [[organizing-for-platforms]] — team setup and organizational placement
  live there; this record only fixes the responsibility boundary between
  platform and application teams.
- Not a technology endorsement — the record stays at the anatomy level;
  specific tools (e.g. Kubernetes) may appear as illustrative examples of an
  implementation choice, never as a recommendation of any portal,
  orchestrator, or cloud product.

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

- **2026-08-12** — Grounded in the "Implementing (Internal) Platforms"
  chapter of Gregor Hohpe, *Platform Strategy: Innovation Through
  Harmonization* (Leanpub, 2024), via its chapter checklist — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-12** — Framed around the three-plane anatomy plus two
  cross-cutting tests (cognitive load, traceability) rather than as a tour
  of the checklist's fourteen sections: the chapter's distinctive claim is
  that implementation quality shows up in reconciliation, traceability, and
  consciously chosen tenancy, not in feature count.

## Sources

- **Internal**
  - `sources/checklists/platform-strategy/Checklist_ PS _ Implementing
    Platforms.pdf` — the chapter checklist; reproduced, adapted, in the
    Checklist tab (`checklist.md`).
- **External**
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024) — the "Implementing (Internal) Platforms" chapter.

## Changelog

- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
