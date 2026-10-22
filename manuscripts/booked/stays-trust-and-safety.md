{id: stays-trust-and-safety}
# 31. Trust as a Platform: Trust and Safety for Stays

![Trust as a Platform: Trust and Safety for Stays — logo](stays-marketplace-architecture/posts/31-stays-trust-and-safety/assets/images/31-stays-trust-and-safety/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Map the trust risks of a stays marketplace and design the platform that handles them: the loop from policy to detection, decision, enforcement and appeal, the trust decision API, the entity graph, enforcement propagation, integrity operations, statements of reasons and the metrics that show whether any of it works.

> **WHY THE BUSINESS CARES:** A guest who arrives at a flat that was never for rent, or a host whose home is wrecked by a party, blames the brand, and so do journalists and regulators. Trust failures cost refunds and guarantees directly and supply and demand indirectly; the same controls, applied clumsily, block good bookings and suspend honest hosts.

> **WHY ARCHITECTS SHOULD CARE:** Trust and safety touches every write path in the marketplace: publishing, booking, messaging, paying out and logging in. If each domain builds its own checks and its own "suspended" flag, nobody can say what was decided about an account, why, or whether every system obeyed. A platform with one decision record and one enforcement path makes trust auditable, explainable and shareable across brands.

> **KEY POINTS:**
>
> * **Separate detection, decision and enforcement.** Detection models and rules belong close to the risk they know (party screening, payment fraud, fake listings). The decision that follows, and the enforcement action it creates, belong to one platform with one record, so that every restriction has an owner, a reason, a scope, an expiry and an appeal path.
> * **An enforcement action is finished only when every system has obeyed it.** Delisting a home while its calendar stays open on the partner API, its messages keep flowing and its payout is released is not enforcement. Treat enforcement as a propagated event with receipts from each consumer, and reconcile what was decided with what is in force.
> * **Explainability is a product requirement, not a legal afterthought.** The EU Digital Services Act and the Platform-to-Business Regulation require a statement of reasons for removals, demotions, payment suspensions and account suspensions, plus a complaint path. A platform that records reasons, evidence and policy versions with every decision gets statements, appeals and transparency reports almost for free; one that does not rebuilds them case by case.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Trust After the Incident** — each scam wave or safety headline produces another tool with its own data and its own "blocked" flag, so a suspension in one tool does not stop the same person in the next one.
> * **The Unwatched Model** — screening, listing-risk and message classifiers suspend people and block bookings without measured precision, appeal outcomes or an owner who watches them drift.

A hotel guest trusts a business that is licensed, staffed and insured. A guest in a hosted home trusts a stranger, and the stranger trusts the guest. Between them stands the marketplace, which has never seen the home or met either party. That is why **trust is the product a hosted-stays marketplace sells** beside the night itself, and why an accommodation marketplace that sells holiday homes and apartments slowly acquires the same problem.

Most marketplaces do not build trust and safety; they accumulate it. A payment-fraud rules engine arrives with the first chargebacks, listing review with the first fake homes, a party filter after the first neighborhood complaint, a phishing filter after the first hijacked hotel account. Together these tools produce the failure this chapter is about: **the marketplace decides something about a person and then fails to act on it everywhere it should.**

This chapter opens Part VII ([Part VII — TRUST: Making Strangers Safe to Stay With](#part-7)), which turns from moving money to the failures of trust behind many of Part VI's refunds and chargebacks. It owns three concepts: the **trust decision**, the **enforcement action** in a stays marketplace, and **integrity operations**. It builds on the gates and states earlier parts defined (publishing, booking, messaging, payout holds) and builds the platform that the rest of Part VII plugs into: fraud on both sides in [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), identity and access in [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access), reviews in [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation), reservation screening and damage protection in [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents), and registration and other legal rules in [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation).

{id: stays-trust-and-safety--setting-the-scene-at-corvane-the-valencia-apartments-that-did-not-exist}
## Setting the Scene at Corvane: The Valencia Apartments That Did Not Exist

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), started 2027 with two trust stacks. Nookaway, its hosted-stays marketplace, ran a trust platform inside Burrow, its Python monolith, plus Go services for reservation screening, listing verification and claims under Nookaway Cover. Roomstead, its accommodation marketplace, had a payment-fraud team with a rules engine in Dublin and a separate partner-account security team. The two stacks shared no data. Corvane Payments, which pays both brands' supply side, held the only joined-up view of who was being paid, and nobody asked it.

In July 2027 a self-described property manager, **Turia Homes**, showed what that cost. Turia had 26 listings in Valencia on Nookaway, managed through a property-management system (PMS) connected to Nookaway's partner API. It also had 19 apartments on Roomstead, onboarded in March 2027 as one property with four room types, sold under the agency model (the guest pays at the property). The company existed in the trade register, so it passed know-your-business checks on both brands. The apartments did not exist as rentals: the photos came from sale ads, and the registration numbers on the listings were valid numbers copied from other, real tourist flats. Turia's messages asked guests to pay a "key deposit" by bank transfer before arrival.

The case unfolded as follows (all figures are illustrative, like everything about Corvane).

| Date (2027) | Nookaway | Roomstead |
| --- | --- | --- |
| 3–8 July | Five guest reports ("the address is someone's home") and a message-classifier flag on bank-transfer language | Nothing visible: agency bookings, no payment signal |
| 8 July, 16:20 | Trust operations suspend the host account and delist all 26 listings | Not informed |
| 8–12 July | 31 future reservations stay confirmed: the suspension acted on listing visibility, not on reservations. The PMS's partner-API token still works, and Turia keeps messaging guests through it; **6** more guests pay deposits | 58 new reservations for Turia apartments |
| 9 July | A payout of **€2,940** for two stays with 7 July check-ins is released: the payout hold was a manual ticket to Corvane Payments, worked on 10 July | — |
| 12 July | All 31 reservations canceled with full refunds; 9 guests with near arrivals rehoused at **€6,300** above their original prices | — |
| 24 July | — | Customer service escalates nine "property does not exist" complaints; Roomstead closes the property and cancels 77 future reservations |

In total, 14 Nookaway guests paid Turia **€11,900** off-platform, 8 of them (€6,800) before the suspension and 6 (€5,100) after it. On Roomstead, 22 guests paid **€27,400**: 3 (€3,800) before 8 July and 19 (€23,600) after. Both brands reimbursed their guests as goodwill. Turia's Nookaway payout account and its Roomstead commission direct-debit mandate used the same IBAN (international bank account number), and both accounts listed the same mobile number. Both facts sat in Corvane systems from the day Turia joined Roomstead.

Sofia Marín, Director of Trust and Safety, whose remit grew from Nookaway to the whole group under the One Stay program in April 2027, presented the case to the architecture forum on 17 August. Her diagnosis had three parts: **Nookaway decided correctly and enforced partially; Roomstead never learned of the decision; and nobody could list which systems had obeyed it.** Mariana Costa, the Group Chief Architect, framed the question for the forum: One Stay promised "one trust platform". What exactly should be in it, and what should stay with each brand?

![A cutaway building where a suspend switch has darkened only the catalog room while messaging, payouts, reservations and the other brand stay lit and busy.](stays-marketplace-architecture/posts/31-stays-trust-and-safety/assets/images/31-stays-trust-and-safety/31-partial-suspension.jpeg)

**Figure 1:** *Nookaway decided correctly and enforced partially: the suspension darkened the catalog while messaging, payouts, reservations and the other brand kept running.*

{id: stays-trust-and-safety--what-trust-and-safety-covers-in-a-stays-marketplace}
## What Trust and Safety Covers in a Stays Marketplace

**Trust and safety** is the set of policies, systems and people that keep the marketplace's users from harming each other, and that keep the marketplace from being used to cause harm. It differs from information security (protecting the company's systems) and from payments risk (protecting the money flow), though it shares data and tools with both.

{id: stays-trust-and-safety--the-risk-catalog}
### The risk catalog

Stays risks are more varied than most marketplaces' because the product is physical, the parties meet, and money moves before the stay.

| Risk | Who is harmed | Where it shows up | Main gate | Chapter that owns the detail |
| --- | --- | --- | --- | --- |
| **Fake or misrepresented listings** | Guest | Listing content, photos, address, registration number | Publish; periodic sweeps | [Describing a Stay: Content, Media and Property Mapping](#content-and-media), [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) |
| **Off-platform payment scams** | Guest | Messages, links, payment requests | Message send and render | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| **Account takeover** (guest, host, hotel extranet) | Account owner, then their guests | Login, sessions, bank-detail changes | Login; sensitive actions | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access), [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) |
| **Payment fraud** (stolen cards, refund abuse) | Platform or property | Checkout, refunds | Booking; refund | [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) |
| **Parties and property damage** | Host, neighbors | Reservation pattern, guest history | Booking (reservation screening) | [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) |
| **Unsafe homes** (no smoke alarm, hidden cameras, structural risk) | Guest | Listing attributes, guest reports | Publish; report | [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) |
| **Harassment, threats, violence** | Guest or host | Messages, reports, emergency calls | Report; emergency line | This chapter; [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) |
| **Discrimination** | Guest | Request-to-book acceptance and decline patterns | Booking flow design; measurement | This chapter |
| **Review manipulation** | Guests, honest competitors | Reviews and ratings | Review submission | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation) |
| **Illegal or unregistered supply** | Cities, neighbors, guests | Registration numbers, night caps, authority orders | Publish; booking; orders | [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) |

