---
status: accepted
revised: 2026-10-20
---

# Spec: Rules of the Marketplace: DSA, DAC7 and Vertical Regulation

## Intent

Show architects of listing marketplaces which regulations shape their systems and how each becomes a system requirement. The chapter maps legal roles (hosting service, online platform, platform allowing distance contracts with traders, online intermediation service, online marketplace, reporting platform operator) to marketplace features, and makes the central point that transaction features move a classifieds site across regulatory perimeters. It turns the DSA, P2B, Omnibus consumer rules, GDPR, DAC7 and vertical disclosure rules (energy performance, new-car labeling) into requirements for a small set of compliance-by-design components: an obligation register, a decision record and evidence store, a trader registry, disclosure surfaces and reproducible reporting views. Veldmark's statement-of-reasons and DAC7 pipelines are the worked examples.

## Audience

Chief and enterprise architects, trust-and-safety, data and payments leads, and regulatory or data-protection leads who must jointly turn legal obligations into systems. They are not lawyers; they need article-accurate obligations, the engineering consequence of each, and a structure that survives the next law.

## Success criteria

- [ ] Reader can explain which rules reach a pure lead-generation classifieds site and which turn on contracts or payments concluded through the platform, with the P2B, UCPD, DSA Section 4 and DAC7 definitions as evidence.
- [ ] Reader can map each relevant DSA article to a system requirement and an owning component, including demotion and payment holds as restrictions.
- [ ] Reader can design a statement-of-reasons pipeline against the Transparency Database schema (batches of 100, `puid` idempotency, no personal data, documented exceptions).
- [ ] Reader can describe DAC7's platform definition, excluded-seller test, quarterly consideration and deadlines, and design the pipeline from the payment ledger.
- [ ] Reader can specify ranking, paid-placement, seller-status, price-reduction and review disclosures, and regulated listing attributes for property and new cars.
- [ ] Reader can set retention per data class, including the DSA's mandatory deletion of trader data.
- [ ] Article references are verified against Official Journal texts; time-sensitive facts carry dates.

## Non-goals

- The moderation pipeline, decision service and enforcement propagation — [[trust-and-safety-architecture]].
- Identity levels, KYB and the business registry — [[identity-and-verification]].
- Payment flows, licensing and buyer protection — [[transactions-and-payments]].
- Ranking and ad-stack internals — [[ranking]], [[advertising-platforms]].
- Legal advice, national transposition detail and competition law.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Whether a pure classifieds listing with a contact button "allows consumers to conclude distance contracts with traders" (DSA Section 4, CRD Art. 6a) remains unsettled; the chapter assumes yes for trader listings.
- Whether a private seller's paid bump is an "advertisement" under DSA Art. 26 or a "paid-for advertisement" under the UK Online Safety Act is left to counsel.
- Status of the proposed P2B repeal and the Digital Fairness Act proposal should be rechecked at the next revision.
- National DAC7 record-keeping periods were not researched per country.

## Decision log

- **2026-10-19** — Organized the chapter around legal roles triggered by features, rather than law by law, because the perimeter shift caused by payments is the most consequential architectural fact.
- **2026-10-19** — Verified DSA, P2B, Omnibus, DAC7, GDPR, EPBD and the transparency-report implementing regulation against Official Journal texts retrieved through the EU Publications Office (EUR-Lex itself was blocked), and added the marketplace section's own small-enterprise exemption (Art. 29), which the brief did not cover.
- **2026-10-19** — Kept UK and US rules to one table, since Veldmark operates only in the EU, while showing that INFORM repeats the DAC7 payment-trigger pattern.
- **2026-10-19** — Used the Femke account suspension and the Lyon apartment's DPE as worked examples to stay consistent with the ledger and with the trust-and-safety chapter.

## Sources

- **Internal**
  - [[trust-and-safety-architecture]] — decision record, 20,000 weekly statements at Tradeyard NL, block-list retention.
  - [[identity-and-verification]] — trader and business registry.
  - [[transactions-and-payments]], [[attribute-schemas]], [[ranking]], [[advertising-platforms]] — systems the obligations land in.
- **External**
  - Regulation (EU) 2022/2065; Implementing Regulation (EU) 2024/2835; DSA Transparency Database and API documentation.
  - Regulation (EU) 2019/1150; Directive (EU) 2019/2161; Council Directive (EU) 2021/514; Regulation (EU) 2016/679; Directive (EU) 2024/1275.
  - Service-Public.fr (DPE); Pkw-EnVKV; Ofcom and legislation.gov.uk (Online Safety Act); FTC (INFORM); 24 CFR § 100.75; FINN help center on ratings.

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: Safe Deal 2026 volume updated to 11.6M transactions / ~€1.02B GMV; Country Fork cost aligned to eight countries; closing hand-off now links [[part-6]]; Transparency Database and P2B-repeal claims spot-checked. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,993 → 7,029 prose words; opening now ties the chapter to Part V and to Part VI; twelve paragraph openings rewritten to state their point; no headings or facts changed; spec unchanged. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: the three surprising table entries now name ranking, payments and seller-data teams (not messaging); the statement-of-reasons pipeline's four stages are named, as Figure 2's eight participants did not show them. *(AI-mediated session)*
