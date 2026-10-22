# Research brief: Airbnb as a documented case

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. Airbnb is the reference case for the **hosted stays** side of the book because it has published more dated engineering material than any other short-term-rental marketplace, and because its SEC filings describe its money flows in unusual detail. The brief is not an endorsement. Where Airbnb has not described a system, the brief says so instead of filling the gap.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, conference summary, vendor write-up), or from a primary Airbnb page that this session could see only as a search-result excerpt and could not open. Each such case is marked "(excerpt only)".
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every statement about an Airbnb system the company has not described falls here. Chapter writers should re-verify these or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Airbnb's engineering record spans 2014–2026, and the company rewrote large parts of its stack in that time. A 2018 talk about Monorail-to-SOA describes a migration that was then "in its early stages"; a 2019 Kubernetes talk describes a platform that was half migrated. Each section states the date of its evidence, and sources older than about three years carry an **⚠ age** note. Do not describe a 2018–2021 system in the present tense without a newer source.

**Date caveat for airbnb.tech.** Airbnb moved its engineering blog from Medium (`medium.com/airbnb-engineering`) to `airbnb.tech`. The dates below for airbnb.tech posts come from the site's WordPress API. Several posts share one date (2025-04-01, 2025-08-11, 2026-02-25), which suggests batch re-publication of articles first posted on Medium. Treat those dates as "no later than".

**Research limitation.** Three things limited this brief:

- **Older Medium posts could not be opened.** Medium returned HTTP 403 for every article URL, and its RSS feed holds only the ten most recent posts (all from 2026). The canonical 2017–2023 Airbnb posts on payments (the Orpheus idempotency library, "Rebuilding Payment Orchestration", the financial-reporting ledger), Minerva, the Experiment Reporting Framework (ERF), Bighead, Zipline and the internationalization platform were therefore **not read**. Where a search-result excerpt of such a post was visible, the claim is tagged WIDELY REPORTED (excerpt only). Archive and reader-proxy services were not used.
- **The shared web-search quota ran out** about two-thirds of the way through. After that point the brief relied on direct fetches of known URLs (SEC EDGAR, investor PDFs, arXiv, InfoQ, airbnb.tech, news.airbnb.com, the Airbnb Help Center).
- **Some topics have no Airbnb primary source at all**: the internal design of the calendar/availability service, the payments ledger's data model, the risk-scoring models, the Smart Pricing serving system and its update cadence. They are listed under Open questions.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: fee percentages, product availability by country, model versions, programme names.

---

## PART 1: The business as of 2025–2026

### 1.1 Scale

| Metric | Value | Period | Source |
| --- | --- | --- | --- |
| Nights and Seats Booked | 533 million (2024: 492 million, +8%) | FY2025 | 10-K |
| Gross Booking Value (GBV) | $91.3 billion (2024: $81.8 billion, +12%) | FY2025 | 10-K |
| Revenue | $12.24 billion (2024: $11.10 billion, +10%) | FY2025 | 10-K |
| Hosts | "over 5 million" | 10-K, Feb 2026 | 10-K |
| Hosts | "over 5.5 million" | Aug 2026 | Q2 2026 letter |
| Guest arrivals, all time | "over 2.5 billion" | 2026 | 10-K, Q2 2026 letter |
| Average nights per booking (stays only) | 3.7 (2024: 3.8) | FY2025 | 10-K |
| Revenue from listings outside the US | 61% | FY2025 | 10-K |
| Employees / third-party support workers | ~8,200 / ~13,000 | 31 Dec 2025 | 10-K |
| GBV | $27.2 billion (+16% YoY) | Q2 2026 | Q2 2026 letter |
| Nights and Seats Booked | 148.3 million (+10% YoY; Q2 2025: 134.4 million) | Q2 2026 | Q2 2026 letter |
| ADR | $184 (+5% YoY) | Q2 2026 | Q2 2026 letter |
| Implied take rate (revenue / GBV) | 13.2% | Q2 2026 | Q2 2026 letter |

