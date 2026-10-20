---
status: accepted
revised: 2026-10-20
---

# Spec: Who Is on the Other Side? Identity and Verification

## Intent

Give architects of listing marketplaces a precise model for identity: how much a marketplace should know about its users, how it verifies it, and how one identity service can serve a group of brands. The chapter separates proof of person, strength of authentication and proof of business; defines identity levels as derived from expiring, revocable claims; treats verified badges as promises with a stated scope; covers passkeys, risk-based authentication and recovery as the defense against account takeover; and argues that a group identity must be designed so that a brand can be separated. After reading, an architect can design the claim contract, the level policy and the group identity topology, and can challenge a "verified" badge that promises more than was checked.

## Audience

Chief and enterprise architects of marketplace groups, identity and security leads, trust-and-safety and product leaders who decide where friction goes, and data protection officers who must approve what verification collects. They know OIDC and MFA in general; they need the marketplace-specific model and the group-level trade-offs.

## Success criteria

- [ ] Reader can explain why proofing, authentication and business verification are separate axes, with the NIST SP 800-63-4 vocabulary as the reference.
- [ ] Reader can design a claim record (type, method, source, attributes, assurance, expiry, status) and derive identity levels and badges from it.
- [ ] Reader can place step-up verification at specific risky actions and estimate its cost, using the Hearthly Spain rental policy as a worked example.
- [ ] Reader can name the account-takeover controls (passkeys, risk-based authentication, recovery assurance, payout-change holds) and the pre-hijacking risk of merging accounts by e-mail.
- [ ] Reader can compare per-brand, shared and pairwise-profile group identity options and explain why separability matters, using the documented Schibsted account separation.
- [ ] Reader can state what the EU Digital Identity Wallet does and does not oblige a marketplace to do, with dates verified against the Official Journal.
- [ ] Every company claim carries a dated source; inferences about real companies are labeled.

## Non-goals

- The seller account model, organizations, branches and trader status — [[sellers-and-accounts]].
- Risk scoring, fraud signals and step-up friction as fraud controls — [[fraud-prevention]].
- The legal detail of DSA trader traceability, DAC7 and other regulation — [[marketplace-regulation]].
- Message-level safety controls — [[messaging-and-leads]].
- Payment KYC internals of PSPs — [[transactions-and-payments]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- EUDI Wallet relying-party fees and per-country availability in Veldmark's markets are not yet known (as of October 2026); revisit when wallets launch.
- The exact date of the Art. 5f(2) private-relying-party obligation is inferred from the implementing acts' entry into force; confirm when the Commission publishes guidance.
- Whether Spain's or France's national eID schemes can serve Hearthly's L4 checks at acceptable cost was not researched.

## Decision log

- **2026-10-19** — Modeled identity as claims with derived levels instead of a single verification flag, because the documented failure (a phone-verified scammer shown with a tick) comes from conflating claims.
- **2026-10-19** — Used FINN (BankID badge, Vend account, Schibsted account separation) and Mercari (passkeys, recovery) as the documented cases, because they are first-party, dated and current; rejected job postings and vendor marketing as evidence.
- **2026-10-19** — Made separability a first-class design rule for Veldmark ID, connecting the PE ownership in the ledger to the Schibsted separation, rather than presenting group SSO as an unqualified synergy.
- **2026-10-19** — Verified eIDAS 2.0, DSA and GDPR article references against Official Journal texts retrieved through the EU Publications Office, since EUR-Lex itself was blocked.

## Sources

- **Internal**
  - [[trust-and-safety-architecture]] — the March 2027 phishing incident and the cross-brand phone number.
  - [[fraud-prevention]] — the Barcelona fake-rental ring and step-up friction.
  - [[sellers-and-accounts]], [[marketplace-regulation]], [[case-adevinta]] — adjacent ownership and the separability lesson.
- **External**
  - Mercari Engineering (2026) — passkeys, risk-based authentication, recovery.
  - FINN help center (2024–2026) — BankID verification, two-step authentication, Schibsted/Vend account.
  - Regulation (EU) 2022/2065 Art. 30; Regulation (EU) 2024/1183 Arts. 5a and 5f; Implementing Regulations (EU) 2024/2979 and 2025/848; GDPR Arts. 5 and 25.
  - NIST SP 800-63-4 (2025); FIDO Alliance passkeys; Sudhodanan and Paverd (2022) on pre-hijacking; Adyen platform verification documentation; Integrity Institute for Ofcom (2026).

## Changelog

- **2026-10-19** — Initial spec and article. *(AI-mediated session)*
- **2026-10-19** — Editorial review pass: eight countries (not seven); Veldmark ID approval is three months, not two, after the March account review. *(AI-mediated session)*
- **2026-10-19** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-20** — Cross-chapter consistency sweep: 4 heading(s) aligned with the book's shared section names, glossary terms and source-group structure; no body text changed. *(AI-mediated session)*
- **2026-10-20** — Sharpening pass: 6,361 → 6,394 prose words; outline unchanged; opening now ties the chapter to Part V and fraud-prevention's hand-off and names the chapters that build on it; 14 paragraph openings rewritten to state their point; two long paragraphs (Mercari/FINN, Schibsted/Vend) split; no facts or quotations removed. *(AI-mediated session)*
- **2026-10-20** — Consistency fix: excerpt now describes separate claims on three axes combined into levels, matching the body and Figure 1, instead of "a ladder of separate claims"; H3 "Two axes, not one ladder" renamed "Three axes, not one ladder", the section's own conclusion. *(AI-mediated session)*
- **2026-10-20** — Replaced 2 mermaid diagram(s) with generated illustrations (figure numbers and captions unchanged; sources archived in `_research/mermaid-figures.json`); known differences from the source: Figure 2: kept attempt 1: 'Fraud and T&S platform' drawn inside the 'Veldmark ID' panel; 'Hearthly' → 'Authentication service' (OIDC login) arrow missing; invented arrow 'Profile service' → 'Hearthly'; 'Account recovery' → 'Authentication service' and 'Authentication service' → 'Profile service' drawn without arrowheads; Figure 3: kept attempt 1 (structure correct): invented title/caption sentence printed at top; words START and END printed beside the dots. *(AI-mediated session)*
