# Research brief: Trust, safety and regulation in accommodation marketplaces

Prepared 21 October 2026 for chapter writers of *BOOKED: Architecting Travel Accommodation and Hosted Stays Marketplaces*. The brief is vendor-neutral. Airbnb and Booking.com get the most space because they have published the most dated, checkable material on trust and because regulators have named them directly, not because the book endorses their choices. The brief covers two halves: **trust and safety** (identity, fraud, risk screening, reviews, damage, messaging, discrimination) and **regulation** (short-term-rental rules, platform law, consumer law, data, payments, accessibility, tax reporting).

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page or official text was fetched in this session (21 October 2026) and supports the claim. Paraphrases stay close to the source, and quoted text is quoted. The date is the source's publication date (for legislation, the date of the act or its application date as stated), not the fetch date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source (press, security-vendor research, law-firm or industry blog, search-engine summary of a page that could not be fetched), not from the company's or regulator's own text.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference. Every architectural statement about a proprietary system the company has not described falls here. Chapter writers should re-verify these claims or present them explicitly as reference-architecture judgement.

**Evidence age matters.** Trust policy and regulation move faster than most architecture. Airbnb's 2021 identity-verification coverage figure (81 % of stays) was superseded by mandatory verification in 2023. Spain's national short-term-rental registry, live from July 2025, was partly annulled by the Supreme Court in May 2026. Each section gives the date of its evidence. Do not describe a dated source in the present tense without checking.

**Research limitation.** The session's shared web-search quota ran out about two thirds of the way through. After that, research relied on direct fetches of known URLs and on official texts from the EU Publications Office. As a result:

- **No primary source was found for Booking.com's own guest-side trust architecture** (guest verification, fraud scoring, messaging link scanning). Booking.com's Partner Hub returned HTTP 403 and its consumer reviews page returned 404. Booking.com's trust behaviour in this brief comes from regulators, security researchers, the press and Booking.com statements quoted by the press.
- **Expedia Group, Vrbo, Agoda and Trip.com trust and safety** have no verified primary source here.
- **Airbnb's engineering posts on fraud and risk** (for example "Fighting financial fraud with targeted friction", 2018) returned HTTP 403 on Medium and are not in the current RSS feed. Airbnb's risk stack is described only from newsroom posts.
- **City rules for Paris** could not be confirmed on an official Paris or Légifrance page; they are tagged WIDELY REPORTED.
- **Fines and enforcement actions** not fetched in this session (for example Spain's national competition authority fine on Booking.com, Spain's consumer-ministry fine on Airbnb, Italian tax settlements) are listed under Open questions, not stated as fact.
- The Schengen Convention text on hotel guest registration could not be fetched.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: city caps, registry status, insurance limits, holiday-screening numbers, enforcement status and product names.

---

## PART 1: Why trust differs between the two marketplace types

### 1.1 The trust problem, side by side

| Dimension | Travel accommodation marketplace (OTA-style) | Hosted stays marketplace (peer-to-peer / STR) |
| --- | --- | --- |
| Supply-side party | A business (hotel, chain, property manager) with staff, a front desk and a PMS | Often a private individual; increasingly professional managers |
| Who must the guest trust? | The platform's listing accuracy and payment handling; the hotel is a regulated business | A stranger's home, its safety, its accuracy and the stranger themselves |
| Who must the supply side trust? | Mostly that the card is good and the guest shows up | That the guest will not damage the home, throw a party or harm neighbours |
| Typical identity check | Guest identity checked at the front desk (often a legal requirement); platform rarely ID-verifies guests | Platform verifies identity of guest and host before booking |
| Main fraud surface | Partner (hotel) **extranet account takeover**, then phishing of guests via the platform's own messaging; card-not-present fraud | Fake listings, off-platform payment scams, account takeover, party and damage risk |
| Physical-risk control | Hotel staff, building security, fire codes | Platform policy (party ban, camera rules), reservation screening, damage protection |
| Reviews | One-way: guests review properties | Two-way: guests and hosts review each other |
| Regulation of supply | Hotel licensing, fire and safety codes already exist | Short-term-rental registration, night caps, zoning; new EU regime from May 2026 |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis. It is supported by the sources in Parts 2–8, in particular: the EU Short-Term Rental Regulation explicitly excludes hotels from its definition of "unit" (Part 8.1); Airbnb mandates identity verification for guests and primary hosts (Part 2.1); and the dominant documented Booking.com fraud pattern of 2023–2025 is hotel-account takeover followed by guest phishing through the platform's messaging (Part 3.2).

### 1.2 The architectural consequence

[ASSUMPTION/JUDGEMENT] In an OTA, trust and safety is mainly **a security and payments problem on the supply side**: protect partner accounts, protect the messaging channel, stop card fraud. In a hosted-stays marketplace it is also **a physical-safety and behaviour problem on both sides**: who the guest is, what they intend to do in the home, what the home really contains. That is why hosted-stays platforms build reservation-screening models, identity verification at booking time and damage-protection programmes, while OTAs invest more in partner authentication, messaging abuse detection and payment-fraud controls. Both converge on the same regulatory obligations (DSA, consumer law, review rules) where they act as platforms.

---

## PART 2: Identity and account security

### 2.1 Airbnb: mandatory identity verification

