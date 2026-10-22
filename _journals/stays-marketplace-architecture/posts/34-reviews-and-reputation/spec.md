---
status: accepted
revised: 2026-10-21
---

# Spec: Trustworthy Reviews: Collection, Integrity and Quality Operations

## Intent

Show architects that a review system is part of the trust platform, not a content feature, and that its integrity depends on its links to the reservation record, identity, payments and enforcement. The chapter argues for three things. A **verified review** is a fact about a stay: eligibility comes from the reservation lifecycle and is recorded with the review, including the weak points (self-reported no-shows under the agency model). **Integrity is a tiered pipeline with a time budget**, driven by relational signals (reservation graph, shared cards, payout accounts, devices) more than text; the double-blind window of two-way reviews gives hosted stays that time for free. **Every consumer reads one event log** of published and removed reviews, so removals propagate to scores, ranking features, screening features, quality programs and partner analytics. It owns the verified review, the double-blind review and the quality program, and shows how EU, UK and US consumer law (Omnibus, DSA, DMCC Act, FTC rule) turn "verified" and "reasonable and proportionate steps" into logging and governance requirements.

Productscape domains covered: TAM `reve` (Review Collection and Stay Feedback), TAM `rept` (Reputation and Quality Operations: review intake and validation, quality monitoring, partner remediation), TAM `prop` (review and quality signals); HSM `grev` (Guest Reviews and Re-engagement), HSM `list` (review and trust evidence service).

## Audience

Chief architects, trust and safety engineering leads, product owners for reviews and host or partner quality programs, and data leads at OTAs and hosted-stays marketplaces. They know event-driven systems and ML; they need the stays-specific shape of review eligibility, two-way reviews, review abuse and the legal duties.

## Success criteria

- [ ] Reader can define review, verified review, double-blind review, reputation and quality program, and list the eligibility facts with their owners and reliability on each marketplace type.
- [ ] Reader can cite dated evidence for booking-gated reviews (Mayzlin et al. 2014), simultaneous reveal (Fradkin et al. 2021) and the documented rules of Booking.com and Airbnb (fetched October 2026).
- [ ] Reader can map Omnibus (UCPD Art. 7(6), Annex I 23b–c), DSA Arts. 16, 17 and 20, DMCC Act Sch. 20 para. 13 and 16 CFR Part 465 to system requirements, including suppression.
- [ ] Reader can draw the collect–decide–distribute architecture (Figure 1), the review state machine (Figure 2) and the relational ring detection (Figure 3), and name the review record's field groups.
- [ ] Reader can classify review abuse (self-booking, rings, competitor, incentive and pressure, suppression, irrelevant, generated) and say where the evidence for each lives.
- [ ] Reader can explain aggregation choices (recency weighting, display windows, minimum counts, shrinkage, recompute on removal, generated summaries) and the batch-versus-streaming nature of quality programs.
- [ ] The Corvane case runs from the 22 March 2027 complaint to the ring's numbers, the enforcement table, Review Integrity v1 (18 May 2027) and Roomstead's self-booking and no-show audit.
- [ ] The Hotels and Homes table and judgement say what to share (service, log, integrity pipeline, graph features, disputes, statement generator) and what to keep per brand (direction, scale, windows, programs).

## Non-goals

- The trust policy-to-enforcement machinery, trust decision API and appeals in general: owned by [[stays-trust-and-safety]].
- Account takeover, payment fraud and booking risk scores: owned by [[travel-fraud]].
- Identity levels and verification: owned by [[identity-accounts-and-access]].
- Reservation screening, damage protection and incidents: owned by [[protection-and-incidents]].
- The review fragment on the property page: owned by [[property-page-and-room-selection]]; the invitation trigger in the trip timeline: [[trip-and-messaging]].
- How quality features enter the ranker and paid-program ranking effects: owned by [[stays-ranking]] and [[promotions-and-loyalty]].
- The full regulatory map: owned by [[stays-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Booking.com's and Airbnb's review rules were read from live pages on 21 October 2026; both are undated and change. Recheck before print.
- Booking.com's and Expedia's fake-review detection methods are not public; the chapter states only what they disclose. The Expedia event-sourcing post (2023) may describe a replaced system.
- Whether an automated review hold or removal always requires a DSA Art. 17 statement of reasons to the author is presented as the author's reading, not settled law.
- Zervas, Proserpio and Byers (2020) is cited for its headline finding only; its abstract could not be fetched in this session.
- The Corvane figures (ring size, Roomstead audit counts, review volumes) are chapter-local illustrations; [[stays-trust-and-safety]] and [[protection-and-incidents]] may reuse them.

## Decision log

- **2026-10-21** — Opened with a hosted-stays review-trading ring rather than a hotel fake-review story, because it shows three consumers of reviews (badge, ranking, guest screening) being attacked at once; added the Roomstead self-booking and no-show audit so the OTA side is specific, not symmetric filler.
- **2026-10-21** — Made relational (graph) signals, not text classifiers, the core of integrity, and framed the double-blind window as a moderation budget.
- **2026-10-21** — Recommended one group review service (Vouch) in the shared trust platform with per-brand policies, and an event log as the only source of derived numbers, following the documented Expedia pattern (2023).
- **2026-10-21** — Treated suppression (no-show marks, dispute wins) as a first-class abuse, because UK and US law name it explicitly.

## Sources

- **Internal**
  - `_research/brief-trust-safety-regulation.md` Part 5 — review practice and regulation.
  - `_research/brief-host-partner-guest-service.md` Part 4 — Superhost, Guest Favorites, quality system; partner review tools.
  - `_research/brief-expedia-agoda-tripcom.md` 5.2 — event-sourced reviews.
  - `_research/brief-booking-com.md` 4.2 — How we work.
  - `_research/productscape-digest.md` — `reve`, `rept`, `prop`, `grev`, `list`.
  - [[stays-ranking]], [[property-page-and-room-selection]], [[merchant-and-agency-models]], [[reservation-lifecycle]].
- **External**
  - Booking.com, *How we work*, section F Reviews (fetched 21 October 2026).
  - Airbnb Help Center articles 13, 2673, 1257 and 829 (fetched or live October 2026).
  - Mayzlin, Dover and Chevalier (AER, 2014); Fradkin, Grewal and Holtz (Marketing Science, 2021); Zervas, Proserpio and Byers (Marketing Letters, 2020).
  - Directive (EU) 2019/2161; Regulation (EU) 2022/2065; Regulation (EU) 2019/1150; DMCC Act 2024 Sch. 20; CMA208 (2025); FTC rule, Federal Register 22 August 2024 (effective 21 October 2024).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: timetoread 33→37; ring, Hearth, Vouch and Roomstead audit figures checked; Airbnb 550,000 removed listings verified in the Q3 2025 shareholder letter. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 3 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
