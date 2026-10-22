---
status: accepted
revised: 2026-10-22
---

# Spec: When Something Goes Wrong: Customer Service and Recovery

## Intent

Answer the chapter's question: how do you build support for a stays marketplace where most problems involve three parties (guest, property or host, marketplace) and a deadline set by the stay? The chapter argues that the marketplace should own three things and buy the rest: the **case** (bound to reservations, parties, a contact driver and an arrival clock, opened by domain events as well as by contacts), the **context read model** agents and AI agents see, and the **recovery decision** (a versioned, limited, ledger-posted remedy with a funder and a liable party). Channels, telephony and the agent desktop can be bought. After reading, an architect can design the case model and its states, set service levels from the arrival clock, specify recovery decisioning, set rules for AI support agents grounded in live reservation state, and plan a disruption mode.

Productscape domains covered: TAM `supp` (Customer Support & Recovery: Case and Workflow Orchestration, Recovery Decisioning, Escalation and SLA Controls, Recovery Event Feed); HSM `reso` (Resolutions & Support: case API, case orchestration, resolution center). The chapter also fills two model gaps: neither model records recovery outcomes as money facts with liability, and neither names a shared contact-driver taxonomy as a data product.

## Audience

Chief architects, principal engineers and customer-service, operations and payments leaders at OTAs and hosted-stays marketplaces. They know event-driven systems and ticketing tools; they need the stays-specific failure path, the money consequences of support decisions and a defensible position on AI agents and outsourcing.

## Success criteria

- [x] Defines contact, contact driver, case, arrival clock, service level, recovery decision, deflection and resolution, and keeps contact vs case and ticket outcome vs recovery decision distinct.
- [x] Works the King's Day relocations with ledger numbers (47 minutes, 9 rooms, 4 Roomstead guests, €2,150, €1,600 recovered at €400 per reservation) and a replay on the target design.
- [x] Gives a Corvane contact-driver distribution and volume/cost table, a component table, a case model and state diagram, an arrival-clock service-level matrix, a recovery cause/funder/liability table and a metrics table.
- [x] Covers documented 2024–2026 AI customer-service deployments with dated sources (Airbnb Q2/Q3 2025 and Q2 2026 letters, Airbnb voice support 2025, Airbnb evaluation 2026, Expedia 2026 via secondary report, Booking.com AgentHub 2026) and labels the Romie report as low confidence; states design rules as reference design, not company internals; cites AI Act Article 50.
- [x] Handles disruption surges with the ATC strike weekend (6,200 requests in 48 hours) and turns it into requirements (disruption mode, declared events, structured waivers, surge capacity).
- [x] Trade-off table, "Hotels and Homes" table with a sharing judgement, failure modes, Chief Architect's view, 10 questions, sources.
- [x] Three diagrams (illustrated) with captions; under 8,500 words.

## Non-goals

- The reservation state machine, delivery and acknowledgement — [[reservation-lifecycle]].
- Cancellation policy models, the policy engine and declared-event definitions — [[changes-and-cancellations]].
- Conversation store, translation and notification routing — [[trip-and-messaging]].
- Oversell prevention, detection and the liability matrix — [[inventory-integrity]].
- Damage claims, evidence and safety incident response — [[protection-and-incidents]].
- Refund accounting, chargebacks and reconciliation — [[refunds-and-reconciliation]].
- The extranet phishing wave and fraud controls — [[travel-fraud]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- No company has published the architecture of its case management or AI support agent beyond outcomes; the design rules remain reference-design judgement. Revisit if a primary post appears.
- The Expedia figures (250 million interactions, over half self-service, over 30% AI) rest on a secondary report of an earnings call; Romie's discontinuation rests on a low-confidence secondary source.
- The AI Act's application dates may be amended (EU simplification proposals); the chapter cites the regulation as adopted and flags the dates for checking.
- Corvane's contact-driver shares and support costs are illustrative; no public industry benchmark for contacts per stayed reservation was found.

## Decision log

- **2026-10-21** — Made the case (not the contact or ticket) the unit of the chapter, and the arrival clock (not the queue service level) the source of urgency, because three-party stays problems are decided by the stay's deadline.
- **2026-10-21** — Introduced the recovery decision as a ledger-posted record with funder and liable party, reusing the liability matrix of [[inventory-integrity]] rather than redefining it; King's Day is replayed on this design.
- **2026-10-21** — Positioned AI agents as one more client of the case, context and decision APIs with actor limits, gated per driver, rather than as a separate channel; Nookaway gets no assistant in 2027 because its expensive drivers are disputes.
- **2026-10-21** — Used the ATC strike weekend for surge handling (ledger example) and left the policy side of declared events to [[changes-and-cancellations]].

## Sources

- **Internal**
  - [[inventory-integrity]] — King's Day reconstruction, liability matrix, oversell baseline.
  - [[calendar-sync]] — conflict cases with a 60-minute guest-contact target.
  - [[extranets-and-host-tools]] — partner exception queues read by support.
  - [[payouts-and-settlement]] — Prinsenkade's April statement with the €1,600 recovery.
  - [[stays-ranking]] — reliability demotion reading support cases.
  - `_research/brief-host-partner-guest-service.md` Part 8; `brief-platform-data-ml.md` Part 8; `brief-booking-reservations.md` Parts 6.4, 7.3, 8; `productscape-digest.md` (`supp`, `reso`).
- **External**
  - Airbnb Form 10-K FY2020 and FY2025; Q2 2025, Q3 2025 and Q2 2026 shareholder letters.
  - Airbnb Tech, voice support (2025); Airbnb Engineering, eval-driven development (2026).
  - Booking Holdings Form 10-K FY2020 and FY2025; Booking.com AgentHub (2026).
  - Hotel Dive (2026) on Expedia's service interactions; Let's Data Science (2026) on Romie.
  - Regulation (EU) 2024/1689, Article 50.

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: ATC strike deadline rendering aligned with changes-and-cancellations (confirmation e-mail, Irish time); €400-cap wording clarified; timetoread corrected. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: regenerated the King's Day replay so "entitlement" ends inside the Recovery lane. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,801 → 5,558 prose words; no headings renamed; Failure Modes cut from eight to three entries plus one line naming the five covered earlier; duplicate Expedia and Airbnb voice figures removed from the AI table; opening now names what depends on the chapter. *(AI-mediated session)*

- **2026-10-22** — Softened the unsourced claim that support is one of the largest costs after marketing (author decision). *(AI-mediated session)*
