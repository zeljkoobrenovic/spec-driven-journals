{id: protection-and-incidents}
# 35. Damage, Parties and Emergencies: Protection and Incident Response

![Damage, Parties and Emergencies: Protection and Incident Response — logo](stays-marketplace-architecture/posts/35-protection-and-incidents/assets/images/35-protection-and-incidents/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Design the protection domain of a stays marketplace: the guest guarantee, host damage protection and liability insurance, deposits, reservation screening and party prevention, the in-stay incident workflow, emergency response, and the damage-claim workflow with its evidence, fraud checks and money. You will see how a protection policy becomes product rules that every part of the platform reads the same way.

> **WHY THE BUSINESS CARES:** For a host deciding whether to rent out a home, protection is a precondition, not a feature: one bad weekend can cost more than a season's earnings. For the guest, the guarantee is what makes booking a stranger's home a reasonable bet. For the CFO, protection is a growing cost line with an insurer behind it, and every unrecovered claim and unexplained goodwill payment comes out of margin.

> **WHY ARCHITECTS SHOULD CARE:** Protection touches the booking path (screening must decide in milliseconds), operations (incidents happen at midnight in someone's home), payments (charging a guest after check-out, paying a host, recovering from an insurer) and machine learning (a screening model whose labels arrive weeks later from claims). Built as separate tools, it produces three case numbers for one party and a model nobody can evaluate. Built as one domain on the reservation, it can learn from each incident.

> **KEY POINTS:**
>
> * **Protection is one lifecycle on the reservation, not three tools.** Screening before booking, the incident during the stay and the claim after it are the same story about the same reservation. Give them one incident record, one evidence store and one timeline, so that what happened on Saturday night is visible to the adjuster on Thursday and to the screening model next month.
> * **Write protection policy once, as versioned data, and stamp its version on the reservation.** Eligibility, limits, filing windows, evidence rules, depreciation and recovery belong in one policy that the listing page, checkout, support tools, claims adjudication and screening all read. Every claim is then judged by the terms the guest and host saw when they booked.
> * **Protection is money with owners, so it needs a ledger and an insurer contract.** Guarantee rebookings, claim payments, guest recoveries and insurer reimbursements are obligations between named parties. Post them to the ledger as they happen rather than booking them as goodwill adjustments. Decide explicitly which losses the platform keeps and which it passes to the insurer.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Trust After the Incident** — Nookaway's screening, safety contacts and damage claims were three tools added after three different headlines, and the Dubrovnik party produced three unconnected cases.
> * **The Unwatched Model** — The screening model allowed the Dubrovnik booking with a missing distance signal and a holiday calendar that did not know Croatia, and nobody measured its misses against claims.
> * **Ledgerless Money** — Claim payments were posted as goodwill adjustments in Burrow's payout tables, so the cost of protection, recoveries from guests and the insurer's share could not be reconciled.

A stays marketplace sells a promise that a stranger will fulfill. Most of the time the promise holds. Sometimes the guest arrives to a locked door. Sometimes a booking for "six adults, quiet weekend" turns into forty people around a pool. Sometimes a wildfire closes a coast with guests still in their rentals. **Protection** is everything the marketplace does to make those failures survivable for the guest, the host and the business: the guarantees it offers, the screening it runs before it confirms a booking, the response it organizes while the stay is happening and the claims it settles afterwards.

On an accommodation marketplace much of this belongs to the hotel. The hotel has staff, a front desk, its own insurance and a legal duty of care, and the marketplace steps in mainly when the room does not exist or a guest must be relocated. On a hosted-stays marketplace **the platform takes on part of the role that a hotel's front desk and insurer play**: it decides who may book an entire home, it receives the neighbor's complaint at midnight, and it pays the host when the guest will not. That is why protection is a hosted-stays domain first, and why accommodation marketplaces are borrowing it for their homes and apartments.

This chapter owns **damage protection**, **reservation screening** and the **incident workflow**. It builds on the trust platform of [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) and leaves payment fraud to [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), oversell relocation to [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity), extenuating circumstances to [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations) and the support case model to [When Something Goes Wrong: Customer Service and Recovery](#customer-service).

{id: protection-and-incidents--setting-the-scene-at-corvane-forty-guests-in-a-four-bedroom-villa}
## Setting the Scene at Corvane: Forty Guests in a Four-Bedroom Villa

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs **Nookaway**, its hosted-stays marketplace, with a protection program called **Nookaway Cover**. Cover promises hosts damage protection up to **€500,000** and liability insurance up to **€1 million** through an insurance partner, and promises guests that Nookaway will rebook or refund them if check-in fails or the home is materially not as described. Under the terms in force in 2027, Nookaway paid each damage claim up to **€10,000** from its own protection budget, and the insurance partner paid the part of any claim above that amount. The liability cover was fully insured.

Ivan Horvat rents out a four-bedroom villa with a pool near Dubrovnik. His house rules say eight guests at most and no parties. On Wednesday **11 August 2027** at 22:47, a guest account created nineteen days earlier booked the villa by instant book for three nights, Friday 13 to Monday 16 August, the long weekend of the Assumption holiday on 15 August, a public holiday in Croatia. The booking declared six adults. Nookaway's reservation screening scored it **0.61**. Croatia used the global thresholds: below 0.45 allow, 0.45–0.70 require the guest to accept the party rule, above 0.70 block entire homes. The guest ticked the box.

On Saturday **14 August** at 23:20, Ivan's outdoor noise sensor, a decibel-only device he had disclosed on the listing, alerted his phone. At 23:41 a neighbor called him. At 23:48 he reported "party in progress" in the Nookaway host app. The report became a general support case, category "guest behavior", with a four-hour response target. The neighbor had no way to reach Nookaway at all. A Nookaway safety agent first saw the case at **00:58**, after the police had already come and gone. The party ended at about 01:30, and Nookaway's agent ended the stay the next morning under the party rule.

![A villa party at night above a timeline from a sensor alert at 23:20 to a support agent first seeing the case at 00:58, with a long ticket queue in between.](stays-marketplace-architecture/posts/35-protection-and-incidents/assets/images/35-protection-and-incidents/35-dubrovnik-night.jpeg)

**Figure 1:** *On the Dubrovnik night the host reported the party at 23:48, but the report waited in a general support queue, and a safety agent first saw it at 00:58, after the police had come and gone.*

On 15 August Ivan filed a Cover claim for **€3,800**. After evidence review Cover reimbursed **€3,450**, and Nookaway recovered **€900** from the guest. Sofia Marín, Director of Trust and Safety, ran the post-incident review in September, and what she found was not a single failure but a design:

- The screening decision, the support case and the Cover claim had **three identifiers in three tools**. The adjuster read about the police visit in Ivan's claim text, not in any record.
- The screening model had computed **distance to the listing** from the guest's account country, so every domestic booking had a missing distance value. Its **holiday calendar** covered New Year's Eve and a dozen Portuguese and Spanish dates, and nothing in Croatia.
- Nobody had ever compared the model's scores with later party reports or claims. The model had no named owner after its 2025 author moved teams.
- The €3,450 was paid as a **goodwill adjustment** in Burrow's payout tables, and the €900 recovery arrived through a payment link in a support email. Neither the protection budget, nor the insurer's share, nor the recovery rate could be read from a ledger.

Mariana Costa, the Group Chief Architect, put the question to the architecture forum on **21 September 2027**: **"What would it take for the next party to be one case, one ledger entry and one training label, and for Roomstead's homes to get the same protection without copying Nookaway's tools?"**

{id: protection-and-incidents--concepts-guarantees-protection-insurance-and-screening}
## Concepts: Guarantees, Protection, Insurance and Screening

The words in this domain are close together and mean different things legally and financially.

- **Guest guarantee.** The marketplace's promise to the guest that if the stay cannot happen as booked (host cancellation, failed check-in, a home materially not as described), it will find comparable accommodation or refund. It is a platform obligation, funded by the platform and sometimes recovered from the host.
- **Host damage protection.** The marketplace's promise to reimburse a host for damage a guest caused and did not pay for, within limits. It may be a contractual promise funded by the platform rather than insurance. Airbnb says of its program: "Host damage protection isn't insurance and isn't related to Host liability insurance" ([Airbnb, How AirCover for Hosts works](https://www.airbnb.com/resources/hosting-homes/a/how-aircover-for-hosts-works-469), 2026).
- **Liability insurance.** An insurance policy that pays third parties, such as an injured guest, a neighbor or a building owner, when the host is legally liable. It is underwritten by a licensed insurer or a captive, and claims are often handled by a **claims administrator**.
- **Security deposit.** Money taken from the guest before or during the stay and released afterwards. It may be a card pre-authorization, a collected payment or, in the softer form, a **post-stay charge** the guest agreed to at checkout. [Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) owns its payment mechanics.
- **Retention.** The part of each loss the platform pays itself before insurance responds. Corvane's €10,000 per damage claim is a retention.
- **Recovery** and **subrogation.** Recovery is collecting from the party who caused the loss, usually the guest. Subrogation is the insurer's right, after paying, to recover in the insured's place.
- **Reservation screening.** A risk decision about a proposed reservation, made before it is confirmed, about **physical and behavioral risk**: parties, damage, unsafe use. It is different from the **booking risk score** of [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), which is about whether the payment and the account are genuine.
- **Incident.** A reported or detected event during or around a stay that threatens a person's safety, a property or the neighbors: a party, an injury, an intrusion, a fire, a lockout at night. An **incident workflow** is the intake, triage, response and closure of incidents as records linked to the reservation.
- **Claim.** A request for money under a protection program, with evidence, a decision and a payment. One incident may lead to several claims (a host's damage, a neighbor's liability claim), and many claims have no incident at all (a stain found at turnover).

The distinction that matters most for architecture is **who carries which loss**: the platform up to the retention and for the guarantee, the insurer above it and for liability, the guest through recovery. If all three are booked as "goodwill", nobody can manage any of them.

![A two-layer tower of coins: platform retention up to a dashed line at 10,000 euros, the insurer above it, and a green arrow of guest recovery returning coins to the platform layer.](stays-marketplace-architecture/posts/35-protection-and-incidents/assets/images/35-protection-and-incidents/35-who-carries-loss.jpeg)

**Figure 2:** *Who carries which loss: Nookaway pays each damage claim up to its €10,000 retention, the insurer pays above it, and recovery from the guest returns part of the platform's share.*

{id: protection-and-incidents--architecture-one-protection-lifecycle-on-the-reservation}
## Architecture: One Protection Lifecycle on the Reservation

I organize protection around the reservation's timeline: **before** the booking is confirmed, **during** the stay and **after** check-out, with money and learning as two loops underneath.

![Booking request, screened, becomes a reservation; the stay may produce an incident and then a claim, whose payments go to the protection ledger; incident and claim outcomes return as labels to the screening model, which sets thresholds for the next booking.](stays-marketplace-architecture/posts/35-protection-and-incidents/assets/images/35-protection-and-incidents/35-protection-lifecycle.jpeg)

**Figure 3:** *The protection lifecycle. Screening, incidents and claims belong to one reservation's story. Money flows into the ledger, and outcomes flow back as labels that tune the next screening decision. Cut either loop and the program stops learning.*

The components below are a reference architecture. Corvane built it after the Dubrovnik review. No company has published its own design at this level of detail.

![A policy registry feeds screening, incidents and claims; all three write to the reservation record; incidents and claims share an evidence store; claims post to the protection ledger, which reports to the insurance partner.](stays-marketplace-architecture/posts/35-protection-and-incidents/assets/images/35-protection-and-incidents/35-protection-components.jpeg)

**Figure 4:** *Protection components. One policy registry feeds screening, incidents and claims; all three write to the reservation record and one evidence store; the claims workflow is the only component that moves money, and it does so through the protection ledger.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Protection policy registry** | Versioned terms: eligibility, limits, windows, evidence rules, depreciation, recovery, screening thresholds and actions per market and listing type | Policy versions and their effective dates | Live in code paths of checkout, support tools or the claims UI |
| **Reservation screening** | Score a proposed reservation and choose an action from the policy | Decisions with reasons, model and policy versions | Block without a reason code, or decide payment fraud ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)) |
| **Incident workflow** | Intake from guests, hosts, neighbors, devices and staff; triage by severity; response; closure | Incident record, severity, timeline, actions | Wait for a support queue when life safety is at stake |
| **Claims workflow** | Filing, evidence, counterparty response, adjudication, payment, recovery, insurer referral | Claim record, line items, decisions | Pay outside the ledger |
| **Evidence store** | Photos, invoices, messages, device events, police references, with retention rules | Evidence objects, hashes, access log | Be readable by everyone who can read a support case |
| **Protection ledger accounts** | Guarantee expense, claim payables, guest receivables, insurer recoverables, reserves | Postings (in the group ledger) | Be a separate spreadsheet |
| **Insurer interface** | Notifications of large losses, monthly bordereau, recoveries | Contract terms, referral thresholds | Leak personal data beyond what the contract requires |

Three interface choices carry most of the design.

1. **The reservation carries the protection terms version.** At confirmation the reservation records which protection policy version applies, which screening decision was taken and which guest commitments were accepted (the party rule, consent to post-stay charges). Every later decision reads these, not the current terms.
2. **Incidents and claims reference each other and the reservation.** A claim can exist without an incident, but if there was one, the claim adjudicator sees its timeline. A screening decision is joined to both when labels are built.
3. **Money only moves through the ledger.** A guarantee rebooking, a claim payment and a guest recovery are postings with a reason and a policy version, made in the group ledger described in [Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement). The payment rails execute what the ledger records.

{id: protection-and-incidents--protection-policy-becomes-product-rules}
### Protection policy becomes product rules

The same protection terms appear in at least six places: the listing page, checkout, the host's tools, the support agent's screen, the adjudicator's rules and the screening policy. When each encodes its own copy, the platform makes promises the adjuster then refuses to honor, which is the protection version of Policy Spaghetti.

| Policy element | Example in Nookaway Cover (2027) | Read by |
| --- | --- | --- |
| Eligibility | Listings with verified hosts in Nookaway's 31 countries; excludes wear and tear, cash, and losses the host caused | Listing page, claim intake |
| Limits | €500,000 damage per stay; €1 million liability per occurrence | Listing page, adjudication, insurer referral |
| Windows | Host files within 14 days of check-out; guest responds within 72 hours | Host app, claim state machine |
| Evidence | Dated photos or video, invoice or quote, pre-stay condition where available | Claim intake, adjudication |
| Depreciation | Furniture loses 10% a year down to a 30% floor | Adjudication |
| Recovery | Post-stay charge on the stored credential if the guest agreed at checkout | Payment orchestration |
| Screening | Thresholds and actions per market, listing type and calendar | Screening service |

{id: protection-and-incidents--reservation-screening-deciding-who-may-book-an-entire-home}
## Reservation Screening: Deciding Who May Book an Entire Home

**Reservation screening** is the pre-confirmation decision about whether this guest, for this home, on these dates, is likely to cause a party, damage or a safety incident, and what to do about it. On a hosted-stays marketplace it is the cheapest point of control, because after confirmation the platform has only expensive options: canceling a confirmed guest, sending someone at midnight or paying a claim.

{id: protection-and-incidents--what-is-documented}
### What is documented

Airbnb has published more about screening than any other platform, all of it in newsroom posts rather than engineering papers. It introduced a party ban in August 2020, "which we then codified in 2022" ([Airbnb Newsroom, 2023](https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior)). In 2022 it described anti-party technology in the United States and Canada that looks at signals including the guest's "history of positive reviews (or lack of positive reviews)", how long the guest has been on Airbnb, trip length, the distance between the guest and the listing, and weekend versus weekday. Flagged guests could still book a private room or a hotel room, and a pilot in Australia had led to "a 35 percent drop in incidents of unauthorized parties" ([Airbnb Newsroom, 2022](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada)). A 2021 post described a separate rule that blocked some last-minute entire-home bookings ([Airbnb Newsroom, 2021](https://news.airbnb.com/building-on-our-commitment-to-trust-2)).

In its 2023 update Airbnb reported a 55% drop in the rate of party reports compared with two years earlier, and that in 2022 "just 0.039 percent of global reservations resulted in an allegation of a party"; about 0.02% of reservations led to damage reimbursement of US$1,000 or more. It also described a neighborhood support line, a 24-hour safety line and free noise sensors for hosts in more than 60 countries ([Airbnb Newsroom, 2023](https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior)). For the July 4 weekend of 2025 it said more than 20,000 people in the United States were redirected from booking entire homes ([Airbnb Newsroom, 2026](https://news.airbnb.com/airbnbs-anti-party-system-returns-for-july-4-weekend)). These are the company's own figures. The model type, features beyond the published list, thresholds and latency are not public.

Two documented design choices are worth copying regardless of the model. **The action set is larger than allow or deny**: redirecting to a private room or hotel keeps a legitimate guest in the marketplace. And **risk is seasonal**: holiday modes tighten policy on known dates.

{id: protection-and-incidents--a-reference-design}
### A reference design

> **INFERENCE, NOT DOCUMENTED:** The following is a plausible reference design for a screening service, derived from the public descriptions above and from general risk-decisioning practice. It is not a description of Airbnb's systems.

The screening service is called synchronously by checkout after the offer is priced and before the reservation is confirmed ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)), and also when a request-to-book reaches the host. It must answer within a small budget (Corvane's Warden booking gate allows 120 milliseconds and fails open into post-booking review), because it sits on the conversion path. It reads three kinds of input:

- **Reservation features**: listing type, capacity and declared party size, nights, arrival day of week, lead time, local calendar (holidays, festivals, school-leaver weeks), price relative to the listing's norm.
- **Guest features**: account age, verified identity level ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)), completed stays and reviews as a guest, prior incidents, distance from the guest's home to the listing, links to other accounts via the identity graph.
- **Listing context**: the host's settings, prior incidents at the listing, the neighborhood's complaint history, the protection exposure (a €2 million villa justifies a lower threshold than a studio).

