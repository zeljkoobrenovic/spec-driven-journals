# Research brief: Marketplace trust, safety, fraud prevention, moderation, identity and regulation

Prepared 19 October 2026 for chapter writers of *LISTED: Architecting Large-Scale Classifieds and Marketplace Platforms*. The brief covers two things. The first is the fraud and abuse that classifieds platforms face, and the engineering used against it. The second is the regulation that now shapes moderation, trader identity and evidence-keeping in the EU, the UK and the US. Named companies appear because they published something. That is not an endorsement.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (19 October 2026) and supports the claim. Paraphrases stay close to the source, and quotations are marked. "Date unknown" means the page carries no publication date.
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source, a search-result summary of a page that could not be fetched, or vendor or company marketing.
- **[ASSUMPTION/JUDGEMENT]**: the analyst's industry knowledge or inference, not checked against a primary source in this session. Every architectural statement about a proprietary system carries this tag. Re-verify before printing it as fact, or present it as a reference-architecture judgement.

**Research limitations (read these first).**

1. **EUR-Lex was unreachable.** It sat behind a WAF challenge, so the official Official Journal texts (DSA, P2B, Omnibus, DAC7, eIDAS 2, EPBD) could not be fetched. DSA article contents are therefore verified against `eu-digital-services-act.com`. That site reproduces Regulation (EU) 2022/2065 article by article, but it is unofficial. Check article wording against EUR-Lex before quoting it in print.
2. **Medium returned HTTP 403** for the Adevinta, leboncoin and Airbnb engineering blogs, and `tech.olx.com` also returned 403. The well-known first-party classifieds T&S engineering posts could not be read. Where they are mentioned, they are tagged ASSUMPTION/JUDGEMENT or WIDELY REPORTED.
3. **The session-wide web-search quota ran out partway through.** Later topics rely on direct fetches of known URLs. These include Zillow, Facebook Marketplace's own statistics, the text of the CMA fake-review guidance, the Omnibus article text, BankID/itsme, eIDAS relying-party deadlines and Ofcom's register of categorised services. Where no fetch worked, the claim is tagged ASSUMPTION/JUDGEMENT.

**Volatility.** ⚠ marks facts likely to change within 12 months: designations, consultation outcomes, repeal proposals, application dates, ownership and product names. Time-sensitive facts are stated "as of" October 2026.

---

## PART 1: The threat model: a classifieds fraud typology

### 1.1 Why classifieds differ from transactional marketplaces

Most classifieds platforms (Kleinanzeigen, leboncoin, Marktplaats, OLX, Gumtree, Facebook Marketplace and the property and vehicle portals) are **lead-generation** businesses. Buyer and seller meet on the platform, but the money often moves off it. That one fact drives the whole threat model:

- The platform sees the listing and the conversation. It often does **not** see the payment, so it cannot reverse one.
- Most fraud is **authorised push payment (APP)** fraud: the victim willingly sends money, usually by bank transfer. UK Finance's definition of a purchase scam says it directly. Although "many online platforms offer secure payment options, the criminal will persuade their victim to pay via a bank transfer instead" [VERIFIED: https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf, published 2026-06-12].
- The controls a classifieds platform can operate are therefore mostly **pre-payment**: who can list, what can be listed, what can be said in messages, and steering users towards a protected in-platform payment. [ASSUMPTION/JUDGEMENT]

### 1.2 Scale: the UK numbers are the best public data

