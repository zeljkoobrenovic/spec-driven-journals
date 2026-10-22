{id: extranets-and-host-tools}
# 10. Running the Supply Side: Extranets, Host Tools and Operations

![Running the Supply Side: Extranets, Host Tools and Operations — logo](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the supply-side workspace: the hotel extranet and its mobile companion, the host app, reservation exception queues, co-hosts and staff roles, turnover and check-in coordination, partner analytics and programs, and the APIs that professional managers use instead of the screens.

> **WHY THE BUSINESS CARES:** Partners and hosts spend their working day in these tools. When a closure does not stick, an exception is missed or a co-host needs the owner's password to do their job, the cost appears as walked guests, partner support contacts, account takeovers and suppliers who move their attention to a competitor's extranet.

> **WHY ARCHITECTS SHOULD CARE:** The extranet is not a set of screens over a database. It is one of several writers into supply, inventory, reservations, messaging and money, next to channel managers, property-management systems (PMS) and AI assistants. Unless the platform states who owns each field and each workflow, those writers overwrite each other and nobody can say why.

> **KEY POINTS:**
>
> * **One partner back-end, many clients, explicit ownership.** The web extranet, the mobile app, connectivity APIs and assistants all write to the same entities. Declare a system of record per field and per property, show it in the user interface, and make overrides restrictive, time-bound and logged, or the channel manager's next push silently undoes the partner's last decision.
> * **Delegation is a relationship, not a user flag.** Hotel staff, co-hosts, cleaners, property managers and their software act on behalf of an owner. Model each grant as party, scope, role, granted-by and validity, keep payout beneficiaries and tax parties separate from operating rights, and step up authentication on money. Otherwise suppliers share passwords, and attackers inherit them.
> * **Supply tools are operations software, and their data is marketplace data.** Reservation exceptions need owners, deadlines and escalation, not a list of e-mails. Partner analytics must come from the same metrics and features as ranking and programs, or partners see numbers that contradict the search results they observe.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Lost at the Front Desk** — reservations that fail delivery, need a reply or carry a special state end up as e-mails and unread badges instead of work items with an owner and a deadline.
> * **Connectivity Roulette** — when the extranet and the channel manager both write availability without an ownership rule, every partner edit is a gamble on which writer arrives last.
> * **The Hotel-Shaped Home** — forcing a hotel-staff permission model onto a home run by an owner, a co-host and a cleaner, or a one-person host app onto a 140-room hotel, breaks both.

Part II has so far modeled supply ([Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)), onboarded it ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)) and connected it to hotel systems and other platforms ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). This last chapter of the part covers the **supply product**, the hotel extranet and the host app, where suppliers then set prices, close calendars, answer guests, see what they are owed and decide whether the marketplace is worth their time. The guest product gets the design reviews and experiments; the supply product gets what is left.

The two marketplace types meet their suppliers in different places. An **accommodation marketplace** (OTA-style; OTA = online travel agency) mostly receives availability, rates and inventory (**ARI**) from a hotel's systems through channel managers ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)), so its **extranet** is a configuration console, a reservation workbench and a fallback. A **hosted-stays marketplace** mostly receives supply from people with phones, so its **host app** is the operating system of their business, until the host grows into a professional manager who wants an API instead.

