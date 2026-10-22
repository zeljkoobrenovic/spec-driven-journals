{id: reviews-and-reputation}
# 34. Trustworthy Reviews: Collection, Integrity and Quality Operations

![Trustworthy Reviews: Collection, Integrity and Quality Operations — logo](stays-marketplace-architecture/posts/34-reviews-and-reputation/assets/images/34-reviews-and-reputation/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Follow a review from the stay that earns it to the score a guest reads: eligibility, invitation, one-way and double-blind collection, integrity checks, publication, aggregation, replies and disputes, and the quality programs and remediation workflows built on top. You will see why consumer law in the EU, the UK and the US now writes part of the specification.

> **WHY THE BUSINESS CARES:** Reviews are the evidence a guest uses to trust a property or a stranger's home, and they are the main quality signal in ranking and in host and partner programs. Fake reviews cost conversion, damage claims and regulatory penalties; unfair moderation costs partner trust. A marketplace GM needs a review score that guests believe and partners do not contest.

> **WHY ARCHITECTS SHOULD CARE:** A review system looks like a simple content feature until it is attacked. Its integrity depends on the reservation system of record, the payments and identity graph, the trust platform's enforcement, and ranking's appetite for its signals. Where those dependencies are implicit, the review store becomes the easiest way to buy visibility on the platform.

> **KEY POINTS:**
>
> * **A review is a fact about a stay, not a piece of content.** Eligibility must come from the reservation's lifecycle (stayed, not canceled before check-in, not a no-show) and be recorded with the review. A review the system cannot tie to a stay is not a "verified" review, and EU, UK and US consumer law now say so explicitly.
> * **Integrity is a pipeline with a time budget, not a moderation queue.** Screen, score and hold reviews before publication, and look for patterns across accounts, payments and devices, not only in text. The double-blind window of two-way reviews gives hosted-stays marketplaces that time for free.
> * **Every consumer of review data reads one published stream.** Scores on the page, ranking features, host and partner credentials and partner analytics should all derive from the same event history of published and removed reviews. When a review is removed, every derived number must change, and the platform must be able to show why.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Trust After the Incident** — review integrity at Nookaway was a text filter and a report button until a review-trading ring showed that cheap fake stays could buy ratings, quality badges and guest reputations.
> * **The Hotel-Shaped Home** — a one-way, hotel-style review model applied to homes loses the host's view of the guest; a two-way model applied to hotels invents a guest rating nobody uses.
> * **The Unwatched Model** — a fake-review classifier and a quality program's thresholds decide which reviews are shown and which hosts are badged, with nobody measuring what they miss or whom they wrongly punish.

A guest who books a night has never seen the room, and a guest who books a stranger's apartment has never met the host. **Reviews are the second-hand evidence that fills that gap.** They tell the next guest what the photos do not, they tell the host or property what to fix, and they feed the ranking, the badges and the partner programs that decide who gets seen.

That makes reviews valuable enough to fake. A hotel can book itself and praise the result. A competitor can book and complain. A ring of hosts can stay at each other's homes for one night and trade five-star ratings in both directions. A property can quietly mark an unhappy guest as a no-show so the guest is never invited to review. Each of these attacks goes through a different system: reservations, payments, identity, messaging. The **review system's integrity is only as good as its links to those systems.**

Part VII ([Part VII — TRUST: Making Strangers Safe to Stay With](#part-7)) treats trust as a platform. [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) owns the policy, detection, enforcement and appeals machinery; [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) owns account takeover and payment fraud; [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) owns who the guest and host are. This chapter owns three terms: the **verified review** (a review tied to a completed stay by the reservation record), the **double-blind review** (a two-way review in which neither side sees the other's review until both have submitted or the window closes), and the **quality program** (a credential, badge or remediation track computed from reviews and operational records). It does not re-teach the review fragment on the property page ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)), the review-invitation trigger in the trip timeline ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)) or how quality features enter the ranker ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)); it shows what those consumers can rely on.

{id: reviews-and-reputation--setting-the-scene-at-corvane-the-ring-behind-the-4-97}
## Setting the Scene at Corvane: The Ring Behind the 4.97

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs **Roomstead**, an accommodation marketplace with 640,000 bookable properties, and **Nookaway**, a hosted-stays marketplace with 1.15 million listings. In 2026 the two brands ran two review systems that had never been compared.

- **Roomstead** kept reviews in a module of **Keystone**, its Java monolith. A guest could review a property once the departure date had passed, if the reservation was not canceled and the property had not marked it as a no-show. Reviews were one-way, scored 1–10 with five subscores, and moderated by a profanity filter, a text classifier and a small team in Dublin. Roomstead collected about **10.8 million** reviews in 2026, from about 36% of its 30 million stayed reservations.
- **Nookaway** kept reviews in **Burrow**, its Django monolith. Guests and hosts reviewed each other within **10 days** of checkout, and neither review was shown until both were in or the window closed. Guests gave an overall rating of 1–5 stars and five category ratings. Nookaway collected about **3.7 million** guest reviews of listings and **4.9 million** host reviews of guests in 2026. Its host credential, **Hearth**, was recomputed every quarter: at least **8** completed stays in the previous 12 months, an average rating of at least **4.75**, a host cancellation rate under 1.5% and quality-related support cases on fewer than 2% of stays.

On **22 March 2027** a guest from Hamburg wrote to Nookaway support from an apartment in Lisbon's Graça district. The flat was dirty, the second bedroom in the photos did not exist, and the host had stopped answering messages. The listing had a rating of **4.97** from 54 reviews, all written in the previous six months. The support agent rehoused the guest under the guest guarantee and, unusually, escalated the case to Sofia Marín, Director of Trust and Safety, with one sentence: "Fifty-four people cannot have loved this flat."

Sofia's team, with analysts from Kenji Arai's data platform, spent three weeks pulling the thread. What they found was a **review-trading ring**:

- **118** host accounts, controlling **264** listings in Lisbon, Porto, the Algarve and Málaga, coordinated through a paid group on a messaging app that sold "review packages".
- Between September 2026 and March 2027, ring members made **1,940** reservations at each other's listings, mostly for one night, at an average subtotal of **€46**, far below the listings' usual prices. Several cards and payout accounts were shared across accounts.
- Those stays produced **3,610** reviews: 1,820 guest reviews of ring listings and 1,790 host reviews of ring guests. Ring listings averaged **4.94**; comparable listings in the same neighborhoods averaged **4.72**.
- **41** of the 118 hosts had reached Hearth status, which gave them a badge and a quality feature in Nookaway's ranker. Eight one-night stays and eight five-star reviews were all it took.
- **29** guest accounts had only ring reviews in their history. **11** of them had booked homes outside the ring, and Nookaway's reservation screening had scored them as low-risk partly because of their spotless guest reputation.
- The ring paid Nookaway about **€14,300** in guest and host fees for the privilege (1,940 × €46 × 16%).

![A circle of houses trading gold stars in both directions, with a 4.97 rating badge in the middle.](stays-marketplace-architecture/posts/34-reviews-and-reputation/assets/images/34-reviews-and-reputation/34-ring-trade.jpeg)

**Figure 1:** *The ring behind the 4.97: 118 host accounts booked 1,940 cheap one-night stays at each other's homes and traded 3,610 reviews in both directions.*

Every one of these reviews was "verified" by the rule Burrow applied: a confirmed reservation, not canceled, with a checkout date in the past. Mariana Costa, the Group Chief Architect, put the question to the architecture forum in April: **what does "verified" mean, who decides, and what else reads a review once it is published?** The answer is the subject of this chapter, and the Corvane remedy appears in "In Practice at Corvane" below.

{id: reviews-and-reputation--what-a-review-is-and-what-makes-it-trustworthy}
## What a Review Is, and What Makes It Trustworthy

Five terms carry the chapter.

| Term | Definition | Why it matters architecturally |
| --- | --- | --- |
| **Review** | A rating and optional text written by one party to a stay about the other party or the accommodation, linked to one reservation | The link to the reservation is the review's provenance; without it the review is unattributed content |
| **Verified review** | A review whose author is a party to a reservation that the reservation record shows as stayed (or arrived), checked against stated eligibility rules | Consumer law in the EU and the UK makes claims of verification a legal statement |
| **Double-blind review** (also *simultaneous reveal*) | A two-way review in which each side's review is hidden until both have submitted or the review window closes | Removes retaliation and reciprocity; creates a publication delay |
| **Reputation** | The aggregate of reviews and operational records (cancellations, responsiveness, support cases) about a property, listing, host or guest | Read by search, ranking, screening and programs, each with its own window and rules |
| **Quality program** | A computed credential (badge, tier) or remediation track derived from reputation, with thresholds, a period and consequences | Turns review data into visibility and money, which creates the incentive to fake it |

{id: reviews-and-reputation--eligibility-a-review-is-a-fact-about-a-stay}
### Eligibility: a review is a fact about a stay

The most important design decision in a review system is **who may review what, and when**. Open review sites let anyone post; booking platforms restrict reviews to people who booked. That restriction is the main defense against fake reviews, and the research record supports it. In a 2014 study in the *American Economic Review*, Mayzlin, Dover and Chevalier compared hotel reviews on Expedia, where only customers could post, with TripAdvisor, where anyone could. Hotels with a strong incentive to fake (independent hotels with single-unit owners) had more positive reviews on the open site relative to the booking site, and their neighbors had more negative ones ([Mayzlin, Dover and Chevalier, 2014](https://doi.org/10.1257/aer.104.8.2421)).

Booking gates raise the cost of a fake review; they do not make it impossible, and the documented rules show how much detail a gate needs. **Booking.com** (fetched October 2026) lets guests review a property booked through the platform "if you stayed there, or if you arrived at the Accommodation but didn't actually stay there", within three months of checkout ([Booking.com, How we work](https://www.booking.com/content/how_we_work.html)). **Airbnb** (fetched October 2026) prompts guests and hosts on the day of checkout, gives them 14 days, excludes reservations canceled before check-in but allows some canceled on or after the check-in day ([Airbnb Help Center, article 13](https://www.airbnb.com/help/article/13)), and treats a review from a guest who "never arrived" as irrelevant ([article 2673](https://www.airbnb.com/help/article/2673)).

Each of those rules needs a fact from another system, and the facts are not equally reliable.

| Eligibility fact | Owner | Reliability on an OTA (agency model) | Reliability on a hosted-stays marketplace |
| --- | --- | --- | --- |
| Reservation exists and is not canceled | Reservation service ([The Life of a Reservation: State Machines, Delivery and Operations](#reservation-lifecycle)) | High | High |
| Guest arrived | Property's PMS (property-management system) or extranet; guest messages | Low: the property reports no-shows, and a no-show often waives commission | Medium: check-in messages, smart-lock events, host confirmation |
| Stay completed | Departure date; property status | Assumed from dates unless the property reports otherwise | Assumed from dates; disputes and early departures recorded in support |
| Author is the guest who stayed | Identity and the reservation's guest list | Medium: the booker is not always the guest | High for the booker; co-travelers usually not individually known |
| Author is not affiliated with the property or host | Identity, payments and device graph | Requires cross-checks against extranet users | Requires cross-checks against host accounts, co-hosts and payout accounts |

The weak row on the OTA side matters. Under the agency model, where the guest pays at the property and the marketplace invoices commission ([Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models)), the platform learns that a guest stayed mainly because the property did not report otherwise. A property that marks a reservation as a no-show both avoids commission and prevents the review. **Any eligibility rule that depends on a party's self-report gives that party a veto over its own reviews**, and the design must assume the veto will sometimes be abused.

{id: reviews-and-reputation--one-way-and-two-way}
### One-way and two-way

OTAs collect **one-way** reviews: guests review properties. Hotels have front desks, identity checks at arrival and the legal standing to refuse a guest; a rating of the guest adds little. Hosted-stays marketplaces collect **two-way** reviews: the guest reviews the listing and the host reviews the guest. The host review is the main public evidence of how a guest behaves in someone's home, and it feeds risk systems. In a 2022 announcement, Airbnb listed a guest's "history of positive reviews (or lack of positive reviews)" among the signals of its anti-party technology in the US and Canada ([Airbnb, 2022](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada)). Airbnb's December 2022 anti-discrimination update also treated giving more guests reviews as a fairness measure ([Airbnb, 2022](https://news.airbnb.com/sixyearadupdate)). A guest's review history is therefore both a trust credential and an access credential, which is why the Corvane ring bothered to fake it.

Two-way reviews create a strategic problem: each side may soften its review for fear of retaliation, or trade a good review for a good review. The fix is the **double-blind window**, and it is one of the few review-design choices with published experimental evidence. Fradkin, Grewal and Holtz analyzed a large experiment on Airbnb in which feedback was hidden until both parties had submitted (treatment) or revealed immediately (control). The simultaneous reveal "stimulated more reviewing in total", "reduced retaliation and reciprocation in feedback and led to lower ratings as a result" ([Fradkin, Grewal and Holtz, *Marketing Science*, 2021](https://doi.org/10.1287/mksc.2021.1311)). Airbnb's help center describes the current rule: reviews are posted after both parties submit or once the 14-day period ends, whichever comes first ([Airbnb Help Center, article 13](https://www.airbnb.com/help/article/13)).

{id: reviews-and-reputation--scales-dimensions-and-inflation}
### Scales, dimensions and inflation

A rating scale is a product decision with data consequences. Booking.com scores 1–10 and collects subscores (location, cleanliness, staff and others) that guests submit independently of the overall score ([Booking.com, How we work](https://www.booking.com/content/how_we_work.html)). Airbnb uses a 1–5 overall rating plus six categories, from cleanliness and accuracy to value ([Airbnb Help Center, article 1257](https://www.airbnb.com/help/article/1257)).

On two-way platforms ratings cluster at the top. The title of Zervas, Proserpio and Byers's 2020 study, "A first look at online reputation on Airbnb, where every stay is above average", states the finding ([*Marketing Letters*, 2020](https://doi.org/10.1007/s11002-020-09546-4)). When most listings sit near the top of the scale, the average no longer separates good from excellent, and a threshold such as Hearth's 4.75 becomes a knife-edge that a handful of fake reviews can push a listing across. Category ratings, text, recency and operational signals (cancellations, support cases) then carry more information than the headline average.

![Listing dots crowded at the top of a rating scale, with a thin threshold line at 4.75 and a few fake stars pushing one listing across it.](stays-marketplace-architecture/posts/34-reviews-and-reputation/assets/images/34-reviews-and-reputation/34-knife-edge.jpeg)

**Figure 2:** *When most ratings crowd the top of the scale, a threshold such as Hearth's 4.75 becomes a knife-edge that a handful of fake reviews can push a listing across.*

{id: reviews-and-reputation--the-law-now-writes-part-of-the-specification}
## The Law Now Writes Part of the Specification

Between 2022 and 2025 the EU, the UK and the US turned fake reviews from a reputational problem into a legal one. The duties are similar enough to design for once.

| Jurisdiction and instrument | Applies from | What it requires | What it means for the system |
| --- | --- | --- | --- |
| **EU — Omnibus Directive** (EU) 2019/2161, amending the Unfair Commercial Practices Directive (UCPD) | 28 May 2022 | Information on "whether and how" a trader ensures reviews come from consumers who used the product is **material information** (UCPD Art. 7(6)); banned: claiming reviews are from real users without "reasonable and proportionate steps", and submitting, commissioning or misrepresenting fake reviews (Annex I points 23b, 23c) | A verification statement on every page that shows reviews, generated from the actual eligibility and moderation rules; evidence that the steps were taken |
| **EU — Digital Services Act** (EU) 2022/2065 | 17 February 2024 | Notice and action for illegal content (Art. 16); a statement of reasons for every restriction of content or accounts (Art. 17); an internal complaint system (Art. 20) | Review removal and account restriction are enforcement actions with reasons, notifications and appeals |
| **UK — Digital Markets, Competition and Consumers Act 2024**, Schedule 20 para. 13; CMA guidance CMA208 | 6 April 2025 | Banned: fake reviews, concealed incentivized reviews, misleading publication (including suppressing negative reviews), and publishing without "such reasonable and proportionate steps as are necessary" to prevent and remove them | Suppression is an offense too: selective invitations and no-show abuse are in scope; the steps must be documented |
| **US — FTC Trade Regulation Rule on Consumer Reviews and Testimonials**, 16 CFR Part 465 | 21 October 2024 | Banned: fake (including AI-generated) reviews, sentiment-conditioned incentives, undisclosed insider reviews, review suppression; civil penalties for knowing violations | Insider and affiliation checks; no incentives conditioned on positive sentiment |

Sources: [Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161), [Regulation (EU) 2022/2065](http://publications.europa.eu/resource/celex/32022R2065), [DMCC Act 2024, Schedule 20](https://www.legislation.gov.uk/ukpga/2024/13/schedule/20), [CMA208 (CMA, 2025)](https://www.gov.uk/government/publications/fake-reviews-cma208), [FTC final rule announcement (2024)](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) and the [Federal Register publication of 22 August 2024](https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials).

Three engineering consequences follow, and they are the same in all three jurisdictions.

1. **The verification statement is generated, not written.** If the page says "only guests who stayed can review", that must be true of every published review, including the ones imported from an acquired brand or a partner. The statement should be rendered from the eligibility policy's current version, as [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) recommends for the ranking description.
2. **"Reasonable and proportionate steps" is an evidence question.** When a regulator asks, the platform must show what it checked, what it caught and what it did, which takes metrics and an audit trail.
3. **Suppression is as illegal as fabrication.** Genuine negative reviews that are never invited, never published or removed on a partner's complaint are a violation too, so the dispute workflow and the no-show path are in scope.

{id: reviews-and-reputation--architecture-from-stay-record-to-published-score}
## Architecture: From Stay Record to Published Score

The review system has three jobs that are often built as one: **collect** reviews from eligible parties, **decide** what to publish, and **distribute** published reviews to everything that reads them. Separating them lets the system both defend and explain itself.

![Reservation lifecycle feeds eligibility, which invites into a blind vault; submitted reviews pass an integrity pipeline that also reads trust signals; published or removed reviews go to one review event log, from which all consumers read.](stays-marketplace-architecture/posts/34-reviews-and-reputation/assets/images/34-reviews-and-reputation/34-review-pipeline.jpeg)

**Figure 3:** *Collection, decision and distribution are separate stages: eligibility comes from the reservation lifecycle, integrity decides before publication, and every consumer derives its numbers from one event log of published and removed reviews.*

The components and their contracts:

| Component | Responsibility | Contract with its neighbors |
| --- | --- | --- |
| **Eligibility and invitation** | Decide who may review which reservation, when the window opens and closes, and send invitations | Consumes reservation state events; never invites from a reservation that is canceled before check-in; records the eligibility policy version on each invitation |
| **Submission and blind vault** | Accept ratings and text; for two-way reviews, hold both sides until both submit or the window closes | Idempotent per reservation, author and direction; edits allowed only before reveal |
| **Integrity pipeline** | Screen text, score fraud and affiliation risk, hold for human review, decide publish, publish with limits, or reject | Reads trust signals through the trust platform's risk signal feed ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)); writes a decision with reason codes |
| **Review event log** | Append-only record of published, edited, hidden, reinstated and removed reviews, with reasons | The only source for every derived number; retained for audit |
| **Aggregates and read model** | Compute scores, subscores, counts, recency windows and the review list for pages | Recomputed when any review is removed; shows the policy version used |
| **Replies and disputes** | Partner or host replies; dispute intake and decisions; guest appeals | Disputes produce events in the same log; decisions carry statements of reasons |
| **Quality programs** | Periodic credentials and remediation tracks from reviews plus operational records | Read from snapshots of the log and other systems, with the snapshot rule stated |

{id: reviews-and-reputation--the-review-record}
### The review record

The record has to carry its own evidence, because the review store will be asked questions long after the reservation has been archived.

| Field group | Contents | Why |
| --- | --- | --- |
| **Identity** | Review ID, reservation ID, direction (guest→listing, host→guest), author account, subject (property, listing, host or guest) | One review per reservation, author and direction |
| **Eligibility evidence** | Reservation state at invitation, arrival evidence, stay dates, eligibility policy version | Proves "verified" for this review, under the rules then in force |
| **Content** | Overall rating, category ratings, text, language, photos, private note to the host or property | Category ratings and private notes may have different visibility |
| **Integrity decision** | Scores, rule hits, reviewer, decision, reason code, decision time | The "reasonable and proportionate steps" evidence |
| **Lifecycle** | Submitted, revealed, published, edited, hidden, removed; each with time and reason | Lets aggregates be rebuilt as of any date |

Expedia Group described in 2023 an event-sourced design for its reviews: moderated reviews are written to a Kafka topic that "acts as the source of truth for all moderated reviews", and independent consumers build aggregation, an in-memory cache behind the APIs, an Elasticsearch index and sentiment analysis ([Expedia Group Technology, 2023](https://medium.com/expedia-group-tech/how-expedia-reviews-engineering-is-using-event-streams-as-a-source-of-truth-d3df616cccd8)). The post is three years old and the current state is not public, but the pattern is the one I recommend: **an append-only log of moderation outcomes, with every read model derived from it**. It makes removals propagate, and it lets the platform answer "what did this property's score look like on 3 March, and which reviews were in it?"

{id: reviews-and-reputation--the-life-of-one-review}
### The life of one review

![Review states: Invited leads to Expired or Sealed, then Screening, which publishes or holds; held reviews can be cleared to Published; Published can be Removed after a dispute and reinstated on appeal.](stays-marketplace-architecture/posts/34-reviews-and-reputation/assets/images/34-reviews-and-reputation/34-review-states.jpeg)

**Figure 4:** *A review is a small state machine. The sealed state of two-way reviews is where integrity checks can run without delaying anything a guest would notice, and removal is never terminal while an appeal is open.*

Two properties of this state machine are worth defending in a design review. First, **screening happens after reveal in two-way reviews but can start at submission**: the integrity pipeline can score a sealed review immediately and decide by the time the window closes. A ten- or fourteen-day blind window is a moderation budget that one-way systems do not have; Roomstead, which publishes one-way reviews, must either hold suspicious reviews visibly or publish and remove later. Second, **"Removed" is reversible**: under the DSA, a removal is a restriction with a statement of reasons and an internal complaint path, and the state machine has to allow reinstatement without losing the history.

{id: reviews-and-reputation--integrity-finding-fake-traded-and-suppressed-reviews}
## Integrity: Finding Fake, Traded and Suppressed Reviews

Review abuse in stays falls into a small number of patterns, and each is visible in a different system. The table is the typology I use with trust teams.

| Pattern | How it works | Hits hardest | Where the evidence lives |
| --- | --- | --- | --- |
| **Self-booking** | Property or host books its own unit through a friend, staff member or second account and reviews it | OTA (commission is the only cost) | Booker identity vs extranet users, devices, payment cards, email domains |
| **Review trading ring** | Hosts book each other's homes for short, cheap stays and exchange top ratings in both directions | Hosted stays | Reciprocal reservation graph, shared cards and payout accounts, price far below normal, no stay messages |
| **Competitor attack** | A competitor books and posts a negative review | Both, rarer behind a booking gate | Affiliation between the author and nearby properties or hosts |
| **Incentivized or pressured review** | Discount, refund or gift in return for a positive review, or a threat of a negative review to extract compensation | Both | Messages (offers of refunds for reviews), support cases, review timing after refunds |
| **Suppression** | Property marks unhappy guests as no-shows, or pressures them to withdraw; host disputes every negative review | OTA (no-shows); hosted stays (dispute volume) | No-show marks on reservations with in-stay messages or arrival evidence; dispute rates per partner |
| **Irrelevant or abusive content** | Reviews about something else, personal data, hate speech | Both | Text classifiers, reports |
| **Generated text** | AI-written reviews from real or fake accounts | Both | Text similarity across accounts, writing-time patterns; weak alone |

Three lessons come out of this table.

**Text is the weakest signal.** Classifiers catch profanity, personal data and copy-paste, but a fluent fake is indistinguishable from a genuine review on its words alone, and generated text makes fluent fakes cheap. The strong signals are **relational**: who booked whom, with which card, from which device, at what price, after which messages. Booking.com says only that it has "people and automated systems that specialise in detecting fake reviews" ([Booking.com, How we work](https://www.booking.com/content/how_we_work.html)); its methods are not public, and I do not infer them.

**Graph features beat review features for rings.** A ring is a dense, reciprocal subgraph in the bipartite graph of guest accounts and listings, enriched with shared payment instruments, payout accounts and devices. Reciprocity (A stays with B and B stays with A within weeks), short stays at prices far below the listing's normal level, missing pre-arrival messages and reviews written within minutes of checkout are each weak, but together they separate the ring from normal behavior well. These are features the trust platform's risk signal feed already computes for fraud ([Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud)); the review pipeline should consume them, not rebuild them.

**Suppression needs its own detector.** Fake-review defenses look for reviews that should not exist. Suppression is about reviews that should exist and do not. The detector compares, per property, the no-show rate and its correlation with complaint signals (in-stay messages, support contacts during the stay, payment at the property), and the dispute rate and dispute success rate against the market. It is a monitoring job on reservation and dispute data, not a classifier on reviews.

![Accounts, cards and devices, and stay messages feed a reservation graph; ring features from the graph drive an integrity decision that writes to the review event log and triggers account enforcement.](stays-marketplace-architecture/posts/34-reviews-and-reputation/assets/images/34-reviews-and-reputation/34-ring-detection.jpeg)

**Figure 5:** *Rings are found in the relationships between accounts, money and stays, not in the text of their reviews; the same decision feeds review removal and account enforcement.*

The integrity pipeline should be **tiered by cost**. Cheap rules and text checks run on every review. Risk scoring runs on every review with relational features from the trust platform. Human review handles the held fraction. Periodic graph sweeps run over the whole review history, because rings are usually visible only after weeks of activity and some reviews will have been published before the ring is found. The pipeline's own metrics are the "reasonable and proportionate steps" evidence: hold rate, removal rate before and after publication, appeal rate and appeal reversal rate, and the time from a ring's first review to its detection.

{id: reviews-and-reputation--aggregation-and-display}
## Aggregation and Display

A review score is a statistic with a definition, and the definition is a policy decision with a version. The documented platforms make different choices.

| Choice | Booking.com (documented) | Airbnb (documented) | Design consideration |
| --- | --- | --- | --- |
| Score formula | Weighted: "the more recent the review, the bigger the impact" | Plain average of all overall ratings | Recency weighting rewards improvement and punishes decline faster |
| Display window | May stop showing reviews older than 36 months or after a change of ownership | Reviews stay unless removed under policy or by the author within 30 days | An ownership change is a reason to reset reputation for hotels; rarely tracked for homes |
| Minimum count | Not stated | Rating shown after 3 reviews | Small samples need a threshold or statistical shrinkage |
| Ordering | Most recent first, adjusted for language and whether text is present | "Most relevant to you" by default, considering language and country | Ordering is ranking, with the same position effects |
| Translation | Reviews may contain Google translations, labeled | Automatic translation extended from listings and messages to reviews in September 2022 | Label machine translation; keep the original |

Sources: [Booking.com, How we work](https://www.booking.com/content/how_we_work.html) (fetched October 2026); [Airbnb Help Center, articles 13 and 1257](https://www.airbnb.com/help/article/13) (fetched October 2026); [Airbnb via Hospitality Net, 2022](https://www.hospitalitynet.org/news/4112343.html) for review translation.

Three rules for the aggregation layer:

- **Shrink small samples toward a prior.** A new listing with two five-star reviews is not better than an established one at 4.8 from 300. Showing the raw average after a minimum count (Airbnb's choice) is honest; ranking on it is not. For ranking and program thresholds, use a Bayesian average or a lower confidence bound, and keep the displayed figure and the ranking feature as separate, documented definitions.
- **Recompute on removal.** A removed review must leave every aggregate it entered: the page score, the subscores, the ranking feature, the badge eligibility, and the partner's benchmark. If aggregates are maintained incrementally, removals are the case that breaks them. Rebuilding from the event log is slower but correct; I would accept the cost.
- **Treat generated summaries as claims by the platform.** Booking.com announced review summaries in testing in October 2024 ([Booking Holdings, 2024](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/)); Airbnb shows generated review highlights on some listings ([Airbnb Help Center, article 13](https://www.airbnb.com/help/article/13)) and in a July 2026 engineering post described evaluation infrastructure behind features including review highlights ([Airbnb Tech, 2026](https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/)); Agoda listed AI review summaries among the features of its renamed Agoda Partner Portal in August 2026 ([Agoda via Kyodo News PR Wire, 2026](https://kyodonewsprwire.jp/release/202608174214)). A summary must be generated only from published reviews, regenerated when a review is removed, and labeled as generated. A summary that still quotes a removed fake review is the platform repeating the fake.

{id: reviews-and-reputation--replies-disputes-and-removal}
## Replies, Disputes and Removal

Partners and hosts need a **public reply** and a **dispute**. Replies are simple: both Booking.com and Airbnb let the reviewed party respond publicly, and partner APIs expose reviews for reading and replying (Expedia Group's 2025 lodging supply documentation lists a Reviews API, [Expedia Group Developer Hub](https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction)). Disputes are where fairness is decided.

A dispute workflow needs a written policy that says what qualifies. Airbnb's published reviews policy is a useful model of the shape: it names categories that can be removed (irrelevant, fake, involving incentives, extortion or pressure, harming competition, retaliatory, or breaching the content policy) and states that disagreement with a star rating alone does not qualify, noting that the policy "is informed by consumer laws that apply to online reviews" ([Airbnb Help Center, article 2673](https://www.airbnb.com/help/article/2673)). Whatever the categories, the architecture is the same:

- **Disputes are cases with reason codes**, decided by people outside the commercial relationship with the partner. An account manager who earns commission from a hotel should not decide whether its negative reviews stay.
- **Every decision is an event in the review log**, with the policy clause, the evidence and a statement of reasons to both the author and the reviewed party. Under the DSA, removing a review restricts the author's content; the author is owed reasons and an appeal.
- **Dispute rates are monitored per partner.** A property that disputes every negative review, and wins often, is either unusually wronged or exploiting a lenient process. Either way someone should look.
- **Extortion is a reason to remove the review and act on the account**, not to compensate. Refunds and the review log should be joinable, so that a refund paid just before a negative review was withdrawn can be found.

{id: reviews-and-reputation--quality-programs-and-remediation}
## Quality Programs and Remediation

Reviews become money through quality programs. Two families exist, and they run on different clocks.

**Credentials** are periodic and positive: a badge that improves visibility and conversion. Airbnb's Superhost is assessed every three months over the trailing 12 months, with thresholds of at least 10 stays (or 3 stays totaling at least 100 nights), a 90% response rate, a cancellation rate under 1% and an overall rating of at least 4.8; ratings published after a period ends count toward the next ([Airbnb Help Center, article 829](https://www.airbnb.com/help/article/829), live page, 2026). In November 2023 Airbnb launched **Guest Favorites**, about 2 million homes selected from ratings, reviews and reliability data, with an average rating above 4.9, high category ratings, and host cancellations plus quality-related customer-service issues below 1% on average ([Airbnb, 2023](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/)). Its current eligibility requires at least 5 reviews in the last 4 years and one in the last 2 years ([Airbnb Help Center, article 13](https://www.airbnb.com/help/article/13)).

**Remediation** is continuous and negative: a track that warns, restricts and eventually removes supply that keeps failing guests. Airbnb's Q3 2025 shareholder letter says that under the hosting quality system launched in 2023 it had removed "over 550,000 listings" ([Airbnb, 2025](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf)). On the OTA side, partner programs mix quality with commercial terms: Booking.com's partner pages say guest review scores matter for joining and keeping its Preferred program, whose members pay a higher commission ([Booking.com Partner Hub](https://partner.booking.com/en-gb/solutions/preferred-partner-programme), n.d.) ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty) and [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) discuss the commercial side). At EXPLORE 2024, Expedia announced partner-facing insights that flag recurring negative review sentiment with recommendations ([Expedia Group, 2024](https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx)), which is remediation by information rather than sanction.

Four architecture points follow from the documented programs.

1. **Credentials are batch, signals are streaming.** A badge recomputed quarterly over a stated snapshot gives hosts stability and gives the platform a reproducible computation. Airbnb's rule that late ratings count toward the next period shows the snapshot is keyed on publication time. Write the snapshot rule down; it decides disputes about why a badge was lost.
2. **Programs fuse reviews with support and messaging data.** Guest Favorites uses quality-related customer-service issues; Superhost uses response rate. That makes the support system's contact-reason taxonomy ([When Something Goes Wrong: Customer Service and Recovery](#customer-service)) and message timestamps ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)) **inputs to a public credential**. Changes to those taxonomies are data migrations with ranking consequences.
3. **Thresholds based on counts are cheap to game.** A credential that requires eight stays and a high average can be bought with eight cheap stays. Thresholds that count **distinct, unaffiliated guests**, weight stays by money at risk, or require that some reviews come from guests with independent histories are harder to fake. This is the lesson of the Corvane ring.
4. **Remediation is enforcement and needs due process.** A remediation track that suspends instant book or delists a home is a restriction under the DSA and, for business users, under the P2B Regulation's rules on restriction and suspension (Art. 4 of [Regulation (EU) 2019/1150](http://publications.europa.eu/resource/celex/32019R1150)). It runs on the trust platform's enforcement machinery ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)), with notices, reasons and appeals, not as a nightly job that flips a flag.

{id: reviews-and-reputation--in-practice-at-corvane-taking-the-ring-apart}
## In Practice at Corvane: Taking the Ring Apart

Sofia Marín's team acted on the ring in **April 2027**. Its enforcement used the trust platform's existing account tools; the review side had to be done by hand.

| Action | Count | Notes |
| --- | --- | --- |
| Ring reviews removed | **3,610** | Every review written on a ring reservation, in both directions |
| Host accounts removed from Nookaway | **64** | Organizers and accounts with shared payout instruments |
| Host accounts restricted | **54** | Listings suspended for 90 days; Hearth revoked |
| Hearth credentials revoked | **41** | Recomputed early, outside the quarterly cycle |
| Guest accounts removed | **29** | Accounts whose entire review history came from the ring |
| Appeals | **14** | **3** reinstated: a former co-host had made the bookings without the owners' knowledge |
| Future reservations at ring listings offered free cancellation | **1,130** | **380** guests canceled |

Removing the reviews was harder than it should have been. Burrow's listing rating was an incrementally maintained column; deleting 3,610 reviews required a one-off script to recompute ratings, and for nine days the ranker's quality feature, refreshed from a nightly export, still used the inflated averages. The screening model's guest-history feature was not refreshed until a model retrain in May. Every statement of reasons was written from a template by an analyst. None of this was a bug in a single system; there was no single system.

The architecture forum adopted **Review Integrity v1** on **18 May 2027**, with Mariana's recommendation and Sofia as business owner:

1. **One group review service, Vouch, with brand-specific policies.** Vouch is built inside the One Stay program's shared trust scope and owned by the trust platform engineering team under Sofia. It holds the review record, the blind vault, the integrity pipeline and the review event log. Eligibility, scales, windows and display rules are versioned per brand: Nookaway keeps two-way, 1–5, double-blind reviews; Roomstead keeps one-way, 1–10 reviews.
2. **Eligibility from the reservation contract.** Vouch reads stay state from the shared One Stay reservation contract, not from Burrow or Keystone tables. Each invitation records the eligibility policy version and the arrival evidence.
3. **Integrity before reveal.** Nookaway reviews are scored while sealed. Reviews with reciprocity, shared-instrument or price-gap signals from the trust platform's risk signal feed are held for review before the window closes. Roomstead reviews above a risk threshold are held for up to 72 hours before publication.
4. **One log, derived numbers.** Page scores, the ranker's quality features, Hearth, guest-reputation features for screening ([Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents)) and partner analytics are rebuilt from the Vouch event log. A removal updates all of them within one hour.
5. **Hearth counts distinct, unaffiliated guests.** From the Q4 2027 assessment, the 8-stay threshold counts only stays by guests with no shared payment instrument, device or payout account with the host, and only stays above 30% of the listing's median nightly price for the season.
6. **The verification statement is generated from policy.** Noor van Dijk's regulatory team reviews each policy version, and the text on both brands' pages is rendered from it.

Vouch's first release went live for Nookaway in **November 2027**; Roomstead's migration out of Keystone's review module is planned for 2028.

{id: reviews-and-reputation--could-this-happen-at-roomstead}
### "Could this happen at Roomstead?"

Mariana asked the question in April, and Roomstead's audit in **June 2027** found the OTA versions of the same problem.

- **Self-booked reviews.** **41** properties had clusters of stayed reservations booked from email addresses or devices that also logged into the property's Partner Hub account, the Roomstead extranet. Under the agency model a self-booking cost the property only its commission: a one-night stay at Roomstead's €128 average daily rate cost about **€19** at a 15% commission. Roomstead removed **1,260** reviews and opened partner-integrity cases.
- **No-show suppression.** **63** properties marked reservations as no-shows at more than three times their market's rate, and those marks fell disproportionately on reservations with guest messages sent during the stay, which is evidence of arrival. Roomstead changed the flow: a no-show mark now notifies the guest, who can contest it; a contested mark with arrival evidence restores review eligibility and the commission. The contested-no-show rate per property became a monitored metric.

Roomstead had no ring. One-way reviews and per-property commission make rings less useful; self-booking is the cheaper attack. The defenses differ, but they read the same graph of identities, devices and payments, which is why Vouch is shared.

{id: reviews-and-reputation--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Who may review** | Anyone (open platform) | Only parties to a stayed reservation | Review sites without transactions | Every booking marketplace; required for any "verified" claim |
| **Direction** | One-way (guest → property) | Two-way, double-blind | Hotels and professional supply with front desks | Homes, where the host's view of the guest is the main evidence of guest behavior |
| **Publication** | Publish immediately, remove later | Hold until integrity checks finish | Low-risk segments where speed matters | Two-way reviews (free time in the blind window); high-risk segments |
| **Score formula** | Plain average | Recency-weighted, shrunk to a prior | Display, if a minimum count applies | Ranking and program thresholds |
| **Display window** | Keep all reviews | Expire after a period or ownership change | Single-owner homes with stable hosts | Hotels that change owners, brands or renovate |
| **Aggregates** | Incremental counters | Rebuilt from the event log | Prototype scale | Any system that removes reviews and must explain past scores |
| **Detection** | Text classifiers | Relational graph features | Abusive content, personal data | Rings, self-booking, affiliation |
| **Credential cadence** | Live score | Periodic snapshot | Internal ranking features | Public badges with consequences hosts can plan for |
| **Ownership** | Review team per brand | One group review service, brand policies | Brands with no shared supply or identity | Groups with shared identity, payments and trust platforms |

The two choices I would not compromise on are **eligibility from the reservation record** and **derived numbers from one log**. Everything else is a calibration that can differ by brand and market.

{id: reviews-and-reputation--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

| Dimension | Accommodation marketplace (Roomstead) | Hosted-stays marketplace (Nookaway) |
| --- | --- | --- |
| **Supply reviewed** | A property operated by a business, with staff and a brand; reputation survives individual employees but not a change of owner | A home and a person; the host's reputation is personal and moves with the host across listings |
| **Direction** | One-way; guest ratings are rarely needed | Two-way; the host's review of the guest is a trust and screening credential |
| **Data model** | Property-level score with subscores; room types usually not rated separately | Listing-level score plus host-level aggregate; guest-level reputation |
| **Eligibility evidence** | Weak arrival evidence under the agency model; property reports no-shows | Stronger arrival evidence from messages, check-in and payments; platform holds the money |
| **Integration** | Reviews read and replied to through extranet and connectivity APIs; PMS vendors surface them | Hosts reply in the host app; PMS-connected managers use the partner API |
| **Typical attack** | Self-booking; no-show suppression; competitor reviews | Review-trading rings; fake guest reputations; retaliation pressure |
| **Quality program** | Partner programs mix review scores with commercial terms | Credentials are quality-only and fuse reviews with support and messaging data |
| **Regulation** | Omnibus, DMCC and FTC duties on the property score and verification claim; P2B on partner restrictions | The same, plus DSA statements of reasons for host and guest account restrictions, which are more frequent |
| **What can be shared** | Review service, event log, integrity pipeline, graph features, dispute workflow, verification statement generator | The same |

The judgement: **share the machinery and the evidence, keep the policies per brand.** The review record, the event log, the integrity pipeline, the graph features from the trust platform, the dispute workflow and the generated verification statement are the same problem twice, and the regulators asking about them are the same. The direction of reviews, the scale, the windows, the display rules and the quality programs encode real differences between hotels and homes and should stay with each brand. Forcing Nookaway's two-way reviews onto Roomstead would invent a hotel rating of guests that no partner uses; forcing Roomstead's one-way model onto Nookaway would delete the host's evidence about guests, which screening depends on. Convergence makes the shared service more valuable, not less: when Nookaway pilots boutique hotels in 2028, Vouch can apply a one-way policy to those listings without a second system.

{id: reviews-and-reputation--failure-modes}
## Failure Modes

**"Verified" means "had a reservation".** The eligibility check reads only reservation existence and checkout date. *Symptom:* paid one-night stays with no messages carry top ratings. *Fix:* eligibility evidence on every review, arrival signals where they exist, and relational integrity checks.

**Removals that do not propagate.** A removed review stays in the ranker's feature store, a badge computation or a generated summary. *Symptom:* a host keeps a credential earned with removed reviews; a summary quotes a fake. *Fix:* every consumer derives from the event log; removal latency is a monitored service level.

**The self-reporting veto.** Eligibility depends on a party's own report, such as a no-show mark. *Symptom:* properties with unusual no-show rates and few negative reviews. *Fix:* notify the guest of the no-show, let the guest contest it, monitor the rate against arrival evidence.

**Guest reputation as an attack surface.** Host reviews of guests feed screening without integrity checks. *Symptom:* guests with spotless but recent and clustered histories in high-risk bookings. *Fix:* treat host→guest reviews with the same integrity pipeline; screening features should discount reviews from affiliated hosts.

**A classifier nobody owns.** A fake-review model blocks or passes reviews with no measured recall and no appeal analysis. *Symptom:* a ring found by a support agent's intuition, months after it started. *Fix:* an owner, labeled samples from investigations, reported recall estimates, and appeal reversal rates (see [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) on model governance).

**A verification claim that drifted.** The page says reviews come only from verified guests, but imported reviews from an acquired brand or a partner feed follow other rules. *Symptom:* a regulator's sample finds reviews that fail the stated policy. *Fix:* the statement is generated from the policy, and every review carries the policy version that admitted it.

{id: reviews-and-reputation--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, reviews are a **trust asset with a regulatory perimeter**, and the decisions that matter are about ownership and evidence, not about rating scales.

1. **Who owns "verified".** The definition of an eligible review is a policy with legal consequences in three jurisdictions. It should be owned by the trust function, approved by legal and regulatory affairs, versioned, and rendered on the page. Product teams may propose changes; they should not ship them alone.
2. **Where the review service sits.** I would place it in the shared trust platform, not in the brands' content or page teams, because its hard dependencies are identity, payments, reservation state and enforcement. The page, ranking and programs are consumers.
3. **What the log must answer.** For any property or listing and any past date: which reviews were published, which were removed and why, and what score was shown. If the system cannot answer that, it cannot answer a regulator or defend a partner dispute.
4. **Who may read review data, and for what.** Ranking, screening, programs, partner analytics and generated summaries all read reviews. Each read should be declared, with its definition (raw average, shrunk score, recency window), so a removal or a definition change can be traced to every consequence.
5. **What to measure.** Collection rate, hold and removal rates, ring detection latency, dispute and appeal reversal rates, and no-show contest rates, reported quarterly to trust and regulatory leadership as the "reasonable and proportionate steps" evidence.
6. **How programs change.** Quality-program thresholds move visibility and money; test changes like ranking changes ([Testing Everything: Experimentation Platforms for Stays](#stays-experimentation)) and announce them to hosts and partners with lead time.

The long-term risk is not fake reviews; it is **reviews losing their meaning**. If every listing is a 4.9 and every hotel a 9.1, guests stop reading the score, and the platform loses its cheapest trust signal.

{id: reviews-and-reputation--questions-to-ask}
## Questions to Ask

1. What exactly makes a review "verified" on our platforms, which system supplies each fact, and what does the page tell guests?
2. Can any party to a stay prevent the other from reviewing it, for example through a no-show mark or a cancellation after arrival?
3. Where are reviews held before publication, and how much time does our integrity pipeline have for one-way and two-way reviews?
4. Which signals other than text does our fake-review detection use, and does it read the trust platform's identity, payment and device graph?
5. When a review is removed, which derived numbers change, how fast, and how would we prove it?
6. Can we reconstruct a property's displayed score and its review list as of any past date?
7. Who decides partner and host disputes, and how do dispute and reversal rates vary by partner?
8. Which quality-program thresholds could be met with cheap, affiliated stays, and how would we notice?
9. Do host reviews of guests feed screening or fraud models, and are they subject to the same integrity checks?
10. Are generated review summaries built only from published reviews and regenerated when one is removed?

The protection programs and screening models that read guest reputations, and the incidents that test them, are the subject of [Damage, Parties and Emergencies: Protection and Incident Response](#protection-and-incidents).

{id: reviews-and-reputation--sources-and-evidence}
## Sources and Evidence

{id: reviews-and-reputation--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [How we work](https://www.booking.com/content/how_we_work.html) — Booking.com, n.d. (updated 2025; fetched October 2026). Review eligibility ("stayed there, or … arrived"), three-month submission window, 36-month display window and ownership change, 1–10 scores and subscores, recency weighting, fake-review detection, replies, Google translations.
- [How Expedia Reviews Engineering is using event streams as a source of truth](https://medium.com/expedia-group-tech/how-expedia-reviews-engineering-is-using-event-streams-as-a-source-of-truth-d3df616cccd8) — Expedia Group Technology, 2023. Kafka topic as source of truth for moderated reviews; derived aggregates, cache, index and sentiment.
- [Put Your Trip on Autopilot: Expedia Group Introduces New Innovations at EXPLORE](https://ir.expediagroup.com/news-and-events/news/news-details/2024/Put-Your-Trip-on-Autopilot-Expedia-Group-Introduces-New-Innovations-at-EXPLORE-to-Take-the-Stress-out-of-Travel-and-Enhance-Partner-Experience/default.aspx) — Expedia Group, 2024. Partner insights on recurring negative review sentiment.
- [Booking.com enhances travel planning with new AI-powered features](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/) — Booking Holdings, 2024. Property Q&A from reviews; review summaries in testing.
- [How reviews work (article 13)](https://www.airbnb.com/help/article/13) — Airbnb Help Center, n.d. (fetched October 2026). 14-day window, simultaneous reveal, cancellation rules, three-review display threshold, rating as plain average, review highlights, Guest Favorite eligibility.
- [Reviews Policy (article 2673)](https://www.airbnb.com/help/article/2673) — Airbnb Help Center, n.d. (fetched October 2026). Removal categories; disagreement with a rating does not qualify; policy informed by consumer law.
- [Star ratings (article 1257)](https://www.airbnb.com/help/article/1257) — Airbnb Help Center, n.d. (fetched October 2026). Rating categories; ordering by relevance.
- [How do I become a Superhost? (article 829)](https://www.airbnb.com/help/article/829) — Airbnb Help Center, n.d. (live 2026). Quarterly assessment and thresholds.
- [Airbnb 2023 Winter Release](https://news.airbnb.com/en-uk/airbnb-2023-winter-release/) — Airbnb Newsroom, 2023. Guest Favorites launch and criteria.
- [Q3 2025 Shareholder Letter](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf) — Airbnb, 2025. Over 550,000 listings removed under the hosting quality system.
- [Airbnb introduces new anti-party technology in US and Canada](https://news.airbnb.com/airbnb-introduces-new-anti-party-technology-in-us-and-canada) — Airbnb Newsroom, 2022. Review history as a screening signal.
- [Six-year update on anti-discrimination work](https://news.airbnb.com/sixyearadupdate) — Airbnb Newsroom, 2022. More guests receiving reviews as an anti-discrimination measure.
- [Preferred Partner Programme](https://partner.booking.com/en-gb/solutions/preferred-partner-programme) — Booking.com Partner Hub, n.d. (live 2026). Review scores in program eligibility.
- [Agoda Partner Portal announcement](https://kyodonewsprwire.jp/release/202608174214) — Agoda via Kyodo News PR Wire, 2026. AI review summaries for partners.
- [Expedia Group lodging supply APIs: introduction](https://developers.expediagroup.com/supply/lodging/docs/avail_and_rate_apis/avail_rates/getting_started/introduction) — Expedia Group Developer Hub, 2025. Reviews API among property-management APIs.
- [Translation Engine launches for reviews](https://www.hospitalitynet.org/news/4112343.html) — Airbnb via Hospitality Net, 2022. Automatic translation extended to reviews.
- [Eval-driven development: lessons from evaluating GenAI at scale](https://airbnb.tech/ai-ml/eval-driven-development-lessons-from-evaluating-genai-at-scale/) — Airbnb Tech, 2026. Evaluation infrastructure for features including review highlights.

{id: reviews-and-reputation--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2019/2161 (Omnibus Directive)](http://publications.europa.eu/resource/celex/32019L2161) — EU, 2019. UCPD Art. 7(6) and Annex I points 23b–23c; applies from 28 May 2022.
- [Regulation (EU) 2019/1150 (P2B Regulation)](http://publications.europa.eu/resource/celex/32019R1150) — EU, 2019. Art. 4 restriction, suspension and termination of business users; applies from 12 July 2020.
- [Regulation (EU) 2022/2065 (Digital Services Act)](http://publications.europa.eu/resource/celex/32022R2065) — EU, 2022. Arts. 16, 17 and 20; applies from 17 February 2024.
- [Digital Markets, Competition and Consumers Act 2024, Schedule 20](https://www.legislation.gov.uk/ukpga/2024/13/schedule/20) — UK legislation, 2024. Paragraph 13 on fake reviews; in force 6 April 2025.
- [Fake reviews (CMA208)](https://www.gov.uk/government/publications/fake-reviews-cma208) — UK Competition and Markets Authority, 2025. Guidance on reasonable and proportionate steps.
- [Federal Trade Commission announces final rule banning fake reviews and testimonials](https://www.ftc.gov/news-events/news/press-releases/2024/08/federal-trade-commission-announces-final-rule-banning-fake-reviews-testimonials) — US FTC, 2024. Scope of the rule.
- [Trade Regulation Rule on the Use of Consumer Reviews and Testimonials](https://www.federalregister.gov/documents/2024/08/22/2024-18519/trade-regulation-rule-on-the-use-of-consumer-reviews-and-testimonials) — Federal Register, 2024. Publication 22 August 2024; effective 21 October 2024.

{id: reviews-and-reputation--research-and-practitioner-sources}
### Research and practitioner sources

- [Promotional Reviews: An Empirical Investigation of Online Review Manipulation](https://doi.org/10.1257/aer.104.8.2421) — Mayzlin, Dover and Chevalier, *American Economic Review*, 2014. Booking-gated reviews versus open reviews for hotels.
- [Reciprocity and Unveiling in Two-Sided Reputation Systems: Evidence from an Experiment on Airbnb](https://doi.org/10.1287/mksc.2021.1311) — Fradkin, Grewal and Holtz, *Marketing Science*, 2021. Simultaneous reveal increases reviewing and reduces retaliation and reciprocity.
- [A first look at online reputation on Airbnb, where every stay is above average](https://doi.org/10.1007/s11002-020-09546-4) — Zervas, Proserpio and Byers, *Marketing Letters*, 2020. Rating concentration on a two-way platform.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
