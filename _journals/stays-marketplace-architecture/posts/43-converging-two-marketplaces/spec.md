---
status: accepted
revised: 2026-10-22
---

# Spec: One Platform or Two? Converging Hotels and Homes

## Intent

Answer the book's central group-level question: should a group that runs an accommodation marketplace (OTA-style) and a hosted-stays marketplace share one platform, and what exactly should it share? The chapter's answer is a **shared core** of engines and contracts for what follows the guest, the money and the law; one supply engine per **supply segment**, chosen by segment rather than by brand; and a **convergence register** that records a grade, owner, reason and review date for every capability. After reading, an architect can place any capability with four tests, route cross-type supply (a hotel sold by a homes brand, a one-unit home sold by an OTA), order the shared work, and tell deliberate convergence from scope creep.

The chapter is also the book's reconciliation point. It gathers the "what to share" judgements of the Parts II–VIII chapters into Corvane's December 2027 One Stay register (map v2: 23 shared engines, 6 shared contracts, 20 brand-specific over 49 capabilities) and explicitly resolves the open cross-chapter conflicts, including the experimentation standard that brought the map's 2028 review forward: content-and-media's five shared content services, the place registry vs Waypoint, the capability map's 16/6/26 split versus later forum decisions, and Clause versus Context Map v1.

Productscape domains covered: the overlap matrix (digest §4) and residuality synthesis (§10.3) of both models as a whole; no single brick. The chapter adds no new brick.

## Audience

Group chief architects, CTOs and engineering leaders of travel groups that own both marketplace types or are acquiring one, plus finance and product leaders who sponsor platform programs. They know platform consolidation in general; they need a defensible line between shared and separate for stays, documented precedent, and governance that survives eight months of incremental decisions.

## Success criteria

- [x] Defines convergence decision, shared core, supply segment, cross-type supply, storefront, supply engine and cross-listing, and reuses the shared engine / shared contract / brand-specific grades of [[stays-capability-map]].
- [x] Cites the documented record with dates: Expedia's front-end consolidation (2022–2023), shared platform list and One Key (FY2025 10-K), Vrbo's slower recovery (Q1 2024), Rapid's distinct Vrbo product; Booking.com's homes on one platform with Request to Book and payouts by supply type; Airbnb's hotel push (Q2 2026) and product-agnostic payments, messaging and support (2026 post). Inference about Vrbo is labeled.
- [x] Gives a placement rule (four tests, diagram), a shareable/not-shareable table, and a cross-type routing rule with a sequence diagram.
- [x] Works the Corvane One Stay register with every 2027 forum decision from earlier chapters placed in a map cell, the grade changes, and the four conflicts resolved; budget allocation of the €145 million; sequence 2027–2030.
- [x] Trade-off tables for platform options and sequencing; a "Hotels and Homes" section on supply that crosses over; failure modes; Chief Architect's view with entry and exit criteria for the shared core.
- [x] Four diagrams (illustrated) with captions; nine questions to ask; under 8,500 words.

## Non-goals

- Drawing the capability map and the overlap matrix — [[stays-capability-map]].
- Context boundaries, aggregates and the contracts stewardship group in depth — [[stays-bounded-contexts]].
- Team design and governance bodies for One Stay — [[organizing-stays-engineering]].
- Migration mechanics (strangler, CDC, parallel run, Keystone retirement) — [[modernizing-a-live-marketplace]].
- Fitness functions over the register's metrics — [[evolving-the-platform]].
- The full Expedia/Vrbo case — [[case-expedia-vrbo]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now.

## Open questions

- Why Vrbo's re-platforming hurt is not documented; the chapter offers a labeled inference only.
- Whether Expedia merged Vrbo's back-end inventory or pricing is not public; the chapter claims only the front end and the listed shared infrastructure.
- [[stays-search-architecture]] dates Waypoint's approval to May 2027 in one table row; the ledger and [[destinations-and-maps]] say June 2027. This chapter uses June.
- Guest overlap between Roomstead and Nookaway is known only as shared verified e-mails (about 2.4 million); booking overlap waits for Corvane ID linking in 2028.

## Decision log

- **2026-10-21** — Framed the Corvane worked example as the December 2027 annual review of the capability map, so the chapter can reconcile the many forum decisions in earlier chapters rather than restate the April board decision.
- **2026-10-21** — Resolved the content-sharing conflict by adopting all five services but adding only one cell (mapping engine): media pipeline and translation were already shared engines, the perceptual-hash index belongs to the media pipeline, and policy rendering comes from Clause and the display policy service.
- **2026-10-21** — Kept the place registry and Waypoint as two components with one dependency direction (Waypoint enriches registry records), and fixed the vocabulary rather than renaming the registry.
- **2026-10-21** — Routed Nookaway's 2028 boutique-hotel pilot to the hotel-type engine (segment chooses engine, brand chooses storefront), consistent with availability-engine, inventory-integrity, dynamic-pricing, property-page and merchant-and-agency chapters.

## Sources

- **Internal**
  - [[two-stay-marketplaces]], [[stays-marketplace-economics]], [[stays-capability-map]], [[stays-bounded-contexts]] — the One Stay split, map v1 and Context Map v1.
  - Parts II–VIII "Hotels and Homes" and "Chief Architect's view" sections, especially [[content-and-media]], [[property-and-listing-model]], [[destinations-and-maps]], [[rates-and-availability-model]], [[changes-and-cancellations]], [[stays-trust-and-safety]], [[reviews-and-reputation]], [[trip-and-messaging]].
  - `_research/brief-expedia-agoda-tripcom.md` Parts 1.3, 3.6, 9; `brief-booking-com.md` Parts 1.2, 3.6; `brief-airbnb.md` Parts 1.7, 2.3; `productscape-digest.md` §4, §10.3; `consistency-issues.md` items 1 and 5.
- **External**
  - Expedia Group Form 10-K FY2022, FY2023, FY2025; Q1 2024 earnings release; Rapid Vrbo integration guide (n.d.).
  - Booking Holdings Form 10-K FY2025; Booking.com Request to Book and payouts documentation (n.d.).
  - Airbnb Q2 2026 shareholder letter; Airbnb Tech Blog, "Scaling beyond one" (2026).
  - Conway, "How Do Committees Invent?" (1968).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: 14 Dec 2027 review set with the board (as in ch. 47); Watchpost (not in ledger) replaced by booking risk score models on Warden; Gauge and Plumbline named in the register. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: regenerated the "names, not scope" figure with set-aside cards labeled Content services and Waypoint. *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 5,221 → 5,149 prose words; deleted the public-record summary table (restated the three paragraphs above it); the four placement tests now stated in the text; lead says where the chapter sits in Part IX; repetitive failure modes compressed to pointers; "Decide what the board's words mean" merged into "Own the register". *(AI-mediated session)*

- **2026-10-22** — Recaptioned Figure 2 to follow the decision tree's order, including the policy-as-data split (author decision). *(AI-mediated session)*
