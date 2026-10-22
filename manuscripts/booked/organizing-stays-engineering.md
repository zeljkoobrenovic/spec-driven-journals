{id: organizing-stays-engineering}
# 44. Who Owns What: Organizing Engineering for Stays

![Who Owns What: Organizing Engineering for Stays — logo](stays-marketplace-architecture/posts/44-organizing-stays-engineering/assets/images/44-organizing-stays-engineering/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how to design the team structure, decision rights and on-call model for a group that runs an accommodation marketplace and a hosted-stays marketplace on partly shared platforms. The chapter covers who owns each journey, engine and contract, how architecture decisions are made and recorded, and who answers the page when a partner's system fails.

> **WHY THE BUSINESS CARES:** A convergence program pays off only if the shared engines are built once and run well. Its money is spent through teams, so the org chart decides whether a shared tax engine ships in a year or becomes three projects that argue. Ownership gaps cost money too: a reservation nobody watches turns into a walked guest, and an alert nobody owns turns into a weekend of redacted check-in codes.

> **WHY ARCHITECTS SHOULD CARE:** Conway's law runs in both directions. A context map with no owners for its contracts will be redrawn by whoever ships first. And architecture governance that cannot decide a cross-brand question within weeks will be bypassed by teams that have deadlines.

> **KEY POINTS:**
>
> * **Own journeys, engines and contracts separately, and name all three.** Stream-aligned brand teams own guest, partner and host journeys end to end, including their journey SLOs (service-level objectives). Platform and complicated-subsystem teams own engines. A small stewardship team with no engine to protect owns each shared contract. Most expensive incidents happen where one of the three has no owner.
> * **Govern decisions by blast radius, not by seniority.** A decision inside one bounded context should go through the advice process and an ADR (architecture decision record) in the repository. A change to a shared contract or a boundary needs a forum decision with the consumers' sign-off. Funding, disputes and accepted risks go to a board. One body that decides everything becomes either a rubber stamp or a five-week queue.
> * **On-call for supplier integrations is a product, not a rota.** Page on journey symptoms such as unacknowledged reservations, stale ARI and calendar conflicts. Route each page by partner through an ownership catalog, and give the on-call engineer partner-level controls and a contact registry. Send partner-caused noise into partner-health remediation instead of the night shift.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Lost at the Front Desk** — reservation delivery runs through a gateway team, a channel-manager team, a reservation team and customer service, and no single team owns whether the booking reached the property.
> * **Connectivity Roulette** — partner integrations have commercial owners but no technical owner for each partner's whole behavior, so nobody is on call for a partner, only for pieces of the pipe.
> * **The Unwatched Model** — pricing, ranking and screening models ship from data-science teams without a named owner for their outcomes or the authority to freeze them.

Most chapters before this one ended with a decision and an owner. **This chapter asks whether those owners add up to an organization.** A group that runs two marketplaces on a partly shared platform has more ownership seams than either marketplace alone. The same reservation crosses brand teams, group platforms, partner integrations and customer service, and each seam is a place where a failure can wait unnoticed.

The chapter owns two terms. A **stays team topology** is the assignment of guest, partner and host journeys, engines, shared contracts and partner integrations to teams of known types, with defined ways of working between them. **Architecture governance (stays)** is the set of decision rights, forums, records and measures that decide how those teams change shared things. Boundaries come from [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) and the shared-versus-separate argument from [One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces). The journey SLOs that on-call protects come from [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability). How the organization moves a live platform is the subject of [Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace).

{id: organizing-stays-engineering--setting-the-scene-at-corvane-two-incidents-eleven-teams}
## Setting the Scene at Corvane: Two Incidents, Eleven Teams

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), had two incidents in the summer of 2027 that looked unrelated. Both are described in earlier chapters; here they matter for **who was involved and who was not**.

The first was **Hotel Miradouro's missing reservations** ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)). On 5 July at 23:30 a PMS (property-management system) release at the Lisbon hotel began rejecting reservations on four legacy rate-plan codes. Corvane Connect, the group's channel-manager business, had already acknowledged each message to Switchyard, Roomstead's connectivity gateway. Keystone, Roomstead's Java monolith, marked the bookings as sent. Connect parked the failures in a dashboard and a shared inbox. Two guests arrived unknown on 10 and 13 July. On 16 July at 18:40 a family from Lyon was walked to a hotel in Belém. By then **33** messages had failed, **19** of them new Roomstead reservations. At least five teams touched these messages: Connect's integration team in Utrecht, the Switchyard team in Dublin, Keystone's reservations team, Roomstead partner support, and the outsourced contact center that took the guests' calls. Each team did its own job correctly. **None of them owned the outcome that mattered: whether the reservation had reached the front desk.**

![Five desks pass an envelope along a relay track, each marked done, while the envelope falls off before reaching the hotel front desk where a family waits.](stays-marketplace-architecture/posts/44-organizing-stays-engineering/assets/images/44-organizing-stays-engineering/44-miradouro-nobody-owns.jpeg)

**Figure 1:** *At Miradouro at least five teams did their own jobs correctly, and none owned whether the reservation reached the front desk.*

The second was the **check-in instructions that never arrived** ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)). On Thursday 5 August a Nookaway trust team shipped a contact-detail detector to stop off-platform scams before booking. The detector read the trip stage from a field that partner-API messages left empty, and redacted door codes and phone numbers in post-booking messages for 53 hours. The detector belonged to the trust team. The partner API belonged to Nookaway's connectivity team. Post-booking messaging belonged to a Burrow messaging team. Support belonged to Elena Petrova's organization. A support team lead noticed the pattern on Saturday evening, after **1,870** check-in contacts. **The team that made the change had no signal about its consequence, and the team that saw the consequence had no way to trace it to the change.**

On 2 September, at the end of the forum session that created Courier and Threadline, Tobias Lindqvist, the Group CTO, put a question to Mariana Costa, the Group Chief Architect:

> "We have a capability map, a context map, sixteen shared engines and six shared contracts on paper. Who builds them, who runs them at three in the morning, and who decides when two of them disagree? Bring me an org design for One Stay by October."

