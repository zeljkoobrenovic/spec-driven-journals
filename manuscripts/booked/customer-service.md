{id: customer-service}
# 25. When Something Goes Wrong: Customer Service and Recovery

![When Something Goes Wrong: Customer Service and Recovery — logo](stays-marketplace-architecture/posts/25-customer-service/assets/images/25-customer-service/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Design customer service for a stays marketplace as a platform: contact drivers and the taxonomy that names them, a case model that spans guest, property or host and marketplace, service levels tied to arrival time, recovery decisioning for refunds, relocations and compensation, the context agents need, self-service and AI agents grounded in live reservation state, and the surge mode for disruptions.

> **WHY THE BUSINESS CARES:** Support is one of the largest operating costs after marketing, and for many guests it is the only part of the marketplace they ever talk to. The hours after a problem decide whether the guest books again, whether the partner or host stays, and how much the marketplace pays to put things right. Each recovery that nobody records is money the marketplace cannot recover from the party that caused it.

> **WHY ARCHITECTS SHOULD CARE:** A support agent's screen is a read model over almost every system in the platform: reservations, payments, messages, inventory, trust and partner contracts. If support runs on a ticketing tool with copied data and free-text outcomes, every recovery becomes an untracked side effect, every policy is re-encoded in agent scripts, and an AI agent added on top only repeats the same errors faster.

> **KEY POINTS:**
>
> * **The unit of support is a case bound to reservations and parties, not a ticket bound to a caller.** Most stays problems involve the guest, the property or host and the marketplace at once, and a deadline set by arrival, not by the contact center's service level. A case that links the reservations, the parties, a contact reason and an arrival clock can be opened by events before anyone calls.
> * **A recovery is a decision with a policy, a funder and a liable party.** Refunds, relocations, credits and goodwill payments should be produced by a recovery-decision service that applies versioned entitlement rules, enforces approval limits and posts to the ledger, so the cost reaches the party that caused it and the next policy change does not mean retraining thousands of agents.
> * **Contact drivers are the backlog; AI agents are one more client of the same APIs.** The cheapest contact is the one the product prevents. An AI agent that answers from live reservation state and acts only through the tools and policies human agents use can resolve a large share of routine issues. Judge it by verified resolution and reopen rate, not by how many conversations it kept from humans.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Lost at the Front Desk** — when the guest learns about an oversold room or a missing booking at the desk, support starts working at the worst possible time, with the least context and the highest replacement prices.
> * **Policy Spaghetti** — refund and compensation rules copied into agent scripts, macros and vendor knowledge bases give a different answer from checkout, payments and the partner's terms.
> * **Built for Sunny Days** — a contact center sized for normal weeks receives a strike, a storm or a mass cancellation as thousands of identical calls, unless the platform can turn the event into one decision and a self-service flow.

An accommodation marketplace sells a promise that someone else fulfills, weeks or months later, in a place the marketplace never sees. When that promise breaks, the guest does not call the hotel's revenue manager or the host's channel manager. They call the marketplace, usually from a train, a taxi or a hotel lobby, with a deadline measured in hours. **Customer service in stays is the failure path of the whole platform**, and its design decides whether a broken promise costs a phone call or a customer.

Three things make stays support harder than retail support. **Most cases have three parties**: the guest, the property or host, and the marketplace, and the party who must act is often not the party who called. **The clock is set by the stay**, not by the queue: a missing booking found two weeks before arrival is an e-mail; found at 23:00 on the arrival night it is a relocation at peak prices. And **the remedies cost money and move it between parties**: a relocation, a refund for a non-refundable rate or a goodwill credit is paid by someone and is often owed by someone else.

This chapter closes [Part V — BOOKING: Making and Keeping the Reservation](#part-5). It owns the **case**, the **contact driver** and the **recovery decision**. It builds on the reservation state machine and delivery of [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), on the cancellation policy engine and declared events of [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations), and on the conversation store and notifications of [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging). It does not re-teach damage claims and safety incidents ([Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents)), oversell prevention and the liability matrix ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)), or refund accounting ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)); it shows how support uses each.

{id: customer-service--setting-the-scene-at-corvane-four-guests-on-king-s-day}
## Setting the Scene at Corvane: Four Guests on King's Day

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs **Roomstead**, an accommodation marketplace in the style of an online travel agency (OTA) that sells 640,000 properties by room type and rate plan, and **Nookaway**, a hosted-stays marketplace with 1.15 million listings. In 2027 the two brands ran support on different stacks: Roomstead on a commercial software-as-a-service (SaaS) case-management tool staffed by two outsourced contact-center vendors, Nookaway on an in-house case tool built inside Burrow, its Django monolith. Elena Petrova, VP Customer Service, reported to both brands and owned neither tool's data model.

On 26 April 2027 the channel manager of **Hotel Prinsenkade**, an independent 140-room hotel in Amsterdam, stopped sending updates for **47 minutes**. Every channel kept selling its last count for the night of 27 April, King's Day, and the hotel ended **9 rooms** oversold. [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) tells the integrity side of the story. This chapter follows the four Roomstead guests whose stays the hotel could not honor, as Elena's team reconstructed them in May. Times are Central European Summer Time; the minute-level detail is illustrative.

| Time (27 April) | What happened | Systems involved |
| --- | --- | --- |
| 11:20 | Prinsenkade's front office e-mails Roomstead partner support: "overbooked tonight, 4 of your guests affected, please relocate" | Partner-support mailbox at vendor A |
| 13:05 | A partner-support agent opens a partner ticket and forwards it to the guest-service queue at vendor B | Two ticket queues, no shared case |
| 13:40–14:30 | Four guest-service agents each open a guest ticket, find the reservation in Keystone, Roomstead's Java monolith, and phone the guests | SaaS tool, Keystone screens, phone |
| 14:30–16:10 | Agents search Roomstead's own website for rooms on King's Day; two guests are already on their way and cannot be reached | Public website, agents' notes |
| 15:10 and 16:20 | Two guests learn of the relocation at the hotel's front desk | — |
| 16:45 | All four are rehoused, two in Haarlem and two in Amstelveen, booked by agents as new Roomstead merchant reservations paid with a service-recovery card | Keystone, Corvane Payments |
| 3 May | A team lead e-mails partner finance asking to recover the cost from the hotel | E-mail, spreadsheet |

The relocations cost **€2,150** including taxis. Partner finance recovered **€1,600** from the hotel, the €400 cap per relocated reservation in Roomstead's partner terms for each of the four guests, as a line on Prinsenkade's April statement ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)). The remaining €550 was Roomstead's.

