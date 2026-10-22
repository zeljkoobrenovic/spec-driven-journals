---
status: accepted
revised: 2026-10-22
---

# Spec: Damage, Parties and Emergencies: Protection and Incident Response

## Intent

Answer the chapter question from PLAN: what protections should a stays marketplace offer, and how are incidents handled end to end? The chapter argues that protection is one domain on the reservation's timeline. Reservation screening comes before confirmation, the incident workflow covers the stay, and the claims workflow follows check-out. Two loops sit underneath: money (a protection ledger with platform retention, guest recovery and an insurer's share) and learning (incident and claim outcomes as labels for screening). One versioned protection policy, stamped on each reservation, turns the program's terms into product rules that the listing page, checkout, support, adjudication and screening all read. The reader leaves able to draw the protection architecture, set up screening as a governed decision system, and judge what a group can share between an OTA's homes and a hosted-stays marketplace.

Owns: **damage protection**, **reservation screening**, **incident workflow**.

Productscape domains covered: HSM `trst` (risk scoring and screening; protection and incident workflow), HSM `reso` (claims, in part); TAM `supp` (recovery, in part); the gap "damage deposits, protection programme and claims ledger"; residuality stressors TAM `fire` and HSM `evac` (destination operating state).

## Audience

Chief architects, trust-and-safety engineering leads, payments and ML leads at hosted-stays marketplaces and at OTAs that sell homes. They know risk scoring and case management in general. They need the stays-specific shape: party screening on the booking path, no front desk at midnight, platform-funded damage protection with an insurer behind it, post-stay charges and emergencies at destination scale.

## Success criteria

- [ ] Reader can distinguish guest guarantee, damage protection, liability insurance, security deposit, retention and recovery, and say who carries which loss.
- [ ] Reader can draw the protection components (policy registry, screening, incident workflow, claims workflow, evidence store, ledger accounts, insurer interface) and state each component's "must not".
- [ ] Reader can design a screening action set beyond allow/deny, and explain holdouts, late labels, fairness measurement and GDPR Article 22 safeguards.
- [ ] Reader can triage incidents by severity and name the side effects that must go through other domains' interfaces.
- [ ] The Dubrovnik worked example reconciles: €3,800 claimed, €3,450 paid (sofa repaired rather than replaced, −€350), €900 recovered, €2,550 net within the €10,000 retention.
- [ ] Every Airbnb, Booking.com and Expedia claim carries a dated source; the screening reference design is labeled as inference.
- [ ] Trade-off table and "Hotels and Homes" section say what to share (incident record, evidence store, ledger accounts, insurer interface, declared events) and what not (programs, limits, thresholds, funding).

## Non-goals

- Payment-fraud scoring, account takeover and extranet phishing: [[travel-fraud]].
- Trust platform, enforcement actions and DSA statements of reasons in general: [[stays-trust-and-safety]].
- Identity levels and verification flows: [[identity-accounts-and-access]].
- Oversell detection and the relocation service: [[inventory-integrity]].
- Cancellation policy engine, extenuating circumstances and refund terms in declared events: [[changes-and-cancellations]].
- Case management, contact drivers and surge staffing: [[customer-service]]; deposits and post-stay charge mechanics: [[stay-payments]].
- Short-term-rental law and the market policy registry: [[stays-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Airbnb's screening model, features beyond the 2022 list and its thresholds are not public; the chapter describes only published signals and outcomes.
- Current caps and markets of Booking.com's guest-pays damage program are not public in the sources checked (2022 pilot only).
- The indoor-camera ban rests on a press report, not an Airbnb primary page.
- Whether a screening redirect is a decision that "similarly significantly affects" the guest under GDPR Article 22 is left to counsel and [[stays-regulation]].

## Decision log

- **2026-10-21** — Structured the chapter around the reservation timeline (before, during, after) with money and learning loops, instead of a product-by-product tour, because the Dubrovnik case failed at the seams between tools, not inside any one of them.
- **2026-10-21** — Added a €10,000 per-claim retention to Nookaway Cover (ledger addition) so the chapter can teach where the platform's loss ends and the insurer's begins.
- **2026-10-21** — Verified the Insurance Distribution Directive (CELEX 32016L0097) and GDPR Article 22 directly, because neither brief covered them and both shape the design.
- **2026-10-21** — Used a tabletop exercise, not an invented real-world disaster, for the destination-emergency example.

## Sources

- **Internal**
  - [[stays-trust-and-safety]], [[travel-fraud]], [[identity-accounts-and-access]], [[reviews-and-reputation]], [[stays-regulation]] — Part VII neighbours.
  - [[stay-payments]], [[payouts-and-settlement]], [[inventory-integrity]], [[calendar-sync]], [[changes-and-cancellations]], [[customer-service]], [[trip-and-messaging]], [[stays-ml-platform]] — dependencies.
  - `_research/brief-trust-safety-regulation.md`, `brief-airbnb.md`, `brief-host-partner-guest-service.md`, `brief-booking-reservations.md`, `productscape-digest.md`, `scenario-ledger.md`.
- **External**
  - Airbnb Form 10-K FY2025 (2026), AirCover pages (2026), newsroom posts on screening and parties (2021–2026), Project Lighthouse paper (2020).
  - Booking.com Partner Liability Insurance (2026) and Terms (2025); Expedia Rapid vacation-rentals documentation.
  - Regulation (EU) 2016/679 (GDPR) Article 22; Directive (EU) 2016/97 (insurance distribution).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: American spelling (fulfill), timetoread 33→36; Dubrovnik claim, Cover structure and 21 Sept 2027 forum decisions checked against the ledger. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: trimmed the components caption to the protection ledger the diagram shows. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 7,108 → 6,832 prose words; opening now ties the chapter to Part VII and names its neighbours; screening costs merged from the trade-offs table into the action table; repeated sentences, the subrogation definition and a duplicated Hotels and Homes row cut; headings unchanged. *(AI-mediated session)*