This chapter owns four terms: **extranet**, **co-host**, **turnover task** and **partner analytics**. Later chapters build on its rules: the ARI model of Part III stores the overrides defined here ([Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model)), customer service reads the same exception queue ([When Something Goes Wrong: Customer Service and Recovery](#customer-service)), and partner analytics reads the metrics of [Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence). The reservation state machine, messaging, identity, account takeover and partner-program design belong to their own chapters ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging), [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access), [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)).

{id: extranets-and-host-tools--setting-the-scene-at-corvane-shared-passwords-and-closures-that-did-not-stick}
## Setting the Scene at Corvane: Shared Passwords and Closures That Did Not Stick

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs two supply products. Roomstead's **Partner Hub** is an extranet that has lived inside Keystone, the Java and Oracle monolith, since the mid-2000s, with a mobile app added in 2021 that calls a partner API on AWS. About **18%** of Roomstead's hotel room nights are managed in Partner Hub directly; the other **82%** arrive through **140** certified connectivity partners. Nookaway's **host app** and web dashboard sit on Burrow, the Django monolith, and serve **610,000** hosts, **82%** of whom have one listing, while professional managers with five or more listings hold **44%** of the **1.15 million** listings.

In September 2027, five months into the One Stay program, two unrelated reports reached Mariana Costa, the Group Chief Architect, in the same week.

**The first came from Nookaway.** On 6 September, after a run of host account takeovers, Rafael Mendes's team switched on step-up verification for new-device logins and for payout and bank-detail changes on accounts with five or more listings. Within ten days, hosts opened **3,900** support contacts that said, in different words, "my colleague has the phone with the code". The data team looked at device and location patterns and estimated that about **187,000** listings, **37%** of the listings held by professional managers, were operated through one owner login shared among several people. Burrow's 2016 co-host model was one flag on a listing: a co-host could do everything except receive money, see earnings or change payouts. **74,000** listings had a co-host. Managers who needed earnings reports, management-fee payouts or a cleaner who saw only the turnover schedule had no way to get them, so they logged in as the owner.

![Before, one owner login key passed among a manager, a co-host and a cleaner; after, each person holds their own key to a different door.](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/10-one-shared-login.jpeg)

**Figure 1:** *About 187,000 Nookaway listings were run through one owner login shared by several people, because the co-host flag could not give each of them their own scope.*

**The second came from Roomstead.** On 14 September, the front-office manager at **Hotel Miradouro**, the independent 84-room four-star hotel in Lisbon whose rates Duarte Silva manages through a cloud PMS and Corvane Connect, used the Partner Hub app to close "Twin" for 15–17 September after a water leak put four rooms out of order. At 02:00 the next morning, Corvane Connect's scheduled full synchronization pushed the PMS's view of availability, which still showed the four rooms as sellable, and reopened the room type on Roomstead. Two reservations arrived for rooms that did not exist that week. The hotel upgraded both guests at its own cost and opened a partner support case titled "Your system ignores my closures". Aisha Rahman's supply team then measured it: in August 2027, connected hotels made about **1.9 million** availability and closure edits in Partner Hub, and **23%** of them were overwritten by a connectivity push within 24 hours. Partner support had tagged **6,700** contacts that month as "change did not stick".

Both reports had one cause: Nookaway assumed one person runs a home, and Partner Hub assumed it was the only writer. One Stay had already decided to share identity, messaging, notifications, data and customer service across the brands, and to keep supply models and connectivity separate. The question for the architecture forum was narrower: **should Corvane build one partner workspace for hotels and homes, and if not, what must the two supply products share so that neither repeats these mistakes?**

{id: extranets-and-host-tools--what-the-supply-side-works-in}
## What the Supply Side Works In

- **Extranet.** The partner-facing application in which a property manages its presence on an OTA: setup, content, policies, rates and availability, reservations, messages, reviews, invoices and payouts, performance and programs. Today it is a web application plus a mobile companion. Booking.com's free Pulse app, for example, lets partners reply to guests with templates in 43 languages, receive alerts for new bookings, reviews, guest requests and sold-out dates, update availability and view invoices, while "the extranet remains the full management tool" ([Booking.com, Pulse](https://www.booking.com/propertyapp.en-gb.html), live page as of October 2026).
- **Host app.** The equivalent surface on a hosted-stays marketplace, built for one person running a few homes from a phone. Airbnb's 2025 annual report lists "scheduling, merchandising, integrated payments, community support, host protections, pricing tools, and feedback from reviews" ([Airbnb Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026).
- **Partner workspace.** My umbrella term for everything a supplier uses: extranet or host app, mobile app, supply-side APIs and notifications. It is a product, backed by several systems.
- **Co-host.** A person or business that operates a hosted-stays listing on behalf of its owner, with rights the owner grants. The OTA counterpart is **partner staff**: employees of a hotel, chain or management company with extranet roles.
- **Reservation exception.** A reservation that needs a human decision from the partner or host: undelivered, awaiting a reply, overbooked, card declined, no-show to mark, change requested. The state machine is in [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle); the exception is the workspace's view of it.
- **Turnover task.** A unit of on-property work derived from reservations (cleaning, linen, inspection, key or code handover), with a window bounded by one check-out and the next check-in.
- **Partner analytics.** The reporting a marketplace gives suppliers about their own visibility, conversion, demand, prices, quality and programs, usually benchmarked against comparable properties or listings.

Who uses which surface depends more on the supplier's size than on the marketplace type.

| Supplier | Main way they manage supply | What they still do in the marketplace's own tools |
| --- | --- | --- |
| **Chain or hotel group** | Central reservation system (CRS) and PMS through a connectivity partner | Contracts, content checks, programs, invoices, exceptions; often handled by a central e-commerce team |
| **Independent hotel** | PMS and channel manager, sometimes the extranet alone | Reservations, guest messages, reviews, closures in a hurry, payouts and invoices |
| **Professional property manager** | Vacation-rental PMS or channel manager through the marketplace's partner API | Messages, reservation issues, quality alerts, owner statements, staff and cleaner access |
| **Individual host** | The host app | Everything: calendar, price, messages, check-in instructions, reviews, payouts |

The table hides the fact that drives the architecture: **the same entity has several writers.** Miradouro's availability can be written by the PMS through Corvane Connect, by Duarte in the web extranet and by the front-office manager in the app. A Nookaway listing's calendar can be written by the host, a co-host, an iCal import ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)) and a PMS through the partner API.

{id: extranets-and-host-tools--architecture-one-partner-back-end-many-clients}
## Architecture: One Partner Back-End, Many Clients

The extranet should not own data. It should be a client of the domain services that own the property, the inventory, the reservations, the conversations and the money, with a thin backend-for-frontend (BFF) that composes them for screens.

![Extranet, mobile app, AI assistant and PMS all pass through one partner gateway and authorization before reaching listings, ARI, reservations and finance.](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/10-one-partner-back-end.jpeg)

**Figure 2:** *The partner workspace as clients of one partner back-end. Every client, human or machine, passes through the same authorization and the same field-ownership rules; the extranet is one client among several, not the owner of supply data.*

Booking.com's Connectivity APIs reach most extranet functions. They cover not only rates, availability and reservations but also Contacts, Licences, Promotions, Messaging, Guest Review, Opportunities, Reporting, Property scores and Market Insights ([Booking.com Connectivity APIs](https://developers.booking.com/connectivity/docs), live documentation as of October 2026).