The output is a **decision with reasons**: a score, the policy version, the action and the top contributing factors. The action comes from the policy, not from the model.

| Action | What happens | When it fits |
| --- | --- | --- |
| **Allow** | Booking proceeds | Low score |
| **Attest** | Guest explicitly accepts the party and occupancy rules | Moderate score; mostly a deterrent and an evidence record |
| **Step up** | Guest must verify a documented identity before confirmation | Thin account history |
| **Convert** | Instant book becomes request-to-book; host sees the guest's history | Moderate score on a high-value home |
| **Redirect** | Entire homes unavailable for this stay; rooms and hotels shown instead | High score, especially on peak dates |
| **Block** | No booking; review route offered | Very high score or prior serious incidents |

{id: protection-and-incidents--fairness-explanation-and-the-right-to-contest}
### Fairness, explanation and the right to contest

Screening decides who may book a home on the basis of a profile, which carries two risks. The first is discrimination. A feature such as distance or age can act as a proxy for protected characteristics, and Airbnb's Project Lighthouse work shows how a platform can measure outcome gaps between groups without linking perceived race to individual accounts ([Airbnb, 2020](https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf)). The second is legal. Under GDPR Article 22, a person has the right "not to be subject to a decision based solely on automated processing, including profiling, which produces legal effects concerning him or her or similarly significantly affects him or her". Where the contract exception applies, the controller must still provide suitable safeguards, at least human intervention, the chance to express a view and to contest the decision ([Regulation (EU) 2016/679](http://publications.europa.eu/resource/celex/32016R0679), 2016).

