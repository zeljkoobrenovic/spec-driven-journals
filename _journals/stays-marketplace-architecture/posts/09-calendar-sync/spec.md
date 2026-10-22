---
status: accepted
revised: 2026-10-22
---

# Spec: One Home, Many Calendars: iCal, APIs and Multichannel Hosts

## Intent

Show architects why a home sold on several platforms gets double-booked, and what a hosted-stays marketplace can and cannot do about it. The chapter defines the **conflict window** as a two-directional quantity, of which the marketplace controls only one half (its own import interval and processing). It argues that conflict risk scales with the window times the product of demand on the two channels, so conflicts cluster on peak nights. It recommends modeling a calendar as a set of **claims with provenance** rather than per-night booleans, so that imports withdraw only their own claims, failed fetches release nothing, conflicts are detected on import, and hosts can migrate from iCal to API connections cleanly. Its design combines adaptive polling, a pre-booking re-check for instant book, conflict detection with a recovery flow, feed-health states with listing-level protection, and a migration path to PMS and channel-manager APIs. It also holds that iCal is a supported fallback, not a strategy. The chapter owns iCal sync, conflict window and multichannel host.

Productscape domains covered: TAM `cald` (partially: calendar controls for homes on the OTA side); HSM `cala` (calendar and availability), `apix` (partner APIs and channel connectivity). **[ADDED]** channel management for hosts (external calendars and channel managers), which the digest identifies as a gap in HSM ("nothing in the model talks to an external calendar or channel manager").

## Audience

Chief architects, principal engineers and engineering leads of hosted-stays marketplaces, vacation-rental PMS and channel-manager vendors, and OTA teams that sell homes. They know HTTP, polling, webhooks and transactional databases. They need the hosted-stays specifics: what iCal carries, who owns which half of the window, why conflicts concentrate on peak dates, and which controls are worth building.

## Success criteria

- [ ] Reader can classify a host set-up (single-channel, iCal mesh, hub, mixed) by where the system of record lives, and explain the n × (n − 1) link count of the mesh.
- [ ] Reader can state what RFC 5545 gives an importer (all-day dates, exclusive `DTEND`, `UID`, required `DTSTAMP`) and what it does not (prices, restrictions, guest data, polling, acknowledgement).
- [ ] Reader can define the conflict window in both directions, say which terms the marketplace controls, and use the demand-product model to explain why conflicts cluster on peak nights.
- [ ] Reader can sketch the claims model and the components around it (scheduler, fetcher, parser, differ, claims store, exporter, conflict detector, health monitor) with their contracts, including the request-forgery and capability-URL rules (Figures 2 and 3).
- [ ] Reader can explain, with the Seville replay (Figure 4), why faster import improves detection but not prevention for outbound conflicts.
- [ ] Reader can compare connection options and polling strategies in trade-off tables, and justify fail-open at booking with protection at listing level.
- [ ] Reader can name the main failure modes (failed fetch read as empty, off-by-one, echo loops and ghost blocks, link rot, two writers, automatic reopening).
- [ ] The Hotels and Homes section compares the two marketplaces specifically and recommends sharing measurement and operations, not protocols.

## Non-goals

- Hotel connectivity, OpenTravel messages, channel managers for hotels and certification: owned by [[connectivity-and-channel-managers]].
- The nightly calendar data model and pricing fields: owned by [[rates-and-availability-model]].
- Concurrency control inside one platform, holds, overbooking and relocation: owned by [[inventory-integrity]].
- The availability read path for search: owned by [[availability-engine]].
- Host tools, co-hosts and booking-request operations: owned by [[extranets-and-host-tools]].
- Host cancellation penalties and policy: owned by [[changes-and-cancellations]]; guest guarantee and protection: [[protection-and-incidents]].
- Night caps and registration law: owned by [[stays-regulation]].

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Airbnb's iCal import interval has changed before (a snippet showed 2 hours; the live page says 3 hours as of October 2026). Recheck before print.
- Vrbo's iCal import interval comes only from third-party PMS vendors (2024). Vrbo's own documentation was not found.
- The "iCal or API but not both" rule for Airbnb listings is a 2024 vendor report; not verified against Airbnb's current terms.
- No platform documents conflict detection on import, adaptive polling or echo suppression. The chapter presents them as recommendation and labels the cross-platform pattern as inference.
- The echo-loop mechanism depends on whether a producer re-exports imported blocks; no producer documents this explicitly.