The review found more than an expensive afternoon. The four guests generated **11 contacts** and about **6 hours 40 minutes** of agent time across three tools. The four new reservations had no link to the originals, so Roomstead's reporting counted them as ordinary bookings and the original reservations as guest cancellations. The cause code "overbooking – property" was free text in one of the four tickets and missing from the other three. And the earliest moment Roomstead could have known was **19:01 on 26 April**, when fresh counts arrived showing negative availability: about 16 hours before the hotel's e-mail and 20 hours before the first guest reached the desk.

![Scattered tickets across three desks for four guests and a hotel, compared with one case folder tied to the reservations, the hotel and the guests with an arrival clock.](stays-marketplace-architecture/posts/25-customer-service/assets/images/25-customer-service/25-tickets-versus-case.jpeg)

**Figure 1:** *On King's Day four guests produced 11 contacts across three tools because each ticket was bound to a caller; a case bound to the reservations, the parties and the arrival clock keeps them as one record.*

Elena's question to the One Stay architecture forum, the group program that decides what Roomstead and Nookaway share, was therefore not "which case tool should we buy". It was **"what should support know, decide and record, and which of that should be one group capability?"**

{id: customer-service--the-vocabulary-of-support}
## The Vocabulary of Support

Support vocabulary comes from contact centers, and contact-center words count the wrong things for a marketplace. The definitions below are the ones this book uses.

| Term | Definition | Why it matters in stays |
| --- | --- | --- |
| **Contact** | One inbound or outbound interaction in one channel: a call, a chat session, an e-mail, a message to the AI assistant | The unit vendors bill and staffing models count |
| **Contact driver** (contact reason) | The underlying reason for a contact, from a controlled taxonomy: "cancel a refundable booking", "property says no reservation", "listing not as described" | The routing key for self-service, AI and human skills, and the link from support to product defects |
| **Case** | The record of one problem, binding parties, reservations, contact driver, deadlines, actions and outcome; may span many contacts and channels | The unit a marketplace should manage, measure and pay for |
| **Arrival clock** | The deadline set by the stay itself: time to check-in, time to check-out, a cancellation deadline | Decides urgency more than any service level does |
| **Service level** (service-level agreement, SLA) | A target such as "80% of calls answered in 60 seconds" or "first reply to e-mail within 24 hours" | Measures the queue, not the outcome |
| **Recovery decision** | A recorded remedy for a case: refund, rebooking, relocation, credit, goodwill payment, fee waiver; with the rule version, amount, funder and liable party | Turns support outcomes into money facts that finance and partner terms can use |
| **Deflection / containment** | The share of contacts that self-service or an AI agent ends without a human | Easy to inflate; says nothing about whether the problem was solved |
| **Resolution** | The case's problem is solved and stays solved, measured by no reopening or repeat contact within a window | The outcome the marketplace pays for |

Two distinctions carry the chapter. A **contact is not a case**: King's Day was 4 cases and 11 contacts. And a **ticket outcome is not a recovery decision**: "resolved – relocated" in free text is a story; a decision with an amount, a funder and a liable party is something finance can recover.

{id: customer-service--what-guests-partners-and-hosts-contact-support-about}
## What Guests, Partners and Hosts Contact Support About

The contact-driver distribution is the most useful document support owns: it says where the product is failing.