The clients also need rules between them. For guest self-service requests, date changes and "cancel for less" "require response via the Extranet", and "Sending a message through the API will deactivate the property's ability to respond via the extranet" ([Booking.com Messaging API](https://developers.booking.com/connectivity/docs/messaging-api/understanding-the-messaging-api), live documentation as of October 2026). That is a **single-channel-of-reply rule**: two staff members must not answer the same request through different clients.

> **INFERENCE, NOT DOCUMENTED:** Booking.com's documentation shows the contract, not the implementation. Whether its extranet, Pulse and the Connectivity APIs share one back-end is not public. The architecture in Figure 2 is a reference design, not a description of Booking.com's systems.

{id: extranets-and-host-tools--field-ownership-the-rule-the-miradouro-closure-was-missing}
### Field ownership: the rule the Miradouro closure was missing

The fix is neither "last writer wins" nor "the extranet always wins" but a declared **system of record** per field group and per property, obeyed by the user interface and the APIs alike.

![Before, an app and a full sync both reach for the same availability key; after, a field-ownership table gives the key to one system of record.](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/10-two-writers-one-field.jpeg)

**Figure 3:** *When the app and the channel manager's full sync both believe they own availability, the last writer wins; a declared system of record per field group ends the tug of war.*

| Field group | Typical system of record (connected hotel) | Typical system of record (individual host) | What other writers may do |
| --- | --- | --- | --- |
| Room count, rates, restrictions | PMS or revenue-management system through the channel manager | Host app | Marketplace-only **restrictive override**: close or reduce, with an expiry, never open or raise |
| Calendar of a home | Vacation-rental PMS, if API-connected | Host app; iCal imports may only block | Block dates; never unblock a booked night |
| Descriptive content and photos | Extranet, or content API for chains | Host app | Propose changes for review |
| Policies (cancellation, house rules) | Rate plan in the PMS or extranet | Host app | None; policy changes need explicit confirmation |
| Reservation confirmation number | PMS | Not applicable | Read only |
| Guest conversation | Whichever client the property chose for that request | Host app or PMS | Read; reply only through the chosen client |
| Bank details, payout routes, tax data | Marketplace finance, owner only | Marketplace finance, owner only | None; step-up authentication and cooling-off period |
| Door codes and access | PMS or lock platform, if connected | Marketplace lock integration | Relay only |

Two rules make the table work.

1. **Show ownership where the edit happens.** If Partner Hub knows that Miradouro's availability is owned by Corvane Connect, the app should not offer a plain "close" button. It should say "Your channel manager controls availability. Close on Roomstead only until 17 September?" and add "Your PMS still sells these rooms on other channels: fix the room status in the PMS too."
2. **Make marketplace-side overrides restrictive and time-bound.** An override that can only close or reduce, expires, is logged with user and reason, and is reported to the connectivity partner protects the guest without pretending the marketplace is the source of truth. An override that can open inventory makes the extranet a competing writer and creates overbooking. The ARI model that stores overrides belongs to [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model).

Airbnb documents the same principle at the door. For PMS-managed locks, "Airbnb sends reservation details to the connected PMS", the PMS creates the code and Airbnb relays it, so Airbnb cannot see battery or offline status ([Airbnb Help, article 4163](https://www.airbnb.com/help/article/4163), live page as of October 2026). The professional's system owns the lock; the marketplace is a relay, and its app should not show a status it cannot know.

{id: extranets-and-host-tools--the-workspace-modules-and-what-they-need-from-the-platform}
### The workspace modules and what they need from the platform

| Module | Owning context | Main read and write paths | Freshness the partner expects |
| --- | --- | --- | --- |
| **Inbox and messages** | Conversations ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)) | Read threads, reply, templates, translation, structured requests | Seconds |
| **Calendar, rates and restrictions** | ARI or calendar | Edit with ownership rules, bulk edits, overrides | Seconds to see the change; minutes for search to reflect it |
| **Reservations and exceptions** | Reservations ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)) | List, search, act on exceptions, mark no-shows, confirm | Seconds for new bookings; real time for exceptions with deadlines |
| **Property or listing content** | Property and listing ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)) | Edit, upload photos, see content score | Minutes |
| **Finance** | Payments and settlement ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)) | Invoices, commission statements, payouts, virtual cards | Daily, but always exact |
| **Performance and programs** | Partner analytics; programs ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)) | Dashboards, benchmarks, opt in and out | Daily, with a stated as-of time |
| **Team and access** | Delegation and identity ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)) | Invite, assign roles, revoke, audit | Immediate on revocation |

A partner forgives a day-old dashboard that says so, but not a revoked employee who can still read guest phone numbers for an hour.

{id: extranets-and-host-tools--reservation-operations-and-exception-queues}
## Reservation Operations and Exception Queues

Most reservations need nothing from the partner. For the rest, a **reservation exception queue** turns those cases into work items, each with a type, an owner role, a deadline and an escalation path.

| Exception | Detected by | Owner role | Deadline | Escalation if missed |
| --- | --- | --- | --- | --- |
| Reservation not acknowledged by the PMS | Delivery monitor | Front office or reservations | Before the fallback window closes | Fallback delivery, then partner support call for arrivals within 48 hours |
| Booking request awaiting decision (request to book) | Reservation service | Host, co-host or reservations | 24 hours at Nookaway | Request expires; response rate falls |
| Guest change or "cancel for less" request | Conversations, structured request | Reservations | Policy-defined | Guest contacts customer service |
| Virtual card declined or not yet charged (merchant bookings) | Payments | Finance or front office | Before check-out | Payout hold and finance case |
| Overbooking or room out of order | Partner, or inventory reconciliation | Front office | Before the guest travels | Relocation through customer service |
| No-show to confirm | Reservation service after the arrival date | Front office | Policy-defined window | Commission or payout default applies |
| Guarantee or protection claim to evidence | Protection | Host or co-host | Claim window | Claim closes |

Booking.com documents the first row. Its reservation API is pull-based: a connectivity provider retrieves new, modified and canceled reservations and, in the OpenTravel flow, acknowledges them. If a reservation is not acknowledged or retrieved within **30 minutes**, it is e-mailed to the property, which must then handle it through the extranet. The window can be extended to 24 hours, "but that can increase queue size and overbookings" ([Booking.com, Reservations API overview](https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview), live documentation as of October 2026). The extranet is where the human fallback lands; if that fallback is an e-mail and a list, the reservation may still be **Lost at the Front Desk**.

![An exception moves from Open to Claimed and Resolved, or to Escalated when there is no owner or the deadline passes, and the marketplace resolves escalated items.](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/10-exception-work-item.jpeg)

**Figure 4:** *A reservation exception as a work item. The state that matters most is the one most tools lack: escalation to the marketplace when the deadline approaches and nobody at the property has claimed the item.*

Three design choices follow.

- **Derive exceptions from events in one service.** Reservation, payment and conversation services publish events; one exception service applies rules ("unacknowledged after 20 minutes and arrival within 7 days") and keeps the queue. Customer service reads the same queue ([When Something Goes Wrong: Customer Service and Recovery](#customer-service)).
- **Route by role, not by person.** "Front office at Hotel Miradouro" owns the item, so it survives shift changes. The delegation model below supplies the roles.
- **Measure the queue.** Exceptions per thousand reservations by type and supplier, the share resolved before deadline and the share escalated. A rising unacknowledged rate is a connectivity problem in the making ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)).

In Corvane's 2027 review, Partner Hub showed exceptions only as icons in one booking feed, and the hotels with the most unacknowledged bookings rarely opened it. The redesigned queue sends each item to its owning role and escalates to Roomstead partner support three hours before an at-risk arrival.

{id: extranets-and-host-tools--delegation-teams-co-hosts-and-roles}
## Delegation: Teams, Co-Hosts and Roles

The two marketplace types arrived at delegation from opposite ends. OTA extranets have long had multi-user accounts with roles, because hotels have staff. Their hard parts are **hierarchy** (a chain, a management company and an owner company above one property) and **third parties** (the connectivity partner, a revenue consultant, a content agency).

