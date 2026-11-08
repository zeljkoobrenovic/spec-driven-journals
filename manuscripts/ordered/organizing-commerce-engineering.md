{id: organizing-commerce-engineering}
# 44. Who Builds and Who Owns: Teams, Vendors, Agencies and Governance

![Who Builds and Who Owns: Teams, Vendors, Agencies and Governance — logo](commerce-platform-architecture/posts/44-organizing-commerce-engineering/assets/images/44-organizing-commerce-engineering/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn who should own each system, integration and app, how to shape a small team around journeys, and how to work with agencies and vendors.

> **KEY POINTS:**
>
> * **Ownership follows money unless it is designed.** An agency is paid to build and a vendor to keep you subscribed; neither is paid to own a connector after launch. The ownership map, one row per system, integration and app with a named owner, is the merchant's first governance artifact, and most incidents at Kestrel & Pine trace to a blank cell in it.
> * **Shape teams around journeys, not vendors.** A team per system reproduces the integration problem in the organization chart. For ten to twenty people the honest shape is one or two stream-aligned teams by journey (buy; fulfill and return), one pair that owns the integration layer as an internal product, and vendors and agencies as services with explicit contracts.
> * **Govern lightly, but govern the facts.** Decision records for ownership, vendor and app decisions; one writer per fact; a contract card per integration; a quarterly app review; API versions pinned and recorded. Heavier process will not be followed by fourteen people, and lighter process lets the Secret Agent back in.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-commerce-platforms-go-wrong):**
>
> * **The Lynchpin** — a capability customers depend on runs through one agency, one consultant or one engineer, with no exit plan.
> * **The Secret Agent** — an app, script or integration changes stock, prices or money with no named owner and no record of what it may touch.
> * **The Spaghetti Junction** — connectors built by whoever was available when a channel arrived, each with its own owner or none, and no inventory.

An order appears in checkout but never reaches the warehouse. The platform vendor, connector partner and agency may each confirm that their own component is working. The merchant still needs someone to trace the whole path, identify the failed handoff and restore the order. Supplier contracts do not necessarily assign that responsibility, so it must be owned explicitly.

The owner needs authority and information to follow a flow across supplier boundaries. This chapter explains who defines the flow, watches it, changes it and recovers it, so an incident does not become a series of referrals between vendors. It covers team structure, agencies, contracts and engineering practices a small team can sustain on rented software.