The public evidence on volumes is thin but consistent in scale. Expedia Group's chief executive said on the first-quarter 2026 earnings call that the group handles "more than 250 million service interactions a year with over half resolved through self-service", with more than 30% powered by AI ([Hotel Dive, 2026](https://www.hoteldive.com/news/expedia-ai-enhance-customer-support-acquire-new-customers/819968/), secondary report of the call). Airbnb's 2020 annual report said that "approximately 7,570 third-party partners that are spread across 24 sites" handled "the vast majority of our community support contacts" ([Airbnb Form 10-K FY2020](https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm), 2021; evidence age: 2020, the current number is not public), and its 2025 report still says that "the vast majority of our community support is performed by third-party service providers" ([Airbnb Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026). Booking Holdings' 2025 report names customer service, "including outsource arrangements", as a risk ([Booking Holdings Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm), 2026). Outsourcing is the norm, and that is an architecture constraint: most cases are handled by another company's staff, in its tools.

The taxonomy itself has a documented example. In a 2025 engineering post on its voice support, Airbnb described a conversational interactive voice response (IVR) system that asks callers why they are calling, classifies the answer against a **contact reason** taxonomy through an "Issue Detection Service" in under 50 ms on average, retrieves a help article for self-service and escalates to a human agent with the context attached ([Airbnb Tech, 2025](https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/)). The reusable lesson is that the contact reason is a shared routing key, not a reporting label.

Corvane's first comparable distribution, built by Elena's team in June 2027 from 2026 data, looked like this.

| Contact driver group | Roomstead share | Nookaway share | Who must act | Product owner of the defect |
| --- | --- | --- | --- | --- |
| Cancel or get a refund | 27% | 21% | Guest (self-service), property or host for waivers | [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) |
| Change dates, guests or room | 14% | 6% | Property or host; marketplace re-prices | [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) |
| Payment, invoice, "why was I charged" | 12% | 9% | Marketplace or property | [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments), [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) |
| Special requests and arrival details | 11% | 4% | Property or host | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| Booking not found, confirmation missing | 9% | 2% | Property, marketplace | [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle) |
| Property or host not responding | 3% | 13% | Property or host | [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| Problem on arrival: no room, cannot get in | 7% | 12% | Marketplace, property or host | [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity), [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) |
| Not as described, cleanliness, amenities | 5% | 9% | Marketplace decides; property or host remedies | [Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation), [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) |
| Damage, safety, disputes between parties | under 1% | 6% | Marketplace | [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents) |
| Account, login, verification | 5% | 10% | Marketplace | [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| Other | 7% | 8% | — | — |

Volumes and costs, 2026:

| | Roomstead | Nookaway |
| --- | --- | --- |
| Guest contacts | 10.9 million | 1.5 million |
| Partner or host contacts | 1.4 million | 0.8 million |
| Contacts per stayed reservation | 0.41 | 0.38 |
| Cases | 6.2 million | 1.3 million |
| Support cost | €61 million | €24 million |
| Cost per case | €9.80 | €18.50 |

Three readings mattered to the forum. First, **much of Roomstead's volume was about things the guest could in principle do alone**: cancel a refundable booking, find a confirmation, read a policy. Those are product and self-service defects, not staffing problems. Second, **Nookaway's expensive cases were between two private parties**: hosts not responding, failed check-ins, homes not as described, damage. No self-service flow resolves "the host says the guest broke the table"; it needs evidence and a judgement. Third, **"booking not found" and "no room on arrival" were Roomstead's most expensive drivers per case**, and both were detectable by Roomstead's own systems before the guest called.

Policy design moves the distribution: in its third-quarter 2025 letter Airbnb said new cancellation-policy options were "reducing customer service cases" in initial tests ([Airbnb Q3 2025 Shareholder Letter](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf), 2025).

{id: customer-service--the-architecture-of-a-support-platform}
## The Architecture of a Support Platform

Most marketplaces start with a ticketing tool and integrate outwards: a reservation lookup here, a refund button there. The tool then knows contacts and agents, and the platform does not know what support decided. The architecture below inverts that: **the marketplace owns the case, the context and the recovery decision; the contact-center tools own channels, queues and the agent desktop.**

![Bought channels, an AI assistant and an agent desktop feed a marketplace-owned case service, which also opens proactive cases from events, reads a context model and calls recovery decisioning, which acts through domain APIs and posts to the ledger.](stays-marketplace-architecture/posts/25-customer-service/assets/images/25-customer-service/25-support-platform.jpeg)

**Figure 2:** *The support platform as a marketplace capability. Channels and the agent desktop can be bought; the case, the context read model and recovery decisioning belong to the marketplace, because they read its events and move its money.*

| Component | Responsibility | Interfaces | Owned by |
| --- | --- | --- | --- |
| **Channels and agent desktop** | Telephony, chat, e-mail, routing to skills, agent workspace, quality monitoring | Contact-center platform APIs; embeds the marketplace's case and context views | Bought; configured by customer-service operations |
| **Case service** | Case lifecycle, parties, linked reservations, contact driver, arrival clock, ownership, escalations, audit | Case API (create, link, assign, transition), case events | Marketplace support platform team |
| **Contact-driver taxonomy** | Versioned list of reasons, mapping to skills, self-service flows and product owners | Reference data with versions and migrations | Support operations with product, under change control |
| **Context read model** | One view of the reservation, payment state, messages, inventory signals, partner health and trust flags for a case | Read-only query API built from events | Marketplace support platform team |
| **Recovery decisioning** | Applies entitlement rules, enforces approval limits, computes funder and liable party, issues actions | Decision API; reads policy engine, liability matrix and declared events | Marketplace, with finance as co-owner of limits |
| **Relocation service** | Finds comparable stays, books the replacement as a linked reservation, records cause | Search and booking APIs of both brands | Marketplace, shared with [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) |
| **AI assistant** | Classifies, answers from curated content, acts through tools within limits, hands off with context | Same case, context and decision APIs as agents | Marketplace AI platform with support |

The design choices that matter:

- **Cases are opened by events, not only by contacts.** An unacknowledged reservation for an arrival within 48 hours, negative headroom after an inventory refresh, a declined scheduled charge, a host cancellation, a calendar conflict found on import: each should open a case with the right driver and clock before the guest notices. [Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools) describes the partner-facing exception queue; the case service reads the same events, so a partner's unresolved exception and a guest's case are one record seen from two sides.
- **The context read model is built from events, not from screen scraping.** The agent should see the reservation's version history, the payment plan and its state, the conversation with the property or host, the delivery and acknowledgement status, and the policy that applied at booking. That is a projection over reservation, payment and messaging events ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)); at Corvane, over Stayline's reservation events, Corvane Payments' payment state feed, Threadline's conversations and the trust decisions of Warden, the group trust platform ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)). Copying data into the vendor's tool creates a second, stale truth that agents then quote to guests.
- **Actions go through the domain APIs, never around them.** A refund is a call to payments with an idempotency key and a reason; a date change is a modification through the reservation service; a relocation is a booking. An agent tool that writes directly into a database, or a "refund" that is a manual bank transfer, is how support creates the reconciliation gaps that finance later chases ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)).

{id: customer-service--the-case-model}
### The case model

A case has more structure than a ticket. The fields below are the minimum I would put in the shared contract.

| Field | Content | Rule |
| --- | --- | --- |
| Case ID and type | Stable identifier; guest, partner, host or multi-party | Never reused across brands |
| Parties | Guest, property or host, co-hosts or staff acting for them, the marketplace | Each with a role; reads use the delegation model of [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) |
| Linked reservations | Original, modified, relocated and replacement reservation IDs | A relocated reservation links original and replacement |
| Contact driver | Taxonomy code and version; secondary drivers allowed | Set by classifier, confirmed or corrected by the agent |
| Arrival clock | Next deadline derived from the reservation: hours to check-in, cancellation deadline, check-out | Recomputed on every reservation event |
| Owner and queue | Current owner (team, vendor, AI assistant, partner) and escalation path | A case always has exactly one owner |
| Actions and decisions | Recovery decisions, messages sent, partner requests | Append-only |
| Outcome | Resolution code, reopen window, satisfaction score | Closed only with a resolution code |