Hosted-stays marketplaces started from one person and one home and retrofitted delegation; Airbnb's help pages show a mature retrofit. The listing owner can add co-hosts, and a full-access co-host can add others with limited access only ([Airbnb Help, article 1243](https://www.airbnb.com/help/article/1243), live page as of October 2026). The permissions page names three levels ([Airbnb Help, article 1534](https://www.airbnb.com/help/article/1534), live page fetched 21 October 2026):

| Area | "Full access" | "Calendar and messaging access" | "Calendar access" |
| --- | --- | --- | --- |
| Calendar | Edit | View | View |
| Pricing and listing details | Manage | No | No |
| Messaging | Guests, host and co-hosts | Guests, host and co-hosts | Host and co-hosts only |
| Reservations | Accept or decline requests, handle changes and cancellations, write guest reviews | View; get support for reservation issues | View |
| Damage and money requests | Yes | No | No |
| Payouts | Can receive payouts set up by the owner; sees the earnings dashboard | Can receive payouts | Can receive payouts |
| Adding co-hosts | Can invite or remove co-hosts, but not other full-access co-hosts | No | No |

The same page says only listing owners can set up a co-host's payouts, co-hosts cannot see the owner's payout method or taxpayer information, and the owner remains responsible for all co-hosts. Every new co-host must be identity-verified ([Airbnb Help, article 1237](https://www.airbnb.com/help/article/1237), live page as of October 2026). Airbnb also built a market for delegation: the Co-Host Network launched on 16 October 2024 with "more than 10,000 co-hosts across 10 countries", recommended by an algorithm using "more than 80 factors" ([Airbnb, 2024 Winter Release](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb), 2024), and by mid-2025 supported "over 100,000" listings ([Airbnb Q2 2025 shareholder letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm), 2025).

Three lessons are architecture, not product detail. **Money rights are separate from operating rights**: a co-host can be paid without seeing the owner's bank details. **Grants have a grantor and a ceiling**: a full-access co-host can delegate, but not at their own level. **Responsibility stays with the owner.**

{id: extranets-and-host-tools--a-delegation-model-that-serves-hotels-and-homes}
### A delegation model that serves hotels and homes

A role on a user account is not enough. Delegation is a **relationship** between a party and a supply object. The generic hosted-stays reference model behind this book reaches the same conclusion when it stress-tests a rule requiring remote owners to appoint a licensed local operator: it models owner, listing controller, licensed operator, co-host, service provider, permit holder, payout beneficiary, fee recipient and tax party as separate roles, and names the failure this prevents: "Informal password sharing and payout workarounds become both unsafe and illegal" (Productscape hosted-stays model, stressor `coho`; a generic model, not a description of any company).

![A grant card links an owner to a delegate and a target, carrying a role and validity; money roles hang on the target; authorization reads the grant.](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/10-delegation-as-data.jpeg)

**Figure 5:** *Delegation as data. A grant links a delegate to a target with a role, a scope and a validity period; money roles hang on the target and are granted separately; every request, from a person or from software, is authorized against current grants.*

The model has five parts.

1. **Parties, not just users.** A party is a person or an organization: Carmen Ruiz, a cleaning company, a hotel management company, a PMS vendor. People act for organizations through their own grants. That is how "Alfama Keys staff" or "Miradouro front office" can hold a role.
2. **Targets at three levels.** A single property or listing, a portfolio (a manager's set of listings or a chain's set of hotels) and, for the OTA, the legal entity that signed the contract. A grant on a portfolio applies to listings added later, which is what professional managers need and what auditors worry about.
3. **Roles as bundles of scopes, with ceilings.** Scopes are fine-grained (`calendar:write`, `rates:write`, `messages:reply`, `reservations:act`, `finance:read`, `payout:configure`, `team:manage`, `tasks:read`). Roles are named bundles that suppliers understand. A grantor can only grant scopes they hold, and some scopes, such as `payout:configure`, are never delegable.
4. **Money roles separate from operating roles.** Who receives which share of the payout, and who is the tax party for it, are attributes of the listing and the reservation, set by the owner and verified ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement), [The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)).
5. **Validity and audit.** Every grant has a start, an optional end and a revocation record; every action records which grant it was performed under. "Who reopened these dates?" must have an answer that names a person and a grant.

Authentication, step-up and the policy engine that evaluates grants belong to [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access); the workspace makes delegation usable with an invite flow that suggests the minimum role, a team page and owner alerts when a grant changes.

Machine delegates get the same treatment. Miradouro's PMS vendor is a party with a grant scoped to ARI and reservations for that property; if Duarte changes vendor, revoking the grant must stop the old vendor's writes at once. Airbnb's API terms show the platform side: software partners join programs for property management, channel management, operations and connected devices, pass a data-security review, implement mandatory features within six months, and may be rate-limited at any time ([Airbnb API Terms of Service](https://www.airbnb.com/terms/api), last updated 15 October 2025).

{id: extranets-and-host-tools--step-up-on-money-and-the-threat-model}
### Step-up on money and the threat model

The delegation model is also a security control. In the documented extranet attacks of 2023–2025, criminals stole hotel staff credentials with infostealer malware or phishing, logged into the property's account and messaged guests from inside the platform asking for "payment verification". A 2023 Secureworks investigation found the victim hotel had not enabled multi-factor authentication (MFA) on its Booking.com access ([Sophos/Secureworks](https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam), 2023); in 2024 Booking.com told KrebsOnSecurity the attacks "stem from partners' machines being compromised with malware" ([KrebsOnSecurity](https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/), 2024). Corvane's own version came in **November 2027**: attackers phished staff credentials at **230** Roomstead partner properties and messaged **4,100** guests; **310** paid, and Roomstead reimbursed **€212,000** ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) owns the incident). The workspace lessons:

- **Least privilege by default.** Most staff need reservations and messages; few need finance; almost nobody needs payout configuration.
- **Step-up on sensitive actions, not only at login.** Bank-detail and payout changes, bulk messages, bulk exports of upcoming reservations and new administrators each need fresh strong authentication and an owner notification. Session cookies stolen by malware bypass login MFA; step-up on the action does not.
- **Make sharing unnecessary before making it impossible.** Nookaway's September rollout failed because suppliers had no way to delegate.

{id: extranets-and-host-tools--turnover-check-in-and-operations-coordination}
## Turnover, Check-In and Operations Coordination

