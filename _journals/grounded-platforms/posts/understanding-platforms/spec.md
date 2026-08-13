---
status: accepted
revised: 2026-08-13
---

# Spec: Understanding Platforms

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State the definition I hold every "platform" in my organization to before it
earns the name: a platform elevates participants by letting them build on
existing capabilities, and it generates value through interaction — a platform
without participants is worth little, and a product relabeled "platform" is
worth nothing extra. The post turns the "Understanding Platforms" chapter of
Gregor Hohpe's *Platform Strategy* into an operating principle: the main
benefits (enable, democratize, self-perpetuate, accelerate, avoid unnecessary
constraints), the automotive lesson that harmonization underneath should
*increase* diversity on top, the four technology platform types (marketplace,
base, developer, business capability), and the reminder that how users access
a platform matters as much as what is inside it. The load-bearing idea:
harmonize below the line, differentiate above it — and test every so-called
platform against that bar.

## Audience

Engineering and platform leaders in my organization deciding what to build as
a platform and what to leave as a product; executives who hear "platform" in
every pitch and need a test for it; peer executives comparing operating
models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that a platform elevates
      participants, generates value through interaction, and that
      harmonization underneath must enable diversity on top; renaming is not
      platform engineering.
- [x] **The definition survives** — elevates participants, value through
      interaction, no participants means no value, true platform vs
      relabeled product.
- [x] **The benefits survive** — enable, democratize, self-perpetuate,
      accelerate, avoid unnecessary constraints.
- [x] **The automotive lesson survives** — reuse expensive engineering,
      standardization can increase diversity, harmonized-in-platform vs
      variable-on-top, the badge-engineering danger.
- [x] **The four types survive** — marketplace, base, developer, and business
      capability platforms, each with purpose and typical interaction, plus
      the layered/fractal combination point and the access-matters point.
- [x] **Credit is explicit** — References name Gregor Hohpe's *Platform
      Strategy* and the "Understanding Platforms" chapter.

## Non-goals

- Not [[platform-strategy]] — that record covers how to write and test a
  platform strategy; this one defines what a platform *is* before any
  strategy applies.
- Not [[designing-platforms]] — design mechanics (interfaces, boundaries,
  abstractions) live there; this record only draws the harmonized-vs-variable
  line.
- Not [[what-is-platform-engineering]] — the Fournier/Nowland case for
  platform engineering as a discipline; this record is Hohpe's
  vocabulary-and-taxonomy foundation.
- Not a catalog of our internal platforms — this is the test they must pass,
  not the inventory.

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

- **2026-08-12** — Grounded in the "Understanding Platforms" chapter of
  Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
  (Leanpub, 2024), via its chapter checklist — read through a
  practitioner-executive lens, as with every record in this journal.
- **2026-08-12** — Framed around the harmonize-below / differentiate-above
  line rather than a taxonomy tour: the chapter's distinctive claim is that
  standardization done right increases diversity, so the record commits to
  that as the test every platform must pass.

## Sources

- **Internal**
  - `sources/checklists/platform-strategy/Checklist_ PS _ Understanding Platforms.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Gregor Hohpe, *Platform Strategy: Innovation Through Harmonization*
    (Leanpub, 2024) — "Understanding Platforms" chapter.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