Mariana started with an audit rather than an org chart. The rest of this chapter follows what she found and what Corvane decided, generalized for any group with two marketplaces.

{id: organizing-stays-engineering--concepts-teams-ownership-and-decision-rights}
## Concepts: Teams, Ownership and Decision Rights

{id: organizing-stays-engineering--conway-s-law-in-both-directions}
### Conway's law, in both directions

Melvin Conway observed in 1968 that organizations which design systems "are constrained to produce designs which are copies of the communication structures of these organizations." For a stays group this has a forward and a reverse reading. **Forward:** two brand engineering organizations that rarely talk will build two of everything, and Corvane's 2027 landscape has two identity systems, two trust stacks, two search engines and two experimentation platforms. **Reverse:** if the group wants a shared reservation contract, some team must be organized to own it, or the contract will drift toward whichever engine team edits it most often. The "inverse Conway maneuver", choosing the team structure that produces the architecture you want, works only when the architecture is already decided.

{id: organizing-stays-engineering--team-types-and-interaction-modes}
### Team types and interaction modes

Matthew Skelton and Manuel Pais's *Team Topologies* (2019) gives a vocabulary that fits stays platforms well. It has four team types and three interaction modes.

| Team type | Definition (Team Topologies) | In a stays group |
| --- | --- | --- |
| **Stream-aligned** | Aligned to "a flow of work from (usually) a segment of the business domain", owning it end to end | A guest journey (search, property page, checkout, trip), a partner journey (onboarding, extranet) or a host journey (listing, calendar, payouts) in one brand |
| **Platform** | Provides "a compelling internal product to accelerate delivery by Stream-aligned teams" | Identity, payments and ledger, tax engine, trust platform, messaging and notifications, data and ML platform, search platform, runtime |
| **Complicated-subsystem** | Owns a part "where significant mathematics/calculation/technical expertise is needed" | Availability and price caches, calendar sync, ranking models, dynamic pricing, fraud and risk models, property matching |
| **Enabling** | "Helps a Stream-aligned team to overcome obstacles", meant to be temporary | Monolith extraction, SLO and on-call adoption, contract migration support |

The three interaction modes are **collaboration** (two teams work closely for a defined period to discover something), **X-as-a-service** (one team consumes another's product through its interface) and **facilitation** (one team coaches another). A good design states the mode for each important pair of teams **and when it ends**. Collaboration that never ends is a merged team with two backlogs.

Team Topologies grounds all of this in **cognitive load**: a team can own only as much domain and technology as it can understand. Stays platforms test that limit. A Roomstead checkout team has to understand rate plans, payment arrangements, cancellation policies, tax display and fraud screening. It cannot also own the price cache or the PSP (payment service provider) integration. The topology exists to keep each team's load bounded.

{id: organizing-stays-engineering--three-kinds-of-thing-to-own}
### Three kinds of thing to own

The two incidents above suggest a distinction the generic vocabulary does not make. Three kinds of thing need owners in a stays platform:

1. **Journeys.** A journey is an outcome a guest, partner or host experiences, for example "the reservation reached the front desk" or "the check-in code arrived". Its owner holds the journey SLO, sees the end-to-end signal and is paged when it breaks.
2. **Engines.** An engine is a running system with a store and an API: Tally, Almanac, Fathom, Levy, Courier. Its owner holds the service's SLOs, capacity and change safety.
3. **Contracts.** A contract is a shared schema and its semantics: the offer, the reservation, the payment arrangement, the stay query. Its owner holds versioning, compatibility tests and the meaning of each field.

When one team owns all three, as in a small marketplace, the distinction is invisible. In a group it is the main design decision. Miradouro's missing reservations had engine owners and no journey owner. The redaction incident had a journey owner (support) without the signal, and engine owners without the journey. Chapter [Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts) already gave the shared contracts a **contracts stewardship group** in the Group Chief Architect's office, because a contract owned by one engine team serves that engine first.

{id: organizing-stays-engineering--decision-rights-and-architecture-governance}
### Decision rights and architecture governance

**Architecture governance** decides who may change what, after consulting whom, and where the decision is recorded. Three mechanisms recur:

- An **architecture decision record (ADR)** is a short document: context, decision, options considered, consequences, and the advice received. It is stored with the code or in a shared decision log.
- The **advice process**, described by Andrew Harmel-Law (martinfowler.com, 2021): "anyone can make an architectural decision", provided they first consult the people significantly affected and the people with relevant expertise. Advice must be sought and recorded, but it need not be followed. It is supported by ADRs, a weekly **architecture advisory forum** where decisions are discussed in public, team-sourced principles, and a technology radar.
- A **design authority** or **architecture board**: a body that approves or rejects decisions above some threshold.

The advice process scales well when decisions are local. A two-marketplace group also has decisions with many affected parties and one natural decision-taker who is biased: the engine team that wants to change a shared contract. The governance design question is therefore **which decisions are local enough for advice, and which need a decision right held by someone with no engine to protect.**

{id: organizing-stays-engineering--architecture-a-team-topology-for-two-marketplaces}
## Architecture: A Team Topology for Two Marketplaces

{id: organizing-stays-engineering--the-shape}
### The shape

Map the topology onto the context map, not onto the current org chart. Its shape for a group with an accommodation marketplace and a hosted-stays marketplace has six layers.

1. **Brand stream-aligned teams, split by side.** Each brand has guest-journey teams and supply-journey teams. On the accommodation side the supply teams serve **partners**: properties and their revenue managers, through onboarding, the extranet and rate tools. On the hosted-stays side they serve **hosts**: individuals and professional managers, through listing creation, calendars, pricing tools, co-hosts and earnings. Each team owns its journey's SLO.
2. **Partner-facing connectivity teams per brand.** These are product teams whose users are channel managers, PMS vendors and iCal feeds. They own the gateway, certification, partner health and the partner integration on-call. They are separate from the extranet teams, because their users are software vendors, not hotels.
3. **Complicated-subsystem teams** where the depth is real: the availability and price cache, calendar-claim sync, ranking per brand, dynamic pricing, risk models, property and room matching. They serve stream-aligned teams through APIs and keep the specialist knowledge in one place.
4. **Group platform teams** for the shared engines: identity, payments and ledger, tax, trust, messaging and notifications, customer-service platform, data and ML platform, search platform, booking platform, place registry and supply party, runtime and developer experience.
5. **Contract stewardship** for the shared contracts, with no engine.
6. **Enabling teams** for time-bound work, above all extracting the monoliths and adopting journey SLOs and on-call. Each has an exit date.

![Brand journey teams use connectivity, subsystems and group platforms as a service; contract stewards supply schemas to the group platforms.](stays-marketplace-architecture/posts/44-organizing-stays-engineering/assets/images/44-organizing-stays-engineering/44-stays-team-topology.jpeg)

**Figure 2:** *A stays team topology. Brand journey teams own the journeys; engines sit in connectivity, complicated-subsystem and group platform teams consumed as a service. Shared contracts have stewards who own no engine and supply the schemas.*

{id: organizing-stays-engineering--what-makes-this-stays-specific}
### What makes this stays-specific

Team Topologies applies anywhere. In stays, four boundaries are not obvious:

| Boundary | Where teams often draw it | Where I would draw it | Why |
| --- | --- | --- | --- |
| Checkout vs price composition | Checkout team computes the final price | Price composition is a complicated subsystem, shared by search, property page and checkout | Price Drift starts when each surface adds fees and taxes itself ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)) |
| Reservation vs delivery | Gateway team owns "sent"; reservation team owns state | One stream-aligned team owns **reservation delivery** as a journey, with acceptance and arrivals SLOs | "Sent" is an engine fact; "the hotel has it" is a journey fact ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)) |
| Extranet vs connectivity | One "partner" org owns both | Separate teams: extranet serves people, connectivity serves software vendors | Different users, release cycles and failure modes ([Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools)) |
| Model vs outcome | Data science owns the model; product owns the screen | Model outcome owned by the product or domain team, with freeze authority; ML platform owns training and serving | Without freeze authority, ownership is decorative ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)) |