Whether a redirect "similarly significantly affects" a guest is a question for counsel ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)); the architecture should not wait for the answer. Every non-allow decision should carry reason codes, a route to human review and a log that a fairness analysis can join to outcomes. I prefer the redirect for this reason: it reduces risk and still lets the guest book.

{id: protection-and-incidents--labels-arrive-late}
### Labels arrive late

A party report arrives within hours, an adjudicated claim within a month, and redirected bookings produce no label at all. A screening model therefore needs a **holdout** (a small share of moderate-risk bookings given a lighter action, so that misses can be measured), labels built from incident and claim records rather than support-case categories, and a named owner who reviews precision and recall per market and season, the discipline [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) describes.

{id: protection-and-incidents--the-incident-workflow-the-night-something-goes-wrong}
## The Incident Workflow: The Night Something Goes Wrong

An incident on a hosted-stays marketplace has no front desk. The first person to know may be a neighbor, the host 300 kilometers away, a noise sensor or the guest locked out at midnight. The platform's job is to **receive every signal into one record, triage it by danger to people, act within a time that matches the danger, and leave a timeline that the claim, the review and the screening model can all use.**

{id: protection-and-incidents--intake-and-triage}
### Intake and triage

Intake channels are many: the guest's safety line in the app, the host app, a neighbor contact page or phone line, messages flagged by [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging) safety scanning, device events from host-connected sensors, and reports from police or city officials. Each creates or updates an **incident** linked to the reservation, deduplicated by listing and time window so that a neighbor's call and the host's report become one record.

