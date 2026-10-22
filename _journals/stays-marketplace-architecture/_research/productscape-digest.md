# Productscape Digest: Travel Accommodations and Hosted Stays Marketplace Domain Models

Research input for *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. Prepared 21 October 2026 from two Productscape domain models. This is a working document for chapter writers, not a publishable text.

## 1. How to read this digest

### 1.1 Provenance

Everything here comes from two Productscape domain-model folders in the sibling `productscape-workspace` repository:

| Short name | Path (under `productscape-examples/_config/product-domains/marketplaces/`) | Model ID / portfolio name |
| --- | --- | --- |
| **TAM** (travel accommodations, OTA-style) | `travel-accommodations-marketplace/` | `travel-accommodations-marketplace`; portfolio "Travel Accommodations Marketplace Platform" v1.0 |
| **HSM** (hosted stays, peer-to-peer / short-term rental) | `hosted-stays-marketplace/` | `hosted-stays-marketplace`; portfolio "Hosted Stays Marketplace Platform" v1.0 |

Files read in both models: `_domain/DOMAIN.md`, `start/config.json`, `customers/customers.json`, `customers/insights.json`, `customers/relations.json`, `customers/links.json`, `business/competition.json`, `product-bricks/product-bricks.json`, `product-bricks/product-stream.json`, `product-deployments/products.json`, `product-deployments/deployment.json`, `data/data-assets.json`, `residuality/residuality.json`. Neither model has a `REVIEW.md`. The brick, customer, data and deployment files were processed with Python scripts; **every brick and every module name was extracted** (the inventory in §3 is complete, not sampled). Images were ignored.

### 1.2 What these models are, and are not

- **Generic domain models written with named operators as inspiration.** TAM's `DOMAIN.md` says it "models the core accommodations marketplace in which Booking.com most clearly operates today" and that it is "intentionally generic rather than Booking.com-branded, but … grounded in Booking.com operating reality". HSM's `DOMAIN.md` says it "models Airbnb's clearest core business". Both cite public investor, help-centre and developer pages as research input (reviewed 2026-03-31).
- **They are not descriptions of Booking.com, Airbnb or any real company.** The book must never present model content — capabilities, brick names, team or product boundaries, KPIs, strategy horizons, data stores, deployment topologies, residuality stressors — as facts about Booking.com, Expedia, Airbnb, Vrbo, Trip.com or anyone else. Use them as a *worked reference model* of a fictional or generic operator.
- **HSM leaks its inspiration into the model text, and the book must scrub it.** The HSM brick `trst` is literally named "Trust, Safety & AirCover"; its module says "Supports AirCover, damage, and safety intervention paths"; persona visions read "Make Airbnb the default place to discover and book distinctive stays…", "Make Airbnb a portfolio-grade operating system…"; a KPI is "Superhost progression". TAM is cleaner, with one leak: a job step says "Supports pay-at-property, pay-in-advance, or Booking-managed payment patterns". **Never reproduce these names as if they described the reference model.** Use neutral terms: "host and guest protection programme", "top-host status", "platform-managed payment".
- **KPI values are illustrative and often nonsensical.** No KPI node carries a `valueStatus`; every dashboard link points to `dashboard.example.com`. Values include "Promotion ROI confidence: 486 (score)", "Net revenue per available room-night: EUR 49M", "Manual touch count per change: 26,129", and HSM "Guest booking conversion: 96.5% of high-intent sessions" next to a year-1 target of "4.7%". **Do not quote any KPI value.** KPI *names and tree shapes* are usable.
- **HSM horizon targets are embedded in north-star text** ("Median time to first booking to 21 days", "Calendar accuracy to 98%", "Co-host adoption to 37%"). They are model hypotheses, not industry benchmarks.
- **Competitor statistics and `DOMAIN.md` figures are the only externally sourced numbers.** The models say competitor stats come from official investor or company pages, with period and scope. They were not re-verified for this digest. Treat them as "as recorded in the model" and re-check against the primary source before citing (see §9).

### 1.3 Maturity of the two models (important for how much to trust each part)

Both models are version 1.0 and noticeably thinner than the LISTED sibling models (GLM had 88 bricks, 12 streams and a curated data catalog). TAM is the richer of the two.

| Aspect | TAM | HSM |
| --- | --- | --- |
| Domain brief | `DOMAIN.md`: research summary, five "value pools", modeling choices | `DOMAIN.md`: research summary with figures, five-point hypothesis |
| Review | None | None |
| Bricks | **34** in 3 root groups, 6 sub-groups; 154 modules (3–6 per brick) | **21** in 3 root groups, 6 sub-groups; 77 modules (2–4 per brick) |
| Brick status | 4 `invest`, 30 `sustaining` | 8 `invest`, 13 `sustaining` |
| Brick dependencies | 56 hand-written edges with specific types (`availability`, `partner-sync`, `refund`, `escalation`…); 7 bricks have no outgoing edge | 23 edges; 5 bricks have no outgoing edge; several important edges missing (§3.5) |
| External systems | 12 named categories (PMS, channel managers, PSPs, mapping, identity providers, CDN) | 3 (identity-verification providers, payment processors, professional operator tooling) |
| JTBD → stream traceability | Job steps put **brick IDs** in `streamsNeeded` (with good per-step `howItSupports` text) | Same defect: brick IDs in `streamsNeeded`, no `howItSupports` depth |
| Streams | 5 streams; only the first carries key facts and pain points; others have bare steps | 5 streams; no key facts or pain points at all |
| Bricks not in any stream | `geoa`, `idam` | `grev` |
| Data assets | 17, all store technology `generated-starter`; **no hand-written core entity** (no property, room, rate plan, reservation, review) | 17, same generator; same absence |
| Residuality | 4 stressors, detailed and excellent | 4 stressors, detailed and excellent (one is only a `candidate`) |
| Product strategy `categoryGate` | Absent | Absent |
| Journey stories | One per persona; Trigger/Trial/Engagement/Retention concrete; Discovery and Evaluation templated | Same pattern |

**Practical rule for writers:** use TAM for supply-side and distribution substance (room and rate selection, inventory backbone, connectivity, partner extranet, settlement ledger, managed travel), HSM for the peer-to-peer hosting substance (host activation, co-hosts, turnover operations, protection programme, local compliance), and **both residuality files as the strongest architectural material**. Treat the data catalogs, KPI values and deployment replicas as structural placeholders.

### 1.4 Structural findings worth knowing up front

1. **Unlike LISTED's two models, these two do not share a capability skeleton.** GLM and REM had identical 88 brick IDs. TAM and HSM were authored separately, at different granularity (34 vs 21 bricks), with only five shared IDs (`srch`, `book`, `trip`, `trst`, `paym`). Mapping them is a *conceptual* exercise (§4), and that mapping is itself a book point: **the two marketplace types share a guest/traveler spine and a payments-and-trust foundation, but their supply sides are structurally different.**
2. **Both models are organized the same way at the top:** a demand-side experience group, a supply-side group, and a shared "Marketplace Foundations" group.
3. **TAM models hotels *and* homes on one supply backbone** (its supply persona set includes an "Independent Host / Holiday Rental Operator"); HSM models homes only. So TAM is a hybrid OTA, which is useful for the book's comparison chapters: it shows what changes when a hotel-shaped platform also takes homes.
4. **Neither model has a property, unit, room type, rate plan, reservation or review entity in its data catalog.** The most important entities of the domain exist only as brick descriptions and residuality residues. The book must build its domain model from those (§7.4) and from the research briefs.
5. **The residuality files are where both models become precise.** Their residual architectures name the separations a real stays platform needs (property vs unit vs listing vs license vs operator vs reservation vs payment route). They converge on the same conclusion from both sides (§10.3).

### 1.5 Conventions in this digest

- IDs are quoted in `code` (brick IDs are four or five letters, e.g. `invt`, `lista`; customer IDs `cg1-p1`; jobs `jtbd-cg1-1`; streams kebab-case; data assets kebab-case; stressors short IDs such as `licn`).
- Where both models use the same brick ID, it is prefixed with the model when ambiguity matters: TAM `trst`, HSM `trst`.
- "As modeled" marks model claims. **Synthesis** headings mark this digest's own interpretation.

---

## 2. Customer groups, personas, jobs-to-be-done and journeys

Both models use the standard Productscape structure: a customer **group** contains **customers** (personas), each with `careAbout`, `winsThem`, `theirFear`, two **jobs-to-be-done** (each with two or three steps mapped to bricks), a **KPI pyramid** (customer outcomes and business outcomes), a **product strategy** (vision + year1/year3/year5 horizons with theme, focus, north-star KPIs, revenue streams and milestones), and a **journey story** (Trigger → Discovery → Evaluation → Trial → Engagement → Retention). Discovery and Evaluation narratives are templated in both models; Trigger, Trial, Engagement and Retention are concrete and quotable as illustrations.

### 2.1 TAM — Travel Accommodations Marketplace (four personas)

#### `cg1-p1` Leisure Traveler / Stay Booker (group: Demand-Side Travelers)

- **Who:** a traveler discovering, comparing and booking accommodation for personal trips. "Success is finding a stay that fits intent, budget, location, and trust expectations without hidden friction around policies, payments, or support."
- **Cares about:** relevant options for the destination and trip type; **transparent prices, taxes, and cancellation rules**; trustworthy reviews and accurate content; fast booking with familiar payment options; confidence that changes can be resolved.
- **Wins them:** strong destination search and ranking; property pages with policy clarity; verified review signals and "trustworthy host labels"; low-friction checkout; post-booking self-service.
- **Fears:** booking the wrong stay because content is misleading; "Getting trapped by unclear cancellation or payment terms"; needing support during travel and not getting it.
- **Jobs:**
  - `jtbd-cg1-1` **Find and book the right stay with confidence**: define destination intent and shortlist ("destination, dates, party size … neighborhood, amenities, breakfast, or free cancellation"; `home`, `dest`, `srch`, `mapb`, `mkli`, `pers`) → evaluate trust, fit and policy clarity ("room fit, review quality, payment timing, and cancellation conditions"; `prop`, `room`, `deal`, `trst`, `ssav`) → book with the preferred payment and policy setup (`book`, `acct`, `paym`, `trip`).
  - `jtbd-cg1-2` **Manage changes and problems without losing the trip**: understand what can be changed and by whom (`trip`, `prop`, `self`, `paym`) → self-serve or escalate (`self`, `msgc`, `supp`, `trip`, `trst`) → recover or close fairly ("rebooking, refund, compensation"; `supp`, `paym`, `sett`, `conn`).
- **KPI tree (names only):** top customer outcome *Search-to-book conversion*; branches *Booking confidence* (Traveler booking confidence → Property content clarity, Review trustworthiness; Decision efficiency → Time to relevant shortlist, Room-offer comparison clarity) and *Trip reliability* (Support-free trip resolution → Self-service change success, Proactive trip update delivery; Booking integrity → **Partner confirmation success**, Avoidable cancellation rate). Business top *Net booked room-night contribution*; *Demand efficiency* (Paid acquisition efficiency → High-intent session share, Direct return session share; Conversion quality → Checkout completion, Room-offer click-through) and *Margin protection* (Avoidable servicing cost rate → Dispute incidence, **Payment confusion contacts**; Booking quality → Net cancellation rate, Fraudulent booking loss rate).
- **Vision:** "Make high-confidence accommodation booking feel as easy as inspiration browsing while still being trustworthy when plans change."
- **Horizons:** Y1 *Trustworthy conversion* (ranking quality, checkout clarity, post-booking self-service; milestones "Unify traveler-facing policy clarity across property detail and checkout", "Improve ranking transparency for high-intent destination searches"; revenue: accommodation commission, payments-related monetization). Y3 *Intent-aware marketplace* ("Improve trust and review integrity for non-hotel inventory", "Expand payment-model coverage without increasing support load"; revenue adds sponsored visibility and partner programs, payments and fintech services). Y5 *Global stay confidence platform* ("Make traveler servicing proactive rather than reactive"; "Create stronger trust, quality, and policy normalization across global supply").
- **Journey (`journey-cg1-p1-1` "Weekend city-break booking and recovery"):** trial is "confirming they understand exactly when they pay and what happens if plans change"; engagement: "if something changes, they try self-service modification first and only escalate if the flow stops being clear".

#### `cg2-p1` Managed Travel Booker / Travel Coordinator (group: Demand-Side Travelers)

- **Who:** a coordinator, executive assistant or policy-constrained business traveler. Success = compliant inventory found quickly, accurate traveler information, invoices and changes handled "without manual chasing".
- **Cares about:** business-relevant locations; **travel-policy fit and invoice readiness**; fast rebooking; reliable traveler details and room assignment; minimal reconciliation after the trip.
- **Wins them:** policy- and billing-aware search filters; clear payment and invoicing setup; bulk-friendly traveler data; reliable change resolution; consistent property quality across repeat trips.
- **Fears:** an out-of-policy or un-expensable stay; time lost fixing itinerary and invoice issues; "Travel disruption creating manual coordination work late at night".
- **Jobs:** `jtbd-cg2-1` **Book compliant accommodation fast for a work trip** (search against location, traveler and policy needs → verify commercial and operational fit: payment timing, invoicing, flexibility → confirm and distribute the itinerary "so the traveler and finance workflow receive the right information"). `jtbd-cg2-2` **Handle itinerary changes without breaking policy or reporting** (assess what can be changed → execute the change and keep stakeholders aligned).
- **KPI tree:** top *Policy-compliant booking rate*; Invoice-ready booking rate, Traveler profile completeness, Invoice field accuracy, Policy-filter hit rate, Business-rate clarity, Business-trip rebooking success, Manual touch count per change, Change turnaround time, Traveler notification accuracy, Finance-ready change closure. Business top *Managed travel room-night growth*; Repeat business-booker rate, Account-linked booking share, Managed traveler coverage, Business account activation rate, Support cost per managed booking, Billing correction incidence, Straight-through invoice rate.
- **Vision:** "Let business accommodation booking feel consumer-simple while preserving policy, billing, and disruption control." Y1 *Operationally clean business booking*; Y3 *Policy-aware traveler platform* ("Strengthen company and traveler identity handling"; "Integrate policy and traveler preferences deeper into ranking"); Y5 *Managed travel stay infrastructure* ("Embed accommodation policy controls into the default search and booking experience").
- **Note:** `DOMAIN.md` says managed travel "is not treated as the primary commercial center of gravity". **No brick models company accounts, travel policies or invoicing** — the persona's needs are spread over `srch`, `acct`, `book`, `paym`. This is a gap (§5).