Two points follow. First, **almost every risk has its gate in a different domain**: publishing in supply, booking in checkout, messages in trip management, payouts in finance. Trust has to be a platform that domains call and obey, not one service in every request path. Second, **the same bad actor crosses rows**: Turia Homes was a fake-listing, off-platform payment and illegal-supply case at once, and with one tool per row it appears as three small problems.

{id: stays-trust-and-safety--five-terms-this-chapter-relies-on}
### Five terms this chapter relies on

- A **trust policy** is a written, versioned rule about what is allowed on the platform, with the evidence standard for acting on it and the consequences: "Payment requests outside the platform are not allowed. One confirmed instance: messaging restricted and listings hidden pending review. Repeat: suspension." Policies are what users agree to and what regulators read, so they must exist as text *and* as configuration the platform can evaluate.
- A **risk signal** is a fact or score about an entity that bears on a policy: a guest report, a classifier score on a message, a perceptual-hash match between photos, a login from a new device, a chargeback, a registration number that failed validation. Signals are evidence, not decisions.
- A **trust decision** is a recorded, versioned answer to "may this actor take this action on this object now, and if not, what happens instead?". It carries the outcome, the reason codes, the policy version, references to the evidence, the decider (rule, model or human), and an expiry. The decision is the unit that is audited, explained and appealed.
- An **enforcement action** is a typed, scoped and reversible restriction that a decision imposes on an entity: hide a listing, block a calendar, restrict messaging, hold a payout, suspend an account, cancel a reservation. It has a scope (which brand, market and capabilities it covers), a start, an expiry or review date, and a link to the decision and to the statement of reasons sent.
- **Integrity operations** are the people, queues and tools that handle what automation cannot: report triage, investigations, appeals, quality assurance of decisions, safety escalations, and the feedback from cases into policies and models.

{id: stays-trust-and-safety--the-loop-policy-detection-decision-enforcement-appeal}
### The loop: policy, detection, decision, enforcement, appeal

![A loop from trust policy to detection, trust decision, enforcement, statement of reasons and appeal, with appeal outcomes flowing back to decisions, detection and policy.](stays-marketplace-architecture/posts/31-stays-trust-and-safety/assets/images/31-stays-trust-and-safety/31-trust-loop.jpeg)

**Figure 2:** *The trust loop. Policies define what detection looks for; decisions turn signals into actions; statements of reasons and appeals send outcomes back as labels for models and as evidence that a policy is unclear. A platform that breaks the loop at any point stops learning.*