| Severity | Examples | First action | Target time to human contact |
| --- | --- | --- | --- |
| **S1 Life safety** | Injury, fire, gas, violence, a guest in danger | Direct to emergency services; safety team calls the reporter | Immediate; seconds to connect |
| **S2 Active harm** | Party in progress, intrusion, hidden device found, guest locked out at night | Safety team contacts guest and host; may end the stay | 15 minutes |
| **S3 Stay at risk** | Home not as described, missing amenities, no access by day | Guest guarantee path: fix, rebook or refund | 1 hour |
| **S4 After the fact** | Damage found at turnover, rule breaches found later | Claim path; review and enforcement | Next business day |

Two rules follow from S1. The platform must never stand between a person and emergency services: the app shows the local emergency number first and the platform's own line second. And the safety team needs the **reservation context at once**: who is staying, how many, contact numbers, the address and access instructions. Airbnb lists "an urgent safety line" and a "24/7 neighborhood support line" among its trust measures ([Airbnb Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026). How it routes them is not public.

{id: protection-and-incidents--response-actions-and-their-side-effects}
### Response actions and their side effects

Incident responses change other domains, and each change goes through that domain's interface:

- **End the stay** for a rule breach: a reservation transition owned by [The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle), with the refund consequence set by the protection policy, not by the agent.
- **Rebook the guest** when the home is unsafe or inaccessible: a linked replacement reservation, as in the guarantee path, using the relocation service of [Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity).
- **Restrict the guest or host account**: an enforcement action through the trust platform of [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety), with a statement of reasons where the DSA requires one.
- **Hold the host's payout** when a guest guarantee case may be charged back to the host: a hold on the balance in the settlement ledger ([Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement)).
- **Preserve evidence**: messages, device events and call notes copied into the evidence store before normal retention deletes them.

{id: protection-and-incidents--device-signals-and-privacy}
### Device signals and privacy

Noise sensors and smart locks give the platform signals no hotel OTA has, and they are also surveillance inside someone's temporary home. Airbnb reportedly banned indoor security cameras in all listings from 30 April 2024 while allowing disclosed outdoor devices ([ABC7, 2024](https://abc7news.com/airbnb-bans-the-use-of-indoor-security-cameras-on-all-properties/14516158/), a press report). **Device policy is therefore structured listing data** (type, indoor or outdoor, what it measures, disclosed or not), and the incident workflow accepts signals only from disclosed devices that measure levels, never content.

{id: protection-and-incidents--emergencies-at-destination-scale}
### Emergencies at destination scale

A wildfire or a flood creates hundreds of incidents at once. The Productscape reference model used for this book (a generic model, not a description of any company) tests exactly that stressor, a wildfire that makes "an entire destination unsafe during active stays", and concludes that the platform must represent a **destination operating state** separately from each listing and booking, with "geography, time, severity, affected trip phases, communication, safety actions, relocation eligibility, payment treatment, and evidence".

That **declared event** is shared with [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations), which owns how it changes cancellation and refund terms (at Corvane, the disruption registry of the Clause policy engine). This chapter owns the safety operation: an **active-stay roster** (who is in the zone now, who arrives in the next 72 hours), outreach in the guest's language, relocation where needed and welfare follow-up. A hotel knows who is in-house; a hosted-stays marketplace often does not know whether the guest has arrived, which is the reason to record arrival as a reservation fact.

{id: protection-and-incidents--the-claims-workflow-from-evidence-to-money}
## The Claims Workflow: From Evidence to Money

A damage claim is a small dispute between two private parties, adjudicated by the platform under its own terms, and paid partly with the platform's money and partly with an insurer's. The workflow should make every step explicit.

