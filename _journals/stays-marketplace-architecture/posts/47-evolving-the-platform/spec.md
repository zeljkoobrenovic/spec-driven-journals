---
status: accepted
revised: 2026-10-22
---

# Spec: Built for the Next Disruption: Evolving a Stays Platform Over a Decade

## Intent

Close the book's main argument by showing chief architects how to keep a stays platform coherent over ten years that nobody can forecast. The chapter makes three moves. **Stressor analysis (stays)**, built on O'Reilly's residuality theory: list environmental changes without estimating probability, trace each through the guest's promise, record attractor, residue and status, and confirm the decomposition with a combined stressor. **Durable records, replaceable engines**: the offer and quote, reservation versions, ledger and place and policy registries must be portable (readable without their writer, historical, replayable, neutral); engines, caches, models and adapters are allowed to be replaced. **The stays fitness function**: five outcome measures (price accuracy, double-booking rate, reservation delivery rate, time to payout, cost per booking), each with an owner, threshold, cadence and the decision a breach triggers, plus structural fitness functions in pipelines. The chapter also synthesizes the book: Corvane's 2027 incidents mapped to the separations built, and the sixteen failure patterns mapped to residues and signals. It hands over to Part X.

Productscape domains covered: the residuality stress tests of both models (TAM `licn`, `fire`, `insv`, `strd`; HSM `licn`, `evac`, `coho`, `midt`) and their residual architectures (digest §10). No product brick is owned here; the chapter is the synthesis across all of them.

## Audience

Group chief architects, CTOs and principal engineers of travel groups who answer to a board for a multi-year platform program. They know evolutionary architecture and SLOs in general; they need the stays-specific stressor list, the records that must be portable in this domain, and a board-readable set of measures.

## Success criteria

- [ ] Defines naive architecture, stressor, attractor, residue, residual architecture, stressor analysis (stays) and stays fitness function, and contrasts fitness functions with journey SLOs and KPIs in a table.
- [ ] Opens with Corvane's 14 December 2027 One Stay review and a table tracing the 2027 ledger incidents to the separation built and the owning chapter.
- [ ] Gives a nine-stressor table from the November 2027 workshop with attractor, residue and status, and a worked combined stressor (Algarve, August 2029) that exposes two gaps and their decisions.
- [ ] Defines portability in four tests and says what should not be portable; argues optionality tied to named stressors.
- [ ] Gives five fitness functions with ledger-consistent baselines (91% accuracy; 1.8 and ~5 per 10,000; 0.65% payout returns; €3.20 and €5.17 per stayed reservation), thresholds, owners and breach decisions, plus structural fitness functions and a portability drill.
- [ ] Maps all sixteen failure patterns to residues and signals.
- [ ] Uses dated public evidence for platform shifts, the 2020 demand collapse and regulation, with the interpretation labeled.
- [ ] Includes three diagrams (illustrated), a trade-off table, a Hotels and Homes table with a sharing judgement, failure modes, the Chief Architect's view, questions, and a hand-off to [[part-10]] and [[case-booking-com]].

## Non-goals

- What exactly to share across brands and in what order ([[converging-two-marketplaces]]).
- Team design and the architecture forum's operating model ([[organizing-stays-engineering]]).
- Migration techniques such as strangler fig, CDC extraction and parallel run ([[modernizing-a-live-marketplace]]).
- Journey SLOs, degradation modes and cost-per-booking derivation ([[global-scale-and-reliability]]).
- Model governance in depth ([[stays-ml-platform]]); AI agents as a channel ([[ai-in-travel-stays]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Chapters 41–46 were not yet written when this chapter was drafted; references to One Stay sharing, organization, Keystone retirement and AI agents are kept general and should be checked against those chapters in review.
- The fitness-function thresholds for 2030 are Corvane's illustrative choices; delivery-rate baseline was "not measured" before arrival manifests.
- Airbnb's 2026 post "What COVID did to our forecasting models" was not read; only the companion post's refit/respecify/hold framing is cited.

## Decision log

- **2026-10-21** — Framed the chapter around a board question ("What will we be fixing in 2032?") so the synthesis table of 2027 incidents serves as both scene and book summary.
- **2026-10-21** — Chose five fitness functions that map to the promise's parts, leaving trust without a single board number and saying why.
- **2026-10-21** — Built the combined stressor from the reference models' evacuation-plus-insolvency case, using Maré Alta Stays, and let it expose two gaps solved by reusing contracts rather than new engines.
- **2026-10-21** — Included the Hotels and Homes section, although optional in Part IX, to show that the method is shared and the exposure differs.

## Sources

- **Internal**
  - [[where-stay-platforms-go-wrong]], [[stays-bounded-contexts]], [[global-scale-and-reliability]], [[stays-regulation]], [[reservation-lifecycle]], [[payouts-and-settlement]], [[availability-engine]], [[inventory-integrity]], [[marketplace-intelligence]], [[event-driven-stays]].
  - `_research/productscape-digest.md` §10; `scenario-ledger.md`; `brief-host-partner-guest-service.md`, `brief-platform-data-ml.md`, `brief-expedia-agoda-tripcom.md`, `brief-airbnb.md`, `brief-booking-com.md`, `brief-trust-safety-regulation.md`, `brief-payments-finance-tax.md`.
- **External**
  - O'Reilly, "An Introduction to Residuality Theory", *Procedia Computer Science*, 2020; *Residues*, Leanpub, 2024.
  - Ford, Parsons and Kua, *Building Evolutionary Architectures*, O'Reilly Media, 2017.
  - Airbnb, Booking Holdings and Expedia 10-K filings for FY2020; Expedia FY2022 and FY2023 10-Ks and Q1 2024 results; EU regulations 2019/1150, 2021/514, 2024/1028, 2025/516; DMA gatekeeper list; CGPJ note of 21 May 2026.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: AI-agent stressor status aligned with Frontdoor v2 (live 15 Nov 2027); Fathom bootstrap described as a 2027 shadow run from a snapshot. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,305 → 5,056 prose words; lead merged to two paragraphs; restating sentences cut across Concepts, Architecture, workshop and Trade-offs; Failure Modes compressed to pointers where the body handles the failure; Chief Architect's view tightened; questions 5 and 6 merged (nine → eight). No heading changes. *(AI-mediated session)*