- The FY2025 key-metrics table reads: "Nights and Seats Booked 492 533 8 % Gross Booking Value $ 81,784 $ 91,273 12 %" (in millions) [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- The metric was renamed from "Nights and Experiences Booked" to **"Nights and Seats Booked"**: it now sums nights booked for stays and seats booked for experiences and services, net of cancellations and alterations [VERIFIED: same 10-K, published 2026-02-12]. Chapter writers comparing Airbnb with an OTA should note that Airbnb's headline volume metric now mixes nights and seats.
- Airbnb describes itself as "a global community of over 5 million hosts who have welcomed over 2.5 billion guest arrivals" operating "in over 220 countries and regions" [VERIFIED: same 10-K, published 2026-02-12]. The Q2 2026 letter updates the host count to "over 5.5 million hosts" [VERIFIED: https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf, published 2026-08-06].
- **Hosts are counted by available listing, and the count can double-count people**: "We count the number of hosts on our platform based on the number of hosts with an available listing as of a certain date. Some individuals may have more than one host account and therefore may be counted more than once" [VERIFIED: same 10-K, published 2026-02-12].
- An **active listing** is one "viewable on Airbnb and has been previously booked at least once on Airbnb (excluding HotelTonight)"; an **available listing** is any listing viewable on a given date [VERIFIED: same 10-K, published 2026-02-12]. The 10-K does not publish an active-listing count. Do not quote a current listing count without a dated source.
- Airbnb reports "Bedroom Nights Booked" (nights × bedroom count) as a new lens: it grew over 12% in Q2 2026 against 10% for Nights and Seats Booked, and passed 1 billion bedroom nights over the trailing twelve months [VERIFIED: Q2 2026 letter, published 2026-08-06].
- 2025 net income was $2.5 billion and free cash flow $4.6 billion [VERIFIED: 10-K, published 2026-02-12].
- Platform hosting: "We rely primarily on Amazon Web Services in the United States and abroad to host and deliver our platform" [VERIFIED: 10-K, published 2026-02-12].

**Derived numbers.** FY2025 implied take rate = 12,241 / 91,273 ≈ **13.4%**; FY2024 ≈ 13.6%. FY2025 GBV per Night-or-Seat ≈ $171 [ASSUMPTION/JUDGEMENT: analyst's arithmetic from the 10-K table; Airbnb itself reported 13.2% for Q2 2026].

**OTA vs hosted stays.** Booking Holdings and Expedia report room nights and gross bookings too, but their room nights come from millions of rooms in professionally run properties with many units per property. Airbnb's 3.7 nights per booking and its "Bedroom Nights" metric reflect whole-home, group stays: one listing usually equals one sellable unit, so one booking blocks the whole calendar for those dates [ASSUMPTION/JUDGEMENT].

### 1.2 Money flow: Airbnb is the merchant of record and holds guest funds until check-in

- "When a guest books and pays for a stay, experience, or service on our platform, we hold the total amount the guest has paid until check-in, at which time we recognize our service fee as revenue and initiate the process to remit the payment to the host, which generally occurs on the business day after the scheduled check-in, barring any alterations or cancellations" [VERIFIED: 10-K, published 2026-02-12].
- "As the merchant of record, we bear all payment processing costs for our bookings, including those from chargebacks due to both fraud and non-fraud activities" [VERIFIED: 10-K, published 2026-02-12]. Merchant fees rose $188 million in 2025 "due to higher pay-in volumes" [VERIFIED: same].
- Integrated payments run "in approximately 50 currencies" [VERIFIED: same].
- Funds held for customers sit on the balance sheet as "Funds receivable and amounts held on behalf of customers" with a matching liability "Funds payable and amounts payable to customers": **$6.96 billion** at 31 December 2025 ($5.93 billion a year earlier) [VERIFIED: same]. On 30 June 2026 Airbnb held "$12.2 billion of funds held on behalf of guests" (seasonal peak before summer check-ins) [VERIFIED: Q2 2026 letter, published 2026-08-06].
- Revenue is recognised **net** at check-in: Airbnb "does not fulfill rental promises, bear inventory risk, or set prices. Therefore, revenue is presented on a net basis"; taxes, cleaning and pet fees are excluded from revenue [VERIFIED: 10-K, published 2026-02-12]. Because "the Company's ToS stipulates that a host may cancel a confirmed booking up to the point of check-in", each booking is treated for accounting as a contract that completes at check-in [VERIFIED: same].
- Regulated payment entities: Airbnb Payments, Inc. is a FinCEN-registered Money Services Business holding US state money-transmitter licences; Airbnb Payments Luxembourg SA is a licensed payment institution across the EEA; Airbnb Payments UK Limited is an electronic money institution; there is a Canadian entity [VERIFIED: 10-K, published 2026-02-12].

**Architectural consequence.** Holding the whole booking amount until check-in, paying out the day after, and allowing host cancellation until check-in means Airbnb's payments platform is a **custody-and-disbursement system** with a long-lived liability per booking, not a pass-through. Reserve Now, Pay Later (1.4) shifts the pay-in closer to the stay but does not change the disbursement point [ASSUMPTION/JUDGEMENT, built on the verified 10-K text].

**OTA vs hosted stays.** In the OTA agency model, the hotel charges the guest at the property and pays the OTA a commission later; in the merchant model the OTA charges the guest and pays the hotel on a net rate. Airbnb operates a single merchant-of-record model for all bookings, pays individuals (not businesses) in local currencies, and therefore needs money-transmitter and e-money licences that an agency-model OTA does not [ASSUMPTION/JUDGEMENT; the Airbnb half is VERIFIED above].

### 1.3 Fee model: from split fee to single host-only fee (October 2025 onward) ⚠

| Structure | Host pays | Guest pays | Status |
| --- | --- | --- | --- |
| Split fee (historic default) | 3% for most hosts; 4% in Brazil and Mexico | 14.1%–16.5% of the booking subtotal (cross-currency bookings up to 16.5%) | Being phased out for home hosts |
| Single fee ("host-only") | 15.5% for most hosts; 14%–16% for others; 16% in Brazil and Mexico | No separate service fee | Mandatory for most hosts, including hotels, serviced apartments and hosts using property-management software |
| Services | Typically 15%, minimum $6 | — | |
| Experiences | Typically 20% | — | |

Sources: [VERIFIED: https://www.airbnb.com/help/article/1857, fetched 2026-10-21; the help article carries no publication date]. A host who moves to the single fee "cannot switch back", and the new fee applies only to bookings made after the switch [VERIFIED: same].

- 10-K wording: "Historically, the Company operated only under a split-fee structure, charging service fees as a percentage of the booking amount to both hosts and guests. In October 2025, the Company began transitioning to a single-fee structure, charging only the host a service fee" [VERIFIED: 10-K, published 2026-02-12].
- Q2 2026 letter: "We initially migrated most property management software hosts from a split fee structure (where hosts paid a 3% fee and guests paid a separate service fee) to a single fee of 15.5%. In July, we announced plans to migrate most of the remaining hosts to a single 15.5% service fee, with migration expected to be completed this year. Hosts are able to adjust their prices to maintain the same net earnings and guests will continue to see the full price upfront" [VERIFIED: Q2 2026 letter, published 2026-08-06].
- Secondary sources date the first automatic switch for software-connected hosts to **27 October 2025**, with a 1 December 2025 deadline for others in some markets; one PMS vendor reports a staggered rollout running into late 2026 [WIDELY REPORTED: https://www.hostfully.com/blog/airbnb-host-fees/, 2026]. Use Airbnb's own wording ("Beginning in Q4 2025") unless a dated Airbnb source is found.

**Architectural consequence.** A fee-structure migration is a **pricing-engine and ledger migration**: two fee models coexist per booking (old bookings keep the split fee even if the stay happens after the switch), the displayed price must become the all-in price, and channel-manager integrations have to push prices grossed up for the host fee [ASSUMPTION/JUDGEMENT]. The coexistence rule is VERIFIED above (help article 1857).

**OTA vs hosted stays.** The single host-only fee makes Airbnb's commercial model look like an OTA commission (hotels on Booking.com typically pay a commission and the guest sees one price). It also matters for all-in price display rules in several jurisdictions [ASSUMPTION/JUDGEMENT].

### 1.4 Pay-later and payment options ⚠

- **Reserve Now, Pay Later** launched for US guests booking US listings on 14 August 2025 [WIDELY REPORTED: https://news.airbnb.com/reserve-now-pay-later, 2025 (excerpt only)] and went worldwide on 17 February 2026 for listings with a flexible or moderate cancellation policy; reservations paid in BRL, INR or TRY are excluded; adoption in Q4 2025 was "over 70 percent" of eligible bookings, measured against GBV [VERIFIED: https://news.airbnb.com/reserve-now-pay-later-is-now-available-worldwide, published 2026-02-17].
- The 10-K lists two programmes, **Pay Less Upfront** and **Reserve Now, Pay Later**, and records "unbilled amounts for confirmed bookings" under them as a foreign-currency exposure [VERIFIED: 10-K, published 2026-02-12]. GBV books the full amount at booking time whichever payment option is used [VERIFIED: same].
- RNPL moves cash later: unearned fees were flat year on year at $2.8 billion on 30 June 2026, and "Absent the impact of Reserve Now, Pay Later bookings, which defer guest payments from the time of booking closer to the date of stay, we expect that unearned fees would have grown" [VERIFIED: Q2 2026 letter, published 2026-08-06]. RNPL also pulls bookings earlier ("guests booking further in advance") [VERIFIED: same].
- Interest-free instalments for eligible guests in Mexico and Brazil were added in 2026 [VERIFIED: Q2 2026 letter, published 2026-08-06].

**Architectural consequence.** Pay-later turns one booking into a **scheduled future charge** that can fail. The system needs a stored payment credential, a charge scheduler tied to the cancellation-policy deadline, retry and dunning logic, and a rule for what happens to the host's calendar when the deferred charge fails [ASSUMPTION/JUDGEMENT; Airbnb has not described its implementation].

**OTA vs hosted stays.** "Book now, pay at the property" is the OTA agency default. Airbnb's version keeps Airbnb as merchant of record and charges before the free-cancellation window closes, so hosts can rebook [ASSUMPTION/JUDGEMENT].

### 1.5 AirCover and the "system of trust" as a product

- AirCover for Hosts (2025 10-K): "property damage protection of up to $3 million per stay, liability coverage of up to $1 million per occurrence for third-party claims of personal injury or property damage, deep cleaning protection, and pet damage protection" [VERIFIED: 10-K, published 2026-02-12]. Liability insurance is provided through a wholly-owned captive insurance subsidiary, "up to $1 million per occurrence, subject to a $1 million cap per listing location" [VERIFIED: same].
- AirCover for guests covers "host cancellations, inability to check-in, inaccurate listings, and a 24-hour safety support line" [VERIFIED: same].
- The 2022 Winter Release packaged guest identity verification, reservation screening ("analyzes hundreds of factors in each reservation and blocks certain bookings"), $3M damage protection, $1M liability insurance and a 24-hour safety line as AirCover for Hosts; damage protection and liability insurance are not offered in Japan [VERIFIED: https://news.airbnb.com/product-releases/airbnb-2022-winter-release, published 2022-11-16]. ⚠ age: 2022.
- Paid guest travel insurance (since 2022) is sold in 12 of Airbnb's largest countries; its revenue rose over 60% in Q2 2026 [VERIFIED: Q2 2026 letter, published 2026-08-06].

**OTA vs hosted stays.** Hotels carry their own insurance and staff; an OTA has no comparable damage-protection product. In hosted stays the platform underwrites (via a captive) part of the risk that a hotel would carry itself, so the claims workflow becomes a platform system [ASSUMPTION/JUDGEMENT].

### 1.6 Co-hosting, professional hosts and software-connected supply

- The **Co-Host Network** launched in the 2024 Winter Release (16 October 2024) with "more than 10,000 co-hosts across 10 countries"; co-hosts are recommended by a ranking algorithm using "more than 80 factors"; hosts can share messaging, calendar access and payouts with co-hosts [VERIFIED: https://news.airbnb.com/airbnb-2024-winter-release, published 2024-10-16].
- The 10-K describes co-hosts as "experienced hosts who provide personalized support based on the hosts' needs, from listing setup to managing bookings and communicating with guests" [VERIFIED: 10-K, published 2026-02-12].
- Identity verification extends to co-hosts: "Every host, new co-host, and booking guest must be identity verified" [VERIFIED: https://www.airbnb.com/help/article/1237, fetched 2026-10-21; undated help article].
- **Software-connected hosts** reach Airbnb through partner API programmes, not a public API. The API Terms list programmes for "property management, channel management", operations management, connected devices, hospitality providers, activity/tour booking software and the Preferred Software Partner Program; partners sign an NDA, pass a data-security review and must implement mandatory features within six months; Airbnb may set "call, volume, and rate limits at any time"; partners may not scrape, generate "platform-wide statistics or data" or derive pricing data from API content [VERIFIED: https://www.airbnb.com/terms/api, last updated 2025-10-15].
- 34 Preferred Software Partners were named for 2024 (15 Preferred+, 19 Preferred), chosen on "integration, technical, foundational, and performance requirements" plus a data-security and API-quality review [VERIFIED: https://news.airbnb.com/announcing-our-2024-preferred-software-partners/, published 2024-02-28]. ⚠ the list is renewed annually.

**OTA vs hosted stays.** OTAs get hotel inventory mainly from channel managers and PMSs over OTA/HTNG-style XML connectivity. Airbnb has a similar partner-API tier for professional hosts, but a large share of its hosts edit calendars and prices directly in the app or sync via iCal (Part 4). Its supply is therefore **bimodal**: API-connected professionals and manual individuals [ASSUMPTION/JUDGEMENT; the programme facts are VERIFIED].

### 1.7 The 2025 relaunch: services, experiences, hotels and an "AI-native" app ⚠

- On 13 May 2025 Airbnb launched **Airbnb Services** (10 categories, including chefs, photography, massage and catering, in 260 cities) and relaunched **Airbnb Experiences** (650 cities) inside a redesigned app with Explore and Trips tabs; Services hosts "complete identity verification" and submit licences and certifications; host tools gained a calendar with Google Calendar integration; messaging gained "integrated payments for customizing services" [VERIFIED: https://news.airbnb.com/airbnb-2025-summer-release, published 2025-05-13].
- By Q4 2025 "almost half of Experiences bookings" were not attached to a stay booking [VERIFIED: https://news.airbnb.com/airbnb-q4-2025-financial-results, published 2026-02-12].
- Q2 2026: Experiences supply rose nearly 80% year on year; Services expanded to partner services (grocery delivery, car rentals, airport pickups, luggage storage); Airbnb added "thousands of boutique and independent hotels" in more than 20 destinations; hotels are "a single-digit percentage of nights booked" but hotel nights grew about three times as fast as homes [VERIFIED: Q2 2026 letter, published 2026-08-06].
- The same letter says "We've rebuilt Airbnb from the ground up to be an AI-native company"; the AI support assistant runs in more than 50 languages and "Nearly 45% of issues that begin with our AI assistant are now resolved without a human agent" [VERIFIED: Q2 2026 letter, published 2026-08-06]. Treat "AI-native" as a marketing claim, not an architectural description [ASSUMPTION/JUDGEMENT].

**What the relaunch did to the data model.** Airbnb's data-warehouse team describes it directly (2.3 below): Services introduced a **parent listing with many offerings**, radius-based **service areas** instead of fixed locations, and availability expressed as **business hours converted into bookable slots**, "unlike date-based Homes or start-time-based Experiences"; payments, messaging and customer support stayed product-agnostic [VERIFIED: https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/, published 2026-06-09].

**OTA vs hosted stays.** OTAs added flights, cars and activities as separate verticals, usually sourced from suppliers. Airbnb added services and experiences as **host-supplied** products on the same identity, messaging and payments rails. Its hotel push now moves it towards OTA-style supply [ASSUMPTION/JUDGEMENT].

---

## PART 2: Architecture evolution, 2014–2026

### 2.1 Monorail to SOA v1 (2015–2019) — ⚠ age: 2018–2019 evidence

Primary evidence is Jessica Tai's QCon SF 2018 talk "The Great Migration: from Monolith to Service-Oriented" [VERIFIED: https://www.infoq.com/presentations/airbnb-soa-migration/, published 2018-12-05] and InfoQ's write-up [VERIFIED: https://www.infoq.com/news/2019/02/airbnb-monolith-migration-soa/, published 2019-02-27].

- The monolith was a Ruby on Rails application called **Monorail**. By about 2015 over 200 engineers committed to it, deploying about 200 commits a day with about 15 hours of average blockage a day [VERIFIED: InfoQ presentation, 2018-12-05].
- The first extraction was the **homes data model**, "accessed by almost every feature". Thousands of call sites ruled out rewrites, so the team intercepted data access with a custom **ActiveRecord adapter** that routed queries to the new service [VERIFIED: same].
- Four **service types** with a strict dependency direction [VERIFIED: same]:

| Service type | Role (as described in the talk) |
| --- | --- |
| Data service | Sole owner of its data; gatekeeper for reads and writes |
| Derived data service | Reads from data services, adds its own store and business logic |
| Middle-tier service | Shared write-validation logic, e.g. **reservation validation**, keeping data services free of product logic |
| Presentation service | Assembles data for the user-facing product |

- Migration safety: reads were dual-run behind a gate ramped 1% → 5% → 10% → 25% → 50% → 100% with mismatch checks; writes went to a **shadow database** and were compared with production using strongly consistent reads; Twitter's **Diffy** replayed production traffic to compare old and new code [VERIFIED: same]. **Thrift** was the IDL; standard observability and alert thresholds were generated from the IDL [VERIFIED: same]. **SpinalTap** (open source) streamed database changes to Kafka [VERIFIED: InfoQ news, 2019-02-27].
- Reported results: more than 250 services and 1,000 endpoints on the IDL framework; deploys from hours to minutes; search page about 3× faster and home description page over 10× faster [VERIFIED: InfoQ presentation, 2018-12-05].
- Tai: "Airbnb's approach is closer to service-oriented architecture (SOA)" than to microservices, because of shared components and storage [VERIFIED: InfoQ news, 2019-02-27].
- Services count: fewer than 100 at the end of 2016; over 500 by 2020 [VERIFIED: https://www.infoq.com/presentations/airbnb-api-architecture/, published 2021-06-11].

### 2.2 SOA v2: data aggregator and service blocks (2020–2021) — ⚠ age: 2021

- In QCon Plus 2021, Tai described **SOA v2**: a **GraphQL data aggregator** that centralises data fetching so presentation services stop duplicating it, and **service blocks**, groups of services behind one facade API. "All our services in SOA v1 were using Thrift APIs" [VERIFIED: https://www.infoq.com/presentations/airbnb-api-architecture/, published 2021-06-11].

### 2.3 Viaduct: a data-oriented service mesh (2020 → 2026)

- **Viaduct** is Airbnb's "data-oriented service mesh" serving one central GraphQL schema; teams host business logic **inside** Viaduct as tenant modules that call each other through GraphQL ("re-entrancy") rather than direct code dependencies. Since its November 2020 introduction, traffic grew about 8×, 130+ teams host code in it, the hosted codebase exceeds 1.5 million lines, over 75% of requests are internal, and incident-minutes halved; it runs on Kubernetes with shuffle-sharded dispatch [VERIFIED: https://airbnb.tech/infrastructure/viaduct-five-years-on-modernizing-the-data-oriented-service-mesh/, published 2025-09-17]. Viaduct 1.0 followed in 2026 [VERIFIED (title and date only): https://airbnb.tech/infrastructure/viaduct-1-0-and-the-future-of-airbnbs-data-mesh/, published 2026-05-13].
- The warehouse team's 2026 multi-product post states its own rule: "A domain's data model had to be either completely separate by product type or completely monolithic", with product-specific IDs (`id_experience`, `id_service`) or a generic `id_product_listing` plus `dim_product_type` [VERIFIED: https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/, published 2026-06-09]. The post covers the **offline warehouse only**, not online services.

**OTA vs hosted stays.** Booking.com and Expedia also migrated from monoliths (Perl and Java respectively, per their own talks — see the OTA briefs). The Airbnb case is useful because the reservation-validation logic is explicitly named as a shared middle-tier concern, which is where double-booking rules for one-unit calendars would live [ASSUMPTION/JUDGEMENT].

### 2.4 Kubernetes, Istio and AWS

- QCon London 2019 (Melanie Cebula): "50% of our services are now in Kubernetes", about 250 on the critical production path, with the rest targeted for H1 2019; an internal generator, **kube-gen**, produced per-environment Kubernetes files from a per-service project file; configuration lived in Git in an `_infra` directory [VERIFIED: https://www.infoq.com/presentations/airbnb-kubernetes-services/, published 2019-04-18]. ⚠ age: 2019.
- Airbnb has run **Istio** at scale since 2019, across "tens of thousands of pods, dozens of Kubernetes clusters, and thousands of VMs", carrying tens of millions of QPS at peak; it has upgraded Istio 14 times using canaried Istiod revisions, a `rollouts.yml` that assigns namespaces to versions by consistent hashing, an in-house mutation framework (**Krispr**) and VM agents (`mxagent`, `mxrc`); sidecar mode only [VERIFIED: https://airbnb.tech/infrastructure/seamless-istio-upgrades-at-scale/, published 2025-08-11 (airbnb.tech date; may be a re-post)].
- Primary hosting on AWS [VERIFIED: 10-K, published 2026-02-12].

---

## PART 3: Payments platform

### 3.1 What Airbnb has said most recently (2026)

"Pay as a Local" is the most recent and most detailed payments post that this session could read [VERIFIED: https://airbnb.tech/payments/pay-as-a-local/, published 2026-02-25 (airbnb.tech date)]:

- A multi-year **Payments LTA** replatforming moved payments "from a monolith to domain-driven, capability-oriented services". The core payment domain has subdomains **Pay-in, Payout, Processing, Ledger, and Settlement & Reconciliation** (paraphrase of the post).
- A **connector and plugin model** onboards new payment service providers (PSPs); the processing subdomain supports API- and file-based integration plus switching and routing.
- **Multi-Step Transactions (MST)** is "a processor-agnostic framework that supports payment flows completed across multiple stages". Vendor plugins normalise PSP responses into an `ActionPayload` with status `ACTION_REQUIRED`, covering redirects, SCA challenges and method-specific steps. Flow archetypes: **redirect**, **async** (QR or push prompt, confirmed by webhook) and **direct**.
- A central YAML **Payment Method Config** drives eligibility, input fields and refund rules; code generation produces Java classes and DTOs; "integrating or updating a payment method is largely declarative — just a config change".
- A **PSP Emulator** simulates redirect and async flows, including webhooks, for testing.
- Scale of the programme: 300+ payment options researched; the top 75 travel markets evaluated; 20+ local payment methods (e.g. PIX, UPI, M-Pesa, Naver Pay, Blik, Cartes Bancaires) launched in about 14 months.

### 3.2 Idempotency and orchestration (2019–2021) — not opened; ⚠ age

- Airbnb built an idempotency library called **Orpheus** for its payments services during the SOA migration; it splits each request into **pre-RPC, RPC and post-RPC** phases and records the request in the database before any remote call [WIDELY REPORTED: https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32, 2023; original post "Avoiding Double Payments in a Distributed Payments System", medium.com/airbnb-engineering, 2019, returned HTTP 403 and was not read].
- "Rebuilding Payment Orchestration at Airbnb" says the orchestration system "is responsible for ensuring reliable money movement between hosts, guests, and Airbnb", that billing data, payment APIs and orchestration had been "tightly coupled with the concept of a reservation for a stay" (which made Experiences hard to support), and that the rebuild split workflows into retryable idempotent steps built on Orpheus, reaching "five 9s" of consistency [WIDELY REPORTED: https://airbnb.tech/?p=49, ~2021 (excerpt only; the URL now returns 404)].
- A "Unified Payments Data Read" layer gave clients one interface and a read-optimised store "to reduce the friction and complexity for client integrations, while greatly improving query performance and reliability" [WIDELY REPORTED: https://airbnb.tech/?p=147, ~2023 (excerpt only; 404 when fetched)]. A secondary summary cites a 150× read-latency gain [WIDELY REPORTED, unverified figure].
- **Riverbed** materialised views list **payments** among their use cases (3.4 / 7.1) [VERIFIED: https://www.infoq.com/news/2023/10/airbnb-riverbed-introduction/, published 2023-10-04].

### 3.3 Durable workflows (2026)

- **Skipper** is an embedded durable workflow engine (a Java/Kotlin library) that stores workflow state in the host service's own database (MySQL or Airbnb's Unified Data Store). Users include **insurance, payments, media processing, incentives and wallet** teams; payments uses it for transaction orchestration and scheduled financial operations. Actions are checkpointed; execution is at-least-once ("Actions may execute more than once in edge cases"), so actions must be idempotent; failures run `@Compensate` methods in reverse order; peak throughput 10,000 workflows per second on DynamoDB; 15+ use cases after a year in production [VERIFIED: https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/, published 2026-04-29].

### 3.4 The ledger

- Airbnb names **Ledger** as a payments subdomain (3.1) but has not, in any source this session could open, described its data model [VERIFIED for the name only: Pay as a Local, 2026-02-25].
- Whether Airbnb's ledger is double-entry, how it models funds held until check-in, and how it reconciles PSP settlement files are **not verified**. A double-entry, append-only ledger with balances per account (guest, host, platform revenue, taxes, PSP clearing) is the standard design for a merchant-of-record marketplace that holds funds [ASSUMPTION/JUDGEMENT]. The 10-K's funds-receivable / funds-payable pair (1.2) is the accounting shadow of such a ledger [ASSUMPTION/JUDGEMENT].

**OTA vs hosted stays.** An agency-model OTA's payments problem is mostly **commission invoicing** to hotels. A merchant-of-record hosted-stays platform runs pay-in, custody, FX, payouts to millions of individuals in ~50 currencies, tax withholding and reconciliation. The verified Airbnb subdomain list (Pay-in, Payout, Processing, Ledger, Settlement & Reconciliation) is a good chapter skeleton [ASSUMPTION/JUDGEMENT; the subdomain list is VERIFIED].

---

## PART 4: Calendar, availability and supply connectivity

### 4.1 What is documented

- **iCal sync**: hosts import an external `.ics` link and export Airbnb's; "Airbnb updates synced calendars every 3 hours"; manual refresh is rate-limited; up to 2 years of data is imported; "Nights booked on another website's calendar will be automatically blocked on Airbnb", but "nights that you block on another calendar may or may not be blocked on Airbnb" [VERIFIED: https://www.airbnb.com/help/article/99, fetched 2026-10-21; undated].
- Host-side availability rules are calendar inputs: preparation time, advance notice and minimum stays [VERIFIED: same].
- API-connected PMS and channel-manager partners operate under data scopes that let them "access, read, modify, write" certain data types [VERIFIED: https://www.airbnb.com/terms/api, last updated 2025-10-15]. The specific endpoints (availability, pricing, reservations) are not public.
- Search retrieval had to cope with "frequent updates to pricing and availability": in the 2025 embedding-based retrieval work, HNSW was rejected partly because those updates made its memory footprint too large; IVF clusters were used as an ordinary search filter instead [VERIFIED: https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/, published 2025-04-01 (airbnb.tech date)].
- Services availability is modelled as business hours turned into bookable slots; Homes are date-based; Experiences are start-time-based [VERIFIED: Scaling beyond one, 2026-06-09].
- The supply strategy now explicitly includes "actively encouraging existing hosts to open up more of their calendar availability" [VERIFIED: Q2 2026 letter, published 2026-08-06].

### 4.2 What is not documented

- No Airbnb source found in this session describes the online **calendar/availability service**: its storage, how it prevents double booking under concurrent requests, how instant book and request-to-book hold dates, or how iCal and API updates are merged.

[ASSUMPTION/JUDGEMENT] For a one-unit listing, the defensible reference design is: one availability row per listing-night (or interval), a conditional write or row lock on the requested nights at booking time, a short-lived hold during payment authorisation, and asynchronous propagation of the change to search indexes and connected channels. The 3-hour iCal refresh means **double bookings across platforms are a known, accepted risk for iCal-only hosts**, which is one reason professional hosts move to API-connected channel managers.

**OTA vs hosted stays.** OTA inventory is **counts per room type per night** (allotments) pushed by channel managers in near real time; overbooking a room type by one is tolerable because the hotel can walk a guest. Hosted-stays inventory is a **single unit**: availability is boolean per night, any overlap is a hard double booking, and a large share of supply syncs by polling iCal [ASSUMPTION/JUDGEMENT; the iCal mechanics are VERIFIED].

---

## PART 5: Search ranking and discovery (2018–2026)

### 5.1 Publication timeline

| Year | Work | Venue | What it established | Tag |
| --- | --- | --- | --- | --- |
| 2015 | Aerosolve open-sourced (pricing tips, ranking, fraud) | OpenAir conference | Early ML library for sparse interpretable features | WIDELY REPORTED |
| 2018 | Real-time Personalization using Embeddings for Search Ranking | KDD 2018 | Listing and user embeddings tailored to a marketplace where guests rarely book the same item twice and "each listing can host only one booking for a given date range" (paraphrase); search ranking and similar listings "drive 99% of conversions" | VERIFIED |
| 2018 | Applying Deep Learning to Airbnb Search | KDD 2019 (arXiv 2018-10) | GBDT gains "plateaued"; move to neural networks; "Deep learning was steep learning for us" | VERIFIED |
| 2020 | Improving Deep Learning for Airbnb Search | KDD 2020 (arXiv 2020-02) | "ABCs": architecture, position **b**ias, **c**old start for new listings | VERIFIED |
| 2022 | Learning To Rank Diversely at Airbnb | CIKM 2023 | Booking probability of a listing is **not** independent of the other results; diversity-aware ranking | VERIFIED |
| 2023 | Optimizing Airbnb Search Journey with Multi-task Learning (Journey Ranker) | KDD 2023 | Multi-task model for long search journeys and host rejection/cancellation; deployed in four products | VERIFIED |
| 2024 | Learning to Rank for Maps at Airbnb | KDD 2024 | List-ranking assumptions "simply break down for maps" | VERIFIED |
| 2024 | Transforming Location Retrieval at Airbnb; Multi-objective LTR by Model Distillation; Predicting Customer Support Needs in Ranking; Listing Embeddings in Two-Sided Marketplace | KDD/CIKM 2024 | Titles listed on Airbnb's paper page | VERIFIED (titles only) |
| 2025 | Embedding-Based Retrieval for Airbnb Search | airbnb.tech | First EBR stage: two-tower model, IVF index used as a filter | VERIFIED |
| 2025 | Interleaving and Counterfactual Evaluation for Search Ranking | KDD 2025 | Experiment sensitivity up to 100× vs A/B tests | VERIFIED |
| 2025 | Beyond Pairwise LTR; Learning to Comparison-Shop; Maps Ranking Optimization; BiListing; Augmenting Search Results with Recommendations | CIKM 2025 | Listed in the 2025 year-in-review | VERIFIED (summaries only) |
| 2026 | Personalizing search from the guest journey | airbnb.tech | Transformer sequence encoder + setwise ranker | VERIFIED |
| 2026 | CASTLE | CIKM 2026 / airbnb.tech | Synthetic training data for natural-language search | VERIFIED |

Sources: [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb, published 2018-08]; [VERIFIED: https://arxiv.org/abs/1810.09591, published 2018-10-22]; [VERIFIED: https://arxiv.org/abs/2002.05515, published 2020-02-10]; [VERIFIED: https://arxiv.org/abs/2210.07774, published 2022-09-19, revised 2023-08-08]; [VERIFIED: https://arxiv.org/abs/2305.18431, published 2023-05-28]; [VERIFIED: https://arxiv.org/abs/2407.00091, published 2024-06-25]; [VERIFIED: https://airbnb.tech/research/academic-papers/, fetched 2026-10-21]; [VERIFIED: https://arxiv.org/abs/2508.00751, published 2025-08-01]; [VERIFIED: https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/, published 2026-02-25]; Aerosolve [WIDELY REPORTED: https://www.phocuswire.com/Airbnbs-pricing-algorithm-and-Aerosolve-its-open-source-machine-learning-tool, 2015 (excerpt only; 403 when fetched)].

⚠ age: the 2018–2020 papers describe models that have since been extended at least three times (Journey Ranker, maps LTR, setwise ranking, EBR). Cite them as history.

### 5.2 The current documented ranking stack (2025–2026)

- **Retrieval**: Embedding-Based Retrieval narrows "the initial set of eligible homes into a smaller pool" for heavier rankers. Two towers: a listing tower computed "offline on a daily basis" and a query tower (location, guests, stay length) run at request time. Training uses contrastive pairs from user "trips": the booked home is the positive; seen-but-not-booked homes are negatives (random negatives made the task "too easy"). **IVF** was chosen over HNSW because HNSW "performed slightly better" but frequent price/availability updates bloated its memory and parallel HNSW + filters had poor latency; cluster assignments are applied as "a standard search filter"; Euclidean distance gave "much more balanced clusters" than dot product. The A/B test showed a "statistically-significant gain in overall bookings" [VERIFIED: https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/, published 2025-04-01 (airbnb.tech date)].
- **Ranking**: a Transformer encodes the guest journey (long-term: up to 80 events over seven years including bookings, reviews and cancellations; short-term: up to 200 listing views over 21 days); the encoder runs as a daily batch job and the ranker fetches the stored embedding in real time; a **setwise ranker** scores candidates together. Online gains: +0.55% uncanceled bookers and +0.82% uncanceled nights from adding the short-term sequence; +0.28% uncanceled bookings from the setwise ranker [VERIFIED: https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/, published 2026-07-27]. A follow-up adds real-time updates through Chronon [VERIFIED (title and date only): https://airbnb.tech/ai-ml/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon/, published 2026-09-23].
- **Maps** are a second result surface with their own ranking theory and NDCG variant [VERIFIED: arXiv 2407.00091, 2024-06-25; 2025 year-in-review].
- **Natural-language search** is in development: CASTLE generates queries from booked-vs-viewed listing pairs using an LLM so that labels are correct "by construction"; KL divergence from real query distributions of 1.01 against 9.33 for the best baseline; expert agreement 91–93% [VERIFIED: https://airbnb.tech/ai-ml/castle-training-natural-language-search-before-the-first-real-query/, published 2026-10-13]. The post does not say the feature has launched.
- **Evaluation**: interleaving and counterfactual methods raise sensitivity "by a factor of up to 100" compared with A/B tests on conversion metrics [VERIFIED: arXiv 2508.00751, 2025-08-01].
- **Underlying engine**: an Apache Lucene-based retrieval system was reported in the LISTED research (January 2026 source) but was **not re-verified** in this session [ASSUMPTION/JUDGEMENT until re-checked].

**What the ranking literature says about hosted stays specifically.** Three marketplace properties recur in the papers and are the hosted-stays chapter's core argument [ASSUMPTION/JUDGEMENT, synthesised from the VERIFIED abstracts]:

1. **Single-unit inventory**: a listing can be booked once per date range, so popularity cannot be scaled up and diversity matters (KDD 2018; Learning To Rank Diversely).
2. **Host-side failure**: a "reservation request" can be "rejected or cancelled by the host prior to check-in" (Journey Ranker), so ranking optimises for **uncanceled** bookings, not clicks.
3. **Long, multi-session journeys**: guests "often spend weeks exploring and comparing" (Journey Ranker), which motivates sequence models over the guest journey.

**OTA vs hosted stays.** OTA ranking chooses among properties that each have many rooms and multiple rate plans; price and availability come from a rates cache fed by suppliers, and the same hotel can be booked by many guests on the same night. Hosted-stays ranking must treat availability as a **hard per-listing filter** and model host acceptance [ASSUMPTION/JUDGEMENT].

---

## PART 6: Pricing

- **KDD 2018, "Customized Regression Model for Airbnb Dynamic Pricing"** (Peng Ye et al.): every listing is unique, so estimating a demand curve is hard; the system has three stages — "a binary classification model predicts the booking probability of each listing-night", a regression model with "a customized loss function" predicts the optimal price, and a personalisation layer produces "the final price suggestions"; deployed in **Price Tips and Smart Pricing**; "Online A/B testing results demonstrate the effectiveness" [VERIFIED: https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing, published 2018-08]. ⚠ age: 2018; no newer pricing-model paper appears on Airbnb's publications page [VERIFIED: https://airbnb.tech/research/academic-papers/, fetched 2026-10-21].
- **Smart Pricing as a product**: uses "hundreds of factors about your listing and your area"; the host sets a minimum and maximum; changes never affect pending or confirmed reservations; hosts can override individual nights; weekly, monthly and trip-length discounts override Smart Pricing; Airbnb may switch it off during disasters or unrest "to prevent extreme price changes and comply with local laws" [VERIFIED: https://www.airbnb.com/help/article/1168, fetched 2026-10-21; undated]. The page does not say how often prices recalculate.
- **Aerosolve** (2015) powered the first price tips; it was described as suited to "sparse, interpretable features" such as "number of rooms, location, price" [WIDELY REPORTED: https://www.phocuswire.com/Airbnbs-pricing-algorithm-and-Aerosolve-its-open-source-machine-learning-tool, 2015 (excerpt only)]. ⚠ age: 2015 — historical only.
- 2025–2026 host tooling: "better pricing tools and price tips" [VERIFIED: 10-K, 2026-02-12]; "Simplified pricing in Airbnb Setup" (weekday/weekend rates) and personalised recommendations on "calendar availability, and pricing" [VERIFIED: Q2 2026 letter, 2026-08-06].
- COVID and forecasting: Airbnb's 2026 posts describe how COVID broke its forecasting models and what it built for the next shock [VERIFIED (titles and dates only): https://airbnb.tech/data/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock/, published 2026-03-24; https://airbnb.tech/ai-ml/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn/, published 2026-08-20]. Not read in detail; worth a follow-up for the pricing chapter.

**OTA vs hosted stays.** Hotels price with revenue-management systems (RMS) across room types, rate plans and length-of-stay controls, and push rates through channel managers; the OTA usually does not set the price. Airbnb **suggests** prices to non-professional hosts (Smart Pricing, Price Tips) inside host-set bounds, because most hosts have no RMS; professional hosts use third-party dynamic-pricing tools over the API [ASSUMPTION/JUDGEMENT; the Airbnb mechanics are VERIFIED]. The host-only fee (1.3) changes what the host's price means: it is now the all-in guest price before taxes, which affects every pricing model and every PMS integration [ASSUMPTION/JUDGEMENT].

---

## PART 7: Data, ML and experimentation platforms

| System | What it is | Evidence | Evidence date |
| --- | --- | --- | --- |
| **Riverbed** | Lambda-architecture framework for distributed materialised views; GraphQL-defined; CDC from Kafka for real time, Spark backfills from daily snapshots; 2.4 billion events and 350 million documents a day; 50+ views; used by payments, search, reviews, itineraries | VERIFIED: https://www.infoq.com/news/2023/10/airbnb-riverbed-introduction/ | 2023-10-04 |
| **Chronon** | Feature platform: define a feature once for offline training and online serving; point-in-time-correct backfills; Kafka, Spark, Hive, Airflow; open-sourced April 2024; adopters listed include Stripe, OpenAI, Netflix, Uber | VERIFIED: https://www.infoq.com/news/2024/04/airbnb-chronon-open-sourced/ ; https://github.com/airbnb/chronon | 2024-04-18; fetched 2026-10-21 |
| **Zipline** | Earlier name of Airbnb's feature-engineering framework, generally reported as Chronon's predecessor | Not verified; neither the Chronon README nor the InfoQ article mentions it | — |
| **Bighead** | End-to-end ML platform presented c. 2018 | Not verified (searches returned nothing; Medium posts unreadable) | ⚠ c. 2018 |
| **Minerva** | Metric platform that standardises metric definitions and computation; "over 12,000 metrics and 4,000 dimensions" | WIDELY REPORTED: https://roundup.getdbt.com/p/ep-1-robert-chang-on-scaling-metrics (interview with a Minerva PM) | ⚠ c. 2021 |
| **ERF** (Experiment Reporting Framework) | Internal A/B testing platform introduced 2014; one Airbnb post cites ~500 concurrent experiments and ~2,500 metrics a day | WIDELY REPORTED: https://medium.com/airbnb-engineering/experiment-reporting-framework-f3faca569e0c (excerpt only) | ⚠ 2014–c. 2017 |
| **Interleaving / counterfactual evaluation** | Up to 100× sensitivity for ranking experiments | VERIFIED: arXiv 2508.00751 | 2025-08-01 |
| **Identity graph** | JanusGraph + DynamoDB + OpenSearch; 7 billion nodes, 11 billion edges; used for trust and fraud | VERIFIED (see 8.3) | 2026-05-19 |
| **Viaduct** | GraphQL data-oriented service mesh | VERIFIED (see 2.3) | 2025-09-17 |
| **Skipper** | Embedded durable workflow engine | VERIFIED (see 3.3) | 2026-04-29 |

- Airbnb's experimentation research output (2021–2026) includes switchback experiments, variance reduction for "sparse and delayed outcomes", long-term ranking effects and batch-adaptive Bayesian inference [VERIFIED: https://airbnb.tech/research/academic-papers/, fetched 2026-10-21]. Delayed outcomes matter for stays because the booking-to-stay gap can be months and cancellations arrive late [ASSUMPTION/JUDGEMENT].

**OTA vs hosted stays.** Booking.com is the best-documented experimentation culture in OTAs (see the OTA brief). Airbnb's distinctive problems are **two-sided interference** (a ranking change moves bookings between hosts) and **long-term marketplace health** — "Beyond the Experiment Window" estimates long-term effects of ranking changes "such as on marketplace health" [VERIFIED: 2025 year-in-review, 2026-02-25].

---

## PART 8: Trust and safety

### 8.1 The documented building blocks

- Airbnb's "system for trust" lists: "host and guest reviews, account protection, risk scoring, secure payments, a nondiscrimination policy, watchlist and background checks in certain jurisdictions, cleanliness, fraud and scam prevention, insurance and similar protections, booking restrictions, an urgent safety line, a 24/7 neighborhood support line, anti-party technology, and a guest refund policy" [VERIFIED: 10-K, published 2026-02-12].
- Its limits, in the 10-K's own words: users are not required to re-verify identity after initial verification; background checks run "in the United States and India for certain users" and users are screened against sanctions watch lists, "but these are not exhaustive"; "We do not verify all listings for safety or compliance, relying instead on user-reported issues" [VERIFIED: 10-K, published 2026-02-12]. Chapter writers should use this candour: the platform's risk controls are probabilistic.

### 8.2 Identity verification

- "Every host, new co-host, and booking guest must be identity verified." Guests verify at booking; hosts before a listing is published. Verification checks legal name, address and contact details against "trusted third-party sources or a government ID"; Airbnb may ask for an ID photo and a selfie ("This selfie won't be used on your profile"); third-party providers authenticate documents and, where lawful, run background checks [VERIFIED: https://www.airbnb.com/help/article/1237, fetched 2026-10-21; undated]. ⚠ verification rules vary by country.
- The 2025 app profile highlighted "over 200 million verified guests and hosts" [VERIFIED: https://news.airbnb.com/airbnb-2025-summer-release, published 2025-05-13].

### 8.3 Reservation screening and the party ban

- The anti-party system for the US and Canada (August 2022) flags "potentially high-risk reservations" using signals including positive-review history, account age, trip length, distance from the listing and weekend vs weekday; it "is designed to prevent a reservation attempt from going through"; blocked guests may still book a private room or a hotel; an Australian pilot from October 2021 reported a 35% drop in unauthorised parties [VERIFIED: https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada, published 2022-08-16]. ⚠ age: 2022.
- The party ban began in August 2020 and was codified in 2022; screening is deployed worldwide; Airbnb reported a 55% drop in the global rate of party reports and that 0.039% of 2022 reservations led to a party allegation, about 0.09% of stays to a safety-related report, and about 0.02% to damage reimbursement of $1,000 or more [VERIFIED: https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior, published 2023-08-31]. These are self-reported figures.
- AirCover's 2022 description of screening: "analyzes hundreds of factors in each reservation and blocks certain bookings" [VERIFIED: 2022 Winter Release, 2022-11-16].
- Airbnb also runs heightened holiday-weekend defences (Halloween, New Year's Eve, July 4) on top of year-round screening [WIDELY REPORTED: news.airbnb.com search results, 2023–2025 (excerpt only)].

### 8.4 Identity graph (2026)

- The identity graph supports Trust and Safety by resolving identities and finding linked accounts ("detecting suspicious activities to identifying linked accounts"); it holds 7 billion nodes and 11 billion edges, growing about 5 million edges a day; most queries are 4–8 hops; stack is JanusGraph, DynamoDB and OpenSearch with Gremlin queries; read P95 fell from about 2.1 s to 1.0 s against the previous vendor [VERIFIED: https://airbnb.tech/infrastructure/scaling-airbnbs-identity-graph-with-a-unified-knowledge-graph-infrastructure/, published 2026-05-19].

### 8.5 What is not documented

- The models behind "risk scoring" and reservation screening (features, training labels, thresholds, latency budget, where in the booking flow they run) are not described in any source found. The plausible design — a synchronous risk score at booking request, with a block / step-up verification / allow decision, fed by account, payment, device and graph features — is [ASSUMPTION/JUDGEMENT].

**OTA vs hosted stays.** OTA fraud work is mostly **payment fraud** (stolen cards, chargebacks) and fake hotel listings; the hotel itself controls who walks in. Hosted stays add **guest-to-host physical risk** (parties, damage, safety) and **host-to-guest risk** (fake listings, scams), so trust becomes a pre-booking decision on the reservation itself, not only on the payment [ASSUMPTION/JUDGEMENT; the Airbnb mechanisms are VERIFIED].

---

## PART 9: Internationalisation, local payments and regulation

- 220+ countries and regions, ~50 currencies, 61% of revenue from listings outside the US [VERIFIED: 10-K, 2026-02-12].
- Local payment methods: 20+ LPMs launched in about 14 months through a config-driven, PSP-agnostic platform (Part 3.1) [VERIFIED: Pay as a Local, 2026-02-25].
- The AI customer-support assistant runs in more than 50 languages [VERIFIED: Q2 2026 letter, 2026-08-06]. LLM-based support research (EMNLP 2025, COLING) is listed in the 2025 year-in-review [VERIFIED: 2026-02-25].
- Translation of user-generated content ("Translation Engine", launched November 2021, 60+ languages) and Airbnb's internationalisation platform post (attributed to Hua Zheng, "62 languages") are known only from secondary or excerpt sources [WIDELY REPORTED: https://news.airbnb.com/br/airbnb-anuncia-expansao-da-tecnologia-translation-engine/, 2021 (excerpt only)]. ⚠ age.
- Regulation as an architectural input: the 10-K names the EU Digital Services Act and "the EU STR Regulation" among laws that may increase liability, and reports that in 2025 "the Spanish Ministry of Consumer Affairs proposed to assess a fine of approximately 65 million Euro ($76 million) in connection with alleged non-compliance with short-term rental listing regulations in Spain"; "We have resolved some disputes by agreeing to remove listings or share data with authorities" [VERIFIED: 10-K, 2026-02-12]. See the regulation brief for the regulation itself.

**OTA vs hosted stays.** OTAs localise a catalogue written by hotels in a few hundred thousand properties and pay businesses; Airbnb translates **user-generated** listings, messages and reviews in real time, and pays individuals locally, often in markets where cards are not the dominant method [ASSUMPTION/JUDGEMENT]. Hosted-stays regulation (registration numbers, night caps, data sharing) lands on the **listing** and the **calendar**; hotel regulation rarely touches the OTA's systems [ASSUMPTION/JUDGEMENT].

---

## PART 10: What the Airbnb case teaches the book

[ASSUMPTION/JUDGEMENT] — analyst synthesis from the VERIFIED material above.

1. **Custody shapes the payments architecture.** Holding the full booking until check-in, paying out the next business day, and letting hosts cancel until check-in produces a ledger-centred, multi-currency, licensed payments platform with explicit Pay-in / Payout / Processing / Ledger / Settlement-and-Reconciliation subdomains.
2. **One-unit inventory shapes everything downstream.** Availability is a hard filter in retrieval; ranking optimises uncanceled bookings and diversity; iCal's 3-hour polling makes cross-platform double bookings a structural risk.
3. **Migration discipline is the reusable lesson from Monorail.** Intercept at the data-access layer, dual-read with a ramped gate, shadow-write and compare, then extract a shared middle tier for reservation validation.
4. **The product line broke the data model.** Services and experiences forced a parent-listing/offering split, slot-based availability and product-agnostic payments; a platform built around "a reservation for a stay" had to be generalised.
5. **Fees are architecture.** The move to a 15.5% host-only fee, with old and new fee models coexisting per booking, is a pricing, display, ledger and partner-API change, not just a commercial decision.

---

## Key numbers

| Number | Value | Source | Date |
| --- | --- | --- | --- |
| Nights and Seats Booked | 533 million (FY2025) | Airbnb 10-K FY2025 | 2026-02-12 |
| Gross Booking Value | $91.3 billion (FY2025) | Airbnb 10-K FY2025 | 2026-02-12 |
| Revenue | $12.24 billion (FY2025) | Airbnb 10-K FY2025 | 2026-02-12 |
| Implied take rate | ≈13.4% (FY2025, analyst arithmetic); 13.2% (Q2 2026, Airbnb) | 10-K; Q2 2026 letter | 2026-02-12; 2026-08-06 |
| Hosts | >5 million (10-K); >5.5 million (Q2 2026) | 10-K; Q2 2026 letter | 2026-02-12; 2026-08-06 |
| Guest arrivals, cumulative | >2.5 billion | 10-K | 2026-02-12 |
| Average nights per booking | 3.7 | 10-K | 2026-02-12 |
| ADR | $184 (Q2 2026) | Q2 2026 letter | 2026-08-06 |
| GBV | $27.2 billion (Q2 2026, +16%) | Q2 2026 letter | 2026-08-06 |
| Currencies supported for payments | ~50 | 10-K | 2026-02-12 |
| Funds held for customers | $6.96 billion (31 Dec 2025); $12.2 billion (30 Jun 2026) | 10-K; Q2 2026 letter | 2026-02-12; 2026-08-06 |
| Split fee | Host 3% (4% BR/MX) + guest 14.1–16.5% | Airbnb Help Center 1857 | fetched 2026-10-21 |
| Single host-only fee | 15.5% (16% BR/MX) | Help Center 1857; Q2 2026 letter | 2026-08-06 |
| Reserve Now, Pay Later adoption | >70% of eligible bookings (Q4 2025) | news.airbnb.com | 2026-02-17 |
| AirCover for Hosts | $3M damage per stay; $1M liability per occurrence | 10-K | 2026-02-12 |
| Co-Host Network at launch | >10,000 co-hosts, 10 countries | news.airbnb.com | 2024-10-16 |
| Services / Experiences at launch | 10 categories in 260 cities / 650 cities | news.airbnb.com | 2025-05-13 |
| Employees / third-party support workers | ~8,200 / ~13,000 | 10-K | 2026-02-12 |
| iCal sync interval | every 3 hours | Help Center 99 | fetched 2026-10-21 |
| Preferred Software Partners | 34 (2024) | news.airbnb.com | 2024-02-28 |
| Services in SOA | <100 (end 2016) → >500 (2020) | InfoQ / QCon Plus | 2021-06-11 |
| Services on Kubernetes | 50% (April 2019) | InfoQ / QCon London | 2019-04-18 |
| Istio footprint | tens of thousands of pods, dozens of clusters, thousands of VMs | airbnb.tech | 2025-08-11 |
| Riverbed throughput | 2.4 billion events/day, 350 million documents/day | InfoQ | 2023-10-04 |
| Identity graph | 7 billion nodes, 11 billion edges | airbnb.tech | 2026-05-19 |
| Skipper peak throughput | 10,000 workflows/s | airbnb.tech | 2026-04-29 |
| Local payment methods launched | 20+ in ~14 months | airbnb.tech | 2026-02-25 |
| Party allegations | 0.039% of 2022 reservations | news.airbnb.com | 2023-08-31 |
| Ranking experiment sensitivity | up to 100× via interleaving | arXiv 2508.00751 | 2025-08-01 |

## Open questions / not verifiable

- **Payments internals**: Orpheus, the 2021 payment-orchestration rebuild, the unified payments read layer and the financial-reporting ledger posts could not be opened (Medium 403; old airbnb.tech `?p=` URLs 404). Whether the ledger is double-entry, how funds-held-until-check-in is modelled, and payout batching remain unverified.
- **Calendar and availability service**: no Airbnb source describes its storage, concurrency control, hold semantics for request-to-book vs instant book, or how iCal and API updates are reconciled.
- **Risk scoring and reservation screening models**: features beyond the 2022 newsroom list, latency, and decision outcomes (block vs step-up) are undocumented.
- **Smart Pricing today**: no pricing paper after KDD 2018 appears on Airbnb's publications page; recalculation cadence and current model family unknown.
- **Bighead, Zipline, Minerva, ERF**: current status (retired, renamed or still running) unknown; only 2014–2021 secondary evidence.
- **Search engine substrate**: the "Lucene-based retrieval with IVF filter" description used in LISTED was not re-verified here.
- **Active-listing count**: not disclosed in the FY2025 10-K; third-party counts (e.g. "8 million listings") should not be used without a dated Airbnb source.
- **Exact fee-migration dates by market**: Airbnb says "Beginning in Q4 2025" and "migration expected to be completed this year" (2026); per-market dates come only from PMS vendors.
- **Internationalisation platform**: language count (60+ vs 62) and architecture not verified from a primary source.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Airbnb, Inc. Form 10-K for fiscal year 2025 | Airbnb / SEC EDGAR | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm |
| Q2 2026 Shareholder Letter | Airbnb | 2026 | https://s26.q4cdn.com/656283129/files/doc_financials/2026/q2/Airbnb-Q2-2026-Shareholder-Letter-FINAL.pdf |
| Airbnb Q4 2025 financial results | Airbnb Newsroom | 2026 | https://news.airbnb.com/airbnb-q4-2025-financial-results |
| Airbnb service fees (help article 1857) | Airbnb Help Center | undated, fetched 2026 | https://www.airbnb.com/help/article/1857 |
| Calendar sync (help article 99) | Airbnb Help Center | undated, fetched 2026 | https://www.airbnb.com/help/article/99 |
| Identity verification (help article 1237) | Airbnb Help Center | undated, fetched 2026 | https://www.airbnb.com/help/article/1237 |
| Smart Pricing (help article 1168) | Airbnb Help Center | undated, fetched 2026 | https://www.airbnb.com/help/article/1168 |
| API Terms of Service | Airbnb | 2025 | https://www.airbnb.com/terms/api |
| Announcing our 2024 Preferred Software Partners | Airbnb Newsroom | 2024 | https://news.airbnb.com/announcing-our-2024-preferred-software-partners/ |
| Reserve Now, Pay Later is now available worldwide | Airbnb Newsroom | 2026 | https://news.airbnb.com/reserve-now-pay-later-is-now-available-worldwide |
| 2025 Summer Release | Airbnb Newsroom | 2025 | https://news.airbnb.com/airbnb-2025-summer-release |
| 2024 Winter Release: Co-Host Network | Airbnb Newsroom | 2024 | https://news.airbnb.com/airbnb-2024-winter-release |
| 2022 Winter Release (AirCover for Hosts) | Airbnb Newsroom | 2022 | https://news.airbnb.com/product-releases/airbnb-2022-winter-release |
| New anti-party technology in the US and Canada | Airbnb Newsroom | 2022 | https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada |
| An update on our work to crack down on parties | Airbnb Newsroom | 2023 | https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior |
| Pay as a Local | Haile, Shi, Liu et al., Airbnb Tech | 2026 | https://airbnb.tech/payments/pay-as-a-local/ |
| Skipper: Building Airbnb's embedded workflow engine | Gamba, Sergiyenko, Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/skipper-building-airbnbs-embedded-workflow-engine/ |
| Scaling beyond one: data architecture for a multi-product world | Lam, Lamba, Stober, Airbnb Tech | 2026 | https://airbnb.tech/uncategorized/scaling-beyond-one-how-airbnb-evolved-its-data-architecture-for-a-multi-product-world/ |
| Viaduct, Five Years On | Airbnb Tech | 2025 | https://airbnb.tech/infrastructure/viaduct-five-years-on-modernizing-the-data-oriented-service-mesh/ |
| Viaduct 1.0 and the future of Airbnb's data mesh | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/viaduct-1-0-and-the-future-of-airbnbs-data-mesh/ |
| Seamless Istio Upgrades at Scale | Rushy R. Panchal, Airbnb Tech | 2025 | https://airbnb.tech/infrastructure/seamless-istio-upgrades-at-scale/ |
| Scaling Airbnb's identity graph | Zhao, Yang, Jain, Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/scaling-airbnbs-identity-graph-with-a-unified-knowledge-graph-infrastructure/ |
| Embedding-Based Retrieval for Airbnb Search | Abdool et al., Airbnb Tech | 2025 | https://airbnb.tech/ai-ml/embedding-based-retrieval-for-airbnb-search/ |
| Personalizing Airbnb search by learning from the guest journey | Zha et al., Airbnb Tech | 2026 | https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/ |
| The guest journey, updated in real time (Chronon) | Airbnb Tech | 2026 | https://airbnb.tech/ai-ml/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon/ |
| CASTLE: training natural language search before the first real query | Wei et al., Airbnb Tech | 2026 | https://airbnb.tech/ai-ml/castle-training-natural-language-search-before-the-first-real-query/ |
| Academic Publications & Airbnb Tech: 2025 Year in Review | Airbnb Tech | 2026 | https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/ |
| Academic Papers | Airbnb Tech | fetched 2026 | https://airbnb.tech/research/academic-papers/ |
| What COVID did to our forecasting models | Airbnb Tech | 2026 | https://airbnb.tech/data/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock/ |
| How we knew COVID was over | Airbnb Tech | 2026 | https://airbnb.tech/ai-ml/how-we-knew-covid-was-over-and-what-our-models-had-to-unlearn/ |
| Real-time Personalization using Embeddings for Search Ranking at Airbnb | Grbovic, Cheng, KDD | 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb |
| Customized Regression Model for Airbnb Dynamic Pricing | Ye et al., KDD | 2018 | https://www.kdd.org/kdd2018/accepted-papers/view/customized-regression-model-for-airbnb-dynamic-pricing |
| Applying Deep Learning to Airbnb Search | Haldar et al., arXiv / KDD 2019 | 2018 | https://arxiv.org/abs/1810.09591 |
| Improving Deep Learning for Airbnb Search | Haldar et al., arXiv / KDD 2020 | 2020 | https://arxiv.org/abs/2002.05515 |
| Learning To Rank Diversely at Airbnb | Haldar et al., arXiv / CIKM 2023 | 2022 | https://arxiv.org/abs/2210.07774 |
| Optimizing Airbnb Search Journey with Multi-task Learning | Tan et al., arXiv / KDD 2023 | 2023 | https://arxiv.org/abs/2305.18431 |
| Learning to Rank for Maps at Airbnb | Haldar et al., arXiv / KDD 2024 | 2024 | https://arxiv.org/abs/2407.00091 |
| Interleaving and Counterfactual Evaluation for Airbnb Search Ranking | Zhang et al., arXiv / KDD 2025 | 2025 | https://arxiv.org/abs/2508.00751 |
| The Great Migration: from Monolith to Service-Oriented | Jessica Tai, QCon SF / InfoQ | 2018 | https://www.infoq.com/presentations/airbnb-soa-migration/ |
| Airbnb's Migration from Monolith to Services | Reda Hmeid, InfoQ | 2019 | https://www.infoq.com/news/2019/02/airbnb-monolith-migration-soa/ |
| Building Services at Scale at Airbnb: QCon London Q&A | InfoQ | 2019 | https://www.infoq.com/news/2019/03/building-services-airbnb/ |
| Develop Hundreds of Kubernetes Services at Scale with Airbnb | Melanie Cebula, QCon London / InfoQ | 2019 | https://www.infoq.com/presentations/airbnb-kubernetes-services/ |
| How to Tame Your Service APIs: Evolving Airbnb's Architecture | Jessica Tai, QCon Plus / InfoQ | 2021 | https://www.infoq.com/presentations/airbnb-api-architecture/ |
| Distributed Materialized Views: Airbnb's Riverbed | Rafał Gancarz, InfoQ | 2023 | https://www.infoq.com/news/2023/10/airbnb-riverbed-introduction/ |
| Airbnb Open-Sources its ML Feature Platform Chronon | Sergio De Simone, InfoQ | 2024 | https://www.infoq.com/news/2024/04/airbnb-chronon-open-sourced/ |
| Chronon repository README | Airbnb, GitHub | fetched 2026 | https://github.com/airbnb/chronon |
| Handling Double Payments at Airbnb (secondary summary of Orpheus) | Biweekly Engineering | 2023 | https://biweekly-engineering.beehiiv.com/p/handling-double-payments-airbnb-biweekly-engineering-episode-32 |
| Rebuilding Payment Orchestration at Airbnb (excerpt only) | Airbnb Engineering | c. 2021 | https://airbnb.tech/?p=49 |
| Unified Payments Data Read at Airbnb (excerpt only) | Airbnb Engineering | c. 2023 | https://airbnb.tech/?p=147 |
| Experiment Reporting Framework (excerpt only) | Airbnb Engineering | c. 2014 | https://medium.com/airbnb-engineering/experiment-reporting-framework-f3faca569e0c |
| Ep 1: Robert Chang on Scaling Metrics @ Airbnb (Minerva) | dbt Roundup | c. 2021 | https://roundup.getdbt.com/p/ep-1-robert-chang-on-scaling-metrics |
| Airbnb's pricing algorithm and Aerosolve (excerpt only) | PhocusWire | 2015 | https://www.phocuswire.com/Airbnbs-pricing-algorithm-and-Aerosolve-its-open-source-machine-learning-tool |
| Airbnb Host Fees: the 15.5% host-only fee explained | Hostfully | 2026 | https://www.hostfully.com/blog/airbnb-host-fees/ |
| Translation Engine expansion (excerpt only) | Airbnb Newsroom Brazil | 2021 | https://news.airbnb.com/br/airbnb-anuncia-expansao-da-tecnologia-translation-engine/ |