#### `cg3-p1` Hotel Revenue & Operations Manager (group: Supply-Side Partners)

- **Who:** a hotel-side operator who distributes rooms, controls rates and availability, improves visibility, manages reservations and receives payouts. Success = "growing profitable demand without breaking on overbookings, bad reviews, or opaque commercial levers".
- **Cares about:** profitable occupancy; **accurate rate and availability sync**; clear visibility drivers and promotion levers; reliable reservation and payout operations; low support overhead around disputes.
- **Wins them:** "Strong reservation sync and overbooking protection"; pricing insights; merchandising programs (promotions, member discounts); fast payout and finance reconciliation; tools to respond to reviews.
- **Fears:** "Overbooking or bad reservation sync damaging operations"; volume that is unprofitable after discounts; "Losing visibility because the marketplace feels opaque or unfair".
- **Jobs:**
  - `jtbd-cg3-1` **Optimize visibility, occupancy, and rate quality**: set up reliable content, rates and availability ("accurate across the selling window"; `extr`, `cont`, `cald`, `invt`, `conn`) → manage visibility and commercial levers ("promotions, member rates, availability windows"; `prom`, `mkli`, `rate`, `prop`) → learn what drives profitable demand ("booked room-night quality, **rate parity pressure**, guest mix, and promotion outcomes"; `mkli`, `perf`, `prom`, `rept`).
  - `jtbd-cg3-2` **Operate reservations, guest issues, and payouts cleanly**: receive and confirm reservations ("reach the PMS or extranet accurately and on time"; `rsrv`, `invt`, `conn`, `trst`) → handle guest issues and review impact ("disputes, no-shows, special requests"; `msgc`, `supp`, `rept`) → reconcile payout and commercial performance ("commissions, payout timing, deductions"; `paym`, `sett`, `extr`, `mkli`).
- **KPI tree:** top *Visibility-adjusted occupancy*; Promotion ROI confidence, Booked room-night growth, Program participation yield, Search exposure share, Detail-to-book conversion, **Availability accuracy**, **Overbooking incident rate**, **Reservation sync latency** (minutes), Guest issue resolution time, Manual reservation touch rate. Business top *Partner room-night monetization*; Net revenue per available room-night, **Take-rate quality**, Qualified occupancy mix, Promotion payback period, Visibility monetization yield, Partner support cost rate, Payout predictability, Exception handling cost, **Ledger adjustment rate**, **Finance reconciliation lead time**.
- **Vision:** "Make the marketplace the most profitable and operationally reliable external demand channel for accommodation partners." Y1 *Reliable partner growth* ("Reduce reservation-sync and overbooking incidents"; "Explain visibility and promotion drivers more clearly in partner tools"; "Improve payout and adjustment transparency"). Y3 *Marketplace operating cockpit* ("Close more reservation operations inside connected systems"; "Normalize hotel and non-hotel payout and quality workflows"). Y5 *Partner operating system* ("Integrate trust, review, and commercial quality into a unified partner score").
- **Journey (`journey-cg3-p1-1` "Independent hotel managing a peak-demand weekend"):** trigger is "A demand spike, weak pacing period, or comp-set movement"; trial is "publishing rate and inventory changes, trusting that the reservation and connectivity layer will keep PMS, channel-manager, and marketplace state aligned".

#### `cg4-p1` Independent Host / Holiday Rental Operator (group: Supply-Side Partners)

- **Who:** a host or small property manager listing homes or apartments **on the hotel-shaped marketplace**. Success = bookings quickly, simple defaults "without running a full hotel revenue operation".
- **Cares about:** early bookings from trustworthy guests; simple setup for listing, pricing and house rules; clear guest communication and review handling; "Protection against damage, fraud, and late surprises"; easy payouts.
- **Wins them:** fast onboarding; simple calendar, pricing and policy defaults; "booking acceptance controls"; payout visibility; trust and protection signals for hosts.
- **Fears:** "Making the listing live but not getting demand"; "Hosting the wrong guest because controls are unclear"; losing money to damages, chargebacks or confusing payouts.
- **Jobs:** `jtbd-cg4-1` **Get a home listing live and bookable quickly** (set up property, policies and calendar: `extr`, `onbo`, `cont`, `medi`, `invt`, `trst` → make the listing visible: `prom`, `mkli`, `rate`, `prop`). `jtbd-cg4-2` **Run guest stays and payouts with minimal admin work** (manage guest communication and stay preparation: `msgc`, `invt`, `rsrv`, `supp` → close out the stay and receive payout: `paym`, `sett`, `rept`, `trst`).
- **KPI tree:** top *First-booking speed* (days); Host setup time, Policy clarity score, Photo and content completion, Verification completion rate, Calendar setup completion, Issue-free stay share, Host payout confidence, Guest-fit confidence, Issue-handling burden. Business top *Alternative-accommodation supply activation*; New live-unit rate, Activation dropout rate, Content-ready listing rate, First-30-day booking rate, Host retention after first stay, Issue-driven churn rate, Support cost per host, Payout issue incidence.
- **Vision:** "Make hosting on a global travel marketplace feel simple, protected, and commercially worthwhile for smaller operators." Y3 *Autopilot hosting*; Y5 *Global small-host operating layer* ("Improve small-host economics **without turning the product into hotel software**").
- **Journey (`journey-cg4-p1-1` "New host launching a city apartment"):** trigger "only if the setup feels manageable and not like running a hotel system"; trial "is not just going live but receiving a booking".

#### TAM relations (`relations.json`, 9 relations, updated 2026-08-13)

| ID | From → To | Type | Name |
| --- | --- | --- | --- |
| rel-01 | leisure traveler → hotel | commercial | Books hotel rooms |
| rel-02 | leisure traveler → host | commercial | Books holiday rentals ("agreeing to house rules and cancellation terms at checkout") |
| rel-03 | managed travel booker → hotel | commercial | Books policy-compliant work stays ("within company policy and negotiated rate rules") |
| rel-04 | leisure traveler → hotel | financial | Pays stays settled to hotel payouts ("the marketplace collects, deducts commission, and settles the payout") |
| rel-05 | leisure traveler → host | financial | Pays rentals settled to host payouts ("held and released to the host as a payout after check-in, net of fees") |
| rel-06 | hotel → leisure traveler | operational | Confirms and services reservations |
| rel-07 | host → leisure traveler | operational | Hosts guests and handles requests |
| rel-08 | managed travel booker → hotel | operational | Coordinates changes and cancellations |
| rel-09 | leisure traveler → host | information | Writes reviews that drive host visibility |

Note what is **absent**: the pay-at-property (agency) model that `DOMAIN.md` and the `paym` brick describe has no relation; the financial relations show only the merchant/collect model. Connectivity providers, channel managers and corporate employers are not nodes. There is no managed-travel → host relation.

### 2.2 HSM — Hosted Stays Marketplace (three personas)

#### `cg1-p1` Guest Stay Booker (group: Demand-Side Guests)

- **Who:** a consumer booking homes or rooms for "leisure, family, remote-work, or event-based travel". Success = a place "that feels distinct, trustworthy, fairly priced, and easy to manage if plans change".
- **Cares about:** stays matching trip intent, location and **group needs**; trustworthy photos, amenities and house rules; **transparent all-in pricing** and cancellation terms; host responsiveness; messaging and issue recovery.
- **Wins them:** "category-led inspiration"; listing pages with review and host credibility signals; checkout with clear pricing; reliable messaging and trip management; fair handling of disruptions.
- **Fears:** "Booking a stay that looks better online than in reality"; hidden fees; "Getting stuck when a host, check-in, or property issue goes wrong".
- **Jobs:** `jtbd-cg1-1` **Find and book a stay that feels worth trusting** (explore options by "categories, map, amenities, and availability": `insp`, `srch`, `wish` → evaluate listing trust and fit: `list`, `trst`, `idvr` → book with clear pricing: `book`, `paym`, `trip`). `jtbd-cg1-2` **Handle questions, changes, and issues without losing the trip** (coordinate directly with the host: `trip`, `grev` → escalate and recover fairly: `reso`, `trst`, `paym`).
- **KPI tree:** top *Guest booking conversion*; Listing trust score, Price transparency score, Checkout completion, Support-free issue recovery. Business top *Booked nights per active guest*; Gross Booking Value growth, Net revenue per booked night, Repeat-booker rate, Mobile app booking share.
- **Horizons:** Y1 *Guest confidence before booking* ("Unify total-price and cancellation explanation patterns"; "Improve listing-trust ranking inputs"; revenue: stay service fees, guest fee, host fee). Y3 *Guest retention through trust and utility* ("Team trip-planning flows become first-class"). Y5 *Trusted repeat travel marketplace* ("Guest identity and preferences travel seamlessly across stays").
- **Journey ("Group weekend stay from search to issue recovery"):** trigger "decides they want a place that feels more flexible or memorable than a standard hotel"; engagement "if check-in goes wrong they expect the platform to step in quickly".

#### `cg2-p1` Everyday Home Host (group: Supply-Side Hosts)

- **Who:** an individual host with one or a few homes or rooms. Success = quick setup, trustworthy bookings, no operational overload, "feeling financially and operationally protected".
- **Cares about:** simple onboarding; reliable bookings from trustworthy guests; calendar, pricing and house-rule control; predictable payouts and understandable fees; strong support "when damage, fraud, or disruption happens".
- **Wins them:** fast time to first listing and first booking; photo-quality help; understandable pricing and discount suggestions; "Protection, screening, and [protection-programme] confidence"; earnings visibility.
- **Fears:** **"Letting the wrong guest into their home"**; "complex rules, pricing, or local requirements"; losing money or time when a stay goes wrong.
- **Jobs:**
  - `jtbd-cg2-1` **Launch a listing and earn bookings without becoming a full-time operator**: get approved and create the listing (`hono`, `lista`, `comp`) → set calendar and pricing (`cala`, `pric`, `data`) → start hosting and learn what improves demand (`host`, `trip`, `grev`).
  - `jtbd-cg2-2` **Run hosting safely and get paid reliably**: screen demand ("guest verification and house-rule risk"; `idvr`, `trst`) → get paid and understand the economics ("payouts, fees, **taxes**"; `paym`, `host`) → recover from damage, disputes or cancellations (`reso`, `trst`, `opco`).
- **KPI tree:** top *Time to first booking*; Host activation rate, **Calendar accuracy rate**, Host protection confidence, Payout predictability. Business top *Active listing quality rate*; New host 90-day retention, First-year listing survival, Occupancy-adjusted earnings, top-host progression.
- **Horizons:** Y1 *Fast and safe host activation*; Y3 *High-quality host automation* ("House rules and risk preferences become easier to configure"); Y5 *Confident host entrepreneurship* ("[protection programme] becomes a major supply moat").

#### `cg3-p1` Professional Host / Co-host Operator (group: Professional Supply Operators)

- **Who:** "A professional operator, boutique manager, or co-host business running multiple listings across one or more markets." Success = portfolio occupancy, disciplined operations, **staff permissions**, issue control.
- **Cares about:** many listings, calendars and staff roles in one system; occupancy without bad discounting; **operational SLA control for cleaning, check-in, and support**; portfolio-level payouts; tools that scale beyond consumer-grade workflows.
- **Wins them:** multi-listing dashboards and permissions; portfolio pricing and availability controls; issue queues; "Clear payout reconciliation and reservation exports"; scalable compliance controls.
- **Fears:** outgrowing the platform's operating tools; opaque performance drivers; "Operational incidents damaging reputation across multiple listings at once".
- **Jobs:** `jtbd-cg3-1` **Operate a portfolio of listings for profitable occupancy** (structure the portfolio and assign co-hosts: `coho`, `lista`, `apix` → optimize occupancy and margin: `pric`, `cala`, `host`, `data` → run daily operations: "cleaning, check-in, guest communication, and readiness workflows"; `opco`, `trip`, `coho`). `jtbd-cg3-2` **Control exceptions, compliance, and portfolio risk** (detect and triage risk: `idvr`, `trst`, `comp` → resolve operational and financial fallout: `reso`, `paym`, `host`).
- **KPI tree:** top *Portfolio revenue per available night*; Multi-listing occupancy, Search visibility efficiency, Operational SLA attainment, Resolution cycle time. Business top *High-quality professional supply growth*; Portfolio retention, **Co-host adoption**, Cancellation-adjusted revenue, Damage-case recovery time.
- **Horizons:** Y1 *Professional host operating leverage* ("Improve co-host permissions and auditability"). Y3 *Scaled operator control* ("Portfolio compliance becomes more proactive"; "**Channel and partner sync becomes easier where appropriate**"). Y5 *Best-in-class pro-host marketplace platform*.
- **Journey ("Growing from a few listings to a managed portfolio"):** trigger "single-host workflows break down"; engagement "every exception tests whether [the platform] behaves like a professional operating system".

#### HSM relations (`relations.json`, 9 relations)

| ID | From → To | Type | Name |
| --- | --- | --- | --- |
| rel-01 | guest → everyday host | commercial | Books stays with everyday hosts |
| rel-02 | guest → professional operator | commercial | Books professionally managed stays ("larger groups, longer remote-work stays, or event travel") |
| rel-03 | everyday host → guest | operational | Hosts and services the stay |
| rel-04 | professional operator → guest | operational | Delivers standardized stay operations ("staffed messaging, cleaning turnover, maintenance response") |
| rel-05 | guest → everyday host | financial | Pays the booking through the platform ("holds the funds and releases the host payout after check-in, netting out service fees") |
| rel-06 | everyday host → professional operator | commercial | **Delegates listing management to co-hosts** ("under agreed permissions and a management-fee arrangement") |
| rel-07 | professional operator → everyday host | financial | **Remits owner payouts** ("statements that reconcile occupancy, payouts, and expenses per listing") |
| rel-08 | guest → everyday host | information | Reviews and rates the stay |
| rel-09 | guest → professional operator | information | Feeds review and issue signals |

