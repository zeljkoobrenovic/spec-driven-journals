---
status: accepted
revised: 2026-10-22
---

# Spec: Trust as a Platform: Trust and Safety for Stays

## Intent

Answer the chapter question from PLAN: how should trust and safety be architected across guests, hosts, properties, listings and messages? The chapter argues for a trust platform that separates detection (rules and models, which may stay with the brand that knows the risk) from the decision record and the enforcement path (which must be shared). Every restriction is a recorded trust decision with reasons, policy version, scope and expiry, and becomes a typed enforcement action that is propagated to every consuming system with receipts and reconciled. The same record renders DSA and P2B statements of reasons, feeds complaints and appeals, and produces transparency reporting. The reader leaves able to draw the platform, specify the decision API and its fallbacks, design enforcement propagation, staff integrity operations and choose what two marketplace brands should share.

Owns: **trust decision**, **enforcement action (stays)**, **integrity operations**.

Productscape domains covered: TAM `trst` (Trust API, Risk Signal Feed, Integrity Operations Layer; fraud and verification only as hand-offs); HSM `trst` (Trust decision API, risk scoring and screening as a detector, incident operations UI as hand-off).

## Audience

Chief architects, trust-and-safety engineering leads, principal engineers and product leaders at OTAs and hosted-stays marketplaces whose trust controls grew tool by tool, or who must merge two brands' trust stacks. They know event-driven systems and ML in general; they need the stays-specific shape: gates in many domains, reservations attached to enforced entities, payouts as restrictions, and EU explainability duties.

## Success criteria

- [x] Reader can name the stays risk catalog, its gates and the chapters that own each threat.
- [x] Reader can define trust policy, risk signal, trust decision, enforcement action and integrity operations, and draw the policy → detection → decision → enforcement → appeal loop.
- [x] Reader can draw the trust platform and state each component's "must not", including the decision API's outcomes and per-gate fallback.
- [x] Reader can explain enforcement propagation with receipts and reconciliation, and why reservations and payouts are part of enforcement.
- [x] Reader can list the DSA (Art. 17, 18, 20–24) and P2B (Art. 4) duties that shape the decision record, with verified citations.
- [x] The Corvane Turia Homes case and Warden replay are internally consistent (€48,540 total; €31,640 avoidable; €10,600 paid before suspicion; €6,300 rehousing).
- [x] Trade-off tables, the "Hotels and Homes" table and judgement, failure modes, Chief Architect's view and questions are present.
- [x] Reader will not leave thinking cross-brand enforcement should copy suspensions automatically.

## Non-goals

- Fraud typology, booking risk score, extranet takeover and the November 2027 phishing wave: [[travel-fraud]].
- Identity levels, verification vendors, authentication and partner roles: [[identity-accounts-and-access]].
- Review collection, moderation and fake-review detection: [[reviews-and-reputation]].
- Reservation screening design, damage protection, claims and emergency incident handling: [[protection-and-incidents]].
- STR registration, market policy registry and authority-order intake: [[stays-regulation]].
- Payout hold mechanics in the ledger: [[payouts-and-settlement]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No primary source describes Booking.com's guest-side trust architecture or any company's enforcement propagation; the chapter labels its propagation design as inference.
- Airbnb's DSA designation status after April 2023 was not checked; the chapter avoids stating it.
- How a European platform can lawfully measure discrimination in its own decisions is left to the regulation and privacy chapters.

## Decision log

- **2026-10-21** — Built a new illustrative case (Turia Homes, July 2027) rather than reusing the extranet phishing wave, because the wave belongs to [[travel-fraud]] and the chapter's point is cross-system and cross-brand enforcement, not detection.
- **2026-10-21** — Kept detectors per brand and shared only decisions, enforcement, graph, cases and statements, consistent with One Stay's "ranking models not shared" stance and the reference model's split of TAM and HSM `trst`.
- **2026-10-21** — Verified DSA Articles 17, 18, 20, 22, 23, 24(5) and P2B Article 4 against the official texts (CELEX 32022R2065, 32019R1150), because the brief summarized only DSA traceability and VLOP duties.
- **2026-10-21** — Included the replay's false-positive finding (1,140 → 310 linked reviews) to make the cross-brand trade-off concrete rather than one-sided.

## Sources

- **Internal**
  - [[travel-fraud]], [[identity-accounts-and-access]], [[reviews-and-reputation]], [[protection-and-incidents]], [[stays-regulation]] — Part VII neighbours.
  - [[content-and-media]], [[partner-onboarding]], [[stays-ranking]], [[payouts-and-settlement]], [[inventory-integrity]], [[extranets-and-host-tools]] — signals, gates and receipts this chapter builds on.
  - `_research/brief-trust-safety-regulation.md`, `brief-airbnb.md`, `brief-booking-com.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Regulation (EU) 2022/2065 (DSA) and Regulation (EU) 2019/1150 (P2B) — statements of reasons, complaints, trusted flaggers, misuse, transparency database, termination notice.
  - Airbnb 10-K for fiscal 2025 (2026), identity-graph engineering post (2026), newsroom posts on verification, anti-party screening and discrimination (2020–2026).
  - Secureworks (2023) and KrebsOnSecurity (2024) on Booking.com partner-account campaigns; Booking.com DSA page (2026).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: American spelling (neighborhood, behavior, honor), timetoread 34→36; Turia figures, Warden dates and external claims (identity graph scale, July 4 redirects, DSA recipients) checked. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,241 → 5,981 prose words; opening now ties the chapter to Part VI and the rest of Part VII; component count corrected to eight; two Failure modes that restated earlier sections merged or cut; Chief Architect's "What to watch" no longer repeats the metrics table. *(AI-mediated session)*