The state machine is short. What matters is that "waiting for partner" is a state with its own clock, because the marketplace is often waiting for a hotel or host to act.

![Case states New, Triaged, With marketplace and With partner, where a missed partner deadline moves the case to the marketplace, both leading to Resolved, then Closed or Reopened back to the marketplace.](stays-marketplace-architecture/posts/25-customer-service/assets/images/25-customer-service/25-case-states.jpeg)

**Figure 3:** *A stays case. "With partner" is a state with its own deadline: when the property or host does not act before the arrival clock allows, the case moves back to the marketplace automatically, which is what should have happened at 11:20 on King's Day.*

{id: customer-service--service-levels-set-by-the-stay}
### Service levels set by the stay

Contact centers measure answer times. A stays marketplace should set its targets from the arrival clock and let the queue targets follow. The rule I use is a priority matrix from two inputs: how close the stay is and whether the guest can sleep tonight.

| Situation | Example | Target |
| --- | --- | --- |
| Guest at or near the property without a usable room | Walked guest, cannot get in, unsafe home | Human contact within 15 minutes; rehoused or solved within 2 hours |
| Arrival within 48 hours and the booking is at risk | Unacknowledged reservation, oversell detected, host canceled | Proactive contact within 1 hour; remedy before travel |
| Arrival within 14 days, money or dates at stake | Change request, waiver request, declined charge | Same business day |
| Everything else | Invoice copy, policy question, post-stay complaint | Self-service first; human reply within 24 hours |

Calendar Sync v2 at Nookaway already used this logic for calendar conflicts: a conflict found on import opens a case with a **60-minute** target to contact the affected guest ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)). The King's Day review applied the same logic to Roomstead.

{id: customer-service--recovery-decisioning}
## Recovery Decisioning

When a stay fails, support chooses a remedy. Usually that choice lives in agents' heads, vendor knowledge-base articles and approval e-mails. The **recovery decision** makes it data.

A recovery decision has six parts: the case and reservations it applies to; the **cause code** (what went wrong, from a short list shared with [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) and [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations)); the **entitlement** the guest, partner or host has under the applicable policy and rule version; the **remedy** chosen (refund, partial refund, relocation, credit, goodwill payment, fee waiver, host compensation); the **funder** who pays now; and the **liable party** who ultimately bears the cost and how it is recovered.

| Cause | Typical remedy | Funder now | Liable party | Recovery path |
| --- | --- | --- | --- | --- |
| Hotel oversell from its own or its channel manager's systems | Relocation to comparable or better, transport | Marketplace | Hotel, capped in partner terms | Line on the partner statement |
| Host cancels or double-booked home | Rebooking under the guest guarantee, price difference | Marketplace | Host, by fee; marketplace for the remainder | Host cancellation fee from next payout |
| Marketplace defect (duplicate charge, wrong price) | Refund, correction, goodwill credit | Marketplace | Marketplace | None; cost is an engineering signal |
| Guest changes plans on a non-refundable rate | Waiver request to property or host; otherwise none | Property or host if granted | — | None |
| Declared disruptive event | Refund or credit under the event's terms | Per event terms | Per event terms | Batch, per declared event |
| Payment fraud against the guest through a partner account | Reimbursement | Marketplace | Partner where terms allow; often marketplace | Partner claim; fraud loss accounting |

Three properties make the service useful rather than another approval form.

**Entitlements are rules, not scripts.** "A walked hotel guest is entitled to a comparable or better room within 5 kilometers or the nearest available, transport, and a refund of any prepaid amount" is a rule with a version, evaluated against the reservation and the cause. The same rule engine serves the AI assistant, the agent and a batch job. When the policy changes, one rule changes, not 40 vendor articles. The cancellation policy engine of [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) is the source for what the guest is owed under the booking's own terms; recovery decisioning adds what the marketplace grants on top.

**Limits are part of the decision, not of the org chart.** Each remedy has an approval limit by actor: the AI assistant, a first-line agent, a senior agent, a supervisor. A first-line agent at a vendor might approve goodwill up to €50 and relocations up to the entitlement; anything above goes to a queue with a named approver. Limits by actor make outsourced and automated support safe to give real authority.

**Every decision posts to the ledger.** A recovery decision emits an event that payments and finance consume: a refund instruction, a credit-account entry, a payable to the relocation hotel, a receivable from the liable partner. Finance can then answer "how much did we spend on relocations caused by connectivity partners in April, and how much did we recover?" from records rather than spreadsheets ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement), and in the finance book [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html)).

![A recovery decision card with rows for cause, entitlement, remedy, funder and liable party, paying the guest now, recovering from the hotel and posting to a ledger.](stays-marketplace-architecture/posts/25-customer-service/assets/images/25-customer-service/25-recovery-decision-anatomy.jpeg)

**Figure 4:** *A recovery decision records the cause, the entitlement, the remedy, who pays now and who bears the cost, and posts all of it to the ledger.*

{id: customer-service--king-s-day-replayed}
### King's Day, replayed

After the review, Corvane rebuilt the four relocations as they would run on the target design. The sequence below starts at the negative-headroom signal that [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity) added to Roomstead's inventory refresh.

![Swimlanes for inventory, case service, hotel, recovery, guest and ledger: a negative-headroom signal opens a case, the hotel confirms 4 reservations, recovery decisioning books linked replacements, the guests hear the evening before and the ledger records the receivable.](stays-marketplace-architecture/posts/25-customer-service/assets/images/25-customer-service/25-kings-day-replay.jpeg)

**Figure 5:** *King's Day on the target design. The guests hear the evening before, the replacement bookings are linked to the originals, and the recovery claim is posted with the decision instead of three days later by e-mail.*

The replay gave these numbers:

| Measure | 27 April 2027 as it happened | Replay on the target design |
| --- | --- | --- |
| First moment Roomstead acted | 13:05 on 27 April | about 19:15 on 26 April (case opened from the 19:01 signal) |
| Guests who learned at the front desk | 2 | 0 |
| Contacts | 11 | 5 (one outbound per guest, one hotel confirmation) |
| Agent time | about 6 h 40 min | about 50 min |
| Relocation cost | €2,150 | about €1,540 (rooms booked the evening before) |
| Recovered from the hotel | €1,600, by e-mail claim on 3 May | €1,540, posted with the decision (all four under the €400 cap) |
| Reporting | 4 guest cancellations, 4 unrelated new bookings | 4 relocated reservations with cause code and linked replacements |

The saving is small for four guests, but Roomstead relocated about **5,400** guests for oversold reservations in 2026 ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)), and the forum made the replay the template for all of them. The larger gains were no guest learning the news at a front desk, and the cost reaching the right statement automatically.

{id: customer-service--context-what-the-agent-must-see}
## Context: What the Agent Must See

An agent with the right context resolves in one contact what an agent without it resolves in three. The context read model should answer five questions without the agent opening another system:

1. **What did the guest buy, under which terms?** Reservation versions, the rate plan or listing terms, the cancellation policy and payment arrangement as they were at booking ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)), and the price lines the guest saw.
2. **Where is the money?** Payment plan, authorizations, captures, refunds, virtual-card status for merchant hotel bookings, and the host's payout status ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)).
3. **Does the property or host know?** Delivery and acknowledgement status, the confirmation number from the property management system (PMS), the last messages in the conversation ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)).
4. **What else is happening?** Partner connectivity health, open exceptions, declared events affecting the destination, recent cases on the same property or listing.
5. **What should I be careful about?** Trust and fraud flags, verified identity level, prior recovery decisions for the same guest, and the reason a field is hidden.

The last question leads to two constraints. **Least privilege applies to agents too.** An outsourced first-line agent rarely needs a guest's full payment details, a host's identity documents or the full address of a home before check-in. The context model should return fields by role and purpose, and log reads ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)). The November 2027 extranet phishing wave, where attackers used stolen partner credentials to message **4,100** Roomstead guests ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)), is a reminder that every support and partner channel is also an attack surface. **Social engineering targets support.** "I am the host, please change the payout account" or "I am the guest, please move the booking to my new e-mail" are classic takeover routes; sensitive changes need step-up verification that the agent cannot override.