![Claim states: Filed, then Guest response, which leads to Accepted or Under review; review may go to the insurer before Decided; Decided leads to Paid to host, then Recovery; an accepted claim goes straight to Recovery.](stays-marketplace-architecture/posts/35-protection-and-incidents/assets/images/35-protection-and-incidents/35-claim-states.jpeg)

**Figure 5:** *The life of a damage claim. The guest's response window comes first, because a claim the guest accepts needs no adjudication. Payment to the host and recovery from the guest are separate states, so that a host is not kept waiting while the platform collects.*

{id: protection-and-incidents--filing-response-and-evidence}
### Filing, response and evidence

Documented programs share a shape. Airbnb lets a host involve Airbnb if a guest does not respond to or pay a damage reimbursement request within 24 hours ([Airbnb, How AirCover for Hosts works](https://www.airbnb.com/resources/hosting-homes/a/how-aircover-for-hosts-works-469), 2026), and its terms provide that amounts may be charged to the payment method of the booking ([Airbnb Terms of Service](https://www.airbnb.com/help/article/2908), 2026). Booking.com's terms say it "won't be involved in any financial settlement related to damage deposits", but a property can submit a damage payment request through the platform within 14 days, which Booking.com then arranges to charge ([Booking.com Terms](https://www.booking.com/content/terms.html), updated 25 August 2025). Expedia's Rapid API supports refundable damage deposits on vacation rentals as an option ([Expedia Group Developer Hub](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/about-vacation-rentals-api), n.d.).

**Evidence** is what makes a claim decidable. Useful evidence is dated and comparable: a turnover photo before the stay and the same view after, an invoice or quote, device events, the incident timeline and the guest's messages. The evidence store should keep a content hash and capture time for every object, and should restrict access to the people working the claim. Photos of a home's interior and of guests are personal data.

{id: protection-and-incidents--adjudication-and-claims-fraud}
### Adjudication and claims fraud

Adjudication applies the policy version on the reservation: is the item covered, is the amount supported, what depreciation applies, is any of it the host's own responsibility. Most claims are small, so I would automate the rules that are mechanical (windows, limits, depreciation, duplicates) and keep a human decision for liability and amounts above a threshold.

Claims have their own fraud patterns, distinct from payment fraud:

- **Pre-existing damage** claimed after an unrelated stay. Counter: turnover photos and a condition baseline per listing.
- **Inflated amounts**: replacement value for old items, inflated quotes. Counter: depreciation schedules and price references.
- **Reused evidence**: the same photo in claims for different stays or listings. Counter: a perceptual-hash index of claim photos, the same technique [Describing a Stay: Content, Media and Property Mapping](#content-and-media) uses for duplicate listing photos.
- **Collusion**: a host and a "guest" staging a booking to claim. Counter: identity-graph links between host and guest accounts, claim frequency per host and per guest, and payment-instrument links.

Claims fraud signals belong in the same trust platform as other risk signals, but the decision stays in the claims workflow.

{id: protection-and-incidents--money-retention-recovery-and-the-insurer}
### Money: retention, recovery and the insurer

The money of a claim has four parties. The **host** is owed the decided amount. The **guest** may owe some or all of it. The **platform** pays up to its retention. The **insurer** pays above it and may want the recovery. In the ledger these are separate accounts: a claim payable to the host, a receivable from the guest, protection expense, and a recoverable from the insurer for amounts above the retention. A **reserve** (an estimate of what open claims will cost) lets finance see the liability before claims close. [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html) in RECONCILED explains how to keep such accounts as postings rather than balances computed from case data.

**Recovery from the guest** depends on choices made at checkout. A post-stay charge is a merchant-initiated transaction that works only if the card was set up with Strong Customer Authentication (SCA) and the scheme reference was stored. The guest must also have agreed to the possibility of such charges ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)). Without that, recovery becomes a payment link the guest can ignore.

The insurer relationship is an integration with a contract behind it: notification of losses that may exceed the retention, a monthly **bordereau** (a schedule of claims and payments), recoveries passed on, and audits. Selling insurance is regulated. The EU Insurance Distribution Directive exempts some ancillary sellers of travel-linked insurance where the premium does not exceed €200 per person for services of three months or less, and keeps liability cover out of the ancillary-intermediary definition unless it complements the seller's main activity ([Directive (EU) 2016/97](http://publications.europa.eu/resource/celex/32016L0097), 2016). Whether a host program is insurance distribution depends on its structure. That is a question for counsel, and its answer decides which legal entity issues the terms.

{id: protection-and-incidents--in-practice-how-marketplaces-package-protection}
## In Practice: How Marketplaces Package Protection

**Platform-funded protection on hosted stays.** Airbnb's 2025 annual report describes AirCover for Hosts as "property damage protection of up to $3 million per stay, liability coverage of up to $1 million per occurrence for third-party claims of personal injury or property damage, deep cleaning protection, and pet damage protection", with liability insurance provided through a wholly owned captive insurance subsidiary, and AirCover for guests as support for "host cancellations, inability to check-in, inaccurate listings, and a 24-hour safety support line" ([Airbnb Form 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), 2026). Since 2022 it has packaged these with identity verification and reservation screening as one host-facing promise ([Airbnb 2022 Winter Release](https://news.airbnb.com/product-releases/airbnb-2022-winter-release), 2022). The guest side asks guests to report within 72 hours, and Airbnb first looks for comparable accommodation before refunding ([Airbnb Help Center, AirCover for guests](https://www.airbnb.com/help/article/3218), n.d., fetched October 2026). The same 10-K is candid about the limits: "We do not verify all listings for safety or compliance, relying instead on user-reported issues." Protection is a promise to make good afterwards, not a promise that nothing will go wrong.

**Insurance and guest-pays damage requests on an OTA's homes.** Booking.com's Partner Liability Insurance for 2026 covers home-like properties (apartments, guest houses, villas, holiday homes) booked through Booking.com, with per-incident limits of €1,000,000 in the European Economic Area, £1,000,000 in the UK and US$1,000,000 elsewhere, insurers from the Zurich group and Crawford & Company as claims administrator. It states that it "does not provide coverage for damage or loss to the Partner's property" ([Booking.com Partner Liability Insurance policy summary](https://admin.booking.com/partner-liability-insurance/policy.html), 2026). Damage to the partner's own property is handled through the damage payment request in the terms above, which the guest pays. A 2022 trade report put that program's cap at about €300 ([Rental Scale-Up, 2022](https://www.rentalscaleup.com/booking-com-partner-liability-insurance-and-damage-deposits-by-booking-com/)); current caps are not public.

**An OTA's protection for homes is mostly insurance plus a guest-pays channel; a hosted-stays marketplace funds damage itself**, and therefore needs a full claims operation, a reserve and an evidence store.

{id: protection-and-incidents--corvane-worked-example-the-dubrovnik-claim-replayed}
## Corvane Worked Example: The Dubrovnik Claim, Replayed

{id: protection-and-incidents--the-claim-as-it-happened}
### The claim as it happened

Ivan's stay was three nights at **€420** a night plus a **€150** cleaning fee, a **€1,410** subtotal, with a 12% guest service fee of **€169.20**. His claim on 15 August listed five items:

| Item | Claimed | Evidence | Decided | Reason |
| --- | --- | --- | --- | --- |
| Glass patio door, replacement | €1,450 | Turnover photo on 13 August shows it intact; glazier's quote | €1,450 | Covered |
| Sofa, replacement | €980 | Photos; upholsterer's quote requested by the adjuster | €630 | Repairable: reupholstery, not replacement |
| Pool cleaning and filter | €420 | Invoice | €420 | Covered |
| Deep cleaning | €380 | Invoice | €380 | Covered |
| Garden lights, glassware, cushions | €570 | Photos; receipts | €570 | Covered |
| **Total** | **€3,800** | | **€3,450** | |

The guest was notified on 15 August with 72 hours to respond. On 17 August the guest accepted the two cleaning items and €100 for glassware, **€900**, and disputed the rest. The adjuster asked for an upholsterer's quote for the sofa on 19 August, decided on 26 August, and Ivan was paid **€3,450** on 27 August, twelve days after filing. The guest's €900 was collected on the card used for the booking, which had been stored with consent for post-stay charges under Payment Plans v1 ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)). Cover's net cost was **€2,550**, all within the €10,000 retention, so the insurance partner saw the claim only on its monthly bordereau. Nookaway closed the guest's account under the party rule.

The outcome was fair; the process was luck. It rested on a turnover photo the cleaner happened to take, on Ivan's description of the police visit and on a payment link, and the €3,450 was a "goodwill adjustment" in Burrow.

{id: protection-and-incidents--what-the-numbers-say-about-the-program}
### What the numbers say about the program

Sofia's team rebuilt Nookaway's 2026 protection figures from the three tools for the review. They are illustrative, like everything about Corvane:

| 2026, Nookaway | Value |
| --- | --- |
| Stayed reservations | about 6.0 million |
| Party and disturbance reports | about 3,000 (5 per 10,000 stayed reservations) |
| Damage claims filed | about 15,600; about 10,100 paid |
| Damage paid to hosts | about €12.4 million; median paid claim about €640 |
| Claims above the €10,000 retention | 41 |
| Recovered from guests | about €3.1 million (25% of damage paid) |
| Guest guarantee spend | about €7.9 million, of which €1.3 million rehousing after calendar conflicts ([One Home, Many Calendars: iCal, APIs and Multichannel Hosts](#calendar-sync)) |

Fewer than one paid claim in two hundred exceeded the retention, so **Nookaway is its own claims operation**. And recovery from guests succeeded mostly where a card could still be charged: it was a payments capability, not an adjusting skill.

{id: protection-and-incidents--what-the-forum-decided}
### What the forum decided

On 21 September 2027 the forum agreed five changes, built on **Warden**, the group trust platform approved in August ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)), and owned by Sofia Marín's group trust and safety organization unless noted:

1. **One incident record as a Warden case type**, linked to the reservation in Stayline, the One Stay reservation service, with severity classes S1–S4 and deduplicated intake from guests, hosts, a new neighbor contact page in every Nookaway market, and disclosed devices. Harbor, Elena Petrova's group support platform, routes S1–S2 contacts to a safety team around the clock and handles rebooking through its relocation service. Target: human contact within 15 minutes for S2, against 70 minutes on the Dubrovnik night.
2. **Screening policy as data** in Warden's policy registry. Thresholds and actions per market, listing type and local calendar, with Croatia, Greece and Italy calendars added first. "Convert to request", "redirect" and a step up to documented identity (IL3, see [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)) were added to the action set. The model stays a Nookaway detector on the group risk spine and is called through Warden's booking gate. Distance is computed from the guest's verified city, with a missing value treated as unknown rather than zero risk. The model gained an owner in Kenji Arai's data and ML platform team, a 3% holdout in the attestation band, and monthly evaluation against incident and claim labels.
3. **Claims as money in Fathom**, the group ledger. Leila Haddad's team added protection accounts (guarantee expense, claim payable, guest receivable, insurer recoverable, reserve). Claim decisions post through the same approval-limited recovery-decision path Harbor uses, and goodwill adjustments for protection were switched off from **1 December 2027**.
4. **Protection terms as policy versions** in the same registry, stamped on every Stayline reservation from Q1 2028 and read by the listing page, checkout, the host app, support tools and adjudication. An open claim keeps the reservation's dispute flag set, so it does not complete 14 days after check-out.
5. **One evidence store**, with hashes, a retention schedule agreed with Noor van Dijk's privacy team, and a turnover-photo feature in the host app so that pre-stay condition stops depending on luck.

Replayed under the new policy, the Dubrovnik booking scores higher: the account is nineteen days old, has no stays, books a four-bedroom home two days ahead for a public-holiday weekend, from 31 kilometers away. Under the Croatian August policy it would have been **redirected**. The guest could still have booked a hotel room on Roomstead or a private room on Nookaway. Ivan's villa would have stayed open for another booking.

{id: protection-and-incidents--roomstead-s-homes}
### Roomstead's homes

Roomstead sells about **435,000** alternative-accommodation properties, about 70% of them from professional property managers. In 2027 it had no damage program; managers took deposits at the property. The forum rejected copying Nookaway Cover to Roomstead, because Roomstead's agency model and its professional supply make a platform-funded guarantee both expensive and unnecessary. It agreed instead that from 2028 Roomstead would offer **partner liability insurance for home-like properties** through the same insurance partner, and a **guest-pays damage request** on the shared claims workflow, capped and with the guest's consent at checkout. Both run on the shared incident record, evidence store and ledger accounts. Policy, limits and funding stay brand-specific.

The same accounts later carried the **€212,000** Roomstead reimbursed to **310** guests after the November 2027 extranet phishing wave ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)), which ran as Harbor recovery decisions posting to the same accounts with their own cause code, rather than as goodwill.