{id: organizing-stays-engineering--ownership-catalog}
### Ownership catalog

The topology is only real if it is machine-readable. An **ownership catalog** lists every production asset with its owning team and on-call rotation. Assets include services, monolith modules, event topics, shared contracts, data products, models, partner connections and scheduled jobs. Each entry also records the bounded context it belongs to and the journey SLOs it contributes to. Alert routing, incident tooling, cost reports and the decision log all read the catalog. Two catalog entries are specific to stays and often missing:

- **Partner connection.** Each certified partner (a channel manager, a PMS vendor, a bedbank) gets a technical owner, a commercial owner, an escalation contact at the partner, a health score and the controls the on-call engineer may use on it.
- **Model.** Each production model gets an outcome owner with freeze authority, a serving owner and an evaluation schedule ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)).

The catalog's most important number is the count of **orphans**: assets with no owning team or no rotation. The target is zero, and every new asset is registered before it reaches production.

{id: organizing-stays-engineering--architecture-governance-three-classes-of-decision}
## Architecture Governance: Three Classes of Decision

{id: organizing-stays-engineering--why-one-body-is-not-enough}
### Why one body is not enough

A single architecture review board that approves every significant change fails in a predictable way. Its agenda grows faster than its meetings, teams learn to frame changes as "not architectural", and the board ends up approving what has already shipped. A pure advice process fails in the opposite way in a group. It lets the engine team that wants a contract change take the decision after "seeking advice" from twelve consumers, and the contract ends up serving the engine.

The design I use sorts decisions by **blast radius**, meaning how many teams, brands and money flows the decision binds.

| Class | What falls in it | Who decides | Record | Typical lead time |
| --- | --- | --- | --- | --- |
| **T: team** | Anything inside one bounded context that does not change a shared contract, a published event's meaning or a journey SLO | The owning team, after the advice process | ADR in the team's repository, linked from the decision log | Days |
| **C: contract** | Changes to shared contracts (offer, reservation, payment arrangement, stay query); new or moved context boundaries; new shared engines' interfaces; events that money systems consume; degradation ladders | The architecture forum, with each consuming team's sign-off and mandatory reviewers by topic | Group decision log, versioned | 1–3 weeks |
| **G: group** | New shared engines and their funding; disputes between brands or with the channel-manager business; accepted risks (a single-region system, a deferred migration); decisions that change commercial terms with partners | The group architecture board | Group decision log plus board minutes | Monthly cycle |

**Mandatory reviewers** are what make class C safe. They are named per topic and have the right to block, which advisers in the advice process do not have. In a stays group the list is short:

- **finance** for anything that changes money boundaries;
- **regulatory and privacy** for display rules, retention and statements of reasons;
- **trust** for messaging policy;
- **payments** for the payment arrangement.

Keep it short, or class C becomes the review board again.

![A proposal passes two questions and goes to the team, the forum or the board; all three write to one decision log, which feeds governance measures.](stays-marketplace-architecture/posts/44-organizing-stays-engineering/assets/images/44-organizing-stays-engineering/44-decision-routing.jpeg)

**Figure 3:** *Routing a decision by blast radius. Most decisions stay with teams under the advice process. Contract and boundary changes go to the forum, and funding, disputes and accepted risks go to the board. All three write to one decision log, which is also where governance is measured.*

{id: organizing-stays-engineering--what-the-architecture-forum-is-for}
### What the architecture forum is for

The forum takes class C decisions and also *shows* class T decisions. Harmel-Law's advisory forum is "a weekly, hour-long" session whose main value is that everyone learns from decisions taken in public. A stays group needs both functions, kept separate on the agenda: a decision section with a quorum and reviewers, and a learning section where a team presents a class T ADR and receives advice it may ignore.

Three rules keep the forum useful:

1. **Bring a real case, not a principle.** The forum decisions in this book that worked started from an incident or a traced reservation: the €12 rate, the Seville double booking, the Novak price drift. A field-by-field trace forces specifics that a slide about "alignment" does not.
2. **Decide or schedule.** Every class C item leaves the session with a decision, a named list of missing information and a date, or an escalation to the board. "Let's discuss again" is not an outcome.
3. **Publish reversals.** A decision changed after new evidence is a sign of health. Count reversals, and present them in the learning section.

{id: organizing-stays-engineering--measuring-governance}
### Measuring governance

Governance that is not measured becomes ceremony. I track five numbers, all from the decision log and the ownership catalog:

| Measure | What it shows | Warning sign |
| --- | --- | --- |
| Median lead time for class C decisions, from first presentation to decision | Whether the forum is a bottleneck | Over three weeks for two quarters |
| Share of decisions taken as class T | Whether teams have real autonomy | Falling, while the forum's agenda grows |
| Contract changes merged without a forum decision | Whether the contract boundary holds | Any, found by the contract repository's checks |
| Orphan assets in the ownership catalog | Whether ownership keeps up with change | Above zero for a month |
| Changes that needed more than one team ([Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts)) | Whether the boundaries fit the teams | Rising after a reorganization |

{id: organizing-stays-engineering--on-call-for-what-you-do-not-control}
## On-Call for What You Do Not Control

{id: organizing-stays-engineering--the-problem}
### The problem

In a stays platform the most important write paths run through other companies' software: ARI (availability, rates and inventory) from channel managers and PMSs, reservations delivered to them, calendars imported from competing platforms. When those fail, the symptom shows up in the marketplace's journey, while the cause and the fix are with the partner. Two bad on-call designs follow from this:

- **On-call by component.** The gateway team is paged when the gateway is unhealthy. But the gateway is healthy: it is accepting messages from a partner whose mapping is wrong, or receiving 200 responses from a channel manager whose PMS is rejecting reservations. Miradouro's missing reservations triggered no alert, because no component failed.
- **On-call for everything partner-related.** One rotation receives every partner anomaly and drowns in noise caused by the partners. Google's *Site Reliability Engineering* (2016) sets a ceiling of about **two incidents per 12-hour shift**. Above it, engineers cannot investigate properly and start to acknowledge without acting. It also sets a minimum rotation of **eight** engineers on one site, or **six** per site across two sites.

{id: organizing-stays-engineering--the-design}
### The design

On-call for supplier integrations works when it is treated as a product with five parts:

1. **Page on journey symptoms.** Alerts come from the journey SLOs: reservation versions not accepted within the deadline, arrivals not verified 24 hours before arrival, ARI freshness by partner, calendar conflicts found on import, held or rejected ARI messages above a partner's baseline. These are the partner-health signals of [Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers) and [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync), computed continuously.
2. **Route by partner through the catalog.** An alert names the partner connection. The catalog gives the owning connectivity team's rotation, the partner's escalation contact, and the properties and arrivals at risk.
3. **Give the on-call engineer partner-level controls.** The controls are: pause a connection's ARI and keep the last good values; switch reservation delivery for affected properties to the extranet inbox; close inventory for affected properties with notice to the hotel; trigger a full re-sync once the partner recovers; for calendars, switch a broken feed's listings to request-to-book. Each control is scoped, logged and expiring, as degradation modes are in [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability).
4. **Bring in customer service early.** Any incident with arrivals inside 48 hours opens a liaison with the customer-service duty manager, so guests are contacted before they reach a locked door or a front desk that has no booking ([When Something Goes Wrong: Customer Service and Recovery](#customer-service)).
5. **Send partner-caused noise to remediation, not to the night.** A recurring partner-caused alert with no guest impact inside the next 48 hours goes to a business-hours partner-engineering queue and counts against the partner's health score. The night page is reserved for journey SLOs that are burning.

![Swimlanes for channel manager, gateway, tracker, on-call and duty manager: a rejection reaches the tracker, which pages on-call; on-call opens a partner incident and alerts the duty manager about arrivals; the fix is resent and accepted.](stays-marketplace-architecture/posts/44-organizing-stays-engineering/assets/images/44-organizing-stays-engineering/44-supplier-oncall.jpeg)

**Figure 4:** *On-call for a supplier integration. The page comes from the delivery journey, not from a component, and is routed to the connectivity team that owns the partner. The on-call engineer uses partner-level controls, opens a partner incident and brings in customer service while arrivals are still days away.*

The design also has to say who handles a partner that is part of the same group. When the group owns a channel manager, as Corvane owns Corvane Connect, the incident protocol must be the same one used with every other partner. Otherwise private escalation paths grow, and the neutrality promised to hotels becomes a story.

{id: organizing-stays-engineering--in-practice-what-the-public-record-shows}
## In Practice: What the Public Record Shows

Companies rarely publish their org charts. What they do publish shows how ownership follows architecture.

{id: organizing-stays-engineering--expedia-group-a-platform-operating-model-then-brand-general-managers}
### Expedia Group: a platform operating model, then brand general managers

Expedia Group's annual reports describe an organizational change made before the technical consolidation. Its FY2023 10-K (published February 2024) says that "during 2020, Expedia Group unified its technology, product, data engineering, and data science teams". The FY2025 10-K (published February 2026) describes a "platform operating model strategy" under which the Hotels.com and Vrbo front-end stacks moved onto the Brand Expedia stack, completed in 2023. In 2024, the same filing says, Expedia added **general managers per consumer brand** "while also leveraging the scale and efficiency of our unified tech platform". The first quarter of 2024 also showed the cost of that path: Expedia's CEO said that "Vrbo's recovery following the recent re-platforming has been slower than anticipated" (earnings release, May 2024).

> **INFERENCE, NOT DOCUMENTED:** The filings do not explain the 2024 brand general managers. One plausible reading, offered as the author's interpretation and not as Expedia's explanation, is that a unified platform organization optimizes for shared capability while the brands' commercial outcomes need a single accountable owner. If so, this is the same tension as journey ownership versus engine ownership in this chapter, resolved at executive level.

{id: organizing-stays-engineering--booking-com-page-owners-and-data-owners}
### Booking.com: page owners and data owners

Two Booking.com engineering sources show ownership drawn deliberately. In a 2026 post on its Node.js rendering platform, Booking.com writes that each major page has "its own Node rendering service, owned by the team responsible for that page". It adds that sections of a page, such as the photo gallery, reviews or rooms table, are owned by different teams, some loaded at runtime through Webpack Module Federation so that a section owner can deploy without redeploying the page. That is stream-aligned ownership at the level of a page fragment. In a 2024 SREcon talk on its MySQL estate (more than 250 clusters), the database team described its ownership boundary as "We do not own data. We do not own tables or schemas". That is a platform team stating explicitly what it does not own. A 2017 paper by Kaufman, Pitchforth and Vermeer credits Booking.com's spread of experimentation across a decentralized organization to shared tooling and safeguards rather than a central team; it is nine years old ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation)).

{id: organizing-stays-engineering--airbnb-the-organizational-cost-of-a-shared-monolith}
### Airbnb: the organizational cost of a shared monolith

Airbnb's account of leaving its Rails monolith, Monorail, is mostly about architecture, and its starting point was organizational. In a 2018 QCon talk Jessica Tai described more than **200** engineers committing to Monorail by about 2015, with about **15 hours** of deploy blockage a day. The migration defined service types with a strict dependency direction (data services, derived data services, a middle tier for shared validation such as reservation validation, and presentation services), each with clear ownership of its data. By 2022, an Airbnb post on incident management described "over a thousand micro services with hundreds of small teams". A 2025 post on Viaduct, its GraphQL data-oriented service mesh, reported that more than **130** teams host code in it. Both posts describe a later state; the 2018 evidence describes a migration then in its early stages.

{id: organizing-stays-engineering--agoda-boundaries-enforced-in-the-build-not-the-org-chart}
### Agoda: boundaries enforced in the build, not the org chart

Agoda's 2026 post on its post-booking API describes an alternative to splitting teams and services. Merge requests on the post-booking codebase "more than quadrupled between 2022 and 2025". Agoda introduced a **modular monolith** with domain components (`rebook`, `cancellation`, `payment`) enforced by architecture tests in continuous integration. It reports that merge requests in the framework-backed area completed review 64% faster at the median in Q2 2026, on a small sample. The lesson for organization design is that ownership boundaries can be enforced by tooling inside one deployable before they become service or team boundaries.

{id: organizing-stays-engineering--what-the-record-does-not-show}
### What the record does not show

None of these companies publishes how it runs on-call for supplier integrations, how architecture decisions are governed across brands, or how it assigns ownership of shared contracts. The designs in this chapter for those three areas are recommendations, not descriptions of any company.

{id: organizing-stays-engineering--corvane-worked-example-one-stay-org-design-v1}
## Corvane Worked Example: One Stay Org Design v1

The figures below are fictional and illustrative, like everything about Corvane.

{id: organizing-stays-engineering--the-audit}
### The audit

In September 2027 Mariana's office loaded every production asset into a first ownership catalog: Roomstead's **180** AWS services, Nookaway's **60** Go services, Keystone and Burrow modules, event topics, models and partner connections. Each item was checked against three questions: does it have an owning team, an on-call rotation, and a journey it contributes to?

| Finding | Count (September 2027) | Consequence |
| --- | --- | --- |
| Services with no on-call rotation listed | **31** of 240 | Alerts routed to a shared channel nobody watched at night |
| Services straddling two or more contexts | **44**, 17 in the booking path ([Drawing the Lines: Bounded Contexts for Stays](#stays-bounded-contexts)) | Changes in checkout needed two to four teams |
| Event topics with no owning team | **96** of about 600 | Schema changes discovered by consumers in production |
| Production models with no outcome owner | **9** of 38 | Smart Rate and the screening model got owners only after incidents |
| Certified Roomstead connectivity partners with one technical owner for their whole behavior | **0** of 140 | Each partner had a commercial account manager; the pipe, delivery and fallback belonged to three teams |
| Roomstead connectivity on-call pages per week, Q3 2027 | **31** average, **64%** partner-caused | Above the 28 a week that a 24-hour, two-incidents-per-shift ceiling allows |

The governance side had its own numbers. Mariana had started the **architecture forum** in **February 2027**, a month after joining, as a weekly 90-minute session. By the end of September it had recorded **71** decisions in the group decision log, from the checkout attempt contract in February to Courier and Threadline on 2 September. Three had gone to the **group architecture board**, which Tobias chairs monthly with the Group CFO, the Group Chief Architect and the brand leaders: the Corvane Connect neutrality rule (May), Fathom as settlement ledger of record (May, with the CFO's co-signature), and Ranking Policy v1 (September). The forum had worked, and it had become the bottleneck: by August its decision queue was **five weeks** long, and teams had started describing changes as "internal" to avoid it.

{id: organizing-stays-engineering--the-design-1}
### The design

Tobias approved **One Stay Org Design v1** at the group architecture board on **19 October 2027**, after the forum's advice session on 13 October. It took effect on **1 January 2028**. Its engineering population is about **1,750** engineers in **190** teams.

| Team type | Corvane examples | Teams | Engineers |
| --- | --- | --- | --- |
| Stream-aligned, Roomstead guest | Search and results, property page, checkout, trips and post-booking, reservation delivery, Circle, apps | 42 | 400 |
| Stream-aligned, Roomstead partner | Onboarding, Partner Hub, Rate Insights, partner finance views | 18 | 160 |
| Stream-aligned, Nookaway guest | Search and listing page, checkout and Pay Later, trips and arrival packages | 18 | 170 |
| Stream-aligned, Nookaway host | Listing creation, calendar and host app, professional managers and co-hosts, earnings | 16 | 150 |
| Partner-facing connectivity | Switchyard and certification, partner engineering (Roomstead); partner API and Calendar Sync v2 (Nookaway) | 10 | 95 |
| Complicated-subsystem | Tally and Pricegrid, Almanac claims, Roomstead and Nookaway ranking, Smart Rate, price composition, Concord matching, booking risk score models, Levy rules engine | 16 | 140 |
| Group platform | Runtime and developer experience, Corvane ID, Courier, data and ML platform, search platform and Waypoint, Corvane Payments with Fathom and Plumbline, Levy, Warden, support platform, booking platform with Clause and Stayline, place registry and supply party | 46 | 450 |
| Enabling and stewardship | Keystone extraction, SLO and on-call adoption, contracts stewardship group (grown from four to six engineers) | 5 | 40 |
| Legacy core | Keystone core, Burrow core | 9 | 75 |
| Corvane Connect | Separate product organization in Utrecht; ordinary partner of Switchyard | 10 | 70 |
| **Total** | | **190** | **1,750** |

Five decisions shaped the table.

**1. Reservation delivery became a journey with an owner.** A Roomstead stream-aligned team in Dublin took "the reservation reached the property" end to end: the acceptance SLO, the 7-day and 48-hour arrivals manifests from [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), and the Partner Hub fallback inbox. Switchyard remained the pipe, owned by the connectivity team. On Nookaway, the trips team took the equivalent journey, "the guest can get in", with the arrival-package SLO from [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging).

**2. Group platforms report to the CTO, and brand-hosted platforms are explicit.** Most shared engines sit in a group platform organization under Tobias. Three do not, and the design says so: **Threadline** stays with Nookaway engineering under Rafael Mendes, because Nookaway has the deeper conversation problem. **Clause** and **Stayline** stay with the group booking platform team in Lisbon, which sits with Nookaway's teams. A brand-hosted platform carries one extra obligation. Its roadmap is reviewed by the forum each quarter, so the other brand is not a second-class customer.

**3. Complicated subsystems are owned where the expertise is, and consumed as a service.** Pricegrid and Tally stay with Roomstead in Dublin, Almanac with Nookaway in Lisbon. The two ranking teams stay separate, consistent with the June 2027 search decision ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture)). Kenji Arai's data and ML platform in Barcelona serves both. Each model has a domain owner with freeze authority.

**4. Interaction modes have end dates.** The design lists the collaborations and when each turns into X-as-a-service.

| Pair | Mode | Until |
| --- | --- | --- |
| Booking platform (Stayline) and Nookaway checkout | Collaboration | Nookaway reservations on Stayline, end of 2028 |
| Booking platform (Stayline) and Keystone extraction team | Collaboration | Keystone reservation module retired, end of 2029 |
| Corvane Payments and Roomstead checkout (payment arrangement) | X-as-a-service | Permanent |
| Contracts stewardship and every engine team | Facilitation for compatibility tests | Each engine's tests in CI |
| SLO and on-call enabling team and brand teams | Facilitation | Every journey SLO has an owner and a rotation, end of Q2 2028 |

**5. Governance split into the three classes.** Class T decisions moved out of the forum, into ADRs in team repositories under the advice process, and the forum's learning section shows a sample each week. Class C kept the forum, with mandatory reviewers named per topic: Marco Bellini's finance team for money events, Noor van Dijk's team for display, retention and statements of reasons, Sofia Marín's trust team for messaging policy, Leila Haddad's team for the payment arrangement. The contracts stewardship group became the forum's secretariat for contract changes. Class G stayed with the board.

{id: organizing-stays-engineering--miradouro-replayed-under-v1}
### Miradouro, replayed under v1

The forum replayed July's missing reservations against the new design in November 2027. It assumed the August delivery decisions (acceptance only with a PMS confirmation number or a reason code) had been certified for Corvane Connect, as planned for Q4 2027.

| Moment | July 2027 (actual) | Under Org Design v1 (replay) |
| --- | --- | --- |
| First rejection, 6 July | Connect parks it in a dashboard; Switchyard has "acknowledged" | Rejection with reason code reaches the delivery tracker within minutes |
| Detection | 10 July, by a front desk | Acceptance SLO alert for one partner after the third rejection, routed to the Roomstead connectivity on-call |
| First action | 16 July, after a walked family | The on-call switches Miradouro's delivery to the Partner Hub inbox and opens a partner incident with Connect through the same protocol as any partner |
| Guest contact | After arrival | Customer-service liaison for the two arrivals inside 48 hours |
| Reservations exposed | 19 new, 3 modified, 4 canceled over 12 days | The replay stopped exposure at under an hour of bookings |
| Who owned the outcome | No one | The reservation-delivery team's acceptance SLO |

The replay changed one thing in the design. The connectivity on-call had a 31-page week as its baseline. Mariana's office routed **partner-caused alerts without arrivals inside 48 hours** to a business-hours partner-engineering queue, to be counted against the partner's health score. Applied to Q3 2027 data, that rule cut night-relevant pages to about **11** a week. The forum also accepted that Switchyard's rotation, eight engineers in Dublin, gets a second site in Kraków in 2028 so that nobody is on call alone across the Asia-Pacific night.

![A funnel splits a stream of alert bells: most go to a daytime partner queue, a few reach the night on-call engineer.](stays-marketplace-architecture/posts/44-organizing-stays-engineering/assets/images/44-organizing-stays-engineering/44-night-pages-filter.jpeg)

**Figure 5:** *Sending partner-caused alerts without arrivals inside 48 hours to a business-hours queue cut the night-relevant pages from 31 a week to about 11.*

{id: organizing-stays-engineering--what-it-cost}
### What it cost

Org Design v1 moved about **210** engineers between reporting lines and created **14** new teams. Most new teams were group platform teams, built from engineers who had owned the brands' duplicate engines. Nobody was hired for the change. Mariana's estimate for the board was a **six-week** productivity dip in the affected teams, scheduled after Black Friday. Funding for the group platforms came from the €145 million One Stay budget; the brands kept funding their stream-aligned teams.

{id: organizing-stays-engineering--trade-offs}
## Trade-offs

{id: organizing-stays-engineering--organizing-two-marketplaces}
### Organizing two marketplaces

| Option | How it works | Strengths | Weaknesses | When it is right |
| --- | --- | --- | --- | --- |
| **Brand-aligned** | Two engineering organizations, each owning everything for its marketplace | Fast within a brand; clear accountability | Two of everything; shared services become negotiations between equals | The marketplaces share little, or one may be sold |
| **Functional across brands** | One search org, one supply org, one booking org, each serving both brands | Maximum reuse; one expert community per domain | Brand outcomes have no single engineering owner; one model is forced onto both marketplaces (The Hotel-Shaped Home) | The two marketplaces are converging on one supply model |
| **Brand journeys plus group platforms** (Corvane) | Brands own journeys and their core subsystems; group owns shared engines; stewards own contracts | Brand speed on what differs, reuse where the problem is the same | More interfaces to govern; platform teams can become ticket queues | Shared engines for person, money and law, separate engines for supply and inventory |
| **One platform organization, brand general managers** | Unified technology organization; brands are commercial units on it | Single platform roadmap; strongest economies of scale | Brand-specific depth competes for one roadmap; costly re-platforming of the different brand | The brands are commercially distinct but technically alike |

{id: organizing-stays-engineering--governing-architecture}
### Governing architecture

| Option | Strength | Weakness | When it is right |
| --- | --- | --- | --- |
| **Central review board approves all significant changes** | Consistency; visible control | Queue; decisions framed to avoid the board; architects as gatekeepers | Small organizations, or a regulated change freeze |
| **Pure advice process** | Speed; ownership stays with teams; learning in public | Shared contracts drift toward the loudest engine; no one can say no | One marketplace, few shared contracts |
| **Three classes by blast radius** | Local speed with a decision right on shared things | Classification arguments; needs a steward with no engine | Groups with shared contracts and money flows |

{id: organizing-stays-engineering--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

The organizational principles are the same for both marketplaces. The team portfolio is not, because the users on the supply side and the core subsystems differ.

| Dimension | Accommodation marketplace | Hosted-stays marketplace |
| --- | --- | --- |
| Supply-side users | Revenue managers and front offices, mostly through software | Individual hosts in an app; professional managers through software |
| Largest supply-side teams | Connectivity, certification and partner engineering; extranet for the 18% not connected | Host product: listing creation, calendar, pricing tools, co-hosts, earnings |
| Core complicated subsystems | Price and availability cache, rate-plan derivation, property matching | Calendar claims and sync, automatic pricing, reservation screening |
| What pages at night | Partner ARI and delivery failures; cache staleness at peaks | Calendar conflicts, arrival packages, host cancellations close to arrival, pricing anomalies |
| Trust organization | Partner-account security and payment fraud | Guest–host trust, screening, protection claims, many policy decisions about people |
| Regulatory load on teams | Display, ranking transparency, P2B (platform-to-business) notices | Plus short-term-rental registration, data sharing and city rules for every market ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)) |
| Operations beside engineering | Market and account managers for properties | Community and host support; field quality where homes are inspected |

**What can be shared** is the organizational machinery: the team types, the ownership catalog, the three decision classes, the decision log, the on-call protocol, partner-health definitions and journey SLO templates. Group platform teams and the contracts stewardship group are shared by definition. **What should not be shared** is the supply-side team portfolio. An accommodation marketplace that organizes its supply teams like a hosted-stays marketplace under-invests in connectivity. A hosted-stays marketplace organized like an OTA builds an extranet for people who live in a phone app. Convergence adds a third case. When the hosted-stays brand starts selling boutique hotels, as Nookaway plans to pilot in 2028, those hotels need connectivity. The design should make that an X-as-a-service request to the accommodation brand's connectivity teams, not a third gateway ([One Platform or Two? Converging Hotels and Homes](#converging-two-marketplaces)).

{id: organizing-stays-engineering--failure-modes}
## Failure Modes

**The platform team as a ticket queue.** A group platform team takes requests from both brands and prioritizes by whoever escalates. *Symptom:* brand teams build workarounds; the shared engine has two forks within a year. *Defense:* the platform has a product owner, a published roadmap reviewed by the forum each quarter, and self-service interfaces. Track the share of consumer integrations completed without a ticket.

**The contract owned by its biggest engine.** The reservation contract sits in the Roomstead reservations team's repository, so changes that suit Keystone pass easily. *Symptom:* the hosted-stays brand maps its concepts into hotel-shaped fields. *Defense:* a steward with no engine, compatibility tests run by consumers, and class C decisions for meaning changes.

**Built by the group, paged in the brand.** A group team ships a shared engine but the brand's on-call is paged when it fails, because the brand owns the journey. *Symptom:* brand engineers restart services they do not understand. *Defense:* the engine's owner carries its rotation; journey owners are paged on symptoms and escalate to engine rotations through the catalog.

**Reorganizing instead of deciding.** The org chart changes before the context map and the shared contracts exist. *Symptom:* new group teams with unclear scope and the same old dependencies. *Defense:* contracts and boundaries first, as Corvane did with Context Map v1 in May and Org Design v1 in October.

**The enabling team that never leaves.** A monolith-extraction team becomes the owner of everything nobody else wants. *Symptom:* it has its own on-call for production services. *Defense:* an exit date and a rule that it never owns production assets in the catalog.

**The in-house partner with a private line.** The group's own channel manager or PMS gets earlier API access, a shared Slack channel and favorable incident handling. *Symptom:* other partners' certification issues take weeks; Connect's take hours. *Defense:* one partner-incident protocol for all, and disputes to the board, as Corvane's neutrality rule requires.

{id: organizing-stays-engineering--the-chief-architect-s-view}
## The Chief Architect's View

**Draw ownership from the context map, and keep the map and the catalog in sync.** I would not approve an org design that cannot list, for every bounded context, the team that owns its engine. For every shared contract it must list the steward, and for every journey SLO the team that is paged. The ownership catalog is how I would check that, and the orphan count is the first number I would look at each month.

**Separate journey ownership from engine ownership in the group's design, and let teams combine them where they can.** Small marketplaces get both from one team for free. In a group, someone must own "the reservation reached the hotel" and "the guest could get in" as journeys, separately from the teams that run the gateway and the messaging engine. These are the outcomes guests remember and regulators ask about.

**Keep the forum's decision right narrow and its learning function wide.** The forum decides contract and boundary changes. It does not approve team designs. Everything else it hears, in public, so that the next team learns from it. If its queue passes three weeks, the cure is reclassification, not more meetings.

**Put finance and regulatory affairs inside governance, not after it.** In a stays group, money events and display rules carry legal consequences. The CFO's co-signature on money boundaries and the regulatory team's veto on display and retention cost a few days per decision. Without them, an audit finding or a regulator's letter arrives months later.

**Fund on-call as a product.** Supplier-integration on-call needs alert design, a partner contact registry, partner-level controls, a customer-service liaison and enough engineers for a humane rotation. Budget it like the gateway. A rotation over the SRE ceiling is a sign of a design gap, not a staffing gap.

**Watch two trends.** Regulation keeps creating standing obligations with deadlines, such as data sharing under the Short-Term Rental Regulation and DSA (Digital Services Act) statements of reasons; each needs an owning team, not a project ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)). And AI coding agents let a team maintain more code but not more domain, so team boundaries should still follow domain depth ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)).