The appeal path is therefore architecture, not a support process: an overturned decision is a **labeled false positive**, and if it never reaches the model owner the model repeats the mistake.

{id: stays-trust-and-safety--architecture-a-trust-platform-that-domains-call-and-obey}
## Architecture: A Trust Platform That Domains Call and Obey

A trust platform for stays has eight components. Detection is deliberately plural: many detectors feed it, some owned by the platform and some by brand teams.

![Domain events feed an entity graph and detectors; gates request decisions from the trust decision service, which uses a policy registry and case management and passes actions to the enforcement service, which sends them with receipts to consumers and produces statements of reasons.](stays-marketplace-architecture/posts/31-stays-trust-and-safety/assets/images/31-stays-trust-and-safety/31-trust-platform-components.jpeg)

**Figure 3:** *The trust platform. Domains send signals and ask for decisions at their gates; the platform records decisions and turns them into enforcement actions that every consuming system must acknowledge. Detection can be owned by brand teams; the decision record and enforcement path cannot.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Risk signal feed** | Carry domain events and detector outputs into the platform, with entity references | Event contracts, entity identifiers, retention | Carry raw ID images or full message bodies to every consumer |
| **Signal store and entity graph** | Resolve accounts, parties, listings, properties, devices, phone numbers and payout instruments into linked entities | Link types, link confidence, provenance of each link | Decide anything on its own; a link is a signal |
| **Detectors** | Score risk: reservation screening, listing risk, message classification, payment-fraud models, login risk | Models, rules, features, evaluation | Write enforcement state into domain databases directly |
| **Policy registry** | Hold trust policies as versioned configuration: thresholds, action ladders, market and date variants | Policy versions, approvals, effective dates | Hold detection logic |
| **Trust decision service** | Answer gate requests synchronously; record every decision with reasons and policy version | Decision log, reason codes, latency budget, fallback behavior | Hide human overrides; overrides are decisions too |
| **Case management** | Queue, investigate, decide and quality-check cases; handle reports, notices, orders, appeals | Queues, evidence store, reviewer tools, QA sampling | Become the system of record for enforcement state |
| **Enforcement service** | Create, propagate, reconcile, expire and reverse enforcement actions | Action records, propagation receipts, reconciliation | Assume a published event was applied |
| **Statements, appeals and transparency** | Render statements of reasons, run complaints, feed regulators' databases and reports | Templates per jurisdiction, complaint workflow, reporting | Compose reasons from free text the decision did not record |

{id: stays-trust-and-safety--the-trust-decision-api}
### The trust decision API

Each gate sends the decision API a request in the same shape: who is acting (actor), what they want to do (action), on what (object), in what context (brand, market, channel, session), and which signals the caller already holds.

| Gate | Example action | Latency budget | If the platform does not answer in time |
| --- | --- | --- | --- |
| **Publish** | Listing goes live; property opens for sale | Seconds (asynchronous is fine) | Wait; publishing is not urgent |
| **Book** | Guest confirms a reservation | About 100–150 ms inside checkout | Fail open with a post-booking review, except where a legal gate applies |
| **Send message** | Host or partner sends a message containing a link | About 50 ms | Deliver with a link warning; scan after delivery |
| **Release payout** | A payable moves from pending to available | Minutes (batch) | Hold until answered |
| **Sensitive account action** | Bank-detail change, bulk export, new administrator | About 200 ms | Require step-up authentication |