{id: protection-and-incidents--the-emergency-exercise}
### The emergency exercise

In October 2027 Sofia ran a tabletop exercise with a fictional wildfire evacuation order on the Algarve coast. The roster query found **1,260** Nookaway reservations with stays in the zone in the next 72 hours and **410** Roomstead reservations at hotels and apartments there. For Roomstead, the hotels knew who was in-house. For Nookaway, only 38% of the reservations had a recorded check-in or lock event, so the platform could not say who was actually there. The exercise produced the requirement that check-in become a reservation fact for every Nookaway stay ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)), and the decision that declared events are one shared object for safety operations and for the cancellation policy engine.

{id: protection-and-incidents--trade-offs}
## Trade-offs

| Decision | Option | When it is right | What it costs |
| --- | --- | --- | --- |
| **How hosts are protected** | Collected deposit or pre-authorization | High-value homes; markets where deposits are normal | Conversion loss; refund operations; the deposit caps the recovery |
| | Post-stay charge on stored credential | Most bookings on a merchant-of-record platform | Charges can fail or be disputed; needs SCA setup and consent at checkout |
| | Platform-funded damage protection | Hosted stays with many individual hosts | A claims operation, a reserve, fraud controls; cost grows with supply |
| | Partner liability insurance and guest-pays requests | OTA homes from professional managers | Narrower promise; hosts still carry their own damage risk |
| **Screening action** | Block | Clear high risk, prior incidents | Lost bookings; contest and review duties |
| | Redirect to rooms and hotels | High risk on entire homes; peak dates | Requires inventory across types; some guests leave anyway |
| | Step up or convert to request | Thin history; high-value homes | Friction for legitimate guests; slower confirmation |
| | Attest only | Moderate risk | Deters a few, mainly creates evidence |
| **Claims operation** | In-house adjusters within a retention | High volume of small claims | Staff and tooling; the platform carries the loss |
| | Insurer or claims administrator for all | Low volume; insurance-led programs | Less control of host experience; data shared with a third party |

