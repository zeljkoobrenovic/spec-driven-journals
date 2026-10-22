# Research brief: Host and partner tools, guest experience, customer service and messaging

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Airbnb, Booking.com and Expedia Group get the most space because they have published dated primary material (shareholder letters, 10-K filings, developer documentation, engineering posts) on these topics. The book does not endorse their choices.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date, not the fetch date. Live help-centre and API-documentation pages carry no publication date. They are marked **undated, live page** and describe the state on the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (trade press, vendor guide, conference report, third-party summary), not from the company's own documentation. Some of these pages were fetched. They keep this tag because they are secondary.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Partner and host products are renamed and rebuilt often. Agoda's extranet was called YCS for years and became the "Agoda Partner Portal" in August 2026. Airbnb's Translation Engine (2021–22) and its 2020 COVID-19 refund programme describe systems and policies that have since changed. Airbnb's extenuating-circumstances policy has become the Major Disruptive Events policy, and COVID-19 is now explicitly excluded. Each section gives the date of its evidence. Do not describe a source older than about three years in the present tense without checking it.

**Research limitation.** The session shared a web-search quota with other researchers, so research relied on direct fetches wherever possible. As a result:

- **partner.booking.com** pages for Genius and Visibility Booster returned HTTP 403 (sign-in required) or 404. Only the Preferred Partner Programme page could be read. Genius partner terms and Visibility Booster mechanics therefore rest on third-party guides and are tagged WIDELY REPORTED.
- **expedia.com/newsroom** returned HTTP 429 throughout, and the Expedia Partner Central pages on `welcome.expediagroup.com` redirect to a generic landing page. Expedia Partner Central features (Rev+, Property Analytics, messaging) rest on secondary sources. The Expedia virtual-agent volume figures rest on trade press and the 10-K wording.
- **Agoda's consumer pages** (AgodaVIP, AgodaCash, PointsMAX) rendered empty. Agoda loyalty claims are secondary.
- No primary engineering post was found on **Airbnb's messaging platform architecture**, on **Booking.com's or Expedia's contact-centre stack**, or on **Vrbo host tools**. The Airbnb post "Intelligent Automation Platform" returned 404 at the URL found.
- The Airbnb press figure that it "automated 45% of support" comes from a PYMNTS summary that could not be checked against a primary transcript. It is not used as a key number.

**Volatility flags.** ⚠ marks claims likely to change within 12 months, such as product names, programme thresholds, fee levels, feature availability by market, and AI-agent coverage.

---

## PART 1: The two supply sides and the tools they need

### 1.1 Who the "partner" or "host" is

| Property | OTA (hotel-centric) | Hosted stays (Airbnb-style) |
| --- | --- | --- |
| Typical supplier | A hotel, chain or professional property manager with staff | An individual host, a co-host, or a professional manager running many units |
| Primary tool | Extranet (web) + mobile companion app + channel manager / PMS connection | Host app and website (Today, Calendar, Listings, Messages, Earnings) + PMS via API for professionals |
| Unit of inventory | Room type × rate plan × date | One listing (usually one unit) × date |
| Who talks to the guest | Front desk / reservations team, often via PMS or guest-messaging tools | The host or co-host personally, mostly in-app |
| Commercial levers | Commission tiers, visibility programmes, discounts for loyalty members, PPC ads | Price, quality badges (Superhost, Guest Favorite), cancellation policy, reviews |
| Onboarding | Contract + extranet registration, often with an account manager | Self-serve listing creation + identity verification |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis. The sources below support each row.

- Booking.com listed about **4.4 million properties** at 31 December 2025: about **500,000 hotels, motels and resorts** and about **3.9 million homes, apartments and other unique places to stay**, in over 220 countries and territories and over 40 languages [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]. Booking.com is therefore an OTA with a majority-homes catalog by count, so its partner tooling has to serve both shapes.
- Expedia Group had about **3.6 million lodging properties** at the end of 2025, including about **2.4 million** online-bookable alternative accommodations through Vrbo and about **1.2 million** hotels and alternative accommodations through its other brands [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13].
- Airbnb describes "a global community of over 5 million hosts who have welcomed over 2.5 billion guest arrivals" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- Booking.com's engineering blog defines the partner simply: "Every property on Booking.com is listed by a partner — the person or business that owns or manages the place to stay." It adds that **self-managed** partners "sign up, list their property, and run it entirely on their own, without a dedicated account manager" [VERIFIED: https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7, published 2026-10-19].

**OTA vs hosted stays.** The OTA partner is an organisation with systems (a PMS, channel manager or revenue-management system) and staff. The extranet is often a fallback or a configuration console, while day-to-day inventory comes over connectivity APIs. The hosted-stays host is often one person on a phone, and the host app *is* the operating system for their business. Both marketplaces now run a long tail of self-serve suppliers and a head of professional suppliers who integrate by API. The architecture has to serve both through one set of domain services. [ASSUMPTION/JUDGEMENT]

### 1.2 Professional managers vs individual hosts