The outcomes are richer than allow and deny. A useful set is **allow**, **allow with friction** (step-up authentication, an attestation, a link warning), **redirect** (offer another product: Airbnb's anti-party system lets blocked guests book a private room or a hotel room instead, as its 2022 announcement described ([Airbnb, 2022](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada))), **hold** (accept but stop the next step until reviewed), and **deny**. Every outcome returns reason codes the caller can show to the user, and an expiry, because a decision about a session should not be reused next week.

The fallback column turns architecture into policy. A trust platform that fails closed on the booking path turns its own outage into a sales outage; one that fails open everywhere is useless during an attack, which is when it is most likely to be overloaded. The rule I use: **fail open on revenue paths with a recorded post-decision review, fail closed on money release and legal gates, and make the choice per gate in configuration, visible to the business.** Registration checks in markets that require a number before publishing are legal gates; [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) covers them.

{id: stays-trust-and-safety--the-entity-graph}
### The entity graph

Bad actors reuse devices, phone numbers, payout accounts, photos, addresses and company registrations; the entity graph turns these into links between accounts. Airbnb described its identity graph in a 2026 engineering post as infrastructure that supports trust and safety "from detecting suspicious activities to identifying linked accounts", holding about 7 billion nodes and 11 billion edges, with most queries traversing four to eight hops ([Airbnb Engineering, 2026](https://airbnb.tech/infrastructure/scaling-airbnbs-identity-graph-with-a-unified-knowledge-graph-infrastructure/)). Link analysis catches what per-account scoring cannot.

A link is evidence, not guilt. A property manager's IBAN legitimately receives payouts for many owners. A family shares a device. A building's address is shared by twenty apartments. Each link type needs a **confidence and a meaning**, and policies should act on a combination (shared payout instrument *and* shared phone *and* one account suspended for fraud) rather than on a single shared attribute. The graph should also record **why** two entities are linked and from which source, because a statement of reasons may have to cite it.

{id: stays-trust-and-safety--the-risk-signal-feed}
### The risk signal feed

The Productscape reference model behind this book names a "risk signal feed" as a worker in its trust domain. In practice it is a set of event contracts domains already publish: listing created and changed, reservation requested and confirmed, message sent, login, bank details changed, refund issued, review submitted, report filed. The platform subscribes to them, as other consumers do ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)).

**Entity references must be canonical**: if the messaging service identifies senders by a messaging handle and the payout system by a beneficiary ID, the graph spends its life reconciling them. A group identity and a place registry ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access), [Hotels and Homes: Modeling What Is Being Sold](#property-and-listing-model)) make the feed cheap. **Sensitive content should stay where it lives**: the feed carries a message ID, extracted URLs and a classifier score, not the message body; it carries "ID verified, method, date", not the passport image. Investigators fetch content from the owning store with an audited request.

{id: stays-trust-and-safety--enforcement-and-its-propagation}
## Enforcement and Its Propagation

A decision is only an opinion until the systems that serve users change. In stays one entity lives in many systems, each with its own copy of state.

{id: stays-trust-and-safety--the-enforcement-ladder}
### The enforcement ladder

| Rung | Typical actions | Use when | Reversible by |
| --- | --- | --- | --- |
| **Inform** | Warning, policy reminder, education message | First low-severity violation | Expiry |
| **Add friction** | Step-up authentication, attestation (for example a no-party pledge), link warnings on messages | Elevated risk, unconfirmed | Expiry or successful verification |
| **Restrict** | Remove instant book, demote in search, limit messaging to templates, cap bookings per day | Confirmed lower-severity violation; risk under review | Review or expiry |
| **Hold** | Hide listing pending verification, hold payouts, hold new reservations for review | Credible high-severity risk, evidence incomplete | Review decision |
| **Suspend** | Account or listing suspended; calendar blocked; payouts held; reservations reviewed | Confirmed serious violation | Appeal or reinstatement |
| **Terminate** | Account closed; listings removed; remaining balances settled under terms | Repeated or severe violation; legal duty | Appeal; P2B notice rules apply to business users |

The ladder exists because **the cost of a wrong action rises with each rung**. A hold that hides a legitimate listing for six hours costs a few bookings; a wrongful termination of a professional manager with 300 units costs a partner and may breach the Platform-to-Business Regulation, which requires a statement of reasons at the time of a restriction or suspension and, for termination of the whole service, at least 30 days' notice except in defined cases such as repeated infringement ([Regulation (EU) 2019/1150, Art. 4](http://publications.europa.eu/resource/celex/32019R1150), applying from 12 July 2020).

{id: stays-trust-and-safety--what-one-enforcement-action-must-reach}
### What one enforcement action must reach

Turia's suspension reached the Nookaway catalog and search, and nothing else. A hosted-stays account suspended for fraud must reach these consumers:

| Consumer | What must change | Typical miss |
| --- | --- | --- |
| **Catalog and search** | Listings hidden; search index updated | Cached result pages and feeds to distribution partners |
| **Calendar** | New bookings blocked; existing reservations flagged | Partner-API and iCal channels keep accepting availability |
| **Reservations** | Future reservations reviewed: kept, moved or canceled with guest support | Reservations left confirmed and unattended |
| **Messaging** | Outbound messages blocked or limited to templates; guests warned | API tokens and PMS integrations still send |
| **Settlement ledger** | Payables move to held | Payout batch already scheduled |
| **Accounts and access** | Sessions revoked, API tokens and delegated grants suspended | Co-host and integration credentials |
| **Other brands** | Linked entities reviewed under each brand's policy | Not informed at all |

The miss column is the reason **enforcement must be a propagated event with receipts**. The enforcement service publishes the action; each consumer applies it and returns a receipt with the state it now holds; the service tracks the action as "in force" only when every required consumer has acknowledged. A reconciliation job compares, every few minutes for open actions and nightly for all, the enforcement record with each consumer's actual state, and opens an incident when they differ.

![Trust operations sends a suspension to the enforcement service, which fans it out to catalog, messaging, ledger, reservations and the other brand; each returns a receipt, and the action is reported in force.](stays-marketplace-architecture/posts/31-stays-trust-and-safety/assets/images/31-stays-trust-and-safety/31-enforcement-with-receipts.jpeg)

**Figure 4:** *Enforcement with receipts. An action is "in force" only when every required consumer has confirmed the state it now holds. A missing receipt is an alert, not an assumption, and the cross-brand step opens a review rather than copying the suspension.*

Enforcement is a write to many systems and needs the same guarantees as any other: inventory integrity applies them to reservations with acknowledgement watermarks ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)), and payouts to holds, where "held" is a balance state with an owner and an expiry rather than a flag on a payout row ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)).

{id: stays-trust-and-safety--reservations-are-the-hard-part}
### Reservations are the hard part

Hiding a listing is cheap; deciding what to do with its 31 future reservations is not, because real guests are attached to them. In a hosted-stays marketplace the options are to keep the reservation with monitoring (when the risk concerns the host's conduct, not the home's existence), to contact the guest and offer rebooking, or to cancel with a full refund and rehousing under the guest guarantee. Each option is a decision with a reason, a cost owner and a customer-service workflow ([When Something Goes Wrong: Customer Service and Recovery](#customer-service)). The enforcement action should **create the review work**, not leave reservations confirmed and invisible. Turia's 31 reservations sat for four days because the suspension had no rule for them.

In an accommodation marketplace the question is easier for hotels and as hard for holiday homes. Closing a hotel for a trust reason is rare; when it happens, reservations are usually honored or relocated under the partner terms used for overbooking ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)). Holiday homes and apartments from small managers behave like hosted stays.

{id: stays-trust-and-safety--integrity-operations}
## Integrity Operations

People handle what automation cannot: ambiguity, severity and appeals. Integrity operations usually grow without design, as queues in the customer-service case tool.

**Queues by severity, not by source.** A guest report, a model flag and a trusted flagger's notice about the same listing should land in one case, ranked by severity and time sensitivity. A guest who says "the host is at the door and threatening me" does not wait behind a review dispute: safety reports need an immediate path to a trained team with authority to rehouse the guest and, where needed, call emergency services. The Digital Services Act also requires a hosting provider that becomes aware of information giving rise to a suspicion of a criminal offence involving a threat to life or safety to inform law enforcement promptly ([Regulation (EU) 2022/2065, Art. 18](http://publications.europa.eu/resource/celex/32022R2065)), which needs a workflow with an owner, not an ad-hoc call.

