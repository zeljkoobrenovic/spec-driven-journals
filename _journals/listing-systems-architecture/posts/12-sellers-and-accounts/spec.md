---
status: accepted
revised: 2026-10-20
---

# Spec: Private Sellers, Dealers and Agencies: Modeling Who Lists

## Intent

Give architects a supply-side seller account model that works from a private seller with one bike to an agency network with franchisees, and show why it must separate four questions that account models usually conflate: who acts (user), who is responsible (legal entity, the trader), who pays (contract and billing account) and who is shown (storefront, branch). Make trader status a governed attribute with evidence and a reclassification process, show integrations as principals with scoped grants, and settle how a multi-brand group shares identity and verified legal facts without merging brand accounts.

## Audience

Chief and principal architects, identity and account-platform leads, and product leads for professional sellers in listing marketplaces, plus technology leaders integrating acquired brands. They know authentication and data modeling; they need the marketplace-specific shape, the regulatory drivers and the group-level choices.

## Success criteria

- [ ] Reader can name the entities of the seller account model (user, legal entity, seller account, branch, network, contract, storefront, integration principal) and what each answers.
- [ ] Reader can explain why franchise networks break a model where branches are children of one legal entity.
- [ ] Reader can list the four parts of a trader status record and describe a reclassification process.
- [ ] Reader can map DSA Art. 30, the consumer-law trader declaration, P2B, DAC7 and INFORM to account data, with dated sources.
- [ ] Reader can design integration authentication with scoped grants, citing RFC 9700 and documented portal interfaces (mobile.de, Rightmove).
- [ ] Reader can compare group identity options and state purpose limits for a shared registry (the Keybridge case).
- [ ] The chapter includes Veldmark worked examples (Agence Rhône Habitat, Femke, Autohaus Ruhrblick, the Poland overlap), trade-off and vertical tables, three diagrams, a Chief Architect's view and design-review questions.

## Non-goals

- Authentication methods, verification levels, KYB vendors and verified badges: [[identity-and-verification]].
- The legal analysis of the DSA, DAC7 and consumer law: [[marketplace-regulation]].
- Packages, pricing, entitlements and billing: [[products-and-entitlements]].
- Lead objects, conversations and routing mechanics: [[messaging-and-leads]].
- Pro tooling and CRM features: [[professional-seller-tooling]].
- Feed contracts and ingestion mechanics: [[listing-ingestion]].
- Reclassification signals and moderation cases: [[trust-and-safety-architecture]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- ~~The wording of the consumer-law provisions (CRD Art. 6a; UCPD Art. 7(6))~~ — resolved 2026-10-19: checked against the Official Journal text of Directive (EU) 2019/2161 via the EU Publications Office; the chapter's summaries are accurate.
- The CJEU's criteria for when an online seller is a trader (Kamenova, C-105/17, 2018) would strengthen the reclassification section; the judgment could not be fetched in this session and is not cited.
- Whether the DSA allows an exception to displaying a home-based sole trader's address (as INFORM does) remains open; see [[marketplace-regulation]].
- National licensing of estate agents (for example France's professional card) is mentioned only generically; verify per country if the chapter is extended.

## Decision log

- **2026-10-19** — Framed the model around four questions (acts, responsible, pays, shown) rather than an entity list, because each Veldmark failure in the scene maps to one conflated question.
- **2026-10-19** — Recommended "seller account linked to a user or a legal entity" over "degenerate organization of one", to keep private sellers' data minimal and make reclassification explicit.
- **2026-10-19** — Used the Keybridge neutrality commitment as the test case for group identity, so the chapter argues for shared identity and verified facts with purpose limits, not a single group account.
- **2026-10-19** — Labeled the party model as a reference architecture inferred from public interfaces (mobile.de, Rightmove), not a description of any company's schema.

## Sources

- **Internal**
  - [[listing-aggregate]], [[location-and-geo]], [[identity-and-verification]], [[products-and-entitlements]], [[marketplace-regulation]], [[listing-ingestion]] — neighbouring ownership.
  - `_research/brief-listing-data-ingestion.md` Part 12; `_research/brief-trust-safety-regulation.md` 4.1, 5.1, 5.4–5.6, 5.8, 5.10; `_research/brief-real-estate-portals.md` B.2; `_research/brief-monetization-economics.md` 4, 6.5; `_research/brief-automotive.md` A.3; `_research/productscape-digest.md` 2.1–2.2, 5.4.4.
- **External**
  - DSA Art. 30 (2022) — trader traceability.
  - Belastingdienst DAC7 guidance; FTC INFORM guidance (2023); European Commission CRD page.
  - mobile.de Seller API; Rightmove RTDF v1.4.1 (2023) and 2025 results (2026); Autotrader FY26; CarGurus 10-K (2026); Bundeskartellamt (2026).
  - IETF RFC 9700 (2025) — OAuth security practice.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: DSA Art. 30, CRD Art. 6a and UCPD Art. 7(6) checked against the Official Journal and cited to EUR-Lex; Bundeskartellamt finding restated as reported (8 Oct 2026); Ruhrblick KYB aligned with identity-and-verification, package named (Pro 150), Golf leads labeled raw vs deduplicated; hand-off to [[part-3]]. *(AI-mediated session)*
- **2026-10-19** — Added 3 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Renamed "party model" to the glossary's "seller account model" in Intent, success criteria and the chapter's INFERENCE callout, to match the renamed Architecture heading. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,764 → 5,788 prose words; lead now ties the chapter to Part II and names what depends on it; 1 subheading renamed ("Who acts, who pays, who is shown" → "Four questions and the entities that answer them"); commercial-unit paragraph split out; seven topic sentences sharpened; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: Figure 3 caption now counts the eight entities the diagram and table show. *(AI-mediated session)*
- **2026-10-20** — Renamed the subheading "Four questions and the entities that answer them" (from the sharpening pass) to "One entity per question": the table has eight entities and eight questions. *(AI-mediated session)*
- **2026-10-20** — Replaced 3 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 5: kept attempt 3: state names joined as 'UnderReview' and 'PendingVerification'; 'enforcement or unpaid contract' (Active to Suspended) branches off the 'limits lifted' line, so it reads as if it starts at Restricted. *(AI-mediated session)*