- Airbnb's API documentation describes a **Homes API** to "create, update, and manage" listing descriptions, amenities and photos, retrieve and manage reservations, and run "Sync Availability Checks" that confirm availability in real time during the booking flow. It also lists Partner API tools for bulk operations and an Error Dashboard [VERIFIED: https://developer.withairbnb.com/, undated, live page]. The landing page does not describe eligibility terms.
- Airbnb's help centre explains that for PMS-connected hosts, "Airbnb sends reservation details to the connected PMS", the PMS creates the door code, and Airbnb relays it to the guest. In that set-up the **PMS owns the lock**, so Airbnb cannot see battery or offline status [VERIFIED: https://www.airbnb.com/help/article/4163, undated, live page]. This is a clean example of the integration boundary: the professional's system is the source of truth, and the marketplace is a relay.
- In October 2025 Airbnb "migrated property management software ("PMS") hosts on our split fee structure (where hosts paid a 3% fee and guests paid a separate service fee) to a single 15.5% single service fee" [VERIFIED: https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf, published 2025-11-06]. Airbnb identifies PMS-connected hosts as a distinct commercial segment. ⚠
- Airbnb ran a **Preferred Software Partner** programme for connectivity vendors from 2018, with Preferred and Preferred+ tiers. Vendors report criteria such as API connection success, feature coverage, feature adoption and technical quality [WIDELY REPORTED: https://www.hostaway.com/blog/hostaway-achieves-preferred-partnership-status-with-airbnb/, 2024; https://hotelrunner.com/en/news/awards-recognitions/hotelrunner-is-once-again-titled-as-preferred-software-partner-by-airbnb, 2024]. Vendor-written; not confirmed by Airbnb in this session.
- Airbnb's Co-Host Network launch compared co-hosts' average rating (**4.86**) with "large property management companies" (**4.62**). The latter were defined as managers with over 30 active listings globally as of 30 September 2024 [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb, published 2024-10-16]. Airbnb publicly favours individual-style hosting over large-PM supply in its quality messaging.

**OTA vs hosted stays.** On an OTA, the "professional" is the default, and connectivity standards (OpenTravel / HTNG-style messages through channel managers) are the main path. On Airbnb, the API is gated to approved software partners. The marketplace keeps product features (smart-lock relay, messaging, pricing tips) inside its own app and decides which of them a PMS can drive. [ASSUMPTION/JUDGEMENT]

---

## PART 2: Hotel partner extranets and their mobile companions

### 2.1 Booking.com extranet and Pulse

- **Pulse** is Booking.com's free partner app for iOS and Android. It links to an existing extranet account, and the page presents it as a mobile complement: the extranet remains the full management tool [VERIFIED: https://www.booking.com/propertyapp.en-gb.html, undated, live page].
- Pulse lets partners reply to guest messages and requests "before, during, and after a stay", set auto-replies to common questions, and use message templates in **43 languages**. It also sends real-time alerts (new bookings, reviews, guest requests, sold-out dates), lets partners update room availability, reply to reviews and view invoices [VERIFIED: same URL].
- [ASSUMPTION/JUDGEMENT] Architecturally, Pulse is a second client of the same partner back-end that the extranet and the Connectivity APIs use. Any write it makes (for example, closing availability) must reconcile with the partner's channel manager, which may overwrite it on its next push. Chapter writers should present "last writer wins vs source-of-truth ownership" as the core design problem of a multi-client partner back-end.

### 2.2 Expedia Partner Central

- Expedia's partner blog describes two Partner Central visibility products. **Accelerator** is pay-per-stay: the partner sets a compensation rate, is charged only when a guest completes a stay in the chosen timeframe, can target date ranges or run "always-on", and can "View the potential impact on your sort order before you commit." **TravelAds Sponsored Listings** is pay-per-click with a daily budget and bidding strategy across "200+ websites" [VERIFIED: https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters, published 2025-08-22 (updated)].
- The same page states (Expedia first-party data, 2024) that properties in the **top 20 sort positions** on Expedia and Hotels.com receive **80% of clicks**, and (first-party, 2025) that properties running Accelerator saw **20% higher gross booking value** and **20% more net room nights** [VERIFIED: same URL]. Vendor claims, no published methodology.
- Partner Central also offers **Rev+**, a free revenue-management view with a price calendar, market demand score and competitive price grid. Expedia picks 5–19 competitor properties. **Property Analytics** reports conversion (transactions to property-page views) and guest value against the prior year and the comp set. Messaging supports templates, scheduled messages and filters [WIDELY REPORTED: https://hospitalitytech.com/expedia-launches-revenue-management-tool-rev, 2019; https://www.lodgify.com/guides/expedia/partner-central/, 2025]. ⚠ Evidence-age warning: Rev+ launch coverage dates from about 2019. Sources disagree on the forward window (90 vs 365 days).
- At EXPLORE 2024 Expedia announced partner-facing **Guest Experience** insights that flag recurring negative review sentiment with recommendations, **Fraud Prevention as a Service**, and a Vrbo **Seasonal Cancellation Policy** [VERIFIED: https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx, published 2024-05-14].

### 2.3 Agoda YCS → Agoda Partner Portal

- On 17 August 2026 Agoda announced the **Agoda Partner Portal**, "formerly known as" the **Yield Control System (YCS)**. It is a unified management platform with revenue-management tools (Agoda Dynamic Rates, "ADR+"), promotion and rate-plan controls, AI review summaries, and "Agoda Intelligence" suggestions for dates up to 90 days ahead, which partners must verify. It also adds a comp-set benchmark that flags periods needing attention, multi-property calendar views, and mobile handling of bookings, availability, promotions and guest messages. KakaoTalk booking notifications are offered for South Korean motels, and WhatsApp and WeChat are planned [VERIFIED: https://kyodonewsprwire.jp/release/202608174214, published 2026-08-17]. ⚠ New name; older documentation and PMS vendors still say "YCS".
- A PMS vendor's help documentation describes YCS as the back-office extranet for rates and availability, photos, room set-up and reservations, and says single exclusive-use units go on **Agoda Homes** while properties with two or more units go on YCS [WIDELY REPORTED: https://nightsbridge-6.screenstepslive.com/a/1973011-how-to-navigate-within-your-agoda-ycs-partner-extranet, undated]. Agoda historically split hotel and homes supply into separate onboarding paths. Re-check before stating it in the present tense.

### 2.4 Partner performance analytics: what the extranet shows

| Signal | Booking.com | Expedia | Agoda |
| --- | --- | --- | --- |
| Ranking position / sort impact | Programme badges and ranking boost (Preferred, Genius) | Preview of sort-order impact before buying Accelerator | "Average boosted ranking" tracked per AGP campaign |
| Comp-set benchmark | Not verified in this session | Rev+ competitive price grid; comp set of 5–19 | Comp-set comparison flags weak periods |
| Review analytics | Reply to reviews in Pulse | Review-sentiment insights (2024) | AI review summaries (2026) |
| Paid-visibility ROI | Not verified | Accelerator / TravelAds reporting | ROAS, room nights, impressions, revenue per campaign |

Sources: the sections above, plus Agoda Growth Program metrics [VERIFIED: https://www.partnerhub.agoda.com/?p=95313, published 2025-02-19].

[ASSUMPTION/JUDGEMENT] Every OTA extranet exposes a **partner-facing view of the ranking function**: either a preview of the effect of paying more, or a performance score that gates a programme. This creates an architectural obligation. The ranking system must be able to explain or simulate its output for a single property, and partner analytics must be served from the same features that ranking uses. Otherwise partners see numbers that disagree with the search results they observe.

**OTA vs hosted stays.** OTAs monetise visibility directly: partners can buy rank with commission (Visibility Booster, Accelerator, AGP) or clicks (TravelAds, Booking Holdings Sponsored Listings). Airbnb has no published pay-for-rank product for stays. Its levers are price, quality badges and policy choices, and its host analytics focus on earnings, price tips and reviews (Part 4). This is the single largest product difference between the two partner experiences.

---

## PART 3: Partner programmes and commercial levers (OTA)

### 3.1 Booking.com Preferred Partner Programme

- Booking.com describes the programme as "an exclusive programme that provides greater visibility and recognition to a limited number of properties in each area that deliver superior stay experiences." Preferred partners "appear higher in search results thanks to a boost in search views and a 'thumbs-up' badge", and "on average, Preferred partners collect up to 20% more bookings" [VERIFIED: https://partner.booking.com/en-gb/solutions/preferred-partner-programme, undated, live page].
- Eligibility: "Only 30% of partners in a particular geographic area who meet all the requirements can be Preferred partners at any given time." Performance and guest review scores matter both for joining and for keeping status. The specific criteria are shown only inside the extranet. For properties in wide-parity or narrow-parity countries, the partner must "provide competitive prices on our platform". This does not apply in no-parity countries, "including all countries in the European Economic Area" [VERIFIED: same URL].
- The page does not state the commission uplift. Third-party guides put Preferred at about **3 percentage points** above base commission (total about 18%) and **Preferred Plus** at about **8 points** [WIDELY REPORTED: https://wise.com/us/blog/booking-com-host-fees, 2025; https://www.hostaway.com/blog/booking-preferred-partner/, 2024]. ⚠
- On 22 April 2026 the Italian competition authority (AGCM) opened an investigation into Booking.com over Preferred Partner and Preferred Plus. It is concerned that selection "appears to be driven largely by criteria that favour accommodation providers paying higher commissions to Booking.com", which could mislead consumers into thinking participants "offer better overall value for money", and "could even lead consumers to book accommodation that is, on average, more expensive" [VERIFIED: https://en.agcm.it/en/media/press-releases/2024/4/PS13115, published 2026-04-22]. This is an investigation, not a finding. ⚠
- [ASSUMPTION/JUDGEMENT] For architects, the AGCM case is the reason a commercial boost must be a **separate, auditable term** in the ranking pipeline, logged per impression, and not blended invisibly into a quality score. Regulators increasingly ask platforms to show which part of a rank was paid.

### 3.2 Booking.com Visibility Booster

- Third-party guides describe Visibility Booster as a pay-per-booking tool that lets a partner "voluntarily increase your commission percentage for specific dates" in exchange for a ranking boost while it is on. Booking.com sets the required rate by destination, season and audience [WIDELY REPORTED: https://wise.com/us/blog/booking-com-host-fees, 2025; https://www.hostaway.com/get-more-bookings-on-booking-com, 2024]. The official page returned 404 in this session. ⚠
- A revenue-management vendor warns that, on OTAs generally, raising commission for a date range can also apply to bookings already received for those dates [WIDELY REPORTED: https://www.mirai.com/blog/visibility-boosters-and-marketing-in-otas-a-guide-to-understanding-choosing-and-comparing-each-option/, 2023]. Not verified for Booking.com specifically.

### 3.3 Booking.com Genius (partner side)

- Booking Holdings lists among its 2025 priorities "expanding Booking.com's Genius loyalty program across verticals and continuing to improve loyalty programs across our brands to provide a more personalized experience for consumers and incremental value to partners" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18].
- Partner-side mechanics come from third-party guides. Participation is opt-in. Third-party guides describe a review-score floor (often cited as 7.5) and a minimum 10% discount for Genius level 1 members, with optional extras (breakfast, upgrades) or deeper discounts for levels 2–3. In return the partner gets a Genius badge and a ranking boost [WIDELY REPORTED: https://travelnest.com/news-and-insights/boost-visibility-and-increase-bookings-with-booking-com-genius-program, 2024; https://hotels.pricelabs.co/blog/genius-loyalty-program-booking-com/, 2024]. The partner Genius page needs a sign-in (403). ⚠ Thresholds vary between guides.
- Traveller levels: guides agree on three levels with progression by number of stays in two years (commonly cited as 5 bookings for level 2 and 15 for level 3) [WIDELY REPORTED: https://thepointsguy.com/loyalty-programs/booking-com-genius-loyalty-programme/, 2024]. ⚠

[ASSUMPTION/JUDGEMENT] Genius is a **partner-funded** loyalty programme. The discount is a rate-plan modifier that the partner opts into, so it lives in the rate and pricing domain (a member-only rate condition evaluated at search and checkout against the traveller's level), not in a separate rewards ledger. Compare One Key (3.5), where the platform funds a currency held in a ledger.

### 3.4 Expedia Accelerator and TravelAds

See 2.2 for mechanics. Additional points:

- Expedia's media arm markets TravelAds as connecting advertisers to travellers across 200+ travel sites and apps. Options include automated bidding, Accelerator as a pay-per-stay option "for a chosen check-in window", and co-op campaigns where brands in one region pool budgets [WIDELY REPORTED: https://www.hospitalitynet.org/news/4123355.html, 2024 (sponsored content by Expedia Group Media Solutions)].
- At EXPLORE 2024 Expedia said its travel media network reaches 200 booking sites in 70+ countries, and its B2B network includes over 60,000 partners [VERIFIED: https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx, published 2024-05-14].

### 3.5 Agoda Growth Program (AGP)

- AGP is Agoda's "long-term marketing solution". Joining properties get a **Preferred Partner badge** on search and property pages, a ranking boost, and increased Agoda spend on their behalf, "up to 90%" more on metasearch and "up to 80%" more on pay-per-click ads [VERIFIED: https://www.partnerhub.agoda.com/?p=95313, published 2025-02-19].
- Cost is an incremental commission called the **cost per booking**: Basic 10%, Standard 12%, Premium 15%. It is deducted from each booking payout or invoiced monthly on departed room nights. A monthly post-paid fee is available to properties that want to protect their average daily rate. There is a free two-week trial and a mandatory 90-day participation period [VERIFIED: same URL]. ⚠
- Agoda reports (2024, Standard plan averages, "not guaranteed") 1.5× impressions, +37% revenue and +42% net room nights [VERIFIED: same URL]. Vendor claims.

| Programme | Platform | Partner pays | Partner gets | Gate |
| --- | --- | --- | --- | --- |
| Preferred / Preferred Plus | Booking.com | Higher commission (≈ +3 / +8 pts, secondary) | Ranking boost + thumbs-up badge | Top 30% per area meeting performance, review and (outside EEA) price-competitiveness criteria |
| Visibility Booster | Booking.com | Higher commission on chosen dates | Temporary ranking boost | Opt-in |
| Genius | Booking.com | Discount to member travellers | Badge + ranking boost + member demand | Opt-in, review-score floor (secondary) |
| Accelerator | Expedia | Compensation per completed stay | Sort-order boost for dates | Opt-in; sort-impact preview |
| TravelAds | Expedia | Cost per click | Sponsored placement | Budget |
| AGP | Agoda | +10–15% cost per booking | Preferred badge, ranking boost, extra Agoda ad spend | Opt-in; 90-day minimum |

**OTA vs hosted stays.** None of these has a published equivalent for Airbnb stays. Airbnb's nearest levers are non-monetary: quality-gated badges (Superhost, Guest Favorite), host-chosen discounts and cancellation policies, and price tips. [ASSUMPTION/JUDGEMENT] That keeps Airbnb's ranking free of paid terms but puts more weight on the integrity of the quality signals (reviews, cancellations, customer-service issue rates).

---

## PART 4: Host tools on a hosted-stays marketplace

### 4.1 The host app surface

- Airbnb's 2025 10-K describes a "robust suite of tools to successfully manage their listings, including scheduling, merchandising, integrated payments, community support, host protections, pricing tools, and feedback from reviews". In 2025 these were updated with cancellation-policy changes, "better pricing tools and price tips, and a refreshed messages tab" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- The **2023 Winter Release** introduced a **Listings tab** with a listing editor (amenities, sleeping arrangements, arrival guide), claiming "Listings with more details can get up to 20% more bookings". It also introduced an **AI-powered photo tour** that groups photos into 19 room types, a redesigned earnings dashboard, two new co-host payout options, and, announced for 2024, prices shown with service fees included plus a price-comparison tool in the calendar [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2023-winter-release/, published 2023-11-09].
- The **2024 Winter Release** (October 2024) added more than 20 host upgrades, including price tips based on similar local listings, customisable quick-reply templates, and an earnings dashboard with custom reports [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb, published 2024-10-16].
- A third-party breakdown of the 2025 Summer Release describes the redesigned host app with five tabs: Today, Calendar, Listings, Messages, Menu [WIDELY REPORTED: https://www.rentalscaleup.com/whats-new-for-airbnb-hosts-in-the-2025-summer-release-tools-built-for-one-listing-hosts/, 2025]. ⚠

[ASSUMPTION/JUDGEMENT] Price tips that compare with "similar local listings" need a host-facing read path into the same comparable-listing and demand features that power pricing suggestions. That is a privacy-sensitive aggregate (no single competitor's price should be exposed) and should be served from precomputed, k-anonymised aggregates.

### 4.2 Superhost

The current criteria (undated, live page), assessed every three months over the trailing 12 months [VERIFIED: https://www.airbnb.com/help/article/829, undated, live page]:

| Criterion | Threshold |
| --- | --- |
| Stays | ≥ 10 reservations, **or** 3 reservations totalling ≥ 100 nights |
| Response rate | Reply to 90% of new messages within 24 hours (declining does not hurt) |
| Cancellation rate | < 1%, excluding Major Disruptive Events and other valid reasons |
| Overall rating | ≥ 4.8 |

- Quarterly assessments start on 1 January, 1 April, 1 July and 1 October. The badge may take up to a week to appear, and ratings published after a period ends count toward the next one [VERIFIED: same URL].
- [ASSUMPTION/JUDGEMENT] Superhost is a **batch-computed, periodically recomputed credential**, not a live score. That is a deliberate choice: hosts get stability for a quarter, and the computation can run over a consistent snapshot of reviews, messages and cancellations. The late-review rule ("published after the period counts toward the next") shows that the snapshot is keyed on review publication time, not stay time.

### 4.3 Guest Favorites (November 2023) and the hosting quality system

- On 9 November 2023 Airbnb launched **Guest Favorites**, "2 million most-loved homes" selected from "ratings, reviews, and reliability data from over half a billion trips". The criteria are an average rating above 4.9, high marks across check-in, cleanliness, accuracy, communication, location and value, and host cancellations plus quality-related customer-service issues below 1% on average. "Nearly two-thirds" come from Superhosts. They carry a badge and are filterable [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2023-winter-release/, published 2023-11-09].
- Since launch, Guest Favorite listings have had "nearly 500 million nights booked" (Q3 2025). Under the "updated hosting quality system" launched in 2023, Airbnb has removed "over 550,000 listings", alongside a year-over-year reduction in customer-service issue rates and chargeback rates [VERIFIED: https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf, published 2025-11-06]. The Q2 2025 letter gave "over 400 million nights" and "over 500,000 listings" removed [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm, published 2025-08-06].
- [ASSUMPTION/JUDGEMENT] Guest Favorites is a **listing-level** credential, unlike Superhost, which is host-level. It fuses review data with **customer-service case data** (quality-related issues), so the support system's case taxonomy becomes a ranking input. The case-reason labels therefore need the same data-quality discipline as reviews.

**OTA vs hosted stays.** Booking.com's Preferred badge combines quality with commission and price parity (3.1). Airbnb's Superhost and Guest Favorite badges are quality-only. The data feeding them (response rate, cancellations, support issues) comes from the messaging and support systems, which makes those systems ranking-critical.

### 4.4 Co-hosting and the Co-Host Network (October 2024)

- Launched 16 October 2024 with **more than 10,000 co-hosts across 10 countries** (Australia, Brazil, Canada, France, Germany, Italy, Mexico, Spain, UK, US). Recommendations are ranked by an algorithm using **more than 80 factors**. **73%** of co-hosts are Superhosts, and **84%** help manage a Guest Favorite. Hosts can message a co-host in-app, give calendar access, and share payouts [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb, published 2024-10-16].
- By Q2 2025 the Co-Host Network "supports over 100,000" listings [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm, published 2025-08-06].
- The 2025 10-K describes co-hosts as "experienced hosts who provide personalized support based on the hosts' needs, from listing setup to managing bookings and communicating with guests" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- New co-hosts must be identity-verified like primary hosts [VERIFIED: https://www.airbnb.com/help/article/1237, undated, live page].
- An Airbnb help page lists the network in 13 markets (adding Japan, Puerto Rico, South Korea) [WIDELY REPORTED: https://www.airbnb.com/resources/hosting-homes/a/join-the-co-host-network-629, 2025]. ⚠

[ASSUMPTION/JUDGEMENT] Co-hosting forces a **delegated-permission model** onto a domain originally built for one owner per listing: per-listing roles (calendar, messaging, pricing, payouts), split payouts to several payees (with tax reporting for each), and a messaging inbox where host, co-host and guest share one thread. The 2023 release already mentioned "two new Co-Host payout options" and Inbox features "to let Hosts and Co-Hosts communicate". The data model needs a listing-team concept a decade after launch.

**OTA vs hosted stays.** OTA extranets have always had multi-user accounts with role permissions, because hotels have staff. Hosted-stays platforms add delegation later and must retrofit it into payouts, tax and trust (each delegate verified).

### 4.5 Host onboarding and verification

- "Every host, new co-host, and booking guest must be identity verified to use our platform." A host's listing is not published until verification is complete. Methods include checks against third-party sources, a government-ID photo, a selfie (not shown to others), optional facial recognition, and NFC chip verification in some countries. Processing typically takes under one hour. Hosts operating as a business, and EU or Brazilian residents earning rental income, may need to verify more (address, citizenship, taxpayer data). The page states the process "doesn't guarantee that someone is who they say they are" [VERIFIED: https://www.airbnb.com/help/article/1237, undated, live page].
- Airbnb conducts background checks "in the United States and India for certain users" and screens against sanctions watch lists. It notes "We do not verify all listings for safety" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- **Ask a Superhost** (2021) matched prospective hosts with experienced Superhosts for one-to-one advice. Over 60,000 prospective hosts had used it by November 2021, and it expanded to 30+ languages [VERIFIED: https://news.airbnb.com/2021-winter-release/, published 2021-11-09]. Evidence age: 2021. The Co-Host Network has since become the main human-assistance channel.
- **Booking.com partner onboarding.** Self-managed partners get stuck in registration "due to its length, unfamiliar terminology, and business-critical decisions they must make before they've learned how the platform works." Booking.com built a RAG chatbot embedded in the registration flow, grounded "strictly in the partner help center content". It uses three purpose-specific retrievers (general help, registration process, and a **templated-answers retriever** that returns pre-approved static answers for legally restricted questions). It was shipped as an A/B test against registration-funnel metrics. On about 2,000 evaluated conversations, the judge-assessed task-completion score rose **1.33×**, and refusals fell [VERIFIED: https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7, published 2026-10-19].
- Booking.com's partner help-centre navigation includes "Verifying your property's location" as an onboarding topic [VERIFIED: https://partner.booking.com/en-gb/solutions/preferred-partner-programme, undated, live page (navigation menu)]. The verification procedure itself was not read.

**OTA vs hosted stays.** OTA onboarding verifies the **business and its location** (contract, bank details, address). Hosted-stays onboarding verifies the **person** (ID, selfie, background checks) and in some places the registration number required by short-term-rental rules (see the regulation brief). The two converge for professional managers and for Booking.com's homes segment.

### 4.6 Host earnings statistics

- A summary of Airbnb's 2025 US economic-impact report says the typical US host earned about **USD 15,600** in 2025, and that hosts in census tracts with no hotels earned more than USD 9.9 billion, nearly 40% of US host earnings [WIDELY REPORTED: https://indiaoutbound.info/?p=216130, 2026]. Not verified against Airbnb's own page. ⚠
- A figure of about USD 14,000 for 2023 circulates on statistics aggregator sites [WIDELY REPORTED: https://ipropertymanagement.com/research/airbnb-statistics, 2024]. Treat both figures as low-confidence until checked against news.airbnb.com.

---

## PART 5: Turnover, check-in and on-property operations

### 5.1 Smart locks and digital keys

- On 21 August 2024 Airbnb made smart-lock integrations available to all hosts in the US and Canada for compatible **Schlage, August and Yale** locks. The integration generates a unique door code per reservation and sends it to guests before the stay. The code is "only active for the duration of a stay" and updates if the host changes check-in or checkout times. Hosts are notified when a guest checks in and when a lock goes offline or runs low on battery. During Early Access, smart-lock stays averaged a **4.96** check-in rating (as of 1 February 2024) [VERIFIED: https://news.airbnb.com/smart-lock-integrations-available-to-all-us-and-canada-hosts, published 2024-08-21]. ⚠ Market and brand coverage changes.
- For PMS-managed locks, the PMS generates codes and Airbnb relays them. Only the first lock per listing is shared, so hosts must provide backup entry instructions. The PMS may send a non-expiring backup code [VERIFIED: https://www.airbnb.com/help/article/4163, undated, live page].
- [ASSUMPTION/JUDGEMENT] The smart-lock integration ties three lifecycles together: the **reservation** (dates and changes), the **access credential** (code validity window), and the **device** (online state, battery). The correct design treats the credential as a derived resource with its own state machine, driven by reservation events (created, altered, cancelled, checked out) and reconciled against device state. A missed alteration event means a locked-out guest at midnight. That is why both paths require a backup entry method.

### 5.2 Check-in instructions and the arrival guide

- The 2023 Listings tab made the **arrival guide** editable alongside amenities [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2023-winter-release/, published 2023-11-09].
- The **Trips tab** redesign (2021) shows an arrival countdown, check-in details, and current and upcoming reservations [VERIFIED: https://news.airbnb.com/2021-winter-release/, published 2021-11-09]. Evidence age: 2021.
- **Verified Wifi** (2021) lets hosts test their connection in the app and show the verified speed to guests [VERIFIED: same URL].

### 5.3 Cleaning and turnover

- AirCover for Hosts includes "deep cleaning protection" and "pet damage protection" alongside property-damage protection up to USD 3 million per stay and liability cover up to USD 1 million per occurrence [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12]. ⚠ Limits change. (The 2020 10-K cited USD 1 million damage protection, which shows how fast these figures move.)
- The Co-Host Network release lists cleaning among the tasks a co-host can take on: "Whether it's setting up a listing, welcoming guests, or cleaning, a co-host can help" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm, published 2025-08-06].
- [ASSUMPTION/JUDGEMENT] No primary source was found describing a marketplace-run cleaning-scheduling system. On both marketplace types, turnover scheduling (cleaner assignment, checklists, linen) lives in the PMS or in specialist tools that subscribe to reservation events. The marketplace's job is to emit reliable, ordered reservation and alteration events and to accept blocked dates back. Chapter writers should present turnover as an **ecosystem integration**, not a core marketplace service.

**OTA vs hosted stays.** In a hotel, check-in, keys and housekeeping are the hotel's own operations (PMS, key-card system, housekeeping module), and the OTA is out of the loop after booking. On hosted stays the marketplace participates in arrival: it delivers check-in instructions and door codes, and it provides AirCover-style remedies when check-in fails (6.2). On-property failures therefore become marketplace support contacts.

---

## PART 6: Guest experience

### 6.1 Planning: wishlists, flexible search, AI planning

- Airbnb's flexible-search feature, "I'm (even more) Flexible", was extended in 2021 to search up to 12 months ahead and had been used more than 500 million times [VERIFIED: https://news.airbnb.com/2021-winter-release/, published 2021-11-09]. Evidence age: 2021.
- Booking.com announced GenAI consumer features on 30 October 2024: **Smart Filter** (natural-language-to-filters), **Property Q&A** (answers from listing details, reviews and photos), and **Review Summaries** (in testing). Its **AI Trip Planner** launched in the US in June 2023 [VERIFIED: https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/, published 2024-10-30].
- Booking.com's **AgentHub** platform supports agents across "Discover & Plan" (trip planner), "Search & Book" (natural-language search, smart filtering, automated property descriptions) and "Cross-Sell & Trip Management" (car-rental assistant and "customer support chatbot"). Every interaction is traced with OpenTelemetry, evaluated with LLM-as-judge, and guarded against prompt injection and PII leakage [VERIFIED: https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50, published 2026-10-02].
- Wishlists: no primary source on wishlist architecture was found in this session. [ASSUMPTION/JUDGEMENT] Wishlists are a strong implicit-preference signal for ranking and a re-engagement channel (price-drop and availability alerts). Treat them as a user-owned collection referencing listings, with a fan-out notification job keyed on listing changes.

### 6.2 Trip itinerary, in-stay support and AirCover for guests

- AirCover for guests "provides support for serious issues with a booking or during a stay, including host cancellations, inability to check-in, inaccurate listings, and a 24-hour safety support line" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- Airbnb's trust system includes reviews, account protection, risk scoring, secure payments, watchlist and background checks in certain jurisdictions, an urgent safety line, a **24/7 neighbourhood support line**, anti-party technology and a guest refund policy [VERIFIED: same URL].
- Expedia's EXPLORE 2024 release added "Get Help Fast" (an updated help centre) and **self-service booking management** for changes, cancellations and air-credit redemption on Expedia and Hotels.com [VERIFIED: https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx, published 2024-05-14].
- Expedia launched **Romie**, an AI travel assistant, in alpha on EG Labs in May 2024 [VERIFIED: same URL]. A 2026 secondary report says Romie was later discontinued, and that Expedia's product chief named the main problem as keeping traveller trust when chatbot answers were not grounded in accurate, real-time inventory and reservation data [WIDELY REPORTED: https://letsdatascience.com/news/expedia-group-shares-ai-chatbot-lessons-learned-239f348a, 2026]. Low-confidence secondary; re-verify. ⚠

### 6.3 Accessibility

- **Accessibility Review** (2021): hosts submit photos of accessibility features, and "a specialized team of Airbnb agents" reviews them manually. By November 2021 agents had confirmed **100,000 accessibility features across 25,000 homes** [VERIFIED: https://news.airbnb.com/2021-winter-release/, published 2021-11-09].
- Current help-centre text: guests can filter home search by "any combination" of accessibility features, and experiences and services by mobility, communication and sensory features. Hosts must accept service animals even when they do not accept pets [VERIFIED: https://www.airbnb.co.nz/help/article/2166, undated, live page]. Airbnb's accessibility page says stays hosts must submit at least one clear photo per feature, which a specialised team reviews manually, and that Airbnb aims to conform to WCAG 2.1 Level AA [VERIFIED: https://www.airbnb.com.sg/accessibility, undated, live page].
- **Adapted** category: minimum requirements are step-free access to the home and to at least one bedroom and one bathroom, plus at least one bathroom accessibility feature. Matterport provides free 3D scans to help hosts show features (not a criterion). Over 1,000 Paris-region listings had step-free features ahead of the 2024 Paralympics [WIDELY REPORTED: https://www.paralympic.org/news/airbnb-paris-region-has-over-1000-listings-step-free-accessibility-features, 2024].
- Booking.com's Review Summaries were pitched as surfacing what matters to each traveller, "whether that is parking availability or wheelchair accessibility" [VERIFIED: https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/, published 2024-10-30].

[ASSUMPTION/JUDGEMENT] Accessibility attributes are **claims that need evidence**, unlike ordinary amenities. Airbnb's design (photo per feature, manual review, verified-only filtering) creates a moderation workflow and an evidence store linked to each attribute, with a review state. For hotels the attribute comes from the partner's content feed and is rarely verified per room. That asymmetry is worth a sidebar.

**OTA vs hosted stays.** Hotel accessibility is typically a room-type attribute in a content feed (often mapped from OpenTravel or HTNG codes), and the hotel is legally responsible. Hosted-stays accessibility is per-unit, host-asserted and platform-verified, because there is no professional operator to hold accountable.

### 6.4 Loyalty

| Programme | Funded by | Structure | Evidence |
| --- | --- | --- | --- |
| Booking.com **Genius** | Partners (discounts, perks) | 3 levels by stays in 2 years | 10-K mention [VERIFIED]; mechanics secondary |
| Expedia Group **One Key** | Expedia Group (OneKeyCash), plus advertiser-funded OneKeyCash from 2024 | Blue / Silver / Gold / Platinum by trip elements per year (5 / 15 / 30) | [VERIFIED] below |
| **AgodaVIP**, AgodaCash, PointsMAX | Agoda / partners | Silver after two bookings in two years; airline-points earn via PointsMAX | Secondary |
| Airbnb | No points programme | Quality badges instead | [ASSUMPTION/JUDGEMENT] |

- **One Key** launched in the US in July 2023 across Expedia, Hotels.com and Vrbo, with "more than 168 million members" across the combined programmes. It uses a single currency, OneKeyCash. Qualifying "trip elements must be worth $25 or more in USD". The release says it "marks the first time a major online vacation rental platform will have a loyalty program" [VERIFIED: https://www.hospitalitynet.org/news/4117344.html, published 2023-07-18 (company press release, reprinted)].
- Expedia rolled One Key out in the UK in 2024 and in 2025 migrated "the majority of Expedia Rewards members" to it. Expedia also migrated the Hotels.com and Vrbo front-end stacks onto the Brand Expedia stack in 2023 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13].
- In May 2024 Expedia added **Advertiser-Funded Loyalty**, which lets destination partners fund OneKeyCash for travellers booking hotels [VERIFIED: https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx, published 2024-05-14].
- AgodaVIP starts at Silver after two bookings in two years. PointsMAX (since 2016) lets members earn points in existing airline programmes such as KrisFlyer and Asia Miles [WIDELY REPORTED: https://www.pointhacks.com.au/agoda-pointsmax/, 2025]. ⚠

[ASSUMPTION/JUDGEMENT] One Key is the cleanest example of loyalty as **platform consolidation**. A single currency across three brands needs a shared identity, a shared ledger, and (per the 10-K) a shared front-end stack. The ledger has payments-grade requirements: accrual on stay completion, reversal on cancellation, expiry, and multi-currency valuation.

**OTA vs hosted stays.** Vrbo was the first major vacation-rental platform with a points programme (2023). Airbnb has none and relies on quality badges and price transparency. Earning on a one-unit host's booking raises a question hotels never had: who funds the reward when the "supplier" is a household? Expedia answered "the platform".

---

## PART 7: Guest–host and guest–property messaging

### 7.1 Booking.com Connectivity Messaging API (for PMS and channel managers)

- The API lets properties "communicate with their guests": retrieve conversations and messages, send and reply, upload and download attachments, tag conversations as "no reply needed" and tag messages as read [VERIFIED: https://developers.booking.com/connectivity/docs/messaging-api/understanding-the-messaging-api, undated, live page].
- **Messaging windows.** Properties can message "From the time of booking until 7 days after the guest checkout", or until 7 days after cancellation. If the guest writes, "the property gets an additional 14-day window to reply". Guests can message "till 66 days after the checkout" [VERIFIED: same URL].
- **Self-service requests** (API v1.2): seven structured types (check-in/out time, date change, cancel for less, parking, bed preference, extra crib, extra bed). Date change and cancel-for-less "require response via the Extranet", and "Sending a message through the API will deactivate the property's ability to respond via the extranet" [VERIFIED: same URL]. This is an explicit **single-channel-of-reply** rule between API and extranet.
- **Redaction.** Messages flagged for phishing are redacted ("This message was deleted"), attachments are removed, and from v1.3 an `is_redacted` attribute exposes it [VERIFIED: same URL].
- **Integration pattern.** Partners poll. Those that store messages "Periodically retrieve messages from the queue". Those that do not "Periodically retrieve conversation again". The conversation list is ordered by most recent activity. Partners are advised to tag messages as read "to inform the guest" [VERIFIED: https://developers.booking.com/connectivity/docs/messaging-api/use-cases-and-best-practices, undated, live page]. No polling frequency is published.
- **Pre-reservation messaging** (Request to Book): enabled by the `messaging_api_rtb_enabled` flag. Each booking request creates a conversation that persists into the confirmed reservation. Attachments are rejected (HTTP 400), contact-information sharing is not allowed, labels are disabled, and at the time of fetch only iOS guests could use it [VERIFIED: https://developers.booking.com/connectivity/docs/request-to-book/pre-reservation-messaging, undated, live page]. ⚠
- **Demand API messaging** is a different product for affiliates. It lets affiliates send guest messages to properties "on their behalf" and retrieve replies via `/3.2/messages/`. `/messages/latest` returns up to 100 messages and requires confirmation to keep receiving new ones. Attachments are PNG or JPEG up to 1 MiB [VERIFIED: https://developers.booking.com/demand/docs/messaging/about-messaging, undated, live page].

[ASSUMPTION/JUDGEMENT] Booking.com's messaging is a **three-party conversation store** (guest, property, platform) with several clients: the guest app, extranet, Pulse, PMS through the Connectivity API, and affiliates through the Demand API. The platform enforces time windows, phishing redaction, read receipts and channel exclusivity. The pre-reservation rules (no attachments, no contact details) exist to stop disintermediation before a booking is secured. The extranet-vs-API exclusivity rule avoids two staff members answering the same structured request through different clients.

### 7.2 Airbnb messaging

- Airbnb reported **over 1.3 billion messages** exchanged in the 12 months to 30 June 2022, "more than 3.5 million a day and over 40 per second" [VERIFIED: https://www.hospitalitynet.org/news/4112343.html, published 2022-09-09 (Airbnb press release, reprinted)]. Evidence age: 2022. No newer volume was found.
- Host messaging upgrades (announced for early 2025): more than a dozen quick-reply templates with placeholders that fill in guest and booking details, **AI-suggested quick replies** that appear "where only you can see it", scheduled messages with reminders, threaded replies, and edit within 15 minutes or unsend within 24 hours [VERIFIED: https://www.airbnb.com/resources/hosting-homes/a/communicate-more-efficiently-with-messaging-upgrades-696, undated (c. late 2024), live page]. ⚠
- The 2024 release added customisable quick-reply templates for welcome messages, check-in details and directions [VERIFIED: https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb, published 2024-10-16]. The 2025 10-K mentions "a refreshed messages tab" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- Airbnb's 2026 evaluation post lists "smart communication features for guests and hosts" among its GenAI launches, alongside review highlights and AI customer support [VERIFIED: https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/, published 2026-07-30].
- Response rate feeds Superhost (4.2), so message timestamps are a **credential input**, not only a UX metric [VERIFIED: https://www.airbnb.com/help/article/829, undated, live page].
- No primary engineering post on Airbnb's messaging back-end was found in this session (see Research limitation).

### 7.3 Automatic translation

- **Translation Engine** (announced 9 November 2021) automatically translates listing descriptions in "over 60 languages", removing click-to-translate buttons. An evaluation commissioned by Airbnb across its top ten languages found it "improves the quality of more than 99% of listings" [VERIFIED: https://news.airbnb.com/2021-winter-release/, published 2021-11-09]. It was extended to **messages** in summer 2022 ("Messages are automatically translated in the user's preferred language") and to **reviews** in September 2022 [VERIFIED: https://www.hospitalitynet.org/news/4112343.html, published 2022-09-09].
- Slator reported that Airbnb's engine runs on **ModernMT** [WIDELY REPORTED: https://slator.com/airbnb-translation-engine-applies-machine-translation-to-ugc/, 2021]. Evidence age: 2021. The model has likely changed since. ⚠
- Booking.com Pulse offers templates in 43 languages (2.1). Translation of free-text partner messages on Booking.com was not verified.

[ASSUMPTION/JUDGEMENT] Translating messages in the read path adds a latency-sensitive dependency to a real-time channel. The robust pattern stores the original text as the record of truth, translates asynchronously or on demand, caches per (message, target language), and always lets either party see the original. That matters for disputes, where support agents and evidence must refer to what was actually written.

**OTA vs hosted stays.** On an OTA, messaging is mostly **operational and structured** (arrival time, parking, bed type), often answered by staff through a PMS, and a messaging API is a must-have connectivity surface. On a hosted-stays marketplace, messaging is **relational and pre-booking** (request-to-book questions, house rules), answered by an individual on a phone. Its timings feed host credentials and its content feeds trust and safety (off-platform payment scams, party detection). Both platforms restrict contact sharing before booking for the same reason: disintermediation.

---

## PART 8: Customer service at scale

### 8.1 Scale and sourcing

| Company | What is disclosed | Source |
| --- | --- | --- |
| Expedia Group | "more than 250 million service interactions a year with over half resolved through self-service"; "more than 30%" AI-powered (CEO, Q1 2026 call) | [WIDELY REPORTED: https://www.hoteldive.com/news/expedia-ai-enhance-customer-support-acquire-new-customers/819968/, 2026] |
| Expedia Group | 24/7 support "by our virtual agent platform, telephone, chat, or e-mail"; a combination of outsourced and in-house contact centres in several countries | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm, published 2026-02-13] |
| Airbnb | "The vast majority of our community support is performed by third-party service providers"; growing pressure "to provide efficient, multilingual support" | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12] |
| Airbnb (2020) | "approximately 7,570 third-party partners that are spread across 24 sites" handled "the vast majority of our community support contacts" | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm, published 2021-02] |
| Booking Holdings | Independent contractors support customer service; risk that "customer service resources (including outsource arrangements) may be unable to provide adequate customer service support" | [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18] |

- Booking Holdings says "Gen AI has also improved customer service resolution times and customer satisfaction" and that it offers "AI assistants to answer consumer queries" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm, published 2026-02-18]. No volume is disclosed.
- Expedia's virtual agent dates back at least to 2019, when the then-CEO cited 1.7 million virtual-agent interactions, 50% with no human involvement [WIDELY REPORTED: https://www.travolution.com/articles/113223/expedia-explore-2019-customers-prefer-text-conversations-to-human-interaction, 2019]. Evidence age: 2019. The Expedia 2020 10-K already described a "conversation platform, which leverages technology and artificial intelligence to provide online customer service options and self-service capabilities" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442421000015/expe-20201231.htm, published 2021-02].

### 8.2 Airbnb's AI customer-service agent (2025)

- Q2 2025: "We're also expanding our AI-powered customer service agent to 100% of U.S. users", "reducing the percentage of hosts and guests who needed to contact a human agent by 15%" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm, published 2025-08-06].
- Q3 2025: the assistant gives "answers tailored to your reservation or listing" and "lets you take common actions—like canceling or changing reservation dates—directly from the chat". In the US it "has already reduced people's need to contact a human agent by around 15%" and cut "the typical resolution time from hours to seconds" for some users. Expansion started "with Spanish in Mexico" [VERIFIED: https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf, published 2025-11-06].
- The same Q3 letter says new cancellation-policy options were "reducing customer service cases" in initial tests [VERIFIED: same URL]. Policy design is a support-volume lever.
- 2025 10-K: "we expanded the use of AI-powered customer service and support features", "AI capabilities now assist in risk assessment and rapid fraud and scam detection", and "enhanced automation in case management, supporting more timely response and resolution for urgent situations" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm, published 2026-02-12].
- Rollout began with about half of US users in April 2025 [WIDELY REPORTED: https://www.customerexperiencedive.com/news/airbnb-ai-first-expands-customer-service-agent-us/757237/, 2025].

### 8.3 Airbnb voice support (IVR) architecture

Airbnb published a detailed architecture for its ML-driven phone support [VERIFIED: https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/, published 2025-06-03]:

1. A conversational IVR asks why the caller is calling, replacing menu trees ("an adaptive, conversational IVR that listens, understands, and responds in real time").
2. **ASR** adapted to noisy phone audio with a domain phrase list. Word error rate fell "from 33% to approximately 10%".
3. **Contact Reason** classification against a taxonomy, served by an **Issue Detection Service** that runs models in parallel, plus a separate model that detects requests for a human. Latency is "under 50ms on average".
4. **Help-article retrieval**: embeddings in a vector database, up to 30 candidates by cosine similarity, an LLM-based ranker picks one, which is sent by SMS or app notification. Retrieval takes about 60 ms.
5. **Paraphrasing**: the caller's issue is matched to UX-writer-authored summaries by embedding nearest neighbour with a calibrated threshold. Precision is above 90%.
6. **Escalation** to a human agent with context attached.

[ASSUMPTION/JUDGEMENT] The reusable pattern for chapter writers is **contact reason as the routing key**. A single taxonomy, shared by chat, voice, the AI agent and human case management, drives self-service content, agent skills routing, and the quality signals that later feed listing quality (Guest Favorites uses "quality-related customer service issues"). Changing the taxonomy is a data migration with ranking consequences.

### 8.4 Disruptions, mass cancellations and policy-as-code

- **COVID-19, 2020 (Airbnb).** In March 2020 Airbnb "applied its extenuating circumstances policy to cancellations resulting from COVID-19". Eligible bookings were those made on or before 14 March 2020 with check-in between 14 March and 31 May 2020. Airbnb "committed up to $250 million for hosts impacted by COVID-19 and an additional $17 million fund for Superhosts". Eligible hosts received 25% of what they would have received under their cancellation policy, and Airbnb recorded "$205.1 million of payments, primarily for hosts" in 2020 [VERIFIED: https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm, published 2021-02].
- **COVID-19, 2020 (OTAs).** Booking Holdings: "increased cancellations, especially early in the pandemic, have resulted in increased customer service costs, as well as higher than normal cash outlays to refund consumers for prepaid reservations" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1075531/000107553121000019/bkng-20201231.htm, published 2021-02]. Expedia: employees "responded quickly to widespread travel cancellations and significant spikes in customer support call volumes" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1324424/000132442421000015/expe-20201231.htm, published 2021-02].
- **Major Disruptive Events policy (current).** It covers large-scale events after booking that prevent or legally prohibit the stay: declared epidemics or public-health emergencies (**COVID-19 excluded**), government travel restrictions, war and civil unrest, prolonged utility outages, and unforeseeable natural disasters. It excludes events affecting only the guest's ability to travel, illness, non-binding advisories, transport disruptions such as flight cancellations, and **foreseeable** weather "such as hurricanes in hurricane season". Hosts who cancel under it get no payout for those dates, and already-paid amounts are withheld from future payouts. The calendar is blocked. Coverage "applies only to the defined area and timeframe" [VERIFIED: https://www.airbnb.com/help/article/1320, undated, live page]. ⚠
- Airbnb's 2026 data post "What COVID did to our forecasting models (and what we built to handle the next shock)" exists. It was found but not read for this brief and is relevant to the demand-shock chapter [VERIFIED: https://airbnb.tech/data/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock/, published 2026-03-24 (existence and title only)].

[ASSUMPTION/JUDGEMENT] The phrase "applies only to the defined area and timeframe" implies that an extreme-event policy is operated as **data**: a declared event with a geography (polygon or region list), a validity window and a booking-date cutoff, evaluated against each affected reservation. That turns a mass-cancellation crisis from millions of individual support contacts into a batch job plus self-service. The 2020 experience (contact spikes at every major OTA, a USD 250 million discretionary host fund at Airbnb) is the argument for building the "declared event" entity before it is needed.

**OTA vs hosted stays.** On an OTA under the agency model, refunds for non-refundable rates depend on the hotel's goodwill and the OTA mediates. Under the merchant model, the OTA holds the cash and carries the refund liability (Booking Holdings' "higher than normal cash outlays"). On a hosted-stays marketplace, the platform's own policy can override the host's cancellation policy, and the platform must decide whether and how to compensate a household host (Airbnb's 25% fund). That compensation is a **marketplace-balance decision** with no hotel equivalent.

---

## PART 9: Cross-cutting architectural implications

[ASSUMPTION/JUDGEMENT] for every item in this part. It synthesises the evidence above.

1. **One partner back-end, many clients.** The extranet, mobile app, connectivity APIs (PMS/channel manager), affiliate APIs and AI assistants all read and write the same entities. Ownership rules (Booking.com's API-vs-extranet reply exclusivity, Airbnb's "PMS owns the lock") must be explicit per field and per workflow.
2. **Partner-facing explainability of ranking.** Paid boosts (Accelerator sort preview, AGP "average boosted ranking") and programme gates (Preferred top 30% per area) require ranking to expose per-property simulations and to log paid terms separately. That is now a regulatory concern (AGCM 2026).
3. **Support data is ranking data.** Guest Favorites uses customer-service issue rates, and Superhost uses response rate and cancellations. The contact-reason taxonomy and message timestamps must be trustworthy, versioned and auditable.
4. **Credentials are batch, signals are streaming.** Superhost is quarterly, and Guest Favorites is periodic. Messaging, check-in and smart-lock state are real time. Separate the two pipelines, and make the batch snapshot rules (for example, review publication time) explicit.
5. **Messaging is a governed channel.** It needs time windows, pre-booking restrictions (no attachments, no contact details), phishing redaction, translation that preserves the original, and read receipts. It is both a product and a trust-and-safety surface.
6. **AI support agents need grounding in live booking state and the ability to act.** Airbnb's agent cancels and changes dates from chat. Booking.com's partner agent uses separate retrievers, including a templated-answers retriever for legally sensitive questions. Expedia's reported Romie lesson was about ungrounded answers. The pattern: retrieval over curated content, tools over transactional APIs, pre-approved answers for regulated topics, and a contact-reason classifier shared with human routing.
7. **Disruption policies as data.** Declared-event entities (geography × window × booking cutoff) make mass cancellation a batch operation with self-service, not a contact-centre surge.
8. **Delegation is a first-class model.** Co-hosts, hotel staff, PMS vendors and channel managers all act on behalf of the owner. Model roles per listing or property, verify each actor, and support split payouts.

---

## Key numbers

| Number | What | Source | Date |
| --- | --- | --- | --- |
| ~4.4 M | Booking.com properties (≈500k hotels/motels/resorts; ≈3.9M homes etc.) | Booking Holdings 10-K FY2025 [VERIFIED] | 2025-12-31 |
| ~3.6 M | Expedia Group lodging properties (≈2.4M Vrbo) | Expedia 10-K FY2025 [VERIFIED] | 2025 year-end |
| > 5 M / > 2.5 B | Airbnb hosts / guest arrivals | Airbnb 10-K FY2025 [VERIFIED] | 2026-02 |
| 30% | Max share of qualifying partners per area that can be Booking.com Preferred | partner.booking.com [VERIFIED] | live page |
| up to 20% | More bookings for Booking.com Preferred partners (Booking.com claim) | partner.booking.com [VERIFIED] | live page |
| 80% | Clicks going to top-20 sort positions on Expedia/Hotels.com (first-party) | Expedia partner blog [VERIFIED] | 2024 data |
| 10 / 12 / 15% | Agoda AGP cost per booking (Basic/Standard/Premium) | Agoda Partner Hub [VERIFIED] | 2025-02 |
| 43 | Languages for Booking.com Pulse message templates | booking.com Pulse page [VERIFIED] | live page |
| 7 / 14 / 66 days | Booking.com messaging windows (property after checkout / extra reply window / guest after checkout) | Booking.com Messaging API docs [VERIFIED] | live page |
| 4.8 / 90% / <1% / 10 stays | Superhost rating / response / cancellation / stays thresholds | Airbnb help 829 [VERIFIED] | live page |
| 2 M | Guest Favorites at launch (>4.9 avg rating; <1% cancellations + quality issues) | Airbnb 2023 Winter Release [VERIFIED] | 2023-11-09 |
| ~500 M | Nights booked at Guest Favorite listings since launch | Airbnb Q3 2025 letter [VERIFIED] | 2025-11-06 |
| > 550,000 | Listings removed under hosting quality system since 2023 | Airbnb Q3 2025 letter [VERIFIED] | 2025-11-06 |
| > 10,000 / 10 | Co-hosts / countries at Co-Host Network launch | Airbnb 2024 Winter Release [VERIFIED] | 2024-10-16 |
| > 100,000 | Listings supported by the Co-Host Network | Airbnb Q2 2025 letter [VERIFIED] | 2025-08-06 |
| 4.86 vs 4.62 | Avg rating: co-hosts vs large PM companies | Airbnb 2024 Winter Release [VERIFIED] | 2024-10-16 |
| 15.5% | Airbnb single service fee applied to PMS hosts from Oct 2025 | Airbnb Q3 2025 letter [VERIFIED] | 2025-11-06 |
| 4.96 | Avg check-in rating for smart-lock stays (Early Access) | Airbnb newsroom [VERIFIED] | 2024-08-21 |
| > 1.3 B | Airbnb messages in 12 months to June 2022 (>40/sec) | Airbnb press release [VERIFIED] | 2022-09-09 |
| > 60 | Languages in Airbnb Translation Engine | Airbnb 2021 Winter Release [VERIFIED] | 2021-11-09 |
| 100,000 / 25,000 | Accessibility features confirmed / homes (manual photo review) | Airbnb 2021 Winter Release [VERIFIED] | 2021-11-09 |
| 168 M | Combined loyalty members at One Key launch | Expedia press release [VERIFIED] | 2023-07-18 |
| ~15% | Reduction in hosts/guests needing a human agent (Airbnb AI agent, US) | Airbnb Q2 & Q3 2025 letters [VERIFIED] | 2025 |
| 33% → ~10% | Airbnb IVR ASR word error rate | airbnb.tech [VERIFIED] | 2025-06-03 |
| < 50 ms | Airbnb contact-reason intent detection latency | airbnb.tech [VERIFIED] | 2025-06-03 |
| 1.33× | Booking.com partner onboarding agent task-completion score uplift (~2,000 dialogues) | booking.ai [VERIFIED] | 2026-10-19 |
| > 250 M | Expedia service interactions per year (>50% self-service; >30% AI) | Hotel Dive [WIDELY REPORTED] | 2026-05 |
| ~7,570 / 24 | Airbnb third-party support partners / sites | Airbnb 10-K FY2020 [VERIFIED] | 2020-12-31 |
| $250 M + $17 M; $205.1 M | Airbnb COVID host fund + Superhost fund; payments recorded in 2020 | Airbnb 10-K FY2020 [VERIFIED] | 2021-02 |

## Open questions / not verifiable

- **Booking.com Genius and Visibility Booster partner terms**: official pages need a sign-in. Thresholds (review floor, discount levels, commission range) are secondary only.
- **Preferred Programme commission uplift**: not stated on Booking.com's public page. The AGCM investigation outcome is pending.
- **Expedia Partner Central internals** (Rev+ horizon, Property Analytics metrics, messaging API for partners): only secondary sources were available. No Expedia engineering post on the partner platform or contact-centre stack was found.
- **Expedia virtual-agent current architecture and Romie's status**: discontinuation is reported only by a low-confidence secondary source.
- **Airbnb messaging back-end architecture** (storage, fan-out, translation pipeline today): no primary post was found. The 2022 volume is the newest number.
- **Airbnb AI support agent architecture** (models, tools, guardrails, handoff): only outcomes are disclosed (≈15% fewer human contacts). The 2026 evaluation post is generic. The "45% of support automated" figure in the press could not be verified.
- **Booking.com customer-service volume and AI agent outcomes**: Booking Holdings discloses only qualitative improvements.
- **Agoda loyalty (AgodaVIP, PointsMAX) and Agoda customer service**: consumer pages did not render.
- **Vrbo host tools and Vrbo messaging**: not researched for lack of reachable primary sources.
- **Airbnb typical host earnings (USD 15,600 in 2025)**: secondary only.
- **Wishlist and trip-itinerary architecture** at any of the companies: no primary source.
- **Booking.com location verification for new properties**: the help topic exists, but the procedure was not read.

## Source list

| Title | Publisher / author | Year | URL |
| --- | --- | --- | --- |
| Form 10-K FY2025 | Booking Holdings Inc. | 2026 | https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm |
| Form 10-K FY2020 | Booking Holdings Inc. | 2021 | https://www.sec.gov/Archives/edgar/data/1075531/000107553121000019/bkng-20201231.htm |
| Form 10-K FY2025 | Expedia Group, Inc. | 2026 | https://www.sec.gov/Archives/edgar/data/1324424/000132442426000008/expe-20251231.htm |
| Form 10-K FY2020 | Expedia Group, Inc. | 2021 | https://www.sec.gov/Archives/edgar/data/1324424/000132442421000015/expe-20201231.htm |
| Form 10-K FY2025 | Airbnb, Inc. | 2026 | https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm |
| Form 10-K FY2020 | Airbnb, Inc. | 2021 | https://www.sec.gov/Archives/edgar/data/1559720/000155972021000010/airbnb-10k.htm |
| Q2 2025 Shareholder Letter (8-K Ex. 99.1) | Airbnb, Inc. | 2025 | https://www.sec.gov/Archives/edgar/data/1559720/000119312525174438/d17531dex991.htm |
| Q3 2025 Shareholder Letter | Airbnb, Inc. | 2025 | https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf |
| How do I become a Superhost? (help 829) | Airbnb | live | https://www.airbnb.com/help/article/829 |
| Major Disruptive Events Policy (help 1320) | Airbnb | live | https://www.airbnb.com/help/article/1320 |
| Identity verification (help 1237) | Airbnb | live | https://www.airbnb.com/help/article/1237 |
| Smart lock integration via PMS (help 4163) | Airbnb | live | https://www.airbnb.com/help/article/4163 |
| Accessibility & disability inclusion (help 2166) | Airbnb | live | https://www.airbnb.co.nz/help/article/2166 |
| Accessibility at Airbnb | Airbnb | live | https://www.airbnb.com.sg/accessibility |
| Communicate more efficiently with messaging upgrades | Airbnb | c. 2024 | https://www.airbnb.com/resources/hosting-homes/a/communicate-more-efficiently-with-messaging-upgrades-696 |
| Airbnb 2021 Winter Release | Airbnb Newsroom | 2021 | https://news.airbnb.com/2021-winter-release/ |
| Translation Engine launches Reviews after expanding to Messages | Airbnb (via Hospitality Net) | 2022 | https://www.hospitalitynet.org/news/4112343.html |
| Airbnb 2023 Winter Release | Airbnb Newsroom | 2023 | https://news.airbnb.com/en-uk/airbnb-2023-winter-release/ |
| Airbnb 2024 Winter Release: Introducing Co-Host Network | Airbnb Newsroom | 2024 | https://news.airbnb.com/en-uk/airbnb-2024-winter-release-introducing-co-host-network-the-best-local-hosts-to-manage-your-airbnb |
| Smart lock integrations now available to all hosts in the US and Canada | Airbnb Newsroom | 2024 | https://news.airbnb.com/smart-lock-integrations-available-to-all-us-and-canada-hosts |
| Airbnb API documentation | Airbnb | live | https://developer.withairbnb.com/ |
| Listening, Learning, and Helping at Scale (voice support) | Cao, Ji, Liu, Wang, Zhang / Airbnb Tech | 2025 | https://airbnb.tech/ai-ml/listening-learning-and-helping-at-scale-how-machine-learning-transforms-airbnbs-voice-support-experience/ |
| Eval-driven development: Lessons from evaluating GenAI at scale | Airbnb Tech | 2026 | https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/ |
| What COVID did to our forecasting models | Airbnb Tech | 2026 | https://airbnb.tech/data/what-covid-did-to-our-forecasting-models-and-what-we-built-to-handle-the-next-shock/ |
| Understanding the Messaging API | Booking.com Developers (Connectivity) | live | https://developers.booking.com/connectivity/docs/messaging-api/understanding-the-messaging-api |
| Messaging API: Use cases and best practices | Booking.com Developers | live | https://developers.booking.com/connectivity/docs/messaging-api/use-cases-and-best-practices |
| Pre-reservation messaging | Booking.com Developers | live | https://developers.booking.com/connectivity/docs/request-to-book/pre-reservation-messaging |
| About messaging (Demand API) | Booking.com Developers | live | https://developers.booking.com/demand/docs/messaging/about-messaging |
| Preferred Partner Programme | Booking.com for Partners | live | https://partner.booking.com/en-gb/solutions/preferred-partner-programme |
| Pulse by Booking.com | Booking.com | live | https://www.booking.com/propertyapp.en-gb.html |
| From Static Help Content to a RAG-Based Onboarding Agent for Partners | Barchukova et al. / booking.ai | 2026 | https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7 |
| Introducing AgentHub | Beladev, Harush, Ross / booking.ai | 2026 | https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50 |
| Booking.com Enhances Travel Planning with New AI-Powered Features | Booking Holdings | 2024 | https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/ |
| PS13115 – Investigation into Booking.com (Preferred programmes) | AGCM (Italian Competition Authority) | 2026 | https://en.agcm.it/en/media/press-releases/2024/4/PS13115 |
| Put Your Trip on Autopilot (EXPLORE 2024) | Expedia Group IR | 2024 | https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx |
| TravelAds and Accelerator: hotel visibility boosters | Expedia Group Partner blog | 2025 | https://partner.expediagroup.com/en-us/resources/blog/travelads-and-accelerator-hotel-visibility-boosters |
| Expedia Group Announces 'One Key' | Expedia Group (via Hospitality Net) | 2023 | https://www.hospitalitynet.org/news/4117344.html |
| Reach your target audience with TravelAds (sponsored) | Expedia Group Media Solutions (via Hospitality Net) | 2024 | https://www.hospitalitynet.org/news/4123355.html |
| Expedia taps AI to enhance customer support | Hotel Dive | 2026 | https://www.hoteldive.com/news/expedia-ai-enhance-customer-support-acquire-new-customers/819968/ |
| Expedia Explore 2019: customers prefer text conversations | Travolution | 2019 | https://www.travolution.com/articles/113223/expedia-explore-2019-customers-prefer-text-conversations-to-human-interaction |
| Expedia Group shares AI chatbot lessons learned | Let's Data Science | 2026 | https://letsdatascience.com/news/expedia-group-shares-ai-chatbot-lessons-learned-239f348a |
| Expedia launches revenue management tool Rev+ | Hospitality Technology | 2019 | https://hospitalitytech.com/expedia-launches-revenue-management-tool-rev |
| Expedia Partner Central guide | Lodgify | 2025 | https://www.lodgify.com/guides/expedia/partner-central/ |
| Agoda unveils Agoda Partner Portal (formerly YCS) | Agoda via PR Newswire / Kyodo | 2026 | https://kyodonewsprwire.jp/release/202608174214 |
| Agoda Growth Program | Agoda Partner Hub | 2025 | https://www.partnerhub.agoda.com/?p=95313 |
| How to navigate within your Agoda YCS extranet | NightsBridge | undated | https://nightsbridge-6.screenstepslive.com/a/1973011-how-to-navigate-within-your-agoda-ycs-partner-extranet |
| Agoda PointsMAX guide | Point Hacks | 2025 | https://www.pointhacks.com.au/agoda-pointsmax/ |
| Airbnb expands AI customer service agent in US | Customer Experience Dive | 2025 | https://www.customerexperiencedive.com/news/airbnb-ai-first-expands-customer-service-agent-us/757237/ |
| Airbnb Translation Engine applies machine translation to UGC | Slator | 2021 | https://slator.com/airbnb-translation-engine-applies-machine-translation-to-ugc/ |
| Airbnb: Paris region has over 1,000 listings with step-free features | International Paralympic Committee | 2024 | https://www.paralympic.org/news/airbnb-paris-region-has-over-1000-listings-step-free-accessibility-features |
| Join the Co-Host Network | Airbnb Resources | 2025 | https://www.airbnb.com/resources/hosting-homes/a/join-the-co-host-network-629 |
| What's new for Airbnb hosts in the 2025 Summer Release | Rental Scale-Up | 2025 | https://www.rentalscaleup.com/whats-new-for-airbnb-hosts-in-the-2025-summer-release-tools-built-for-one-listing-hosts/ |
| Booking.com fees: guide for US hosts | Wise | 2025 | https://wise.com/us/blog/booking-com-host-fees |
| Tips on how to become a Booking.com Preferred Partner | Hostaway | 2024 | https://www.hostaway.com/blog/booking-preferred-partner/ |
| How to get more bookings on Booking.com | Hostaway | 2024 | https://www.hostaway.com/get-more-bookings-on-booking-com |
| Visibility boosters and marketing in OTAs | Mirai | 2023 | https://www.mirai.com/blog/visibility-boosters-and-marketing-in-otas-a-guide-to-understanding-choosing-and-comparing-each-option/ |
| Booking.com Genius Program | TravelNest | 2024 | https://travelnest.com/news-and-insights/boost-visibility-and-increase-bookings-with-booking-com-genius-program |
| Genius loyalty program: guide for independent hoteliers | PriceLabs | 2024 | https://hotels.pricelabs.co/blog/genius-loyalty-program-booking-com/ |
| Booking.com Genius loyalty programme | The Points Guy | 2024 | https://thepointsguy.com/loyalty-programs/booking-com-genius-loyalty-programme/ |
| Hostaway is a 2024 Airbnb Preferred+ Software Partner | Hostaway | 2024 | https://www.hostaway.com/blog/hostaway-achieves-preferred-partnership-status-with-airbnb/ |
| HotelRunner titled Preferred Software Partner by Airbnb | HotelRunner | 2024 | https://hotelrunner.com/en/news/awards-recognitions/hotelrunner-is-once-again-titled-as-preferred-software-partner-by-airbnb |
| Airbnb drives record USD 93 billion in US economy in 2025 | India Outbound | 2026 | https://indiaoutbound.info/?p=216130 |
| Airbnb statistics | iPropertyManagement | 2024 | https://ipropertymanagement.com/research/airbnb-statistics |
