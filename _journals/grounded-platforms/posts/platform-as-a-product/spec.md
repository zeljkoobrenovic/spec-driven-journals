---
status: accepted
revised: 2026-08-13
---

# Spec: Platform as a Product

> Working doc for the post in this folder. The spec drives the post; the post
> is the artifact.

## Intent

State how I run internal platforms as products with real customers, not as
infrastructure projects with captive users. The post turns the "Platform as
a Product" chapter of Camille Fournier and Ian Nowland's *Platform
Engineering* into an operating principle: platform teams treat internal
engineers as customers whose workflows they observe, resist becoming a
feature shop for the loudest team, validate product–market fit before
committing investment, plan adoption and migration as first-class product
work, measure impact rather than activity, and keep product and engineering
responsibilities distinct and healthy. The load-bearing idea: mandatory
usage is not product success — a platform earns adoption the way any
product does, and I hold platform teams to that bar.

## Audience

Platform team leads and product managers in my organization (so they know
the product bar their platform is held to); platform engineers who need to
see why customer empathy and adoption planning are their job too; peer
executives comparing platform operating models. First-person declarative.

## Success criteria

- [x] **Principle is quotable** — highlight states that internal platforms
      are products with customers, that mandatory usage is not success, and
      that adoption, migration, and impact measurement are product work.
- [x] **The customer-culture side survives** — internal users treated as
      customers, workflows observed rather than assumed, engineers exposed
      to customer support, customer-focused goals, and the captive-audience
      risks of internal customers.
- [x] **The product-discipline side survives** — the feature-shop trap,
      discovering products from internally proven tools, validating internal
      product–market fit with real commitments, rethinking the problem
      rather than just the interface.
- [x] **The adoption-and-measurement side survives** — migration cost in
      the build decision, the customer's change budget, impact vs guardrail
      vs product-health metrics, outcome-defined features, internal
      marketing, reliability as part of the product experience, and healthy
      product/engineering responsibility split.
- [x] **Credit is explicit** — References name Camille Fournier and Ian
      Nowland's *Platform Engineering* and the "Platform as a Product"
      chapter.

## Non-goals

- Not [[four-pillars]] — that record covers the whole pillar model of which
  "curated product" is one; this one is the full product operating
  discipline behind that pillar.
- Not [[operating-platforms]] — reliability appears here only as part of
  the product experience; the operational machinery (on-call, support,
  operational feedback) lives there.
- Not [[planning-and-delivery]] — the roadmap appears here as a product
  artifact; the planning mechanics live there. (Known overlap: checklist §11
  reproduces the chapter's roadmap-creation steps as part of the product
  artifact; the planning discipline itself still lives in
  planning-and-delivery.)
- Not a tooling or vendor recommendation — the record is about the product
  discipline, not which developer portal to buy.

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

- **2026-08-12** — Grounded in the "Platform as a Product" chapter of
  Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
  Technical, Product, and People Leaders* (O'Reilly, 2024), via its chapter
  checklist — read through a practitioner-executive lens, as with every
  record in this journal.
- **2026-08-12** — Framed around "mandatory usage is not product success"
  rather than a generic product-management primer: the chapter's
  distinctive claim is that internal customers are captive, which makes
  product discipline harder, not optional.

## Sources

- **Internal**
  - `sources/checklists/platform-engineering/Checklist_ PE _ Platform as a Product.pdf`
    — the chapter checklist; reproduced, adapted, in the Checklist tab
    (`checklist.md`).
- **External**
  - Camille Fournier and Ian Nowland, *Platform Engineering: A Guide for
    Technical, Product, and People Leaders* (O'Reilly, 2024) — the
    "Platform as a Product" chapter.

## Changelog

- **2026-08-13** — Summary and dialog modalities added (Summary and Conversation tabs, Ana/Ben dialog cast). *(Željko, AI-mediated session)*
- **2026-08-13** — Post-review fixes applied (see REVIEW.md). *(Željko, AI-mediated session)*
- **2026-08-12** — Comics modality added (comics.md, Comic tab, shared VERA/KAI cast); 3 inline figures generated in the article. *(Željko, AI-mediated session)*
- **2026-08-12** — Initial spec, article, and checklist written; spec and
  post agree. Status `accepted`. *(Željko, AI-mediated session)*
