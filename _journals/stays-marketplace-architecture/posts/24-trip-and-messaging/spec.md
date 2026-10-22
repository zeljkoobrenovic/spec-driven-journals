---
status: accepted
revised: 2026-10-22
---

# Spec: Between Booking and Check-Out: Trips, Messaging and Notifications

## Intent

Show that the part of a stay between confirmation and the review invitation is carried by three platform services that own almost none of the facts they present: the trip timeline (a read model over reservation, payment, message, access and notification events), guest–host and guest–property messaging (a governed three-party conversation store), and notification routing (one platform that turns domain events into delivered, seen messages). The chapter argues three things: trip status must be derived from facts with provenance, not from reservation state; messaging policy must be stage-aware and evaluated in one place for every client; and arrival-critical information is a deliverable with readiness, deadlines, fallback and human escalation. After reading, an architect can design or review a trip, messaging and notification platform for either marketplace type and decide what a two-marketplace group should share (the channel) and keep per brand (policy packs and arrival templates).

Productscape domains covered: TAM `trip` (Trip Management & Messaging: trip timeline, message and notification routing, trip status explanation), `msgc` (Guest-Property Messaging), `reve` (review invitation trigger only); HSM `trip` (Trip Messaging & Itinerary), `grev` (re-engagement and review triggers only). Also the digest's gap "notifications platform" and "check-in and property access".

## Audience

Chief and principal architects, guest-experience and messaging platform leads, trust-and-safety engineering leads and product directors at OTAs, hosted-stays marketplaces and groups that run both. They know distributed systems and event-driven design; they need the stays-specific obligations and failure modes.

## Success criteria

- [x] Defines and owns trip timeline, guest–host messaging and notification routing; defines trip status explanation, arrival package, access credential, structured request and disintermediation.
- [x] Opens with a concrete Corvane incident (the check-in instructions that never arrived: the 7 August 2027 redaction of door codes) whose root causes the chapter's architecture removes, and replays it on the new design.
- [x] Presents the trip timeline as an event-built read model with a status-from-facts rule, and the arrival package as a state machine with deadlines and escalation.
- [x] Grounds messaging in documented public evidence (Booking.com Messaging API windows, structured requests, single-channel-of-reply, redaction; Airbnb message volume, translation, messaging features, Superhost response rate) and labels the conversation model as inference.
- [x] Gives a stage-by-stage messaging policy table and safety controls tied to the documented 2023–2024 partner-account phishing chain.
- [x] Describes the notification pipeline (intent, policy, channel plan, adapters, delivery tracking), event classes with separate lanes, mailbox-provider and WhatsApp channel constraints with dated sources.
- [x] Includes a trade-off table, the "Hotels and Homes" comparison with a sharing judgement, failure modes, the Chief Architect's view, design-review questions and four diagrams (illustrated).
- [x] Corvane numbers agree with the ledger; new canonical facts are appended to the ledger.

## Non-goals

- The reservation state machine, delivery to properties and completion ([[reservation-lifecycle]]).
- Change and cancellation policy, disruption declarations and refunds ([[changes-and-cancellations]], [[refunds-and-reconciliation]]).
- Support case management and recovery decisions ([[customer-service]]).
- Extranet account takeover and fraud scoring ([[travel-fraud]]); trust decisions and enforcement ([[stays-trust-and-safety]]).
- Review collection, publication and moderation ([[reviews-and-reputation]]); supply-side event classes, access-code lifecycle and turnover ([[extranets-and-host-tools]]).
- Price alerts and wishlists as products ([[personalization-and-recommendations]]); AI assistants in depth ([[ai-in-travel-stays]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- No primary engineering source describes Airbnb's, Booking.com's or Expedia's messaging or trip back ends; revisit if one is published.
- Whether private guest–host messages fall under any DSA notice-and-action duty was not analyzed; the chapter avoids the claim.
- Retention periods for messages are given as a design principle, not as market-specific legal periods.

## Decision log

- **2026-10-21** — Built the Corvane story around a safety rule applied at the wrong trip stage, so that messaging safety, check-in delivery and trip status all fail in one incident rather than in three separate examples.
- **2026-10-21** — Named the group platforms Courier (notifications) and Threadline (conversations) and placed the arrival package and trip timeline with Nookaway, built on the shared reservation contract, to stay consistent with One Stay's shared list and the extranets chapter's "shared spine".
- **2026-10-21** — Kept access-code lifecycle and supply-side notification classes in [[extranets-and-host-tools]] and referenced them, rather than re-teaching them.
- **2026-10-21** — Used the ATC strike weekend for the notification-lane failure (disruption e-mails behind a campaign) to tie the chapter to Built for Sunny Days.

## Sources

- Internal: [[reservation-lifecycle]], [[extranets-and-host-tools]], [[destinations-and-maps]], [[personalization-and-recommendations]], [[stay-payments]], [[travel-fraud]], [[customer-service]], [[reviews-and-reputation]], [[event-driven-stays]].
- Booking.com Connectivity Messaging API, Use cases and best practices, Pre-reservation messaging (live documentation, October 2026).
- Airbnb: 2021 and 2023 Winter Releases; 2022 translation release; 2024 smart-lock release; messaging upgrades page; help articles 4163 and 829; Form 10-K FY2025.
- Booking.com AgentHub (booking.ai, 2026); Expedia EXPLORE 2024; Agoda Partner Portal (2026).
- Secureworks/Sophos (2023); KrebsOnSecurity (2024).
- Google email sender guidelines (from February 2024); WhatsApp Business Platform pricing (October 2026); GDPR Article 5.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: trimmed from 9,046 to 8,482 words; payout sentence corrected to stay events; PMS acronym placement, American spelling and buzzword fixed. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: regenerated the check-in replay so "seen 18:40" runs from Courier to the arrival package. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,541 → 6,159 prose words; headings unchanged; 4 paragraphs deleted as needless (one folded into the replay table); restatements of the opening scene, secret-handling and SLO metrics removed; design-review questions merged from 10 to 8. *(AI-mediated session)*
