---
status: accepted
revised: 2026-10-21
---

# Spec: Data Platform for Marketplaces: Events, Lakehouse and Data Products

## Intent

Show a marketplace group's architects how to collect, govern and use data so that liquidity becomes measurable and comparable across brands. The chapter argues that the decisive parts of a data platform are contracts, not engines: a tracking plan for behavioral events, data contracts at ingestion, governed metrics with one owner and one definition (above all, the "contact"), and purpose-bound access policy for cross-brand sharing. Technology choices (lakehouse, warehouse, open table formats) are treated as consequences of those contracts and of the group's changing shape through acquisitions and disposals.

## Audience

Chief architects, heads of data and ML, analytics engineering leads and engineering directors of multi-brand listing marketplaces. They should leave able to write a contact definition card, specify a marketplace tracking plan's core events, choose where the durable copy of data lives, assign data-product ownership, and turn cross-brand data-sharing limits into enforceable policy.

## Success criteria

- [ ] Reader can distinguish domain events, CDC and behavioral events, and say which one carries which kind of fact.
- [ ] Reader can list the core events of a marketplace tracking plan, including impressions with ranking and experiment context and consent state on the envelope.
- [ ] Reader can write a governed-metric definition card for "qualified contact", including exclusions, timing and restatement.
- [ ] Reader can compare warehouse, lakehouse and hybrid options and justify open storage for groups that change shape.
- [ ] Reader can assign ownership of data products using "fact owner owns the source product; decision owner owns the consumer product".
- [ ] Reader can explain the four limits on cross-brand data sharing and express a neutrality commitment (Keybridge) as auditable access policy.
- [ ] Every company claim carries a dated source; Veldmark numbers agree with the ledger; at least two mermaid diagrams and a trade-off table are present.

## Non-goals

- The listing event stream, outbox and schema evolution ([[event-driven-listings]]).
- Systems of record, read models and erasure mechanics across operational copies ([[listing-data-management]]).
- Experiment design and statistics ([[experimentation]]); feature stores and model governance ([[ml-platform]]).
- Advertising consent mechanics and audiences ([[advertising-platforms]]); regulatory detail of DSA and DAC7 ([[marketplace-regulation]]).
- Pro tooling product design ([[professional-seller-tooling]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Whether any classifieds group has published a governed definition of "contact" or "lead"; none was found, so the chapter relies on Veldmark.
- Feature-store and metrics-layer products are deliberately not named; revisit if a classifieds case documents one.
- National exemptions for consent-free audience measurement differ; the chapter states the principle only.

## Decision log

- **2026-10-19** — Built the chapter around one board question ("how many contacts last week?") rather than a technology survey, because the governed contact metric is where the platform's value and politics are both visible.
- **2026-10-19** — Recommended open table formats plus a warehouse as main compute, rejecting "one warehouse" (blocks acquisitions on other clouds) and "warehouse per brand" (Deal-Shaped Architecture), citing Adevinta's 2025 decentralization as the portability argument.
- **2026-10-19** — Made "server-side for facts, client-side for context" a core rule, because consent and client loss bias client-side counts differently by country.
- **2026-10-19** — Treated Keybridge neutrality as the canonical cross-brand sharing case, expressed as access policy with external audit.

## Sources

- **Internal**
  - [[liquidity-and-network-effects]] — liquidity metric vocabulary.
  - [[event-driven-listings]], [[listing-data-management]] — upstream event and data ownership.
  - [[experimentation]], [[ml-platform]] — downstream consumers.
  - `_research/brief-platform-data-ml.md` Parts 2, 8, 9; `_research/brief-adevinta.md` 4.2; `_research/brief-monetization-economics.md` 5.3.
- **External**
  - Adevinta Tech Blog (2022–2024) — UBCT events, data contracts, lakehouse to data mesh, Artemis metric monitoring, logging cost.
  - Vinted Engineering (2019); Zalando Engineering (2021) — tracking schemas and generated SDKs.
  - AutoScout24 Tech Blog (2025) — BI consolidation.
  - OLX Tech Blog (2026) — causal measurement of paid packages.
  - Dehghani (2019) — data mesh; Armbrust et al., CIDR (2021) — lakehouse.
  - GDPR and ePrivacy Directive — purpose limitation and device-storage consent.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: clarified the 72-hour restatement for the phishing account, flagged older Adevinta and Meilleurs Agents evidence, softened an only-source claim, expanded acronyms, American spelling. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,908 → 6,938 prose words (opening now ties the chapter to Part VII's contract argument and to Part VI's contact counts); 1 heading renamed ("Data Products and the Data Mesh" → "Data Products: Federate Ownership, Not Substrate"); buried points moved to first sentences in 9 paragraphs; 3 long paragraphs split; no spec change. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Ingrid's line says three contact definitions, matching the scene table; the replay table and intro now say the Essen Golf row (April) was added after the March week. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`). *(AI-mediated session)*
- **2026-10-21** — Renamed failure patterns to match [[where-listing-systems-go-wrong]]: Seeing Double, Search as System of Record, Multiplier Creep, Fast Mail for Fraudsters, The Copy-Paste Country, Deal-Shaped Architecture, The Forced Fit, Billing by Guesswork, Set-and-Forget AI. *(AI-mediated session)*
