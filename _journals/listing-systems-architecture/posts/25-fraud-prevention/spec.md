---
status: accepted
revised: 2026-10-20
---

# Spec: Scams, Fakes and Account Takeovers: Fraud Prevention for Listings

## Intent

Explain how listing marketplaces detect and stop fraud, and what the architecture behind it looks like. The chapter sets out the classifieds threat model: mostly authorized push payment fraud that happens off-platform, which pushes the controls before the payment. It gives a typology and a signal taxonomy, then designs a risk scoring service with real-time and streaming paths, rules and models, an identity graph and actor-level scoring. It shows step-up friction with an explicit cost model, covers messaging-based scams and the feedback loop with its late and biased labels, and makes the case for bank and police collaboration. The Barcelona fake-rental ring is the main worked example. Its signals existed on day one, and the lesson is how to act on them on day one.

## Audience

Heads of trust and safety, fraud and data science leads, principal engineers on insertion, messaging and identity, and chief architects deciding what to share across brands. Readers know ML and streaming basics; they may not know APP fraud, perceptual hashing or friction economics.

## Success criteria

- [ ] Owns and defines fraud signal, risk score and step-up friction.
- [ ] Gives a fraud typology with dated public evidence (UK Finance 2026, OLX 2026, Which? 2024, Meta 2024).
- [ ] Gives a signal taxonomy with availability and cost of evasion, including price and graph signals.
- [ ] A component diagram of the risk scoring service separates real-time from streaming and batch work; the feature store is presented as conditional, with point-in-time correctness.
- [ ] Rules and models are compared, and the rule lifecycle (backtest, shadow, rollout, audit) is grounded in Stripe Radar and Sigma.
- [ ] A friction threshold example with arithmetic shows the cost-minimizing threshold and names who owns the inputs.
- [ ] The Barcelona ring agrees with the ledger (26 accounts, 180 listings, about 35% below market, 63 victims, about €71,000, perceptual-hash plus price-anomaly detection) and with [[entity-resolution]], and ends in a missing-capability table.
- [ ] Includes messaging controls, the label-source table, adversarial adaptation, bank and police collaboration, trade-offs, vertical differences, failure modes, the Chief Architect's view and 10 questions.

## Non-goals

- The moderation pipeline, decision service, enforcement propagation, appeals and T&S metrics: [[trust-and-safety-architecture]].
- Identity levels, KYB, passkey rollout and verified badges in depth: [[identity-and-verification]].
- The legal analysis of message scanning, the DSA and the UK Online Safety Act: [[marketplace-regulation]].
- Payment-side fraud in transactional flows and buyer protection design: [[transactions-and-payments]].
- Perceptual hashing as an image capability: [[media-pipeline]]. Clustering of legitimate duplicates: [[entity-resolution]].
- The feature store and model governance as platform components: [[ml-platform]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- The Airbnb targeted-friction evidence comes from a 2018 InfoQ summary; the original Medium post was not fetched (Medium returns 403). Verify against the original before print.
- No classifieds fraud-scoring architecture is publicly documented. Revisit if Vinted's Trust & Safety streaming talk or Adevinta material becomes fetchable.
- The friction cost model's inputs (€180 harm per fraud account, €25 per lost genuine account, 8% abandonment) are illustrative; a later edition could use published abandonment data if any exists.
- The Verification of Payee non-euro-area date is reported inconsistently by secondary sources; only the euro-area date is used.

## Decision log

- **2026-10-19** — Framed Barcelona as "signals existed, decisions failed" rather than "detection failed", to agree with the ledger and with [[entity-resolution]], which says the hash index caught the ring, and because the decision gap is the more useful lesson.
- **2026-10-19** — Kept the 7 March 2027 city bike phishing as a secondary example limited to message-gate design, leaving its conversation to [[messaging-and-leads]] and its enforcement propagation to [[trust-and-safety-architecture]].
- **2026-10-19** — Recommended "buy signals, own decisions and labels" instead of a pure build or buy answer, because label portability is the long-term asset.
- **2026-10-19** — Used a worked threshold table instead of abstract ROC discussion, so readers see that the optimum depends on business-owned cost inputs.

## Sources

- **Internal**
  - `_research/brief-trust-safety-regulation.md` — typology, UK Finance data, OLX evidence, Grigorev pipeline, PDQ, messaging design, Mercari, friction evidence, feedback loops.
  - `_research/brief-platform-data-ml.md` — feature store evidence (Uber 2017), absence of classifieds feature-store documentation, price model as fraud feature.
  - `_research/scenario-ledger.md` — Barcelona ring, city bike phishing, Tradeyard messaging and phishing report volumes.
  - [[trust-and-safety-architecture]], [[entity-resolution]], [[attribute-schemas]] — neighbouring chapters kept consistent.
- **External**
  - UK Finance, *Annual Fraud Report 2026*. OLX Group (2026), ITWeb (2018), PyCon DE (2019), Mercari (2026), Meta (2015, 2024), Stripe Radar docs, InfoQ on Airbnb (2018), Uber (2017), PDQ, McCann FitzGerald on Verification of Payee (2025), Integrity Institute for Ofcom (2026), Which? (2024).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: stated that the Barcelona ring's 26 accounts had proved only an e-mail address, matching identity-and-verification; UK Finance, OLX and Mercari figures spot-checked. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 3 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 5,991 → 6,044 prose words; lead now ties the chapter to Part V and to the trust-and-safety and identity chapters; "Messaging-Based Scams" renamed "Fraud Controls in Messaging"; five paragraphs restructured so their point comes first; no spec criteria changed. *(AI-mediated session)*
