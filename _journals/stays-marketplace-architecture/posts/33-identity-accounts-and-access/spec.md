---
status: accepted
revised: 2026-10-22
---

# Spec: Who Is Booking, Who Is Hosting: Identity, Accounts and Access

## Intent

Show that identity in a stays marketplace is three separable things — who someone is (the identity core: credentials, sessions, verified attributes), what each brand knows about them (accounts and traveler profiles) and what they may do (an authorization engine over roles and delegation grants) — and that the right amount of identity is set per action, not at sign-up. After reading, an architect can design or review the identity layer of an OTA, a hosted-stays marketplace or a group that runs both: define identity levels with evidence and expiry, choose authentication and session policies for guests, hosts, partner staff, machines and support agents, decide where authorization lives, minimize what is stored, and decide how far to share identity across brands.

Productscape domains covered: TAM `acct` (Traveler Account & Wallet), `idam` (Identity & Access Management), `trst` (identity and verification part); HSM `idvr` (Identity & Verification).

## Audience

Chief and principal architects, identity and platform engineering leads, trust and privacy leads, and product directors of guest accounts and partner tools at OTAs, hosted-stays marketplaces and multi-brand travel groups. They know OAuth and distributed systems; they need the stays-specific identity problems and trade-offs.

## Success criteria

- [x] Defines identity, account, traveler profile, party, grant and identity level, and owns identity level (stays), partner role model and traveler profile.
- [x] Presents an identity-level ladder (IL0–IL3 plus KYB) with evidence and expiry, and a per-action, per-brand policy table.
- [x] Presents a component architecture (session core, level store, verification service, policy engine, brand accounts, event feed) with a diagram and a responsibility table.
- [x] Grounds authentication and verification in dated public sources (Airbnb 2023 and 2026, NIST 2025, W3C WebAuthn, eIDAS 2024/1183, Secureworks 2023, Krebs 2024) and labels the Expedia identity inference.
- [x] Works two Corvane examples consistent with the ledger: the Novak family linking accounts (tourist-tax figure €56) and Hotel Miradouro's role migration, plus the 2027 baseline and the June 2027 Corvane ID decision.
- [x] Covers privacy and minimization (outcomes over documents, guest registration as a property duty, DAC7 retention against erasure) and the traveler profile and wallet boundaries.
- [x] Includes trade-off tables, the "Hotels and Homes" comparison with a sharing judgement, failure modes, the Chief Architect's view and design-review questions; two diagrams (illustrated).

## Non-goals

- Account-takeover and extranet-takeover detection, and the November 2027 phishing wave ([[travel-fraud]]).
- Trust decisions, reservation screening models and enforcement ([[stays-trust-and-safety]], [[protection-and-incidents]]).
- Onboarding funnels, KYB process and supply-party records ([[partner-onboarding]]); the delegation data model and partner workspace ([[extranets-and-host-tools]]).
- Payment authentication (SCA, 3-D Secure) and stored credentials ([[stay-payments]]); loyalty design ([[promotions-and-loyalty]]).
- The full regulatory map ([[stays-regulation]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary source describes Booking.com's guest identity verification or whether passkeys or MFA are enforced for all partners; the chapter relies on Krebs (2024) and Secureworks (2023).
- How Expedia Group links or merges accounts across Expedia, Hotels.com and Vrbo is not documented; the chapter labels its reading as inference.
- The exact date by which Member States must issue EU Digital Identity Wallets depends on the implementing acts; the chapter states the rule ("within 24 months") rather than a date.

## Decision log

- **2026-10-21** — Separated identity, brand account, profile, party, grant and identity level as distinct concepts, because the Corvane baseline (two controllers, 2.4 million overlapping people) shows that a single "user" model cannot be shared lawfully.
- **2026-10-21** — Chose "shared identity core, separate brand accounts, person-initiated linking" as Corvane's decision, consistent with One Stay and with the cross-brand consent rule already set in personalization-and-recommendations.
- **2026-10-21** — Made Nookaway's guest verification risk-based (21% of 2026 bookings) rather than universal, so Corvane does not mirror Airbnb's documented 2023 policy and the trade-off can be argued.
- **2026-10-21** — Kept the delegation grant model in extranets-and-host-tools and owned here only the role catalog, scopes, conditions and the engine that evaluates them.

## Sources

- **Internal**
  - [[meet-corvane]], [[partner-onboarding]], [[extranets-and-host-tools]], [[personalization-and-recommendations]], [[taxes-on-stays]], [[travel-fraud]], [[stays-trust-and-safety]], [[reviews-and-reputation]].
  - `_research/brief-trust-safety-regulation.md` (Parts 2, 3, 9.6), `brief-airbnb.md` (8.1–8.4), `brief-host-partner-guest-service.md` (co-hosting, One Key), `brief-payments-finance-tax.md`, `brief-platform-data-ml.md`, `productscape-digest.md` (bricks `acct`, `idam`, `trst`, `idvr`), `scenario-ledger.md`.
- **External**
  - Airbnb Engineering, Flexible Authentication (2026); Airbnb newsroom (2023, 2025); Airbnb Help article 1237; Airbnb 10-K FY2025; Expedia Group 10-K FY2025 and One Key release (2023).
  - W3C WebAuthn Level 2 (2021); NIST SP 800-63B-4 (2025); RFC 8693 (2020); Regulation (EU) 2024/1183 Article 5f (fetched 21 October 2026); GDPR; DAC7 (record retention, fetched 21 October 2026); DSA.
  - Pang et al., Zanzibar (2019); Sudhodanan and Paverd, pre-hijacked accounts (2022); Secureworks (2023); KrebsOnSecurity (2024).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: timetoread 33→36; Airbnb annual-report reference dated as fiscal 2025; Corvane ID baseline, rollout and Miradouro migration checked against the ledger. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 2 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,296 → 6,003 prose words; opening now places the chapter in Part VII (after stays-trust-and-safety and travel-fraud, feeding protection-and-incidents); three architecture boundaries merged into one paragraph; summary paragraph under the identity-level policy table deleted; authentication/authorization definition dropped from Concepts; Chief Architect's "Decide" list and two review questions merged. *(AI-mediated session)*
- **2026-10-22** — Verified Lisbon tourist tax / Portuguese VAT against official sources. *(AI-mediated session)*