HSM's relations encode the **owner–operator split** (rel-06, rel-07) that its residuality stressor `coho` later turns into a structural requirement. Payment always passes through the platform; there is no pay-at-property path.

### 2.3 Cross-model persona comparison

| Role | TAM | HSM | What differs |
| --- | --- | --- | --- |
| Leisure demand | `cg1-p1` Leisure Traveler — destination → room/rate choice; payment timing; policy clarity | `cg1-p1` Guest Stay Booker — categories, wishlists, group trips, all-in price, host credibility | TAM evaluates room offers and payment models; HSM evaluates a unique home and its host |
| Business demand | `cg2-p1` Managed Travel Booker — policy, invoices, traveler data | **Not modeled** | Corporate booking is OTA territory in these models |
| Professional supply | `cg3-p1` Hotel Revenue & Ops Manager — rates, availability, parity, PMS/channel-manager sync, settlement | `cg3-p1` Professional Host / Co-host Operator — portfolio of homes, staff roles, turnover SLAs, reservation exports | Hotel revenue management vs portfolio operations; inbound connectivity vs outbound export |
| Small supply | `cg4-p1` Independent Host on the OTA — wants simple defaults, not hotel software | `cg2-p1` Everyday Home Host — fears the wrong guest in their home; protection is a precondition | Same person, different platform shape: TAM must simplify a hotel model; HSM is built around the host |
| Owner (non-operating) | Not modeled | Implicit in rel-06/rel-07 and stressor `coho` | Owner vs operator vs permit holder only in HSM |
| Connectivity partners (channel managers, PMS vendors) | Not a persona; external system on `invt`/`conn`; `DOMAIN.md`: "modeled through products and capabilities rather than as the main customer narrative" | Not a persona; "Professional operator tooling" external consumer of `apix` | Gap in both: no integration-partner persona (LISTED's GLM/REM had one) |
| Cleaners, maintenance, service providers | Not modeled | Appear in rel-04 and `coho` residue ("service provider") | No service-provider persona |
| Support agents, trust & safety operators, market managers | Implicit (internal ops console) | Implicit | No internal-operator persona in either model |
| Affiliates, metasearch, travel agents | Mentioned only as discovery channels ("metasearch", "partner channels") | Not modeled | Gap: demand-side distribution partners |

---

## 3. Business capability map (product bricks) — complete domain inventory

This section is the **coverage checklist for the book**: every root group, sub-group and brick of both models, with ID, type, status, all modules (by layer), and a one-line purpose condensed from the model.

### 3.1 How bricks are modeled

A **brick** has an ID, name, type (`full-stack`, `service`, `integration`), status (`invest` or `sustaining`), description, `layers` (ui / interfaces / worker / service / integration, each with named modules and module-to-module dependencies), `brickDependencies` (to other bricks, with a typed edge and description), external systems in both directions, `dataDependencies` (asset ID + role `own`, `read`, `write`, `query`, `publish`) and a generic evidence link.

- **TAM:** 34 bricks; types 20 `full-stack`, 13 `service`, 1 `integration` (`conn`). Status: `invest` = `book`, `prom`, `paym`, `mkli` (checkout, partner merchandising, payments, marketplace intelligence); the other 30 `sustaining`.
- **HSM:** 21 bricks; 15 `full-stack`, 5 `service`, 1 `integration` (`apix`). Status: `invest` = `list`, `book`, `hono`, `lista`, `pric`, `opco`, `coho`, `reso` (listing trust, checkout, host activation and authoring, pricing, turnover operations, co-hosts, resolutions); 13 `sustaining`.
- **Module names are more specific than LISTED's generic templates** (e.g. "Reservation State Machine", "Payment Model Normalization", "Restriction Policy Engine", "Turnover task engine"), so they *can* be mined for architecture sketches, with care.

### 3.2 TAM inventory (34 bricks)

#### Root A. Traveler Experience

**A1. Discovery and consideration (8)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `home` | Marketplace Home & Destination Landing | full-stack / sustaining | ui: Traveler Entry UI · interfaces: Landing Assembly API · worker: Journey Event Stream · service: Landing Experience Shell; Session Recall and Intent Recovery; Merchandising Slot Orchestration | Traveler entry surfaces: destination inspiration, recent-search recall, campaign landings, jump-off into search |
| `dest` | Destination Discovery | full-stack / sustaining | ui: Destination Discovery UI · interfaces: Destination Metadata API · worker: Destination Signal Feed · service: Destination Context Graph; Travel Intent Resolution; Destination Experience Layer | Move travelers from broad trip intent into accommodation search with destination and map context |
| `srch` | Search, Ranking & Filters | full-stack / sustaining | ui: Search Experience UI · interfaces: Search and Ranking API · worker: Inventory Update Feed · service: Search Index and Facet Engine; Ranking and Eligibility Pipeline; Filter and Explainability Controls | Accommodation search, filtering, sorting, map browsing and ranking across traveler and policy intent |
| `mapb` | Map-Based Stay Browser | full-stack / sustaining | ui: Map Browse UI · interfaces: Viewport Search API · service: Map Tile and Geometry Adapter; Viewport Result Resolver | Map-centric browse for neighborhood, landmark and travel-radius decisions on the same ranked inventory |
| `pers` | Personalization & Recommendations | service / sustaining | interfaces: Recommendation API · worker: Personalization Event Feed · service: Traveler Intent Models; Recommendation Delivery Layer | Recommendation, recirculation and traveler-intent modeling across home, search and return journeys |
| `deal` | Deals and Member Merchandising | full-stack / sustaining | ui: Offer Presentation UI · interfaces: Offer Decision API · service: Offer Eligibility Resolver; Merchandising Presentation Layer; Treatment Experimentation Controls | Traveler-facing presentation of discounts, member programs, urgency signals and merchandising treatments |
| `ssav` | Saved Searches & Price Alerts | full-stack / sustaining | ui: Saved Search UI · interfaces: Alert Decision API · worker: Alert Trigger Feed · service: Saved Intent Store; Alert Trigger Engine | Persist search intent, watch prices, trigger alert-driven return journeys |
| `prop` | Property Detail & Reviews | full-stack / sustaining | ui: Property Detail UI · interfaces: Property Detail API · service: Property Content Assembly; Review and Quality Signals; Trust and Policy Explanation Layer | Property page, room detail, policy presentation, reviews and booking-confidence content |

**A2. Booking and trip management (7)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `room` | Room & Rate Selection | full-stack / sustaining | ui: Room Selection UI · interfaces: Room Offer API ("bookable room, rate, and occupancy combinations") · service: Room Plan Resolver; Rate Condition Comparison ("Normalizes cancellation, payment, and meal-plan differences across room offers") | Select and compare room plans, rate conditions, occupancy fit and bundled options before checkout |
| `book` | Checkout & Booking Orchestration | full-stack / **invest** | ui: Checkout UI · interfaces: Reservation API · worker: Reservation Event Feed · service: Checkout State and Eligibility; Policy and Disclosure Layer · integration: Reservation Orchestration ("Creates and updates booking records across marketplace and partner systems") | Checkout, reservation creation, policy handling, confirmation and booking-state management |
| `acct` | Traveler Account & Wallet | full-stack / sustaining | ui: Traveler Account UI · interfaces: Traveler Profile API · service: Traveler Profile Store; Wallet and Preference Controls | Traveler profile, preferences, traveler-party data, loyalty-adjacent preferences, saved payment or invoicing context |
| `trip` | Trip Management & Messaging | full-stack / sustaining | ui: Trip UI · interfaces: Trip API · worker: Notification Event Feed · service: Trip Timeline; Message and Notification Routing; Trip Status Explanation Layer | Itinerary, pre-stay and post-booking messaging, self-service entry, reservation-state communication |
| `msgc` | Guest-Property Messaging | service / sustaining | interfaces: Messaging API · worker: Message Event Feed · service: Conversation Thread Store; Message Delivery and Policy Controls | Structured and free-form traveler–property–operations communication |
| `self` | Self-Service Changes & Recovery | full-stack / sustaining | ui: Change and Recovery UI · interfaces: Change Decision API · service: Eligibility and Policy Engine; Recovery Flow Orchestration | Change, cancellation, modification and incident-recovery flows that reduce support load |
| `reve` | Review Collection & Stay Feedback | full-stack / sustaining | ui: Review Invitation UI · interfaces: Review Submission API · service: Stay Completion Triggering; Review Submission Experience | Post-stay review invitation and verified-review submission tied to completed bookings |

#### Root B. Partner Operations

**B1. Supply onboarding and content (4)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `extr` | Partner Extranet | full-stack / sustaining | ui: Partner UI · service: Partner Control UI; Operational Workbench | Partner control surface: listing setup, policies, reservation operations, finance visibility, performance |
| `onbo` | Partner Onboarding & Verification | full-stack / sustaining | ui: Onboarding UI · interfaces: Activation API · service: Partner Eligibility and Setup Workflow; Verification and Activation Controls ("risk gating before a property becomes bookable") | Onboard hotels and hosts: business identity, property legitimacy, operating readiness, first-booking activation |
| `cont` | Content & Policy Studio | full-stack / sustaining | ui: Content Authoring UI · interfaces: Listing Content API · service: Content Quality Validation; Policy Authoring Workspace ("house rules, cancellation terms, and stay conditions") | Property content, photo quality, room setup, amenities, cancellation and house policies |
| `medi` | Property Media Pipeline | service / sustaining | interfaces: Media Asset API · worker: Media Processing Feed · service: Media Ingestion and Transformation; Media Moderation and Categorization | Upload, moderation, enhancement, categorization and distribution of property and room media |

**B2. Inventory and commercial performance (7)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `invt` | Inventory, Rates & Reservations | service / sustaining | interfaces: Supply Core API · worker: Reservation Event Feed · service: Rate and Availability Core; **Reservation State Machine**; **Supply Integrity Controls** ("validation and conflict rules to prevent inconsistent bookable inventory") | The rate, availability, room, reservation and booking-state backbone for supply |
| `cald` | Calendar & Availability Controls | full-stack / sustaining | ui: Calendar Control UI · interfaces: Availability Control API · service: Availability Editing Workspace; **Restriction Policy Engine** ("minimum-stay, arrival, departure, and booking-window controls") | Partner control of calendar state, stay restrictions, booking windows and closures across hotel and homes supply |
| `rsrv` | Reservation Inbox & Operations | full-stack / sustaining | ui: Reservation Operations UI · interfaces: Reservation Operations API · service: Reservation Work Queue; Reservation Exception Controls ("overbooking, no-show, and special-case operational states") | Partner reservation management: no-shows, check-in state, special requests, exceptions |
| `prom` | Partner Merchandising & Programs | full-stack / **invest** | ui: Commercial Controls UI · interfaces: Promotion Rules API · service: Program Eligibility and Enrollment; Promotion Authoring; Program Impact Feedback | Promotions, member rates, preferred programs, merchandising choices, commercial optimization |
| `rate` | Rate Recommendation Engine | service / sustaining | interfaces: Pricing Guidance API · service: Comp-Set and Demand Signal Models; Recommendation Delivery API; Constraint and Margin Guardrails | Price, availability-window and discount recommendations for partners |
| `perf` | Partner Performance Analytics | full-stack / sustaining | ui: Partner Analytics UI · interfaces: Performance Reporting API · service: Performance Metrics Warehouse; Insight and Narrative Layer | Partner reporting on visibility, occupancy, conversion, program impact and quality |
| `rept` | Reputation & Quality Operations | service / sustaining | interfaces: Quality Operations API · worker: Quality Signal Feed · service: Review Intake and Validation; Quality and Issue Monitoring; Partner Remediation Workflow | Verified review handling, quality monitoring, content integrity, partner remediation |

#### Root C. Marketplace Foundations

**C1. Payments and recovery (3)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `paym` | Payments & Payouts | service / **invest** | interfaces: Payments API · worker: Payment State Feed · service: Traveler Payment Orchestration; Partner Remittance and Reconciliation; **Payment Model Normalization** ("pay-now, pay-later, pay-at-property, and managed-payment logic across markets") | Collection, guarantees, payout orchestration, refunds, disputes, finance visibility for multiple payment models |
| `sett` | Partner Settlement & Ledger | service / sustaining | interfaces: Settlement Ledger API · service: Settlement Ledger Core ("line-level financial records for bookings, deductions, and remittance"); Finance Adjustment Workflow | Partner-facing ledger, settlement accounting, commission adjustments, audit-ready finance records |
| `supp` | Customer Support & Recovery | service / sustaining | interfaces: Support Operations API · worker: Recovery Event Feed · service: Case and Workflow Orchestration; Recovery Decisioning; Escalation and SLA Controls | Case management, triage, rebooking and recovery, exception handling for travelers and partners |

**C2. Trust, connectivity, and intelligence (5)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `trst` | Trust, Verification & Risk Controls | service / sustaining | interfaces: Trust API · worker: Risk Signal Feed · service: Identity and Verification ("partner and host verification"); Fraud and Abuse Controls ("risky booking, payment, and interaction patterns"); Integrity Operations Layer | Host verification, fraud checks, abuse prevention, incident handling, risk scoring across bookings, reviews, messaging |
| `conn` | Connectivity & Partner APIs | **integration** / sustaining | interfaces: Partner Connectivity API · worker: Partner Integration Event Feed · service: Partner Reliability Controls · integration: Partner Contract and Validation Layer; Reservation and Inventory Sync | Inbound connectivity, reservation sync and inventory APIs for PMS, channel managers and other partners |
| `mkli` | Marketplace Intelligence | service / **invest** | interfaces: Insight APIs and Reporting Feeds · worker: Marketplace Signal Feed · service: Marketplace Metrics and Attribution; Decisioning Models; Experiment and Causal Analysis Layer | Decision support and data products for ranking, pricing, promotion, quality and marketplace economics |
| `geoa` | Geo & Localization Services | service / sustaining | interfaces: Geo and Localization API · service: Place and Boundary Resolver; Localization and Market Context | Geo-resolution, local-market normalization, localization and place intelligence |
| `idam` | Identity & Access Management | service / sustaining | interfaces: Identity API · worker: Identity Event Feed · service: Authentication and Session Core; Role and Access Policy Engine | Authentication, authorization, sessions and roles for travelers, partners and internal users |

### 3.3 HSM inventory (21 bricks)

#### Root A. Guest Experience ("Guest-facing discovery, booking, and trip confidence capabilities")

**A1. Discovery and consideration (4)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `insp` | Inspiration & Category Discovery | full-stack / sustaining | ui: Browse UI · interfaces: Landing content API · service: Category and destination landing assembly; Intent recovery and recirculation | Turn broad trip intent into categories, destinations and marketplace sessions |
| `srch` | Search, Ranking & Map Browse | full-stack / sustaining | ui: Search UI · interfaces: Search and ranking API · service: Search index and relevance engine; Map browse and geo-intent layer | Search, ranking, filtering and map-led browsing across homes, rooms and stay attributes |
| `list` | Listing Detail & Review Trust | full-stack / **invest** | ui: Listing detail UI · interfaces: Listing detail API · service: Listing content renderer; Review and trust evidence service | Listing page, reviews, amenity clarity, host reputation, policy explanation |
| `wish` | Wishlists & Sharing | full-stack / sustaining | ui: Wishlists UI · interfaces: Saved list API · service: Saved-lists service; Share and collaboration layer | Guest shortlisting, sharing and group coordination before booking |

**A2. Booking and stay management (3)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `book` | Booking & Checkout | full-stack / **invest** | ui: Checkout UI · interfaces: Reservation API · service: Reservation orchestration ("Validates listing state, guest details, and policy conditions"); Checkout experience | Reservation creation, fee and policy explanation, payment choice, confirmation |
| `trip` | Trip Messaging & Itinerary | full-stack / sustaining | ui: Trip UI · interfaces: Messaging API · service: Reservation timeline service; Guest-host messaging | Reservation visibility, guest–host messaging, check-in coordination, itinerary |
| `grev` | Guest Reviews & Re-engagement | full-stack / sustaining | ui: Review submission UI · interfaces: Review API · service: Review collection service; Re-engagement triggers | Post-stay reviews, reputation loops and recirculation into the next booking |

#### Root B. Host Success ("Host activation, listing quality, operating control, and earnings capabilities")

**B1. Host activation and optimization (4)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `hono` | Host Onboarding & Verification | full-stack / **invest** | ui: Host onboarding UI · interfaces: Readiness API · service: Host activation flow; Host readiness service | Host signup, readiness checks and verification before a listing goes live |
| `lista` | Listing Authoring & Content | full-stack / **invest** | ui: Listing editor UI · interfaces: Listing content API · service: Listing editor; Content quality service | Listing setup, content, photo guidance, policy selection, amenities |
| `cala` | Calendar & Availability | full-stack / sustaining | ui: Calendar UI · interfaces: Availability API · service: Availability engine ("bookable dates, blocks, and stay restrictions"); Calendar control UI | Date availability, stay rules, booking windows, availability accuracy |
| `pric` | Pricing & Discounts | full-stack / **invest** | ui: Pricing UI · interfaces: Pricing API · service: Pricing rules engine ("host-defined pricing, discounts, and length-of-stay rules"); Pricing guidance layer | Nightly pricing, discount programs, stay rules and pricing guidance |

**B2. Host operations and economics (3)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `opco` | Turnover & Operations Coordination | full-stack / **invest** | ui: Operations UI · interfaces: Operations API · service: Turnover task engine; Ops coordination UI | Changeover, cleaning, readiness and reservation-level operating coordination |
| `coho` | Co-host Network & Permissions | full-stack / **invest** | ui: Co-host management UI · interfaces: Permissions API · service: Role and permission service ("delegated permissions and audit trails"); Co-host collaboration UI | Delegated operations, listing-level permissions, portfolio collaboration across hosts and co-hosts |
| `host` | Host Performance & Earnings | full-stack / sustaining | ui: Host dashboard UI · interfaces: Host analytics API · service: Host performance warehouse; Earnings and performance dashboards | Occupancy, earnings, response quality, listing performance and operator reconciliation views |

#### Root C. Marketplace Foundations ("Shared trust, financial, policy, analytics, and integration capabilities")

**C1. Trust, payments, and policy (5)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `idvr` | Identity & Verification | service / sustaining | interfaces: Verification API · service: Identity verification workflow | Guest and host identity verification, document checks, core screening signals |
| `trst` | Trust, Safety & [protection programme] | service / sustaining | ui: Incident operations UI · interfaces: Trust decision API · service: Risk scoring and screening ("reservation risk and policy-sensitive demand"); Protection and incident workflow ("damage, and safety intervention paths") | Reservation screening, trust enforcement, host protection, guest safety |
| `paym` | Payments, Taxes & Payouts | service / sustaining | interfaces: Payments API · service: Payment orchestration; Host payout ledger ("fees, taxes, and payout timing") | Guest payments, host payouts, fee logic, refunds, tax flows, financial ledger state |
| `reso` | Resolutions & Support | full-stack / **invest** | ui: Resolution UI · interfaces: Support case API ("claims, disputes, and issue-case state") · service: Case orchestration; Resolution center | Support, claims, refunds, disputes and service recovery |
| `comp` | Local Compliance & Policy Controls | service / sustaining | interfaces: Policy control API · service: Market policy registry ("market-level rules, restrictions, and listing requirements") | Market-specific rules, listing eligibility, policy enforcement and audit state |

**C2. Marketplace intelligence and connectivity (2)**

| ID | Name | Type / status | Modules | Purpose |
| --- | --- | --- | --- | --- |
| `data` | Marketplace Intelligence & Experimentation | service / sustaining | interfaces: Insights API · service: Marketplace insight warehouse; Experimentation and recommendation layer | Demand insight, experiments, search intelligence, pricing signals, reporting |
| `apix` | Partner APIs & Channel Connectivity | **integration** / sustaining | interfaces: Partner API · integration: Partner gateway; Sync and export services | Partner sync, operational exports and connectivity for scaled operators and their tooling |

### 3.4 TAM dependency spine (hand-written; usable as an architecture sketch)

Most depended-on: `invt` (6 incoming), `mkli` (6), `trst` (5), `paym` (5), then `srch`, `trip`, `rept`, `book` (3 each). Bricks with no outgoing edges — the foundations — are `invt`, `rept`, `paym`, `trst`, `mkli`, `geoa`, `idam`. Key edges, quoted from the model:

- **Supply backbone.** `invt` is the source of truth for rates, availability and reservation state. `srch` → `invt` ("Depends on live rate and availability state"); `room` → `invt` ("Uses live room, rate, and availability state from supply systems"); `cald` → `invt` ("Uses supply state as the underlying source of truth for calendar actions"); `rsrv` → `invt` ("Uses core reservation state to power partner reservation workflows"); `rate` → `invt`; `conn` → `invt` ("Uses supply-core data to power external sync"). External: `invt` "Consumes and emits reservation state to PMS and channel manager systems".
- **Discovery.** `home` → `dest`, `pers`; `dest` → `geoa`, `srch` (handoff); `mapb` → `srch` ("Uses the same underlying ranked inventory as core search"), `geoa`; `srch` → `mkli` ("commercial, quality, and demand signals"), `deal` ("Uses eligible offer treatments when ranking"); `pers` → `mkli`, `acct`; `ssav` → `srch` (search definitions), `trip` (notification routing).
- **Offer and checkout.** `prop` → `rept` (verified reviews), `trst` ("Displays host-type and trust indicators"), `room`; `room` → `deal` ("Applies eligible commercial treatments to room offers"); `deal` → `prom` ("Consumes partner promotion and program data"), `mkli`; `book` → `room` ("Uses selected room and rate context to create the booking"), `paym` ("charge, guarantee, and refund flows"), `conn` ("Coordinates with partner connectivity where required").
- **Post-booking.** `trip` → `book` (state), `msgc`, `supp` (escalation); `msgc` → `trip`, `trst` ("govern risky or policy-sensitive messaging"); `self` → `trip`, `paym` ("show accurate financial consequences"), `supp`; `reve` → `book` ("completed booking state to determine review eligibility"), `rept`.
- **Partner side.** `extr` → `idam`, `paym`; `onbo` → `trst` (partner legitimacy), `cont` ("content and policy readiness as an activation gate"); `cont` → `medi`, `rept`; `medi` → `trst`; `prom` → `mkli`, `rate`; `perf` → `mkli`, `prom`.
- **Money and recovery.** `sett` → `paym` ("payment and payout events to maintain settlement records"), `book` ("explain finance outcomes against reservation events"); `supp` → `paym`, `conn` ("connectivity and partner-state data during booking recovery").
- **External systems (12):** Marketing and Acquisition Platforms; Web and Mobile Clients; Traveler Web and App Clients; Search Infrastructure; Mapping Platforms; External Mapping and Geo Datasets; Email and Push Delivery Platforms; Media Storage and CDN Platforms; Property Management Systems; Channel Managers and PMS Platforms ("XML/JSON APIs"); Payment Service Providers; Identity Providers.

**Defects to avoid copying:** `trip` hosts "Message and Notification Routing" and `ssav` uses it for alerts, so notifications have no shared owner; `invt` holds reservation state *and* `book` owns the checkout record — the model never says which is the reservation system of record (see stressor `insv`, which forces the question); `reve` → `rept` and `prop` → `rept` but no brick feeds reviews into ranking explicitly.

### 3.5 HSM dependency spine (thinner; several essential edges missing)

Most depended-on: `trst` (4), `data` (3), `paym` (3), `book` (3). Edges:

- `insp` → `srch` (handoff); `srch` → `data` (ranking signals), `list` ("Depends on accurate listing content and review quality"); `list` → `trst`, `grev`.
- `book` → `paym` ("payment, fee, and refund logic"), `trst` ("Checks trust and screening state before confirmation"); `trip` → `book`; `grev` → `trst` (moderation).
- `hono` → `idvr`, `comp` ("local market policy eligibility and restrictions"); `lista` → `list` ("Provides listing data consumed by guest-facing listing pages" — the edge is drawn in the wrong direction); `cala` → `book` ("Receives booking-state changes that affect availability"); `pric` → `data`.
- `opco` → `trip` ("reservation timing and itinerary details"); `coho` → `host`; `host` → `paym`, `data`.
- `trst` → `idvr`; `reso` → `paym`, `trst`; `apix` → `book`, `host`.
- **External systems (3):** Identity verification providers ("document, watchlist, and identity checks"); Payment processors; Professional operator tooling (consumer of `apix`).

**Missing edges a writer must supply:** `book` does not depend on `cala` or `pric` (a booking that never checks availability or price); `srch` does not depend on `cala` (search without availability); `comp` is depended on only by `hono`, so local rules never gate `cala`, `book` or `srch` (the `licn` stressor fixes exactly this); `lista` has no media pipeline; `opco` does not depend on `coho` for task assignment; nothing in the model talks to an external calendar or channel manager.

---

## 4. Overlap and difference matrix

### 4.1 Brick-to-brick mapping

Legend: **Same** = same concept and scope; **Partial** = overlapping responsibility, different scope or granularity; **TAM only** / **HSM only** = no counterpart brick in the other model.

| TAM brick | HSM brick | Match | Note |
| --- | --- | --- | --- |
| `home` Marketplace Home & Destination Landing | `insp` Inspiration & Category Discovery | Partial | HSM merges home and destination entry into one brick and leads with *categories* (stay types, themes) rather than destinations |
| `dest` Destination Discovery | `insp` | Partial | TAM has a "Destination Context Graph" and "Travel Intent Resolution" |
| `srch` Search, Ranking & Filters | `srch` Search, Ranking & Map Browse | Same | Same ID. TAM ranking consumes offers (`deal`) and live rates (`invt`); HSM ranking consumes listing and review quality (`list`) |
| `mapb` Map-Based Stay Browser | `srch` ("Map browse and geo-intent layer") | Partial | Map is a brick in TAM, a module in HSM |
| `pers` Personalization & Recommendations | `data` ("Experimentation and recommendation layer") | Partial | HSM has no traveler-intent model brick |
| `deal` Deals and Member Merchandising | — (host-side discounts in `pric`) | TAM only | Guest-facing member rates, urgency signals and merchandising treatments have no HSM counterpart |
| `ssav` Saved Searches & Price Alerts | `wish` Wishlists & Sharing | Partial | Different concepts: TAM saves a *query* and watches price; HSM saves *listings* and shares them with a group |
| `prop` Property Detail & Reviews | `list` Listing Detail & Review Trust | Same | TAM shows rooms and "host-type" labels; HSM emphasizes host reputation |
| `room` Room & Rate Selection | — | **TAM only** | The defining OTA capability: room types × rate plans × occupancy × cancellation/payment/meal conditions. In HSM the listing *is* the bookable unit |
| `book` Checkout & Booking Orchestration | `book` Booking & Checkout | Same | Same ID. TAM orchestrates across "marketplace and partner systems"; HSM checks trust screening before confirmation |
| `acct` Traveler Account & Wallet | — | TAM only | HSM has no account, profile or wallet brick (guest identity only in `idvr`) |
| `trip` Trip Management & Messaging | `trip` Trip Messaging & Itinerary | Same | Same ID |
| `msgc` Guest-Property Messaging | `trip` ("Guest-host messaging") | Partial | Separate service in TAM; a module in HSM |
| `self` Self-Service Changes & Recovery | `reso` (partly) | Partial | HSM has no self-service change/cancellation brick; changes route to resolutions |
| `reve` Review Collection & Stay Feedback | `grev` Guest Reviews & Re-engagement | Same | HSM adds re-engagement; `grev` is in no stream |
| `extr` Partner Extranet | — (host UIs live in `hono`, `lista`, `cala`, `pric`, `host`) | TAM only | TAM has one partner control surface; HSM distributes host UI across capability bricks |
| `onbo` Partner Onboarding & Verification | `hono` Host Onboarding & Verification | Same | TAM includes business identity and property legitimacy for hotels; HSM depends on `comp` for local eligibility |
| `cont` Content & Policy Studio | `lista` Listing Authoring & Content | Same | Both own house rules and cancellation policy authoring |
| `medi` Property Media Pipeline | — (photo guidance inside `lista`) | TAM only | HSM has no media pipeline |
| `invt` Inventory, Rates & Reservations | `cala` (availability only) | Partial | TAM's backbone holds rates, availability, reservation state machine and integrity controls; HSM splits availability (`cala`), price (`pric`) and reservation (`book`) with no integrity layer |
| `cald` Calendar & Availability Controls | `cala` Calendar & Availability | Same | Both own min-stay, booking-window and blocked-date rules |
| `rsrv` Reservation Inbox & Operations | `opco` (partly), `trip` | Partial | TAM: partner work queue, no-shows, overbooking exceptions. HSM: turnover tasks per reservation |
| `prom` Partner Merchandising & Programs | `pric` ("discount programs") | Partial | TAM programs (preferred, member rates) influence visibility; HSM discounts are host pricing rules |
| `rate` Rate Recommendation Engine | `pric` ("Pricing guidance layer") | Partial | TAM: comp-set and demand models with margin guardrails; HSM: guidance inside the pricing brick |
| `perf` Partner Performance Analytics | `host` Host Performance & Earnings | Same | HSM adds earnings and operator reconciliation views |
| `rept` Reputation & Quality Operations | `grev` + `trst` (moderation) | Partial | TAM has partner remediation workflow; HSM does not |
| `paym` Payments & Payouts | `paym` Payments, Taxes & Payouts | Same | Same ID. TAM normalizes multiple payment models; HSM adds taxes and always collects |
| `sett` Partner Settlement & Ledger | `paym` ("Host payout ledger") | Partial | Settlement ledger is a brick in TAM, a module in HSM |
| `supp` Customer Support & Recovery | `reso` Resolutions & Support | Same | HSM adds claims (damage) |
| `trst` Trust, Verification & Risk Controls | `trst` Trust, Safety & [protection] + `idvr` Identity & Verification | Partial | Same ID, different scope: TAM is verification + fraud; HSM splits identity out and adds reservation screening and damage/safety protection |
| `conn` Connectivity & Partner APIs | `apix` Partner APIs & Channel Connectivity | Partial | **Opposite direction**: TAM is inbound supply connectivity (PMS, channel managers push rates/availability, receive reservations); HSM is mostly outbound "sync and export" for operator tooling |
| `mkli` Marketplace Intelligence | `data` Marketplace Intelligence & Experimentation | Same | Both include experimentation |
| `geoa` Geo & Localization Services | — (geo layer inside `srch`) | TAM only | Localization (language, market context) absent in HSM |
| `idam` Identity & Access Management | — (`coho` has a role service) | TAM only | HSM has no authentication/authorization brick |
| — | `opco` Turnover & Operations Coordination | **HSM only** | Cleaning, changeover, readiness tasks per reservation |
| — | `coho` Co-host Network & Permissions | **HSM only** | Delegated roles per listing, portfolio collaboration, audit trail |
| — | `comp` Local Compliance & Policy Controls | **HSM only** | Market policy registry and listing eligibility (TAM covers licensing only in residuality) |
| — | `wish` Wishlists & Sharing (group collaboration aspect) | HSM only (partial vs `ssav`) | Group trip planning is an HSM theme (Y3 "Team trip-planning flows") |

**Counts:** 12 TAM bricks have a **same-concept** HSM counterpart (`srch`, `prop`, `book`, `trip`, `reve`, `onbo`, `cont`, `cald`, `perf`, `paym`, `supp`, `mkli`); 15 are **partial** overlaps (including `home` and `dest`, which together equal HSM `insp`); 7 are **TAM only** (`room`, `deal`, `acct`, `extr`, `medi`, `geoa`, `idam`); 3 are **HSM only** (`opco`, `coho`, `comp`), with `wish` partially new.

### 4.2 Structural differences explained (synthesis)

| Dimension | TAM (OTA-style) | HSM (hosted stays) | Architectural consequence |
| --- | --- | --- | --- |
| **What is sold** | A *room offer*: property → room type → rate plan (conditions: cancellation, payment timing, meal plan) × occupancy × dates (`room`, `invt`) | A *listing*: one home or room with one calendar and one price set (`lista`, `cala`, `pric`) | OTA needs an offer-composition layer and a rate model; hosted stays needs a unit calendar and length-of-stay pricing rules |
| **Inventory model** | Counted inventory per room type and date, with restrictions and "Supply Integrity Controls" against inconsistent bookable inventory | Binary date availability per unit ("bookable dates, blocks") | OTA overbooking is a counting and sync problem; hosted-stays double booking is a calendar-sync problem (external calendars are not modeled — §5) |
| **Supply connectivity** | Inbound and machine-driven: PMS and channel managers push rates and availability and receive reservations over "XML/JSON APIs" (`conn`, `invt`); KPIs "Reservation sync latency", "Overbooking incident rate" | Mostly human: hosts edit in-app; `apix` offers "Sync and export services" to operator tooling | OTA's source of truth for availability sits *outside* the platform; hosted stays' sits inside |
| **Supplier tooling** | One partner extranet (`extr`) plus reservation inbox (`rsrv`), merchandising (`prom`), rate recommendations (`rate`) | Host app surfaces spread across bricks; investment in activation (`hono`, `lista`) and operations (`opco`, `coho`) | OTA builds a B2B workspace for revenue managers; hosted stays builds a guided consumer-grade host app plus a pro layer |
| **Payment model** | Multiple: pay now, pay later, pay at property, platform-managed ("Payment Model Normalization"); partner settlement with commission deductions in a ledger (`sett`) | Platform always collects; holds funds; releases payout after check-in net of split service fees (rel-05; `paym` "Host payout ledger") | OTA must model agency vs merchant of record and receivables/payables per partner; hosted stays must model escrow-like holds, payouts to individuals, fee splits, and tax withholding |
| **Settlement** | Line-level settlement ledger, finance adjustments, "Ledger adjustment rate", "Finance reconciliation lead time" | Payout ledger inside `paym`; owner remittance by co-host operators off-model (rel-07) | Book should treat the ledger as a first-class domain in both, but its shape differs: partner invoices/commissions vs per-booking payouts |
| **Who operates the stay** | The hotel; the platform hands over the reservation | The host, a co-host, or a professional operator; cleaning and readiness are coordinated in-platform (`opco`) | Hosted stays extends into operations software (task engine, readiness state) |
| **Roles and delegation** | Partner users via `idam` roles | `coho` delegated permissions per listing; stressor `coho` separates owner, controller, licensed operator, co-host, service provider, payout beneficiary, tax party | Hosted stays needs a role/relationship model on the listing, not just user roles |
| **Protection and trust** | Verification, fraud and abuse scoring, integrity operations (`trst`); host "protection signals" only as a persona want | Reservation screening before confirmation (`book` → `trst`), damage and safety intervention workflow, claims in `reso` | Hosted stays needs a protection/claims domain (guarantee programme, damage claims, liability); OTA needs fraud and payment-risk controls |
| **Local regulation** | Not a brick; appears only in residuality `licn` (STR caps, invalid licenses) | `comp` Local Compliance & Policy Controls: market policy registry, listing eligibility, audit state | Both converge on effective-dated eligibility per unit, operator, jurisdiction and stay date (§10.3) |
| **Guest pre-booking behavior** | Saved searches and price alerts (`ssav`); deals and member pricing (`deal`) | Wishlists, sharing and group coordination (`wish`); categories (`insp`) | OTA optimizes price-watching intent; hosted stays optimizes social, group decision-making |
| **Reviews** | Verified reviews tied to completed bookings; partner remediation workflow (`rept`) | Two-sided reputation feeding conversion and host status (`grev`, `list`) | Both need booking-gated review eligibility; hosted stays adds host-to-guest signals (not modeled) |
| **Business travel** | Managed travel persona with policy and invoice jobs | Absent | OTA needs company accounts, policies and invoicing (not modeled as bricks — §5) |
| **Investment emphasis (`invest`)** | Checkout, partner merchandising, payments, marketplace intelligence | Listing trust, checkout, host activation and authoring, pricing, turnover ops, co-hosts, resolutions | OTA invests in monetization levers; hosted stays invests in supply creation and operations |

---

## 5. Gaps: domains a real architecture needs but neither model has as a brick

Each row is a **candidate addition** for the book's reference architecture. "Traces" lists where the models hint at the capability without owning it.

| Candidate capability | Traces in the models | Why the book needs it |
| --- | --- | --- |
| **Property, unit and room-type catalog (system of record)** | `cont`, `lista`, `invt` descriptions; residues `licn`/`insv` ("physical property and unit") | Neither data catalog has a property, unit, room-type or listing entity; every other capability needs one owner for "what is being sold" |
| **Rate plan and offer model** | `room` ("Room Plan Resolver", "Rate Condition Comparison"); residue "rate plan" | Rate plans (conditions, meal plans, cancellation, payment timing, derived/member rates) need their own model and API, not a UI brick |
| **Reservation system of record** | Split between `invt` "Reservation State Machine" and `book`; HSM `book` only | Stressor `insv` shows reservation truth must survive a failed distributor; the book must name one owner and its events |
| **Tax engine** (VAT, city/tourist/occupancy tax, remittance) | Traveler "Transparent prices, taxes"; HSM `paym` "tax flows"; host job "payouts, fees, taxes" | Taxes vary by jurisdiction, stay length and property type, and the platform may collect and remit them; this is a rules engine, not a payment module |
| **Fees and total-price calculation** | HSM Y1 "Unify total-price and cancellation explanation patterns"; insight hsm-05 | All-in price display (fees, taxes, discounts, currency) must be identical in search, listing page and checkout |
| **Channel manager / iCal sync for hosts** | HSM pro-host Y3 "Channel and partner sync becomes easier where appropriate"; `apix` exports only | Multi-channel hosts keep calendars in sync through iCal feeds or channel managers; double-booking risk lives here |
| **Content and property mapping / deduplication** | Residue `licn` "duplicate units"; residue `insv` "inventory mappings" | The same property can arrive from several sources (direct, channel manager, wholesaler); OTAs need mapping and dedup |
| **Third-party supply sourcing** (bedbanks, wholesalers, GDS, other OTAs) | Residue `insv` "connectivity distributor"; competitor note on B2B lodging | OTAs source inventory they do not contract directly; merchant/agency role per source matters |
| **B2B / affiliate distribution and demand API** | `DOMAIN.md`: "Connectivity and demand APIs expose accommodation search, availability … for ecosystem partners" | Selling inventory to affiliates, travel agents and partner sites is a separate API product with its own rate and commission rules |
| **Metasearch integration** | Managed-travel discovery: "travel search, metasearch" | Price feeds, landing-page parity and bid management for metasearch channels are a distinct acquisition domain |
| **Loyalty and member programme** | `acct` "loyalty-adjacent preferences"; `deal` "member programs"; `prom` "member rates" | Tiers, eligibility and member-only rates need a ledger and rules, not a merchandising treatment |
| **Notifications platform** | TAM `trip` "Message and Notification Routing"; `ssav` → `trip`; external Email and Push platforms | One preference-aware delivery service (email, push, SMS) across alerts, confirmations and disruption messages |
| **Customer data platform and consent management** | `consent-record` asset has no owning brick in either model | Consent, profile unification and audience building need an owner; the generated catalogs scatter ownership |
| **Company accounts, travel policy and invoicing** | TAM `cg2-p1` jobs and KPIs ("Invoice-ready booking rate") | Managed travel needs company entities, policy rules, invoice data and reporting |
| **Partner account and entity hierarchy** (chains, groups, legal entities, contracts) | `onbo` "business identity"; HSM `coho` roles | LISTED's GLM had `iess`; here neither model has a partner master record or contract/commission terms |
| **Partner CRM and market management** | Journey: "market-manager outreach" | Account managers, commission negotiation and partner health are an operating domain |
| **Sponsored visibility / advertising** | TAM Y3 revenue "Sponsored visibility and partner programs" | Paid placement must be modeled and labelled separately from organic ranking (regulatory explainability) |
| **Currency, FX and multi-currency pricing** | "currency" appears only in KPI units | Prices, payments and payouts cross currencies; rounding and FX exposure are a ledger concern |
| **Translation and localization of content and reviews** | TAM `geoa` "Localization and Market Context" | Global supply and reviews need translation pipelines and locale-aware content |
| **Availability/price cache for search** | TAM `srch` worker "Inventory Update Feed" | Search at scale cannot query live rates per result; a cache with freshness rules is a classic OTA component |
| **Damage deposits, protection programme and claims ledger** | HSM `trst` protection workflow; `reso` claims; KPI "Damage-case recovery time" | Guarantees, deposits and claim payouts are financial obligations with their own evidence and limits |
| **Check-in and property access** (lockboxes, smart locks, access codes) | HSM `trip` "check-in coordination"; `opco` readiness | Hosted stays without a front desk need an access-handover capability |
| **Platform regulatory reporting** (platform tax reporting, STR registry reporting, DSA trader data) | Links: EU DSA; residue `licn` "prove to the city which rule and permit governed every decision" | Regulators increasingly require platform-side reporting of hosts, earnings and permits |
| **Connected trip / packages** | TAM links: EU Package Travel Directive; `DOMAIN.md` "connected-trip motions" | Flights, cars and packages are out of scope in both models; the book should state that boundary explicitly |
| **Data platform** (event backbone, lakehouse, feature store) | `mkli`/`data` warehouses; no ingestion/platform brick | Ranking, pricing and fraud models depend on a governed data platform neither model owns |
| **Fraud and payment-risk separation** | TAM `trst` covers booking, payment and interaction fraud in one brick | Payment fraud (chargebacks, card testing) and marketplace fraud (fake listings, account takeover) usually split |
| **Model-specific gaps** | HSM lacks media pipeline, geo/localization, IAM, account/wallet, self-service changes; TAM lacks turnover ops, co-host roles, local compliance registry, wishlists | Each model's "only" bricks (§4.1) are gaps in the other |

---

## 6. Value streams (product streams)

Streams are "outcome-based" groupings that compose bricks and carry flows of steps. Both models have five streams with flow model version 3.2. **Only the first TAM stream has key facts and pain points**; the rest list steps and dependencies only.

### 6.1 TAM streams (5)

| Group | Stream ID | Name | Composed bricks | Outcomes | Steps (dependencies) |
| --- | --- | --- | --- | --- | --- |
| Traveler Journey | `discover-and-compare-stays` | Discover and Compare Stays | `home`, `dest`, `srch`, `mapb`, `pers`, `ssav`, `prop`, `mkli` | Higher search-to-book conversion; better traveler confidence before checkout | Enter destination intent (`dest`) → Filter and rank options (`srch`, `mkli`) → Inspect property confidence (`prop`) |
| Traveler Journey | `book-and-confirm-stay` | Book and Confirm Stay | `room`, `book`, `acct`, `conn`, `deal` | Higher checkout completion; lower avoidable support and dispute cost | Review booking terms (`book`) → Complete payment model (external PSPs) → Create confirmed reservation (`book`, `conn`: "synchronize booking state to partner systems when needed") |
| Traveler Journey | `manage-trip-and-recover-issues` | Manage Trip and Recover Issues | `trip`, `msgc`, `self`, `reve`, `trst` | Higher self-service issue resolution; lower support-driven trip failure | Review trip state (`trip`) → Escalate issue if needed (`trst`) → Close financial outcome (no dependency) |
| Partner Journey | `grow-partner-visibility-and-occupancy` | Grow Partner Visibility and Occupancy | `extr`, `onbo`, `cont`, `medi`, `cald`, `prom`, `rate`, `perf` | Higher visibility-adjusted occupancy; clearer commercial decision-making | Configure property basics (`extr`) → Adjust visibility levers (`prom`) → Evaluate profitability (no dependency) |
| Partner Journey | `operate-partner-reservations-and-payouts` | Operate Partner Reservations and Payouts | `invt`, `rsrv`, `paym`, `sett`, `rept`, `supp` | Lower partner support burden; higher payout confidence and reservation accuracy | Receive and confirm reservations (`invt`: "create and maintain operational booking truth") → Resolve guest quality events (`rept`, `supp`) → Reconcile financial outcome (`paym`: "close commissions, remittance, and dispute adjustments") |

Not in any stream: `geoa`, `idam`. Stream metadata sources point at Booking.com public pages (how-we-work, partner join page, demand API docs).

**Quotable key facts and pain points (discover stream only):**
- "Travelers often start with broad place and date intent, not a specific property." Pain: "Users abandon when the marketplace does not feel location-aware."
- "Ranking quality is central to perceived marketplace quality." "Search results need to reflect policy, budget, and quality expectations." Pain: "**Hidden commercial logic can make partners and travelers feel the system is opaque.**"
- "Property-page quality often determines whether search interest turns into checkout." "Travelers need policy and review clarity, not just photos and price." Pain: "Incomplete policy detail creates support and cancellation risk later."

### 6.2 HSM streams (5)

| Group | Stream ID | Name | Composed bricks | Outcomes | Steps |
| --- | --- | --- | --- | --- | --- |
| Guest Journey | `discover-and-shortlist-stays` | Discover and Shortlist Stays | `insp`, `srch`, `list`, `wish`, `data` | Higher guest search-to-book conversion; lower booking regret | Start from trip intent (`insp`) → Rank and compare options (`srch`, `data`) → Judge trust and fit (`list`) |
| Guest Journey | `book-and-manage-a-stay` | Book and Manage a Stay | `book`, `paym`, `trip` | Higher checkout completion; lower avoidable support contacts | Complete booking (`book`, `paym`) → Coordinate the trip (`trip`) |
| Host Journey | `launch-a-new-host` | Launch a New Host | `hono`, `lista`, `cala`, `pric` | Faster time to first booking; higher quality of newly activated supply | Activate and verify (`hono`) → Author the listing (`lista`) → Make the listing bookable (`cala`, `pric`) |
| Professional Host Journey | `operate-a-host-portfolio` | Operate a Host Portfolio | `coho`, `opco`, `host`, `apix` | Higher portfolio occupancy and margin; lower operating overhead per listing | Delegate and control (`coho`) → Execute operations (`opco`) → Optimize performance (`host`) |
| Trust and Support | `recover-issues-and-protect-the-marketplace` | Recover Issues and Protect the Marketplace | `idvr`, `trst`, `reso`, `comp` | Lower support cost leakage; higher trust and host retention | Detect and screen risk (`idvr`, `trst`) → Resolve financial and support impact (`reso`) |

Not in any stream: `grev`. No key facts or pain points.

### 6.3 Stream comparison

| Concern | TAM | HSM |
| --- | --- | --- |
| Discovery | Discover and compare (destination-led, map, deals) | Discover and shortlist (category-led, wishlists) |
| Booking | Book and confirm — includes room/rate selection and partner sync | Book and manage — booking, payment and trip in one stream |
| Post-booking | Manage trip and recover issues (traveler stream) | Recovery sits in a separate trust-and-support stream |
| Supply activation | Inside "Grow partner visibility and occupancy" | Its own "Launch a new host" stream |
| Supply operations | Operate partner reservations and payouts | Operate a host portfolio (co-hosts, turnover, performance) |
| Money | Partner reservations and payouts stream holds settlement | Payment sits in the guest booking stream; payouts implicit in `host` |
| Trust | Inside traveler post-booking stream | Its own stream, with local compliance |
| Platform streams | None | None |

---

## 7. Data assets: entities, ownership, sensitivity

### 7.1 How data assets are modeled

Same schema as the LISTED models: each asset has `id`, `name`, `kind` (`logical-object`, `reference-data`, `document`, `event`, `derived-metric`), `description`, `businessMeaning`, `classification` (`internal`, `confidential`, `restricted`), `personalDataLevel` (`none`, `personal`, `sensitive`), `dataSubjects`, `legalTags` (`gdpr`, `pci`), optional `securityCriticality`, `authenticationMaterial`, `systemOfRecordBrickId`, `stores` (with role) and `interfaces`, and `governance` (retention, residency, sharing). Stores carry `kind` and `technology`.

**Both catalogs are generator output ("Starter catalog of key business, PII, and security-sensitive data assets", model version 1.0).** Every store's technology is `generated-starter`; every residency is `eu` (for global marketplaces); brick-derived assets carry the boilerplate meaning "Reusable domain data centered on <brick name>". Unlike LISTED's REM model, **there is no hand-written core entity** — no property, unit, room type, rate plan, availability, reservation, review, listing, partner account, payout or license.

### 7.2 TAM data assets (17)

| Asset ID | Kind | SoR brick | Class. / personal | Legal | Store (kind) | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `customer-profile` | logical-object | — | restricted / personal; high | gdpr | operational-database | Owned by `acct`, `sett` and `supp` (three owners) |
| `customer-contact-point` | logical-object | — | restricted / personal; high | gdpr | operational-database | Written by `acct`, `sett`, `supp` |
| `identity-credential` | logical-object | — | restricted / sensitive; critical; password | gdpr | operational-database | Read by `onbo`, `idam` |
| `session-token` | logical-object | — | restricted / sensitive; critical; token | gdpr | cache | Owned by `onbo` and `idam` |
| `access-policy` | reference-data | — | restricted / none; critical | — | operational-database | Owned by `onbo` and `idam` |
| `consent-record` | logical-object | — | restricted / personal; high | gdpr | operational-database | Read by `acct`, `sett`, `supp`; **no owner** |
| `audit-log` | event | — | restricted / personal; critical | gdpr | event-topic | Published by `room`, `book`, `self`, `onbo`, `rsrv`, `paym`, `mkli`, `idam` |
| `payment-instrument-reference` | logical-object | — | restricted / sensitive; critical; token | gdpr, pci | operational-database | Read by `room`, `book`, `acct`, `paym`, `sett` |
| `transaction` | logical-object | — | confidential / personal; high | gdpr | operational-database | Written by `room`, `book`, `paym`; read by `mapb`, `medi`, `prom`, `perf`, `rept`, `conn` |
| `marketplace-home-destination-landing` | logical-object | `home` | internal / none | — | operational-database | Brick-derived |
| `destination-discovery` | logical-object | `dest` | internal / none | — | operational-database | Brick-derived |
| `search-ranking-filters` | reference-data | `srch` | internal / none | — | operational-database | Brick-derived; read by `home`, `dest`, `pers`, `ssav`, `mkli`, `geoa` |
| `traveler-account-wallet` | document | `acct` | restricted / sensitive | gdpr | blob-store | Read by 8 bricks |
| `personalization-recommendations` | derived-metric | `pers` | confidential / personal | gdpr | feature-store | Queried by `rate` |
| `saved-searches-price-alerts` | event | `ssav` | internal / **none** | — | event-topic | Stored per-user intent classified non-personal (wrong) |
| `trip-management-messaging` | logical-object | `trip` | confidential / personal | gdpr | operational-database | Read by 12 bricks |
| `checkout-booking-orchestration` | **reference-data** | `book` | confidential / personal | gdpr | operational-database | The only reservation-like asset, mis-kinded as reference data; read by `prop`, `room`, `trip`, `reve`, `invt`, `cald`, `rsrv`, `paym`, `trst` |

### 7.3 HSM data assets (17)

| Asset ID | Kind | SoR brick | Class. / personal | Legal | Notes |
| --- | --- | --- | --- | --- | --- |
| `customer-profile`, `customer-contact-point`, `identity-credential`, `session-token`, `access-policy`, `consent-record`, `audit-log`, `payment-instrument-reference`, `transaction` | as TAM | — | as TAM | as TAM | Same generic platform assets. `session-token` and `access-policy` are "owned" by `insp`, `lista` and `idvr`; `transaction` written by `book`, `paym`, read by `apix` |
| `search-ranking-map-browse` | logical-object | `srch` | internal / none | — | Read by `data` |
| `wishlists-sharing` | logical-object | `wish` | confidential / personal | gdpr | No reader |
| `guest-reviews-re-engagement` | logical-object | `grev` | confidential / personal | gdpr | Read by `srch`, `wish`, `trip`, `trst`, `paym`, `apix` |
| `pricing-discounts` | reference-data | `pric` | internal / none | — | Read only by `data` — **checkout never reads price** |
| `listing-authoring-content` | document (blob-store) | `lista` | internal / **none** | — | Read by `list`, `hono`, `coho`, `host`, `comp`; classified non-personal although host listings carry addresses, house photos and host details |
| `booking-checkout` | reference-data | `book` | restricted / sensitive (no subjects) | gdpr | Read by `list`, `wish`, `grev`, `cala` |
| `calendar-availability` | reference-data | `cala` | confidential / personal (no subjects) | gdpr | **No reader** — `book` and `srch` never read availability |
| `turnover-operations-coordination` | reference-data | `opco` | internal / none | — | Read by `trip`, `coho`; grouped under "Architecture, Portfolio, and Planning Data" (misfiled) |

### 7.4 Core entities the book must reconstruct (synthesis)

Assembled from brick and module descriptions, KPIs and residuality residues. Each line names its source.

- **Property** (both): physical property; address and jurisdiction; owner; operating partner (residues `licn`, `insv`; HSM `coho` residue: "property owner, listing controller, licensed operator"). Hotel vs home vs room is a property type (TAM `cg4-p1`, rel-02).
- **Unit / room type** (TAM `room`, `invt`; residue "rentable unit", "physical property and unit"): the thing a night is sold on. For hotels, a room type with an inventory count; for homes, usually one unit.
- **Rate plan** (TAM `room` "Rate Condition Comparison": cancellation, payment, meal-plan differences; residue "rate plan", "rate source"): conditions, derived and member rates (`deal`, `prom`), restrictions (`cald` "minimum-stay, arrival, departure, and booking-window controls").
- **Availability assertion** (TAM residue: "availability assertion", "inventory assertion" from a "connectivity source"): availability is a *claim made by a source*, not a fact — the key insight of stressor `insv`.
- **Listing** (HSM `lista`, `list`; residues): the published offer, separate from the property and from "whether a particular stay may currently be sold" (HSM `licn` residue on `lista`).
- **License / permit** (both residues): license, license holder, eligibility evidence, rule version, effective interval, appeal, reinstatement.
- **Reservation** (TAM `invt` "Reservation State Machine", `book`, `rsrv`; residues): reservation request, source acknowledgement, property confirmation, traveler contract, modifications, cancellation, no-show; "confirmation evidence".
- **Stay obligation** (TAM residue `fire`: "Recovery is organized around the traveler obligation rather than the original room"; HSM `evac`: "guest commitment stays separate from the replaceable property that fulfills it").
- **Money** (TAM `paym`, `sett`, residue `insv`): payment instruction, merchant of record, charge, safeguarded funds, partner receivable, distributor payable, payout route, refund obligation, claim; HSM residue `coho`: payout beneficiary, fee recipient, tax party, financial splits.
- **Roles** (HSM `coho`): owner, listing controller, licensed operator, co-host, service provider, guest contact, permit holder, payout beneficiary, fee recipient, tax party — "separate effective roles".
- **Review** (TAM `reve`, `rept`; HSM `grev`): booking-gated eligibility, verification, moderation, remediation.
- **Disruption / operating state** (TAM `fire` residue on `geoa`: "disruption boundaries"; HSM `evac`: "destination operating state … versioned emergency policy").
- **Turnover task** (HSM `opco`): changeover, cleaning, readiness per reservation.

### 7.5 What the data layer teaches (for the modeling chapters)

- **A generated catalog that misses the domain's core is worse than none.** Neither catalog contains property, rate plan, reservation or review; ownership of profile, session and policy assets is scattered across unrelated bricks. Use this as a cautionary example, as LISTED did with REM's classification errors.
- **Classification errors repeat:** listing content and saved searches marked non-personal; calendar and checkout records marked personal but with no data subjects.
- **Missing reads reveal missing dependencies:** HSM `calendar-availability` and `pricing-discounts` are not read by checkout or search — the same gaps the brick graph shows (§3.5).

---

## 8. Products and deployments (how capabilities are packaged)

### 8.1 Product portfolios

Products are given in `products.json`; brick assignments come from `usedInProducts` in `deployment.json` (only deployed bricks are assigned).

**TAM — "Travel Accommodations Marketplace Platform" v1.0 (3 products):**

| ID | Product | Type | Primary customers | Bricks (from deployment) |
| --- | --- | --- | --- | --- |
| `p1` | Traveler Discovery and Booking Experience | B2C | `cg1-p1`, `cg2-p1` | `srch`, `book`, `paym`, `dest`, `prop`, `trip` |
| `p2` | Partner Supply and Performance Workspace | B2B | `cg3-p1`, `cg4-p1` | `invt`, `mkli`, `extr`, `prom` |
| `p3` | Partner Connectivity and Marketplace Sync | B2B2C | `cg3-p1` | `invt`, `conn` |

`supp`, `trst`, `rept` are deployed to the internal operations console with no product. **Connectivity is its own product** (`p3`), with `invt` shared between the partner workspace and connectivity — a defensible packaging statement.

**HSM — "Hosted Stays Marketplace Platform" v1.0 (3 products):**

| ID | Product | Type | Primary customers | Bricks (from deployment) |
| --- | --- | --- | --- | --- |
| `p1` | Guest Discovery and Booking Experience | B2C | `cg1-p1` | `srch`, `book`, `trip`, `trst`, `insp`, `list` |
| `p2` | Host Setup and Listing Studio | B2B2C | `cg2-p1` | `paym`, `lista`, `host`, `cala` |
| `p3` | Professional Host and Co-host Operations | B2B | `cg3-p1` | `reso`, `host`, `coho`, `apix` |

`comp` is deployed with no product. `paym` is attributed only to the host studio ("Supports payouts, taxes, and fee visibility").

### 8.2 Deployment channels

Both models use the same channel taxonomy: a core cloud runtime plus ten numbered `cloud-01`…`cloud-10` runtimes (identical replicas — read as per-region or per-market runtimes, but generated), `web-cdn-edge`, iOS and Android app stores, `partner-api-gateway`, and an `internal-ops-console`.

| Channel | TAM bricks (deployment role) | HSM bricks (deployment role) |
| --- | --- | --- |
| Core + 10 cloud runtimes | `srch` (search, ranking, availability service packages), `book` (reservation orchestration), `invt` (supply core services and workers), `paym` (payments and reconciliation), `supp`, `conn` (partner gateway and sync services), `mkli` (decisioning and insight) | `srch`, `book` (reservation and checkout services), `trip` (messaging and trip state), `paym` (payment, tax and payout services), `trst` (risk, protection and trust services), `reso` |
| Web CDN edge | `dest`, `srch`, `prop`, `extr`, `prom` | `insp`, `list`, `lista`, `host`, `coho` |
| iOS / Android | `dest`, `srch`, `book`, `trip` | `insp`, `book`, `trip`, `cala` ("Host … calendar controls") |
| Partner API gateway | `conn`, `book`, `invt` ("Primary API exposure surface for partner connectivity and demand APIs") | `apix`, `book`, `host` ("Portfolio sync, exports, and partner integration APIs") |
| Internal ops console | `supp`, `trst`, `rept` | `trst`, `reso`, `paym`, `comp` ("Market-rule and policy enforcement controls") |

TAM deploys 14 of 34 bricks; HSM deploys 14 of 21. Nothing in either model is deployed for `pers`, `rate`, `geoa`, `idam` (TAM) or `idvr`, `data`, `pric`, `opco` (HSM) — generator truncation, not design intent.

### 8.3 Packaging lessons (synthesis)

- Products are cut by **side of the marketplace** (guest, small supply, professional supply) and, in TAM, by **connectivity** as a product in its own right.
- The mobile app is the guest's primary surface in both; HSM also puts a **host calendar** in the app, signalling that hosts run their business from a phone.
- The partner API gateway faces different directions: TAM exposes supply and demand APIs; HSM exposes operator exports.
- Internal operations consoles carry trust, support and (HSM) payouts and compliance — the operating teams the personas never name.

---

## 9. Competition and business model notes (model content, not verified fact)

Everything in this section is **as recorded in the models**. Competitor statistics were stated by the model authors to come from official investor or company pages; they have not been re-verified here and must be checked against the primary source before any use in the book. Strategy and monetization statements are the model's hypotheses about a generic operator.

### 9.1 TAM competitive landscape (`competition.json`, generated 2026-04-18)

Scope: "Global accommodations marketplaces relevant to a domain modeled on hotel, apartment, vacation-rental, and partner distribution workflows across leisure and managed travel stays." Note: "Some players report company-wide travel metrics rather than accommodations-only metrics. Those are preserved as reported and labeled with their scope."

| ID | Player | Category | Recorded stats (period, scope) |
| --- | --- | --- | --- |
| `booking_holdings` | Booking Holdings / Booking.com | category_leader | Gross travel bookings $166bn (FY2024, company); room nights booked 1.1bn (FY2024, lodging); listings 31m+ and properties ~4m (accessed 2026-04-18, booking.com) |
| `expedia_group` | Expedia Group | scaled_global_challenger | Gross bookings growth 7% and revenue growth 7% (FY2024, company); booked room nights growth 9% (FY2024, lodging); lodging gross bookings growth 12% (Q4 2024) |
| `airbnb` | Airbnb | alternative_accommodations_leader | Revenue $11bn+ (FY2024); nights and experiences booked 491m+ (FY2024); GBV $82bn (FY2024); listings 8m+ (Q2 2024) |
| `tripcom_group` | Trip.com Group | asia_global_challenger | Net revenue RMB53.3bn (FY2024); accommodation reservation revenue RMB21.6bn (FY2024); international OTA hotel and air bookings growth 70%+ (Q4 2024); corporate travel revenue RMB2.5bn (FY2024) |

### 9.2 HSM competitive landscape (generated 2026-04-18)

| ID | Player | Category | Recorded stats |
| --- | --- | --- | --- |
| `airbnb` | Airbnb | category_leader | Same four stats as TAM |
| `vrbo_expedia` | Vrbo / Expedia Group | vacation_rental_challenger | Expedia Group lodging stats only (room nights +9% FY2024; lodging GB +12% Q4 2024; company GB +7% FY2024) — no Vrbo-specific figure |
| `bookingcom_homes` | Booking.com Homes and Apartments | hybrid_hotel_and_homes_competitor | Alternative accommodations 3.5m; reported listings **~29m** (both accessed 2026-04-18); room nights 1.1bn (FY2024, parent) |
| `tripcom_group` | Trip.com Group | asia_growth_competitor | Accommodation revenue RMB21.6bn; international OTA bookings growth 70%+; inbound travel bookings growth 100%+ (Q4 2024) |

**Inconsistency to resolve before citing:** TAM records Booking.com listings as "31m+" and HSM as "~29m", both from the same factsheet and the same access date. Neither model lists a European or regional vacation-rental specialist, a hotel chain's direct channel, metasearch, or a channel-manager vendor as a competitor.

### 9.3 Figures in `DOMAIN.md` (as recorded; re-verify)

- **TAM** (from Booking.com "How we work", updated 31 May 2025, as summarized by the model): the platform provides the service while the provider delivers the stay; payments may happen at the property, be charged in advance by the property, or be organized by the platform or an affiliate; recommendations are influenced by "popularity, conversion, quality, commission, payouts, availability, and participation in programs"; reviews come from customers who booked and are "generally shown for 36 months". Partner pages: supply spans hotels, apartments, holiday homes, guest houses, B&Bs; hosts can choose instant booking or request to book; "daily payouts".
- **HSM** (as summarized by the model): over 5 million hosts and over 2 billion guest arrivals (Feb 2025); Q4 2025 app share 64% of nights booked and pay-later adoption above 70% of eligible bookings; over 1.3 million hosts reached the top-host status; host protection includes $1 million liability insurance and up to $3 million damage protection; fees "about 3% host fee and roughly 14.1% to 16.5% guest fee in eligible setups" (fee guidance updated 25 Aug 2025).

### 9.4 Business model as modeled

**TAM `DOMAIN.md` "five connected value pools":** (1) traveler demand capture through destination discovery, trust and high-conversion search; (2) booking conversion through transparent policies, pricing, payments and low-friction checkout; (3) stay confidence through reviews, support, self-service changes and disruption recovery; (4) partner yield and supply quality through pricing, availability, merchandising and payout operations; (5) platform defensibility through trust, payments, connectivity and marketplace intelligence. Revenue streams in horizons: accommodation commission; payments-related monetization and fintech services; sponsored visibility and partner programs; enterprise travel programs. Insight `tam-02` (sourced) notes that ranking reflects commission and program participation; insight `tam-03` that "Payment operating model flexibility is a product requirement, not a back-office detail".

**HSM `DOMAIN.md` hypothesis:** (1) guest conversion depends on search relevance, distinctive listing quality and trust signals; (2) host supply quality depends on fast activation, simple calendar/pricing control and confidence in payout, protection and support; (3) professional host growth depends on operational tooling, co-host permissions and multi-listing management; (4) defensibility depends on identity, risk screening, protection, payments, policy enforcement and data-driven ranking; (5) growth beyond the core still "starts with bookable nights, high-quality listings, and reliable host economics". Revenue streams in horizons: stay service fees (guest fee, host fee); payments and incentive optimization; repeat demand.

---

## 10. Residuality stressors and architectural implications

Both models include a residuality stress test explicitly based on Barry M. O'Reilly, *Residues: Time, Change, and Uncertainty in Software Architecture* (Leanpub, 2024). Each stressor has `detection`, `attractor`, `businessReaction`, `residue`, status (`integrated`, `candidate`, `already-survived`) and ten impacts (vision, job, journey step, KPI, product, stream, three bricks, competitor benchmark). **These are the strongest content in both models** and map directly onto the book's domain-modeling and resilience chapters. HSM adds a caveat worth keeping: "An integrated change means included in the adapted model, not a claim about a particular marketplace's production implementation."

### 10.1 TAM

**Naive architecture (as modeled):** "A property or connectivity partner publishes content, rates, and availability; a traveler books a room or home; the marketplace confirms the reservation, processes or coordinates payment, sends the booking to the accommodation, and later pays the partner or records payment at the property. The design assumes the property remains licensed and habitable, the inventory source remains authoritative, and the reservation and money path stay available through the stay."

**Residual architecture:** "separates physical property and unit, owner, operating partner, connectivity source, license and jurisdiction, content, rate plan, availability assertion, reservation, confirmation evidence, traveler intent, stay obligation, disruption, replacement option, payment instruction, merchant, safeguarded funds, partner receivable, payout route, refund, communication, and final outcome. A property can lose permission or availability without losing the traveler commitment, and a failed distributor can be replaced without erasing reservation or financial rights."

| ID | Stressor | Residue (what must be separated) | Bricks changed | Status |
| --- | --- | --- | --- | --- |
| `licn` | "Cities impose short-term-rental caps and invalidate thousands of existing property licenses" | physical property, rentable unit, owner, operating partner, address and jurisdiction, license, license holder, eligibility evidence, rule version, effective interval, appeal, listing, content, availability, reservation, traveler notice, replacement, refund, enforcement action, reinstatement. "**Bookability is evaluated per unit, operator, jurisdiction, and stay date.**" Attractor: "Removing the listing does not resolve confirmed travelers, collected money, partner obligations, duplicate units…" | `onbo` (separates host identity, ownership, operating authority, unit, license, evidence), `cont` (versions policies and permit disclosures), `invt` ("Publishes rates and availability only for eligible unit, operator, jurisdiction, and stay-date combinations") | integrated |
| `fire` | "A fast-moving wildfire closes a destination and displaces travelers already staying there" | traveler and party, intent, current location and contact, accessibility or care need, reservation, stay phase, property status, authoritative disruption zone, access route, partner confirmation, safety action, replacement requirement, candidate stay, transport constraint, choice, cancellation, refund, partner compensation, welfare follow-up, outcome. "**Recovery is organized around the traveler obligation rather than the original room.**" | `self` (disruption-specific actions), `supp` (prioritize current-stay safety), `geoa` ("Versions disruption boundaries, property and traveler exposure, route access") | integrated |
| `insv` | "A major connectivity distributor becomes insolvent with reservations and prepaid funds in flight" | property and unit, operating partner, distributor, connectivity account, inventory assertion, rate source, reservation request, source acknowledgement, property confirmation, traveler contract, **merchant of record**, charge, safeguarded fund, partner receivable, distributor payable, payout route, refund obligation, replacement source, claim, outcome. "**Reservation and economic truth survive the distributor account.**" Attractor: "A booking reference can exist without a room held at the property." | `conn` (versions source mappings, acknowledgements, gaps, migration, direct replacement), `rsrv` (separates source request, property confirmation, traveler contract), `sett` (obligations independent of distributor balances and payout routes) | integrated |
| `strd` | Combined: "A managed traveler is evacuated from an unlicensed home booked through the insolvent distributor" | **Already survived** — "license-to-unit records block the ineligible property, traveler-centered disruption recovery selects a safe replacement, and provider-independent reservation and ledger records preserve service and money rights despite distributor failure. One managed-trip case coordinates the existing parts." | `trip` (itinerary versions, coordinator choices, policy exceptions), `paym` ("Prevents duplicate collection"), `trst` (combines property, operator, license, distributor, reservation and payment evidence) | already-survived (reuses `licn`, `fire`, `insv`) |

Notable KPI impacts: "Verification completion requires current property-operation authority for the stay dates offered"; "Avoidable cancellation distinguishes unavoidable closure from failures to offer a safe reachable replacement"; "Payout predictability follows recognized property service and protected obligations across provider replacement"; "Business-trip rebooking succeeds only when the traveler has a safe confirmed stay and all obligations have an owner".

### 10.2 HSM

**Naive architecture:** "A host verifies an account, publishes a home with one calendar and price, and accepts a booking from a guest. The marketplace assumes that the listing remains legal and usable, that the host is the owner and operator, and that the booked property will fulfill the stay."

**Residual architecture:** "Instead of binding the listing, property, legal permission, operating host, owner, payout recipient, booking, and physical stay into one record, the adapted design manages them separately over time. Eligibility can change without erasing a listing, roles and money can be assigned explicitly, and a guest commitment can move to a safe replacement or refund path when the original property can no longer fulfill it."

| ID | Stressor | Residue | Bricks changed | Status |
| --- | --- | --- | --- | --- |
| `licn` | "A city changes short-term-rental permission street by street with 48 hours' notice" | property, listing, address, owner, operator, permit, zone rule, booking eligibility, stay date, marketplace decision. "**Effective-dated policy evaluates each proposed or existing stay**; a listing remains visible to its owner with an explained restricted state." Business reaction: "prove to the city which rule and permit governed every decision". | `comp` (versions local rules, evaluates against property, operator, permit, dates, stay terms), `lista` (content separate from sellability), `cala` ("Blocks only the dates and stay shapes that the effective permission makes ineligible") | integrated |
| `evac` | "Wildfire makes an entire destination unsafe during active stays" | "Represent a **destination operating state** separately from each listing and booking. A versioned emergency policy carries geography, time, severity, affected trip phases, communication, safety actions, relocation eligibility, payment treatment, and evidence; guest commitment stays separate from the replaceable property that fulfills it." | `trip` (safety state, replacement itinerary), `reso` (one recovery case), `paym` (emergency assistance, protected funds, delayed responsibility) | integrated |
| `coho` | "Cities require every remote owner to appoint a locally licensed operating host" | "Model property owner, listing controller, licensed operator, co-host, service provider, guest contact, permit holder, payout beneficiary, fee recipient, and tax party as **separate effective roles**. Bookings and tasks resolve to the responsible role, while permissions, evidence, obligations, and financial splits remain independently revocable and auditable." Attractor: "Informal password sharing and payout workarounds become both unsafe and illegal." | `coho` (verified role, scope, duty, service level, revocation), `idvr` ("Verifies people and organizations against the role they claim"), `paym` ("Allocates fees, payouts, withholding, and tax evidence to the correct legal and economic parties") | **candidate** (not yet integrated) |
| `midt` | "A city suspends all active stay permits and requires guests to relocate within twelve hours" | **Already survived** — "effective-dated eligibility identifies the precise stays whose permission changed, and the destination recovery model moves each guest commitment to a safe replacement, assistance, or refund path while preserving the original booking, evidence, and later financial decision." | `comp` (applies order to active stays by address, permit, effective time), `reso`, `paym` | already-survived (reuses `licn`, `evac`) |

### 10.3 Architectural implications (synthesis)

1. **Both models converge on the same separation from opposite starting points.** TAM starts from hotel distribution and ends with "physical property and unit, owner, operating partner, connectivity source, license"; HSM starts from one-host-one-home and ends with "property, listing, … owner, operator, permit". The book's core domain model should be one model for both: **property ≠ unit ≠ listing ≠ permission ≠ operator ≠ owner ≠ reservation ≠ stay obligation ≠ money route**.
2. **Bookability is a computed, effective-dated decision**, evaluated per unit, operator, jurisdiction and stay date (`licn` in both), not an active/inactive flag on the listing.
3. **Availability is an assertion from a source** (TAM `insv`). The OTA must record which source asserted it and what was acknowledged, so reservation truth survives the source.
4. **The traveler's commitment, not the room, is the unit of recovery** (TAM `fire`, HSM `evac`). A booking can be fulfilled by a replacement property; refunds, compensation and partner responsibility are decided later.
5. **Money has explicit parties and routes:** merchant of record, safeguarded funds, receivables and payables per party, payout beneficiary, fee recipient, tax party. This is where OTA (merchant/agency, distributor payables) and hosted stays (owner/operator splits, withholding) differ in detail but share the structure.
6. **Destination operating state is a first-class object** (versioned emergency policy with geography and time), separate from every listing and booking.
7. **Combined stressors are survived by a case that composes existing residues** (`strd`, `midt`) — the same test LISTED used to show a decomposition is right.
8. **Roles are relationships with scope and revocation** (HSM `coho`), which is why a co-host capability is more than a user-permissions screen.

---

## 11. Insights and links worth carrying into the book

### 11.1 TAM insights (`insights.json`, 6 items, all sourced to Booking.com or Booking Holdings pages)

- `tam-01` (high) Accommodation economics hinge on traveler conversion and partner take-rate → keep discovery, checkout and partner merchandising connected.
- `tam-02` (high) "Ranking, review quality, and program participation shape partner visibility" → "Partner tools must connect pricing, availability, content, reviews, and merchandising rather than treating them as separate surfaces."
- `tam-03` (high) "**Payment operating model flexibility is a product requirement, not a back-office detail**" → treat payment orchestration, payout transparency and cancellation handling as first-class.
- `tam-04` (medium) Alternative-accommodation hosts need simpler control → "Design home-host tools for clarity, defaults, and automation rather than hotel-style control depth everywhere."
- `tam-05` (medium) "Managed travel buyers need consumer-grade choice with policy-grade controls" → layer policy, invoicing and reporting on the same supply and checkout foundation.
- `tam-06` (high) "**Connectivity is core to supply scale and quality**" → "Keep connectivity, reservation sync, and validation tooling close to partner quality and overbooking risk controls."

### 11.2 HSM insights (5 items, sourced to Airbnb investor, SEC and resource-centre pages)

- `hsm-01` (high) Hosted stays remain the core economic engine → prioritize guest conversion, supply quality and booking reliability.
- `hsm-02` (high) "**Host trust and protection are product features, not policy footnotes**" → own trust, protection and recovery "with product rigor, not only operations tooling".
- `hsm-03` (high) "Pricing and availability discipline are central to host monetization" → "Keep calendar, pricing, promotions, and listing responsiveness in one host-performance loop."
- `hsm-04` (high) Casual hosts and professional operators coexist → separate personas "while reusing the same marketplace core".
- `hsm-05` (high) "Service-fee structure means payout transparency and all-in guest price clarity both matter" → "Treat fee explanation, taxes, payout timing, refunds, and incentives as one monetization system."

### 11.3 Links files (updated 2026-06-17)

TAM links: Booking.com, Expedia Group brands, Airbnb (reference marketplaces); Booking.com "How we work" and Booking Holdings IR (industry context); Booking.com partner join page and **developers.booking.com** connectivity and demand APIs (partners); **EU Digital Services Act** and **EU Package Travel Directive** (trust and regulation). HSM links: Airbnb, Vrbo, Booking.com homes (reference platforms); Airbnb IR Q4/FY2024, Airbnb newsroom, Booking Holdings factsheet (industry); host protection page; pricing-tools and top-host pages (hosts and operators). The research briefs should verify these sources independently.

---

## 12. Implications for the book (synthesis)

### 12.1 Reusable patterns across stays marketplaces

1. **One guest spine, two supply sides.** Discovery, listing/property page, checkout, trip, reviews, payments, trust and support are shared; supply-side capabilities diverge (§4).
2. **A single supply system of record with search as a projection.** Neither model names it cleanly; the book should (property/unit/listing catalog + rate/availability store + search cache).
3. **Inventory truth may live outside the platform** (OTA) or inside it (hosted stays), and the architecture changes with that: sync, acknowledgements, integrity controls and overbooking handling vs calendar edits and external-calendar sync.
4. **The offer is composed at request time** in OTAs (room × rate plan × occupancy × conditions × member treatment); in hosted stays the price is computed from host rules (nightly price, length-of-stay discounts, fees, taxes).
5. **Price transparency is a cross-cutting correctness property** (traveler "Transparent prices, taxes, and cancellation rules"; HSM "all-in pricing"): one pricing and fee service must feed search, page and checkout.
6. **Payment model is a domain choice, not an integration** (`tam-03`): merchant vs agency vs pay-at-property in OTAs; collect-hold-release with fee splits in hosted stays.
7. **Ledger and settlement are first-class** — TAM settlement ledger; HSM payout ledger; both residuals add receivables, payables and beneficiaries.
8. **Trust is layered:** identity verification, reservation screening, fraud, review integrity, protection programmes and claims, local compliance.
9. **Recovery is a product,** not a support afterthought: self-service changes, disruption zones, replacement stays, compensation.
10. **Partner tooling is a B2B product** (extranet, connectivity, analytics in TAM; host app, co-hosts, operations in HSM).
11. **Effective-dated eligibility** (licensing) and **destination operating state** (disasters) are residues both models arrive at.
12. **Professional supply converges the two models:** a professional operator on a hosted-stays platform needs connectivity, portfolio pricing and exports — the hotel-like capabilities; a home host on an OTA needs simple defaults and protection — the hosted-stays capabilities.

### 12.2 Coverage checklist for chapter planning

Use §3.2–§3.3 as the brick checklist (55 bricks: 34 TAM + 21 HSM) and §5 as the list of capabilities to add from the research briefs. Suggested mapping of model content to book parts (to be reconciled with the book outline):

| Book area | TAM bricks | HSM bricks | Gaps to fill (§5) |
| --- | --- | --- | --- |
| Discovery, search and ranking | `home`, `dest`, `srch`, `mapb`, `pers`, `ssav`, `deal`, `prop` | `insp`, `srch`, `wish`, `list` | Availability/price cache, sponsored visibility, metasearch, translation |
| Offer, pricing and checkout | `room`, `book`, `acct` | `book`, `pric` | Rate plan model, fees and total price, tax engine, currency/FX, loyalty |
| Supply onboarding and content | `extr`, `onbo`, `cont`, `medi` | `hono`, `lista` | Property/unit catalog, content mapping and dedup, partner entity hierarchy |
| Inventory, calendar and connectivity | `invt`, `cald`, `conn` | `cala`, `apix` | Reservation SoR, channel manager/iCal sync, third-party supply sourcing |
| Partner and host operations | `rsrv`, `prom`, `rate`, `perf` | `opco`, `coho`, `host` | Check-in/access, partner CRM and market management |
| Post-booking, trips and recovery | `trip`, `msgc`, `self`, `supp` | `trip`, `reso` | Notifications platform, disruption/destination state |
| Reviews and reputation | `reve`, `rept` | `grev` | Host-to-guest reviews |
| Payments, settlement and finance | `paym`, `sett` | `paym` | Ledger design per payment model, deposits and claims ledger, regulatory reporting |
| Trust, safety and compliance | `trst` | `idvr`, `trst`, `comp` | Licensing registry for OTAs, fraud vs payment-risk split, DSA trader data |
| Data and intelligence | `mkli` | `data` | Data platform, CDP and consent |
| Platform foundations | `geoa`, `idam` | — | IAM for hosted stays, geo/localization |
| Distribution beyond the marketplace | `conn` (supply side only) | — | B2B/affiliate demand API, metasearch, connected trip boundary |
| Business travel | (persona only) | — | Company accounts, policy, invoicing |

### 12.3 Rules for writers

- Describe the reference architecture as a **fictional operator** built from these models plus the research briefs. Do not attribute any model capability, brick, KPI, product boundary, deployment or strategy to Booking.com, Airbnb, Expedia, Vrbo, Trip.com or anyone else.
- Do not reuse brand-derived labels from HSM ("AirCover", "Superhost", "Make Airbnb…") or TAM ("Booking-managed"). Use neutral names.
- Do not quote KPI values. KPI names and tree shapes are fine.
- Quote competitor and `DOMAIN.md` figures only after re-verifying them at the primary source, with period and scope.
- Use the residuality residues as the backbone of the domain-model chapters; they are the most precise statements in either model.
- Treat both data catalogs, deployment replicas and module templates as placeholders; build entities from §7.4.

---

## 13. Glossary seeds

| Term | Definition (as used in the models or this digest) |
| --- | --- |
| Availability assertion | A source's claim that a unit or room type is bookable for given dates; may come from a connectivity partner (TAM residue). |
| Bookability | The effective-dated decision that a unit may be sold for a stay date, given operator, license and jurisdiction (`licn`). |
| Channel manager | Third-party software that distributes a property's rates and availability to many marketplaces; TAM external system on `invt`/`conn`. |
| Co-host | A delegated operator acting on a host's listing with scoped permissions (`coho`); paid via a management fee (HSM rel-06). |
| Connectivity partner / distributor | An intermediary that carries inventory and reservations between properties and the marketplace (TAM `conn`, stressor `insv`). |
| Destination operating state | A versioned area-level emergency state (geography, time, severity, actions) separate from listings and bookings (HSM `evac`). |
| Extranet | The partner-facing control surface for content, policies, reservations, finance and performance (TAM `extr`). |
| Guest commitment / stay obligation | The marketplace's obligation to the traveler, which can be fulfilled by a replacement property (TAM `fire`, HSM `evac`). |
| House rules | Host-defined conditions of stay, authored in `cont` / `lista`. |
| Listing | The published offer of a home or room (HSM), separate from the property and from its current sellability. |
| Local compliance registry | Market-level rules, restrictions and listing requirements (HSM `comp` "Market policy registry"). |
| Managed travel | Policy-constrained business booking with invoicing needs (TAM `cg2-p1`). |
| Merchant of record | The party that legally sells the stay and takes the payment; named in TAM residue `insv`. |
| Overbooking | Selling more nights than the property can deliver, usually from sync failure; TAM KPI "Overbooking incident rate". |
| Partner settlement ledger | Line-level records of bookings, deductions and remittance per partner (TAM `sett`). |
| Payment model normalization | Handling pay-now, pay-later, pay-at-property and platform-managed payment consistently (TAM `paym`). |
| PMS | Property management system; a hotel's operational system that exchanges availability and reservations with the marketplace. |
| Protection programme | Host damage and liability protection plus guest safety intervention (HSM `trst`; brand name in the model must not be reused). |
| Rate parity | A partner's concern that prices match across channels (TAM `jtbd-cg3-1` "rate parity pressure"). |
| Rate plan | Price conditions attached to a room type: cancellation, payment timing, meal plan, member eligibility (TAM `room`). |
| Request to book / instant book | Whether the host must accept a booking or it confirms immediately (TAM `DOMAIN.md`). |
| Reservation screening | Risk evaluation of a booking before confirmation (HSM `trst`, `book` → `trst`). |
| Residue | The structural change that lets an architecture survive a stressor (O'Reilly). |
| Restriction | Minimum stay, closed to arrival or departure, booking window (TAM `cald` "Restriction Policy Engine"). |
| Room type | A category of rooms with an inventory count in a hotel (implied by TAM `room`/`invt`). |
| Room night | One room (or unit) booked for one night; the core volume measure in TAM. |
| Service fee (split / single) | Platform fee charged to guest and/or host (HSM `DOMAIN.md`, insight `hsm-05`). |
| Turnover | Cleaning and readiness work between stays (HSM `opco`). |
| Unit | The rentable thing a night is sold on — a hotel room type instance or a whole home (residues). |

---

*End of digest. Source models: `productscape-examples/_config/product-domains/marketplaces/travel-accommodations-marketplace/` and `…/hosted-stays-marketplace/`. All model content describes generic, fictional operators and must not be presented as fact about any named company.*