On a hotel stay, the marketplace leaves the stage once the reservation is delivered; housekeeping and keys run in the hotel's PMS. On a home stay there is no front desk, so the marketplace often stays involved until the guest is inside.

A turnover task is derived from two adjacent reservations. Its inputs are reservation events, the listing's turnover rules (cleaning duration, preparation time) and the people with an operations role; its outputs are a notification to the cleaner, a readiness state, and, if the window is too short, a block or warning back to the calendar.

Airbnb's smart-lock integration, opened to all US and Canadian hosts on 21 August 2024 for compatible Schlage, August and Yale locks, shows the reservation-driven pattern: a unique code per reservation, "only active for the duration of a stay", updated when check-in or check-out times change, with host alerts when a guest checks in or a lock goes offline or runs low on battery ([Airbnb Newsroom](https://news.airbnb.com/smart-lock-integrations-available-to-all-us-and-canada-hosts), 2024).

![A guest's later check-out alters the reservation, whose event moves the cleaner's turnover task and reissues the lock access code, and the guest gets updated details.](stays-marketplace-architecture/posts/10-extranets-and-host-tools/assets/images/10-extranets-and-host-tools/10-one-change-three-lifecycles.jpeg)

**Figure 6:** *One reservation change, three lifecycles. The reservation, the turnover task and the access credential each have their own state; all three must react to the same ordered event, and a missed alteration means a cleaner arriving during a stay or a guest locked out at midnight.*

The design rules:

- **Treat access codes and turnover tasks as derived resources with their own state**, driven by reservation events and reconciled nightly against reservations and device state, to catch "code valid for a canceled reservation" or "no task before tomorrow's check-in".
- **Order matters.** Alterations carry a version; consumers reject older ones, or a cancellation followed by a rebooking can leave the wrong code active.
- **Keep a fallback.** Airbnb's PMS lock page tells hosts to provide backup entry instructions. Every digital key path needs a non-digital fallback in the arrival guide ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) owns how check-in details reach the guest).

**How much should the marketplace build?** I found no primary source describing a marketplace-run cleaning-scheduling system at Airbnb, Booking.com or Expedia; professional managers run turnover in their PMS or specialist tools that subscribe to reservation events. My rule: the marketplace must **emit reliable, ordered reservation events and accept blocks and readiness back**, and should build only a **minimal** task capability for individual hosts with a home or two and a cleaner: a cleaner role that sees only the turnover schedule, a task per turnover with a window, a "ready" confirmation, and a calendar warning when a booking leaves less time than the preparation rule.

{id: extranets-and-host-tools--partner-analytics-and-programs-as-features}
## Partner Analytics and Programs as Features

Partners want three answers from analytics: *how am I doing*, *compared with whom*, and *what should I change*. Public documentation shows how OTAs answer them.