UK Finance publishes the most granular public purchase-scam series. Its 2026 report covers calendar year 2025 [VERIFIED: UK Finance Annual Fraud Report 2026 PDF, 2026-06-12; landing page https://www.ukfinance.org.uk/policy-and-guidance/reports/annual-fraud-report-2026, published 2026-06-15]:

| Metric (purchase scams, UK) | 2020 | 2023 | 2024 | 2025 | Change 2024→25 |
| --- | --- | --- | --- | --- | --- |
| Cases | 84,292 | 156,516 | 166,798 | 175,809 | +5% |
| Payments | 107,493 | 219,594 | 239,791 | 262,876 | +10% |
| Losses | £51.1m | £85.9m | £98.7m | £118.1m | +20% |
| Returned to victims | £14.6m | £55.8m | £60.7m | £91.8m | +51% |

- In 2025, 71% of all APP scam cases were purchase scams. Purchase scams also had the lowest average case value of the eight APP types, £671, up from £549 in 2023 [VERIFIED: same PDF].
- 78% of purchase-scam losses were returned to victims in 2025 [VERIFIED: same PDF]. [ASSUMPTION/JUDGEMENT] The jump in reimbursement reflects the UK's mandatory APP reimbursement regime, which took effect in October 2024. The cost lands on the banks, which explains why banks lobby for platform obligations (below).
- 66% of APP cases (32% of losses) were "enabled by online sources" in 2025. Online-enabled cases "tend to include lower-value scams such as purchase fraud" [VERIFIED: same PDF]. The online share of volume was 78% in 2022, 76% in 2023 and 70% in 2024 [VERIFIED: same PDF].
- UK Finance's typical purchase-scam scenarios are a car or a technology product advertised cheaply, fake holiday rentals and concert tickets [VERIFIED: same PDF].
- **Policy ask aimed at marketplaces.** UK Finance asks the government to "legislate to mandate seller verification and secure payment protections on online marketplaces". It also asks Ofcom to "move swiftly" with tougher Online Safety Act fraud duties [VERIFIED: same PDF]. Financier Worldwide reports the same ask: marketplaces should verify sellers and use secure payment mechanisms rather than off-platform bank transfers [VERIFIED: https://www.financierworldwide.com/fw-news/2026/7/2/uk-fraud-losses-close-to-13bn-reveals-new-report, published 2026-07-02]. ⚠ This is a lobbying position, not law, as of October 2026.

**Platform-specific UK evidence (all secondary or bank-sourced):**

| Source | Finding | Tag |
| --- | --- | --- |
| TSB (Jan 2024) | Its fraud team sampled 100 Facebook Marketplace posts and judged 34% to be scams. 73% of TSB's purchase-fraud cases came from Facebook Marketplace | [VERIFIED: https://fstech.co.uk/fst/Over_Third_Of_Facebook_Marketplace_Ads_Are_Scams_Warns_TSB.php, published 2024-01-18]. The sample is tiny and the method informal. It is one bank's customer base. |
| Lloyds (Dec 2023) | Purchase scams +42% year on year. 78% of purchase scams start on social media. Nearly half of holiday scams originate on Facebook Marketplace | [VERIFIED: https://www.crowdfundinsider.com/2023/12/218012-fraudulent-activities-uk-purchase-scams-rising-by-42-compared-to-last-year-report/, published 2023-12-12]. This is a secondary write-up of a bank press release. |
| Which? survey (Jan 2024 fieldwork) | 32% of second-hand buyers reported a scam in the past two years. By platform: Depop 57%, Shpock 53%, Preloved 51%, Nextdoor 51%, Amazon Marketplace 35%, Gumtree 29%, eBay 29%, Facebook Marketplace 24%, Vinted 22% | [VERIFIED: https://www.which.co.uk/policy-and-insight/article/a-third-of-buyers-have-experienced-a-scam-on-popular-second-hand-marketplaces-in-the-last-two-years-which-warns-aEea68N4nnah, published 2024-05-09]. Self-reported, with a broad definition of "scam" that includes wrong or counterfeit goods. |
| Which? undercover test | Fake camera ads on Facebook Marketplace, Gumtree and Nextdoor, using new identities, devices and Wi-Fi, stayed live for at least half a day. On Facebook, after the price was halved and Apple gift cards demanded, the ad stayed live for almost 48 hours. Gumtree's first scam-style ad was blocked, but edited versions passed review "in minutes" | [VERIFIED: https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1, published 2024-12-12] |
| Which? buyer protection finding | Amazon Marketplace, Depop, eBay, Preloved, Vinted and Shpock offer some buyer protection. Facebook Marketplace, Gumtree and Nextdoor do not. Yet 25% of Facebook Marketplace and 25% of Gumtree buyers believed theirs did | [VERIFIED: same, 2024-12-12] |

**Architectural reading.** Which?'s Gumtree result is the key detail for a moderation designer. Gumtree's first submission was blocked. **Edits made after approval** then passed review in minutes. Edit-after-approval is a classic gap: moderation must re-score on every material edit (price drop, payment terms, contact details), not only at creation [ASSUMPTION/JUDGEMENT, grounded in the Which? test above]. Gumtree's head of trust and safety told Which? that flagged ads are investigated within four hours [VERIFIED: https://www.which.co.uk/news/article/its-a-steal-how-we-listed-fake-bargains-on-marketplace-websites-aQDLs8m1bFWa, published 2024-12-12].

### 1.3 Typology

Each row gives the mechanism, the platform's best leverage point and the evidence.

| Scam type | Mechanism | Primary signals / leverage | Evidence |
| --- | --- | --- | --- |
| **Advance-payment / non-delivery** | Fake seller asks for bank transfer, PayPal "Friends and Family" or gift cards before shipping, then disappears | Below-market price; stock photos; new or thin profile; payment terms in text; refusal to meet | Which? lists bargain prices, unusual payment requests (bank transfer, gift cards, PayPal F&F), stock images and thin or new profiles [VERIFIED: Which? 2024-12-12]. Kleinanzeigen warns against Western Union, PaySafe, MoneyGram and cash in envelopes, and tells PayPal users to pick "Goods and services" [VERIFIED: https://themen.kleinanzeigen.de/sicherheitshinweise/, date unknown] |
| **Fake payment link / phishing ("pay via our safe delivery service")** | Fake *buyer* sends the *seller* a link or QR code to a counterfeit "payment received" or courier page that harvests card or bank data | URLs and QR codes in chat; off-platform domains impersonating the platform; spoofed emails | OLX detects fraudulent QR codes sent through chat, which can lead to card-harvesting phishing sites, with "80% precision" [VERIFIED: https://www.olxgroup.com/?p=4590, published 2026-01-28]. Kleinanzeigen warns of spoofed emails and of fake "Kleinanzeigen" chat messages written by the chat partner [VERIFIED: Kleinanzeigen safety page]. A French consumer group reports fake leboncoin payment-confirmation emails linking to counterfeit payment pages [WIDELY REPORTED: https://connexionfrance.com/article/Practical/Money/French-consumer-group-warns-against-new-online-purchasing-scam, date not captured] |
| **Manipulated / fake images in chat** | Fraudster sends fake payment screenshots or doctored documents in chat | Image classification in messaging | OLX: in Poland "fraudulent images make up about 30% of fraud cases". Its "Chat Images GenAI" system blocks suspicious chat images in real time, before they reach users. It is live in Poland, Portugal, Bulgaria and Romania [VERIFIED: OLX, 2026-01-28] |
| **Fake rental listings** | Copied photos of a real property, a below-market rent and a "landlord abroad" who wants a deposit before viewing | Duplicate or stolen images; price anomaly; no viewing; lister not a registered agent | UK Finance names fake holiday rentals [VERIFIED: UK Finance 2026]. Rightmove says it "carr[ies] out checks on all of our customers before we allow them to advertise". Its agents must belong to a government-approved redress scheme, and it warns that "Rightmove"-branded ads elsewhere are not genuine [VERIFIED: https://www.rightmove.co.uk/guides/?p=385, date unknown]. Industry sources say scammers favor open platforms (Gumtree, Facebook Marketplace) because the main UK portals accept only registered agents [WIDELY REPORTED: search summary of letting-industry sources, 2024–2025] |
| **Vehicle deposit scams** | A car priced to sell fast; "seller" asks a deposit to "hold" it, or offers delivery through a fake escrow or shipping firm | Price vs. valuation model; VIN/plate reuse across listings; external escrow domains in text | Cars are UK Finance's first-named purchase-scam example [VERIFIED: UK Finance 2026]. Lloyds names cars among common targets [VERIFIED: CrowdFund Insider 2023-12-12]. The deposit mechanics are [ASSUMPTION/JUDGEMENT] |
| **Triangulation (Dreiecksbetrug)** | Fraudster lists a real seller's item. The victim buyer pays the real seller directly, believing the money is for the fraudster's item. The fraudster collects the goods or a parallel payment, and two victims dispute each other | Cloned listing with different contact data; payment reference mismatch | Kleinanzeigen's safety page does **not** name the scheme. Mechanics are [ASSUMPTION/JUDGEMENT]. Duplicate detection is the main counter (see 3.4) |
| **Overpayment** | Fake buyer "overpays" (fake cheque or fake transfer screenshot) and asks for the difference back | Payment-proof images; refund request keywords | Consumer guides describe it for Kleinanzeigen [WIDELY REPORTED: search summary, unreliable blog]. Treat as [ASSUMPTION/JUDGEMENT] |
| **Account takeover (ATO)** | Credential phishing or stuffing. An aged, reputable account is then used to list scam ads | Session posture change (device, IP, client integrity); sudden change in listing behavior | Kleinanzeigen recommends 2FA and unique passwords [VERIFIED: Kleinanzeigen safety page]. Mercari models session posture (client integrity, network reputation, device and user-agent from fingerprinting) and account posture. Where passkeys are required, "large-scale phishing financial damages have been effectively zero" [VERIFIED: https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/, published 2026-07-30]. Ofcom-commissioned expert interviews note that compromised accounts are used to post "really scammy organic content" [VERIFIED: Integrity Institute for Ofcom, July 2026] |
| **Fake sellers / fake shops** | Batches of new accounts or pseudo-dealers with stolen identity or company data | Identity-reuse graph (same device, IP, email pattern); trader-register mismatch | Signals listed by experts: multiple accounts on the same IPs, email or phone changes, an IP country that differs from the target market [VERIFIED: Integrity Institute report for Ofcom, July 2026, https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf] |
| **Counterfeit** | Branded goods at implausible prices | Brand × price anomaly; rights-holder notices | leboncoin was condemned in 2015 after counterfeit luggage ads (published, then removed after a complaint) contradicted its claim that all ads were validated (see 3.1) [VERIFIED: https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html, published 2015-12-17] |
| **Prohibited / illegal items** | Weapons, drugs, protected species, unsafe or recalled products | Category and keyword rules, image classifiers, product-safety databases | DSA Art. 31(3) requires random checks of official databases for products flagged illegal (see 5.1) [VERIFIED: DSA Art. 31]. In the DSA Transparency Database, "Unsafe, non-compliant or prohibited products" is a top-three category [VERIFIED: https://transparency.dsa.ec.europa.eu/, rolling 180 days to 2026-10-19] |
| **Spam / bot posting** | Mass-created accounts posting repetitive ads, affiliate links or contact-harvest ads | Velocity, near-duplicate text, and device or emulator fingerprints | DSA Art. 17 statements of reasons are not required for "deceptive high-volume commercial content" [VERIFIED: DSA Art. 17 via eu-digital-services-act.com] |
| **Review / reputation fraud** | Fake ratings to build seller trust before a scam; review extortion | Graph of reviewer–reviewee pairs; transaction-backed reviews only | UK DMCC Act ban from 6 April 2025 and US FTC rule (see 5.6–5.7) |

**Supply-side context.** Meta reports taking down "over two million accounts" linked to scam centers in Cambodia, Myanmar, Laos, the UAE and the Philippines [VERIFIED: https://about.fb.com/news/2024/11/cracking-down-organized-crime-scam-centers/, published 2024-11-21, updated 2025-07-14]. [ASSUMPTION/JUDGEMENT] Classifieds fraud is increasingly industrial: organized, operating from offshore compounds, and adapting within days. A static rules engine without fast feedback loops falls behind.

---

## PART 2: Documented marketplace T&S engineering (what is actually public)

### 2.1 Evidence inventory

The honest headline: **classifieds companies publish very little about their T&S architecture.** Most of what exists is old conference material or recent press-style posts with few technical details.

| Company | What is public | Age / reliability |
| --- | --- | --- |
| **OLX Group** | 2026 post on AI fraud prevention. Real-time chat moderation; "Chat Images GenAI" (generative AI with pre-trained knowledge plus predefined rules) that blocks inauthentic images before delivery; QR-code phishing detection (80% precision) with account bans "as the fraud occurs"; image fraud ≈30% of fraud cases in Poland. The page describes the system as handling "thousands of conversations every day". It does not mention human review | [VERIFIED: https://www.olxgroup.com/?p=4590, 2026-01-28]. Press-level; no architecture diagram. The "thousands of conversations" figure is surprisingly low for OLX's scale; probably a per-feature or per-market number. Do not extrapolate. |
| **OLX South Africa (2018)** | ML flags potential scammers in chat. Payment keywords ("PayPal") and attempts to move to email or WhatsApp trigger safety tips and flag the account. Users chatting with a flagged account get an alert. ≈200,000 scammers blocked in 10 months; fraud incidents −44% | [VERIFIED: https://www.itweb.co.za/article/olx-blocks-scammers-using-advanced-algorithms/nWJadvb8APOMbjO1, 2018-05-14]. Eight years old; the system is certainly replaced. Cite the *pattern* (warn-in-context), not the system. |
| **OLX (Alexey Grigorev, PyCon DE 2019)** | Duplicate-listing detection for fraud. Candidate generation (category, city, seller, IP/device, image hashes) → pairwise classifier trained on human-labeled pairs (price difference, location distance, title similarity, image similarity). Images: MD5 → dHash → MobileNet embeddings + PCA/SVD → LSH via random projections, stored in Elasticsearch. Pipeline: S3 upload event → AWS Lambda → queue → Elasticsearch; target ≈10M listings/day, sub-second responses. Cropping, rotation and flipping break the hashes | [VERIFIED: https://pycon.de/archive/2019/talks/fighting-fraud-finding-duplicates-at-scale/, 2019]. Seven years old but the best public classifieds-specific design. |
| **OLX Ukraine (2025)** | ML models to "quickly detect new fraud schemes", plus daily checks by moderators and category specialists and law-enforcement cooperation | [WIDELY REPORTED: https://en.interfax.com.ua/news/general/1038382.html, 2025-01; search summary only] |
| **Adevinta / Kleinanzeigen / leboncoin** | Job postings: Kleinanzeigen seeks data scientists for "production-grade, end-to-end machine learning models that detect fraud and assess user risk in the Trust and Safety domain". A Paris posting describes a "Serenity" team in the "Trust and Connecting" area building a global fraud detection and moderation component deployed in 6 countries. A Barcelona posting lists XGBoost, PyTorch, scikit-learn, Airflow, MLflow and LLMs for "classification, summarization, or risk signal extraction from unstructured text" | [WIDELY REPORTED: https://builtin.com/job/senior-data-scientist-d-f-m/7228169 and search summaries of welcometothejungle.com postings, 2025–2026]. Job ads are weak evidence: they describe intent and stack, not a production design. The Medium tech blogs were 403 in this session. |
| **Kleinanzeigen (customer-facing)** | "Sicher bezahlen" escrow-style payment with OPP (Online Payment Platform), covering non-delivery and not-as-described. "Fraud-detection technology" for fake listings and suspicious activity; a team that reacts to reports; cooperation with authorities; spoofed emails forwarded to spoof@kleinanzeigen.de | [VERIFIED: https://themen.kleinanzeigen.de/sicherheitshinweise/, date unknown] |
| **leboncoin (legal record)** | 2015 Paris court finding on misleading pre-moderation claims (see 3.1) | [VERIFIED: Clubic, 2015-12-17] |
| **Rightmove** | Pre-advertising customer checks; mandatory redress-scheme membership for agents; fraud reporting channel | [VERIFIED: Rightmove guide, date unknown] |
| **Zillow** | Not retrieved (403). | Gap |
| **Facebook Marketplace** | No Marketplace-specific T&S engineering found. Meta's general scam-center enforcement is public (above) | [VERIFIED: Meta 2024-11-21] |
| **Mercari (JP)** | Risk-based authentication and passkey migration; ≈13M passkey users | [VERIFIED: Mercari Engineering, 2026-07-30] |

**Adjacent, well-documented reference systems** (not classifieds, but the patterns transfer):

- **Facebook Sigma** is a rule engine that evaluates policies on every interaction to remove spam, phishing and malware. It serves ">1 million requests per second". Policies are written in Haskell, with Haxl for implicit concurrent data fetching, and are continuously deployed with hot-swapped compiled rules [VERIFIED: https://engineering.fb.com/2015/06/26/security/fighting-spam-with-haskell/, 2015-06-26]. Old, but it is the canonical "rules as code, deployed in minutes" design.
- **Stripe Radar** documents a mature rules-plus-ML operating model [VERIFIED: https://docs.stripe.com/radar/rules, date unknown, current docs]:
  - Rules have the form `{action} if {attribute} {operator} {value}`, with actions block, review, allow and request-3DS. Request-3DS rules are evaluated first. Allow rules override everything, including the ML risk score.
  - Rules are **backtested on the last 6 months** of charges before activation.
  - **Traffic allocation** supports gradual rollout. A 0% allocation is a **shadow mode** that "evaluates the rule and reports what would have happened". Retries are bucketed consistently.
  - A **rule audit trail** records who created, edited or disabled each rule, with before and after predicates, for 180 days.
  - Review queues come with explicit guidance: reviews should be low-volume, add human value, and show a mix of good and bad outcomes. A queue that mostly ends in refunds should become a block rule.
  - Limits: 200 transaction rules and 100 account rules.
  - An LLM "Radar Assistant" turns natural language into rules.

### 2.2 What the absence of evidence means for the book

[ASSUMPTION/JUDGEMENT] Chapter writers should present classifieds T&S architecture as a **reference architecture inferred from adjacent public systems** (Sigma, Radar, Mercari, Grigorev's duplicate pipeline, OLX's chat moderation) and from regulatory requirements (DSA statements of reasons, trader traceability). They should not present it as "how Adevinta does it". Adevinta's group-wide fraud and moderation component (the "Serenity" postings) suggests a **shared T&S platform serving multiple country marketplaces**. That is plausible, given that Adevinta runs Kleinanzeigen, leboncoin, Marktplaats, mobile.de, Subito and others, but it is not documented. ⚠ Adevinta's ownership and portfolio changed after it was taken private in 2024 by a Permira/Blackstone-led consortium [ASSUMPTION/JUDGEMENT; verify current portfolio before print].

---

## PART 3: Moderation pipelines

### 3.1 Pre- vs post-moderation: the legal lesson from leboncoin

- In December 2015, the Tribunal de grande instance de Paris found leboncoin guilty of **misleading commercial practices**. leboncoin claimed all ads passed a validation process. In fact, not all ads were reviewed before going live: counterfeit ads were published, then removed after a luxury-luggage maker complained. The court also confirmed leboncoin's **hosting-provider** status, so it is *not* obliged to check every ad before publication but must remove reported infringing ads promptly. The remedy was publishing the decision on its homepage and in three publications, and revising its terms [VERIFIED: Clubic, 2015-12-17].
- **Lesson.** Your terms and marketing must describe your *actual* moderation mode. "All ads are checked" is a factual claim that a court can test. [ASSUMPTION/JUDGEMENT]
- **The hosting safe harbor survives in the DSA.** Article 6 keeps the conditional liability exemption. Article 16(3) says a notice confers actual knowledge where "a diligent provider" could identify the illegality "without a detailed legal examination" [VERIFIED: DSA Art. 16 via eu-digital-services-act.com]. Article 7, which protects voluntary own-initiative investigations, is [ASSUMPTION/JUDGEMENT; text not fetched].

**Moderation modes as a design spectrum:**

| Mode | Latency to live | Fraud exposure | Cost | Typical use |
| --- | --- | --- | --- | --- |
| Full pre-moderation (human) | Minutes to hours | Lowest | Highest | Small sites, high-risk categories (pets, tickets, rentals) |
| Automated pre-moderation (rules + ML gate), human for grey zone | Seconds; grey zone minutes | Low | Medium | Mainstream classifieds default |
| Publish-then-score (async), takedown on score/report | Instant | Window of exposure | Lower | Low-risk categories, trusted sellers |
| Reactive (notice-and-action only) | Instant | Highest | Lowest | Legally minimal; not defensible for fraud at scale |

[ASSUMPTION/JUDGEMENT] Large classifieds platforms run a **risk-tiered hybrid**. The tier depends on seller trust (account age, verification, history), category risk, and listing risk score. Re-scoring is triggered on **every material edit**. The Which? Gumtree result in 1.2 shows why.

### 3.2 Pipeline anatomy (reference architecture)

**Reference-architecture inference** [ASSUMPTION/JUDGEMENT, assembled from Sigma, Radar, Grigorev, OLX and the DSA schema]:

1. **Ingest event.** `ListingCreated` / `ListingEdited` / `MessageSent` / `AccountCreated` / `LoginSucceeded` go onto the event bus.
2. **Synchronous gate (p99 budget ≈100–300 ms).**
   - Deterministic rules (prohibited keywords, blocked entities, velocity limits).
   - Lookups against lists (phone, email, IBAN, device, image hash).
   - A light ML score.
   - Outcome: *allow*, *hold for review* or *reject*.
3. **Asynchronous enrichment.**
   - Image models (classification, CSAM/PhotoDNA-style hash match, perceptual-hash duplicate search).
   - Text models and LLM classifiers.
   - Price-anomaly model against category valuations.
   - Graph features (shared devices, payment instruments, phone numbers).
   - Outcome: possibly post-hoc takedown or demotion.
4. **Decision service.** Combines scores and rules into an action from a **graduated ladder**: nudge or warning, friction (SMS or ID re-verification), reach limit or demotion, hold, removal, account suspension, payment freeze. The Ofcom-commissioned experts describe the same ladder, from "nudge" through posting limits, payment freezes and re-verification to suspension. They note that payment freezes need a "higher evidentiary threshold" [VERIFIED: Integrity Institute for Ofcom, July 2026].
5. **Human review queues.** Prioritized by expected harm × uncertainty. Trusted-flagger notices are routed to a priority lane (DSA Art. 22).
6. **Statement-of-reasons emitter.** For every restriction, a user-facing notice (Art. 17) and a Transparency Database submission (Art. 24(5)). See Part 5.
7. **Appeals / complaints.** Art. 20 queue, decided by qualified staff, "not solely on the basis of automated means".
8. **Feedback loop.** Reviewer labels, appeal reversals, user reports, chargebacks and bank fraud reports flow back into training sets and rule metrics. Shadow-mode evaluation precedes enforcement (Radar pattern).

### 3.3 Human review economics

- Ofcom-commissioned experts recommend that larger platforms "regularly review randomly sampled ad impressions and the most viewed ads" to **estimate prevalence** of violating content [VERIFIED: Integrity Institute for Ofcom, July 2026]. [ASSUMPTION/JUDGEMENT] For classifieds, the equivalent is random sampling of live listings by category, giving a prevalence metric that does not depend on what the classifiers already catch. Without it, a model that misses a new scam pattern looks "accurate".
- Stripe's guidance applies directly: a review queue that almost always ends the same way should become an automated rule [VERIFIED: Stripe Radar docs].

### 3.4 Image moderation, duplicate and stolen photos

| Technique | Catches | Misses | Evidence |
| --- | --- | --- | --- |
| Cryptographic hash (MD5/SHA) | Exact re-uploads | Any re-encode | [VERIFIED: Grigorev, PyCon DE 2019] |
| Perceptual hash (dHash, pHash, **PDQ**) | Re-compression, small edits | Crops, rotations, flips (partially) | Grigorev [VERIFIED]. Meta's open-source PDQ is a DCT-based perceptual hash with a quality score. Suggested starting thresholds: distance ≤31 to match; discard hashes with quality ≤49. Rotation and flip invariance is not guaranteed. Faiss-based matching reaches ≈4,000 images/s [VERIFIED: https://github.com/facebook/ThreatExchange/tree/main/pdq, implementation list current to 2025-11] |
| CNN embeddings + ANN/LSH | Semantically similar photos, crops | Adversarial edits; costs more | Grigorev: MobileNet + PCA + random-projection LSH in Elasticsearch [VERIFIED] |
| Generative/VLM image check | Fake payment screenshots, manipulated documents, "inauthentic" images | Novel forgeries; cost and latency | OLX Chat Images GenAI [VERIFIED: 2026-01-28] |
| External reverse image search | Photos stolen from other portals (rental scams) | Coverage limits, ToS | [ASSUMPTION/JUDGEMENT] |

**Design note** [ASSUMPTION/JUDGEMENT]: duplicate detection is *two* problems with opposite policies. **Same seller reposting** is a spam or ranking-abuse issue (merge or demote). **Different seller, same photos** is a fraud signal (block or review). The candidate-generation keys Grigorev lists (seller, IP/device) are what separate the two cases.

### 3.5 Messaging safety

- **Warn-in-context.** OLX SA (2018) triggered safety tips when a buyer was asked to pay via PayPal before seeing the item, or when a conversation moved to email or WhatsApp. Payment keywords flagged the account, and users chatting with a flagged account got an alert [VERIFIED: ITWeb 2018-05-14].
- **Block-before-delivery** for images and QR codes in chat [VERIFIED: OLX 2026-01-28].
- **Reference design** [ASSUMPTION/JUDGEMENT]:
  - Tokenize messages for URLs, phone numbers, emails, IBANs, QR payloads and messaging-app handles.
  - Check URLs against allow and deny lists and a domain-age service (new lookalike domains are the phishing tell). Render unknown links non-clickable, or behind an interstitial.
  - Mask or delay off-platform contact details for unverified or new accounts.
  - Score conversation-level patterns ("courier", "safe payment", "deposit") with a sequence model or LLM.
  - Treat the platform's own brand in a chat message as a high-risk signal. Kleinanzeigen explicitly warns that fake "Kleinanzeigen" messages are written by chat partners [VERIFIED: Kleinanzeigen safety page].
- **Privacy constraint** [ASSUMPTION/JUDGEMENT]: automated scanning of private messages engages GDPR (purpose limitation, minimization, transparency) and, in the EU, the ePrivacy framework. Document the purpose (fraud prevention), retention and legal basis (legitimate interest, with a DPIA), and say in your terms that automated tools are used. The DSA requires disclosing automated means in notice decisions (Art. 16(6)) and statements of reasons (Art. 17(3)(c)).

### 3.6 LLM moderation (2024–2026)

- **Evidence of production use in classifieds:** OLX's generative-AI chat-image model [VERIFIED: 2026-01-28]. Adevinta-group job ads list LLMs for "classification, summarization, or risk signal extraction from unstructured text" [WIDELY REPORTED: job postings, 2025–2026].
- **Policy-as-prompt models:** Llama Guard, from Meta researchers, is an instruction-tuned Llama 2-7B safeguard model. Its taxonomy can be customized through zero- or few-shot prompting, and its weights are released [VERIFIED: https://arxiv.org/abs/2312.06674, submitted 2023-12-07]. OpenAI's 2023 post on GPT-4 for content moderation could not be fetched (403) [gap].
- **Stripe** ships an LLM assistant that writes fraud rules from natural language [VERIFIED: Stripe Radar docs].
- **Architectural judgement** [ASSUMPTION/JUDGEMENT]:
  1. **Cost and latency.** Use LLMs on the grey zone only: the uncertain band of a cheap classifier, or items queued for human review. Do not run them on 100% of traffic at a large classifieds platform's volume.
  2. **Policy agility.** The real value is fast policy iteration. A new scam script can be described in a prompt the same day, then distilled into a cheap classifier once labels accumulate.
  3. **Explanations for statements of reasons.** LLMs can draft the `decision_facts` and explanation text required by DSA Art. 17. A human or template must constrain that output, because the statement is a legal document.
  4. **Appeals.** DSA Art. 20(6) forbids complaint decisions taken "solely on the basis of automated means". An LLM can triage and summarize, but cannot be the decider.
  5. **Adversarial robustness.** Fraudsters probe the gate. Keep deterministic rules and hash lists as a floor that prompt injection cannot bypass.

---

## PART 4: Identity, verification and payment-scam controls

### 4.1 Verification ladder

| Level | Mechanism | Defeats | Doesn't defeat | Evidence |
| --- | --- | --- | --- | --- |
| 0 | Email verification | Typos, trivial bots | Disposable emails, farms | [ASSUMPTION/JUDGEMENT] |
| 1 | Phone/SMS OTP | Bulk account creation (cost per number) | SIM farms, virtual numbers, SMS-pumping fraud against you | [ASSUMPTION/JUDGEMENT] |
| 2 | Device fingerprinting / client integrity, network reputation | Multi-accounting, emulators, ATO from new devices | Residential proxies, device farms | Mercari's session-posture signals [VERIFIED: 2026-07-30]. Experts list "Multiple accounts tied to the same IP's", IP bouncing, email/phone changes and credit-card changes [VERIFIED: Integrity Institute for Ofcom, July 2026] |
| 3 | Strong authentication (passkeys / 2FA) | Phishing-driven ATO | Social-engineering of recovery flows | Mercari: passkey-required accounts show "effectively zero" large-scale phishing losses; recovery requires My Number Card or document + selfie and never restores the password [VERIFIED: Mercari 2026-07-30] |
| 4 | Payment-instrument / bank verification (IBAN name check, card) | Fake identities without bank accounts | Money mules | [ASSUMPTION/JUDGEMENT] |
| 5 | Identity proofing (document + liveness, eID, bank ID) | Most fake-seller farms | Stolen or synthetic identity at small scale | [ASSUMPTION/JUDGEMENT] |
| 6 | KYB for traders (trade register, VAT, ID) | Fake dealers and agents | Real but rogue businesses | Required for traders by DSA Art. 30 (Part 5) |

**Verified badges** [ASSUMPTION/JUDGEMENT]: a badge is a *claim* the platform makes to buyers, and so a liability. A badge must state exactly what was verified ("phone verified" vs. "identity verified" vs. "registered business"). If a verified account is taken over, the badge amplifies the scam. The Ofcom-commissioned experts make the same point: account takeover is attractive because fraudsters "gain check marks, verification" [VERIFIED: Integrity Institute for Ofcom, July 2026]. Pair badges with ATO detection and badge revocation on posture change.

**Friction as a weapon.** The experts recommend "creating delays between creating an account and reaching a large audience" and introducing verification friction, which "directly disrupts" repeat bad actors [VERIFIED: Integrity Institute for Ofcom, July 2026]. In classifieds terms: cap new accounts' listing velocity and contact-detail visibility until they build trust [ASSUMPTION/JUDGEMENT].

### 4.2 eIDAS 2.0 / EU Digital Identity Wallet, BankID, itsme

- The European Digital Identity Framework (Regulation (EU) 2024/1183) **entered into force in May 2024**. Each Member State must offer at least one EUDI Wallet "by 2026". A January 2026 Commission news item says wallets "are set to launch at the end of 2026". Implementing acts on relying-party registration and certification were adopted in May 2025 [VERIFIED: https://ec.europa.eu/digital-building-blocks/sites/display/EUDIGITALIDENTITYWALLET/EU+Digital+Identity+Wallet+Home, date unknown; https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation, updated 2026-06-22]. ⚠ Wallet launch timing varies by Member State.
- **Selective disclosure.** Users share only what the service needs, for example proving they are over an age threshold without revealing their birth date [VERIFIED: EUDI wallet home].
- **Private relying-party obligations** [ASSUMPTION/JUDGEMENT; the EUR-Lex text was not reachable]: the regulation (new Art. 5f) requires *very large online platforms* that require user authentication to accept the wallet when the user requests it. Private parties legally required to use strong authentication must accept it within a set period after the implementing acts. The Commission page confirms only that "service providers legally required to identify customers must accept the wallet" [VERIFIED: eudi-regulation page]. Since no classifieds platform is a VLOP (5.1), the VLOP clause does not bind classifieds directly as of October 2026.
- **DSA Art. 30(1)(b) already names eIDAS.** A trader can supply "a copy of an identification document or other electronic identification under Regulation (EU) No 910/2014" [VERIFIED: DSA Art. 30]. **Architectural implication:** design the trader-onboarding (KYBC) flow with a pluggable eID adapter (EUDI wallet presentation, national bank-ID schemes, document + liveness vendors) behind one verification-result contract. [ASSUMPTION/JUDGEMENT]
- **BankID (Sweden, Norway), itsme (Belgium), MitID (Denmark)** are mature bank-anchored eIDs that Nordic and Benelux marketplaces commonly use for seller verification. [ASSUMPTION/JUDGEMENT; the vendor pages were not fetched]

### 4.3 Payment-scam controls: moving money on-platform

- **In-platform payment with buyer protection** is the single control that converts an unrecoverable APP fraud into a recoverable, platform-mediated dispute. Kleinanzeigen's "Sicher bezahlen" with OPP covers non-delivery and goods not as described [VERIFIED: Kleinanzeigen safety page]. Which? found buyer protection at eBay, Vinted, Depop, Shpock, Preloved and Amazon Marketplace, but not at Facebook Marketplace, Gumtree or Nextdoor [VERIFIED: Which? 2024-12-12]. UK Finance's legislative ask is exactly this: "secure payment protections on online marketplaces" [VERIFIED: UK Finance 2026].
- **Trade-offs** [ASSUMPTION/JUDGEMENT]:
  - Escrow-style flows make the platform (or its PSP) part of the money flow. That brings KYC of payees (payment-facilitator or marketplace models), DAC7 reporting (5.4), chargeback exposure and a new fraud surface: fake "payment received" phishing that impersonates the platform's own escrow brand. That last risk is why OLX and Kleinanzeigen focus on phishing links and spoofed emails.
  - Adoption is the hard part. Buyers who meet in person pay cash, so in-platform payment fits shipped goods. For vehicles and property, the deposit is the attack surface, and escrow for large sums is a regulated activity.
- **Bank-side controls interact with platform signals.** UK Confirmation of Payee and the EU Verification of Payee (mandatory for euro-area PSPs from 9 October 2025 under the Instant Payments Regulation) check whether the payee name matches the account. They do not catch a fraudster using a real mule account in their own name. [ASSUMPTION/JUDGEMENT; see the payments brief in the RECONCILED journal for the VoP citation]

---

## PART 5: Regulation

### 5.1 EU Digital Services Act (Regulation (EU) 2022/2065): what classifieds must build

**Status and applicability.** The DSA has applied to all providers since 17 February 2024 [ASSUMPTION/JUDGEMENT, consistent with the Art. 30(2) reference to traders "already using the platform … on 17 February 2024", VERIFIED]. A classifieds site is a *hosting service* and an *online platform*. Where it lets consumers conclude distance contracts with traders (dealers, agents, professional sellers), it is also an **online marketplace** in the Section 4 sense (Arts. 30–32). [ASSUMPTION/JUDGEMENT] Whether a pure-lead C2C classifieds service "allows consumers to conclude distance contracts with traders" is arguable. In practice, the trader listings on such sites (dealers on mobile.de, agents on property portals, pro sellers on general classifieds) put them in scope for those listings, so treat Arts. 30–32 as applicable.

**Small-company exemption (Art. 19).** The online-platform section does not apply to micro or small enterprises (Recommendation 2003/361/EC), except Art. 24(3). A firm that grows out of the category keeps the exemption for 12 months; designated VLOPs never qualify [VERIFIED: DSA Art. 19 via eu-digital-services-act.com]. [ASSUMPTION/JUDGEMENT] Being part of a large group generally defeats the exemption through the Recommendation's linked-enterprise rules, so Adevinta-, Axel Springer- or Prosus-owned brands should assume full scope.

**Are any classifieds VLOPs? No (as of 15 October 2026).**

- The Commission's list shows **25 active VLOPs**. The marketplaces among them are AliExpress, Amazon Store, App Store, Booking.com, Google Play, Google Maps, Google Shopping, Zalando (all 25 April 2023), Shein (26 April 2024) and Temu (31 May 2024). The others are social, video or adult services, plus WhatsApp (26 January 2026), Reddit and Roblox (both 31 August 2026). Stripchat's designation was terminated on 27 May 2025. No classifieds, real-estate or automotive marketplace appears: no OLX, leboncoin, Kleinanzeigen, Marktplaats or Vinted [VERIFIED: https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses, updated 2026-10-15].
- **Facebook** is a VLOP (25 April 2023), and Facebook Marketplace runs inside Facebook [VERIFIED: same list]. Whether Marketplace content is governed by Facebook's VLOP risk-assessment obligations is [ASSUMPTION/JUDGEMENT]. It runs inside the designated service, so likely yes. ⚠ Designations change; the threshold is ≥45 million average monthly active EU recipients (Art. 33) [ASSUMPTION/JUDGEMENT on article number; the 45M figure is consistent with the Commission page].
- **Every platform must publish its average monthly active EU recipients at least every six months** (Art. 24(2)) [VERIFIED: DSA Art. 24]. Classifieds groups therefore publish MAU figures that are a public signal of VLOP proximity [ASSUMPTION/JUDGEMENT; individual figures not retrieved].

**Obligations table (classifieds-relevant):**

| Article | Obligation | Engineering consequence | Tag |
| --- | --- | --- | --- |
| **16 Notice and action** | Easy, electronic-only notice mechanism. Notices carry reasons, exact URL(s), the notifier's name and email, and a good-faith statement. Confirm receipt without undue delay if an email is given. Notify the decision and redress options. Process "in a timely, diligent, non-arbitrary and objective manner". Disclose use of automated means | Structured "report listing" form capturing the four elements. Notice entity with status lifecycle. Notifier communications. Automated-means flag | [VERIFIED: Art. 16 via eu-digital-services-act.com] |
| **17 Statement of reasons** | For any restriction (visibility removal, disabling or demotion; monetary suspension; service suspension; account suspension or termination), give the affected user: the restriction, its territorial scope and duration; the facts, including whether triggered by a notice or own-initiative; whether automated detection or decision was used; the legal ground (illegal) or contractual ground (ToS) with explanation; redress options. Applies only where electronic contact details are known. Does **not** apply to "deceptive high-volume commercial content" | Every moderation action must emit a structured, user-readable reason. Demotion counts, so ranking-level penalties ("shadow" demotion of suspected scam ads) trigger the obligation | [VERIFIED: Art. 17] |
| **20 Internal complaints** | Free, electronic complaints for **at least six months** after the decision. Timely, non-arbitrary handling. Reverse unfounded decisions. Decisions under qualified staff supervision, not solely automated | Appeals queue; retain decision evidence ≥6 months (practically longer, see 5.10); reversal path that restores the listing and its ranking | [VERIFIED: Art. 20] |
| **21 Out-of-court dispute settlement** | Users can escalate to certified ODS bodies | Export case file to ODS bodies; Art. 24(1) reporting of ODS outcomes | [VERIFIED by reference in Arts. 20 and 24] |
| **22 Trusted flaggers** | Status awarded by the national Digital Services Coordinator. Notices "given priority and are processed and decided upon without undue delay". Commission publishes a database of trusted flaggers. Platforms may report flaggers who submit many imprecise notices | Priority lane keyed on a trusted-flagger registry; quality metrics per flagger | [VERIFIED: Art. 22] |
| **23 Misuse** | Suspend users who frequently post manifestly illegal content, or submit manifestly unfounded notices or complaints, after a warning; criteria in the terms | Strike system with warnings; Art. 24(1)(b) counts | [VERIFIED by reference in Art. 24] |
| **24 Transparency** | Add ODS and Art. 23 suspension figures to Art. 15 reports; publish EU MAU every six months; submit every Art. 17 statement of reasons to the Commission database "without undue delay", without personal data | Statement-of-reasons pipeline to the DSA Transparency Database API (5.2) | [VERIFIED: Art. 24] |
| **26 Advertising** | Label ads in real time; show on whose behalf and who paid; main targeting parameters; no profiling on GDPR special categories | **Promoted / "top" listings are ads in the DSA sense** [ASSUMPTION/JUDGEMENT]: label them and expose the parameters | [VERIFIED: Art. 26] |
| **27 Recommender transparency** | Main recommender parameters in the terms in plain language; user-selectable options where offered | Document search-ranking parameters (overlaps P2B Art. 5 and Omnibus) | [VERIFIED: Art. 27] |
| **30 Trader traceability (KYBC)** | Before letting a trader promote or offer to EU consumers, obtain: (a) name, address, phone, email; (b) ID document copy or eIDAS e-identification; (c) payment account details; (d) trade register and number, if registered; (e) self-certification of offering only compliant products. Make "best efforts" to assess reliability using free official databases or supporting documents. Traders already on the platform on 17 Feb 2024 had 12 months, or suspension. Act on inaccurate data (request correction, then suspend). Store securely for **six months after the relationship ends, then delete**. Display (a), (d) and (e) to users on the listing interface | Trader-onboarding service with register lookups (e.g., VIES VAT, national registers); document vault with lifecycle-based deletion; trader-info panel on listing pages; suspension hooks | [VERIFIED: Art. 30] |
| **31 Compliance by design** | Interface lets traders provide pre-contractual, compliance and product-safety information (economic-operator contact, product identification, marks and labels). Best efforts to check before offers go live; reasonable efforts at **random checks** against official databases for products flagged illegal | Listing schema fields for product-safety data; scheduled random-sample job against Safety Gate-type databases [ASSUMPTION/JUDGEMENT on database name] | [VERIFIED: Art. 31] |
| **32 Right to information** | If the platform learns a trader offered an illegal product or service, inform consumers who bought in the previous six months (trader identity, remedies), or publish the notice if contact details are missing | Requires *knowing* who bought, which a lead-generation classifieds site often does not. Fall back to a public notice. Record contact events (messages, leads) per listing | [VERIFIED: Art. 32] |

### 5.2 The DSA Transparency Database: concrete schema

The Commission database is the most concrete "evidence store" requirement any classifieds architect will meet.

- **Submission.** API or webform, same schema. Single endpoint `POST /api/v1/statement`, batch `POST /api/v1/statements` with **max 100 statements per call**. A batch fails atomically if any statement fails validation. A `GET /api/v1/statement/existing-puid/<PUID>` check makes idempotent resubmission possible. Onboarding goes through the Digital Services Coordinator, with a sandbox before production [VERIFIED: https://transparency.dsa.ec.europa.eu/page/api-documentation, date unknown; https://digital-strategy.ec.europa.eu/en/faqs/dsa-transparency-database-questions-and-answers, updated 2025-07-07].
- **Key fields** [VERIFIED: API documentation]:
  - `decision_visibility` (CONTENT_REMOVED, CONTENT_DISABLED, CONTENT_DEMOTED, CONTENT_AGE_RESTRICTED, CONTENT_INTERACTION_RESTRICTED, CONTENT_LABELLED, OTHER), plus `decision_monetary`, `decision_provision` and `decision_account`.
  - `account_type` (BUSINESS / PRIVATE).
  - `decision_facts` (≤5,000 chars).
  - `decision_ground` (ILLEGAL_CONTENT / INCOMPATIBLE_CONTENT) with legal or contractual ground and explanation fields.
  - `content_type`, including **PRODUCT**.
  - `category`, one of 16, including **STATEMENT_CATEGORY_SCAMS_AND_FRAUD**, with ≈70 keyword specifications.
  - `territorial_scope` (EU/EEA country codes).
  - `content_date`, `application_date` and restriction end dates.
  - `source_type` (ARTICLE_16 notice, TRUSTED_FLAGGER, OTHER_NOTIFICATION, VOLUNTARY).
  - `automated_detection` (Yes/No) and `automated_decision` (FULLY / PARTIALLY / NOT_AUTOMATED).
  - `puid`, a platform-unique ID.
- **No personal data** may be submitted [VERIFIED: FAQ].
- **Retention of the public data.** Statements are searchable for 180 days and kept in daily dumps (zipped CSV) for 540 days. Aggregates are kept for 5 years [VERIFIED: FAQ].
- **Scale signal.** For the rolling last 180 days (accessed 19 October 2026): **4,421,303,827** statements of reasons from **375** active platforms, with **41% fully automated** decisions. Top categories: other ToS violations; "Unsafe, non-compliant or prohibited products"; consumer-information infringements [VERIFIED: https://transparency.dsa.ec.europa.eu/]. A third-party tracker reports that Google Shopping accounts for nearly half of all statements [WIDELY REPORTED: https://www.checkstep.com/dsa-statement-of-reason-report, date unknown]. ⚠ Counts change daily.

**Architectural implications** [ASSUMPTION/JUDGEMENT]:

1. Make the **statement of reasons a first-class domain object** produced by the decision service, not an afterthought. Its fields map to the moderation decision: action, ground, policy reference, category, automation flags, source, territorial scope and duration.
2. The `puid` is your **decision ID**. Keep a stable mapping from `puid` to the internal case, listing, user and evidence snapshot, so you can answer appeals, ODS bodies and regulators.
3. **Strip PII before submission**, but keep the full internal record. Two records, one decision.
4. Batch and retry with idempotency on `puid`. A classifieds platform rejecting millions of ads a month generates millions of submissions.
5. The **"deceptive high-volume commercial content" exception** in Art. 17 matters for spam-bot floods. Define, in policy, which automated rejections fall under it, and log the classification.
6. **Demotion is a restriction.** If the ranking system silently down-ranks suspected-scam listings, that is CONTENT_DEMOTED and needs a statement of reasons. Many ranking teams don't know this.

### 5.3 Transparency reports (Art. 15 / 24)

- Art. 24(1) adds out-of-court-dispute counts, outcomes, median resolution times and the share implemented, plus Art. 23 suspension counts, to the Art. 15 transparency reports [VERIFIED: Art. 24]. Art. 24(6) lets the Commission set templates by implementing act [VERIFIED].
- ⚠ [ASSUMPTION/JUDGEMENT; the Commission page URL was not found] The Commission adopted an implementing regulation with harmonized templates in late 2024, requiring data collection on the harmonized basis from 1 July 2025 and first harmonized reports in early 2026. Verify the regulation number and dates before print.
- **Engineering consequence.** Moderation metrics (notices by type, median time to action, automated vs. human, complaints and reversals) must be computable from the event log by reporting period, and **reproducible**. Build them from the same decision events that feed the Transparency Database. [ASSUMPTION/JUDGEMENT]

### 5.4 DAC7 (Council Directive (EU) 2021/514): platform seller reporting

- **What it is.** EU platform operators must collect, verify and report data about sellers to tax authorities [VERIFIED: https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7, date unknown].
- **Relevant activities:** rental of immovable property, personal services, sale of goods, rental of means of transport [VERIFIED: Belastingdienst].
- **Data reported** [VERIFIED: Belastingdienst]:
  - Seller identity: name, primary address, date of birth, VAT ID.
  - Financial and tax identifiers: financial account identifier, TIN with issuing Member State, business registration number.
  - Location data: EU permanent establishment; property address and land registration number for rentals.
  - Activity data: **total consideration per quarter, number of relevant activities, and fees, commissions and taxes withheld**.
- **Timing:** collect and verify by 31 December of the reportable year; report by 31 January of the following year. First reporting (2023 data) was due 31 January 2024 [VERIFIED: Belastingdienst].
- **De minimis:** sellers of goods with **fewer than 30 relevant activities and consideration of €2,000 or less** in the period are excluded [VERIFIED: Belastingdienst; WIDELY REPORTED: Bird & Bird, PwC Malta, Grant Thornton Ireland commentary]. Both conditions must hold, and the exclusion covers goods only, not services or rentals. Commentary states the test is applied per platform [WIDELY REPORTED]. Entities with >2,000 rental activities per property listing are separately excluded [VERIFIED: Belastingdienst].
- **Does DAC7 bite classifieds?** [ASSUMPTION/JUDGEMENT] DAC7's "consideration" means amounts paid or credited to the seller in connection with the relevant activity that are *known or reasonably knowable* to the operator. Platforms that "engage solely in allowing payment processing, listing or advertising, or redirecting users" are excluded from the platform definition [WIDELY REPORTED: search summary of commentary]. A **pure lead-gen classifieds site is therefore largely outside DAC7. Once it adds in-platform payment** (Kleinanzeigen "Sicher bezahlen", Marktplaats/leboncoin shipping-plus-payment flows), the platform knows the consideration and must report sellers above the threshold. **The decision to launch in-platform payments is also a tax-reporting decision.** Design the payment ledger to aggregate per seller, per quarter and per Member State from day one.

### 5.5 Platform-to-Business Regulation (EU) 2019/1150: ranking transparency

- It has applied since **12 July 2020** [VERIFIED: https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices, updated 2026-07-02].
- **⚠ Repeal proposed.** On 19 November 2025 the Commission proposed repealing the P2B Regulation, citing overlap with the DSA and DMA. Its ranking guidelines are non-binding and "will remain in application even if the Regulation is repealed" [VERIFIED: same page]. As of October 2026 the repeal is a proposal; check its legislative status before print.
- **Art. 5 content** [ASSUMPTION/JUDGEMENT; text not fetched]: platforms must set out in their terms the **main parameters determining ranking** and their relative importance. This includes any possibility for business users to influence ranking against payment, which covers classifieds "bump", "top ad" and premium-placement products. The small-enterprise exemption applies to the internal complaint system (Art. 11), not to Art. 5.
- **Who is a "business user" on a classifieds site?** Dealers, agents and professional sellers. These are the same population as DSA Art. 30 traders, so one trader registry can serve both. [ASSUMPTION/JUDGEMENT]

### 5.6 Omnibus Directive (EU) 2019/2161: marketplace transparency and consumer reviews

- Adopted 27 November 2019; **applied from 28 May 2022**; amends the Consumer Rights Directive (and the UCPD) [VERIFIED: https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en, date unknown]. The Commission's 2021 CRD Guidance covers "obligations of online marketplaces" [VERIFIED: same page].
- **Provisions relevant to classifieds** [ASSUMPTION/JUDGEMENT; the article text could not be fetched, so verify against EUR-Lex]:
  - **CRD Art. 6a.** Before a consumer is bound, a marketplace must disclose: the **main ranking parameters**; **whether the third party is a trader or not** (based on the third party's own declaration); that EU consumer-rights law does not apply when the counterparty is not a trader; and how obligations are split between the marketplace and the trader. *Engineering consequence: a mandatory "private / business" seller declaration on account or listing creation, displayed on the listing.* The DSA Transparency Database `account_type` (BUSINESS/PRIVATE) field mirrors this.
  - **UCPD Art. 7(4a).** Ranking-parameter information in search results.
  - **UCPD Art. 7(6).** Where a trader gives access to consumer reviews, it must say **whether and how it ensures reviews come from consumers who actually used or bought the product**.
  - **UCPD Annex I blacklist** additions: undisclosed paid ranking or paid advertising in search results; claiming reviews come from real users without taking reasonable and proportionate steps to check; submitting or commissioning fake reviews or misrepresenting reviews.
  - **Penalties.** For widespread infringements under coordinated CPC action, maximum fines of at least 4% of annual turnover in the Member States concerned (or €2 million where turnover is unavailable).
- ⚠ **Digital Fairness Act.** The Commission is preparing a Digital Fairness Act addressing dark patterns, addictive design, unfair personalization and unfair pricing practices, following its Fitness Check published 3 October 2024 [VERIFIED: https://commission.europa.eu/law/law-topic/consumer-protection-law/review-eu-consumer-law_en, date unknown]. A proposal could change ranking, personalization and review rules again.

### 5.7 UK: Online Safety Act 2023 and the DMCC Act 2024

**Online Safety Act: two different fraud regimes.**

1. **Illegal-content duties (all regulated user-to-user services, including classifieds).** Fraud is a **priority offence**: Schedule 7, paragraph 33 lists Fraud Act 2006 sections 2, 4, 7 and 9; paragraph 34 covers articles for use in fraud (Scotland); paragraphs 35–36 cover FSMA 2000 and Financial Services Act 2012 offences; paragraph 39 covers inchoate offences [VERIFIED: https://www.legislation.gov.uk/ukpga/2023/50/schedule/7]. Ofcom's Illegal Harms statement was published 16 December 2024. Providers had to complete illegal-harms risk assessments by **16 March 2025**, and safety measures applied from **17 March 2025** [VERIFIED: https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-protecting-people-from-illegal-harms-online, published 2024-12-16, updated 2026-06-25]. [ASSUMPTION/JUDGEMENT] A user's scam *listing* on Gumtree or Facebook Marketplace is user-generated content, governed by these duties, not by the fraudulent-advertising duty.
2. **Fraudulent-advertising duties (s.38 Category 1; s.39 Category 2A search).**
   - **Scope.** Applies to **paid-for** ads that amount to a listed fraud offence and are not regulated user-generated content.
   - **Duties.** Proportionate systems to prevent users encountering such ads, minimize how long they are present, and swiftly take them down when alerted. Any proactive technology must be explained in the terms.
   - **Commencement.** s.38 came into force on 10 January 2024 (S.I. 2023/1420) [VERIFIED: https://www.legislation.gov.uk/ukpga/2023/50/section/38].
   - **Ofcom's draft Fraudulent Advertising Codes.** Consulted from **10 July 2026**, closing **2 October 2026**, with a final statement "by mid-2027" at the latest. The proposals cover paid-for ads and exclude user-generated content and non-sponsored search content [VERIFIED: https://www.ofcom.org.uk/online-safety/online-fraud/consultation-fraudulent-advertising-code-of-practice, published 2026-07-10, updated 2026-07-28].
   - Ofcom published its register of categorised services alongside [WIDELY REPORTED: RPC, Fieldfisher commentary, July 2026]. ⚠ Which classifieds, if any, are Category 1 could not be verified.
   - **Open question for classifieds** [ASSUMPTION/JUDGEMENT]: is a *paid listing upgrade* (a "featured" or "bump" product bought by a private seller) a "paid-for advertisement" or user-generated content? The answer determines whether Category 1 fraudulent-ad duties attach to promoted scam listings. Ask counsel.
   - **Evidence base.** The Ofcom-commissioned Integrity Institute report (July 2026) recommends multiple detection signals, advertiser verification, friction between account creation and reach, easy user reporting, and prevalence measurement by random sampling [VERIFIED: Integrity Institute for Ofcom, July 2026]. Which? criticized the pace and called for faster implementation [VERIFIED: Which? 2024-12-12].

**DMCC Act 2024: fake reviews.**

- Since **6 April 2025** it has been banned to commission or submit fake reviews, to **host consumer reviews without taking reasonable steps to check they are genuine**, and to offer or advertise fake-review services. The CMA can decide breaches itself, without first going to court, and fine **up to 10% of global turnover** [VERIFIED: https://www.which.co.uk/news/article/fake-reviews-and-sneaky-fees-banned-under-new-law-campaigned-for-by-which-aLzVp4g0S76D, published 2025-04-07].
- Commentary reports a three-month grace period to early July 2025, CMA guidance published in April 2025, and a CMA review of >100 websites [WIDELY REPORTED: Osborne Clarke, Ashurst, Taylor Wessing, 2025]. The guidance text was not fetched.
- **Engineering consequence for marketplace ratings** [ASSUMPTION/JUDGEMENT]: tie reviews to a **verifiable interaction**, a completed in-platform transaction or at least a message thread plus a confirmed handover. Detect reciprocal and collusive rating rings in the user graph. Log what "reasonable steps" were taken, because that log is the defense.

### 5.8 US: INFORM Consumers Act, FTC rules, fair housing, auto

**INFORM Consumers Act** (effective 27 June 2023) [VERIFIED: https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act, published 2023-06, edited 2025-01]:

| Element | Requirement |
| --- | --- |
| Scope | "Online marketplaces" with "high-volume third party sellers" of new or unused consumer products |
| High-volume threshold | In any continuous 12 months within the past 24: **≥200 separate sales and ≥$5,000 gross revenue**. Only sales made through the marketplace **with payment processed by it** count |
| Collect (within 10 days of threshold) | Bank account (or payee name); business or taxpayer ID; contact info (individuals: name, email, phone; entities: government ID or record showing business name and address) |
| Verify | Within 10 days of receipt; annual electronic re-certification |
| Disclose | Sellers with **≥$20,000** annual gross revenue: full name, physical address, direct contact info on the listing or order confirmation (limited home-seller exception) |
| Suspend | After notice, if no response within 10 days |
| Report | Listing pages show a clear phone number and electronic channel for reporting suspicious activity |
| Data use | Reasonable security; compliance data not used for other purposes |
| Penalties | Treated as FTC rule violations; **$53,088 per violation** (inflation-adjusted); state AG enforcement |

[ASSUMPTION/JUDGEMENT] A US lead-gen classifieds site (Craigslist-style, Facebook Marketplace local pickup) that does not process payment largely falls outside the counting rule, because only marketplace-processed sales count. As in DAC7, **adding payments brings the seller-verification obligation with it.** And used goods, which most classifieds traffic is, are outside "new or unused consumer products".

**FTC Trade Regulation Rule on fake reviews and testimonials** (announced 14 August 2024; effective 60 days after Federal Register publication). It bans [VERIFIED: https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials, 2024-08-14]:
- Creating, buying or disseminating fake reviews, including AI-generated ones, from people who don't exist or had no real experience.
- Review suppression by threats or intimidation.
- Buying sentiment-conditioned reviews.
- Undisclosed insider reviews.
- Company-controlled "independent" review sites.
- Buying or selling fake social indicators.

The FTC can "seek civil penalties against knowing violators". [ASSUMPTION/JUDGEMENT] It took effect 21 October 2024.

**Fair housing advertising (real-estate portals and rental classifieds).**
- 24 CFR §100.75 makes it unlawful to make, print or publish any notice, statement or advertisement about selling or renting a dwelling that indicates a preference, limitation or discrimination based on race, color, religion, sex, handicap, familial status or national origin. That includes words, phrases, photos, symbols or forms conveying such a preference; selecting media or locations to deny particular groups information; and refusing ads or charging differently on protected bases [VERIFIED: https://www.law.cornell.edu/cfr/text/24/100.75, date unknown].
- **Engineering consequences** [ASSUMPTION/JUDGEMENT]:
  - Run a listing-text classifier for discriminatory phrases ("no kids", "Christian household", "perfect for singles").
  - **Ad-delivery and targeting systems are themselves in scope.** The US Department of Justice's 2022 settlement with Meta over housing-ad delivery led to its "Variance Reduction System" [ASSUMPTION/JUDGEMENT; the DOJ page was not retrieved].
  - Personalized ranking or recommendation of housing listings must be audited for disparate delivery.

**Automotive.**
- The FTC Used Car Rule (16 CFR Part 455, in effect since 1985; last amended by a 2016 final rule) requires dealers to display a **Buyers Guide** stating warranty or "as is" status [VERIFIED: https://www.ftc.gov/legal-library/browse/rules/used-car-rule]. The page does not address online listings.
- [ASSUMPTION/JUDGEMENT] The FTC's CARS Rule (Combating Auto Retail Scams, adopted December 2023) was vacated by the Fifth Circuit in January 2025. Its FTC page returned 404 in this session. Verify before print.
- Dealer listing obligations on portals (advertised-price inclusiveness, mileage, accident history) are mostly state law in the US and national consumer law in the EU. [ASSUMPTION/JUDGEMENT]

### 5.9 Real-estate specifics in the EU and UK

- **Energy Performance of Buildings Directive (recast) (EU) 2024/1275.** Published 8 May 2024, entered into force 28 May 2024, **transposition by 29 May 2026**. EPCs move to a common template with common criteria for energy-performance classes and become digital [VERIFIED: https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/energy-performance-buildings-directive_en, date unknown].
  - [ASSUMPTION/JUDGEMENT; directive text not fetched] Since the 2010 EPBD, advertisements for sale or rent must state the **energy performance indicator/class** where an EPC exists. The recast keeps this and moves toward a harmonized A–G scale.
  - **Engineering consequence:** property-portal listing schemas need structured EPC fields (class, indicator value, certificate ID, validity date), validation against national EPC registries where APIs exist, and visible display rules per country. ⚠ National transposition varies.
- **UK rental fraud context.** Rightmove's customer checks and redress-scheme requirement act as KYB for agents [VERIFIED: Rightmove guide]. [ASSUMPTION/JUDGEMENT] Open platforms that accept private landlords lack that filter, so property-ownership checks (Land Registry title lookups) and viewing-before-payment nudges become the controls.

### 5.10 GDPR: retention, minimization and address privacy

- **Art. 5(1)(c) data minimization** ("limited to what is necessary") and **Art. 5(1)(e) storage limitation**. Art. 5(2) **accountability** requires the controller to *demonstrate* compliance [VERIFIED: https://gdpr-info.eu/art-5-gdpr/, an unofficial reproduction].
- **The retention tension T&S architects must resolve** [ASSUMPTION/JUDGEMENT]:
  - Fraud models want long histories: device graphs and banned-identity lists kept for years.
  - GDPR wants purpose-bound, time-limited retention.
  - The DSA *mandates* some retention: Art. 30 trader data for 6 months after the relationship ends, then **deletion** [VERIFIED].
  - The DSA *implies* other retention: decision evidence must last the Art. 20 complaint window (≥6 months), then ODS proceedings and possible litigation [VERIFIED: Art. 20 for the window; the extension is judgement].
  - Resolution pattern: tiered retention per data class. Raw content snapshots are kept for the appeal window plus a buffer. Hashed identifiers (phone, email, IBAN, device hash) go on block lists with a documented, longer retention justified as fraud prevention (GDPR recital 47 names fraud prevention as a legitimate interest). Aggregates go to reporting. Each class carries a deletion job and an audit trail.
- **Address privacy in listings** [ASSUMPTION/JUDGEMENT]: show approximate location (postcode district or jittered map pin) for private sellers and landlords. Exact addresses help burglary targeting and stalking. DSA Art. 30(7) requires displaying a *trader's* address, which conflicts with home-based sole traders. INFORM provides a home-seller exception at the ≥$20,000 tier [VERIFIED: FTC]. Check whether the DSA allows a similar exception; nothing was found in Art. 30.

### 5.11 Competition: the Facebook Marketplace case

- The European Commission fined Meta for abusing dominance by **tying Facebook Marketplace to Facebook** and **imposing unfair trading conditions on competing online classified-ads providers** [VERIFIED (subject matter only): https://ec.europa.eu/commission/presscorner/detail/en/ip_24_5801]. The excerpt retrieved did not include the amount or date.
- [ASSUMPTION/JUDGEMENT] The decision was 14 November 2024, with a fine of €797.72 million. The "unfair trading conditions" concerned Meta's use of ad-related data from competing classifieds advertisers on Facebook and Instagram. Classifieds incumbents (Adevinta brands, OLX and others) were the complainants' constituency. This is relevant to the book's competitive-landscape chapter, and to T&S because Marketplace's free, unverified, payment-less model is the one Which? and UK Finance criticize.

---

## PART 6: Reference architecture for marketplace T&S (inferred)

**Everything in this part is [ASSUMPTION/JUDGEMENT]**, a reference-architecture inference assembled from the verified building blocks cited above. No classifieds company has published this design.

### 6.1 Components

| Component | Responsibility | Key design notes | Grounding |
| --- | --- | --- | --- |
| **Signal collection** | Client SDK (device fingerprint, client integrity), server events (listing, message, login, payment) and external feeds (bank fraud reports, trusted flaggers, phishing domain feeds) | Version every signal; time-travel-safe feature computation for training | Mercari postures [VERIFIED]; Ofcom expert signal tables [VERIFIED] |
| **Entity resolution / identity graph** | Links accounts through shared device, phone, email, IBAN, IP range and image hashes | Core weapon against repeat offenders. Experts note new accounts can be matched to removed ones by shared emails and identical content [VERIFIED: Integrity Institute] | Grigorev candidate keys [VERIFIED] |
| **Feature store** | Online (low-latency) and offline (training) parity | Velocity counters (listings/hour/device), account-age buckets, price-to-valuation ratios | — |
| **Rules engine** | Deterministic policies as code; hot deploy; backtest; shadow mode; audit trail | Sigma: hot-swapped, >1M rps [VERIFIED]. Radar: 6-month backtest, 0% shadow, 180-day rule history [VERIFIED] | — |
| **Model serving** | Listing risk, account risk, message risk, image models, LLM grey-zone classifier | Champion/challenger; calibrated scores so thresholds mean something | OLX GenAI images [VERIFIED]; Llama Guard pattern [VERIFIED] |
| **Decision service** | Combines rules and scores into actions on the graduated ladder; writes a decision record | Single writer of decisions, so DSA reporting has one source | Ofcom expert action ladder [VERIFIED] |
| **Case management** | Queues (by harm × uncertainty), reviewer tooling, evidence snapshot, notes, SLA timers, QA sampling | Trusted-flagger priority lane (Art. 22); notifier comms (Art. 16) | DSA [VERIFIED] |
| **Statement-of-reasons service** | Renders user notices; strips PII; submits to the Transparency Database in batches of ≤100 with `puid` idempotency | One decision → user notice + DB record + internal evidence record | TDB API [VERIFIED] |
| **Appeals service** | Art. 20 complaints ≥6 months; human-decided; reversal restores listing *and ranking*; ODS export | Appeal outcomes are high-value labels, so feed them back | DSA Art. 20 [VERIFIED] |
| **Trader registry (KYBC)** | Art. 30 data, verification results, register lookups, re-verification triggers, 6-month post-relationship deletion; also P2B business users, Omnibus trader status, DAC7 reportable sellers, INFORM high-volume sellers | One registry, many regulatory views | DSA Art. 30, DAC7, INFORM [VERIFIED] |
| **Evidence and audit store** | Immutable (WORM-style) log of decisions, rule versions, model versions, reviewer IDs and content snapshots; retention per data class | Must answer "why was this listing removed, by which rule or model version, who reviewed it?" months later | GDPR Art. 5(2) accountability [VERIFIED]; DSA Arts. 17, 20 and 24 [VERIFIED] |
| **Measurement** | Prevalence by random sampling, precision and recall per policy, time-to-action, appeal reversal rate, user-report rate, bank-reported fraud linked back to listings | Prevalence must not depend on detection | Integrity Institute [VERIFIED] |

### 6.2 Flow (one listing)

```
seller submits/edits listing
  → sync gate: rules + list lookups + light model (p99 ≤ ~300 ms)
      allow ─────────────► publish (risk tier recorded)
      hold  ─────────────► review queue (priority = harm × uncertainty)
      reject ────────────► decision record → SoR notice + TDB submission
  → async: image hashes/embeddings, duplicate search, price anomaly,
           graph features, LLM grey-zone check
      score crosses threshold → decision service → takedown/demote/friction
                                → decision record → SoR + TDB (+ case)
buyer report / trusted flagger notice / bank fraud report
  → notice record (Art.16 elements) → priority lane if trusted flagger
  → decision → notifier informed (Art.16(5)) → SoR to seller (Art.17)
seller complaint (≤6 months) → appeals queue (human) → uphold/reverse
  → labels back to training; reversal metrics to policy owners
```

### 6.3 Feedback loops and their failure modes

1. **Label sources and their biases.** Reviewer labels only cover what was queued (selection bias). User reports skew toward visible harms. Bank fraud reports arrive weeks late. Appeal reversals are the best signal of false positives. Use random-sample review to correct selection bias. [ASSUMPTION/JUDGEMENT; random sampling grounded in Integrity Institute VERIFIED]
2. **Adversarial drift.** Fraudsters A/B-test your gate: Which?'s team switched devices, Wi-Fi and identities, then edited approved ads [VERIFIED: Which? 2024-12-12]. Re-score on edit. Rate-limit rejections-and-retries per identity cluster. Avoid leaking precise rejection reasons to suspected bad actors. Note the Art. 17 tension: you must give reasons, but you don't have to give your detection thresholds.
3. **Rule rot.** Rules that no longer match, or that block more and more good users, need monitoring. Radar's rule-metrics guidance offers a ready taxonomy ("blocks going up but fraud steady → may block good users") [VERIFIED: Stripe Radar docs].
4. **Shadow before enforce.** Every new rule or model runs at 0% traffic first [VERIFIED pattern: Stripe Radar].
5. **Cross-market learning.** A shared T&S platform across country marketplaces (the Adevinta "Serenity" model, if job postings reflect reality) gives faster pattern transfer. The cost is per-market policy and legal differences, such as different illegal-content grounds per Member State. Store `territorial_scope` per decision [VERIFIED field: TDB].

---

## Key lessons for the book

1. **Classifieds fraud is mostly APP fraud the platform cannot reverse, so controls must sit before the payment.** UK purchase scams reached 175,809 cases and £118.1m in 2025: 71% of APP cases, average £671. Banks returned 78% of losses and now lobby for mandatory seller verification and secure payments on marketplaces. [VERIFIED: UK Finance 2026]
2. **Moving money on-platform is the strongest anti-fraud lever, and it is also a regulatory switch.** Buyer protection turns unrecoverable APP fraud into a mediated dispute. It also makes the platform "know the consideration", which brings DAC7 seller reporting (30 sales / €2,000 de minimis) and INFORM's high-volume seller rules (200 sales / $5,000, marketplace-processed). [VERIFIED: Which? 2024-12-12; Belastingdienst; FTC INFORM; the link between them is JUDGEMENT]
3. **Re-moderate on every material edit, not only at creation.** Which? got scam edits through Gumtree's review "in minutes" after an initial block, and kept a gift-card scam ad live on Facebook Marketplace for nearly 48 hours. [VERIFIED: Which? 2024-12-12]
4. **Say what you actually do.** leboncoin was condemned for claiming all ads were validated when they weren't. Hosting status protects you from a duty to pre-check, not from misleading claims. [VERIFIED: Clubic 2015]
5. **Treat the statement of reasons as a first-class domain object.** DSA Art. 17 covers removal *and demotion*. Art. 24(5) requires every statement to reach the Commission database. The database schema (category SCAMS_AND_FRAUD, content_type PRODUCT, automated_detection/decision, source_type, `puid`) should shape your decision record. [VERIFIED: DSA Arts. 17 and 24; TDB API]
6. **Ranking teams are in the moderation business.** Demotion is a restriction under Art. 17, promoted listings are ads under Art. 26, and ranking parameters must be disclosed (DSA Art. 27, P2B Art. 5, Omnibus). [VERIFIED: DSA Arts. 17, 26 and 27; P2B and Omnibus content is JUDGEMENT]
7. **Build one trader registry serving many laws.** DSA Art. 30 KYBC (ID or eIDAS, payment account, register number, self-certification, 6-month post-relationship deletion), Omnibus trader declaration, P2B business users, DAC7 and INFORM all need the same verified trader record with different views. [VERIFIED: DSA Art. 30; INFORM; DAC7; consolidation is JUDGEMENT]
8. **Appeals must have a human in the loop by law.** Art. 20 requires ≥6-month complaint windows and decisions "not solely on the basis of automated means". LLMs can triage and draft, not decide, and reversals are your best false-positive labels. [VERIFIED: DSA Art. 20]
9. **Rules as code, with backtest, shadow mode and audit trail.** Sigma (>1M rps, hot-swapped Haskell policies) and Stripe Radar (6-month backtests, 0% shadow allocation, 180-day rule history) are the public templates. [VERIFIED: engineering.fb.com 2015; Stripe docs]
10. **Duplicate and stolen-image detection is core fraud infrastructure.** The best public classifieds design is still OLX's 2019 pipeline: candidate keys, then a pairwise classifier, with hashes and embeddings in an inverted index at ≈10M listings/day. Perceptual hashes like PDQ have known blind spots (rotation, flips, crops). [VERIFIED: PyCon DE 2019; PDQ repo]
11. **Messaging is where scams close.** Warn-in-context on payment keywords and off-platform moves (OLX 2018). Block fake payment images and phishing QR codes before delivery (OLX 2026: images ≈30% of Polish fraud cases; QR precision 80%). [VERIFIED: ITWeb 2018; OLX 2026]
12. **Verification badges and aged accounts are attack targets.** ATO buys fraudsters "check marks, verification". Passkeys plus risk-based authentication drove Mercari's large-scale phishing losses to "effectively zero" where passkeys were enforced. [VERIFIED: Integrity Institute for Ofcom 2026; Mercari 2026]
13. **No classifieds platform is a DSA VLOP (as of 15 October 2026).** Classifieds carry the full online-platform and marketplace obligations, not systemic-risk audits. Facebook (with Marketplace inside it) *is* a VLOP. ⚠ [VERIFIED: Commission VLOP list]
14. **The UK splits fraud into two regimes.** Scam *listings* fall under OSA illegal-content duties (fraud is a Schedule 7 priority offence; duties since 17 March 2025). Paid fraudulent *ads* fall under s.38/39 Category 1/2A duties, whose code is still in consultation (final by mid-2027). Whether paid listing upgrades count as ads is open. [VERIFIED: legislation.gov.uk; Ofcom 2024-12-16 and 2026-07-10; the "bump" question is JUDGEMENT]
15. **Reviews must be anchored to real interactions.** The UK DMCC Act (6 April 2025, CMA fines up to 10% of global turnover) and the US FTC rule (August 2024) make hosting unverified reviews a liability. Log the "reasonable steps" you take. [VERIFIED: Which? 2025-04-07; FTC 2024-08-14]

## Open questions / not publicly documented

- **Adevinta / Kleinanzeigen / leboncoin / Marktplaats T&S architecture.** Only job postings and customer-facing pages were reachable. Medium blogs returned 403. Does the "Serenity" shared fraud and moderation component exist as described, and how is it split between group and country? Not documented.
- **Zillow and other US rental portals' scam-detection measures.** Not retrieved.
- **Facebook Marketplace scam prevalence from Meta itself.** Only bank-sourced estimates (TSB 34%, a 100-post sample) are public. Meta reports nothing Marketplace-specific in the scam-center post.
- **Exact DSA article wording from EUR-Lex** (all article content here came from an unofficial reproduction). Also the transparency-report implementing regulation number and dates.
- **Omnibus article text** (CRD 6a, UCPD 7(4a), 7(6), Annex I points) and **P2B Art. 5** wording; **P2B repeal** legislative status after the 19 November 2025 proposal.
- **eIDAS 2.0 relying-party obligations** (Art. 5f) and the timeline for private-sector acceptance; national bank-ID (BankID, itsme, MitID) usage by classifieds platforms.
- **Ofcom register of categorised services (July 2026).** Are any UK classifieds (Gumtree, Rightmove, Zoopla, Auto Trader) Category 1? Does a paid listing upgrade count as a "paid-for advertisement" under s.38?
- **CMA fake-review guidance** text: what "reasonable and proportionate steps" means for marketplaces.
- **Whether DAC7 reaches classifieds with optional in-platform payments** for only part of their transactions. The "knowable consideration" test is unclear here.
- **DSA Art. 30(7) home-address display** for sole traders: whether any Member State or Commission guidance allows an INFORM-style home-seller exception.
- **MAU figures** published by classifieds under DSA Art. 24(2) (how close any is to 45M).
- **The CARS Rule's** current status (believed vacated in January 2025) and the Meta–DOJ housing-ads settlement details (2022).
- **LLM moderation in production at classifieds scale:** cost per decision, latency and accuracy against classical classifiers. No first-party numbers are public beyond OLX's 80% QR precision.

## Source list

| # | Title | Publisher | Date | URL |
| --- | --- | --- | --- | --- |
| 1 | Annual Fraud Report 2026 (PDF) | UK Finance | 2026-06-12 | https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf |
| 2 | Annual Fraud Report 2026 (landing page) | UK Finance | 2026-06-15 | https://www.ukfinance.org.uk/policy-and-guidance/reports/annual-fraud-report-2026 |
| 3 | UK fraud losses close to £1.3bn, reveals new report | Financier Worldwide | 2026-07-02 | https://www.financierworldwide.com/fw-news/2026/7/2/uk-fraud-losses-close-to-13bn-reveals-new-report |
| 4 | Over third of Facebook Marketplace ads are scams, warns TSB | FStech | 2024-01-18 | https://fstech.co.uk/fst/Over_Third_Of_Facebook_Marketplace_Ads_Are_Scams_Warns_TSB.php |
| 5 | UK Purchase Scams Rising by 42% (Lloyds) | Crowdfund Insider | 2023-12-12 | https://www.crowdfundinsider.com/2023/12/218012-fraudulent-activities-uk-purchase-scams-rising-by-42-compared-to-last-year-report/ |
| 6 | A third of buyers have experienced a scam on popular second-hand marketplaces | Which? | 2024-05-09 | https://www.which.co.uk/policy-and-insight/article/a-third-of-buyers-have-experienced-a-scam-on-popular-second-hand-marketplaces-in-the-last-two-years-which-warns-aEea68N4nnah |
| 7 | Scam ads slipping through the net too easily on second-hand marketplaces | Which? | 2024-12-12 | https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1 |
| 8 | It's a steal: how we listed fake "bargains" on marketplace websites | Which? | 2024-12-12 | https://www.which.co.uk/news/article/its-a-steal-how-we-listed-fake-bargains-on-marketplace-websites-aQDLs8m1bFWa |
| 9 | Fake reviews and sneaky fees banned under new law | Which? | 2025-04-07 | https://www.which.co.uk/news/article/fake-reviews-and-sneaky-fees-banned-under-new-law-campaigned-for-by-which-aLzVp4g0S76D |
| 10 | We fight online fraud with the power of AI | OLX Group | 2026-01-28 | https://www.olxgroup.com/?p=4590 |
| 11 | OLX blocks scammers using advanced algorithms | ITWeb | 2018-05-14 | https://www.itweb.co.za/article/olx-blocks-scammers-using-advanced-algorithms/nWJadvb8APOMbjO1 |
| 12 | Fighting fraud: finding duplicates at scale (A. Grigorev, OLX) | PyCon DE & PyData Berlin | 2019 | https://pycon.de/archive/2019/talks/fighting-fraud-finding-duplicates-at-scale/ |
| 13 | OLX fraud detection (Ukraine) | Interfax-Ukraine | 2025-01 (search summary only) | https://en.interfax.com.ua/news/general/1038382.html |
| 14 | Senior Data Scientist (Kleinanzeigen T&S) job posting | Built In | 2025–2026 (search summary) | https://builtin.com/job/senior-data-scientist-d-f-m/7228169 |
| 15 | Sicherheitshinweise (safety advice) | Kleinanzeigen | date unknown | https://themen.kleinanzeigen.de/sicherheitshinweise/ |
| 16 | Leboncoin a prétendu à tort qu'il relisait toutes les annonces | Clubic | 2015-12-17 | https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html |
| 17 | French consumer group warns against new online purchasing scam | Connexion France | date not captured | https://connexionfrance.com/article/Practical/Money/French-consumer-group-warns-against-new-online-purchasing-scam |
| 18 | Rightmove fraud guide | Rightmove | date unknown | https://www.rightmove.co.uk/guides/?p=385 |
| 19 | Cracking down on organized crime behind scam centers | Meta | 2024-11-21 (upd. 2025-07-14) | https://about.fb.com/news/2024/11/cracking-down-organized-crime-scam-centers/ |
| 20 | Fighting spam with Haskell | Engineering at Meta | 2015-06-26 | https://engineering.fb.com/2015/06/26/security/fighting-spam-with-haskell/ |
| 21 | Fraud prevention rules (Radar) | Stripe Docs | current, date unknown | https://docs.stripe.com/radar/rules |
| 22 | Bridging the gap between passwords and passkeys with risk-based authentication | Mercari Engineering | 2026-07-30 | https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/ |
| 23 | PDQ (ThreatExchange) | Meta / GitHub | current (impl. list Nov 2025) | https://github.com/facebook/ThreatExchange/tree/main/pdq |
| 24 | Llama Guard: LLM-based Input-Output Safeguard for Human-AI Conversations | arXiv (Inan et al.) | 2023-12-07 | https://arxiv.org/abs/2312.06674 |
| 25 | Fraudulent Advertising and Account Integrity: Expert Insights on Best Practice | Integrity Institute for Ofcom | 2026-07 | https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf |
| 26 | Consultation: Fraudulent Advertising Codes of Practice | Ofcom | 2026-07-10 (upd. 07-28) | https://www.ofcom.org.uk/online-safety/online-fraud/consultation-fraudulent-advertising-code-of-practice |
| 27 | Statement: Protecting people from illegal harms online | Ofcom | 2024-12-16 (upd. 2026-06-25) | https://www.ofcom.org.uk/online-safety/illegal-and-harmful-content/statement-protecting-people-from-illegal-harms-online |
| 28 | Online Safety Act 2023, s.38 | legislation.gov.uk | in force 2024-01-10 | https://www.legislation.gov.uk/ukpga/2023/50/section/38 |
| 29 | Online Safety Act 2023, Schedule 7 | legislation.gov.uk | 2023 | https://www.legislation.gov.uk/ukpga/2023/50/schedule/7 |
| 30 | Ofcom publishes Register of Categorised Services | RPC | 2026-07 (search summary) | https://www.rpclegal.com/thinking/media/ofcom-publishes-register-of-categorised-services/ |
| 31 | Supervision of the designated VLOPs and VLOSEs | European Commission | upd. 2026-10-15 | https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses |
| 32 | DSA Articles 16, 17, 19, 20, 22, 24, 26, 27, 30, 31, 32 (unofficial reproduction of Reg. (EU) 2022/2065) | eu-digital-services-act.com | Regulation of 2022-10-19 | https://www.eu-digital-services-act.com/Digital_Services_Act_Article_30.html (and the corresponding _Article_NN pages) |
| 33 | DSA Transparency Database (homepage statistics) | European Commission | rolling 180 days to 2026-10-19 | https://transparency.dsa.ec.europa.eu/ |
| 34 | DSA Transparency Database API documentation | European Commission | date unknown | https://transparency.dsa.ec.europa.eu/page/api-documentation |
| 35 | DSA Transparency Database: questions and answers | European Commission | upd. 2025-07-07 | https://digital-strategy.ec.europa.eu/en/faqs/dsa-transparency-database-questions-and-answers |
| 36 | DSA Statement of Reasons transparency report | Checkstep | date unknown | https://www.checkstep.com/dsa-statement-of-reason-report |
| 37 | Information about DAC7 for platform operators | Belastingdienst (NL Tax Administration) | date unknown | https://belastingdienst.nl/wps/wcm/connect/en/business/content/information-for-platform-operators-dac7 |
| 38 | DAC7 – Reporting obligations for digital platform operators | Bird & Bird | 2021 | https://cm.twobirds.com/en/insights/2021/belgium/belgium-dac7-reporting-obligations-for-digital-platform-operators |
| 39 | Platform-to-business trading practices | European Commission | upd. 2026-07-02 | https://digital-strategy.ec.europa.eu/en/policies/platform-business-trading-practices |
| 40 | Consumer Rights Directive | European Commission | date unknown | https://commission.europa.eu/law/law-topic/consumer-protection-law/consumer-contract-law/consumer-rights-directive_en |
| 41 | Review of EU consumer law (Digital Fairness) | European Commission | date unknown | https://commission.europa.eu/law/law-topic/consumer-protection-law/review-eu-consumer-law_en |
| 42 | European Digital Identity Regulation | European Commission | upd. 2026-06-22 | https://digital-strategy.ec.europa.eu/en/policies/eudi-regulation |
| 43 | EU Digital Identity Wallet Home | European Commission | date unknown | https://ec.europa.eu/digital-building-blocks/sites/display/EUDIGITALIDENTITYWALLET/EU+Digital+Identity+Wallet+Home |
| 44 | Energy Performance of Buildings Directive | European Commission (DG ENER) | date unknown | https://energy.ec.europa.eu/topics/energy-efficiency/energy-efficient-buildings/energy-performance-buildings-directive_en |
| 45 | Art. 5 GDPR (unofficial reproduction) | gdpr-info.eu | date unknown | https://gdpr-info.eu/art-5-gdpr/ |
| 46 | Commission press release IP/24/5801 (Facebook Marketplace) | European Commission | 2024 (amount not retrieved) | https://ec.europa.eu/commission/presscorner/detail/en/ip_24_5801 |
| 47 | Informing Businesses about the INFORM Consumers Act | US FTC | 2023-06 (edited 2025-01) | https://www.ftc.gov/business-guidance/resources/informing-businesses-about-inform-consumers-act |
| 48 | FTC announces final rule banning fake reviews and testimonials | US FTC | 2024-08-14 | https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials |
| 49 | Used Car Rule | US FTC | rule 1985; last amended 2016 | https://www.ftc.gov/legal-library/browse/rules/used-car-rule |
| 50 | 24 CFR § 100.75 Discriminatory advertisements | Cornell LII | date unknown | https://www.law.cornell.edu/cfr/text/24/100.75 |