The setting is a merchant with roughly a dozen engineers, an agency and several vendors. Its job is to coordinate those suppliers and integrations. Platform vendors organize much larger teams to build the products themselves; [Part XI — PRACTICE: How Others Built It](#part-11) examines those different constraints.

**Where we are in the order's journey.** Eva's jacket purchase and exchange at Kestrel & Pine, the fictional outdoor brand, cross several systems between 13 and 22 April 2027. For each handoff, someone must own the contract, monitoring, changes and recovery. "Probably the agency" is an unresolved responsibility.

{id: organizing-commerce-engineering--setting-the-scene-at-kestrel-pine-the-ownership-map}
## Setting the Scene at Kestrel & Pine: The Ownership Map

When Noor Visser becomes Head of Engineering in January 2027, Kestrel & Pine has thirteen systems, 34 integrations and 41 apps. On **8 February**, a marketplace connector retires an API version. A 2021 agency script stops sending stock to bol, but nobody acts until seller support escalates canceled orders two days later.

The agency says the script falls outside its retainer. Ecommerce Manager Milan Petrov did not know it existed. This is the **Deprecated Endpoint** incident: a published change meets an unowned dependency.

Noor maps each system, integration and app to a business owner, technical owner, supplier, renewal date, API version and write permissions. The hosted integration tool, or **integration platform as a service (iPaaS)**, belongs to Ruben Alves's team. The planned **order management system (OMS)** and **product information management system (PIM)** need owners too.

January's inventory found **13 of 34 integrations unowned**. Eight receive owners; **five remain unassigned in April 2027**, the date of the table below.

| What | Count | Owned by the integration team | Owned by the agency | Owned by a vendor or partner | No named owner |
| --- | --- | --- | --- | --- | --- |
| Integrations | 34 | 14 (flows in the iPaaS, Ruben Alves' team) | 9 (scripts, mostly from 2019–2022) | 6 (vendor connectors, including the ERP partner's platform↔ERP connector) | **5** |
| Installed apps | 41 | — | 22 installed by the agency | — | 19 installed by various people; 6 unused; **3 write inventory** |
| Systems | 13 | Business owner known for all; technical owner known for 8 | — | — | 5 systems with no technical owner inside the company |

The five integrations still unowned in April included the bol stock script, a price-list export to the German storefront (the one behind the **Price Drift** of October 2026: €179 instead of €199 for nine days, about €8,200 of margin) and the pre-order app's inventory write (the **App That Wrote Stock**, March 2026). Three of the ten incidents in the ledger sat in the blank cells of one spreadsheet. That is the whole case for the map: **the incidents were not caused by bad code; they were caused by code with no owner.**

{id: organizing-commerce-engineering--what-owning-means}
## What Owning Means

Before team shapes, a definition, because "owner" is used loosely. To **own** a system, integration or app is to carry five duties: to **decide** its contract (what it does, which fields, which direction, how often, which system is the source of truth); to **change** it, or approve changes; to **watch** it, with a monitor and a reconciliation that says when it is wrong; to **fix** it, which means being the one called at 20:40 on Black Friday; and to **retire** it when it is no longer needed or when the vendor retires what it depends on. An agency can do the second and, under contract, the fourth; it will rarely do the first, the third or the fifth, because it is not paid to.

![Loop of five ownership duties around one integration pipe: decide, change, watch, fix and retire.](commerce-platform-architecture/posts/44-organizing-commerce-engineering/assets/images/44-organizing-commerce-engineering/44-five-duties-of-an-owner.jpeg)

**Figure 1:** *To own a system, integration or app is to carry five duties: decide its contract, change it, watch it, fix it and retire it.*

Ownership follows money unless it is designed. The vendor-side economics are public. Shopify's partner page (undated, accessed November 2026) pays a partner that builds or transfers a store 20% of the monthly platform fee plus 0.1% of eligible GMV (gross merchandise value: the order value that passes through the platform) for four years, and a one-time $2,500 for a Plus or enterprise referral; partners are tiered Silver to Diamond on attributed GMV and attributed shops, and the older tiers retire on 1 January 2027. An agency on such a program is paid by the platform for keeping the merchant on it and by the merchant for building. Nothing in that arrangement pays for owning a connector after launch, for a reconciliation job, or for an exit. This is not a criticism of agencies; it is the reason the merchant must design ownership rather than inherit it.

A few terms the rest of the chapter uses. A **system of record** is the one system whose value is the truth when copies disagree ([Who Owns the Truth: Boundaries, Bounded Contexts and Systems of Record](#boundaries-and-systems-of-record)). An **integration contract** is a short written agreement for one flow: fields, direction, frequency, source of truth, what happens on a repeat or a failure ([APIs, Events, Files and Middleware: How Commerce Systems Talk](#integration-styles)). An **ADR** (architecture decision record) is a one-page note of a decision, its context and its consequences. A **sandbox** is a copy of a service where nothing real happens. An **API version** is a dated edition of a vendor's interface that the vendor promises to keep working for a stated period. A **stream-aligned team** owns one flow of work end to end; a **platform team** provides internal services to other teams.

{id: organizing-commerce-engineering--the-ownership-map}
## The Ownership Map

The map is a table, kept where the integration inventory of [APIs, Events, Files and Middleware: How Commerce Systems Talk](#integration-styles) is kept, and reviewed quarterly. Its columns:

| Column | What goes in it | Why |
| --- | --- | --- |
| Item | System, integration or app, by role name | One row per thing that can fail |
| Business owner | The manager accountable for the outcome (Milan for the storefront, Sanne de Wit for the ERP, Daniel Okafor for the WMS) | Decides priorities and accepts risk |
| Technical owner | The named engineer, team or partner who decides, changes, watches, fixes and retires | The person called |
| Builder and vendor | Who built it and who runs it | Separates "who wrote it" from "who answers for it" |
| What it may write | The facts it changes (stock, price, order status, refunds) and in which system | The Secret Agent check: one writer per fact |
| Contract | Renewal date, notice period, exit terms, support hours | Vendor management lives here |
| Depends on | API versions pinned, platform release tested against, vendor deprecation calendar | The Pulled Rug check |
| Watched by | The monitor and the reconciliation job, and who reads them | Ownership without watching is a name on a list |

Two rules make the map more than documentation. **Every row has a technical owner inside the company**, even when the builder is a partner; the owner may be the person who manages the partner, but the row is never blank. And **no fact has two writers**: if two rows claim to write stock in the platform, one of them is wrong, and the map says which. At Kestrel & Pine the second rule removed the pre-order app's inventory permission and became Waypoint decision W1's organizational half.

![Diagram: Kestrel & Pine's ownership map in outline](commerce-platform-architecture/posts/44-organizing-commerce-engineering/assets/images/44-organizing-commerce-engineering/fig01-kestrel-pine-s-ownership-map-outline.jpeg)

**Figure 2:** *Kestrel & Pine's ownership map in outline: every system has a business owner and a technical owner inside the company, the agency is a contributor, and the five integrations still unowned in April and the three stock-writing apps are assigned to the integration pair until retired or re-homed.*

{id: organizing-commerce-engineering--team-shapes-for-a-commerce-merchant}
## Team Shapes for a Commerce Merchant

Conway's 1968 paper observed that organizations "are constrained to produce designs which are copies of the communication structures of these organizations." In a merchant this works in reverse: a landscape of a dozen vendors pushes the organization into one team, or one person, per vendor, and the handoffs between systems become handoffs between people who report to different managers. **The organization copies the vendor landscape, and the vendor landscape's gaps become the organization's.**

*Team Topologies* (Skelton and Pais, 2019) gives the vocabulary that fits a small team. Four team types: **stream-aligned** (aligned to a flow of work from a segment of the business domain), **platform** (an internal product that accelerates stream-aligned teams), **enabling** (helps a team overcome obstacles and detects missing capabilities) and **complicated-subsystem** (where deep technical expertise is needed). Three interaction modes: collaboration, X-as-a-service, facilitation. One premise: teams can only handle so much complexity before breaking down. The vocabulary was written for software companies; the mapping to a merchant is mine.

{id: organizing-commerce-engineering--the-options}
### The options

**By system (one team or person per vendor).** The default a vendor landscape produces: the platform person, the ERP person, the WMS person, the agency for the storefront. Cheap to set up, matches support contracts, and reproduces every integration gap as an organizational gap. Nobody owns the order's journey.

**By journey (stream-aligned).** One team owns "buy" (storefront, catalog publication, checkout, marketplaces listings, promotions) and one owns "fulfill and return" (order hub, warehouse integration, shipping, returns, EDI, the electronic exchange of orders and invoices with trading partners). Each team touches several vendors; each handoff inside a journey has one owner. The integrations between the two journeys (the order leaving checkout for the OMS) need a contract between the teams.

**By layer (front end, integration, data).** A storefront team, an integration team, a data team. Fits the skills most merchants hire (front-end, back-end, data) and makes the integration layer a product with an owner. The risk is that the integration team becomes the bottleneck for every change and nobody owns a journey end to end.

**Agency-led.** The agency owns the storefront and the apps; the merchant owns the accounts and a backlog. Right at the Starting stage, workable at the Growing stage, and the origin of most Omnichannel-stage incidents when the merchant has not taken the joins in-house.

| | By system | By journey | By layer | Agency-led |
| --- | --- | --- | --- | --- |
| Who owns the order's journey | Nobody | A team | Nobody; the layers do | The agency, implicitly |
| Who owns the integration layer | The vendor connector or nobody | Must be assigned separately | The integration team | The agency or nobody |
| Fits team size | Any | 8 and up (two teams of 3–5 plus a pair) | 10 and up | 1–5 |
| Handoffs become | Tickets between people | Contracts between two teams | Queues into the integration team | Change requests |
| Main risk | The Spaghetti Junction in the org chart | Both teams need the same integration pair | The bottleneck | The Lynchpin |
| When it fits | Starting; a Group's shared-service vendor management | Omnichannel | Omnichannel with a strong integration lead | Starting, early Growing |

**My recommendation for ten to twenty people** combines the second and third: one or two stream-aligned teams by journey, one pair (not a team) that owns the integration layer, the ownership map and the reconciliation jobs as an internal product, the data engineers as a second small platform function under the data lead, and the vendors and agency as X-as-a-service providers with written contracts. The pair, not a team, because at this size a full integration team becomes the bottleneck the by-layer option warns of. The condition under which this does not hold: fewer than eight engineers, where one journey team plus one integration engineer is all the structure the people can carry.

Two public cautions bound the autonomy a merchant gives its teams. Henning Jacobs' retrospective of March 2020 on a decade at Zalando reports that team autonomy over technology choice produced similar services "written in six languages", which "hurts productivity at scale", and that a standard stack would have been "a major win".

Uber's July 2020 account of its domain-oriented architecture describes about 2,200 microservices in which a root-cause investigation could run through fifty services owned by twelve teams.

Both are six years old and describe organizations a hundred times larger than any merchant; the lesson scales down without change: **journey teams need a shared integration standard, or each will build its own connector to the same ERP.** Werner Vogels' 2006 line "you build it, you run it", relayed by AWS's blog at the time, is the other half: the team that changes a flow is the team paged when it fails.

![Diagram: Kestrel & Pine's 2027 team shape](commerce-platform-architecture/posts/44-organizing-commerce-engineering/assets/images/44-organizing-commerce-engineering/fig02-kestrel-pine-s-2027-team-shape.jpeg)

**Figure 3:** *Kestrel & Pine's 2027 team shape: two journey teams, an integration pair that serves both as an internal product, a data pair, shared application support, and the agency and vendors as services under contract.*

{id: organizing-commerce-engineering--working-with-agencies-and-implementation-partners}
## Working With Agencies and Implementation Partners

An agency or implementation partner builds what the merchant cannot staff: the theme, the first apps, a replatforming, an ERP implementation. Hobbycraft's 2022 move to Salesforce Commerce Cloud, reported by a trade site in June 2022, was built by an agency after a competitive pitch, using the agency's accelerator and a stack of six third-party services; the article reports the build, not the outcome, which is typical of agency-sourced evidence. The vendor-side mechanisms for agency work are structural: Shopify's development stores exist so a partner can build a store and transfer it to the merchant, with real transactions disabled until transfer (undated, accessed November 2026); Salesforce's cartridge path layers partner-built code over the vendor's base.

The rules I use, stated as judgement because no dated study of merchant–agency practice in the Netherlands, Belgium or Germany could be found:

- **The merchant owns the repository, the vendor accounts, the API credentials, the ownership map and the decision records.** The agency commits to the merchant's repository and holds review rights, not ownership. If the agency holds the platform login, the merchant has a Lynchpin.
- **Every custom module, app or script the agency builds is a row in the map** with its scopes (what it may read and write), its pinned API version, the platform release it was tested against, and an exit plan: who could maintain it if the agency left.
- **The statement of work names the API versions and platform releases the deliverable is tested against**, and a deprecation clause: when a vendor announces a retirement, who updates what by when.
- **Ownership after launch is written down before launch.** Either the agency owns the row under a support contract with a named engineer, or the merchant's team does, from the day of go-live. "We'll see" means nobody.
- **Separate building from keeping.** Pay the agency for the first; staff the second.

Kestrel & Pine's agency has been retained since 2017 at €14,000 a month for the theme, apps and small integrations. The 2027 statement of work, after the map, lists each of its nine scripts with an owner and a pinned version; three scripts that write to stock or prices moved in-house to the integration pair, and the rest stay with the agency under a named engineer *(illustrative)*. The ERP partner's platform↔ERP connector, built in 2023, gets the same treatment: the partner maintains it; Ruben's pair owns the contract, the monitor and the reconciliation.

{id: organizing-commerce-engineering--vendor-management-what-the-contract-must-say}
## Vendor Management: What the Contract Must Say

A merchant on rented software is governed by its vendors' terms more than by its own policies. Shopify's Terms of Service, last updated 20 October 2026, provide the services "as is" and "as available", do not warrant that they "will be uninterrupted, timely, secure, or error-free", and reserve the right to modify the services "for any reason, without notice and at any time". Plus and enterprise agreements may add service levels; none was available to verify, so ask for the actual agreement rather than a marketing uptime figure.

What a merchant can govern is its own dependence. The **vendor card**, one per vendor, sits beside the ownership map:

| Field | What to record | Dated example |
| --- | --- | --- |
| Term and notice | Contract length, renewal, notice period | Shopify Plus is sold on one- or three-year terms (pricing page, accessed 2026-11) |
| Versioning and deprecation | How the vendor versions its API and how long versions live | Shopify releases an API version quarterly, supports each for at least twelve months, and "falls forward" retired versions to the oldest supported one (developer documentation, accessed 2026-11); Adobe Commerce gives each release three years of standard support and will stop maintaining cloud environments on unsupported versions from 1 June 2027 (lifecycle policy, accessed 2026-11); WooCommerce states that backward compatibility between releases "is not guaranteed" |
| Rate limits and quotas | What the tenant may call, shared by every app and connector | Shopify's GraphQL Admin API bucket refills at a plan-dependent rate, from 100 to 2,000 points a second (accessed 2026-11); every app on the store draws from it ([Many Merchants, One Platform: Multi-Tenancy, Pods and Isolation](#multi-tenancy-and-isolation)) |
| Export and exit | What data can be exported, in what form, at what cost | The EU Data Act (Regulation 2023/2854) prohibits switching charges for data processing services from 12 January 2027; whether hosted commerce platforms fall under it is an open legal question as of November 2026 |
| Extension retirement | Which mechanisms the vendor has retired and on what notice | Shopify Scripts and the Script Editor were retired on 30 June 2026; scripts no longer run on any store (help documentation, accessed 2026-11) |
| Service levels in your units | Not the vendor's uptime but your checkout success rate, order-to-WMS latency, stock-sync lag | Google's SRE book (2017) defines an SLO as a target for a measured service level and an SLA as the contract with consequences; the vendor's SLA covers its uptime, and the merchant's integration SLOs are nobody else's |
| Residency and tenancy | Which region each SaaS system was provisioned in | commercetools' regions are isolated and moving is a migration, not a setting (documentation, accessed 2026-11) |

The versioning row deserves emphasis because it is the Pulled Rug's calendar. Kestrel & Pine's Deprecated Endpoint was a published date that nobody had put on a calendar. The vendor card turns each vendor's deprecation policy into a dated list, and the ownership map says who updates which row by when. [Promises Between Systems: API Contracts, Webhooks and Versioning](#api-contracts-and-versioning) owns the mechanics.

{id: organizing-commerce-engineering--governance-that-fourteen-people-will-follow}
## Governance That Fourteen People Will Follow

Governance in a merchant has one purpose: to keep the ownership decisions true after the meeting ends. Heavy process (architecture boards, review gates, templates that take an afternoon) will not survive a team of fourteen with a peak season. Light process can, if it is specific.

**Decision records.** Michael Nygard's note of November 2011 defined the architecture decision record: a short text file with title, context (the forces at play, "described as neutral facts, often in tension"), decision ("We will…"), status (proposed, accepted, deprecated, superseded) and consequences. Without one, a newcomer can only "blindly accept the decision" or "blindly change it". In a merchant the decisions worth a record are the ownership ones (which system is the system of record for stock, price, product, order), the vendor ones (why this OMS, with what exit) and the app ones (which apps may write stock). Kestrel & Pine's Waypoint decisions W1–W8 are ADR-shaped; Noor numbered them as the first eight records *(illustrative)*, and the 2029 review is the date on which W4 is re-opened.

**Standing rules.** Rules that need no meeting, because they are checkable from the map:

| Rule | Check | Pattern it prevents |
| --- | --- | --- |
| One writer per fact | The map's "what it may write" column has no duplicates | The Secret Agent, The Phantom Stock |
| Every integration has an owner, a contract card, idempotent handling and a reconciliation job (Waypoint W5) | No blank cells; each row names its reconciliation | The Spaghetti Junction, The Message in a Bottle |
| Every app's scopes are recorded and reviewed quarterly; unused apps are removed | 41 apps, 6 unused, 3 writing stock becomes 34 apps by July 2027, none unused and none writing stock | The Secret Agent |
| Every integration pins an API version, recorded with the vendor's retirement date | The vendor card's calendar has no past-due rows | The Pulled Rug |
| No change to stock, price or order flows in the four weeks before peak without the peak owner's approval | A dated freeze in the calendar | The First Snowfall |

**A lightweight review.** One 45-minute **architecture hour** a week, open to both journey teams, the integration pair and the data pair, with a standing agenda: new rows in the map, proposed ADRs, deprecation dates in the next ninety days, and one incident replayed against the map. No slides. The output is edits to the map and to ADRs. At Kestrel & Pine this hour replaced three vendor-specific status meetings *(illustrative)*.

{id: organizing-commerce-engineering--the-product-manager-in-a-merchant}
## The Product Manager in a Merchant

A merchant that buys everything still needs its own product managers, for a reason of asymmetry. The vendor's product manager optimizes the platform's product: GMV through it, tenancy, the app ecosystem. The merchant's product manager's product is **the order's journey**: the share of visits that become orders, the average order value, the share of orders delivered when promised, the return rate and the cost of a return, the time from "where is my order?" to an answer. Those are the metrics of [Who Sells What to Whom: Business Models and the Economics That Shape Architecture](#commerce-business-models), and no vendor optimizes them for a particular merchant. Kestrel & Pine's two product managers sit one per journey team; their backlogs are written in those metrics, and a vendor's roadmap is an input, not a plan.

{id: organizing-commerce-engineering--engineering-practices-on-rented-software}
## Engineering Practices on Rented Software

**Environments and sandboxes.** On SaaS the merchant never gets a full copy of production. Shopify's development stores are for development and testing only, cannot process real transactions and are capped at 250 per organization (accessed November 2026); Stripe's sandboxes are isolated test environments where "card networks and payment providers don't process payments" (accessed November 2026); Adobe Commerce Cloud Pro provides integration, staging and production environments, with staging on dedicated hardware matching production (accessed November 2026).

The gap is the chain: no vendor offers a sandbox of platform plus payment provider (PSP) plus ERP plus WMS together. Zalando's 2020 account of its Cyber Week preparation describes order-flow simulators that place marked test orders which fulfillment skips, exercising inventory and payments in production.

A small team can copy the pattern at small scale: a test customer, a test SKU, an order flag the WMS and the ERP recognize, and a weekly run through the whole chain.

**Release management.** The release calendar is set by the vendors: quarterly API versions on hosted platforms, yearly release lines on suites, connector updates whenever a marketplace or carrier changes its interface. The cheapest control is to pin the version in every connector and record it in the map.

**Feature flags.** Pete Hodgson's taxonomy of October 2017 (release, experiment, ops and permissioning toggles) gives the team a vocabulary: release toggles to ship unfinished checkout changes dark, ops toggles as the peak-day switch-off list of [Black Friday Every Year: Peak Load, Resilience and Recovery](#peak-load-and-reliability), permissioning toggles for staff-only or B2B-only features.

**AI coding tools.** The dated evidence is mixed and worth stating plainly. DORA's 2024 report (October 2024) found more than 75% of respondents relying on AI for at least one daily task, with a 25% increase in adoption associated with small gains in documentation and code quality but an estimated 1.5% lower delivery throughput and 7.2% lower delivery stability. DORA's 2025 report calls AI "an amplifier, magnifying an organization's existing strengths and weaknesses".

METR's randomized trial of July 2025, with sixteen experienced developers on 246 tasks in mature repositories, measured a 19% *increase* in completion time with early-2025 tools, while the developers believed they had been 20% faster. Shopify's CEO wrote to staff in April 2025 that "reflexive AI usage" is a baseline expectation and that teams must show why AI cannot do a task before asking for headcount.

For a commerce team the stability finding is the one that matters: AI tools raise output on exactly the code that touches stock and prices (connectors, theme code, app glue), so tests against sandboxes, small batches, review and the one-writer rule are preconditions, not afterthoughts. AI shifts the bottleneck from writing a connector to owning it.

{id: organizing-commerce-engineering--across-scale-stages-when-it-fits-and-when-it-limits}
## Across Scale Stages: When It Fits and When It Limits

| | Starting | Growing | Omnichannel | Group |
| --- | --- | --- | --- | --- |
| **Typical shape** | Founder plus the platform's support; an agency for the theme | The agency builds; a first engineer; the ERP partner | 10–20 people: journey teams, an integration pair, a data function | Stream-aligned teams per brand or journey; a platform team; vendor management as a function |
| **Who owns integrations** | The platform's own connectors; nobody else needed | The agency or the partner, then nobody after launch | The integration pair, by map | The platform team, as an internal product with API guidelines |
| **What becomes necessary** | The founder holds every account; an app list with scopes | The first engineer owns the map, the repository and the API pins; a staging store with marked test orders | Named owner per row; ADRs; the architecture hour; quarterly app review; a peak owner | Shared standards across teams; an acquisition integration playbook; group vendor contracts |
| **Warning signs of outgrowing it** | A second channel arrives and the agency builds the connector with no owner | Support tickets route to the agency; an incident reveals a script nobody knew | Both journey teams build their own connector to the same ERP; the integration pair is the bottleneck for every change | Teams choose their own stacks and build the same service twice (Zalando's six languages) |
| **Kestrel & Pine** | 2016–2018 | 2019–2022: Ruben Alves from 2022 | 2027 shape above | Deferred to the 2029 review |

The judgement: the team shape should change one stage *before* the system landscape does, because the owner has to exist before the connector is built. Kestrel & Pine hired its lead integration engineer in 2022, a year after the connector and the iPaaS arrived; the thirteen integrations without a named owner in January 2027 are the cost of that year.

{id: organizing-commerce-engineering--in-practice-kestrel-pine-before-and-after}
## In Practice: Kestrel & Pine, Before and After

**Before (January 2027).** Thirteen systems; 34 integrations of which thirteen had no named owner; 41 apps of which three wrote inventory; the agency holding the theme, 22 apps and nine scripts on a €14,000 monthly retainer; the ERP partner holding the platform↔ERP connector; one engineer (Ruben) owning the iPaaS and, informally, everything nobody else owned; technology spend of about €2.6 million a year. Support answered "where is my order?" from five tabs. Nobody had a calendar of vendor deprecation dates.

**After (from April 2027).** The ownership map with no blank cells. Two journey teams (Buy: three storefront and apps engineers and a product manager, with Milan as business owner; Fulfil and Return: two back-end engineers and a product manager, with Daniel and Lea as business owners), the integration pair (Ruben and one back-end engineer) owning the iPaaS, the contracts, the reconciliation jobs and the map, the data pair under Hanna Berg, and two application support specialists serving both journeys. ADRs KP-001 to KP-008 are Waypoint W1–W8. The two integration engineers Waypoint adds from mid-2027 join one journey team each, so the integration pair stays a pair. A vendor card per vendor with a deprecation calendar. The agency under a statement of work that lists each script with an owner and a pinned version. The architecture hour on Tuesdays.

![Before and after: a tangle of unowned integrations held by one engineer, then neat integrations each with an owner tag.](commerce-platform-architecture/posts/44-organizing-commerce-engineering/assets/images/44-organizing-commerce-engineering/44-ownership-before-after.jpeg)

**Figure 4:** *Before, 13 of 34 integrations had no named owner and one engineer held whatever nobody else owned; after, the ownership map has no blank cells.*

**The Deprecated Endpoint, replayed.** With the map, the bol stock script has a row: technical owner the integration pair, pinned version recorded, the connector's retirement date on the vendor card ninety days ahead, and a monitor on stock-sync lag to bol. The script is updated in the week the retirement is announced, or retired in favor of the connector's native stock flow. The two stale days do not happen. The cost of the control is one row and one calendar entry.

{id: organizing-commerce-engineering--when-it-goes-wrong}
## When It Goes Wrong

**The Lynchpin leaves.** The one EDI consultant who built Bergzicht's connection, or the one engineer who knows the iPaaS, resigns. Detection: the map shows one name on many rows. Recovery: pair every critical row with a second name, document the contract card, and treat a single-name row as a risk register entry with a date.

**The agency contract ends.** On exit the agency holds the theme repository, the app credentials and the scripts. Detection: the merchant cannot deploy a theme change without the agency. Recovery: repository and credentials transfer as a condition of every statement of work, from the first one; a handover run through the map, row by row.

**The vendor retires the mechanism.** Shopify's retirement of Scripts on 30 June 2026 is the dated example of a platform ending an extension mechanism on a published date; Adobe's June 2027 enforcement of supported versions on its cloud is another. Detection: the vendor card's calendar. Recovery: migration to the replacement mechanism (Functions, in Shopify's case) planned a year ahead, owned by the row's owner ([Apps, Plugins and Functions: Extensibility and Ecosystem Governance](#extensibility-and-app-ecosystems)).

**The Secret Agent returns.** A new app, installed by a marketer to run a pre-order campaign, asks for an inventory-write scope and gets it. Detection: the quarterly app review, or better, an install rule that routes any write scope on stock, price or orders through the integration pair. Recovery: revoke the scope, reconcile the stock the app touched (the May 2027 reconciliation found 2.3% of active variants different, most from such apps), and record the decision.

**Two teams, two connectors.** Both journey teams integrate with the ERP, each its own way. Detection: two rows in the map with the same target and different contracts. Recovery: the integration pair owns one flow and the other team consumes it; this is what the pair is for.

{id: organizing-commerce-engineering--what-to-take-away}
## What to Take Away

**Established.**

- Organizations produce designs that copy their communication structures (Conway, 1968); a merchant organized one team per vendor reproduces its integration gaps in the organization chart.
- Vendor partner programs pay agencies to build and to keep merchants on the platform (Shopify: 20% of the platform fee plus 0.1% of GMV for four years, accessed 2026-11), not to own integrations after launch; ownership must be designed by the merchant.
- Decision records with context, decision, status and consequences (Nygard, 2011) are the lightest durable form of architecture governance and fit a team of any size.
- Autonomy without shared standards is costly at scale (Zalando's 2020 "six languages"; Uber's 2020 fifty-service investigations), and the lesson holds for two journey teams sharing one ERP.

**Depends on context.**

- Journey teams plus an integration pair fit ten to twenty people at the Omnichannel stage; below eight engineers, one journey team and one integration owner is all the structure the people can carry; at the Group stage the pair becomes a platform team.
- Agency-led engineering is right at the Starting stage and workable at the Growing stage, provided the merchant holds the accounts, the repository and the map from the first contract.
- How much to formalize vendor management depends on the vendors' versioning policies: quarterly dated API versions with twelve-month support (Shopify) need a calendar; three-year release lines (Adobe Commerce) need an upgrade plan; "not guaranteed" compatibility (WooCommerce) needs a test suite.
- AI coding tools raise output where the evidence says stability falls (DORA 2024); their value in a commerce team depends on the tests, review and scope governance already in place.

**The author's synthesis.**

- The ownership map is the merchant's first architecture artifact and the only one that prevents incidents on its own: at Kestrel & Pine three of ten incidents sat in its blank cells.
- Change the team shape one stage before the system landscape changes; the owner must exist before the connector does.

{id: organizing-commerce-engineering--questions-to-ask}
## Questions to Ask

1. Is there a map with one row per system, integration and app, and does every row name a technical owner inside the company?
2. Which facts (stock, price, order status, refunds) have more than one writer, and which row says so?
3. Who holds the platform, PSP, ERP and connector logins, the repository and the API credentials: the merchant or the agency?
4. Which vendor deprecation dates fall in the next twelve months, and who updates which integration by when?
5. Does the agency's statement of work name the API versions and releases the deliverable is tested against, and who owns each deliverable after go-live?
6. Does any team own the order's journey end to end, or only systems?
7. Is there a written decision for which system is the system of record for stock, orders and product content, and when it will be reviewed?
8. How does a change to a stock, price or order flow reach production: through which review, which sandbox, which flag, and under which freeze before peak?
9. Which rows in the map carry one name only, and what happens if that person leaves?

Ownership answers "who"; the last chapter of this part asks what the next kind of actor, an AI agent that discovers, compares and buys, will need from the systems and the owners described here. Continue with [Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce).

{id: organizing-commerce-engineering--sources-and-evidence}
## Sources and Evidence

*Company, product and investor sources*

- [How to earn as a Shopify Partner](https://help.shopify.com/en/partners/how-to-earn), Shopify Help Center, n.d., accessed 2026-11 — partner revenue share and referral payouts.
- [Shopify Plus Partner Program](https://help.shopify.com/partners/plus-partners), Shopify Help Center, n.d., accessed 2026-11 — partner tiers by attributed GMV and shops; older tiers retiring 1 January 2027.
- [Development stores](https://shopify.dev/docs/apps/build/dev-dashboard/stores/development-stores), Shopify developer documentation, n.d., accessed 2026-11 — test stores cannot process real transactions; cap of 250.
- [API versioning](https://shopify.dev/docs/api/usage/versioning), Shopify developer documentation, n.d., accessed 2026-11 — quarterly versions, twelve-month support, fall-forward behavior.
- [GraphQL Admin API rate limits](https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits), Shopify developer documentation, n.d., accessed 2026-11 — plan-dependent bucket shared by every app on a store.
- [Script Editor](https://help.shopify.com/en/manual/checkout-settings/script-editor), Shopify Help Center, n.d., accessed 2026-11 — Scripts retired on 30 June 2026.
- [Shopify Terms of Service](https://www.shopify.com/legal/terms), Shopify, 2026 — services provided "as is" and modifiable without notice.
- [Shopify CEO: prove AI can't do the job before asking for headcount](https://www.cnbc.com/2025/04/07/shopify-ceo-prove-ai-cant-do-jobs-before-asking-for-more-headcount.html), CNBC, 2025 — the April 2025 memo.
- [Adobe Commerce lifecycle policy](https://experienceleague.adobe.com/en/docs/commerce-operations/release/planning/lifecycle-policy), Adobe Experience League, n.d., accessed 2026-11 — three-year standard support; cloud enforcement from 1 June 2027.
- [Adobe Commerce Cloud Pro architecture](https://experienceleague.adobe.com/en/docs/commerce-cloud-service/user-guide/architecture/pro-architecture), Adobe Experience League, n.d., accessed 2026-11 — integration, staging and production environments.
- [Getting started with extensions](https://developer.woocommerce.com/docs/extensions/getting-started-extensions/), WooCommerce developer documentation, n.d., accessed 2026-11 — backward compatibility not guaranteed.
- [Stripe sandboxes and test mode](https://docs.stripe.com/test-mode), Stripe documentation, n.d., accessed 2026-11 — isolated test environments where no payments are processed.
- [General concepts](https://docs.commercetools.com/api/general-concepts), commercetools documentation, n.d., accessed 2026-11 — isolated regions; data residency chosen at provisioning.
- [Astound Commerce enlists Hobbycraft for e-commerce replatforming project](https://retailtechinnovationhub.com/home/2022/6/14/astound-commerce-enlists-hobbycraft-for-e-commerce-replatforming-project), Retail Technology Innovation Hub, 2022 — an agency-led replatforming, agency-sourced.
- [How Zalando prepares for Cyber Week](https://engineering.zalando.com/posts/2020/10/how-zalando-prepares-for-cyber-week.html), Zalando Engineering, 2020 — order-flow simulators with marked test orders; production-readiness reviews; older than three years.
- [One decade in Zalando tech](https://srcco.de/posts/one-decade-in-zalando-tech.html), Henning Jacobs, 2020 — the cost of autonomy without a standard stack; older than three years.
- [Introducing Domain-Oriented Microservice Architecture](https://www.uber.com/blog/microservice-architecture/), Uber Engineering, 2020 — ownership blur across about 2,200 services; older than three years.
- [Werner Vogels interview relayed](https://aws.amazon.com/blogs/aws/acm_queue_inter), AWS News Blog, 2006 — "you build it, you run it"; twenty years old.

*Standards, regulation and official documentation*

- [Regulation (EU) 2023/2854 (Data Act)](http://publications.europa.eu/resource/celex/32023R2854), EU Publications Office, 2023 — switching charges prohibited from 12 January 2027; applicability to hosted commerce platforms open.
- [Service Level Objectives](https://sre.google/sre-book/service-level-objectives/), Google SRE book, 2017 — SLI, SLO and SLA definitions; older than three years.

*Research and practitioner sources*

- [How Do Committees Invent?](https://www.melconway.com/Home/Committees_Paper.html), Melvin Conway, 1968 — organizations produce designs that copy their communication structures.
- [Team Topologies: key concepts](https://teamtopologies.com/key-concepts), Matthew Skelton and Manuel Pais, n.d., accessed 2026-11 (book 2019) — the four team types and three interaction modes.
- [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions), Michael Nygard, 2011 — the architecture decision record; older than three years.
- [Feature Toggles](https://martinfowler.com/articles/feature-toggles.html), Pete Hodgson, 2017 — release, experiment, ops and permissioning toggles; older than three years.
- [Announcing the 2024 DORA report](https://cloud.google.com/blog/products/devops-sre/announcing-the-2024-dora-report), Google Cloud, 2024 — AI adoption associated with lower delivery throughput and stability.
- [State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report/), DORA, 2025 — AI as an amplifier of existing strengths and weaknesses.
- [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://arxiv.org/abs/2507.09089), METR (arXiv), 2025 — the randomized trial showing a 19% slowdown.

Kestrel & Pine is fictional; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.