**Evidence and decisions in one tool.** Reviewers see the entity graph, listing history, message excerpts, payout events and previous cases on one screen, every view of sensitive content logged, and record decisions as structured reason codes against a policy version, because the statement of reasons and the appeal are built from the codes.

**Quality assurance is sampling, not supervision.** A second reviewer re-decides a random sample of cases blind; agreement rates per policy and per reviewer show where policy is unclear or training is missing. Appeal outcomes are a second, biased sample: they over-represent decisions that someone cared enough to contest.

**Priority inputs from outside.** The DSA requires online platforms to process notices from trusted flaggers (entities that a Digital Services Coordinator has awarded that status) with priority and without undue delay ([Regulation (EU) 2022/2065, Art. 22](http://publications.europa.eu/resource/celex/32022R2065)). Short-term-rental authorities can order listings removed ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)). Both arrive as cases with service-level targets and must end in enforcement actions like any other.

**Capacity moves with the calendar.** Reports peak on summer weekends, event dates and holiday nights. Airbnb redirected more than 20,000 people in the US from booking entire homes over the July 4 weekend of 2025 ([Airbnb, 2026](https://news.airbnb.com/airbnbs-anti-party-system-returns-for-july-4-weekend)); the operational equivalent is staffing and a safety lane planned from the booking calendar, not from last month's average.

{id: stays-trust-and-safety--statements-of-reasons-appeals-and-transparency}
## Statements of Reasons, Appeals and Transparency

EU law turned explainability from good practice into an interface. Under the DSA, a hosting provider must give a "clear and specific statement of reasons" to affected users for restrictions of visibility (removal, disabling, **demotion**), for "suspension, termination or other restriction of monetary payments", for suspension of the service and for suspension of the account, imposed because content is illegal or incompatible with the terms ([Regulation (EU) 2022/2065, Art. 17](http://publications.europa.eu/resource/celex/32022R2065), applying from 17 February 2024). The statement must say what was decided and for how long, the facts relied on, whether automated means were used, the legal or contractual ground, and the routes to redress.

Online platforms must also run a free internal complaint-handling system for at least six months after a decision, reverse decisions "without undue delay" when a complaint shows them unfounded, and point complainants to out-of-court dispute settlement (Art. 20 and 21). They must submit their decisions and statements of reasons to the Commission's public, machine-readable database (Art. 24(5)), and must suspend users who frequently provide manifestly illegal content, after a warning, and set out that policy in their terms (Art. 23). Booking.com, designated a very large online platform in April 2023, publishes transparency reports under Articles 15, 24 and 42 and reports EU average monthly recipients "well above 45 million" for the first half of 2026 ([Booking.com, 2026](https://www.booking.com/content/dsa.html)). Corvane's two brands are below the very-large threshold, which spares them the risk-assessment and audit duties but none of the duties above.

**If the decision record holds the reason codes, the policy version, the evidence references, the automation flag and the scope, a statement of reasons is a rendering of the record.** If it does not, someone writes each statement by hand from case notes, and the transparency database receives whatever they wrote. Three details are easy to miss:

- **Demotion is a restriction.** A trust-driven ranking demotion owes the affected partner or host a statement of reasons, as Roomstead learned with its reliability demotion ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)). Ranking consumes trust decisions; it should not invent its own.
- **Payout holds are restrictions of monetary payments.** A payout hold that the ledger applies without a decision record cannot produce a statement.
- **Reasons must be specific without teaching the attacker.** "Your listing was removed under our misrepresentation policy because photos match images published elsewhere and guests reported the address as a private home" is specific. Listing the model features and thresholds is not required and would help the next fraudster.

Because the P2B Regulation adds notice rules for business users only, the decision record also needs the **trader or non-trader status** captured at onboarding ([From Sign-Up to First Booking: Partner and Host Onboarding](#partner-onboarding)).

{id: stays-trust-and-safety--measuring-trust}
## Measuring Trust

Trust work fails quietly in two directions: harm that is not caught, and good users who are blocked. Both need numbers with owners.

| Metric | What it shows | Watch out for |
| --- | --- | --- |
| **Harm rate per 10,000 stays** by type (safety reports, party reports, scam losses, listing-not-as-described) | Whether the marketplace is getting safer | Reporting rates change with product design; a better report button raises the metric |
| **Prevalence** of violating listings, from random audits | How much bad supply is live | Reports and model flags find only what they look for |
| **Time to action** from first signal to enforcement in force | Whether detection and propagation are fast enough | Measure to the last receipt, not to the decision |
| **Propagation completeness**: actions with all receipts within target | Whether enforcement is real | Consumers added after the platform was built |
| **Precision of enforcement**: appeal overturn rate; QA disagreement | Whether actions hit the right people | Few non-English speakers and small hosts appeal |
| **Good-user friction**: share of bookings blocked, redirected or stepped up, and their conversion | The revenue cost of controls | Blocked guests who would have been fine are invisible without holdouts |
| **Disparity** of decision rates across guest groups | Whether controls or hosts discriminate | Measuring protected characteristics is itself regulated |
| **Loss**: guarantees, reimbursements and goodwill paid | The money trust costs | Losses land in many budgets |

Airbnb's anti-discrimination work measured the gap in booking success rates between guests by **perceived race**, using a privacy-preserving pipeline with p-sensitive k-anonymity; in a sample of 750,000 US reservation requests from 2021, the booking success rate was 91.4% for guests perceived as Black against 94.1% for guests perceived as white ([Airbnb, 2022](https://news.airbnb.com/sixyearadupdate); method in [Basu et al., 2020](https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf)). The method is US-only. In the EU, data revealing racial or ethnic origin is a special category under GDPR Article 9, so a European platform needs a legal basis and a design reviewed by its privacy office before measuring anything similar. What every platform can do without such data is to **reduce discretionary decisions** (Airbnb's 2022 update describes expanding instant book eligibility and more guests getting reviews as remedies) and to audit its own models for features that proxy for protected traits, such as names or photos.

{id: stays-trust-and-safety--in-practice-what-public-sources-show}
## In Practice: What Public Sources Show

Companies describe trust outcomes and products more than systems, but what is documented supports the shape argued above.

**Airbnb** lists its "system for trust" in its annual report for fiscal 2025: reviews, account protection, risk scoring, secure payments, a nondiscrimination policy, watchlist and background checks in certain jurisdictions, fraud and scam prevention, insurance and similar protections, booking restrictions, safety and neighborhood support lines, anti-party technology and a guest refund policy ([Airbnb 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm)). The same filing is candid about limits: "We do not verify all listings for safety or compliance, relying instead on user-reported issues". Two architectural facts are visible in Airbnb's public descriptions. Identity verification became a **booking-path gate** in 2023: unverified primary hosts have their calendars blocked and unverified guests cannot book ([Airbnb, 2023](https://news.airbnb.com/an-update-on-identity-verification-on-airbnb)). And the anti-party screening returns **more than two outcomes**, redirecting some guests to private rooms or hotels rather than rejecting them. Airbnb reported that 0.039% of its 2022 reservations led to a party allegation ([Airbnb, 2023](https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior)); these are self-reported figures. How its risk models, thresholds and enforcement plumbing are built is not public.

**Booking.com** has published little about its own trust systems, but its partner-account campaigns of 2023–2025 are well documented by security researchers. Criminals stole hotel staff credentials with infostealer malware, logged into the extranet and messaged real guests through the platform asking for "payment verification" ([Secureworks via Sophos, 2023](https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam); [Krebs, 2024](https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/)). Booking.com told Krebs that its internal systems were not compromised and that the attacks stemmed from partners' machines. The lesson here is enforcement scope, not detection: once a partner account is suspected, the action must reach **messaging and guests' upcoming reservations**, not only the login. [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) treats the attack chain in depth.

**Device policy as data.** Airbnb's widely reported March 2024 ban on indoor security cameras, with outdoor cameras allowed if disclosed with their location before booking ([ABC7 News, 2024](https://abc7news.com/airbnb-bans-the-use-of-indoor-security-cameras-on-all-properties/14516158/)), works only as a **structured listing attribute** that the publish gate checks, the listing page shows and a guest report can contradict.

> **INFERENCE, NOT DOCUMENTED:** Neither company has published how its decisions propagate to calendars, messaging and payouts, or whether it keeps a single decision record across products. The propagation design in this chapter is a reference architecture derived from the documented attack chains and from the obligations in Articles 17, 20 and 24 of the DSA, not a description of either company's systems.

{id: stays-trust-and-safety--corvane-worked-example-warden-and-the-turia-replay}
## Corvane Worked Example: Warden and the Turia Replay

The architecture forum approved **Warden**, the group trust platform, on 17 August 2027. Its scope followed the split argued above.

- **Shared in Warden:** the entity graph (built on Corvane ID accounts, the place registry and Corvane Payments' beneficiary records), the policy registry, the decision service and log, the enforcement service with receipts, one case tool for both brands' integrity teams, and the statements-of-reasons and complaints service.
- **Kept with the brands:** detectors. Nookaway keeps reservation screening and listing-risk models; Roomstead keeps payment-fraud rules and partner-session anomaly detection. Each registers its detectors' outputs as signals, and its policies as versions in the registry.
- **Cross-brand rule:** a suspension for fraud in one brand never suspends an account in the other automatically. It opens a **linked-entity review** in the other brand, and Warden applies a hold there if the link score crosses a policy threshold. The hold hides listings or properties pending review, restricts messaging to templates and blocks free-text payment requests. Noor van Dijk, Head of Regulatory Affairs and Privacy, required that both brands' terms describe cross-brand reviews and that each hold produces its own statement of reasons.

Warden runs on AWS in eu-central-1, beside Corvane Payments, because payout holds and payment signals are its most frequent writes. Nookaway's booking gate calls it from Google Cloud with a 120-millisecond budget and fails open into post-booking review. The first release, in **Q4 2027**, covered Nookaway's publish, booking and payout gates and Roomstead's partner bank-detail changes; Roomstead's message-send gate follows in **Q1 2028**.

The forum asked for a replay of the Turia case against Warden, using the recorded events.

| Step | July 2027 (actual) | Replay with Warden |
| --- | --- | --- |
| Suspension at Nookaway, 8 July 16:20 | Listings hidden in catalog and search | Same action, propagated to seven consumers; all receipts by 16:24 |
| Partner-API token and messaging | Still active until 12 July; 6 guests pay €5,100 | Tokens revoked at 16:21; guests with future stays get a warning message |
| Future reservations (31) | Confirmed and unattended for 4 days | 31 review tasks created at 16:22; guests contacted within the guest-guarantee target |
| Payout of €2,940 | Released 9 July | Payables held in Fathom at 16:22 |
| Roomstead account | Unknown until 24 July | Linked-entity review opened at 16:22 (shared IBAN, shared phone, fraud suspension); link score above threshold, so Roomstead property held at 16:23 |
| Roomstead guests who paid | 22, €27,400 | 3 who paid before 8 July (€3,800); the 19 later payments (€23,600) would most likely not have happened |

On these numbers the replay avoids **€5,100 + €2,940 + €23,600 = €31,640** of the €48,540 Corvane lost or reimbursed on the case (€11,900 + €27,400 + €6,300 + €2,940), plus the 16 days in which Roomstead kept taking bookings for flats that did not exist. It does not avoid the first €10,600 paid before anyone suspected Turia. That part belongs to detection: photo reuse across brands, registration numbers checked against the unit they belong to, and message classifiers on Roomstead as well as Nookaway. The forum assigned those to [Describing a Stay: Content, Media and Property Mapping](#content-and-media), [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) and [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud).

![Two coin columns: the full Turia loss on the left, and on the right a shield deflecting most of it, with a small remaining stack marked for detection.](stays-marketplace-architecture/posts/31-stays-trust-and-safety/assets/images/31-stays-trust-and-safety/31-turia-replay.jpeg)

**Figure 5:** *Replayed against Warden, enforcement with receipts avoids €31,640 of the €48,540 the Turia case cost; the money paid before anyone suspected Turia remains a detection problem.*

The replay also produced a warning. Run against all of 2026, the same cross-brand link rule would have opened **1,140** linked-entity reviews, and a sample of 200 suggested that about 70% concerned legitimate property managers whose shared IBAN served many owners. Sofia's team added a policy condition: shared payout instruments of verified property-management companies count as a link only together with a second, independent signal. That cut the projected reviews to about **310** a year. A cross-brand rule that floods the other brand's queue with honest partners would have been switched off within a month.

{id: stays-trust-and-safety--trade-offs}
## Trade-offs

| Option | How it works | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- | --- |
| **Embedded per domain** | Each domain builds its own checks and enforcement state | Fast to start; checks close to the data | No single record; enforcement does not cross domains; duplicated policy | One small product, few risks |
| **Central trust service in every path** | One service decides and enforces everything, synchronously | One policy, one record | Bottleneck on every write; knows too little about each domain's risk; outages spread | Rarely; small catalog, simple risks |
| **Platform: shared decisions and enforcement, distributed detection** | Domains own detectors and gates; the platform owns decisions, enforcement, cases and statements | One record and one enforcement path; domain expertise preserved | Needs canonical entity IDs and disciplined event contracts; propagation must be built | Most marketplaces with several products or brands |

Three smaller trade-offs recur in design reviews.

| Choice | Option A | Option B | My default |
| --- | --- | --- | --- |
| **Timing** | Synchronous decision at the gate | Asynchronous review after the event | Synchronous for booking, money release and sensitive account actions; asynchronous with fast holds for content and messages |
| **Automation** | Automatic enforcement | Human decision | Automatic up to "hold" for high-confidence signals; humans for suspension and termination of business users, and for anything with an ambiguous safety dimension |
| **Cross-brand action** | Copy enforcement across brands | Open a review in the other brand | Review with a threshold-based hold; never automatic suspension |

Copying enforcement across brands spreads a false positive to every product a partner sells through; a review with a bounded hold gives most of the protection, as the Turia replay showed, and keeps each brand's decision explainable under its own terms.

{id: stays-trust-and-safety--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

The two marketplaces differ in their trust risks, not in the plumbing.

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Who must be trusted** | The platform's accuracy and payment handling; the hotel is a licensed business with staff | A private home and a stranger, in both directions |
| **Dominant threats** | Takeover of hotel extranet accounts, then guest phishing; card fraud; fake holiday-home listings in the apartment segment | Fake listings, off-platform payment scams, host account takeover, parties and damage, harassment |
| **Main gates** | Partner login and sensitive actions; message send; checkout for payment fraud | Publish; booking (screening, identity); message send; payout release |
| **Guest identity** | Usually checked at the front desk by the hotel | Commonly verified by the platform before booking |
| **Physical safety** | Hotel regulation, fire codes, staff on site | Platform policy, listing attributes, screening, safety line |
| **Enforcement targets** | Properties with many rooms and reservations; partner staff accounts | Individual listings and hosts; co-hosts; professional managers with many listings |
| **Cost of a wrong suspension** | High per partner (a hotel's whole distribution), rare | Lower per listing, frequent; high for large managers |
| **Reviews** | One-way, guest about property | Two-way; guest reviews feed risk decisions |
| **Regulatory weight** | DSA duties; P2B notice rules for business users; STR rules for the apartment segment only | DSA duties; P2B for professional hosts; STR rules for nearly all supply |

**What to share.** The decision record, enforcement service with receipts, entity graph, policy registry, case tool, statements-of-reasons service and transparency reporting are the same problem in both marketplaces. Sharing them lets a fraud case in one brand reach the other, and they carry the heaviest legal requirements, so build them once.

**What not to share.** Detection models and their thresholds. A reservation-screening model trained on party reports in homes has nothing to say about a hotel booking, and a partner-session anomaly model trained on hotel staff behavior fits individual hosts badly. Policies are partly shared: off-platform payment, harassment and discrimination policies should read the same in both brands; party, device and listing-accuracy policies are hosted-stays policies that apply to Roomstead's apartment segment, not to its hotels. That is real convergence: an OTA that sells holiday homes should adopt hosted-stays trust policies for that supply rather than invent its own.

{id: stays-trust-and-safety--failure-modes}
## Failure Modes

- **The partial suspension.** Listings disappear from search while the calendar sells through the partner API, messages still flow and confirmed reservations wait unattended. *Fix:* enforcement with receipts and reconciliation, and reservation review work created by every account- or listing-level action.
- **Flags without owners.** "Suspended", "blocked" and "risky" flags in a dozen databases, set by scripts and support tools, with no reason or expiry. Nobody can say why an account is restricted or lift the restriction cleanly. *Fix:* enforcement state lives only in the enforcement service; domain flags are projections that it writes and reconciles.
- **Statements written by hand.** Statements composed from case notes disagree with the decision and send inconsistent text to the transparency database. *Fix:* render statements from the decision record's reason codes and policy versions.
- **Unmeasured models.** A screening or listing-risk model blocks bookings or hides listings for months without precision measurement, holdouts or a link from appeals to its training data (The Unwatched Model). *Fix:* every detector has an owner, an evaluation set, a holdout, drift monitoring and a feed of appeal outcomes.
- **Link-based overreach.** Shared IBANs, addresses or devices trigger automatic action against legitimate property managers, families or apartment buildings, as the Turia replay's first rule would have done. *Fix:* link types with confidence, actions on combinations of signals, and humans before suspension.

{id: stays-trust-and-safety--the-chief-architect-s-view}
## The Chief Architect's View

**Decide what "one trust platform" means before building it.** To different people the phrase means one vendor, one team, one model or one database. The useful definition is narrower: **one decision record, one enforcement path with receipts, one entity graph, one case tool and one statements service**, with detection distributed. Write that definition down, because it sets what each brand must give up (its own enforcement flags) and what it keeps (its models).

**Make enforcement a contract every domain signs.** Every system that serves users accepts actions through one interface, returns receipts and supports reconciliation; new systems join the consumer list before they launch, not after the first incident. Once the contract exists, the next scam wave tests detection, not plumbing.

**Govern policies like code and like law.** Trust policies change after incidents, during holidays and when regulators write. Changes need a version, an approver from trust and from regulatory affairs, an effective date and a record of which decisions used which version. The registry is also where holiday modes and market variants live, so they are reviewable instead of hidden in model thresholds.

**Who decides.** The Director of Trust and Safety owns policy and integrity operations. Brand engineering leads own their detectors and gates. The platform team owns the decision service, enforcement and the graph. Regulatory affairs is a mandatory reviewer of statements, cross-brand rules and anything touching special-category data. The architecture forum owns the enforcement contract and the list of consumers that must honor it.

**What to watch.** The metrics in the table above, plus the size and age of the safety queue on peak nights. Read them in pairs: when a detector's appeal overturn rate rises, it is drifting; when time to enforcement rises while time to decision does not, a consumer has stopped honoring the contract.

**The long view.** Regulation increasingly treats trust decisions as reviewable acts, and agents acting for guests and hosts will add a new kind of actor to the decision API ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)). Decisions recorded with reasons absorb both changes; flags do not.

{id: stays-trust-and-safety--questions-to-ask}
## Questions to Ask

1. If we suspend an account now, which systems will still let that account sell, message or get paid in an hour, and how would we know?
2. Where does enforcement state live? Can we list every restriction on an account, with its reason, policy version, scope and expiry, from one place?
3. What does each gate do when the trust service does not answer in time, and who in the business agreed to that behavior?
4. Which detectors make consequential decisions, who owns each one, and what are their appeal overturn rates and holdout results?
5. Can we render a DSA statement of reasons for any restriction from the decision record, without reading case notes?
6. What happens to confirmed reservations when a listing or property is suspended, and who pays for the guest's alternative stay?
7. How do links between accounts get created and weighted, and which link types alone are never enough to act?
8. Does a fraud suspension in one brand reach the others, and under which terms and statements?
9. How are integrity operations staffed on the busiest night of the year, and where do safety reports go?
10. How would we know if our controls or our hosts' decisions treat some groups of guests worse than others?

The trust platform gives the marketplace a way to decide and to act. The most expensive decisions it makes are about fraud: stolen cards at checkout, hijacked hotel extranets messaging real guests, fake homes collecting deposits and promotions abused at scale. [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) takes those threats one by one, with the extranet phishing wave that reached Roomstead's guests in November 2027 as its worked example.

{id: stays-trust-and-safety--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Airbnb, Inc. Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), Airbnb / SEC EDGAR, 2026: the "system for trust" components, the stated limits of verification and listing checks, AI-assisted risk assessment.
- [Scaling Airbnb's identity graph with a unified knowledge graph infrastructure](https://airbnb.tech/infrastructure/scaling-airbnbs-identity-graph-with-a-unified-knowledge-graph-infrastructure/), Airbnb Engineering, 2026: identity graph for trust and safety, linked accounts, scale.
- [An update on identity verification on Airbnb](https://news.airbnb.com/an-update-on-identity-verification-on-airbnb), Airbnb Newsroom, 2023: verification of all booking guests and primary hosts; calendars blocked for unverified hosts.
- [Airbnb introduces new anti-party technology in the US and Canada](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada), Airbnb Newsroom, 2022: screening signals and redirect outcome.
- [An update on our work to crack down on parties and disruptive behavior](https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior), Airbnb Newsroom, 2023: party-allegation rate for 2022 reservations.
- [Airbnb's anti-party system returns for July 4 weekend](https://news.airbnb.com/airbnbs-anti-party-system-returns-for-july-4-weekend), Airbnb Newsroom, 2026: holiday-period redirects in 2025.
- [A six-year update on Airbnb's work to fight discrimination](https://news.airbnb.com/sixyearadupdate), Airbnb Newsroom, 2022: booking success rates by perceived race (2021 data) and interventions.
- [Measuring discrepancies in Airbnb guest acceptance rates using anonymized demographic data](https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf), Basu et al., Airbnb, 2020: privacy-preserving measurement method.
- [Digital Services Act](https://www.booking.com/content/dsa.html), Booking.com, 2026: VLOP status, average monthly recipients, transparency reports.

*Standards, regulation and documentation*

- [Regulation (EU) 2022/2065, Digital Services Act](http://publications.europa.eu/resource/celex/32022R2065), European Union, 2022: Articles 17 (statement of reasons), 18 (notification of suspected criminal offences), 20–21 (complaints and out-of-court settlement), 22 (trusted flaggers), 23 (misuse), 24(5) (transparency database); applies from 17 February 2024.
- [Regulation (EU) 2019/1150, Platform-to-Business](http://publications.europa.eu/resource/celex/32019R1150), European Union, 2019: Article 4 statements of reasons and 30-day notice for termination of business users; applies from 12 July 2020.
- [Regulation (EU) 2016/679, GDPR](http://publications.europa.eu/resource/celex/32016R0679), European Union, 2016: Article 9 special categories of data.

*Research and practitioner sources*

- [Vidar infostealer steals Booking.com credentials in fraud scam](https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam), Secureworks Counter Threat Unit (on Sophos), 2023: extranet credential theft and guest messaging abuse.
- [Booking.com phishers may leave you with reservations](https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/), Brian Krebs, KrebsOnSecurity, 2024: in-app phishing after partner compromise; Booking.com's statement.
- [Airbnb bans the use of indoor security cameras on all properties](https://abc7news.com/airbnb-bans-the-use-of-indoor-security-cameras-on-all-properties/14516158/), ABC7 News, 2024: indoor camera ban and outdoor disclosure rule (press report).

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