{id: organizing-stays-engineering--questions-to-ask}
## Questions to Ask

1. For each guest, partner and host journey with an SLO, which team is paged when it burns, and does that team see the end-to-end signal?
2. Who owns each shared contract, and does that owner run an engine that benefits from changing it?
3. How many production assets in the ownership catalog have no owning team or no on-call rotation today?
4. Which decisions can a team take alone, which need the forum, and which need the board, and is that written down?
5. What is the median lead time for a contract-level decision, and how many contract changes were merged without one last quarter?
6. When a channel manager starts rejecting reservations, which alert fires, who receives it, and which controls can they use without asking anyone?
7. How many supplier-integration pages per shift does the on-call receive, and what share is caused by partners with no guest impact in the next 48 hours?
8. For each production model, who can freeze it at three in the morning?
9. Which collaborations between teams have no end date?
10. If the group owns a channel manager or PMS, does it follow exactly the same certification and incident process as competing partners?

{id: organizing-stays-engineering--from-owners-to-migration}
## From Owners to Migration

An organization designed for the target architecture still has to get there while the old one is selling rooms. Keystone holds parts of nine contexts and Burrow of seven, and the teams of Org Design v1 own engines that do not yet exist alongside monoliths that still take every booking. [Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace) turns to that problem: moving a live booking platform to the new boundaries without losing reservations or money on the way.

