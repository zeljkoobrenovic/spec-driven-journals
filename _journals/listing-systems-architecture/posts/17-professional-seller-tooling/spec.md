---
status: accepted
revised: 2026-10-20
---

# Spec: Serving the Pros: Dealer, Agent and Merchant Tooling

## Intent

Close Part III by explaining what professional sellers need from a marketplace and how to architect it. The chapter owns **pro tooling**, **lead management for pros** and **pro SaaS**. Its argument: professionals buy outcomes and check them against their own systems, so statistics, lead exports and billing must come from one event stream; pro tooling should be a workspace over domain systems of record plus a first-class partner API; and software sold to professionals (an agent CRM that publishes to competing portals) must be neutral by architecture, enforced through four controls that produce audit evidence.

## Audience

Architects and engineering leads who own dealer portals, agency workspaces, partner APIs or an acquired pro SaaS product, and group leaders who must decide what to share and how to keep a SaaS business neutral. They know BFFs, event streams and OAuth; they need the professional's view and a design that survives renewal negotiations and independent review.

## Success criteria

- [ ] The reader can list the professional's jobs and the capabilities that serve each, with a dated public example per row.
- [ ] The professional's lead lifecycle is shown as a state diagram, and the chapter explains which states the marketplace observes and which return from the CRM.
- [ ] A reference architecture diagram shows the pro API gateway, workspace backend, lead ledger, performance read model and one event stream feeding statistics, leads and billing.
- [ ] The Golf's 23 contacts are reconciled to 19 deduplicated leads and 14 CRM leads, consistent with [[monetization-models]], with concrete design changes.
- [ ] Neutrality is designed with four controls (separate tenancy, API parity, data boundary, ranking blindness) and grounded in P2B Articles 7 and 9, noting the 2025 repeal proposal.
- [ ] The Keybridge example answers whether Hearthly may see the portal performance report, with a boundary diagram and an evidence pack.
- [ ] Trade-off table (build, integrate, own SaaS) and vertical-differences table are present.
- [ ] Company claims carry dated sources; inferences are labeled.

## Non-goals

- Lead, conversation and lead routing design on the marketplace side: [[messaging-and-leads]].
- Package, entitlement and billing systems: [[products-and-entitlements]]; revenue models: [[monetization-models]].
- Organization hierarchy and trader status: [[sellers-and-accounts]].
- Feed contracts and ingestion: [[listing-ingestion]].
- AI agents acting for professionals: [[ai-in-listing-systems]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The legislative status of the proposed P2B repeal should be re-checked before print.
- Whether a dealer's DMS sale export by VIN is personal data under GDPR (it links to a buyer) needs counsel; the chapter treats sale matching as opt-in per dealer.
- Immowelt's historical broker software was only WIDELY REPORTED in the brief and is deliberately not cited.

## Decision log

- **2026-10-19** — Framed the chapter around the professional's jobs and the reconciliation test rather than a feature catalog, because renewal depends on numbers that match the professional's systems.
- **2026-10-19** — Kept the marketplace-side lead model in [[messaging-and-leads]] and modeled only the professional's lifecycle here, to avoid two definitions of a lead.
- **2026-10-19** — Verified P2B Articles 7 and 9 directly (legislation.gov.uk EU text) to ground neutrality in law, rather than relying on the brief's Article 5 coverage.
- **2026-10-19** — Introduced Motorvane Dealer Hub and Autohaus Ruhrblick's package as local facts (now the canonical Pro 150 package, €1,450/month, 150 slots, per the editor's ledger line), recorded in the scenario ledger with the Keybridge parity and evidence-pack rules.

## Sources

- **Internal**
  - [[meet-veldmark]], scenario ledger — Keybridge decision, Golf and Lyon examples.
  - [[monetization-models]] — lead-ledger proposal and the 19-lead deduplication rule.
  - [[vertical-requirements]] — the layer model used for shared engines versus brand front ends.
- **External**
  - Autotrader FY2026 results and developer portal; mobile.de Seller API and July 2026 platform update; CarGurus and Cars.com 10-Ks; Cox Automotive.
  - Rightmove RTDF v1.4.1 and FY2025 results; Zillow 10-K FY2025; Scout24 FY2025 preliminary results; AVIV Ultimmo (2022).
  - OLX causal-inference post (2026); Vinted commercial-selling Q&A (2026); Bundeskartellamt mobile.de/Carwow clearance (2026).
  - Regulation (EU) 2019/1150 Articles 7 and 9; European Commission P2B page; RFC 9700.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Ruhrblick moved to the canonical Pro 150 package (€1,450, 150 slots), sale-record date aligned with ingestion, Rhône Habitat branch wording, OLX causal claim corrected to the source, P2B verified against the Official Journal, hand-off to [[part-4]]. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 1 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