My rule of thumb: **pay small claims yourself and insure the tail**, as Corvane does, once the claims workflow, ledger and evidence store exist. Before they exist, a lower retention and an insurer-administered process buy time. That is the right choice for an OTA starting protection for its homes.

{id: protection-and-incidents--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **Who carries damage risk** | The hotel, through its own insurance and incidental holds | The host, backed by the platform's damage protection |
| **Guest identity** | Usually checked at the front desk; the platform rarely verifies guests | The platform verifies guests before booking |
| **Pre-booking screening** | Payment fraud and no-show risk | Party, damage and safety risk, plus payment fraud |
| **First responder in-stay** | Hotel staff on site | Host remotely, the platform's safety team, then emergency services |
| **Guest guarantee** | Relocation when a room is oversold, mostly charged to the hotel | Rebooking or refund when the home fails, mostly funded by the platform |
| **Who knows who is in-house** | The hotel's property management system | Only check-in and lock events, if recorded |
| **Typical claim** | Rare; damage handled by the hotel | Frequent and small, decided by the platform |
| **Documented programs** | Partner liability insurance for home-like stock (Booking.com, 2026); damage requests | Damage protection, liability insurance and guest guarantee as one promise (Airbnb, 2026) |
| **Regulation** | Hotel safety and licensing already exist | Platform terms, data protection for screening and evidence, insurance distribution questions |
| **What to share** | Incident record, evidence store, ledger accounts, insurer interface, declared events | Same |

The two marketplaces genuinely differ in **who carries the risk** and in **the policy**, and they should keep separate programs, limits and screening thresholds. They do not differ in what an incident record, an evidence object, a claim posting or a declared event is. I would build those once in the group trust platform, as Corvane did, and let Roomstead's homes use them under Roomstead's own terms. Convergence makes this more urgent: to a guest planning a party, a Roomstead apartment and a Nookaway home look the same.

{id: protection-and-incidents--failure-modes}
## Failure Modes

- **Three tools, three case numbers.** Screening, support and claims each keep their own record, and nobody can reconstruct an incident without reading free text. *Fix:* one incident record on the reservation that every tool links to.
- **Safety in the support queue.** A party in progress waits behind refund requests because intake has one category and one service-level target. *Fix:* severity classes with their own routing and staffing; S1 always points to emergency services first.
- **A screening model nobody evaluates.** Thresholds are set once, labels come from support categories, and redirected bookings are never measured. *Fix:* an owner, a holdout, labels from incidents and claims, and monthly review per market and season.
- **Terms that differ by surface.** The listing page promises one thing, the agent another, the adjuster pays a third. *Fix:* one policy registry; the reservation records the version.
- **Goodwill as an accounting category.** Claim payments, guarantee rebookings and recoveries are booked as adjustments, so the program's cost and recovery rate are unknown. *Fix:* protection accounts in the ledger, with reasons and policy versions.
- **Recovery without a credential.** The guest's card was never set up for later charges, so recovery depends on goodwill. *Fix:* SCA setup and consent at checkout for every reservation the protection policy covers.
- **No roster in an emergency.** The platform cannot say which guests are inside an evacuation zone. *Fix:* declared events, an active-stay roster and check-in as a recorded fact.

{id: protection-and-incidents--the-chief-architect-s-view}
## The Chief Architect's View

Protection decisions are product, finance, legal and engineering decisions at once. These are the ones I would put on the table.

- **Decide what the platform promises, and to whom.** The size of the guest guarantee and of host damage protection is a commercial and risk decision for the brand's leadership and the CFO. Engineering's job is to make the promise one policy with one version, not to decide it. Changing a limit should be a configuration change with an effective date.
- **Name one owner for the protection domain.** At Corvane it is the Director of Trust and Safety, with support, payments and the ML platform contributing. Without one owner, each team optimizes its own part: support for handle time, payments for authorization rate, the model team for a score nobody uses.
- **Set the retention with data, and revisit it yearly.** The retention is the boundary between the platform's operation and the insurer's. Move it only when the ledger can show loss distributions by market and listing type.
- **Treat screening as a governed decision system.** Policy versions, reason codes, human review, fairness analysis and an evaluation cadence. The model can be replaced. The governance is what keeps it from becoming the Unwatched Model.
- **Plan for the destination-scale emergency before it happens.** The declared event, the active-stay roster, multilingual outreach and the relocation service should be exercised at least once a year, together with the cancellation-policy owners and the customer-service surge plan in [Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability).
- **Watch five numbers:** party and safety reports per 10,000 stays, time to human contact for S1 and S2, claim cycle time from filing to payment, recovery rate from guests, and protection cost as a share of brand revenue.

The long-term consideration is that protection becomes a supply advantage. A platform that can pay a fair claim in days, explain the decision and keep the guest away from the next host has an asset that rests on years of labeled incidents and cannot be copied quickly. A platform that bought a protection product after a headline has only a cost line.

{id: protection-and-incidents--questions-to-ask}
## Questions to Ask

1. If a guest, host or neighbor reports a party at midnight, how many minutes pass before a human at the platform knows, and what reservation context do they see?
2. Do screening, incidents and claims share one record on the reservation, or do they share only a guest ID?
3. Which policy version governed the last claim you paid, and could the listing page and the support agent have quoted the same terms?
4. Who owns the screening model, and when were its misses last measured against incident and claim labels, per market and season?
5. What can a guest do when screening redirects or blocks them, and how would you show a regulator the reasons?
6. What share of damage paid did you recover from guests last year, and what share of reservations had a credential that could be charged after check-out?
7. Where do protection payments sit in the ledger, and can finance separate platform losses, guest recoveries and insurer recoveries?
8. If an evacuation order covered a city tonight, how long would it take to list every guest inside the zone?

Protection is where the platform's promises meet the real world. Regulation is where the real world sets rules for those promises. Registration numbers, night caps, platform duties and consumer law decide which homes may be sold at all and what the platform must prove. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) turns them into a market policy registry and compliance by design.

{id: protection-and-incidents--sources-and-evidence}
## Sources and Evidence

*Company engineering and investor sources*

- [Airbnb, Inc. Form 10-K for fiscal 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm), Airbnb / SEC EDGAR, 2026: AirCover for Hosts limits and captive insurer; AirCover for guests scope; system of trust including safety and neighborhood lines; listings not all verified.
- [How AirCover for Hosts works](https://www.airbnb.com/resources/hosting-homes/a/how-aircover-for-hosts-works-469), Airbnb, 2026: damage protection is not insurance; 24-hour guest response before involving Airbnb.
- [Airbnb 2022 Winter Release](https://news.airbnb.com/product-releases/airbnb-2022-winter-release), Airbnb Newsroom, 2022: protection packaged with verification and screening.
- [Building on our commitment to trust](https://news.airbnb.com/building-on-our-commitment-to-trust-2), Airbnb Newsroom, 2021: risk-based restrictions on entire-home and last-minute bookings.
- [Airbnb introduces new anti-party technology in the US and Canada](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada), Airbnb Newsroom, 2022: published screening signals; redirect to rooms and hotels; Australian pilot result.
- [An update on our work to crack down on parties and disruptive behavior](https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior), Airbnb Newsroom, 2023: party ban history; outcome rates; neighborhood support line and noise sensors.
- [Airbnb's anti-party system returns for July 4 weekend](https://news.airbnb.com/airbnbs-anti-party-system-returns-for-july-4-weekend), Airbnb Newsroom, 2026: holiday redirections and 2025 party-report rate.
- [Measuring discrepancies in Airbnb guest acceptance rates using anonymized demographic data (Project Lighthouse)](https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf), Airbnb anti-discrimination team, 2020: privacy-preserving measurement of outcome gaps.
- [Booking.com Partner Liability Insurance policy summary](https://admin.booking.com/partner-liability-insurance/policy.html), Booking.com, 2026: limits, insurers, claims administrator, home-like eligibility, exclusion of the partner's own property.

*Standards, regulation and documentation*

- [AirCover for guests (help article 3218)](https://www.airbnb.com/help/article/3218), Airbnb Help Center, n.d. (fetched October 2026): 72-hour reporting; comparable accommodation before refund.
- [Airbnb Terms of Service (help article 2908)](https://www.airbnb.com/help/article/2908), Airbnb, 2026: damage amounts charged to the booking's payment method.
- [Booking.com Terms](https://www.booking.com/content/terms.html), Booking.com, 2025: no involvement in damage deposits; damage payment requests within 14 days.
- [About the vacation rentals API](https://developers.expediagroup.com/rapid/lodging/vacation-rentals/about-vacation-rentals-api), Expedia Group Developer Hub, n.d. (fetched October 2026): optional refundable damage deposits.
- [Regulation (EU) 2016/679 (GDPR)](http://publications.europa.eu/resource/celex/32016R0679), European Parliament and Council, 2016: Article 22 on automated individual decisions and safeguards.
- [Directive (EU) 2016/97 on insurance distribution](http://publications.europa.eu/resource/celex/32016L0097), European Parliament and Council, 2016: ancillary insurance intermediaries; exemption thresholds for travel-linked insurance; transposition by 23 February 2018.

*Research and practitioner sources*

- [Airbnb bans the use of indoor security cameras on all properties](https://abc7news.com/airbnb-bans-the-use-of-indoor-security-cameras-on-all-properties/14516158/), ABC7, 2024: press report of the indoor-camera ban and outdoor-device disclosure.
- [Booking.com's new €1,000,000 Partner Liability Insurance and Damage Deposits](https://www.rentalscaleup.com/booking-com-partner-liability-insurance-and-damage-deposits-by-booking-com/), Rental Scale-Up, 2022: earlier damage program pilot; over three years old.
- [Never Update, Only Append: Designing Custom Ledgers](https://zeljkoobrenovic.github.io/spec-driven-journals/finance-systems-architecture/designing-financial-ledgers.html), RECONCILED, 2026: posting rules and reserves that the protection accounts assume.
- Productscape reference models for travel accommodation and hosted stays (author's sibling repository), n.d.: the destination-emergency stressor and the protection and claims gap; generic models, not company descriptions.
- BOOKED research briefs on trust, safety and regulation, on Airbnb, and on hosts, partners and guest service, 2026 (internal): synthesis of screening, protection and incident practice.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
