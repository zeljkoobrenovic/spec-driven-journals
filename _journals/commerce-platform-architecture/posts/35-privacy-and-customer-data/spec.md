---
status: accepted
revised: 2026-11-07
---

# Spec: Whose Data Is It? Privacy, Consent and Retention

## Intent

Make a reader new to the field able to say where personal data lives in a commerce estate, which legal role and lawful basis each flow has, and how consent, retention and deletion are designed across many systems. The chapter reads the GDPR and ePrivacy rules as an architect (controller and processor, lawful bases, demonstrable consent, the one-month request deadline, tax retention) against dated primary sources (the Official Journal texts, the EDPB guidelines, the Dutch and Belgian regulators, business.gov.nl, §147 AO, Shopify's compliance webhooks, the Sephora settlement, the DPF and its pending appeal), and makes a deletion request that touches nine of Kestrel & Pine's systems the spine. After reading, the reader can annotate the system-of-record map with a legal role per system, explain why the order and the marketing profile must separate, and describe the identity index, the request orchestrator and the per-system action table.

## Audience

Newcomers to commerce architecture. The engineer or integration lead who inherits the first deletion request, and the product manager asked whether a tracking tag or a CDP is allowed, benefit most; the operations or finance lead who must reconcile "delete my data" with "keep the invoice for seven years" benefits next, because the chapter gives the split (person versus transaction) that resolves it.

## Success criteria

- [x] A reader new to the field can define every term the chapter uses from the chapter alone (personal data, GDPR, controller, processor, DPA, lawful basis, consent, soft opt-in, data subject request, retention, pseudonymization, CMP, server-side tagging, adequacy decision, SCCs, DPF, identity index, request orchestrator, OMS, WMS, PSP, POS, PIM, iPaaS, CDP); every acronym is expanded on first use.
- [x] The business problem (fines, trust, the one-month clock, data in nine places) comes before any component.
- [x] A data inventory table (data, where, purpose, lawful basis, retention), a role table per system (processor, independent controller), a lawful-basis table, a requirements table per privacy flow, a per-system action table (erase, pseudonymize, retain, plus refer and except) and a trade-off table across runbook, platform-centered, orchestrator and privacy product.
- [x] The "Across Scale Stages: When It Fits and When It Limits" section with the four-stage table and a judgement.
- [x] A Kestrel & Pine worked example labeled illustrative: the request from Ghent of 10 May 2027 touching nine named systems from the ledger's systems table (platform, marketplace connector, ERP, WMS, shipping service, PSP, POS, returns portal, data warehouse), answered 4 June 2027; the autumn 2027 orchestrator and the two-day second request.
- [x] Three mermaid diagrams with captions (controller and processors; the deletion fan-out sequence; the person-versus-transaction split); a "When It Goes Wrong" table; the three take-away tiers; 6–10 questions; a closing hand-off to [[commerce-regulation]]; grouped, dated Sources and Evidence.
- [x] Retention facts carry their verification status: Dutch seven years verified (business.gov.nl), German ten, eight and six verified (§147 AO), Belgian ten years labeled unverified.
- [x] Article at or under 6,500 words including tables; the chapter states once that it is not legal advice.

## Non-goals

- Customer identity, matching, survivorship and the cross-reference itself — [[identity-and-master-data]] (this chapter only reuses the index).
- Security controls: card data, PCI DSS, account takeover, bots, skimming, admin MFA — [[commerce-security]].
- The regulatory calendar beyond privacy: consumer law, e-invoicing, accessibility, DSA, product safety, AI Act — [[commerce-regulation]].
- App governance and the app inventory — [[extensibility-and-app-ecosystems]]; the integration inventory itself — [[integration-styles]].
- Analytics design and metric definitions on pseudonymized data — [[commerce-data-and-analytics]].
- A country-by-country legal treatment; the chapter is explicit that it is not legal advice.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- The Belgian ten-year retention rule (VAT Code Article 60) and the Dutch official pages beyond business.gov.nl could not be fetched; a reviewer with access should confirm. The German eight-year voucher period's start date (2025 reform) is not relied on.
- Lotte Claes (a Ghent customer) is a new local character introduced for the deletion example; the ledger addition records her request so other chapters can reuse it. The claims window (twelve months) and backup retention (35 days) are labeled assumptions.
- The Digital Omnibus proposal and the DPF appeal are volatile; the chapter dates both "as of November 2026" and a reviewer should re-check before publication.

## Decision log

- **2026-11-07** — Made the deletion request the spine (scene, Figure 2, action table, worked example) rather than cookies, because the contract names it and because it is the privacy problem that exposes the integration map most directly; cookies and tracking are taught as the consent half.
- **2026-11-07** — Chose a new minor character in Ghent for the request instead of Eva Janssen, so that the recurring order stays intact for the Journeys chapters and so that a Belgian customer brings the Belgian regulator, bpost and a bol order into one example.
- **2026-11-07** — Took the explicit position that server-side tagging is governance, not a consent bypass, following the EDPB technical-scope guidelines and labeled as the author's reading.
- **2026-11-07** — Kept the vendor's processor obligations to one paragraph and the US contrast (CCPA, GPC, state laws) to one paragraph, because the book is Europe-first and the US detail belongs to [[commerce-regulation]].

## Sources

- **Internal**
  - [[meet-kestrel-and-pine]] — the systems table, the cast, the Familiar Stranger; [[identity-and-master-data]] — the identity index and consent on the master.
  - [[boundaries-and-systems-of-record]], [[integration-styles]], [[organizing-commerce-engineering]] — the maps and inventories this chapter adds a legal-role column to.
  - [[extensibility-and-app-ecosystems]], [[replatforming-and-migration]], [[stores-and-omnichannel]] — neighbouring chapters that reference the nine-system deletion.
  - `_research/brief-security-privacy-regulation.md` Part 2 and `_research/brief-integration-and-data.md` Section 4.6 — the evidence base.
  - `_research/scenario-ledger.md` — all Kestrel & Pine figures.
- **External**
  - GDPR (Regulation (EU) 2016/679), Articles 4, 6, 7, 12, 28, 33, 83; Directive 2009/136/EC (ePrivacy Article 5(3)); Directive 2002/58/EC Article 13(2).
  - EDPB Guidelines 07/2020 (controller and processor, 2021), 05/2020 (consent, 2020), 2/2023 (technical scope, 2024).
  - Autoriteit Persoonsgegevens, "Cookies" (n.d.); Gegevensbeschermingsautoriteit, "Cookies en andere traceringsmiddelen" (2023).
  - business.gov.nl, "Keeping business records" (verified 2026-11); §147 Abgabenordnung.
  - Shopify developer documentation: privacy law compliance webhooks; protected customer data (accessed 2026-11).
  - California Attorney General, Sephora settlement (2022) and CCPA page; IAPP state tracker (2025–2026).
  - Decision (EU) 2023/1795 (DPF); Decision (EU) 2021/914 (SCCs); Case C-703/25 P; Lewis Silkin (2025); Osborne Clarke (2025).

## Changelog

- **2026-11-07** — Initial spec and article. *(AI-mediated session)*
- **2026-11-07** — Editorial review pass: acronyms expanded (PSP, WMS, ERP, POS, iPaaS, OMS, CDP, EDPB, IAPP), app count and deadline arithmetic corrected, PIM removed from processor row, Sephora flagged as older evidence. *(AI-mediated session)*
- **2026-11-07** — Final consistency pass: dated the unowned-integration count (13 of 34 as of January 2027; 5 still unowned in April 2027, item 16); scale-stage reference no longer points to the ledger. *(AI-mediated session)*
- **2026-11-07** — Visual layer: redrew 3 mermaid diagrams as illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