| Signal | Booking.com | Expedia Group | Agoda |
| --- | --- | --- | --- |
| Program status and ranking effect | Preferred Partner badge and search boost; "only 30% of partners in a particular geographic area who meet all the requirements" can be Preferred ([Booking.com](https://partner.booking.com/en-gb/solutions/preferred-partner-programme), live page) | Accelerator lets partners "View the potential impact on your sort order before you commit" ([Expedia Group, 2025](https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters)) | Agoda Growth Program reports impressions, room nights, revenue and return on ad spend per campaign ([Agoda, 2025](https://www.partnerhub.agoda.com/?p=95313)) |
| Comp-set benchmark | Not verified | Revenue view with a competitive price grid, reported by secondary sources since 2019 | Partner Portal comp-set benchmark flags periods needing attention ([Agoda, 2026](https://kyodonewsprwire.jp/release/202608174214)) |
| Guest experience | Reply to reviews in the extranet and Pulse | Review-sentiment insights announced in May 2024 ([Expedia Group, 2024](https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx)) | AI review summaries (2026) |

Two details show why this is more than reporting. Expedia's partner blog states, from its 2024 data, that properties in the **top 20 sort positions** on Expedia and Hotels.com receive **80% of clicks** ([Expedia Group, 2025](https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters)), so partners will ask how to move up. Agoda's Partner Portal, announced on 17 August 2026 as the successor of the Yield Control System (YCS), adds "Agoda Intelligence" suggestions up to 90 days ahead that partners must verify ([Agoda, 2026](https://kyodonewsprwire.jp/release/202608174214)). The extranet has become a delivery channel for the marketplace's models. At Corvane, Partner Hub's Rate Insights (launched 2025) shows comp sets and rate recommendations; hotels accepted only **9%** of them in 2026, which says as much about trust in the numbers as about the model ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)).

On hosted stays the levers are price, quality and policy rather than paid visibility. Airbnb's October 2024 release added price tips "based on similar local listings" and an earnings dashboard with custom reports ([Airbnb, 2024](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb)). Superhost is assessed every three months over the trailing year on stays, a 90% response rate, cancellations under 1% and a rating of at least 4.8 ([Airbnb Help, article 829](https://www.airbnb.com/help/article/829), live page as of October 2026): a batch credential whose progress the host app must show before the quarter closes.

{id: extranets-and-host-tools--the-architectural-obligations}
### The architectural obligations

1. **One metric definition, two audiences.** "Conversion", "cancellation rate" and "response rate" must mean the same in the dashboard, ranking features, program eligibility and internal reporting ([Knowing the Marketplace: Data Platform, Metrics and Partner Insight](#marketplace-intelligence)). If the program says 7.4 and the dashboard says 7.6, the partner will call support, rightly.
2. **Explain the ranking without exposing it.** "Why am I on page three?" should be answered from the features the ranking used, summarized into levers the partner controls (price, availability, content, reviews, policy, programs), with any paid term's effect stated separately. [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) owns the ranking log that makes this possible.
3. **Benchmarks are aggregates with privacy rules.** A comp set of five hotels in a small town can reveal one competitor's occupancy. Serve precomputed aggregates with minimum group sizes.
4. **Programs are features with eligibility computed by the platform.** Preferred-style programs, loyalty discounts and visibility boosters are opt-in, with eligibility based on performance, quality and sometimes commission. The Italian competition authority opened an investigation into Booking.com's Preferred Partner and Preferred Plus programs on **22 April 2026**, concerned that selection "appears to be driven largely by criteria that favour accommodation providers paying higher commissions" ([AGCM, PS13115](https://en.agcm.it/en/media/press-releases/2024/4/PS13115), 2026); it is an investigation, not a finding. Eligibility and a program's ranking effect must therefore be computed by one auditable component, logged and explainable to the partner and to a regulator; for Roomstead's Front Row program ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)) that component decides who is enrolled and logs the boost per impression. That keeps **Pay-to-Rank Creep** visible; [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) designs the programs.

{id: extranets-and-host-tools--apis-mobile-and-supply-side-notifications}
## APIs, Mobile and Supply-Side Notifications

Professional suppliers want the functions, not the screens. Connectivity APIs ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers), [One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)) carry ARI and reservations; professionals increasingly expect messaging, reviews, reporting and programs by API too, as Booking.com's API list shows. So **every workspace module needs an API contract before it has a screen**, under the same authorization and ownership rules.

Mobile-first is the default for hosts and for hotel staff away from a desk. The app is for urgent, small jobs (reply, accept or decline, close a date, confirm readiness, act on an exception); rate-plan setup, contracts and bulk content stay on the web. A useful test: can a host run a whole stay, from request to payout, from the phone?

Notifications are the workspace's biggest source of noise: the supplier chooses channels per event class; the platform decides which events may never be silenced.

| Event class | Examples | Default channels | Can the supplier mute it? |
| --- | --- | --- | --- |
| **Act now** | Request to book expiring, unacknowledged arrival today, overbooking, lock offline before check-in | Push and SMS or messaging app, then a call from partner support | No |
| **Act today** | New guest message, change request, card declined, review to answer | Push, e-mail digest | Channel only |
| **Know** | New reservation, cancellation, payout sent | Push or e-mail | Yes |
| **Learn** | Performance summary, program eligibility, price suggestions | E-mail, in-app | Yes |
| **Security** | New device login, bank details changed, new administrator added | E-mail and push to the owner, always | No |

Messaging apps are now a supply-side channel too: Agoda's August 2026 announcement includes KakaoTalk booking notifications for South Korean motels and plans for WhatsApp and WeChat ([Agoda, 2026](https://kyodonewsprwire.jp/release/202608174214)). The routing service itself belongs in Courier, the group notification platform ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)); the workspace owns the event classes and the rule that "act now" events escalate to a human when nobody acknowledges them.

AI assistants are the newest client. In October 2026 Booking.com described a partner onboarding assistant grounded "strictly in the partner help center content", with a separate retriever for pre-approved answers to legally restricted questions ([booking.ai](https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7), 2026). An assistant that answers questions is a reader. One that changes rates or replies to guests is a writer and must act under a delegation grant, with the same scopes and audit trail as a person ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)).

{id: extranets-and-host-tools--in-practice-corvane-s-two-workspaces-on-one-spine}
## In Practice: Corvane's Two Workspaces on One Spine

The forum's decision, in October 2027, was **two products on a shared spine**. Partner Hub and the Nookaway host app stay separate products with separate teams, because a revenue manager at an 84-room hotel and Carmen Ruiz with one apartment in Triana do different jobs. They share five platform components under One Stay: Corvane ID for authentication and step-up; a **delegation service** with the party, grant and scope model above, built on the shared supply-party records recommended in [From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding); the exception queue engine; Courier; and the partner analytics read model built on Gauge, the group metric layer. Supply models, ARI stores (Tally and Almanac) and connectivity stay separate.

{id: extranets-and-host-tools--worked-example-1-alfama-keys-moves-off-a-shared-login}
### Worked example 1: Alfama Keys moves off a shared login

Alfama Keys is a fictional Lisbon property manager with **38** Nookaway listings belonging to **14** owners, connected through a vacation-rental PMS that owns calendars and prices. Before the change, its six office staff used the owners' logins to answer guests in the Nookaway app and to see earnings, because a 2016-style co-host could not see earnings or receive a fee. After the migration in the first quarter of 2028, the setup is:

| Party | Grant | Target | Scopes |
| --- | --- | --- | --- |
| Each of the 14 owners | Owner | Their own listings | All, including `payout:configure` |
| Alfama Keys (company) | Manager | Portfolio of 38 listings | Calendar and rates read (PMS writes them), reservations, messages, tasks, `finance:read` |
| PMS vendor (software party) | Connected system | Portfolio | `calendar:write`, `rates:write`, reservations read |
| 3 guest-relations staff | Through Alfama Keys | Portfolio | `messages:reply`, `reservations:act` |
| 2 operations coordinators | Through Alfama Keys | Portfolio | `tasks:manage`, calendar read |
| 1 finance officer | Through Alfama Keys | Portfolio | `finance:read` |
| 6 contracted cleaners | Service provider | Assigned listings | `tasks:read` for their listings only |

Money roles are set by each owner. For a four-night stay at €150 a night with a €60 cleaning fee, the booking subtotal is **€660**. Alfama Keys has chosen Nookaway's host-only fee of **17%**, so the guest pays no service fee and the host-side fee is **€112.20**, leaving a payout of **€547.80**, released 48 hours after scheduled check-in. The owner's split rule sends the €60 cleaning fee and a 20% management fee on the remainder, (€547.80 − €60) × 20% = **€97.56**, to Alfama Keys, and **€390.24** to the owner. Each share has its own payout beneficiary and tax party, so the tax reporting for each owner and for Alfama Keys comes from the same allocation ([The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays)).

No staff member knows an owner's password. A departing guest-relations employee loses access when Alfama Keys revokes one grant, without 14 owners changing passwords, and step-up on payout changes reaches the owner who holds that scope.

{id: extranets-and-host-tools--worked-example-2-miradouro-s-closure-under-the-ownership-rule}
### Worked example 2: Miradouro's closure under the ownership rule

Under the ownership rule, Partner Hub knows from Switchyard's connection record that Miradouro's ARI for Roomstead is owned by Corvane Connect. The front-office manager's "close Twin, 15–17 September" becomes a **Roomstead-only restrictive override** with an expiry of 18 September, logged with her user, grant and reason ("rooms out of order"). Roomstead notifies Corvane Connect. When the 02:00 full sync arrives, the ARI store applies the PMS's numbers underneath the override, and Roomstead stays closed for those nights.

Aisha's team set a target for the end of 2028: fewer than **2%** of Partner Hub availability edits on connected properties overwritten within 24 hours, against **23%** in August 2027.

{id: extranets-and-host-tools--trade-offs}
## Trade-offs

**How many partner workspaces?**

| Option | What it means | Works when | Fails when |
| --- | --- | --- | --- |
| **One workspace for hotels and homes** | One product and one user interface for every supplier | Supply is converging and most suppliers are professional | Individual hosts get a hotel tool; hotels get a phone-first tool that cannot handle rate plans (**The Hotel-Shaped Home**) |
| **Two products on a shared spine** (Corvane's choice) | Separate products; shared identity, delegation, exceptions, notifications, analytics serving | Supplier jobs differ but security, delegation and metric definitions should not | The spine is under-funded and each product rebuilds it locally |
| **Two independent stacks** | Separate products and platforms | Brands are run as separate businesses that may be sold | Every security and regulatory change is built twice, as Nookaway's step-up rollout showed |

**What happens when the extranet and a connected system disagree?**

| Option | Effect | When it is right |
| --- | --- | --- |
| **Last writer wins** | Simple; partner edits are silently undone by the next push | Never for availability; acceptable for low-stakes content drafts |
| **Extranet edits blocked for connected properties** | No conflicts; partners cannot react in an emergency | Chains with central teams that insist on one source of truth |
| **Restrictive, expiring, marketplace-only overrides** | Emergencies are handled; the marketplace never opens inventory the PMS has not | My default for connected hotels and API-connected homes |
| **Two-way sync back to the PMS** | The PMS learns about extranet edits | Only when the connectivity partner certifies the inbound message; rarely available |

{id: extranets-and-host-tools--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Supplier and user** | A business with staff, a PMS and often a channel manager; users are employees in roles | Mostly one person on a phone; a minority of professional managers with teams and software |
| **Role of the tool** | Configuration console, reservation workbench, finance view and fallback; most ARI arrives by API | The operating system of the host's business, until the host connects a PMS |
| **Data the tool edits** | Room types, rate plans, restrictions, policies per rate plan, content per room type | One calendar, a nightly price with discounts, house rules, arrival guide |
| **Delegation** | Multi-user from the start; hard parts are hierarchy (chain, management company, owner) and third-party systems | Retrofitted co-hosts; hard parts are split payouts, tax parties, verification of each delegate and service providers such as cleaners |
| **Reservation exceptions** | Unacknowledged delivery, overbooking, no-shows, virtual-card charging, walking guests | Request-to-book decisions, guest change requests, check-in failures, damage claims |
| **On-property operations** | The hotel's own systems; the marketplace is out of the loop after delivery | The marketplace often relays door codes and check-in details and handles failed arrivals |
| **Commercial levers in the tool** | Paid visibility and programs, commission-based boosts, loyalty discounts, comp-set revenue tools | Price tips, quality credentials, policy choices; no published pay-for-rank product at Airbnb |
| **Main security threat** | Staff credential theft and takeover of the extranet, then guest phishing | Account takeover of hosts, payout redirection, shared logins |
| **Regulatory touchpoints** | Ranking and program transparency, parity rules, invoicing | Registration numbers per listing, host tax reporting, operator and permit holder roles |

**What to share.** Share the spine Corvane chose (identity and step-up, delegation, the exception queue engine, notification routing, partner analytics on one metric layer): these are the same problem on both sides, and they are where security and regulatory change land. Do not share the products, the supply editing screens (rate plans versus a nightly calendar) or the operations features. Convergence is real: about 3.9 million of Booking.com's 4.4 million listed properties at the end of 2025 were homes and apartments ([Booking Holdings Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026), and Airbnb reported adding "thousands of boutique and independent hotels" ([Airbnb Q2 2026 shareholder letter](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf), 2026). But professional managers on both marketplaces need the same delegation and API, not the same screens; a group that builds one workspace for both will build it for the larger supplier type and lose the other.

{id: extranets-and-host-tools--failure-modes}
## Failure Modes

| Failure | Symptom | Handled in |
| --- | --- | --- |
| **The extranet as a second source of truth** | A support category called "change did not stick" | Field ownership |
| **The fallback that is only an e-mail** | "We have no booking for you" at properties with a healthy connection on paper (**Lost at the Front Desk**) | Reservation Operations and Exception Queues |
| **Everyone is an administrator** | One takeover exposes payout details and enables bulk messaging | Step-up on money and the threat model |
| **Delegation by password** | MFA rollouts break operations; many devices per account | A delegation model that serves hotels and homes |
| **Revocation that lags** | A dismissed employee or replaced PMS vendor keeps writing | Short token lifetimes for sensitive scopes; revocation events clients honor |
| **Dashboards that contradict ranking** | Partners quote numbers support cannot reconcile with program decisions | The architectural obligations |
| **Turnover tasks that miss alterations** | Cleaners arrive during a stay; guests locked out after a date change | Turnover, Check-In and Operations Coordination |
| **Notification fatigue** | Suppliers mute the app and miss the one urgent alert | APIs, Mobile and Supply-Side Notifications |

{id: extranets-and-host-tools--the-chief-architect-s-view}
## The Chief Architect's View

The workspace looks like a front end, so it is easy to under-govern. I govern it as a **product with platform obligations**.

**Decide**, at group level, the five rules of this chapter: supply functions as APIs with owning domains; the field-ownership table per marketplace; one delegation model and its list of never-delegable scopes; the exception catalog with owners, deadlines and escalation; and one metric layer for analytics, ranking and programs.

**Who decides.** Product leads for Partner Hub and the host app own the user experience and the roadmap. The group architecture forum owns the shared spine and the field-ownership rules, because they bind connectivity, inventory and trust teams. Trust and security own the step-up policy. Regulatory affairs signs off program eligibility and ranking explanations shown to partners.

**Watch**, every month:

- the share of human edits overwritten by connected systems within 24 hours;
- exceptions per thousand reservations, share resolved before deadline, share escalated;
- accounts with many concurrent devices, as a proxy for shared logins, and the share of suppliers with more than one active user;
- step-up challenges on payout changes and their failure rate;
- partner support contacts per thousand active suppliers, by reason;
- the gap between dashboard metrics and the values used by ranking and programs, which should be zero.

**Long term.** Suppliers are moving toward professional software and AI assistants acting for them; a delegation model that treats a PMS vendor, a co-host and an assistant as parties with scoped grants absorbs that shift; one built on special cases will be rebuilt.

{id: extranets-and-host-tools--questions-to-ask}
## Questions to Ask

1. For each field a partner or host can edit, which system is the source of truth for a connected property, and can the partner tell from the screen that a change will be overwritten by their channel manager or PMS?
2. When a reservation fails delivery, who at the property owns it, by when, and what happens if nobody acts?
3. Can a supplier give a cleaner, a co-host, a finance clerk and a software vendor exactly the rights they need, and revoke any one of them without affecting the others?
4. Which actions require step-up authentication, and does that include bulk messaging and bulk exports, not only payout changes?
5. Are payout beneficiaries and tax parties modeled separately from operating roles?
6. Do partner dashboards, ranking features and program eligibility read the same metric definitions? Who reconciles them?
7. How do reservation alterations reach turnover tasks and access codes, and what reconciles them if an event is lost?
8. Which supply-side notifications cannot be muted, and what escalates when nobody acknowledges them?
9. If an AI assistant replies to a guest or changes a rate for a supplier, under whose grant does it act, and where is that recorded?

The workspace is where partners and hosts set the numbers that the rest of the marketplace sells. Part III turns to those numbers: how availability, rates and restrictions are modeled so that they stay correct and searchable, beginning with [Part III — INVENTORY: Availability, Rates and Price](#part-3) and the ARI data model in [Rooms, Rates and Restrictions: The ARI Data Model](#rates-and-availability-model).

{id: extranets-and-host-tools--sources-and-evidence}
## Sources and Evidence

{id: extranets-and-host-tools--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), Airbnb, Inc., 2026: host tools and co-host description.
- [Q2 2025 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm), Airbnb, Inc., 2025: Co-Host Network supporting over 100,000 listings.
- [Airbnb 2024 Winter Release: Introducing Co-Host Network](https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb), Airbnb Newsroom, 2024: Co-Host Network launch figures, price tips, earnings dashboard.
- [Smart lock integrations now available to all hosts in the US and Canada](https://news.airbnb.com/smart-lock-integrations-available-to-all-us-and-canada-hosts), Airbnb Newsroom, 2024: per-reservation codes, alteration handling, lock notifications.
- [Announcing our 2024 Preferred Software Partners](https://news.airbnb.com/announcing-our-2024-preferred-software-partners/), Airbnb Newsroom, 2024: software-partner program context.
- [From Static Help Content to a RAG-Based Onboarding Agent for Partners](https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7), Booking.com (booking.ai), 2026: AI assistant in partner tools with templated answers.
- [TravelAds and Accelerator: hotel visibility boosters](https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters), Expedia Group, 2025: sort-order preview; top-20 positions receive 80% of clicks (2024 data).
- [Put Your Trip on Autopilot (EXPLORE 2024)](https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx), Expedia Group, 2024: partner-facing guest-experience insights.
- [Agoda Partner Portal announcement](https://kyodonewsprwire.jp/release/202608174214), Agoda via Kyodo News PR Wire, 2026: YCS renamed; comp-set benchmark, AI suggestions, messaging-app notifications.
- [Agoda Growth Program](https://www.partnerhub.agoda.com/?p=95313), Agoda Partner Hub, 2025: program metrics reported to partners.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), Booking Holdings Inc., 2026: homes share of Booking.com's listed properties.
- [Q2 2026 Shareholder Letter](https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf), Airbnb, Inc., 2026: hotels added to Airbnb.

{id: extranets-and-host-tools--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Connectivity APIs overview](https://developers.booking.com/connectivity/docs), Booking.com, n.d. (live as of October 2026): API list including reporting, scores, messaging and programs.
- [Reservations API overview](https://developers.booking.com/connectivity/docs/reservations-api/reservations-overview), Booking.com, n.d.: 30-minute acknowledgement window and extranet fallback.
- [Understanding the Messaging API](https://developers.booking.com/connectivity/docs/messaging-api/understanding-the-messaging-api), Booking.com, n.d.: extranet-only responses and single-channel-of-reply rule.
- [Pulse by Booking.com](https://www.booking.com/propertyapp.en-gb.html), Booking.com, n.d.: mobile companion functions.
- [Preferred Partner Programme](https://partner.booking.com/en-gb/solutions/preferred-partner-programme), Booking.com, n.d.: 30% per-area cap and eligibility.
- [Co-hosts: An introduction (article 1243)](https://www.airbnb.com/help/article/1243), Airbnb Help Center, n.d.: who can add co-hosts.
- [What co-hosts can do (article 1534)](https://www.airbnb.com/help/article/1534), Airbnb Help Center, n.d. (fetched 21 October 2026): co-host permission levels, payout and responsibility rules.
- [Identity verification (article 1237)](https://www.airbnb.com/help/article/1237), Airbnb Help Center, n.d.: verification of co-hosts.
- [Smart lock integration via PMS (article 4163)](https://www.airbnb.com/help/article/4163), Airbnb Help Center, n.d.: PMS owns the lock; Airbnb relays.
- [How do I become a Superhost? (article 829)](https://www.airbnb.com/help/article/829), Airbnb Help Center, n.d.: quarterly credential thresholds.
- [API Terms of Service](https://www.airbnb.com/terms/api), Airbnb, 2025: software-partner programs, security review, mandatory features.
- [PS13115: investigation into Booking.com](https://en.agcm.it/en/media/press-releases/2024/4/PS13115), Autorità Garante della Concorrenza e del Mercato, 2026: Preferred programs investigation opened 22 April 2026.

{id: extranets-and-host-tools--research-and-practitioner-sources}
### Research and practitioner sources

- [Booking.com phishers may leave you with reservations](https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/), Brian Krebs, KrebsOnSecurity, 2024: partner-machine compromise and in-app guest phishing.
- [Vidar infostealer steals Booking.com credentials in fraud scam](https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam), Sophos (Secureworks Counter Threat Unit), 2023: hotel without MFA on extranet access.
- Productscape travel-accommodations and hosted-stays reference models (bricks `extr`, `rsrv`, `perf`, `opco`, `coho`, `host`; residuality stressor `coho`), the author's sibling repository, 2026: generic reference models, not descriptions of any company.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
