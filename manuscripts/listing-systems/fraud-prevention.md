{id: fraud-prevention}
# 25. Scams, Fakes and Account Takeovers: Fraud Prevention for Listings

![Scams, Fakes and Account Takeovers: Fraud Prevention for Listings — logo](listing-systems-architecture/posts/25-fraud-prevention/assets/images/25-fraud-prevention/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn the fraud types that classifieds platforms face and the signals that expose them. You will see how a risk scoring service combines real-time and batch features, rules and models, and how step-up friction, messaging controls and feedback loops turn a score into prevention, using a fake-rental ring in Barcelona.

> **WHY THE BUSINESS CARES:** Most classifieds fraud is a bank transfer the platform never sees and cannot reverse. The victim blames the brand anyway. Fraud losses do not appear on the marketplace's profit and loss statement, but they show up in lost buyers, support costs, press coverage and, increasingly, in demands from banks and regulators that platforms carry part of the cost.

> **WHY ARCHITECTS SHOULD CARE:** Fraud prevention is a real-time decision system with adversarial inputs, delayed and biased labels, and a latency budget inside the insertion, messaging and login paths. The design of features, identity linking and feedback loops decides whether the platform learns faster than the fraudsters do.

> **KEY POINTS:**
>
> * **Classifieds fraud happens before the payment, so prevention has to happen there too.** In lead-generation marketplaces the money usually moves off the platform by bank transfer. The controls that work sit before it: who can list, what can be said in messages, which links get through, and steering buyers towards a protected payment.
> * **Score the actor, not only the item.** A fake rental looks plausible one listing at a time. The fraud becomes visible when listings, accounts, devices, payment accounts and photos are linked into one graph. Signals that are weak on their own (a stolen photo, a low price, a new account) become decisive together. The risk scoring service exists to combine them within the latency of a user action.
> * **Answer risk with graduated friction, and learn from every outcome.** Blocking everything suspicious punishes good users. Step-up friction (verification, delays, limits) costs genuine users little and fraudsters a lot. Thresholds should come from an explicit cost model, and labels from victims, banks, reviewers and appeals have to reach the models within days, because organized fraud adapts within days.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Fast Mail for Fraudsters** — payment-link phishing and deposit requests close in the conversation, so messaging without link, domain and pattern controls becomes the platform's main fraud channel.
> * **Set-and-Forget AI** — a fraud model with stale labels and no shadow testing goes on approving the scam pattern that replaced the one it was trained on.
> * **Seeing Double** — when stolen photos are treated as harmless duplicates, the deduplication pipeline that should expose a fake listing ends up hiding it.

A listing marketplace is a machine for getting strangers to trust each other enough to meet, call or pay. Fraud exploits exactly that. The fraudster borrows the trust the platform has built, uses it to start a conversation, and then moves the victim somewhere the platform cannot see: a bank transfer, a fake payment page, a messaging app. **Most of the loss happens after the victim has left the platform, but the platform is where the scam was set up.**

This chapter is about catching the setup. It owns three terms. A **fraud signal** is an observable property of an item, actor, session or relationship that changes the probability of fraud. A **risk score** is a calibrated estimate of that probability for a specific action, such as publishing a listing, sending a message, logging in or releasing a payout. **Step-up friction** is an additional check imposed in proportion to risk, which genuine users pass easily and fraudsters do not.

This chapter supplies the scores that Part V's shared trust platform acts on. [Trust and Safety as a Platform](#trust-and-safety-architecture) built the decision service that turns a score into enforcement and appeals; fraud scoring is how that service catches fraudsters who exploit the speed Part IV gave new listings. The strongest frictions it recommends are identity checks, which [Who Is on the Other Side? Identity and Verification](#identity-and-verification) designs next. Payment-side fraud in transactional flows (chargebacks, payout holds) is covered in [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments). The running example is Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

{id: fraud-prevention--setting-the-scene-at-veldmark-the-barcelona-fake-rental-ring}
## Setting the Scene at Veldmark: The Barcelona Fake-Rental Ring

On Thursday **1 July 2027**, a new account on Hearthly Spain published a rental listing for a renovated two-bedroom flat in Barcelona's Eixample district at about 35% below comparable rents. Hearthly Spain was the former Casavista, acquired in 2025 and rebranded in 2026. Over the next twelve days, **26 accounts** published **180** such listings. Every listing used photos copied from real listings, most of them still live on Hearthly and published by real agencies. Each "landlord" was abroad, could not arrange a viewing and asked for a deposit by bank transfer to secure the flat.

By the time the listings came down on Tuesday **13 July**, **63 people** had reported losses totaling about **€71,000**, roughly €1,130 each, in most cases one month's advertised rent paid as a "deposit". The listings had received about 4,700 contacts.

The detectors did not miss the ring, and that is the uncomfortable part. The ledger records that it was detected through **perceptual-hash matches** against existing listings plus **price anomalies**. A perceptual hash is a fingerprint of an image that survives resizing and recompression ([Photos Sell: Media Pipelines for Listings](#media-pipeline) owns the capability). Hearthly Spain's hash index matched the first stolen photos on 1 July, within minutes of upload. Its rent-anomaly check flagged most of the listings as well. The signals existed from the first day. What failed was everything between the signals and a decision.

- **Each signal went to a different place.** The photo match created a "possible duplicate" item in the general moderation queue. The rent anomaly created a separate, low-priority "price check" item. No component combined them.
- **Reviewers saw listings, not actors.** A reviewer looking at one listing whose photos matched an agency's listing saw something that looked like a second agency marketing the same flat, which is common in real estate ([One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)). Eleven of the first photo-match items were closed as legitimate duplicates.
- **Nobody linked the accounts.** The 26 accounts used five devices and four Spanish bank accounts, which turned out to belong to recruited money mules. Hearthly Spain's stack had no identity graph, and none of the accounts had been asked to prove more than an e-mail address ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)). Each account looked new and unremarkable.
- **The first victim report, on Friday 9 July, was routed to support** as a dispute between a tenant and a landlord.

![Three fraud signals, a photo match, a price anomaly and a victim report, flowing into three walled-off trays while an empty dashed gear in the middle combines nothing.](listing-systems-architecture/posts/25-fraud-prevention/assets/images/25-fraud-prevention/signals-in-separate-places.jpeg)

**Figure 1:** *In Barcelona the photo matches, rent anomalies and the first victim report all existed early, but each went to a different place and no component combined them into one decision.*

On Monday 12 July, a Hearthly analyst in Barcelona noticed that three victim reports named listings whose photos had been flagged. She queried the hash matches, the price flags and the account metadata by hand, and linked all 26 accounts in an afternoon. A combined rule went live on Tuesday morning, and by 16:40 that day all 180 listings had been removed and the accounts suspended. Hearthly Spain was not yet on Veldmark's shared trust-and-safety platform, which went live for Tradeyard Netherlands and Belgium in November 2027.

Ingrid Halvorsen, the Group Chief Architect, asked Aisha Rahman, the Group Head of Trust & Safety, and Priya Raman, Head of Data & ML, one question in the review that followed: **"We had the signals on day one. What would it have taken to act on day one?"** The rest of this chapter is the answer: a risk scoring service that scores actors as well as items, an identity graph, a combination of rules and models, graduated friction, and feedback loops measured in hours.

{id: fraud-prevention--the-threat-model-what-classifieds-fraud-looks-like}
## The Threat Model: What Classifieds Fraud Looks Like

{id: fraud-prevention--why-classifieds-differ}
### Why classifieds differ

Most classifieds platforms are lead-generation businesses: buyer and seller meet on the platform, but the money often moves elsewhere ([Classifieds, Leads, Transactions and Managed Models: A Marketplace Taxonomy](#marketplace-taxonomy) covers the business models). The platform sees the listing and the conversation. It often does not see the payment and cannot reverse it. The dominant fraud is therefore **authorized push payment (APP) fraud**: the victim willingly sends money, usually by bank transfer, to someone who is not who they claim to be.

Purchase scams, the typical classifieds fraud, are the most common kind of APP fraud in UK Finance's data, the most detailed public series. Its 2026 annual fraud report, covering 2025, counts **175,809 purchase-scam cases** in the UK with losses of **£118.1 million**. Purchase scams were **71% of all APP scam cases** and had the lowest average value of the APP types, **£671**. It describes the typical pattern: although "many online platforms offer secure payment options, the criminal will persuade their victim to pay via a bank transfer instead". **78% of purchase-scam losses were returned to victims**, which reflects the UK's mandatory reimbursement regime from October 2024 and explains why banks now ask the government to "mandate seller verification and secure payment protections on online marketplaces" ([UK Finance, 2026](https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf)). As of October 2026 that is a lobbying position, not law.

The architectural consequence is that a classifieds platform's controls are mostly **pre-payment**: who can list, what can be listed, what can be said and linked in messages, and how strongly buyers are steered towards a protected in-platform payment where one exists.

{id: fraud-prevention--a-typology}
### A typology

| Fraud type | Mechanism | Strongest signals | Main control point |
| --- | --- | --- | --- |
| **Advance payment / non-delivery** | Fake seller asks for a bank transfer, gift cards or a "friends and family" payment, then disappears | Below-market price, stock photos, new account, payment terms in text | Listing scoring; message scanning; protected payment |
| **Payment-link phishing** | Fake *buyer* sends the *seller* a link or QR code to a counterfeit "payment received" or courier page that harvests card or bank data | New domain, platform brand in a foreign URL, QR code in chat | Message gate: link and domain controls |
| **Fake rentals** | Copied photos of a real property, low rent, landlord "abroad", deposit before viewing | Stolen photos, rent anomaly, no viewing, unregistered lister | Listing scoring with image reuse; lister verification |
| **Vehicle deposit scams** | A car priced to sell fast; deposit to "hold" it, or delivery through a fake escrow or shipping firm | Price vs. market value, VIN or plate reused across listings, external escrow domains in text | Listing scoring; dealer verification; message scanning |
| **Triangulation** | Fraudster relists a real seller's item; the victim pays the real seller, believing it is for the fraudster's item; two victims dispute each other | Cloned listing with different contact data | Duplicate detection across sellers |
| **Overpayment** | Fake buyer "overpays" with a fake transfer screenshot and asks for the difference back | Payment-proof images, refund keywords | Message image checks; warnings |
| **Account takeover (ATO)** | Credentials phished or stuffed; an aged, reputable account then posts scam listings | Session change: new device, network, client; sudden change of behavior | Login risk; step-up authentication |
| **Fake sellers and fake shops** | Batches of new accounts or pseudo-dealers with stolen identity or company data | Shared devices, IPs, e-mail patterns, register mismatch | Onboarding risk; identity graph; business verification |
| **Counterfeit and prohibited goods** | Branded goods at implausible prices; weapons, drugs, recalled products | Brand × price anomaly, rights-holder notices, image classifiers | Listing scoring ([Trust and Safety as a Platform](#trust-and-safety-architecture)) |

Three public observations sharpen the table.

- **Images are a large share of chat fraud.** In a January 2026 post, OLX said fraudulent images make up about **30% of fraud cases** on its Polish marketplace. Its generative-AI chat image system blocks suspicious images in real time and detects fraudulent QR codes in chat with **80% precision**. It is live in Poland, Portugal, Bulgaria, Romania and other markets ([OLX Group, 2026](https://www.olxgroup.com/?p=4590)).
- **Scammers edit after approval.** In Which?'s December 2024 undercover test, Gumtree blocked a first scam-style ad, but edited versions passed review "in minutes" ([Which?, 2024](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1)).
- **Fraud is industrial.** Meta reported in November 2024 that it had removed more than two million accounts linked to scam centers in Southeast Asia and elsewhere ([Meta, 2024](https://about.fb.com/news/2024/11/cracking-down-organized-crime-scam-centers/)). Classifieds fraud is increasingly run by organized groups that test a platform's defenses systematically and change scripts within days. A rules engine updated twice a week loses that race.

{id: fraud-prevention--fraud-signals}
## Fraud Signals

A fraud signal is useful only if it is available at decision time, hard for the fraudster to change cheaply, and not too costly for genuine users. The families below are the ones that matter for listings.

| Signal family | Examples | Available when | Cost to the fraudster to evade |
| --- | --- | --- | --- |
| **Device and client** | Device identifier, emulator or rooted device, client integrity attestation, app version | Login, insertion, message send | Medium: device farms and emulator kits exist |
| **Network** | IP reputation, data-center or proxy IP, IP country vs. market, IP velocity | Every request | Low to medium: residential proxies are cheap |
| **Account and identity** | Account age, verification level, e-mail and phone age and type (virtual numbers), recent changes of contact details or password | Every action | Medium: aged accounts are bought, or taken over |
| **Behavior and velocity** | Listings per hour, first contacts per hour, time from sign-up to first listing, copy-paste patterns, typing cadence | Rolling windows | Medium: slowing down costs the fraudster throughput |
| **Content** | Payment terms, off-platform contact details, urgency phrases, text in images (OCR), language mismatch with market | Insertion, edit, message | Low per item, but every evasion is a new pattern to learn |
| **Price** | Price vs. market estimate for the category, model, location and condition | Insertion, edit | High: a fake bargain needs a low price to work |
| **Media reuse** | Perceptual-hash or embedding match to another seller's photos, to stock photos, to known scam images | After upload, seconds | Medium: cropping and flipping defeat simple hashes, but embeddings catch more |
| **Graph** | Shared devices, phones, IBANs, IP ranges, images and text across accounts; distance to known fraud | Near real time if maintained incrementally | High: rings must share infrastructure to be economical |
| **External** | Bank fraud reports, phishing-domain feeds, domain registration age, trusted-flagger notices, chargebacks | Minutes to weeks | Not controllable by the fraudster |

Two signals deserve special attention because they are hard to fake. **Price** is the bait: a fake bargain has to be a bargain. A valuation or market-price model, built for buyers, doubles as a fraud feature. Motorvane's market-value model, which rates the Essen Volkswagen Golf at €22,800 against an asking price of €21,900, can flag a 2021 Golf offered at €12,000 just as easily ([Models in Production: ML Platforms and Use Cases](#ml-platform) owns these models). **The graph** is the ring's weak point: organized fraud has to reuse devices, phone numbers, bank accounts and photos to stay profitable, and every reuse is a link.

The Barcelona ring illustrates both. Its prices were about 35% below market, which required structured surface, rooms and district to compute ([Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)). Its 26 accounts shared five devices and four IBANs. No single account was alarming; the cluster was unmistakable.

{id: fraud-prevention--duplicate-photos-one-detector-two-policies}
### Duplicate photos: one detector, two policies

Image reuse is the strongest single signal against fake rentals and cloned listings, and the best public classifieds design for it is still a 2019 conference talk. At PyCon DE 2019, Alexey Grigorev described OLX's duplicate-listing detection for fraud. Candidates were generated by category, city, seller, IP or device and image hashes. A pairwise classifier, trained on human-labeled pairs, compared price difference, location distance, title similarity and image similarity. Images were matched with hashes and then neural embeddings indexed for approximate search in Elasticsearch, at a target of about ten million listings a day. The talk also noted that cropping, rotation and flipping defeat simple hashes ([PyCon DE, 2019](https://pycon.de/archive/2019/talks/fighting-fraud-finding-duplicates-at-scale/)). The system is seven years old and certainly replaced, but the shape is sound.

A platform needs both a hash for cheap exact and near-exact matches and an embedding for crops and edits. Meta's open-source PDQ perceptual hash documents its own limits: a suggested match threshold, a quality score below which hashes should be discarded, and no guaranteed invariance to rotation or flips ([Meta ThreatExchange, n.d.](https://github.com/facebook/ThreatExchange/tree/main/pdq)).

The design lesson from Barcelona is about the policy, not the detector. **"Same photos" means opposite things depending on who posted them.** Same seller, same photos is a repost: a spam or ranking problem. Different seller, same photos is either a legitimate multi-agency listing or a stolen one, and the evidence that separates them is the relationship between the sellers: same agency network, same software vendor feed, verified agency accounts, or a new private account with a foreign phone number. The [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution) chapter makes the same point from the clustering side. A photo match between unrelated sellers must go to fraud scoring with the seller context attached, never to a deduplication queue on its own.

{id: fraud-prevention--architecture-the-risk-scoring-service}
## Architecture: The Risk Scoring Service

A **risk scoring service** answers one question for many callers: *how risky is this action, by this actor, right now?* Callers include the insertion and edit flows, the message send path, login and account recovery, contact-detail reveal, and payout release where the marketplace handles payments. The service does not decide the enforcement action; it returns scores, reasons and recommended friction to the decision service described in [Trust and Safety as a Platform](#trust-and-safety-architecture).

The design below is a **reference-architecture inference**, built from public adjacent systems (Meta's Sigma rule engine, Stripe Radar's documented rule operations, Uber's 2017 description of a shared feature store, Mercari's 2026 risk-based authentication) and from the evidence above. No classifieds company has published a fraud-scoring architecture in this form.

![Diagram: The risk scoring service](listing-systems-architecture/posts/25-fraud-prevention/assets/images/25-fraud-prevention/fig02-risk-scoring-service-real-time-path.jpeg)

**Figure 2:** *The risk scoring service. The real-time path reads precomputed features and evaluates rules and models within the caller's latency budget; streaming and batch jobs keep the features, the identity graph and the image index current; decisions and their outcomes return as labels.*

{id: fraud-prevention--real-time-and-batch-what-runs-where}
### Real-time and batch: what runs where

The real-time path has a budget measured in tens of milliseconds, because it sits inside a user's action. It cannot compute a graph traversal or an image embedding on the request. It **reads** features that streaming and batch jobs have already computed: counters ("first contacts sent by this device in the last hour"), graph features ("distance from this account to the nearest account terminated for fraud"), image matches ("photos of this listing match photos of another seller's live listing") and price features ("asking price relative to estimate").

| Work | Where it runs | Latency | Example |
| --- | --- | --- | --- |
| Block-list lookups, simple rules | Real-time path | Milliseconds | Phone number on the shared block list; URL domain registered today |
| Model inference on precomputed features | Real-time path | Tens of milliseconds | Listing risk, message risk, login risk |
| Velocity counters | Stream processing | Seconds | First contacts per device per hour |
| Image hashes and embedding matches | Asynchronous after upload | Seconds | Photo match to another seller's listing |
| Identity graph updates | Stream processing, incremental | Seconds to minutes | New account shares a device with a suspended one |
| Graph-wide community detection | Batch | Hours | Rings of accounts sharing infrastructure |
| Model training and backtesting | Batch | Daily to weekly | Retraining on last week's labels |

A **feature store**, a shared system that serves the same feature definitions online for scoring and offline for training, is justified once real-time behavioral features drive decisions. Uber's 2017 description of Michelangelo is the standard reference: precomputed online features, the same pipelines for training and serving, and predictions logged and joined with outcomes ([Uber Engineering, 2017](https://www.uber.com/blog/michelangelo-machine-learning-platform/)). No classifieds company has documented one publicly, and many classifieds models run on attributes the listing record already holds. Fraud is the use case that changes the calculation, because its best features are behavioral, cross-entity and time-sensitive. The essential property is **point-in-time correctness**: training must use the feature values as they were when the decision was taken, not as they are now, or the model learns from information it would not have had. [Models in Production: ML Platforms and Use Cases](#ml-platform) owns the feature store as a platform component.

{id: fraud-prevention--rules-and-models-together}
### Rules and models together

Rules and models are not alternatives. They do different jobs.

| | Rules | Models |
| --- | --- | --- |
| Best at | Known patterns, hard policy, fast response to a new script | Combining many weak signals, generalizing to variants |
| Time to deploy | Minutes, if the rule platform allows it | Days to weeks (labels, training, validation) |
| Explainability | Direct: "domain registered today" | Needs reason codes from feature attributions |
| Failure mode | Rot: rules accumulate, overlap and block good users | Drift: the scam changes and the model keeps scoring the old pattern |
| Adversarial behavior | Easy to probe and evade once discovered | Harder to probe, but learnable from rejections |

The operating model that works is the one Stripe documents for Radar: rules written as conditions on attributes, including model scores, **backtested** against historical data before activation, run in **shadow mode** at 0% traffic to report what they would have done, rolled out gradually, and recorded in an audit trail ([Stripe Radar docs, n.d.](https://docs.stripe.com/radar/rules)). Meta's 2015 description of Sigma adds the deployment discipline: policies as code, hot-swapped into production continuously ([Engineering at Meta, 2015](https://engineering.fb.com/2015/06/26/security/fighting-spam-with-haskell/)).

The Barcelona combined rule shows the division of labor. It was written in an afternoon:

> photo match to a listing of an **unrelated** seller **and** rent at least 25% below the district estimate **and** account younger than 30 days **and** lister not a verified agency → hold all the account's listings and open one case for the account cluster.

That rule stopped the ring. A model trained on the ring's 180 listings, and on the 2,000 or so fake-rental listings Hearthly Spain had removed over the previous year, replaced it six weeks later, because the next ring would use 20% discounts and slightly older accounts. **Rules are the fast response; models are the durable one.** A platform that only has one of the two either reacts too slowly or overfits to last month.

{id: fraud-prevention--scoring-actors-not-just-items}
### Scoring actors, not just items

The deepest design choice in the service is the **unit of scoring**. A listing score answers "is this listing fraudulent?" An actor score answers "is this account, or this cluster of accounts, operated by a fraudster?" Organized fraud is an actor problem. A ring's individual listings are designed to pass item-level checks. Its infrastructure is not.

The **identity graph** links accounts through shared attributes: devices, phone numbers, e-mail patterns, payment accounts, IP ranges, image hashes, even near-identical listing text. Its main uses are to:

- **propagate known fraud**: an account two hops from a terminated fraud account starts with a higher risk score;
- **detect rings**: dense clusters of new accounts sharing infrastructure are suspicious even before any report; and
- **scope enforcement**: when one account is confirmed as fraud, the linked accounts are reviewed in the same case, so a ring is taken down at once rather than one listing at a time.

![Rental listings that each look clean in an item view, contrasted with an actor view where many accounts link to a few shared devices and payment accounts in one cluster.](listing-systems-architecture/posts/25-fraud-prevention/assets/images/25-fraud-prevention/actor-graph-reveals-ring.jpeg)

**Figure 3:** *A ring designed to pass item-level checks shows up in the actor view: the 26 Barcelona accounts shared five devices and four bank accounts, which an identity graph links at creation.*

The graph has two hard constraints. Shared attributes are not proof: families share devices, offices share IP addresses, agencies share photos legitimately. Graph features should raise scores and widen cases, not trigger terminations on their own. And the graph is personal data. At Veldmark, the shared cross-brand block list holds only hashed identifiers of accounts terminated for fraud, with a two-year retention approved by Lucía Ortega, the Group Data Protection Officer, under a fraud-prevention legitimate interest. Each brand's graph of ordinary accounts stays within that brand.

{id: fraud-prevention--step-up-friction}
## Step-Up Friction

Blocking is a blunt answer to a probability. Most risky actions are taken by genuine users, and a platform that blocks every account with a score above 0.5 loses customers it needed. **Step-up friction** asks for more evidence instead: something a genuine user can provide quickly and a fraudster cannot, or can only at a cost that ruins the economics of the scam.

Airbnb described the approach publicly in 2018 as **targeted friction**. Machine-learning models score bookings for payment fraud. Instead of blocking above a threshold, Airbnb applies frictions such as micro-authorizations (two small charges the cardholder must identify), 3-D Secure authentication or billing-statement verification. The threshold is chosen by minimizing a loss that weighs the cost of genuine users abandoning the friction against the fraud losses it prevents, and the effect of each friction on good users is measured by A/B testing on low-risk users ([InfoQ, 2018](https://www.infoq.com/news/2018/03/financial-fraud-ml-airbnb/), summarizing an Airbnb engineering post). The system is eight years old; the method is the durable part.

A friction ladder for a listing marketplace:

| Friction | Defeats | Cost to genuine users | Typical trigger |
| --- | --- | --- | --- |
| In-context warning ("never pay a deposit before a viewing") | Naive victims | Almost none | Payment keywords, off-platform request in a message |
| Delay: listing held for a few minutes or until asynchronous checks finish | Hit-and-run listings | Small | New account in a high-risk category |
| Limits: listings, first contacts or contact-detail reveals per day | Spam and mass outreach | Small for normal users | Velocity, new account |
| Phone verification by SMS | Cheap bulk accounts | Small; virtual numbers weaken it | Account risk in the grey band |
| Strong authentication (passkey or second factor) | Phishing-based account takeover | Small once set up | Login from a new device; recovery |
| Identity or business verification ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)) | Most fake-seller farms | Medium | Rentals, high-value vehicles, payouts |
| Protected payment only | Advance-payment fraud | Medium: some buyers prefer cash | High-risk category and price band |

Two public sources support the ladder's upper rungs. Mercari reported in July 2026 that where passkeys were required, "large-scale phishing financial damages have been effectively zero", and that its risk-based authentication scores session and account posture, using client integrity, network reputation and device signals ([Mercari Engineering, 2026](https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/)). The Ofcom-commissioned expert report of July 2026 recommends "creating delays between creating an account and reaching a large audience" and notes that verification friction "directly disrupts" repeat bad actors ([Integrity Institute for Ofcom, 2026](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf)).

{id: fraud-prevention--choosing-a-threshold-a-worked-example}
### Choosing a threshold: a worked example

Tradeyard's shared T&S platform introduced a friction in December 2027: a new account that tries to send more than five first-contact messages within an hour must verify a phone number before sending more, if its message-risk score is above a threshold. The question was which threshold. Priya Raman's team ran a two-week shadow evaluation and estimated, per week, about **2,000 fraudulent new accounts** reaching the velocity trigger. Their working assumptions: 85% of fraud accounts fail or abandon the verification; 8% of genuine accounts abandon it; an unstopped fraud account causes about **€180** of expected harm (victim losses, support cost and lost buyers); a lost genuine account costs about **€25** in expected future contribution. All figures are illustrative.

| Threshold | Accounts challenged per week | Fraud accounts challenged | Genuine accounts challenged | Fraud stopped | Genuine lost | Weekly cost |
| --- | --- | --- | --- | --- | --- | --- |
| No friction | 0 | 0 | 0 | 0 | 0 | €360,000 |
| Score ≥ 0.3 | 60,000 | 1,800 | 58,200 | 1,530 | 4,656 | €201,000 |
| Score ≥ 0.5 | 22,000 | 1,500 | 20,500 | 1,275 | 1,640 | **€171,500** |
| Score ≥ 0.7 | 6,000 | 1,050 | 4,950 | 893 | 396 | €209,160 |

The weekly cost is (2,000 − fraud stopped) × €180 + genuine lost × €25. The lowest cost is at 0.5, not at the most aggressive threshold and not at the most permissive. Three things matter more than the specific numbers. The **cost of a lost genuine user is a business input**, and the marketplace general manager, not the fraud team, should own it. The 8% abandonment rate is **measured by experiment**, not guessed, because friction design (one tap versus a form) changes it several-fold. And the threshold is **revisited when fraud adapts**: if fraudsters start buying verified phone numbers, the "fraud stopped" column shrinks and the optimum moves.

{id: fraud-prevention--fraud-controls-in-messaging}
## Fraud Controls in Messaging

Most classifieds scams close in the conversation, so the controls have to act before a message is delivered. Payment-link phishing, deposit requests, fake courier offers and moves to other messaging apps all happen there. [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) owns the conversation model and its storage; this section covers the fraud controls inside it.

Tradeyard shows the cost of scanning too late. Its users sent about 11 million messages a day in 2026, and NL and BE users filed about **41,000 reports of payment-link phishing** that year. On Sunday 7 March 2027, a fake Safe Deal payment link reached Femke, who was selling a €240 city bike in Rotterdam, because its domain had been registered that day and no rule looked at domain age. The account was suspended seven minutes after Femke reported it, and a new rule then withheld 37 similar messages to other sellers. Seven minutes was fast, but the message should never have been delivered.

A reference design for message-level fraud controls:

1. **Extract** URLs, QR payloads (decoded from images), phone numbers, e-mail addresses, IBANs and messaging-app handles from every message and image.
2. **Check links** against allow and deny lists, a domain-age service and a brand-impersonation check. A domain containing the platform's or its payment product's name that the platform does not own is the strongest phishing tell. Unknown links are rendered non-clickable or behind a warning page.
3. **Withhold before delivery** when the gate is confident: OLX's 2026 description of blocking suspicious chat images before they reach users is the public example.
4. **Warn in context** when it is not. OLX South Africa described in 2018 how payment keywords and attempts to move a conversation to e-mail or WhatsApp triggered safety tips to the counterparty and flagged the account ([ITWeb, 2018](https://www.itweb.co.za/article/olx-blocks-scammers-using-advanced-algorithms/nWJadvb8APOMbjO1)). The system is long replaced; the warn-in-context pattern is not.
5. **Score the conversation, not only the message.** A sequence of "courier", "safe payment", "deposit" and a link is a pattern no single message shows.
6. **Mask or delay off-platform contact details** for new and unverified accounts, so the scam cannot leave the platform before the platform has had a chance to see it.

![Diagram: The 7 March 2027 phishing message as it would be handled by the target design](listing-systems-architecture/posts/25-fraud-prevention/assets/images/25-fraud-prevention/fig04-7-march-2027-phishing-message-it.jpeg)

**Figure 4:** *The 7 March 2027 phishing message as it would be handled by the target design. The message is scored before delivery; the domain-age and brand check is decisive; the decision service withholds the message, restricts the sender and opens a case for linked accounts.*

Scanning private messages for fraud has a legal side. In the EU it engages the GDPR's purpose-limitation and minimization principles and the ePrivacy framework. The DSA also requires platforms to disclose their use of automated means in moderation. Veldmark documents fraud prevention as the purpose, runs a data protection impact assessment, says in its terms that automated tools scan messages for scams, and keeps scanned content only as long as the case needs it. [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers the legal analysis.

{id: fraud-prevention--feedback-loops-and-labels}
## Feedback Loops and Labels

A fraud model is only as current as its labels, and fraud labels are **late, biased and incomplete**.

| Label source | What it confirms | Delay | Bias |
| --- | --- | --- | --- |
| Reviewer decisions | Fraud or not, for queued items | Minutes to hours | Only covers what the system already flagged |
| User reports | Visible harm | Hours to days | Skews to harms victims notice; many victims never report |
| Victim loss reports | Confirmed loss | Days | Strongly underreported |
| Bank and police reports | Confirmed fraud, often with payment details | Weeks | Sparse; arrives after the model has moved on |
| Chargebacks (where payments run on-platform) | Payment fraud | Weeks to months | Only for on-platform payments |
| Appeal reversals | Confirmed false positives | Days to weeks | Undercounts: most wrongly blocked users do not appeal |
| Random-sample review | Unbiased prevalence and recall | Days | Small samples for rare fraud types |

![Diagram: The fraud feedback loop](listing-systems-architecture/posts/25-fraud-prevention/assets/images/25-fraud-prevention/fig05-fraud-feedback-loop-labels-arrive-several.jpeg)

**Figure 5:** *The fraud feedback loop. Labels arrive from several sources with different delays and biases; the random sample corrects selection bias; new models and rules run in shadow mode before they score live traffic, and rule metrics retire rules that have rotted.*

Four practices keep the loop honest.

- **Correct selection bias with the random sample.** If labels only come from flagged items, the model never learns what it misses. A stratified random sample of live listings and delivered messages, reviewed blind, is the only unbiased source ([Trust and Safety as a Platform](#trust-and-safety-architecture) covers prevalence measurement).
- **Treat late labels as first-class.** A bank report about a transfer three weeks ago must be joined to the listing, the account and the features as they were then. That requires stable identifiers and point-in-time feature logs.
- **Shadow before enforce.** Every new rule and model runs at 0% traffic first and reports what it would have done, as Stripe documents for Radar. The comparison against the current champion is the promotion test.
- **Monitor rules for rot.** Stripe's guidance on rule metrics gives a ready diagnostic: if a rule's blocks rise while confirmed fraud stays flat, the rule may be blocking good users. Every rule needs an owner and an expiry review date.

{id: fraud-prevention--adversarial-adaptation}
### Adversarial adaptation

Fraudsters probe the gate. Which?'s testers changed devices, Wi-Fi networks and identities between attempts, and edited approved ads into scam ads. Professional fraud groups do the same at scale. Three design rules follow:

1. **Re-score on every material edit** (price, payment terms, contact details, photos), not only at creation.
2. **Do not leak thresholds.** A rejection message, or a statement of reasons under the DSA, must give the ground and the relevant facts. It need not reveal which signal tipped the score or by how much.
3. **Rate-limit retries per identity cluster**, not per account. A ring that is rejected and retries from 26 accounts is one actor learning the system.

{id: fraud-prevention--collaboration-with-banks-and-police}
## Collaboration with Banks and Police

A classifieds platform sees the setup; the bank sees the money. Neither can stop APP fraud well alone.

- **Bank-side checks have limits.** Under the EU Instant Payments Regulation, payment service providers in the euro area have had to offer **Verification of Payee**, a check that the payee name matches the account, before a credit transfer since 9 October 2025 ([McCann FitzGerald, 2025](https://www.mccannfitzgerald.com/knowledge/financial-services-regulation/are-you-vop-to-go-prepare-for-verification-of-payee-by-october-2025)). It stops some impersonation, but not a fraudster who uses a money mule's real account in the mule's own name. In Barcelona, the four IBANs belonged to recruited mules, so a name check would have matched.
- **The exchange that matters is identifiers.** Banks can tell a platform which payee accounts received fraud proceeds. Platforms can tell banks which IBANs fraudsters asked victims to pay. Both are fraud signals for the other side. Exchanging them needs a legal basis, a secure channel and agreed formats.
- **Police need evidence packages.** A ring case with linked accounts, listings, messages, payment details and timelines is what an investigation needs. The evidence store from [Trust and Safety as a Platform](#trust-and-safety-architecture) produces it, with a disclosure log.

After Barcelona, Veldmark set up a bank liaison function for Hearthly Spain and Tradeyard, starting with two Spanish and three Dutch banks. It receives reported mule IBANs and adds them, hashed, to the shared block list, so that a message or listing asking for payment to one of them is held before delivery. **Platform-bank exchange is slow to set up and cheap to run.** It is one of the few controls that addresses the money side of a fraud the platform cannot see.

{id: fraud-prevention--back-to-barcelona-what-day-one-action-would-have-required}
## Back to Barcelona: What Day-One Action Would Have Required

Ingrid's question can now be answered component by component.

| What happened | Missing capability | Target design |
| --- | --- | --- |
| Photo matches queued as "possible duplicates" | Policy separating unrelated-seller matches from multi-agency duplicates | Photo match with an unrelated, non-agency seller is a fraud signal sent to risk scoring with seller context |
| Price anomaly in a separate low-priority queue | Score combination | One listing risk score combining photo reuse, price, account age and lister verification |
| 26 accounts looked unrelated | Identity graph | Shared devices and IBANs link new accounts at creation; cluster risk raises every member's score |
| Reviewers judged one listing at a time | Actor-level cases | One case per cluster, with all listings, accounts and evidence |
| First victim report went to support | Intake routing | Victim reports routed as notices to trust and safety, linked to the listing and the account |
| Combined rule took 12 days to exist | Rule platform with shadow mode | Analysts write and shadow-test a rule in hours, then promote it |

With those components, a plausible timeline is that the first five or six listings go live on 1 July, the cluster forms when the third account links through a shared device that evening, and the remaining listings are held at the gate. That would not have prevented every loss, but most of the €71,000 was paid between 5 and 12 July. Hearthly Spain's move to the shared platform was brought forward to the first quarter of 2028.

{id: fraud-prevention--trade-offs}
## Trade-offs

{id: fraud-prevention--build-buy-or-share}
### Build, buy or share

| Option | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- |
| **Per-brand in-house scoring** | Local fit; teams know their fraud | No cross-brand signals; models built several times; small label sets per brand | One brand, or brands with nothing in common |
| **Shared group risk platform** (Veldmark's choice) | Shared graph, block lists and label store; one rule and model lifecycle; larger training sets | Data protection limits on sharing; platform team must support vertical detectors | Several brands under one legal regime with overlapping fraud |
| **Commercial fraud-detection vendor** | Fast start; cross-customer intelligence; mature tooling | Labels and features may not be portable; vendor sees platform data; generic models miss vertical fraud | Early-stage platforms, or for specific signals such as device intelligence |
| **Hybrid**: vendor signals into an in-house platform | Buys hard-to-build signals (device fingerprinting, phishing-domain feeds) while keeping decisions and labels | Integration and contract work; latency of external calls | Most mature marketplaces |

My recommendation for a group is the hybrid: **buy signals, own decisions and labels**. Device intelligence and domain-reputation feeds are expensive to build and benefit from data across many customers. The decision logic, the identity graph and the label store are the platform's memory of its own adversaries, and they should not live in someone else's system.

{id: fraud-prevention--friction-versus-liquidity}
### Friction versus liquidity

Every friction costs liquidity somewhere. A held listing is not searchable; a verification step loses some sellers; a masked phone number slows some genuine contacts. The [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) chapter shows why the first hours of a listing and the speed of first contact matter. The defensible position is **targeted friction with measured costs**: frictions applied by risk tier, each with an experiment that measures abandonment, and thresholds reviewed with the general managers who own the liquidity targets.

{id: fraud-prevention--real-time-versus-batch-detection}
### Real-time versus batch detection

| Choice | Benefit | Cost |
| --- | --- | --- |
| Everything real-time | Earliest possible action | Latency budget limits features; expensive |
| Real-time gate plus asynchronous scoring | Rich features within minutes | A window of exposure for items published on the gate's verdict |
| Batch only | Cheap; full graph analysis | Hours or a day of exposure; organized fraud strikes in that window |

Most platforms need the middle row, with **risk tiers deciding which items wait for the asynchronous result**. In Barcelona, a rental listing from a new, unverified private account should have waited.

{id: fraud-prevention--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs | Recommerce with payments |
| --- | --- | --- | --- | --- | --- |
| Dominant fraud | Payment-link phishing, advance payment, counterfeit | Fake rentals and deposit fraud | Deposit scams, cloned listings, fake escrow | Fake job offers, mule recruitment, data harvesting | Shipping and refund fraud, phishing that imitates the platform's payment product |
| Typical loss per victim | Tens to hundreds of euros | One or two months' rent | Hundreds to thousands of euros | Personal data, sometimes "training fees" | Item value |
| Strongest signal | Domain and link checks, price | Photo reuse, rent anomaly, lister verification | VIN and plate reuse, price vs. market value | Contact details and salary anomaly | Payment and shipping events |
| Natural friction | Message warnings, limits | Lister verification; viewing before payment | Dealer verification; protected deposits | Employer verification | Protected payment by default |
| Where the money moves | Off-platform transfer | Off-platform transfer | Off-platform transfer or fake escrow | Usually no money; data is the target | On-platform, through the payment provider |

The last row explains the strategic link between fraud and transactions. Moving money onto the platform with buyer protection turns unrecoverable APP fraud into a mediated dispute, which is why UK Finance asks for "secure payment protections on online marketplaces". It also creates a new fraud surface: phishing that impersonates the platform's own payment product, which is exactly what Femke received. [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) covers the transactional pivot. The fraud consequence is that **launching protected payments changes the threat model, it does not end it**.

{id: fraud-prevention--failure-modes}
## Failure Modes

1. **Signals without combination.** Photo matches, price flags and account-age checks each raise their own queue item. No component combines them, so each looks minor. Barcelona is the canonical case.
2. **Item-only scoring.** Rings design listings to pass item checks. Without an identity graph and actor-level cases, enforcement removes listings one by one while the ring posts new ones.
3. **Duplicates and fraud in one queue.** Stolen photos are closed as legitimate duplicates because the reviewer sees two listings of the same flat.
4. **Messages delivered, then scanned.** The phishing link reaches the seller before any check runs. Detection after delivery is forensic, not preventive.
5. **Models trained on last year's fraud.** Labels arrive late, retraining is quarterly, and there is no shadow comparison. The model scores the old pattern well and the new one not at all.
6. **Rules without owners.** Hundreds of rules accumulate. Some block good users, some never fire, and nobody can say which.
7. **Blocking instead of friction.** High-risk-but-genuine users are blocked, appeal rates rise, and the team raises thresholds until fraud gets through.
8. **Verified badges that survive takeover.** An aged, verified account is taken over and its badge makes the scam more convincing. Badges must be suspended on a change of session posture.
9. **Thresholds leaked in rejections.** Detailed rejection reasons teach fraudsters exactly which signal to change.
10. **Late labels dropped.** Bank and police reports arrive weeks later as e-mails and are never joined to the listing and account, so the model never learns from the most reliable labels it has.

{id: fraud-prevention--the-chief-architect-s-view}
## The Chief Architect's View

Fraud prevention is where a marketplace group's scale is a genuine advantage, provided the architecture lets it be one. A fraud ring that hits Tradeyard Netherlands will try Tradeyard Belgium next week and possibly Motorvane after that. A shared identity graph, shared block lists and a shared label store let the group learn once. Four separate stacks learn four times, each too slowly.

The decisions I would put on the architecture agenda:

| Decision | Who decides | What to watch |
| --- | --- | --- |
| A single risk scoring service, with a contract for all callers (insertion, message, login, payout) | Chief Architect, Head of Data & ML, Head of T&S | Callers that implement their own scoring |
| Actor-level scoring and the identity graph, with data protection boundaries | Head of T&S and the DPO | Graph-only terminations; cross-brand data flows outside the approved hashed lists |
| Rule lifecycle: backtest, shadow, rollout, owner, expiry | Head of T&S | Time from new scam pattern to rule in production; rules with no owner |
| Friction thresholds and the cost of a lost genuine user | Marketplace GMs with T&S | Abandonment per friction from experiments; fraud stopped per friction |
| Label pipeline, including bank and police reports | Head of Data & ML | Label delay per source; share of fraud cases with a joined late label |
| Buy versus build per signal | Chief Architect and procurement | Label and feature portability in vendor contracts |
| Bank and law-enforcement data exchange | DPO, legal and T&S | Turnaround time; hits on exchanged identifiers |

Three numbers belong on the group dashboard: **sampled prevalence of fraudulent listings by brand**, **time from first fraudulent listing to cluster takedown** for confirmed rings, and **fraud losses reported by victims per million contacts**. The second is the one Barcelona exposed: about twelve and a half days, when the signals were there on day one. Under the target design, the number to aim for is hours.

In the long term, fraud and trust will increasingly be **AI against AI**. Generative tools make fake listings, fake documents and convincing messages cheap, and they make fraud scripts easy to translate into every market's language. The same tools make detectors faster to build and policies faster to change. [AI Across the Listing Lifecycle](#ai-in-listing-systems) covers the broader shift. The architectural defense does not change: a platform that combines signals, scores actors, applies friction in proportion and learns from labels within days will absorb new attack tools. A platform that relies on any single detector, however capable, will not.

{id: fraud-prevention--questions-to-ask}
## Questions to Ask

1. Which actions are scored for fraud risk today (insertion, edit, message, login, recovery, contact reveal, payout), and which are not?
2. Do our photo-reuse matches between unrelated sellers go to fraud scoring with seller context, or to a deduplication queue?
3. Can we link new accounts to known fraud accounts through shared devices, phones, payment accounts or images at the moment of creation?
4. How long does it take from spotting a new scam pattern to having a shadow-tested rule live in every market?
5. Are messages with links, QR codes or payment terms scored before delivery, and is domain age part of the check?
6. How are our friction thresholds set, who owns the cost of a lost genuine user, and when were abandonment rates last measured by experiment?
7. What is the delay from a bank or police report to a joined label in our training data?
8. Which fraud signals do we buy, and do our contracts let us keep the labels and features if we switch vendor?
9. When a verified account shows a change of session posture, does its badge stay visible?
10. For our last confirmed fraud ring, how long did it take from the first fraudulent listing to the takedown of the whole cluster?

{id: fraud-prevention--from-risk-to-identity}
## From Risk to Identity

Fraud prevention keeps coming back to one question: who is on the other side? A risk score is a probability estimated from indirect evidence, and step-up friction is a request for better evidence. The strongest frictions are identity checks: strong authentication, verified phone numbers, verified identities and verified businesses. They are also the most expensive and the most sensitive. [Who Is on the Other Side? Identity and Verification](#identity-and-verification) takes up that question: how much a marketplace should know about its users, how it verifies it, and what a verified badge should and should not promise.

{id: fraud-prevention--sources-and-evidence}
## Sources and Evidence

{id: fraud-prevention--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [We fight online fraud with the power of AI](https://www.olxgroup.com/?p=4590) — OLX Group, 2026. Chat image fraud about 30% of Polish fraud cases; QR-code phishing detection with 80% precision; blocking before delivery.
- [OLX blocks scammers using advanced algorithms](https://www.itweb.co.za/article/olx-blocks-scammers-using-advanced-algorithms/nWJadvb8APOMbjO1) — ITWeb, 2018. Warn-in-context on payment keywords and off-platform moves (OLX South Africa).
- [Fighting fraud: finding duplicates at scale](https://pycon.de/archive/2019/talks/fighting-fraud-finding-duplicates-at-scale/) — Alexey Grigorev, PyCon DE, 2019. OLX duplicate detection: candidate keys, pairwise classifier, hashes and embeddings.
- [Bridging the gap between passwords and passkeys with risk-based authentication](https://engineering.mercari.com/en/blog/entry/20260730-bridging-the-gap-between-passwords-and-passkeys-with-risk-based-authentication/) — Mercari Engineering, 2026. Session and account posture; passkeys and phishing losses.
- [Fighting financial fraud with machine learning at Airbnb](https://www.infoq.com/news/2018/03/financial-fraud-ml-airbnb/) — InfoQ (Srini Penchikala), 2018, summarizing Airbnb's "targeted friction" post by David Press. Friction instead of blocks; loss-based thresholds; A/B testing frictions.
- [Meet Michelangelo: Uber's machine learning platform](https://www.uber.com/blog/michelangelo-machine-learning-platform/) — Uber Engineering, 2017. Shared feature store with consistent training and serving features.
- [Fighting spam with Haskell](https://engineering.fb.com/2015/06/26/security/fighting-spam-with-haskell/) — Engineering at Meta, 2015. Rules as code, deployed continuously.
- [Cracking down on organized crime behind scam centers](https://about.fb.com/news/2024/11/cracking-down-organized-crime-scam-centers/) — Meta, 2024. Scale of organized scam operations.
- [Fraud prevention rules (Radar)](https://docs.stripe.com/radar/rules) — Stripe, n.d. (current documentation). Backtesting, shadow mode, rollout, audit trail, rule metrics.

{id: fraud-prevention--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [PDQ perceptual hash](https://github.com/facebook/ThreatExchange/tree/main/pdq) — Meta ThreatExchange, n.d. Match thresholds, quality score, invariance limits.
- [Are you VoP to go? Prepare for Verification of Payee by October 2025](https://www.mccannfitzgerald.com/knowledge/financial-services-regulation/are-you-vop-to-go-prepare-for-verification-of-payee-by-october-2025) — McCann FitzGerald, 2025. Verification of Payee obligation for euro-area payment service providers from 9 October 2025.
- [Fraudulent advertising and account integrity: expert insights on best practice](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf) — Integrity Institute for Ofcom, 2026. Signals, friction between account creation and reach, enforcement ladder.

{id: fraud-prevention--research-and-practitioner-sources}
### Research and practitioner sources

- [Annual Fraud Report 2026](https://www.ukfinance.org.uk/system/files/2026-06/UK%20Finance%20Fraud%20Report%202026.pdf) — UK Finance, 2026. Purchase-scam cases, losses, share of APP fraud, reimbursement, policy asks.
- [Scam ads slipping through the net too easily on second-hand marketplaces](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1) — Which?, 2024. Undercover test: edited scam ads passing review; evasion by changing devices and identities.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
