---
status: accepted
revised: 2026-10-21
---

# Spec: Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law

## Intent

Show architects which regulations shape a stays marketplace and how each becomes a system requirement, and argue for **compliance by design**: rules held as versioned data with a legal source, effective period and owner in one **market policy registry**, evaluated at a few fixed enforcement points (publish, book, sweep, report), with every decision stored with its rule version and reason code so it can be explained to a host, a guest or an authority, and reversed when a court changes the law. The chapter maps the EU Short-Term Rental Regulation (EU) 2024/1028, national and city rules, the DSA, DMA, P2B, consumer law, GDPR, guest registration, PSD2, the European Accessibility Act and the AI Act (as amended by the 2026 AI Omnibus) onto system requirements, and uses Spain's 2026 registry annulment to show why rule provenance matters. After reading, the reader can design the registry, evaluator, evidence store and regulator gateway, and decide what a multi-brand group shares.

Productscape domains covered: HSM `comp` (Local Compliance & Policy Controls: market policy registry, listing eligibility, audit state); TAM `cont` (policy authoring workspace); residuality stressor `licn` (eligibility per unit, operator, jurisdiction and stay date).

Owns: STR registration, market policy registry, compliance by design (stays).

## Audience

Chief architects, platform and trust leads, and engineering directors of OTAs and hosted-stays marketplaces who must answer to regulatory affairs and legal teams, plus the regulatory leads who need to know what to ask engineering for. They should leave with a component model, a rule schema, the enforcement-point table and a governance split.

## Success criteria

- [ ] Reader can state what Regulation (EU) 2024/1028 requires of platforms (Articles 6–9, 13), its scope excluding hotels, and its dates.
- [ ] Reader can map each instrument in the regulatory table to a system requirement and an owning chapter.
- [ ] Reader can name the rule primitives and explain why night caps cannot be certified by one platform.
- [ ] Reader can describe the obligation register, authoring workspace, registry, resolver, evaluator, evidence store and regulator gateway, and the fields of a rule version (including transition policy and retroactive end date).
- [ ] Reader can explain the four enforcement points and their fail behavior.
- [ ] The Corvane worked example matches the ledger (6,900 listings; 2,900 honored; 8,300 canceled; purge February–April 2026 before the May 2026 ruling) and shows the replay that reason codes make possible.
- [ ] Spain's Supreme Court annulment is described from official sources (CGPJ note; BOE consolidated text), with regional numbers still applying; company claims carry dated sources and inferences are labeled.
- [ ] Chapter contains a trade-off table, the Hotels and Homes section and table, three mermaid diagrams, the Chief Architect's view and questions to ask.

## Non-goals

- Trader verification (KYC/KYB) and the readiness service ([[partner-onboarding]]).
- Unit identity and the place registry ([[property-and-listing-model]]); jurisdiction geometry ([[destinations-and-maps]]).
- Total-price display rules and the display policy service ([[property-page-and-room-selection]]).
- Ranking transparency, P2B Article 5 and DMA parity in ranking ([[stays-ranking]]).
- Trust policy, enforcement actions and statements of reasons as a moderation workflow ([[stays-trust-and-safety]]); review law ([[reviews-and-reputation]]).
- Tax, DAC7 and ViDA ([[taxes-on-stays]]); payment licensing ([[merchant-and-agency-models]]).
- Legal advice on any jurisdiction.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Which Supreme Court judgment number corresponds to which date: the CGPJ note (21 May 2026) names judgment 620/2026; the BOE consolidated text cites judgments of 19 May, 21 May and 1 June 2026. The chapter says "announced on 21 May 2026" and cites both.
- How Spain's digital single window now validates numbers after Article 10 of Royal Decree 1312/2024 was annulled, and which regional registers offer machine lookups.
- Which Member States had live single digital entry points and published Article 13 lists by mid-2027; the Commission's technical API specification was not reviewed.
- Paris 90-night cap rests on a secondary source; Amsterdam rules rest on Airbnb's undated help page.
- Whether Article 32 DSA (right to information) applies to homes sold without a required registration number is the author's reading, flagged as such ("may count").

## Decision log

- **2026-10-21** — Framed regulation as an obligation → control → rule → evidence chain rather than a law-by-law survey, because the reusable architecture is the same across instruments; the survey is compressed into one table with short subsections.
- **2026-10-21** — Used the Spanish purge and the later annulment as the scene and the replay, per the editor's ledger line: purge February–April 2026 under the then-valid national registry, annulment as a real event, Corvane's removals fictional, regional numbers still applying. The lesson is reason codes and rule provenance, not Spanish law.
- **2026-10-21** — Recommended fixed rule primitives over a general rules language, and a shared registry/evaluator/evidence/gateway with per-brand enforcement points and classification.
- **2026-10-21** — Treated the AI Act briefly with the AI Omnibus dates (Annex III from 2 December 2027) verified on the Commission's page, because most stays systems are not high-risk.

## Sources

Internal: [[partner-onboarding]], [[property-and-listing-model]], [[destinations-and-maps]], [[calendar-sync]], [[property-page-and-room-selection]], [[stays-ranking]], [[stays-trust-and-safety]], [[taxes-on-stays]], [[changes-and-cancellations]], [[event-driven-stays]].

External: Regulation (EU) 2024/1028 (CELEX 32024R1028); Real Decreto 1312/2024 (BOE-A-2024-26931, consolidated text); CGPJ note on judgment 620/2026; Real Decreto 933/2021; DSA (32022R2065); DMA (32022R1925); P2B (32019R1150); Omnibus Directive (32019L2161); GDPR (32016R0679); PSD2 (32015L2366); EAA (32019L0882); AI Act (32024R1689) and the Commission's AI Omnibus note (2026); Airbnb and Booking Holdings 10-Ks for 2025; Airbnb City Portal (2021) and Amsterdam help page; Booking.com DSA page and connectivity docs; Expedia lodging supply hub; NYC Local Law 18; Service-Public.fr; Catalan News, TechCrunch, Hosteltur and Houst as secondary sources.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: American spelling (license, program), timetoread 37→34; purge timing and Supreme Court judgments verified against the BOE consolidated text; AI Omnibus dates verified; unverified Article 3(12) pin-cite replaced by a reference to the activity-data definition. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: dropped the authoring workspace from the compliance-chain caption to match the diagram. *(AI-mediated session)*
