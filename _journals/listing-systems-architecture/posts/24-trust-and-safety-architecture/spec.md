---
status: accepted
revised: 2026-10-20
---

# Spec: Trust and Safety as a Platform

## Intent

Show architects how to build trust and safety (T&S) as a platform capability rather than as a queue attached to the insertion flow. The chapter splits T&S into five functions (policy, detection, decision, enforcement, review and redress) plus measurement. It argues for one decision service as the single writer of decision records, enforcement as events that every consumer acknowledges, policies as versioned reference data, and metrics based on sampled prevalence and overturn rates. It ends with a group-level answer to "what do we share across brands?": share the machinery, evidence and lawful signals; keep policy content, thresholds and vertical detectors local. After reading, an architect can draw the components and their interfaces, defend the pre- versus post-moderation choice as a set of risk tiers, and say what must happen in every system when a listing or account is restricted.

## Audience

Chief architects of marketplace groups, heads of trust and safety and their engineering leads, and principal engineers who own insertion, search, messaging or ranking and need to understand where those systems meet moderation. Readers know distributed systems; they may not know DSA terminology or T&S metrics.

## Success criteria

- [ ] The five functions are defined, with the speed at which each changes and its typical failure, and the chapter owns the terms moderation pipeline, enforcement action and T&S metrics.
- [ ] A component diagram shows intake, synchronous and asynchronous detection, the decision service, case management, enforcement events, statements of reasons, appeals, the evidence store and metrics.
- [ ] Enforcement propagation is worked through consumer by consumer (search, alerts, recommendations, messaging, SEO, ads, payments, partner feeds), with a sequence diagram and the Ghost Inventory link.
- [ ] The moderation-mode spectrum and the risk-tiered hybrid are explained with the Which? 2024 edit test and the 2015 leboncoin ruling, both dated.
- [ ] A metrics table defines prevalence, time to action, precision, recall, overturn rate, report rate and reviewer agreement, including how each misleads.
- [ ] A Veldmark worked example uses ledger numbers (94% automated, about 138,000 reviews a week, 210 moderators, 1.9% removals in NL, the 7 March 2027 phishing suspension) and shows the shared-platform design targets.
- [ ] Shared-versus-local table, trade-off tables, a vertical-differences table, failure modes, the Chief Architect's view and 10 review questions are present.
- [ ] Every company claim carries a dated source; the Adevinta shared-platform inference from job postings is labeled.

## Non-goals

- Fraud typology, risk scoring, fraud signals and step-up friction: [[fraud-prevention]].
- Identity levels, KYB and verified badges: [[identity-and-verification]].
- Legal detail of the DSA, DAC7, the UK Online Safety Act and vertical regulation, and Veldmark's statement-of-reasons pipeline: [[marketplace-regulation]].
- Message storage and conversation design: [[messaging-and-leads]].
- The end-to-end publication path and freshness targets: [[publication-pipeline]].
- Ranking mechanics: [[ranking]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- DSA article wording is taken from an unofficial reproduction; verify quotations against EUR-Lex before print.
- No classifieds company has published a T&S architecture; revisit the "In practice" section if Adevinta, OLX or Vinted publish one.
- Whether the shared hashed block list across brands survives a full DPIA in every Veldmark country is asserted in the story, not analyzed; [[identity-and-verification]] or [[marketplace-regulation]] may need to pick this up.

## Decision log

- **2026-10-19** — Organized the chapter around five functions rather than around the pipeline alone, because the decision record and enforcement propagation are where multi-brand platforms fail, and a pipeline-only framing hides them.
- **2026-10-19** — Used the 7 March 2027 city bike phishing incident as the opening scene, but from the group's viewpoint (what happened outside Tradeyard NL), leaving the message mechanics to [[messaging-and-leads]] and the fraud detection to [[fraud-prevention]].
- **2026-10-19** — Kept the Barcelona fake-rental ring out of this chapter so [[fraud-prevention]] can use it as its main worked example.
- **2026-10-19** — Presented the architecture as a labeled reference inference built from Sigma, Stripe Radar, OLX, Adevinta and DSA requirements, rather than as any company's design, because no classifieds T&S architecture is publicly documented.

## Sources

- **Internal**
  - `_research/brief-trust-safety-regulation.md` — moderation modes, pipeline anatomy, DSA obligations, Transparency Database schema, enforcement ladder.
  - `_research/brief-adevinta.md` — chat and moderation as early global components; the OCR service.
  - `_research/scenario-ledger.md` — Veldmark volumes, moderation numbers, city bike timeline, Common Ground decisions.
  - [[publication-pipeline]], [[event-driven-listings]], [[ranking]], [[marketplace-regulation]] — neighbouring owners.
- **External**
  - Which?, *Scam ads slipping through the net too easily* (2024) — edits passing review.
  - Clubic, leboncoin ruling (2015) — moderation claims and hosting status.
  - Integrity Institute for Ofcom, *Fraudulent advertising and account integrity* (2026) — enforcement ladder, prevalence sampling.
  - Stripe Radar documentation (n.d.) and Meta's Sigma post (2015) — rule lifecycle and rules as code.
  - OLX Group (2026) and Adevinta (2023, 2024) — public classifieds moderation evidence.
  - DSA Articles 16, 17, 20, 24 and the Transparency Database documentation.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Ingrid joined five weeks (not three) before 7 March; DSA Arts. 16, 17, 20 and 24(5) verified against the Official Journal and unofficial-mirror links replaced; Transparency Database demotion value corrected to DECISION_VISIBILITY_CONTENT_DEMOTED. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