## Decision log

- **2026-10-21** — Built the chapter around the conflict window as a measurable, two-directional quantity, rather than around protocols. Without it, "poll faster" looks like the answer, and the Seville case shows that it is not.
- **2026-10-21** — Used a simple demand-product model (my judgement, labeled) to justify adaptive polling and to explain why conflicts cluster on peak dates.
- **2026-10-21** — Recommended a claims-with-provenance model behind Almanac's existing read interface, so the change is a migration that does not touch search.
- **2026-10-21** — Kept the Seville case faithful to the ledger and replayed it under the new design to show detection (75 minutes earlier) rather than prevention. Reused the 2026 conflict baseline from [[inventory-integrity]] (about 3,100, 78% iCal-only) and appended the direction split, the fetch volumes, Calendar Sync v2 and a Roomstead iCal fact to the ledger.

## Sources

- **Internal**
  - `_research/brief-supply-connectivity.md` Parts 3–5 and 7 — iCal standard and platform behavior, VR PMS APIs, certification.
  - `_research/brief-airbnb.md` 1.6 and Part 4 — API-connected hosts, iCal sync, undocumented calendar internals.
  - `_research/brief-expedia-agoda-tripcom.md` 2.3 and the Hostaway API — iCal and API channels side by side; Vrbo gaps.
  - `_research/brief-booking-reservations.md` 3.3, 5.1, Part 9 — Vrbo integrated accounts, iCal lag, end-to-end window.
  - `_research/brief-availability-pricing.md` 5.2, 10.2–10.3 — iCal pull, auto-replenishment, one-unit zero tolerance.
  - `_research/productscape-digest.md` — `cala`, `apix`, `cald`; the external-calendar gap.
  - [[connectivity-and-channel-managers]], [[property-and-listing-model]], [[inventory-integrity]], [[extranets-and-host-tools]], [[converging-two-marketplaces]].
- **External**
  - RFC 5545 (IETF, 2009).
  - Airbnb Help Center articles 99, 2348 and 2965 (live October 2026); Airbnb Newsroom (2024).
  - Vrbo connectivity program and integrated-accounts help (live 2026); Booking.com overbooking troubleshooting (live 2026).
  - Hostaway API (2026), Hostfully (2026), Hospitable (2026), Beds24 wiki (2024), Cloudbeds myallocator (2019).

## Changelog

- **2026-10-21** — Initial spec and article. *(AI-mediated session)*
- **2026-10-21** — Editorial review pass: acronyms expanded on first use (OTA, PMS, CRS, ARI), American spelling, hedged two unverified/old claims, added a hand-off section to extranets-and-host-tools, timetoread 35 min. *(AI-mediated session)*
- **2026-10-21** — Visual layer: converted 4 mermaid diagrams to illustrations and added 2 conceptual figures (article-illustrator). *(AI-mediated session)*
- **2026-10-21** — Figure fixes: aligned the Seville replay alt text with the image (alert to Carmen only). *(AI-mediated session)*
- **2026-10-22** — Sharpening pass: 6,604 → 6,587 prose words; opening now ties the chapter to Part II's "copy of someone else's truth" rule; two paragraphs merged; filler and announcing sentences cut; no headings changed, no facts removed. *(AI-mediated session)*
- **2026-10-22** — Second sharpening pass: 6,604 → 6,166 prose words since HEAD (−6.6%); Failure Modes compressed to one-line pointers to the sections that handle each failure (unique facts kept); Seville re-tellings in the claims and replay sections, the double-booking/overbooking contrast, the Feria-week guarantee point and the request-to-book protection repeated across three sections cut back; Chief Architect's view tightened; no headings, figures or facts removed. *(AI-mediated session)*