Messages need a specific rule. When the platform translates guest–host messages automatically, as Airbnb has done for messages since 2022 ([Airbnb, via Hospitality Net, 2022](https://www.hospitalitynet.org/news/4112343.html)), the agent who judges a dispute must be able to see the original text, because the evidence is what was written, not the translation.

{id: customer-service--self-service-and-ai-agents}
## Self-Service and AI Agents

Self-service is the oldest deflection tool and still the most effective: a guest who can cancel a refundable booking in the app does not call. The newer tool is an AI agent that understands the guest's question, reads the booking and acts.

{id: customer-service--what-the-companies-have-documented}
### What the companies have documented

| Company and date | What was published | Evidence |
| --- | --- | --- |
| Airbnb, June 2025 | Voice support: domain-adapted speech recognition cut word error rate "from 33% to approximately 10%"; contact-reason detection under 50 ms; help-article retrieval; escalation with context | [Airbnb Tech, 2025](https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/) |
| Airbnb, Q2–Q3 2025 | AI customer-service agent expanded to all US users, "reducing the percentage of hosts and guests who needed to contact a human agent by 15%"; lets users "take common actions—like canceling or changing reservation dates—directly from the chat" | [Q2 2025 letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm), [Q3 2025 letter](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf) |
| Airbnb, Q2 2026 | Assistant in "more than 50 languages"; "Nearly 45% of issues that begin with our AI assistant are now resolved without a human agent"; customer-support cost per booking down about 16% year on year, "driven in part" by the assistant; an AI voice assistant to follow | [Airbnb Q2 2026 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm), August 2026 |
| Airbnb, 2026 | Evaluation practice for generative AI (GenAI) features including AI customer support: sample 5% of live de-identified traffic daily, run programmatic checks and model-based judges, send flagged outputs to human review | [Airbnb engineering blog, July 2026](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788) |
| Expedia Group, 2026 | More than 250 million service interactions a year, over half self-service, more than 30% AI-powered | [Hotel Dive, 2026](https://www.hoteldive.com/news/expedia-ai-enhance-customer-support-acquire-new-customers/819968/), secondary |
| Booking.com, October 2026 | AgentHub, a platform for modular large language model (LLM) agents including a "customer support chatbot"; interactions traced with OpenTelemetry, evaluated with LLM-as-judge, guarded against prompt injection and personal-data leakage | [booking.ai, 2026](https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50) |

One reported failure is as instructive. The figures above also measure different things ("resolved without a human agent" against "AI-powered interactions"), and nobody publishes how resolutions are verified. A 2026 secondary report says Expedia discontinued Romie, the AI travel assistant it launched in alpha in May 2024, and quotes its product chief on the difficulty of keeping traveler trust when chatbot answers were not grounded in accurate, real-time inventory and reservation data ([Let's Data Science, 2026](https://letsdatascience.com/news/expedia-group-shares-ai-chatbot-lessons-learned-239f348a)). The source is secondary and I treat it as low confidence, but the lesson matches the architecture: an assistant that cannot read the booking guesses.

{id: customer-service--design-rules-for-an-ai-support-agent}
### Design rules for an AI support agent

The public record describes outcomes, not internals, so the following is a reference design, not a description of any company's system.

1. **Ground answers in live state through tools.** The agent reads the case's context model, not a copy, and answers questions about a booking only from it. Policy questions are answered from curated, versioned content.
2. **Act only through the decision and domain APIs, within an actor limit.** Cancelling a refundable booking or resending a confirmation is a tool call with the AI assistant's own approval limits, the same idempotency and the same audit as a human agent's action. It cannot grant what a first-line agent could not.
3. **Use pre-approved answers where the law or money is involved.** Refund entitlements, consumer-law rights, safety instructions and anything a regulator may later read should come from templated, reviewed text with variables filled from the reservation, not from free generation.
4. **Hand off with the case, not a transcript.** Escalation passes the classified driver, the context and what the assistant already tried, so the human does not start again. Safety contacts go to humans at once.
5. **Disclose and log.** Under the EU Artificial Intelligence Act (Regulation (EU) 2024/1689), providers must ensure that AI systems intended to interact directly with natural persons inform them that they are interacting with an AI system unless that is obvious (Article 50); the regulation applies generally from 2 August 2026 ([Regulation (EU) 2024/1689](http://publications.europa.eu/resource/celex/32024R1689), 2024; check later amendments for the dates in force). What the assistant said is evidence in a later dispute, so keep it with the case.
6. **Evaluate continuously and measure resolution.** Sample live conversations daily, score them against policy and tone, and track reopen and repeat-contact rates per driver. Containment without resolution moves cost from the contact center to the next contact.

{id: customer-service--corvane-s-assistant-pilot}
### Corvane's assistant pilot

Corvane piloted an assistant on Roomstead's app chat in English from **September 2027**, limited to five drivers: resend a confirmation, send an invoice copy, cancel a booking inside its free-cancellation window, pass an arrival-time message to the property, and explain the cancellation terms of a booking. In its first six weeks the assistant resolved **38%** of in-scope conversations without an agent, and **4.1%** of those reopened within seven days, against 3.2% for agent-handled cases of the same drivers. Most reopenings had one cause: the assistant confirmed arrival-time messages before the property's PMS had acknowledged them. The fix was a tool change, not a prompt change: the tool now reports the message as pending until acknowledged.

Nookaway got no assistant in 2027. Its expensive drivers were disputes and failed check-ins, where the hard part is judgement and evidence, and Rafael Mendes, VP Engineering at Nookaway, argued that an assistant would first need recovery decisioning and the evidence store of [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents). The forum agreed.

{id: customer-service--when-everyone-calls-at-once-disruption-surges}
## When Everyone Calls at Once: Disruption Surges

Support capacity is planned for a normal week. Travel's worst weeks are not normal: strikes, storms, volcanic ash, pandemics and platform outages arrive as thousands of contacts about the same thing within hours. Airbnb applied its extenuating circumstances policy to COVID-19 cancellations in March 2020 and committed up to $250 million for affected hosts ([Airbnb Form 10-K FY2020](https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm), 2021); Booking Holdings reported that "increased cancellations, especially early in the pandemic, have resulted in increased customer service costs" ([Booking Holdings Form 10-K FY2020](https://www.sec.gov/Archives/edgar/data/1075531/000107553121000019/bkng-20201231.htm), 2021). Both are evidence from 2020; the policies have since changed. Airbnb's current Major Disruptive Events policy "applies only to the defined area and timeframe" ([Airbnb Help Center, article 1320](https://www.airbnb.com/help/article/1320), live page, 2026), which reads like a policy operated as data.

Corvane's test came with the **air-traffic-control strike over France on 5–7 June 2027**. About **17,000** Roomstead and **2,600** Nookaway reservations were affected, and Roomstead received **6,200** cancellation requests in 48 hours. A flight cancellation does not by itself entitle a hotel guest to a refund; for most bookings the question was whether the rate allowed free cancellation and, if not, whether the property would waive the fee. [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) tells the policy side; support saw this:

| Group | Requests | What happened in support |
| --- | --- | --- |
| Self-service cancellations | 2,950 | None: the app handled them |
| Free-cancellation guests who called anyway | 750 | The confirmation e-mail showed deadlines in Irish time and the app in property time, so guests thought they had missed them |
| Non-refundable or past the deadline | 2,500 | Agents applied a **support macro that waived penalties** on 1,860 reservations, without asking whether Roomstead held the money |

The macro was Policy Spaghetti in its purest form: a rule written in the case tool, outside the policy engine and the payment model. For 1,140 agency bookings the hotel, not Roomstead, held the guest's money; 610 properties charged the guests anyway, and Roomstead reimbursed **€167,900**. For 720 merchant bookings, 290 virtual cards had already been charged by hotels, and **€31,200** was never recovered. The voice queue's wait peaked at about **2 hours 40 minutes** on 5 June, partly because Roomstead's disruption e-mails shared a sending queue with a marketing campaign and arrived a median **3 hours 10 minutes** late ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)). Nookaway had its own surge two months later: on 7 August a faulty message filter hid check-in codes, and support took **1,870** check-in contacts in one day against about 450 on a normal Saturday.

The forum drew four requirements from these weekends:

- **A disruption mode** that a duty manager can switch on per event: a recorded IVR message and app banner naming the event, priority routing for guests with arrivals in the next 48 hours, and a pause on non-urgent queues.
- **Declared events as data, and overrides as typed decisions.** The event (cause, area, dates, booking cutoff, terms) is defined once in Clause, the group cancellation policy engine and disruption registry ([When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations)); the case service opens cases for affected reservations in bulk, and a support override is a typed recovery decision that knows who holds the money, never a macro.
- **Structured waiver requests.** Where Roomstead does not hold the money, a waiver is a partner request with a deadline (12 hours under Clause's disruption policy) in the partner's queue and API, answered once per reservation, not an e-mail. The response flows back into the case and, if granted, into a self-service cancellation for the guest.
- **Capacity that scales with the event.** Vendor contracts with surge clauses and an AI assistant that, during disruption mode, handles the "can I cancel for free?" driver with the event's terms.

{id: customer-service--measuring-quality-and-cost}
## Measuring Quality and Cost

The metric set has to serve three audiences: the contact center, which manages queues; the product teams, which own the defects behind drivers; and finance, which pays for recovery.

| Metric | Definition | Use | Trap |
| --- | --- | --- | --- |
| Contacts per stayed reservation, by driver | Contacts ÷ stayed reservations, per driver group and brand | The product backlog; compare brands and markets | Falls if contact channels are hidden |
| Cost per case | Total support cost ÷ cases | Budget and vendor management | Rises when easy cases move to self-service, which is good |
| Verified resolution rate | Cases with no repeat contact or reopening within 7 days ÷ cases closed | Primary outcome for humans and AI alike | Requires stable case linking across channels |
| Proactive share | Cases opened by events before the guest contacted ÷ cases for that driver | Measures detection, e.g. oversells and unacknowledged bookings | — |
| Arrival-clock attainment | Cases resolved before the stay deadline ÷ cases with an arrival clock | The service level that matters | Needs reliable deadlines from reservation data |
| Recovery spend and recovery rate | Recovery decisions by cause and funder; recovered ÷ recoverable | Finance and partner management | Only possible with recovery decisions as data |
| Guest satisfaction (CSAT) and partner satisfaction | Survey after case closure | Quality check | Survivor bias; low response from angry guests |

Support data also feeds other systems. Airbnb's Guest Favorites program, launched in November 2023, requires host cancellations plus "quality-related" customer-service issues below 1% on average ([Airbnb 2023 Winter Release](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/), 2023). At Corvane, the Roomstead reliability demotion in ranking reads relocation and partner-caused cancellation cases ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)). When a driver code decides a property's position or a host's badge, **the taxonomy becomes a governed data product**: versioned, with migrations, and with cause codes that keep a marketplace defect from being charged to a hotel ([Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation)).

{id: customer-service--trade-offs}
## Trade-offs

| Choice | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Where the case lives | In the bought contact-center or case tool | In a marketplace case service; the tool embeds it | Small marketplace, one brand, few integrations | Several brands or vendors, proactive cases, recovery money to track |
| Recovery authority | Agents decide within guidelines | Recovery-decision service with rules and limits | Low volume, experienced in-house agents | Outsourced or AI first line, many policies, partner recovery |
| One support platform or one per brand | Shared case, context and decisioning | Each brand builds its own | Brands share payments, identity and guests | Brands share nothing below the brand line |
| Sourcing | In-house agents | Outsourced vendors | Disputes, safety, high-value cases, specialist partner support | Routine, multilingual, follow-the-sun volume |
| AI assistant autonomy | Answers only; agents act | Acts through tools within limits | Before decisioning and context APIs exist | Once actions are idempotent, limited and audited |

For a group of Corvane's size I would take the right-hand column on the first three rows, mix sourcing, and move to tool-acting AI driver by driver. For a single-brand marketplace small enough that one team knows every policy, a good bought tool with deep integrations is cheaper and a case service is premature.

{id: customer-service--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| Typical counterpart | A hotel or property manager with staff, systems and a front desk | An individual host on a phone, or a co-host or manager |
| Dominant drivers | Cancellations, changes, payment model questions, missing bookings, special requests | Host not responding, check-in failures, not as described, disputes, damage and safety |
| Who acts | Often the property: waivers, relocations, changes go through the partner | Often the marketplace: it holds the money and can override the host's policy |
| Remedies | Relocation by the hotel or marketplace; refunds depend on rate and payment model | Rebooking under the guest guarantee; host fees and calendar blocks; damage claims |
| Integration for support | Partner exception queues, PMS acknowledgement, waiver and no-show APIs | Host app, messaging, smart-lock status, evidence uploads |
| Evidence | System records: delivery logs, rate terms, PMS confirmation | Messages, photos, check-in logs, statements from both parties |
| Failure modes | Booking not found at the desk; agent cannot reach the property; agency vs merchant confusion | Host unreachable at arrival; he-said-she-said disputes; safety cases handled as routine |

**What to share.** I would share the case service, the contact-driver taxonomy, the context read model, recovery decisioning, the relocation service and the AI assistant platform across both brands. The guest is often the same person, the money flows through the same payments institution and ledger, and the cause codes feed group-level metrics and ranking. I would keep separate the **playbooks and skills**: a Roomstead agent handling a hotel waiver and a Nookaway agent mediating a damage dispute need different training, different queues and different approval limits, configured on the same platform. Nookaway's dispute and safety work stays in-house; Roomstead's routine volume stays with vendors.

{id: customer-service--failure-modes}
## Failure Modes

**The ticket that forgets the reservation.** Cases keyed by a guest's e-mail cannot be joined to cancellations, relocations or payouts.

**Recovery as a side effect.** Agents book replacement rooms on a company card or issue refunds outside the payments service. The money moves; the record does not. Finance meets it months later as an unreconciled amount ([Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation)).

**Waiting for the partner without a clock.** A case marked "waiting for hotel" has no deadline, so it waits until the guest arrives.

**Containment theater.** An AI assistant or IVR that ends conversations without solving them improves the deflection chart and raises repeat contacts, chargebacks and negative reviews. Without a verified-resolution metric nobody notices.

**Ungrounded AI.** An assistant answering from help articles tells a guest they can cancel free when their rate does not allow it; the marketplace then honors the promise or argues with a guest who has a transcript.

**The support channel as an attack path.** Account and payout changes made by an agent on the strength of a convincing story. Attackers learn which vendor sites are easiest to persuade.

**Surge without a switch.** No disruption mode, no declared events, no bulk actions: every strike is handled one call at a time while the queue grows.

**Taxonomy drift.** Each vendor adds its own reason codes. After two years, "booking issue – other" is the largest driver, and ranking signals built on support data mean nothing.

{id: customer-service--the-chief-architect-s-view}
## The Chief Architect's View

Mariana Costa, Group Chief Architect, took Elena's question to the One Stay forum in June 2027. The forum approved **Harbor**, the group support platform, with five decisions. They generalize.

**1. Own the case, the context and the decision; buy the channels.** Harbor is a marketplace service on AWS with the case service, the context read model, recovery decisioning and the relocation service. Roomstead's commercial case tool stays as the agent desktop for its two vendors, embedding Harbor's views; Nookaway's Burrow case tool is replaced by the same desktop by the third quarter of 2028. Owner: Elena Petrova for the product; a support platform engineering team in Lisbon for the code.

**2. One contact-driver taxonomy, under change control.** Version 1 has 64 drivers in 11 groups, shared by both brands, the vendors and the AI assistant. Changes need support operations, the affected product owner and the data platform, because ranking and quality programs read it. Owner: Elena; reviewer: Jonas Weber for ranking consumers.

**3. Every remedy is a recovery decision posted to Fathom.** Fathom, the double-entry ledger of Corvane Payments, receives refunds, relocation payables, credits and recovery receivables from the decision service. Approval limits by actor are set jointly by customer service and finance. Owner: Elena with Leila Haddad's payments and finance engineering team; Marco Bellini, Group CFO, signs the limits. The first mass run came in November 2027, when the reimbursement of **310** guests who paid fraudsters during the extranet phishing wave, **€212,000** in total, went through recovery decisions with cause code "partner account compromise" rather than as individual refunds ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)).

**4. Proactive cases from domain events.** Reservation acknowledgement, inventory headroom, payment-plan state, calendar conflicts and host cancellations open cases with an arrival clock. The domains own the events; Harbor owns the rules that turn them into cases. Target: half of Roomstead's oversell cases opened before the guest contacts by the end of 2028.

**5. AI per driver, with a gate.** A driver moves to tool-acting AI only when its decision rules exist, its actions are idempotent, its verified resolution rate in a pilot is within one point of human handling, and regulatory affairs (Noor van Dijk's team) has approved its templated answers. Owner: Elena with Kenji Arai's data and ML platform for evaluation ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)).

What to watch: cost per case will rise as routine contacts move to self-service, and someone will propose cutting the in-house dispute team because the average looks expensive. Judge support by contacts per stayed reservation and verified resolution instead. And a vendor paid per contact is paid for the problem, not the resolution.

{id: customer-service--questions-to-ask}
## Questions to Ask

1. What are our top ten contact drivers per stayed reservation, by brand and market, and which product team owns each?
2. Is the unit we manage a contact or a case, and can we link every case to the reservations it concerns?
3. Which cases do our own systems open before the guest calls, and what share of oversells and unacknowledged bookings do we catch that way?
4. Where are our refund, relocation and compensation rules written today, and how many places would change if a policy changed tomorrow?
5. Who funds each remedy, who is liable, and can finance see recoveries owed by partners and hosts as ledger entries?
6. What can an outsourced first-line agent see and do, and what stops them from changing a payout account on a convincing call?
7. Does our AI assistant read live reservation state and act through the same APIs and limits as agents, and how do we measure that its resolutions stay resolved?
8. Can we declare a disruptive event, find every affected reservation and apply its terms in bulk within an hour?
9. Which ranking, quality or partner-terms decisions read support data, and is the taxonomy they read versioned?
10. Are our vendors paid per contact, per case or per resolution?

Customer service is where the booking path meets the money path: nearly every recovery decision is a refund, a payable or a receivable. [Part VI — MONEY: Who Pays Whom, When and How Much](#part-6) follows that money, starting with the question that decides who holds it in the first place: [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models).

{id: customer-service--sources-and-evidence}
## Sources and Evidence

{id: customer-service--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm) — Airbnb, Inc., 2026. Support largely performed by third-party providers; AirCover for guests; AI in support and case management.
- [Form 10-K FY2020](https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm) — Airbnb, Inc., 2021. About 7,570 third-party partners across 24 sites; COVID-19 extenuating-circumstances application and host funds.
- [Q2 2025 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm) — Airbnb, Inc., 2025. AI agent to all US users; 15% fewer contacts needing a human.
- [Q3 2025 Shareholder Letter](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf) — Airbnb, Inc., 2025. Actions from chat; cancellation-policy options reducing cases.
- [Q2 2026 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm) — Airbnb, Inc., 2026. Assistant in 50+ languages; nearly 45% resolved without a human; support cost per booking down about 16%.
- [Listening, Learning, and Helping at Scale: How Machine Learning Transforms Airbnb's Voice Support Experience](https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/) — Airbnb Tech, 2025. Conversational IVR, contact-reason detection, retrieval, escalation.
- [Eval-driven development: Lessons from evaluating GenAI at scale](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788) — Airbnb Engineering, 2026. Daily sampling and judging of live GenAI traffic.
- [Airbnb 2023 Winter Release](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/) — Airbnb Newsroom, 2023. Guest Favorites and its quality inputs.
- [Translation Engine launches Reviews after expanding to Messages](https://www.hospitalitynet.org/news/4112343.html) — Airbnb via Hospitality Net, 2022. Automatic message translation.
- [Major Disruptive Events Policy](https://www.airbnb.com/help/article/1320) — Airbnb Help Center, n.d. (live page, 2026). Event scoped to a defined area and timeframe.
- [Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm) — Booking Holdings Inc., 2026. Outsourced customer service as a risk; GenAI improving resolution times.
- [Form 10-K FY2020](https://www.sec.gov/Archives/edgar/data/1075531/000107553121000019/bkng-20201231.htm) — Booking Holdings Inc., 2021. Pandemic cancellations raising customer-service costs.
- [Introducing AgentHub](https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50) — Booking.com, 2026. Agent platform including a customer-support chatbot, tracing and evaluation.

{id: customer-service--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](http://publications.europa.eu/resource/celex/32024R1689) — European Parliament and Council, 2024. Article 50 transparency for AI systems interacting with people; general application from 2 August 2026.

{id: customer-service--research-and-practitioner-sources}
### Research and practitioner sources

- [Report on Expedia Group's AI customer support (Q1 2026 earnings call)](https://www.hoteldive.com/news/expedia-ai-enhance-customer-support-acquire-new-customers/819968/) — Hotel Dive, 2026. Secondary report of Expedia's 250 million interactions and AI share.
- [Expedia Group shares AI chatbot lessons learned](https://letsdatascience.com/news/expedia-group-shares-ai-chatbot-lessons-learned-239f348a) — Let's Data Science, 2026. Secondary, low-confidence report on Romie's discontinuation and grounding.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