{id: organizing-stays-engineering--sources-and-evidence}
## Sources and Evidence

{id: organizing-stays-engineering--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Expedia Group, Inc. Form 10-K for fiscal year 2023](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000007/expe-20231231.htm), Expedia Group / SEC, 2024 — 2020 unification of technology, product, data engineering and data science teams.
- [Expedia Group, Inc. Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm), Expedia Group / SEC, 2026 — platform operating model; unified front-end stack in 2023; brand general managers in 2024.
- [Expedia Group first quarter 2024 earnings release](https://www.sec.gov/Archives/edgar/data/1324424/000132442424000024/earningsrelease-q12024.htm), Expedia Group / SEC, 2024 — Vrbo's slower recovery after re-platforming.
- [Node.js at scale, rebalanced: how we cut cost by 38%](https://medium.com/booking-com-development/node-js-at-scale-rebalanced-how-we-cut-cost-by-38-62ce247a3002), Booking.com Engineering, 2026 — page-owning teams and section ownership with Module Federation.
- [MySQL at Booking.com (SREcon24 EMEA slides)](https://usenix.org/system/files/srecon24emea_slides-androulidakis.pdf), Androulidakis / USENIX, 2024 — database team owns infrastructure, "not data".
- [The Great Migration: from Monolith to Service-Oriented](https://www.infoq.com/presentations/airbnb-soa-migration/), Jessica Tai / InfoQ (QCon SF), 2018 — Monorail committers and deploy blockage; service types and dependency direction.
- [Incident Management at Airbnb](https://medium.com/airbnb-engineering/incident-management-ae863dc5d47f), Airbnb Engineering, 2022 — "over a thousand micro services with hundreds of small teams".
- [Viaduct, five years on](https://airbnb.tech/infrastructure/viaduct-five-years-on-modernizing-the-data-oriented-service-mesh/), Airbnb Tech, 2025 — more than 130 teams hosting code in a shared data-oriented service mesh.
- [How we cut the coupling tax in a post-booking API](https://medium.com/agoda-engineering/how-we-cut-the-coupling-tax-in-a-post-booking-api-2156a3175538), Agoda Engineering, 2026 — modular monolith with domain components enforced by architecture tests.

{id: organizing-stays-engineering--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Being On-Call](https://sre.google/sre-book/being-on-call/), Andrea Spadaccini, in *Site Reliability Engineering*, Google / O'Reilly, 2016 — two incidents per 12-hour shift; minimum rotation of eight on one site or six per site on two.
- [Team Topologies key concepts](https://teamtopologies.com/key-concepts), Team Topologies, n.d. — definitions of the four team types, three interaction modes and cognitive load.

{id: organizing-stays-engineering--research-and-practitioner-sources}
### Research and practitioner sources

- [How Do Committees Invent?](https://www.melconway.com/Home/Committees_Paper.html), Melvin E. Conway, *Datamation*, 1968 — designs copy the communication structures of the organizations that make them.
- [Team Topologies: Organizing Business and Technology Teams for Fast Flow](https://teamtopologies.com/book), Matthew Skelton and Manuel Pais, IT Revolution, 2019 — team types, interaction modes, cognitive load and the inverse Conway maneuver.
- [Scaling the Practice of Architecture, Conversationally](https://martinfowler.com/articles/scaling-architecture-conversationally.html), Andrew Harmel-Law / martinfowler.com, 2021 — the advice process, decision records and the weekly architecture advisory forum.
- [Democratizing online controlled experiments at Booking.com](https://arxiv.org/abs/1710.08217), Kaufman, Pitchforth and Vermeer / arXiv, 2017 — four practices that spread experimentation across a decentralized organization.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