- Airbnb announced that by the end of June 2023 **all guests booking homes and all primary Hosts getting booked globally** must complete identity verification. This expanded a 2022 process that covered guests travelling to the top 35 countries and regions [VERIFIED: https://news.airbnb.com/an-update-on-identity-verification-on-airbnb, published 2023-06-29].
- Method as described: Airbnb compares a government ID (driver's licence, passport or national identity card) with the information the user gave, sometimes with a **selfie for photo matching**, and may match name, phone, address and date of birth against "secure third-party databases"; in the US it may use a Social Security number [VERIFIED: https://news.airbnb.com/an-update-on-identity-verification-on-airbnb, published 2023-06-29].
- Enforcement is built into the booking flow: unverified primary Hosts have their **calendars blocked**, "preventing them from accepting any more bookings", and unverified guests cannot book. Verified accounts show an "identity verified" badge [VERIFIED: https://news.airbnb.com/an-update-on-identity-verification-on-airbnb, published 2023-06-29].
- Quote, Airbnb Director of Trust Nabarupa Banerjee: "As a platform that works to build trust, the identity verification process is a foundational aspect of what we do." [VERIFIED: https://news.airbnb.com/an-update-on-identity-verification-on-airbnb, published 2023-06-29]
- Historical baseline (⚠ superseded): in October 2021 about **81 % of global stays** were booked between a Host and guest who had both completed verification, **97 % in the US** [VERIFIED: https://news.airbnb.com/building-on-our-commitment-to-trust-2, published 2021-10-29]. Use only to show the move from "most" to "all".
- Airbnb's March 2026 AirCover page still lists guest identity verification as a host protection and says some US-based guests may also get background checks [VERIFIED: https://www.airbnb.com/resources/hosting-homes/a/how-aircover-for-hosts-works-469, published 2026-03-31].
- Scale claim: Airbnb's 2025 Summer Release reportedly refers to "over 200 million guests and hosts" who have completed identity verification [WIDELY REPORTED: https://news.airbnb.com/airbnb-2025-summer-release, 2025]. This came from a search summary; the page was not fetched.

[ASSUMPTION/JUDGEMENT] Architecturally, identity verification in hosted stays is a **booking-path gate**, not an onboarding nicety. It needs a verification state on the account, a vendor integration for document and selfie checks, a policy service that decides which actions need which verification level, and a retention policy for ID images (see GDPR, Part 9.6). Airbnb has not published its vendor or internal service design.

### 2.2 Booking.com and OTAs: partner identity and authentication

- Booking.com stated in 2024 that two-factor authentication "is required and enforced, including for partners to access payment details from customers securely" [WIDELY REPORTED: https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/, 2024]. Krebs notes it was unclear whether this applied to all partners or only newer ones.
- The Secureworks investigation of an October 2023 incident found the victim hotel **had not enabled MFA** on its Booking.com access, which made login with stolen credentials easy [VERIFIED: https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam, published 2023 (describes an October 2023 incident; page shows no date)].
- [ASSUMPTION/JUDGEMENT] OTAs historically did not ID-verify leisure guests, because the hotel checks identity at the front desk and because high-friction checks cut conversion. No primary source for Booking.com guest identity verification was found in this session (see Open questions).

### 2.3 Regulatory identity duties: "know your business customer"

- **DSA Article 30 (traceability of traders)**: online platforms that let consumers conclude distance contracts with traders must, before letting a trader offer services, collect the trader's name, address, phone and email, **a copy of the trader's identification document** (or eIDAS e-ID), **payment account details**, trade-register number where applicable, and a self-certification of compliance; and must "make best efforts" to assess whether this is reliable and complete, using official databases or supporting documents [VERIFIED: http://publications.europa.eu/resource/celex/32022R2065, published 2022-10-19 (Regulation (EU) 2022/2065)].
- The DSA applies in general **from 17 February 2024** [VERIFIED: http://publications.europa.eu/resource/celex/32022R2065, published 2022-10-19].
- **DAC7** (Council Directive (EU) 2021/514) requires platform operators to report sellers, explicitly including those renting immovable property; the first information covers reportable periods **from 1 January 2023**, reported by **31 January** of the following year [VERIFIED: http://publications.europa.eu/resource/celex/32021L0514, published 2021-03-22].
- DAC7 excludes from reporting an **entity seller for which the platform facilitated more than 2,000 rental activities for one property listing** in the period, and publicly listed entities [VERIFIED: http://publications.europa.eu/resource/celex/32021L0514, published 2021-03-22].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] DAC7's 2,000-rental exclusion and its listed-company exclusion mean large hotel entities often fall outside seller reporting, while individual hosts almost always fall inside it. A hosted-stays platform therefore needs tax-identity collection (TIN, date of birth, address, payout account) for nearly every host; an OTA needs it for small independent properties and home-like listings. DSA Article 30 applies to "traders"; many private hosts are not traders, so a platform needs a **trader / non-trader declaration** in host onboarding (which also drives consumer-law labelling, see Part 9.4).

### 2.4 Account login as a trust surface (hosted stays)

- Airbnb rebuilt login as "Flexible Authentication": an **"Identify first then Challenge"** model where a server-side policy engine chooses the challenge most likely to succeed (for example WhatsApp OTP in Brazil, Naver login in South Korea), with a server-driven "Try another way" challenge picker; "the client never decides which challenge to present" [VERIFIED: https://medium.com/airbnb-engineering/flexible-authentication-reimagining-authentication-for-millions-of-users-at-airbnb-3a8a4c917137 (via RSS feed), published 2026-08-12].
- The post frames irregular logins as structural: a guest books in January and may not return until summer; a host checks in only when a reservation arrives; "a failed login means a lost booking" [VERIFIED: same, published 2026-08-12].

[ASSUMPTION/JUDGEMENT] A server-chosen challenge is also the natural hook for risk-based step-up authentication (choosing a stronger challenge when the session looks risky), but the post describes the policy engine in terms of success rate, not fraud risk. Do not claim Airbnb uses it for risk step-up.

---

## PART 3: Fraud typology in travel accommodation

### 3.1 Typology

| Fraud type | Mechanism | Who is hit first | More common in | Main control |
| --- | --- | --- | --- | --- |
| Stolen-card bookings | Card-not-present fraud; chargebacks months later | Platform (merchant model) or property (agency model) | Both | Risk scoring, 3-D Secure / SCA, velocity limits |
| Partner extranet account takeover | Infostealer or phishing captures hotel credentials | Property, then its guests | OTA | Partner MFA / passkeys, session anomaly detection |
| Guest phishing via platform messaging | Attacker in a hijacked partner account messages real guests with fake payment links | Guest | OTA (documented); also hosted | Link scanning, payment-request rules, guest warnings |
| Lookalike-domain phishing | Fake "Booking.com" pages, fake CAPTCHA (ClickFix) delivering malware to hotel staff | Property staff | OTA | Staff training, endpoint protection |
| Fake listings | Non-existent or hijacked property listed to collect prepayment | Guest | Hosted stays, holiday homes on OTAs | Listing verification, address checks, payout holds |
| Off-platform payment scams | Guest persuaded to pay by bank transfer outside the platform | Guest | Both | Message content detection, policy, education |
| Triangulation / resale fraud | Fraudster resells rooms booked with stolen cards or compromised accounts at a discount | Card holder, property | OTA | Name-mismatch checks, risk scoring |
| Account takeover of guests | Stolen guest credentials used to book or redeem credits | Guest | Both | Login risk, step-up auth |
| Parties and damage | Legitimate-looking guest uses a home for a party | Host, neighbours | Hosted stays | Reservation screening, party ban, damage protection |

[ASSUMPTION/JUDGEMENT] Synthesis table. The extranet-takeover and messaging-phishing rows are documented in 3.2. The resale row is supported by Krebs' observation that underground sellers offered "up to 50 % off" hotel reservations paid with compromised accounts [WIDELY REPORTED: https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/, 2024].

### 3.2 The 2023–2025 Booking.com partner-account campaigns (documented)

This is the best-documented fraud pattern in the industry and a strong case study for the book. The chain is: compromise the hotel, then use the platform's trusted channel to defraud the hotel's guests.

1. **Initial access, 2023.** A threat actor emailed hotel operations staff posing as a former guest who had lost an ID (later "a passport"); a follow-up email with no attachment linked to a Google Drive ZIP containing the **Vidar infostealer**, which stole the hotel's Booking.com credentials [VERIFIED: https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam, published 2023 (Secureworks CTU; incident October 2023)].
2. **Account abuse.** "Access to this portal would allow the threat actor to see all upcoming bookings and directly message customers." Guests then received messages asking them to confirm payment details at malicious URLs, and several hours later complained that money had been taken [VERIFIED: same].
3. **Timeline and demand.** Hotels reported abuse of Booking.com's messaging system in **March 2023 and August 2023**; Secureworks observed high demand for Booking.com property credentials on underground forums [WIDELY REPORTED: https://www.helpnetsecurity.com/2023/12/04/booking-com-hotel-booking-scam/, 2023]. Perception Point had earlier described payloads including Vidar, StealC and Lumma [WIDELY REPORTED: same].
4. **Scale-up, 2024.** ESET found the **Telekopye** scam-as-a-service network, previously focused on second-hand marketplaces, expanded to Booking.com and Airbnb, using "compromised accounts of legitimate hotels and accommodation renters", which it believes were "most likely access[ed] via stolen credentials purchased on cybercriminal forums"; the fake pages were prefilled so that "the info provided on the fraudulent pages matches real bookings made by the targeted users". In **July 2024** these scams surpassed Telekopye's marketplace scams in ESET detections for the first time [VERIFIED: https://www.welivesecurity.com/en/eset-research/telekopye-hits-new-hunting-ground-hotel-booking-scams/, published 2024-10-10].
5. **In-app delivery, 2024.** Krebs documented a phishing message delivered **inside the Booking.com app** minutes after a guest booked a California hotel, using the hotel's name and reservation details and claiming Booking.com's anti-fraud system needed more information; the landing domain's registrant was linked to over 700 other phishing domains [VERIFIED: https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/, published 2024-11-01].
6. **Booking.com's position.** Booking.com told Krebs "there has been no compromise of Booking.com's internal systems", that "the phishing attacks stem from partners' machines being compromised with malware", and that criminals "follow-up with messages to try and get customers to make payments outside of our platform" [VERIFIED: same, published 2024-11-01].
7. **ClickFix, 2024–2025.** Microsoft tracked **Storm-1865** running a Booking.com-themed campaign from December 2024 targeting hospitality staff in North America, Oceania, South and Southeast Asia and Europe. Lures were fake guest complaints, booking requests and account-verification notices; a fake CAPTCHA told the user to paste a command into the Windows Run dialog, delivering XWorm, Lumma Stealer, VenomRAT, AsyncRAT, Danabot and NetSupport RAT, all able "to steal financial data and credentials for fraudulent use" [VERIFIED: https://www.microsoft.com/en-us/security/blog/2025/03/13/phishing-campaign-impersonates-booking-com-delivers-a-suite-of-credential-stealing-malware/, published 2025-03-13].
8. **Volume.** Booking.com's head of internet safety, Marnie Wilking, told the Collision conference of a "500 to a 900 percent increase" in travel scams over roughly 18 months, saying "the uptick started shortly after ChatGPT got launched" and calling 2FA "the best way to combat phishing and credential stealing" [WIDELY REPORTED: https://silicon.co.uk/ai/booking-com-scam-surge-ai-569105, 2024]. Booking.com also reportedly said it blocked **85 million fraudulent reservations and over 1.5 million phishing attempts in 2023** [WIDELY REPORTED: https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/, 2024]. Both figures are company statements relayed by the press; no primary Booking.com document was fetched.

⚠ Campaign names, payloads and lures change monthly. Present the **chain**, not the malware names, as the durable lesson.

### 3.3 Architectural lessons from the campaigns

[ASSUMPTION/JUDGEMENT] None of these is a described Booking.com internal; they are reference-architecture conclusions from the documented attack chain.

- **The platform's messaging channel is part of the attack surface.** When attackers send from a genuine partner account, the guest sees a genuine thread. Controls must sit on the **content and context** of messages: URL extraction and reputation, blocking or warning on links to non-platform payment pages, detecting "pay again / verify card" language, and rate-limiting messages from a partner account whose session looks new.
- **Partner sessions need anomaly detection, not only MFA.** Infostealers steal session cookies as well as passwords, so MFA at login is necessary but not sufficient. Signals: new device and geography for a long-stable property account, bulk reads of upcoming reservations, bulk messaging to unpaid reservations, changes to payout bank details (a WKO notice describes payout details changed to a foreign account [WIDELY REPORTED: https://www.wko.at/wien/tourismus-freizeitwirtschaft/hotellerie/online-sicherheit-bei-buchungplattformen, date unknown]).
- **Least privilege in the extranet.** Separate roles for reservations, messaging, finance and payout changes, with step-up authentication on payout and bank-detail changes.
- **Payment requests must be structured, not free text.** If the only legitimate way to ask a guest for money is a platform payment request object, then any free-text payment ask is anomalous by definition.
- **Merchant vs agency model changes who loses.** In the agency model the hotel charges the card, so stolen card data in a hotel's hands is a direct risk; in the merchant model the platform holds the card and can keep card data away from partner screens.

### 3.4 Payment fraud and strong customer authentication (EU)

- The PSD2 regulatory technical standards on strong customer authentication (Commission Delegated Regulation (EU) 2018/389) apply **from 14 September 2019** [VERIFIED: http://publications.europa.eu/resource/celex/32018R0389, published 2017-11-27].
- **Low-value exemption** (Article 16): SCA may be skipped for remote payments up to **EUR 30**, until the cumulative amount since the last SCA exceeds EUR 100 or five consecutive transactions [VERIFIED: same].
- **Transaction-risk-analysis exemption** (Article 18): a PSP may skip SCA for low-risk remote payments if its fraud rate is at or below reference rates. For remote card payments the Annex sets **0.13 % up to EUR 100, 0.06 % up to EUR 250, 0.01 % up to EUR 500** [VERIFIED: same].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Accommodation baskets are usually above EUR 100, so TRA exemptions only help platforms (or their acquirers) with very low fraud rates. Pay-later and pay-at-property bookings (common in OTAs) raise a further SCA problem: the card is captured long before the charge, so the flows depend on merchant-initiated-transaction treatment, set up with SCA at booking time. That is an EBA interpretation and card-scheme practice, not text in the RTS fetched here. Hosted-stays platforms usually charge at or soon after booking (merchant model), so SCA lands in the booking flow.

---

## PART 4: Risk scoring and reservation screening (hosted stays)

### 4.1 Airbnb anti-party screening

- **Origin.** Airbnb introduced a party ban in August 2020 "which we then codified in 2022" [VERIFIED: https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior, published 2023-08-31].
- **Signals (2022 description).** The anti-party technology in the US and Canada looks at the guest's "history of positive reviews (or lack of positive reviews)", how long the guest has been on Airbnb, trip length, distance between guest and listing, and weekend vs weekday, among other factors [VERIFIED: https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada, published 2022-08-16].
- **Outcome for flagged guests.** Blocked guests can still book a **private room or a hotel room** through Airbnb [VERIFIED: same]. The system therefore **redirects** rather than simply rejects, which keeps the guest in the marketplace.
- **Pilot result.** An Australian pilot led to "a 35 percent drop in incidents of unauthorized parties" [VERIFIED: same, published 2022-08-16].
- **Earlier screening (2021).** A risk-based restriction in the US and Canada blocked certain guests from booking entire homes, and a separate rule blocked some **last-minute entire-home bookings**; each had "blocked thousands of distinct reservation attempts" [VERIFIED: https://news.airbnb.com/building-on-our-commitment-to-trust-2, published 2021-10-29].
- **Outcome metrics (2023 post).** A "55 percent year-over-two-year drop in the rate of party reports"; in 2022, "just 0.039 percent of global reservations resulted in an allegation of a party"; about 0.09 % of stays had a safety-related report; about 0.02 % of reservations led to damage reimbursement of USD 1,000 or more. The tool is described as "proprietary reservation screening technology", rolled out worldwide [VERIFIED: https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior, published 2023-08-31].
- **Holiday surges (⚠).** For July 4 2025, more than **20,000 people** in the US were redirected from booking entire-home listings; in 2025 "fewer than approximately 0.06% of stays on Airbnb in the US resulted in a report of a party" [VERIFIED: https://news.airbnb.com/airbnbs-anti-party-system-returns-for-july-4-weekend, published 2026-06-24]. For Halloween 2024, about 38,000 people were reportedly blocked or redirected in the US [WIDELY REPORTED: https://news.airbnb.com/airbnb-rolls-out-anti-party-system-for-halloween/, 2025 (search summary; not fetched)].
- **Other levers** described in 2023: a Neighborhood Support Line, a 24-hour safety line, free noise sensors for hosts in more than 60 countries, and heightened enforcement around Halloween and New Year's Eve [VERIFIED: https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior, published 2023-08-31].

[ASSUMPTION/JUDGEMENT] Architecture implied by the public description: a **pre-booking risk decision** in the reservation path (synchronous, low-latency), fed by account-history and trip features; a **policy layer** whose thresholds tighten on specific dates and regions (holiday modes); an **action set** larger than allow/deny (redirect to room types, require attestation, allow); and **outcome labels** from party reports and damage claims to train and measure. Airbnb has not published the model type, features beyond the list above, or thresholds in the sources fetched here. Do not describe them.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] OTAs screen reservations mainly for **payment fraud and no-show risk** (the hotel's loss is an empty room or a chargeback). Behavioural screening for parties is a hosted-stays problem because the asset is a private home with neighbours and no staff.

### 4.2 Hidden cameras and in-home devices

- Airbnb announced on 11 March 2024 that **indoor security cameras are prohibited in all listings** regardless of location or prior disclosure; hosts had until 30 April 2024 to remove them. Outdoor cameras such as doorbell cameras remain allowed but must be disclosed with their general location before booking [WIDELY REPORTED: https://abc7news.com/airbnb-bans-the-use-of-indoor-security-cameras-on-all-properties/14516158/, 2024]. Previously, disclosed and visible indoor cameras were allowed in common areas but never in sleeping areas or bathrooms [WIDELY REPORTED: same].

[ASSUMPTION/JUDGEMENT] For architecture, device policy becomes **structured listing attributes** (outdoor camera: yes/no, location; noise monitor: yes/no) that are shown before booking, plus a reporting and enforcement path. OTAs rely on hotel regulation and rarely model such attributes.

---

## PART 5: Reviews and review integrity

### 5.1 Platform practice

- Booking.com states that "the only way to leave a review is to first make a booking", that this is "how we know our reviews come from real guests who have stayed at the property", and that it screens for inappropriate language and checks authenticity before publishing; it reportedly shows reviews from the past 14 months only [WIDELY REPORTED: https://www.booking.com/reviews.html, date unknown (page content seen via search; direct fetch returned 404)].
- A third-party hotel-marketing source says a reservation is enough to trigger a review invitation (so no-shows may be invited); this is unconfirmed [WIDELY REPORTED: https://www.hostaway.com/booking-com-reviews-policy-and-how-to-remove-reviews-on-booking-com, date unknown].
- Airbnb increased the number of guests who receive reviews as an anti-discrimination measure, expecting it to help Black and Latino/Hispanic guests in particular [VERIFIED: https://news.airbnb.com/sixyearadupdate, published 2022-12-13].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] OTA reviews are one-way (guest about property). Hosted-stays reviews are two-way, and guest reviews are themselves a trust signal used by hosts and by risk systems (Airbnb's anti-party signals include review history, Part 4.1). Two-way reviews need simultaneous-reveal or blind-period mechanics to stop retaliation; Airbnb's mechanics were not verified in this session.

### 5.2 Regulation of reviews

| Jurisdiction | Instrument | Applies from | Core duty for a platform showing reviews |
| --- | --- | --- | --- |
| EU | Omnibus Directive (EU) 2019/2161 | 28 May 2022 | Tell consumers **whether and how** reviews are checked to come from real users; banned to claim reviews are from real users without "reasonable and proportionate steps"; banned to submit, commission or misrepresent fake reviews |
| UK | Digital Markets, Competition and Consumers Act 2024, Sch. 20 para 13 | 6 April 2025 | Banned: fake reviews, concealed incentivised reviews, misleading publication; publishers must take "reasonable and proportionate steps" to prevent and remove them |
| US | FTC Trade Regulation Rule on Consumer Reviews and Testimonials | Announced 14 Aug 2024; effective 60 days after Federal Register publication | Banned: fake (incl. AI-generated) reviews, sentiment-conditioned incentives, undisclosed insider reviews, review suppression; civil penalties |

Sources:

- EU: Annex I point 23b bans "stating that reviews of a product are submitted by consumers who have actually used or purchased the product without taking reasonable and proportionate steps to check that they originate from such consumers"; point 23c bans submitting, commissioning or misrepresenting false reviews; new Article 7(6) makes information on "whether and how" reviews are verified **material information**; Member States apply the measures from 28 May 2022 [VERIFIED: http://publications.europa.eu/resource/celex/32019L2161, published 2019-11-27].
- UK: paragraph 13(1)–(4) of Schedule 20 bans fake reviews, concealed incentivised reviews, misleading publication (for example suppressing negative reviews), and publishing without "such reasonable and proportionate steps as are necessary" to prevent and remove them; in force 6 April 2025 [VERIFIED: https://www.legislation.gov.uk/ukpga/2024/13/schedule/20, published 2024 (Act); paragraph in force 2025-04-06]. The CMA published fake-reviews guidance (CMA208) on 4 April 2025 [VERIFIED: https://www.gov.uk/government/publications/fake-reviews-cma208, published 2025-04-04].
- US: FTC final rule announced 14 August 2024; prohibits the practices listed above and lets the FTC seek civil penalties against knowing violators. Chair Khan: "Fake reviews not only waste people's time and money, but also pollute the marketplace." [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials, published 2024-08-14]. The effective date (widely cited as 21 October 2024) was not checked in the Federal Register.

[ASSUMPTION/JUDGEMENT] Architectural consequence: a review is valid only if it is **linked to a completed stay record** (reservation ID, stay dates, cancellation/no-show status). The review store therefore depends on the reservation system of record, and the platform must be able to **explain its verification policy** on the page (EU material information) and **evidence its steps** to a regulator (UK "reasonable and proportionate steps"). Moderation decisions, removals and the reasons for them need an audit log.

---

## PART 6: Damage protection, guarantees and liability

### 6.1 Airbnb AirCover for Hosts (⚠ limits change)

- **Host damage protection: USD 3 million.** Covers home and contents when a guest does not pay for damage, including art and valuables, parked cars and boats, pet damage, deep cleaning and income lost to guest-caused cancellations. Airbnb states: "Host damage protection isn't insurance and isn't related to Host liability insurance." [VERIFIED: https://www.airbnb.com/resources/hosting-homes/a/how-aircover-for-hosts-works-469, published 2026-03-31]
- **Host liability insurance: USD 1 million**, underwritten by third-party insurers, for guest injury, guest property damage or theft and damage to common areas [VERIFIED: same].
- If a guest does not respond to or pay a damage reimbursement request within **24 hours**, the host can involve Airbnb [VERIFIED: same]. A 14-day documentation window for involving Airbnb Support is reported in help-centre summaries [WIDELY REPORTED: https://www.airbnb.com/help/article/3142, date unknown].
- AirCover bundles protection **with** identity verification and reservation screening as one host-facing promise [VERIFIED: same AirCover page, 2026-03-31].

### 6.2 Booking.com Partner Liability Insurance and damage programme

- **Partner Liability Insurance (PLI)**: per-incident limits of **EUR 1,000,000 (EEA), GBP 1,000,000 (UK), USD 1,000,000** elsewhere, with an aggregate programme limit of 10 million; insurers are Zurich Insurance entities (Steadfast Insurance Company in the US); claims administrator Crawford & Company; policy period 1 January–31 December 2026; eligible properties are **home-like types** (apartments, guest houses, villas, holiday homes) booked through Booking.com. "The PLI does not provide coverage for damage or loss to the Partner's property." [VERIFIED: https://admin.booking.com/partner-liability-insurance/policy.html, published 2026 (policy year 2026)]
- In Québec the policy does not satisfy the legal minimum and partners must arrange their own [VERIFIED: same].
- **Damage programme** (pilot as described in 2022): no deposit collected up front; the guest is told they "could be asked to pay up to EUR XYZ after check-out"; hosts file within **14 days** through the extranet; Booking.com collects if the guest accepts; the cap was reported as EUR 300 [WIDELY REPORTED: https://www.rentalscaleup.com/booking-com-partner-liability-insurance-and-damage-deposits-by-booking-com/, 2022]. ⚠ Over three years old; check current terms.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Booking.com's PLI explicitly targets **home-like properties, not hotels**, which shows the OTA borrowing the hosted-stays trust model for its alternative-accommodation supply. The architectural pieces are the same in both: a post-stay **claim workflow** (evidence upload, deadline, guest response window, platform adjudication), a **payment path that can charge the guest after checkout** (requiring a stored payment credential and, in the EU, SCA-compatible merchant-initiated charging), and integration with an insurer or claims administrator. The size of the platform-funded guarantee differs sharply: Airbnb's USD 3 million damage protection versus a capped guest-pays damage request.

---

## PART 7: Discrimination and fairness (Airbnb Project Lighthouse)

- **Problem statement.** Airbnb's anti-discrimination team defines an "experience gap" and an **acceptance rate gap** between groups of guests, measured on **perceived race**, because "discrimination is generally a result of one person's perception of another" [VERIFIED: https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf, published 2020-06].
- **Privacy design.** The system enforces **p-sensitive k-anonymity** "to prevent certain attribute disclosure" and uses "asymmetric encryption across trust boundaries to ensure that data flows are one-way"; a simulation methodology shows anonymised data still gives adequate statistical power [VERIFIED: same]. Reviewers named in the paper include Harvard's Data Privacy Lab, the EFF, Upturn and the Center for Democracy & Technology [VERIFIED: same].
- **Results (2021 data).** Booking Success Rates for US guests by perceived race, from a random sample of **750,000** reservation requests: Asian 93.4 %, Black **91.4 %**, Latino/Hispanic 94.4 %, white **94.1 %**, other/unknown 93.2 % [VERIFIED: https://news.airbnb.com/sixyearadupdate, published 2022-12-13].
- **Interventions.** Showing hosts the guest photo only after acceptance narrowed the Black–white gap by "less than half a percentage point"; Instant Book eligibility expanded in November 2022 to at least 5 million more people; more guests get reviews [VERIFIED: same].
- **Open-sourced tooling (2026).** Airbnb open-sourced `project-lighthouse-anonymize` and published two arXiv papers ("Core Mondrian" for scalable k-anonymity, and a data-quality framework using Pearson correlation, RILM and NMIv1); perceived race data "is never linked to individual accounts" and users can opt out in privacy settings [VERIFIED: https://medium.com/airbnb-engineering/project-lighthouse-part-3-introducing-project-lighthouse-anonymize-74f8b26653fb (via RSS feed), published 2026-08-25]. The post refers to results "shared in 2024", which were not fetched.

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Discrimination risk is structural in **request-to-book** flows, where a human host accepts or declines a named guest. OTA instant confirmation against hotel inventory removes the human decision, so the acceptance-rate gap barely exists. The architectural lever is the same one Airbnb used: **reduce discretionary human decisions** (more instant booking, delayed photo reveal) and **measure gaps with privacy-preserving pipelines**. Note that under GDPR Article 9, data "revealing racial or ethnic origin" is a special category whose processing is prohibited unless an exception applies [VERIFIED: http://publications.europa.eu/resource/celex/32016R0679, published 2016-04-27]; Airbnb's published method is US-only.

---

## PART 8: Short-term-rental regulation

### 8.1 EU Short-Term Rental Regulation (EU) 2024/1028

The single most important regulatory change for hosted-stays architecture in this period.

- **Scope excludes hotels.** A "unit" is furnished accommodation in the EU rented short-term, but **not** "hotels and similar accommodation" (NACE 55.1) or hostels and holiday-and-other short-stay accommodation listed under NACE 55.2, nor campsites (55.3) [VERIFIED: http://publications.europa.eu/resource/celex/32024R1028, published 2024-04-11]. "Host" covers professional and non-professional providers [VERIFIED: same].
- **Applies from 20 May 2026**; Member States had to adopt penalty rules by the same date [VERIFIED: same].
- **Registration.** Member-state registration procedures must run on host declarations, be online and allow the "automatic and immediate issue of a registration number, that shall not include personal data", with one registration per unit [VERIFIED: same, Article 4(3)].
- **Compliance by design (Article 7).** Platforms must design their interface so hosts **self-declare** whether the unit is in an area with a registration procedure; ensure hosts provide a registration number **before** the listing can be offered and display it clearly; make reasonable efforts to **randomly check** declarations and number validity using the single digital entry point; and inform authorities and hosts "without undue delay" of incorrect declarations, misuse or invalid numbers [VERIFIED: same].
- **Data reporting (Article 9).** For units in listed areas, platforms must collect and **monthly** transmit to the Member State's single digital entry point **activity data per unit**, with registration number, specific address and listing URL, "by machine-to-machine communication means". Small or micro platforms below a monthly average of **4,250 listings** in the previous quarter may report quarterly, by machine or manually [VERIFIED: same].
- **Activity data** means the number of nights rented and the number of guests per night "along with the country of residence of each guest" [VERIFIED: same, Article 3(12)].
- **Single digital entry point (Article 10).** Each Member State with registration must provide one, with an **API based on technical requirements defined by the Commission**, support for platform random checks, interfaces for competent authorities, and a freely accessible machine-readable database for validity checks [VERIFIED: same].
- **Orders.** Competent authorities may suspend or withdraw registration numbers and order platforms to **remove or disable listings** "without undue delay"; orders must contain reasons and information to identify the listing [VERIFIED: same, Article 6].
- **Retention by authorities.** Competent authorities keep activity data no longer than **18 months** and may share only de-identified aggregates for policy and research [VERIFIED: same, Article 12(3)].
- **Review.** The Commission evaluates the Regulation by 20 May 2031 [VERIFIED: same, Article 18].

[ASSUMPTION/JUDGEMENT] What this means for a platform's architecture:

1. **Listing data model**: a jurisdiction-resolved `registration_required` flag, a host-declared `registration_number`, a validation status and last-check timestamp, and a link from listing to unit address precise enough to report.
2. **Publish gate**: listing publication becomes a state machine that blocks "bookable" until registration is provided where required.
3. **Geo-to-jurisdiction service**: a maintained mapping from address to the areas listed by each Member State (the Article 13 lists), versioned because lists change.
4. **Regulatory reporting pipeline**: monthly per-country batch jobs aggregating nights and guests per unit, with guest country of residence, delivered machine-to-machine to 27 potential endpoints, with retries, receipts and reconciliation.
5. **Order intake**: a takedown-order workflow with SLAs, audit trail and host notification, shared with the DSA notice-and-action pipeline (Part 9.1).
6. **Guest country of residence** becomes a required booking field, which affects checkout design and GDPR minimisation.

**OTA vs hosted stays.** The hotel exclusion is the sharpest contrast in this brief. An OTA's hotel inventory is outside the Regulation; its **holiday-home and apartment inventory is inside it**. A mixed platform such as Booking.com therefore needs per-listing classification (hotel vs unit) that drives whether the registration gate and reporting apply [ASSUMPTION/JUDGEMENT].

### 8.2 National and city rules (⚠ all volatile)

| Place | Rule (as documented) | Evidence | Platform-side mechanism |
| --- | --- | --- | --- |
| Spain (national) | Royal Decree 1312/2024 set up a single registry and digital single window; registration number mandatory for booking-enabled platforms from 1 July 2025. **Supreme Court judgment 620/2026 annulled the national registry** provisions (State lacks competence) but **upheld the digital single window and platform data-sharing obligations** | Verified (CGPJ note, 21 May 2026) | Number capture and display; regional registries become the source of truth again; data sharing continues |
| Spain (enforcement) | Airbnb removed nearly 65,000 listings in 2025 at the consumer ministry's request | Widely reported | Bulk takedown from government lists |
| Barcelona | Non-renewal of about 10,000 tourist-apartment licences from **November 2028**; Constitutional Court upheld the Catalan decree in March 2025 | Verified (press) | Licence-expiry-driven delisting |
| Amsterdam | Entire-home rental max **30 nights a year**; registration number and annual permit since 1 April 2021; host must notify the city before each rental; city can ask Airbnb to block the calendar once the limit is reached | Verified (Airbnb help) | Night counter per unit; calendar block on request |
| Paris / France | Paris lowered the primary-residence cap from 120 to **90 nights** from 1 January 2025 under the 2024 "Le Meur" law; 13-character registration number shown on every listing | Widely reported / verified (number format) | Night cap enforcement; number format validation |
| New York City | Local Law 18: hosts register with the Office of Special Enforcement; platforms may **not process transactions** for unregistered rentals and must use the city's verification system; enforcement from **5 September 2023** | Verified (NYC OSE) | Verification API call before payment; 30-day minimum conversion |

Sources and detail:

- **Spain, legal basis.** Royal Decree 1312/2024 of 23 December 2024 implemented the EU Regulation; registration numbers became mandatory for platforms enabling online booking from 1 July 2025 [WIDELY REPORTED: https://www.spanishpropertyinsight.com/guides/short-term-rental-registry-and-ventanilla-unica-digital/, 2025 (updated 2026-06-06)].
- **Spain, Supreme Court.** Judgment 620/2026 (ECLI:ES:TS:2026:2148), on an appeal by the Generalitat Valenciana, annulled the provisions creating the "registro único de arrendamientos" because "el Estado carece de título competencial para establecer una regulación exhaustiva de un registro nacional"; it **dismissed** the appeal for the digital single window, its coordination, platform data-sharing obligations and statistical transmission. The court noted the EU Regulation requires adapting existing registration systems but does not require a single national registry [VERIFIED: https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-anula-el-Registro-Unico-de-arrendamientos-de-corta-duracion-por-considerar-que-el-Estado-carece-de-competencia-para-su-creacion, published 2026-05-21].
- **Spain, takedowns.** Airbnb removed nearly 65,000 listings at the request of Spain's consumer affairs ministry; a further 54,728 were identified as lacking a registration number [WIDELY REPORTED: https://www.catalannews.com/housing-crisis/item/airbnb-removes-almost-65000-illegal-listings-at-request-of-spains-consumer-affairs-ministry, 2025].
- **Barcelona.** The Constitutional Court rejected the PP's appeal and held that "tourist exploitation cannot be considered inherent to buildings designated by urban planning for residential use"; the city's non-renewal of about 10,000 licences takes effect in November 2028; the Catalan decree applies to 262 municipalities with housing pressure [VERIFIED: https://www.catalannews.com/society-science/item/barcelona-mayor-welcomes-constitutional-court-ruling-on-tourist-apartment-restrictions, published 2025-03-14].
- **Amsterdam.** "You can only rent out your entire home in Amsterdam for a maximum of 30 nights per year"; registration number plus permit since 1 April 2021; notify the city every time; "The City of Amsterdam can request Airbnb to block the calendar for the rest of the year"; B&Bs need a permit but have no night limit [VERIFIED: https://www.airbnb.com/help/article/860, date unknown (help page, fetched 2026-10-21)]. A reported cut to 15 nights in parts of the centre from 1 April 2026 rests on one blog and is **not verified** [WIDELY REPORTED: https://www.keycafe.com/s/ar/blog/understanding-short-term-rental-regulations-in-amsterdam, 2026].
- **France.** The registration number has 13 characters (5-digit INSEE commune code, 6-digit identifier, 2-character key) and must appear on every listing, including on platforms; operators of tourist furnished lets must keep a police registration form for non-French guests for 6 months [VERIFIED: https://www.service-public.gouv.fr/particuliers/vosdroits/F2043, published 2026-05-21 (last verified date)]. Paris's 90-night cap from 1 January 2025 [WIDELY REPORTED: https://www.houst.com/blog/reglementation-airbnb-paris, 2025]. Sources disagree on whether the national registration portal opened on 20 May 2026 or is due in Q4 2026 [WIDELY REPORTED: https://www.guestready.com/fr/blog/airbnb-90-jours/, 2026].
- **New York City.** Local Law 18 (adopted 9 January 2022) "requires short-term rental hosts to register with the Mayor's Office of Special Enforcement" and prohibits platforms from processing transactions for unregistered rentals; from 5 September 2023 OSE focused on platforms "using the city's verification system"; rentals of 30 consecutive days or more and Class B multiple dwellings are exempt; OSE maintains a Prohibited Buildings list [VERIFIED: https://www.nyc.gov/site/specialenforcement/registration-law/registration.page, date unknown (fetched 2026-10-21)]. Airbnb said unregistered listings would be converted to 30-day-minimum stays or deactivated [WIDELY REPORTED: https://thepointsguy.com/news/airbnb-nyc-regulations, 2023].
- **Government data portals.** Airbnb reported in 2021 that more than 100 local and national governments and destination marketing organisations used its **City Portal** [VERIFIED: https://news.airbnb.com/building-on-our-commitment-to-trust-2, published 2021-10-29].

[ASSUMPTION/JUDGEMENT] The pattern across jurisdictions is a small set of **rule primitives**: registration-number required (with a format and a validation API), night cap per unit per year, minimum stay length, guest-count limit, prohibited buildings or zones, licence expiry, and government-initiated takedown or calendar block. A platform that models these as **configurable per-jurisdiction policies** evaluated at publish time, at booking time and in nightly sweeps scales better than one that hard-codes each city. Night caps need a per-unit counter that is accurate across channels, which a single platform cannot see when a host multi-lists; that is why cities require host notifications (Amsterdam) or platform reporting (EU Regulation).

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] Hotels are licensed businesses outside these regimes. For an OTA, the STR rule engine applies only to its alternative-accommodation segment; for a hosted-stays platform it applies to almost all inventory and is on the critical path of publishing and booking.

---

## PART 9: Platform, consumer, data, payments and accessibility law

### 9.1 Digital Services Act (DSA)

- On 25 April 2023 the Commission designated 17 VLOPs and 2 VLOSEs; **Booking.com is a designated VLOP; Airbnb was not on the list** [WIDELY REPORTED: https://www.freevacy.com/news/european-commission/eu-commission-designates-19-very-large-organisations-under-dsa/3640, 2023]. Designated services had to comply within four months.
- The VLOP regime applies to platforms with **45 million or more** average monthly active recipients in the EU [VERIFIED: http://publications.europa.eu/resource/celex/32022R2065, published 2022-10-19, Article 33].
- Booking.com reports EU average monthly recipients "well above 45 million" for 1 January–30 June 2026, publishes transparency reports under DSA Articles 15, 24 and 42, and runs an ad repository created "following designation as a Very Large Online Platform" [VERIFIED: https://www.booking.com/content/dsa.html, published 2026].
- DSA Article 31 (**compliance by design**) requires marketplace interfaces that let traders give legally required pre-contract and compliance information [VERIFIED: http://publications.europa.eu/resource/celex/32022R2065, published 2022-10-19]. The STR Regulation borrows the same "compliance by design" language and states that DSA Chapter IV enforcement applies to its Articles 7(1) and 8 [VERIFIED: http://publications.europa.eu/resource/celex/32024R1028, published 2024-04-11].

[ASSUMPTION/JUDGEMENT] DSA duties that shape architecture for every accommodation platform: notice-and-action intake with statements of reasons, an internal complaint system, trader traceability (Part 2.3), and transparency reporting. VLOPs add systemic-risk assessments, independent audits, ad repositories and data access for researchers. Treat Airbnb's VLOP status as **unverified**; check the Commission's current list before writing that it is or is not designated.

### 9.2 Digital Markets Act (DMA)

- On **13 May 2024** the Commission designated Booking as a gatekeeper for its **online intermediation service Booking.com**, on the basis of Booking's 1 March 2024 self-assessment; Booking had **six months** to comply [VERIFIED: https://aztn.hr/ea/wp-content/uploads//2024/05/Commission_designates_Booking_as_a_gatekeeper_and_opens_a_market_investigation_into_X__.pdf (copy of Commission press release IP/24/2561), published 2024-05-13]. Fines can reach 10 % of worldwide turnover, 20 % for repeat infringement [VERIFIED: same].
- DMA Article 5(3): the gatekeeper "shall not prevent business users from offering the same products or services to end users through third-party online intermediation services or through their own direct online sales channel at prices or conditions that are different" (a ban on **wide and narrow price parity**) [VERIFIED: http://publications.europa.eu/resource/celex/32022R1925, published 2022-09-14].
- Article 5(4): business users may, free of charge, communicate and promote offers to end users acquired via the platform and conclude contracts with them outside the platform [VERIFIED: same].
- Article 5(2) restricts combining personal data across services without consent [VERIFIED: same].
- **CJEU C-264/23** (19 September 2024, Booking.com and Booking.com (Deutschland) v 25hours Hotel Company Berlin and others, reference from Rechtbank Amsterdam): parity clauses, "both wide and narrow", between online hotel reservation platforms and hotels **are not ancillary restraints** outside Article 101(1) TFEU; market definition for block exemption needs a concrete substitutability analysis [VERIFIED: http://publications.europa.eu/resource/celex/62023CJ0264, published 2024-09-19].

**OTA vs hosted stays.** [ASSUMPTION/JUDGEMENT] The DMA hits the OTA model directly: rate-parity enforcement (a rate-shopping service that penalised hotels selling cheaper elsewhere) is no longer allowed for Booking.com in the EU, and data-combination limits constrain cross-vertical personalisation (stays, flights, cars, attractions). Article 5(4) also legitimises hotels contacting platform-acquired guests, which interacts uneasily with the anti-fraud rule "never pay outside the platform" (Part 3). No hosted-stays platform is a designated gatekeeper as of the sources checked.

### 9.3 Platform-to-Business (P2B) Regulation (EU) 2019/1150

- Applies **from 12 July 2020** [VERIFIED: http://publications.europa.eu/resource/celex/32019R1150, published 2019-06-20].
- Article 5: online intermediation services must set out in their terms "the main parameters determining ranking" and the reasons for their relative importance, and describe any possibility to **influence ranking against remuneration** and its effects [VERIFIED: same].

[ASSUMPTION/JUDGEMENT] Relevant to both models: a hotel's commission-based visibility programme and a host's quality-based search placement both need explainable ranking parameters. Trust-and-safety demotions (for example for high cancellation or complaint rates) are ranking parameters too and must be describable.

### 9.4 Consumer protection: CPC actions and price display

- **Airbnb (CPC, 2018–2019).** Common position of **5 July 2018**; changes implemented by **11 July 2019**: "whenever properties are offered, the consumer is provided with the total price inclusive of all the applicable mandatory charges and fees", fairer terms, and distinguishing "professional traders from private peer hosts" [VERIFIED: https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en, published 2018–2020].
- **Booking.com (CPC, 2019–2020).** EU-wide commitments accepted **18 December 2019**, factsheet 18 December 2020, on how it presents offers, discounts and prices so consumers can "make informed comparisons" [VERIFIED: same].
- **Expedia Group (CPC, 2020).** Commitments 18 December 2020 for Expedia, ebookers and hotels.com [VERIFIED: same].
- **Omnibus Directive ranking disclosure.** Paid placement in search results must be disclosed; information on main ranking parameters is required [VERIFIED: http://publications.europa.eu/resource/celex/32019L2161, published 2019-11-27].
- **US: FTC rule on unfair or deceptive fees** (announced 17 December 2024) requires short-term lodging businesses (hotels and vacation rentals named) to show "the true total price inclusive of all mandatory fees" as the most prominent price; taxes may be excluded if disclosed before payment details are entered [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees, published 2024-12-17]. The press page links to a notice that the rule took effect on 12 May 2025 [VERIFIED: same page, related link].

[ASSUMPTION/JUDGEMENT] Price-display rules turn the **pricing service** into a compliance component: every surface that shows a price (search cards, maps, listing page, checkout, ads feeds) must compute the same all-in total including cleaning and service fees, per jurisdiction. Hosted-stays platforms with host-set cleaning fees were the original target (Airbnb 2018); OTAs were targeted on discounts, strike-through prices and scarcity presentation (Booking.com 2019). Trader/non-trader labelling of hosts flows from host onboarding (Part 2.3) into the listing page.

### 9.5 European Accessibility Act (EAA), Directive (EU) 2019/882

- Applies to services provided to consumers **after 28 June 2025**, including **e-commerce services** and the websites, apps and e-ticketing of passenger transport [VERIFIED: http://publications.europa.eu/resource/celex/32019L0882, published 2019-04-17].
- **Microenterprises providing services are exempt** from the accessibility requirements [VERIFIED: same, Article 4(5)].

[ASSUMPTION/JUDGEMENT] Booking and checkout flows of OTAs and hosted-stays platforms are e-commerce services in scope. Individual hosts are not service providers to the platform's consumers for EAA purposes, and small hotels may be microenterprises, but the platform's own interfaces are not exempt. **Accessibility of the accommodation** (step-free access, accessible bathrooms) is a separate matter of listing data quality, not EAA scope; both models need structured accessibility attributes that are verifiable. Not checked: national transposition and enforcement status.

### 9.6 GDPR: guest data, ID documents and retention

- Data minimisation: personal data must be "adequate, relevant and limited to what is necessary"; storage limitation: kept identifiable "for no longer than is necessary" [VERIFIED: http://publications.europa.eu/resource/celex/32016R0679, published 2016-04-27, Article 5(1)(c),(e)].
- **Biometric data "for the purpose of uniquely identifying a natural person"** is a special category whose processing is prohibited unless an Article 9(2) exception applies [VERIFIED: same, Article 9]. Selfie-to-ID face matching for verification falls here.
- Member States may set specific conditions for processing **national identification numbers** [VERIFIED: same, Article 87].
- France requires the police registration form for non-French guests to be kept for 6 months [VERIFIED: https://www.service-public.gouv.fr/particuliers/vosdroits/F2043, published 2026-05-21].

[ASSUMPTION/JUDGEMENT] Design consequences: store **verification outcomes** (verified, method, date, vendor reference) rather than ID images wherever possible; keep ID images in a segregated store with short, documented retention; obtain explicit consent or another Article 9 basis for face matching; treat guest-registration data required by national law (Spain, Italy, France, and other Schengen states require hotels and many rentals to record guest identity for the police) as a **property-side legal duty** that platforms may support but must not over-collect. The EU STR Regulation adds guest **country of residence** to activity data (Part 8.1), a new required field. OTAs often pass guest names and contact details to hotels under the agency model; hosted-stays platforms often mask guest contact details (relay email and phone), which is also an anti-fraud measure (Part 3).

### 9.7 Payments regulation summary

See Part 3.4 for SCA exemptions. [ASSUMPTION/JUDGEMENT] Payouts to individual hosts make hosted-stays platforms subject to payment-licensing questions (holding funds for others), anti-money-laundering and sanctions screening on payees, and DAC7 reporting (Part 2.3). OTAs in the agency model avoid holding guest funds; in the merchant model they hold funds and face the same questions for hotel remittances.

---

## PART 10: Reference architecture for trust and compliance (judgement)

[ASSUMPTION/JUDGEMENT] The whole Part is the analyst's synthesis for chapter writers; no company has published this design.

| Capability | Inputs | Decision point | Hosted stays emphasis | OTA emphasis |
| --- | --- | --- | --- | --- |
| Identity and verification service | ID document, selfie, databases, tax IDs | Before booking or hosting; before payout | Guests and hosts | Partners (KYBC), small properties |
| Partner/host account security | Login, device, session signals | Login; sensitive actions (payout change, bulk messaging) | Host ATO | **Extranet ATO** (dominant 2023–25 threat) |
| Reservation risk engine | Account history, trip features, payment signals | Synchronous at booking | Party / damage risk + payment fraud | Payment fraud, no-show |
| Messaging safety | Message text, URLs, sender session risk | On send and on render | Off-platform payment asks | Phishing from hijacked hotel accounts |
| Listing integrity | Address, photos, registration number, licences | Publish gate; periodic sweeps | Fake listings; STR registration | Hotel identity; holiday-home registration |
| Jurisdiction policy engine | Unit location, jurisdiction rules | Publish, booking, nightly sweep | Night caps, registration, zones | Only alternative-accommodation inventory |
| Regulatory reporting | Stays, guests, country of residence, host tax data | Monthly / annual batch | EU STR Art. 9; DAC7 for most hosts | DAC7 for small partners; STR for homes |
| Orders and notices | Government orders, DSA notices | Case workflow with SLA | Takedowns, calendar blocks | Takedowns, ad repository |
| Reviews integrity | Reservation of record, moderation | Post-stay | Two-way, blind reveal | One-way |
| Claims and guarantees | Evidence, payment credential, insurer | Post-stay | Large platform-funded guarantees | Liability insurance for home-like stock |

Design principles to carry into chapters:

1. **Make the reservation the root of trust.** Reviews, damage claims, regulatory activity data, and fraud labels all hang off the reservation record. A clean, auditable reservation system of record is the foundation of the trust stack.
2. **Gate, then sweep.** Check at publish and booking time (synchronous, fail closed for legal gates such as registration), then re-check in batch (random checks under EU STR Art. 7(1)(c), licence expiry, night caps).
3. **Policies as data.** Jurisdiction rules, holiday risk modes and verification requirements change faster than code; keep them in versioned configuration with audit history.
4. **Separate evidence from decisions.** Store verification and moderation outcomes with reasons and retention policies; keep raw ID images and message content in restricted stores.
5. **Design for the regulator as a client.** Machine-to-machine reporting to single digital entry points, verification APIs (NYC), and order intake are external integrations with SLAs, not ad-hoc exports.

---

## Key numbers

| Number | What it is | Source | Date |
| --- | --- | --- | --- |
| 20 May 2026 | EU STR Regulation applies | Regulation (EU) 2024/1028 | 2024-04-11 |
| Monthly | EU STR activity-data reporting cadence for platforms | Regulation (EU) 2024/1028 Art. 9 | 2024-04-11 |
| 4,250 | Monthly average listings below which small platforms may report quarterly | Regulation (EU) 2024/1028 Art. 9(2) | 2024-04-11 |
| 18 months | Max retention of activity data by competent authorities | Regulation (EU) 2024/1028 Art. 12(3) | 2024-04-11 |
| 45 million | EU monthly active recipients threshold for VLOP | DSA Art. 33 | 2022-10-19 |
| 17 Feb 2024 | DSA general application date | DSA Art. 93 | 2022-10-19 |
| 25 Apr 2023 | Booking.com designated VLOP | Freevacy (secondary) | 2023 |
| 13 May 2024 | Booking designated DMA gatekeeper | Commission IP/24/2561 | 2024-05-13 |
| 19 Sep 2024 | CJEU C-264/23: parity clauses not ancillary restraints | CJEU | 2024-09-19 |
| 12 Jul 2020 | P2B Regulation applies | Regulation (EU) 2019/1150 | 2019-06-20 |
| 28 May 2022 | Omnibus review rules apply | Directive (EU) 2019/2161 | 2019-11-27 |
| 6 Apr 2025 | UK DMCC fake-review bans in force | DMCC Act Sch. 20 para 13 | 2024 |
| 14 Aug 2024 | FTC fake-reviews rule announced | FTC | 2024-08-14 |
| 12 May 2025 | FTC fees rule effective (lodging, total price) | FTC | 2024-12-17 |
| 28 Jun 2025 | European Accessibility Act applies to services | Directive (EU) 2019/882 | 2019-04-17 |
| 14 Sep 2019 | PSD2 SCA RTS applies | Delegated Regulation (EU) 2018/389 | 2017-11-27 |
| EUR 30 / 0.13 %–0.01 % | SCA low-value cap; TRA reference fraud rates (≤100 / ≤250 / ≤500 EUR) | Delegated Regulation (EU) 2018/389 | 2017-11-27 |
| 1 Jan 2023 | First DAC7 reportable period | Directive (EU) 2021/514 | 2021-03-22 |
| >2,000 | DAC7 rental activities per listing above which an entity seller is excluded | Directive (EU) 2021/514 | 2021-03-22 |
| End June 2023 | All guests booking homes and primary Hosts must be ID-verified (Airbnb) | Airbnb newsroom | 2023-06-29 |
| 81 % / 97 % | Share of stays with both parties verified, global / US (superseded) | Airbnb newsroom | 2021-10-29 |
| 35 % | Drop in unauthorised parties in Airbnb's Australia pilot | Airbnb newsroom | 2022-08-16 |
| 0.039 % | Global Airbnb reservations with a party allegation (2022) | Airbnb newsroom | 2023-08-31 |
| 55 % | Drop in party-report rate since the ban (year-over-two-year) | Airbnb newsroom | 2023-08-31 |
| >20,000 | US guests redirected from entire homes, July 4 2025 | Airbnb newsroom | 2026-06-24 |
| <0.06 % | US Airbnb stays with a party report (2025) | Airbnb newsroom | 2026-06-24 |
| USD 3M / USD 1M | AirCover host damage protection / host liability insurance | Airbnb | 2026-03-31 |
| EUR/GBP/USD 1M | Booking.com Partner Liability Insurance per incident (home-like properties) | Booking.com policy | 2026 |
| 91.4 % vs 94.1 % | Booking Success Rate, guests perceived Black vs white (US, 2021 data) | Airbnb newsroom | 2022-12-13 |
| 750,000 | Reservation requests sampled for Lighthouse 2021 measurement | Airbnb newsroom | 2022-12-13 |
| 500–900 % | Booking.com-reported rise in travel scams over ~18 months | Silicon UK (secondary) | 2024-06-24 |
| 85 million | Fraudulent reservations Booking.com said it blocked in 2023 | Krebs (secondary) | 2024-11-01 |
| July 2024 | Telekopye accommodation scams overtake its marketplace scams | ESET | 2024-10-10 |
| 30 nights | Amsterdam entire-home annual cap | Airbnb help | fetched 2026-10-21 |
| 90 nights | Paris primary-residence cap from 2025 | Houst (secondary) | 2025 |
| ~10,000 / Nov 2028 | Barcelona tourist-apartment licences not renewed | Catalan News | 2025-03-14 |
| 5 Sep 2023 | NYC Local Law 18 enforcement start | NYC OSE | fetched 2026-10-21 |
| 21 May 2026 | Spanish Supreme Court annuls national STR registry (judgment 620/2026) | CGPJ | 2026-05-21 |
| ~65,000 | Spanish listings Airbnb removed at ministry request (2025) | Catalan News (secondary) | 2025 |

## Open questions / not verifiable

- **Booking.com guest-side controls.** Does Booking.com verify guest identity for any segment (for example holiday homes)? How does it scan messages and links? Has it adopted passkeys or forced MFA for all partners? No primary source found.
- **Airbnb VLOP status under the DSA.** Not on the April 2023 list; later designations not checked.
- **Airbnb risk-model internals.** Model type, features beyond the 2022 list, latency budget and holiday thresholds are not public in the sources fetched. The 2018 "targeted friction" engineering post could not be read (403).
- **Airbnb fake-listing statistics** (removals and prevented listings) — not fetched.
- **Booking.com damage programme today.** Current cap, countries and whether guest payment is voluntary; the only source is from 2022.
- **Enforcement actions not verified here:** Spain's competition authority fine on Booking.com (2024); Spain's consumer ministry fine on Airbnb (reported December 2025, over EUR 64 million); Italian tax settlements with Airbnb; any Commission DSA requests for information to Booking.com on scams. Check before citing.
- **Paris and France.** Exact legal text of the 2024 Le Meur law (Loi n° 2024-1039), the Paris council decision on 90 nights, and the national registration portal's launch date.
- **Amsterdam 15-night centre cap** from April 2026 — single blog source.
- **Spain after the Supreme Court.** How regional registries and the digital single window now interact with EU Regulation reporting; whether platforms still require the national number.
- **Single digital entry points.** Which Member States had live endpoints on 20 May 2026, and the Commission's technical API specification.
- **FTC fake-reviews rule effective date** in the Federal Register (widely cited as 21 October 2024).
- **Two-way review mechanics** (blind reveal windows) at Airbnb and Vrbo.
- **Expedia/Vrbo, Agoda and Trip.com** trust programmes — no sources.
- **Schengen guest-registration duty** (Convention implementing the Schengen Agreement, Article 45) — text not fetched; national implementations (Spain's SES.Hospedajes, Italy's Alloggiati Web) not checked.

## Source list

| # | Title | Publisher / author | Year | URL |
| --- | --- | --- | --- | --- |
| 1 | Regulation (EU) 2024/1028 on data collection and sharing relating to short-term accommodation rental services | EU (Publications Office) | 2024 | http://publications.europa.eu/resource/celex/32024R1028 |
| 2 | Regulation (EU) 2022/2065, Digital Services Act | EU (Publications Office) | 2022 | http://publications.europa.eu/resource/celex/32022R2065 |
| 3 | Regulation (EU) 2022/1925, Digital Markets Act | EU (Publications Office) | 2022 | http://publications.europa.eu/resource/celex/32022R1925 |
| 4 | Regulation (EU) 2019/1150, Platform-to-Business | EU (Publications Office) | 2019 | http://publications.europa.eu/resource/celex/32019R1150 |
| 5 | Directive (EU) 2019/2161, Omnibus (better enforcement and modernisation) | EU (Publications Office) | 2019 | http://publications.europa.eu/resource/celex/32019L2161 |
| 6 | Directive (EU) 2019/882, European Accessibility Act | EU (Publications Office) | 2019 | http://publications.europa.eu/resource/celex/32019L0882 |
| 7 | Council Directive (EU) 2021/514, DAC7 | EU (Publications Office) | 2021 | http://publications.europa.eu/resource/celex/32021L0514 |
| 8 | Commission Delegated Regulation (EU) 2018/389, SCA RTS | EU (Publications Office) | 2017 | http://publications.europa.eu/resource/celex/32018R0389 |
| 9 | Regulation (EU) 2016/679, GDPR | EU (Publications Office) | 2016 | http://publications.europa.eu/resource/celex/32016R0679 |
| 10 | Judgment C-264/23, Booking.com v 25hours Hotel Company and others | Court of Justice of the EU | 2024 | http://publications.europa.eu/resource/celex/62023CJ0264 |
| 11 | Commission designates Booking as a gatekeeper and opens a market investigation into X (IP/24/2561, PDF copy) | European Commission | 2024 | https://aztn.hr/ea/wp-content/uploads//2024/05/Commission_designates_Booking_as_a_gatekeeper_and_opens_a_market_investigation_into_X__.pdf |
| 12 | EU Commission designates 19 "Very Large" organisations under DSA | Freevacy | 2023 | https://www.freevacy.com/news/european-commission/eu-commission-designates-19-very-large-organisations-under-dsa/3640 |
| 13 | Digital Services Act (Booking.com DSA page) | Booking.com | 2026 | https://www.booking.com/content/dsa.html |
| 14 | Accommodation booking: coordinated actions | European Commission | 2018–2020 | https://commission.europa.eu/live-work-travel-eu/consumer-rights-and-complaints/enforcement-consumer-protection/coordinated-actions/accommodation-booking_en |
| 15 | Federal Trade Commission announces final rule banning fake reviews and testimonials | US FTC | 2024 | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials |
| 16 | FTC announces bipartisan rule banning junk ticket and hotel fees | US FTC | 2024 | https://www.ftc.gov/news-events/news/press-releases/2024/12/federal-trade-commission-announces-bipartisan-rule-banning-junk-ticket-hotel-fees |
| 17 | Digital Markets, Competition and Consumers Act 2024, Schedule 20 | UK legislation.gov.uk | 2024 | https://www.legislation.gov.uk/ukpga/2024/13/schedule/20 |
| 18 | Fake reviews (CMA208) | UK CMA | 2025 | https://www.gov.uk/government/publications/fake-reviews-cma208 |
| 19 | An update on identity verification on Airbnb | Airbnb newsroom | 2023 | https://news.airbnb.com/an-update-on-identity-verification-on-airbnb |
| 20 | Building on our commitment to trust | Airbnb newsroom | 2021 | https://news.airbnb.com/building-on-our-commitment-to-trust-2 |
| 21 | New anti-party technology in the US and Canada | Airbnb newsroom | 2022 | https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada |
| 22 | An update on our work to crack down on parties and disruptive behavior | Airbnb newsroom | 2023 | https://news.airbnb.com/an-update-on-our-work-to-crack-down-on-parties-and-disruptive-behavior |
| 23 | Our anti-party system returns for July 4 weekend | Airbnb newsroom | 2026 | https://news.airbnb.com/airbnbs-anti-party-system-returns-for-july-4-weekend |
| 24 | Rolling out our anti-party system for Halloween (not fetched) | Airbnb newsroom | 2025 | https://news.airbnb.com/airbnb-rolls-out-anti-party-system-for-halloween/ |
| 25 | 2025 Summer Release (not fetched) | Airbnb newsroom | 2025 | https://news.airbnb.com/airbnb-2025-summer-release |
| 26 | How AirCover for Hosts works | Airbnb Resource Center | 2026 | https://www.airbnb.com/resources/hosting-homes/a/how-aircover-for-hosts-works-469 |
| 27 | AirCover help article (search summary only) | Airbnb Help Center | date unknown | https://www.airbnb.com/help/article/3142 |
| 28 | Responsible hosting in Amsterdam (help article 860) | Airbnb Help Center | date unknown | https://www.airbnb.com/help/article/860 |
| 29 | A six-year update on Airbnb's work to fight discrimination | Airbnb newsroom | 2022 | https://news.airbnb.com/sixyearadupdate |
| 30 | Measuring discrepancies in Airbnb guest acceptance rates using anonymized demographic data (Project Lighthouse) | Airbnb anti-discrimination team (Basu et al.) | 2020 | https://news.airbnb.com/wp-content/uploads/sites/4/2020/06/Project-Lighthouse-Airbnb-2020-06-12.pdf |
| 31 | Project Lighthouse — Part 3: Introducing project-lighthouse-anonymize | Airbnb Tech Blog (A. Bloomston) | 2026 | https://medium.com/airbnb-engineering/project-lighthouse-part-3-introducing-project-lighthouse-anonymize-74f8b26653fb |
| 32 | Flexible Authentication: Reimagining authentication for millions of users at Airbnb | Airbnb Tech Blog (J. Santos, M. Barry) | 2026 | https://medium.com/airbnb-engineering/flexible-authentication-reimagining-authentication-for-millions-of-users-at-airbnb-3a8a4c917137 |
| 33 | Fighting financial fraud with targeted friction (not readable, 403) | Airbnb Tech Blog | 2018 | https://medium.com/airbnb-engineering/fighting-financial-fraud-with-targeted-friction-82d950d8900e |
| 34 | Partner Liability Insurance policy summary | Booking.com | 2026 | https://admin.booking.com/partner-liability-insurance/policy.html |
| 35 | Booking.com's new €1,000,000 Partner Liability Insurance and Damage Deposits | Rental Scale-Up | 2022 | https://www.rentalscaleup.com/booking-com-partner-liability-insurance-and-damage-deposits-by-booking-com/ |
| 36 | Booking.com reviews page (search summary only; fetch 404) | Booking.com | date unknown | https://www.booking.com/reviews.html |
| 37 | Booking.com reviews policy | Hostaway | date unknown | https://www.hostaway.com/booking-com-reviews-policy-and-how-to-remove-reviews-on-booking-com |
| 38 | Vidar infostealer steals Booking.com credentials in fraud scam | Secureworks CTU (on Sophos) | 2023 | https://www.sophos.com/en-us/blog/vidar-infostealer-steals-booking-com-credentials-in-fraud-scam |
| 39 | Booking.com customers targeted in hotel booking scam | Help Net Security (H. Labus) | 2023 | https://www.helpnetsecurity.com/2023/12/04/booking-com-hotel-booking-scam/ |
| 40 | Booking.com phishers may leave you with reservations | KrebsOnSecurity (B. Krebs) | 2024 | https://krebsonsecurity.com/2024/11/booking-com-phishers-may-leave-you-with-reservations/ |
| 41 | Telekopye hits new hunting ground: hotel booking scams | ESET WeLiveSecurity (J. Souček, R. Jizba) | 2024 | https://www.welivesecurity.com/en/eset-research/telekopye-hits-new-hunting-ground-hotel-booking-scams/ |
| 42 | Scammers target Airbnb and Booking.com users | Help Net Security | 2024 | https://www.helpnetsecurity.com/2024/10/11/telekopye-booking-platforms-scams/ |
| 43 | Phishing campaign impersonates Booking.com, delivers a suite of credential-stealing malware | Microsoft Threat Intelligence | 2025 | https://www.microsoft.com/en-us/security/blog/2025/03/13/phishing-campaign-impersonates-booking-com-delivers-a-suite-of-credential-stealing-malware/ |
| 44 | Booking.com warns of AI-fuelled 900 percent scam surge | Silicon UK | 2024 | https://silicon.co.uk/ai/booking-com-scam-surge-ai-569105 |
| 45 | Online-Sicherheit bei Buchungsplattformen (not fetched) | WKO Wien | date unknown | https://www.wko.at/wien/tourismus-freizeitwirtschaft/hotellerie/online-sicherheit-bei-buchungplattformen |
| 46 | Airbnb bans the use of indoor security cameras on all properties | ABC7 News | 2024 | https://abc7news.com/airbnb-bans-the-use-of-indoor-security-cameras-on-all-properties/14516158/ |
| 47 | El Tribunal Supremo anula el Registro Único de arrendamientos de corta duración | Consejo General del Poder Judicial | 2026 | https://www.poderjudicial.es/cgpj/es/Poder-Judicial/Tribunal-Supremo/Noticias-Judiciales/El-Tribunal-Supremo-anula-el-Registro-Unico-de-arrendamientos-de-corta-duracion-por-considerar-que-el-Estado-carece-de-competencia-para-su-creacion |
| 48 | Short-term rental registry and Ventanilla Única Digital | Spanish Property Insight | 2025 (updated 2026) | https://www.spanishpropertyinsight.com/guides/short-term-rental-registry-and-ventanilla-unica-digital/ |
| 49 | Airbnb removes almost 65,000 illegal listings at request of Spain's consumer affairs ministry | Catalan News | 2025 | https://www.catalannews.com/housing-crisis/item/airbnb-removes-almost-65000-illegal-listings-at-request-of-spains-consumer-affairs-ministry |
| 50 | Barcelona mayor welcomes Constitutional Court ruling on tourist apartment restrictions | Catalan News | 2025 | https://www.catalannews.com/society-science/item/barcelona-mayor-welcomes-constitutional-court-ruling-on-tourist-apartment-restrictions |
| 51 | Faire de sa résidence secondaire une location de vacances (meublé de tourisme) | Service-Public.fr | 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F2043 |
| 52 | Réglementation Airbnb Paris (not fetched) | Houst | 2025 | https://www.houst.com/blog/reglementation-airbnb-paris |
| 53 | Limite Airbnb 90 jours (not fetched) | GuestReady | 2026 | https://www.guestready.com/fr/blog/airbnb-90-jours/ |
| 54 | Understanding short-term rental regulations in Amsterdam (not fetched) | Keycafe | 2026 | https://www.keycafe.com/s/ar/blog/understanding-short-term-rental-regulations-in-amsterdam |
| 55 | Registration Law (Local Law 18) | NYC Mayor's Office of Special Enforcement | date unknown | https://www.nyc.gov/site/specialenforcement/registration-law/registration.page |
| 56 | Airbnb NYC regulations (not fetched) | The Points Guy | 2023 | https://thepointsguy.com/news/airbnb-nyc-regulations |
