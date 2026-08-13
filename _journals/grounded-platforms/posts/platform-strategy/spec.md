---
status: accepted
revised: 2026-08-12
---

# Spec: Strategy for Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I expect a platform strategy to be written and tested before anyone
builds against it: derived from our business strategy and our unique context
(never copied), told as an explicit chain from context to objectives to
mechanisms to design decisions so it never collapses into an "IT hourglass",
aimed at increasing the organization's rate of change rather than reaching a
fixed target state, and passed through the ACED test — Alignment, Clarity,
Evolution, Decisions — before it is approved. The post turns the "Strategy
for Platforms" chapter of Gregor Hohpe's *Platform Strategy* into an
operating principle: a platform strategy is transformation (changed ways of
working), not optimization (new technology, old habits); design separates
commodity from differentiator and leaves users freedom; governance
centralizes expertise while decentralizing usage; the landscape is mapped
(Wardley-style) and the roadmap is point, path, and terrain with explicit
decision points. The load-bearing idea: a strategy that makes no actual
choices is a wish list wearing a strategy's clothes.

## Audience

Platform and engineering leaders in my organization writing or defending a
platform strategy; executives who approve those strategies and need a test
sharper than the quality of the slides; peer executives comparing operating
models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that a platform strategy
      is derived from our context, told as context → objectives → mechanisms
      → design decisions, aimed at rate of change, and only approved when it
      makes actual choices and passes ACED.
- [x] **The four layers survive** — context, objectives, mechanisms, design
      decisions; the explicit connection between them; the IT-hourglass
      problem the layers exist to avoid; no buzzwords standing in for
      mechanisms.
- [x] **Transformation vs optimization survives** — changed ways of working,
      constraints removed, speed *and* quality, speed *and* compliance,
      innovation and harmonization not treated as opposites.
- [x] **Design and governance survive** — commodity vs differentiator, low
      friction, user freedom (no all-encompassing IT pyramid), centralized
      expertise with decentralized usage, guardrails without ticket friction.
- [x] **Landscape and roadmap survive** — Wardley-style component evolution
      mapping; point, path, and terrain; decision points, alternative paths,
      and the data needed to choose; tactics change while direction holds.
- [x] **ACED survives** — Alignment, Clarity, Evolution, Decisions as the
      approval gate, plus the go/no-go framing.
- [x] **Credit is explicit** — References name Gregor Hohpe's *Platform
      Strategy* and the "Strategy for Platforms" chapter.

## Non-goals

- Not [[understanding-platforms]] — that record defines what a platform is;
  this one governs how we decide why and where to build one.
- Not [[designing-platforms]] — design mechanics live there; this record only
  requires that design decisions appear in the strategy as explicit
  trade-offs.
- Not [[implementing-platforms]] or [[planning-and-delivery]] — execution
  mechanics; this record ends where the roadmap's first decision point
  begins.
- Not a template for our current strategy document — this is the standard any
  such document must meet, not the document.

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

- **2026-08-12** — Grounded in the "Strategy for Platforms" chapter of
  Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
  (Leanpub, 2024), via its chapter checklist — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-12** — Framed around the four-layer chain and the ACED approval
  gate rather than a strategy-writing tutorial: the chapter's distinctive
  claims are that the layers prevent the IT hourglass and that a strategy
  must make actual choices, so the record commits to both as standards I
  enforce.

## Sources

- **Internal**
  - `sources/checklists/platform-strategy/Checklist_ PS _ Strategy for Platforms.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024) — "Strategy for Platforms" chapter.

## Changelog

- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
