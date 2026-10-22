{id: trust-and-safety-architecture}
# 24. Trust and Safety as a Platform

![Trust and Safety as a Platform — logo](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take trust and safety apart into policies, detection, decisions, enforcement, review and measurement. You will learn which parts belong in a shared group platform and which stay local, and how one enforcement decision has to reach every system that shows, alerts on or monetizes a listing.

> **WHY THE BUSINESS CARES:** A buyer who is scammed once rarely comes back, and a seller who is wrongly blocked tells other sellers. Trust is the reason a buyer contacts a stranger, so moderation quality, speed and fairness decide liquidity as directly as search does. Since 2024, the Digital Services Act has also made every moderation decision a record a regulator can ask about.

> **WHY ARCHITECTS SHOULD CARE:** Trust and safety touches every bounded context: insertion, search, messaging, alerts, payments, ads and support. A platform without one decision record and one propagation path cannot say what it removed, why, or whether the removal actually took effect.

> **KEY POINTS:**
>
> * **Trust and safety is five functions, not one queue.** Policy, detection, decision, enforcement and review fail in different ways and change at different speeds. Architect them as separate components joined by one decision record, and treat policies as versioned data rather than as code scattered across services.
> * **An enforcement action is only real once every consumer has applied it.** Removing a listing has to reach search, alerts, recommendations, messaging, SEO pages, ads and payments. Emit enforcement as events with the same discipline as listing state changes, and monitor how long propagation takes.
> * **Measure harm, not activity.** Queue sizes and removal counts show how busy the team is. Prevalence from random sampling, time to action, precision, and the appeal overturn rate show whether the marketplace is safe and fair. A shared platform pays for itself mostly through shared evidence, tooling and signals, while policy stays local where law and markets differ.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **Moderation as an Afterthought** — a queue bolted onto the insertion flow cannot re-score edits, route reports or produce the evidence the DSA requires, and it grows faster than the team that empties it.
> * **Ghost Inventory** — a takedown that reaches the listing database but not the alert digest, the recommendation cache or the SEO page leaves fraudulent listings visible after they were "removed".
> * **Set-and-Forget AI** — moderation classifiers that auto-decide 94% of listings, with no prevalence sampling or overturn monitoring, look accurate while a new scam pattern goes past them.

Most marketplaces build trust and safety (T&S, the policies, systems and people that keep users safe and the inventory honest) in the order problems appear. A keyword filter arrives after the first wave of spam, a review queue after the first press story, a report button after the first regulator letter. Each piece is attached to whatever system was nearest. Ten years later the group has **four moderation stacks that cannot share a signal**, and nobody can answer a simple question: *what did we remove last month, why, and did it actually disappear?*

Part IV built search, recommendations and alerts to put a listing in front of buyers within seconds, and each of them must also obey a removal. This chapter, the first of Part V, treats trust and safety as a **platform capability** with its own architecture. It defines the five functions and the components that implement them. It follows one enforcement decision through every system that has to obey it, and sets out the metrics that show whether the platform works. It also argues for a split: share the machinery across brands, keep the policy local.

Fraud is the most expensive harm a classifieds platform faces, and it has its own chapter, [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), which owns risk scoring, fraud signals and step-up friction. Identity levels and verification belong to [Who Is on the Other Side? Identity and Verification](#identity-and-verification). The legal detail of the Digital Services Act (DSA) and other regulation belongs to [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation). Here we build the platform those chapters plug into. The running example is Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

{id: trust-and-safety-architecture--setting-the-scene-at-veldmark-four-stacks-and-one-phishing-link}
## Setting the Scene at Veldmark: Four Stacks and One Phishing Link

On Sunday **7 March 2027** at 20:11 CET, a "buyer" sent Femke, a private seller in Rotterdam, a fake Tradeyard Safe Deal payment link for her **€240** city bike. The message was delivered because the link's domain had been registered that day and no rule looked at domain age. Femke reported it at 20:19. Tradeyard Netherlands' in-house rules engine suspended the account at 20:26, and an analyst wrote a rule that then withheld **37** similar messages to other sellers. By the standards of most classifieds platforms, seven minutes from report to suspension is fast. The details, including the bike's sale the next day, are in [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads) and [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention).

Ingrid Halvorsen had joined Veldmark as Group Chief Architect five weeks earlier. On Tuesday **16 March** she asked Aisha Rahman, the Group Head of Trust & Safety, to walk her through what had happened *outside* Tradeyard NL. The answers were less comfortable than the seven minutes:

- The phone number used to register the suspended account had also registered a **Motorvane** private-seller account three weeks earlier. Motorvane could not know. Each brand runs its own identity system, so no shared block list exists.
- Tradeyard **Belgium** shares the Netherlands rules engine, but the new rule took until Wednesday to reach it. Each country's rules are deployed with the country's Yardstick configuration, and Yardstick, Tradeyard's PHP monolith, deploys twice a week.
- Tradeyard **Poland** and **Portugal** use an outsourced moderation queue with its own keyword lists. Neither received the rule.
- **Hearthly** runs in-house rules on Google Cloud. Its Spanish brand, the former Casavista, still uses Casavista's review tool.

Aisha's inventory of the group's T&S landscape fitted on one slide:

| Brand | Detection | Human review | Policies | Appeals | DSA statements of reasons |
| --- | --- | --- | --- | --- | --- |
| Tradeyard NL/BE | In-house rules engine plus three ML models (listing, image, message) | 46 in-house moderators, Lisbon | Wiki pages per country, partly translated | E-mail to support; no link to the original decision | Template in Yardstick; nightly batch to the Transparency Database |
| Tradeyard PL/PT | Vendor keyword lists; NL image model via an API | 112 outsourced moderators, two vendors | Vendor playbooks | Vendor ticket system | Vendor export, monthly |
| Motorvane | Dealer KYB at contract signature only; private-seller checks | 17 moderators, Düsseldorf | Contract terms for dealers | Account managers | Hand-built for private sellers |
| Hearthly FR/ES | In-house rules; manual review of new agencies | 35 moderators, Lyon and Barcelona | Two documents, French and Spanish | Support tool | Separate exporters for FR and ES |

That made **210 moderators**, four definitions of a "prohibited item", three appeal processes and five ways of producing a DSA **statement of reasons** (the notice the DSA requires a platform to send a user whose content it restricts). At Tradeyard alone, **94%** of new-listing decisions were automated and about **138,000 listings a week**, 6% of 2.3 million, went to human review.

Ingrid's question for the Common Ground program was not whether to centralize the moderators. It was narrower and harder: **which parts of trust and safety are one platform, and which must stay four?** The rest of this chapter is the answer the architecture advice forum adopted in mid-2027. The shared T&S platform went live for Tradeyard NL and BE in November 2027.

{id: trust-and-safety-architecture--concepts-the-five-functions-of-trust-and-safety}
## Concepts: The Five Functions of Trust and Safety

Trust and safety work is easier to architect once it is split into functions that change at different speeds and fail in different ways.

| Function | Question it answers | Changes at the speed of | Typical failure |
| --- | --- | --- | --- |
| **Policy** | What is allowed, for whom, where? | Law, market and scam trends: weeks to months | Policies exist only as wiki prose; rules drift from the written policy |
| **Detection** | Which items, accounts or messages might violate a policy? | Adversaries: hours to days | Detection runs only at creation; edits and messages are not scored |
| **Decision** | What do we do about this item, given policy and evidence? | Policy and risk appetite | Several services decide independently and contradict each other |
| **Enforcement** | Did the action take effect everywhere? | System architecture | Removal reaches the database but not search, alerts or caches |
| **Review and redress** | Was the decision right, and can the user contest it? | Volume and law | Appeals are support tickets with no link to the decision or evidence |

A sixth concern runs across all five: **measurement and transparency**, the ability to say, reproducibly, how much harm exists, how much was caught, how fast, and how often decisions were wrong.

![Five gears of different sizes labeled Policy, Detection, Decision, Enforcement and Review, joined by one record ribbon and watched by a magnifying glass.](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/five-functions-different-speeds.jpeg)

**Figure 1:** *Trust and safety is five functions that change at different speeds and fail in different ways, joined by one decision record and watched by measurement.*

Five definitions are used throughout the chapter.

- A **policy** is a named, versioned rule of conduct with a scope (category, country, seller type), a rationale and a legal or contractual ground. "No live animals in Tradeyard PT except through registered breeders" is a policy. A keyword list is not; it is one detector for a policy.
- The **moderation pipeline** is the sequence of components that evaluates content and behavior against policies and produces decisions: synchronous gates, asynchronous detectors, human review queues and sampling. This book uses the term for listings, accounts and messages alike. This chapter owns it.
- An **enforcement action** is the concrete restriction a decision imposes: a warning, a reach limit, a demotion, a hold, a removal, a suspension, a payment freeze. Every action has a target (listing, account, message, payment), a scope (country, brand), a duration and a reason. This chapter owns the term.
- A **case** is the unit of human work: one or more items, the evidence, the decisions and the communications that belong together. A fake-rental ring of 26 accounts is one case, not 180 tickets.
- **T&S metrics** are the measures of harm, speed and accuracy defined later in this chapter: prevalence, time to action, precision and recall, and the appeal overturn rate. This chapter owns them.

The functions also separate the **listing view** from the **actor view**. A listing can violate a policy on its own: a weapon, a counterfeit, a discriminatory rental ad. An actor can be a problem even when every listing looks clean: a fraud ring, a takeover account, a reseller of stolen goods. Mature platforms decide on both, and the decision record links them. The [Bounded Contexts for Marketplaces: Where One Listing Becomes Many Models](#bounded-contexts) chapter treats Trust as its own bounded context with its own model of the listing. That model is a *subject under evaluation*, not a catalog item.

{id: trust-and-safety-architecture--policies-as-versioned-reference-data}
### Policies as versioned reference data

The most underrated design decision in trust and safety is to **treat policies as data**: a registry of policy records that rules, models, reviewer guidelines, user notices and reports all point to. A policy record at Veldmark looks like this:

| Field | Example (Tradeyard, payment-link phishing) |
| --- | --- |
| Policy ID and version | `POL-FRAUD-PAYLINK` v3, effective 18 March 2027 |
| Scope | Messages and listings; all Tradeyard countries; all account types |
| Statement | Messages may not contain links or QR codes that imitate Tradeyard payment, shipping or Safe Deal pages |
| Ground | Contractual (terms of service section 7.2); in NL also an illegal-content ground (fraud) |
| DSA category | Scams and fraud |
| Detectors | Domain-age rule, platform-brand-in-URL rule, QR decoder, message model v12 |
| Allowed actions | Withhold message; suspend account; freeze Safe Deal payouts pending review |
| Reviewer guideline | Link to guideline v3, with five labeled examples |
| User-facing reason | Template ID and approved text in Dutch, French, Polish, Portuguese |
| Owner | Group T&S policy lead; local policy owner per country |

Three consequences follow. First, a decision can cite **policy ID and version**, so a statement of reasons, an appeal and a transparency report all refer to the same thing. Second, a policy can have **country overlays** (Poland may prohibit something the Netherlands allows) without forking the platform. Third, the policy registry is where legal review happens. Lawyers review policies and user-facing reasons. Engineers review detectors. Neither needs to read the other's code.

The [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) chapter treats category trees as versioned reference data. The same reasoning applies here, with one addition: **a decision must stay explainable under the policy version that was in force when it was taken**, even after the policy changes.

{id: trust-and-safety-architecture--architecture-the-moderation-pipeline-and-its-components}
## Architecture: The Moderation Pipeline and Its Components

The reference architecture below is assembled from public building blocks: Meta's Sigma rule engine, described in a 2015 engineering post; Stripe Radar's documented rule operations; OLX's published chat moderation; the DSA's notice, statement-of-reasons and appeal requirements; and the practices recommended in a July 2026 expert report commissioned by Ofcom, the UK online-safety regulator. **It is a reference-architecture inference. No classifieds company has published its T&S architecture in this form.**

![Diagram: The trust and safety platform as components](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/fig02-trust-safety-platform-components-detection-human.jpeg)

**Figure 2:** *The trust and safety platform as components. Detection and human review both feed one decision service, which is the single writer of decision records; enforcement, user notices, appeals, evidence and metrics all derive from those records.*

| Component | Responsibility | Key interface |
| --- | --- | --- |
| **Policy registry** | Versioned policies, overlays, reviewer guidelines, reason templates | Read API; change events when a policy version takes effect |
| **Synchronous gate** | Rules, list lookups and a light model inside the insertion or send path; returns allow, hold or reject | Called by insertion, edit, message send, login; strict latency budget |
| **Asynchronous detectors** | Image models, duplicate and stolen-photo search, text and LLM classifiers, price anomaly, graph features | Subscribe to listing and message events; publish scores |
| **Random sampling** | Draws unbiased samples of live listings and messages for human labeling | Feeds review queues; feeds prevalence metrics |
| **Decision service** | Combines rule hits, scores, actor context and human input into an action from the enforcement ladder; writes the decision record | The only component that writes decisions |
| **Case management** | Queues, prioritization, reviewer tooling, evidence views, service-level timers, quality sampling | Reviewer UI; case API for support and legal |
| **Enforcement events** | Publishes `EnforcementApplied` and `EnforcementLifted` events; tracks acknowledgement by consumers | Event backbone; propagation dashboard |
| **Statement-of-reasons service** | Renders user notices, strips personal data, submits to the DSA Transparency Database | Driven by decision records |
| **Appeals** | Accepts complaints, routes them to qualified reviewers, reverses or upholds | Writes a new decision linked to the original |
| **Evidence and audit store** | Immutable record of decisions, rule and model versions, reviewer identity and content snapshots, with retention per data class | Query API for appeals, regulators, law enforcement requests |
| **Metrics** | Prevalence, time to action, precision, overturn rates, transparency-report figures | Built from decision records and samples, not from operational logs |

{id: trust-and-safety-architecture--the-synchronous-gate-and-the-asynchronous-path}
### The synchronous gate and the asynchronous path

The pipeline has two speeds. The **synchronous gate** sits inside the user's action: publishing a listing, editing it, sending a message, logging in. It has a budget of a few hundred milliseconds at most and can only afford deterministic rules, lookups against block lists (phone numbers, e-mail addresses, IBANs, device identifiers, image hashes) and a cheap model. Its outcomes are *allow*, *hold for review* and *reject*.

The **asynchronous path** runs on events after the action. Image classification, duplicate search, OCR on images (text in an image is a classic way to smuggle a phone number past text filters), graph features linking accounts, price anomaly against a valuation model and LLM classifiers all take longer. They can still demote, hold or remove a listing that is already live.

Which checks run in which path is a **risk decision, not a technical one**. A €15 children's book can go live on the gate's verdict and be re-checked within minutes. A rental flat in a city with a known fake-rental problem should wait for the image and duplicate checks, because the harm of a fake listing being live for ten minutes is larger than the cost of a ten-minute delay. The [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline) chapter owns the end-to-end publication path and its freshness targets. This chapter owns the moderation gate inside it.

![A road splitting into a fast green lane where a book goes live at once and an orange lane where a rental listing waits for image and duplicate checks.](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/risk-tiered-two-speed-path.jpeg)

**Figure 3:** *Which checks run before publication is a risk decision: a €15 book can go live on the gate and be re-checked within minutes, while a rental in a fake-rental hotspot waits for the image and duplicate checks.*

{id: trust-and-safety-architecture--moderation-modes-a-spectrum-not-a-choice}
### Moderation modes: a spectrum, not a choice

Pre-moderation (checking before publication) and post-moderation (publishing first and checking afterwards) are usually presented as a choice. In practice they are the ends of a spectrum, and large platforms run several points on it at once.

| Mode | Time to live | Exposure to harm | Cost | Where it fits |
| --- | --- | --- | --- | --- |
| Full human pre-moderation | Minutes to hours | Lowest | Highest | Small sites; high-risk categories such as pets, tickets, rentals |
| Automated pre-moderation, human review for the grey zone | Seconds; grey zone minutes | Low | Medium | The mainstream default for large classifieds |
| Publish, then score asynchronously | Instant | A window of exposure | Lower | Low-risk categories and trusted sellers |
| Reactive only (notice and action) | Instant | Highest | Lowest | Legally minimal; not defensible for fraud at scale |

The design that works is **risk-tiered**: the mode depends on the category's risk, the seller's trust level (account age, verification level from [Who Is on the Other Side? Identity and Verification](#identity-and-verification), history) and the listing's risk score. A verified dealer's car listing from a DMS feed can go live on the gate. A new account's first rental listing waits for the full check.

Two public cases show why the mode matters.

- **Re-moderate on every material edit.** In a December 2024 undercover test, the UK consumer organization Which? posted fake camera ads on Facebook Marketplace, Gumtree and Nextdoor. Gumtree blocked the first scam-style ad, but **edited versions passed review "in minutes"**, and on Facebook one ad stayed live for almost 48 hours after the price was halved and Apple gift cards demanded ([Which?, 2024](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1)). The lesson is architectural: a change of price, payment terms, contact details or photos is a new submission, and the pipeline must treat it as one.
- **Say what you actually do.** In December 2015, a Paris court found leboncoin guilty of misleading commercial practices because it claimed all ads passed a validation process when not all did. The court also confirmed leboncoin's status as a hosting provider, which does not oblige it to check every ad before publication ([Clubic, 2015](https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html)). The case is more than ten years old, but the principle has not aged: the moderation mode is a factual claim, and the terms and marketing must describe the mode the architecture actually runs.

{id: trust-and-safety-architecture--human-review-queues-priorities-and-sampling}
### Human review: queues, priorities and sampling

Human review exists for three reasons: to decide the grey zone that automation cannot, to produce **labels** that train and evaluate the models, and to satisfy the law where the law requires a human (DSA appeals, discussed below). Each reason calls for a different queue design.

- **Grey-zone queues** should be prioritized by expected harm multiplied by uncertainty, not by arrival time. A suspected fake rental with ten contacts in its first hour outranks a possibly miscategorized sofa.
- **Label queues** need an unbiased sample. If reviewers only see what the models flagged, the labels describe the models' blind spots poorly, because the blind spots never reach a reviewer.
- **Regulated queues** (appeals, trusted-flagger notices, authority orders) carry legal timers and need qualified reviewers.

Stripe's documentation for its Radar fraud product gives a rule that transfers directly: **a review queue that almost always ends in the same outcome should become an automated rule** ([Stripe Radar docs, n.d.](https://docs.stripe.com/radar/rules)). The inverse also holds. An automated rule that reviewers would frequently overturn should go back to the queue.

The **random sample** gives the only number in trust and safety that does not depend on what the detectors already catch. The Ofcom-commissioned expert report of July 2026 recommends that larger platforms regularly review randomly sampled ad impressions and the most-viewed ads to estimate the prevalence of violating content ([Integrity Institute for Ofcom, 2026](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf)). For a classifieds platform the equivalent is a stratified sample of live listings and delivered messages per category and country, reviewed blind.

{id: trust-and-safety-architecture--llms-in-the-pipeline}
### LLMs in the pipeline

Large language models (LLMs) entered production moderation between 2024 and 2026. The public classifieds evidence is thin but real. In a January 2026 post, OLX described a generative-AI system that detects and blocks suspicious images in sales chats in real time, live in Poland, Portugal, Bulgaria, Romania and other markets ([OLX Group, 2026](https://www.olxgroup.com/?p=4590)). Llama Guard, published by Meta researchers in December 2023, showed that a policy taxonomy can be supplied to a safety model as a prompt rather than retrained ([Inan et al., 2023](https://arxiv.org/abs/2312.06674)).

My rule for placing LLMs in a moderation pipeline has four parts:

1. **Grey zone only.** Run LLM classifiers on the uncertain band of a cheap classifier and on items already headed for human review, not on all traffic. At Tradeyard's 2.3 million new listings a week, the cost difference is an order of magnitude.
2. **Policy agility is the main value.** A new scam script can be described in a prompt the day it appears, then distilled into a cheaper classifier once labels accumulate.
3. **Deterministic floors stay.** Hash lists, block lists and hard rules cannot be argued with by a cleverly worded listing. Prompt injection in a listing description is an attack surface.
4. **Drafts, not decisions, where the law needs a human.** An LLM can summarize a case and draft the explanation in a statement of reasons. It cannot decide a DSA complaint, which must not be decided "solely on the basis of automated means".

{id: trust-and-safety-architecture--enforcement-actions-and-their-propagation}
## Enforcement Actions and Their Propagation

{id: trust-and-safety-architecture--the-enforcement-ladder}
### The enforcement ladder

Removal is one rung of a ladder of actions, and often not the right one. The Ofcom-commissioned experts describe a graduated ladder, from a nudge through posting limits, payment freezes and re-verification to suspension. They note that payment freezes need a higher evidentiary threshold ([Integrity Institute for Ofcom, 2026](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf)). A ladder for a classifieds platform:

| Rung | Action | Target | Typical trigger | DSA statement of reasons? |
| --- | --- | --- | --- | --- |
| 1 | In-context warning to the counterparty | Conversation | Payment keywords, off-platform move | No restriction on the sender's content |
| 2 | Nudge or correction request | Listing | Missing mandatory field, wrong category | No, unless visibility is restricted |
| 3 | Friction or re-verification (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)) | Account | Unusual login, risk score in the grey band | Yes, if service is restricted |
| 4 | Reach limit or **demotion** | Listing or account | Low-trust actor, suspected duplicate | **Yes**: demotion is a restriction |
| 5 | Hold for review | Listing, message | Gate verdict "hold" | Yes, if it lasts and the user is told |
| 6 | Removal or disabling | Listing, message | Clear policy violation | Yes |
| 7 | Payment freeze | Payouts | Strong fraud evidence on a transaction | Yes (monetary restriction) |
| 8 | Suspension or termination | Account, and linked accounts | Fraud, repeated violations | Yes |

The fifth column surprises many ranking teams: Article 17 of the DSA covers **demotion** as well as removal, so a ranking system that quietly pushes suspected scam listings down the results is taking a moderation decision that needs a statement of reasons. The DSA Transparency Database schema has a value for exactly this case, `DECISION_VISIBILITY_CONTENT_DEMOTED` ([European Commission, n.d.](https://transparency.dsa.ec.europa.eu/page/api-documentation)). **Ranking teams are in the moderation business**, and actor-trust down-ranking belongs behind the decision service, not inside a ranking feature. [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking) covers the ranking side of this boundary.

{id: trust-and-safety-architecture--one-decision-many-consumers}
### One decision, many consumers

A removal is not finished when the listing's status changes. A classifieds platform shows, alerts on and monetizes a listing through many systems, and each holds its own copy of it.

| Consumer | What it holds | What enforcement must do there |
| --- | --- | --- |
| Listing system of record | Status | Set the restricted state, keep the version history |
| Search index | Listing document | Delete or hide within seconds |
| Saved-search alerts and digests | Pending notifications | Drop queued alerts; exclude from digests already built |
| Recommendations | Candidate caches, embeddings | Evict; block from similar-listing results |
| Messaging | Conversations about the listing or with the account | Warn counterparties; withhold pending messages; block new contact |
| SEO pages and sitemaps | Rendered listing page | Return **410** (gone), not a soft 404; drop from sitemaps |
| Advertising | Sponsored placement, retargeting audiences | Stop serving; stop billing |
| Payments | Open Safe Deal transactions, payouts | Hold or freeze per policy |
| Partner feeds and syndication | Copies sent to partners or price-comparison sites | Send deletion |
| Analytics | Event history | Mark as enforced; do not delete the evidence |

The pattern that works is the one [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) sets out for listing state changes: the decision service emits an **`EnforcementApplied`** event with the decision ID, target, action, scope and duration. Each consumer applies it idempotently and acknowledges it. A propagation monitor tracks the time from decision to the last acknowledgement for each consumer. When an appeal reverses the decision, an `EnforcementLifted` event restores the listing **and its ranking state**, because a reinstated listing buried on page nine has not really been reinstated.

The failure mode is **Ghost Inventory** caused by enforcement. Veldmark's ledger records one benign version. Femke's bike was marked sold at 18:10 on Monday 8 March and removed from search at 18:11, yet the evening alert digest still featured it the next morning. A sold bike in a digest wastes a buyer's time. A *fraudulent* listing in a digest, after the platform has decided to remove it, sends buyers to a scammer under the platform's own brand. Unpublish propagation for sold and expired listings is owned by [From Submitted to Searchable: The Publication Pipeline](#publication-pipeline). Enforcement should ride on the same mechanism, with a higher priority and a stricter time budget.

![Diagram: Enforcement as an event](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/fig04-enforcement-event-one-decision-fans-out.jpeg)

**Figure 4:** *Enforcement as an event. One decision fans out to every consumer that holds a copy of the account's listings or conversations, and each consumer acknowledges, so the platform can prove when the suspension actually took effect everywhere.*

The "warn 9 counterparties" step in Figure 4 is the target design, not what happened in March 2027. On that Sunday the suspension in Yardstick blocked the account from sending new messages, but the other sellers it had already contacted received no warning. Two of them found out the next day, from Femke's warning in a neighborhood chat group.

{id: trust-and-safety-architecture--intake-cases-and-appeals}
## Intake, Cases and Appeals

{id: trust-and-safety-architecture--notice-and-action}
### Notice and action

Detection is only one way violations arrive. Users report listings and messages, rights holders report counterfeits, authorities send orders, banks report accounts that received fraud proceeds, and since the DSA, **trusted flaggers** (organizations granted that status by a national Digital Services Coordinator) send notices that must be processed with priority.

Article 16 of the DSA requires an easy, electronic notice mechanism and lists what a notice should contain: an explanation, the exact location (URL), the notifier's name and e-mail address, and a statement of good faith. The platform must confirm receipt, decide "in a timely, diligent, non-arbitrary and objective manner", tell the notifier the outcome and disclose any use of automated means ([Regulation (EU) 2022/2065, Art. 16](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Article 22 adds the priority lane for trusted flaggers. The [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) chapter covers the legal detail. The architectural consequence is that **a notice is an entity with a lifecycle**, not an e-mail in a support inbox:

| Notice field | Why the architecture needs it |
| --- | --- |
| Notice ID, received timestamp, channel | Time-to-action metrics; confirmation of receipt |
| Notifier type (user, trusted flagger, rights holder, authority, bank) | Routing and priority; transparency counts by source |
| Target references (listing, message, account) | Case grouping |
| Claimed policy or legal ground | Routing to the right reviewer skill |
| Good-faith statement, notifier contact | Legal completeness; outcome communication |
| Status and decision link | Proves the notice was decided and how |

{id: trust-and-safety-architecture--case-management}
### Case management

Case management is where most T&S platforms either earn or lose their reviewers' productivity. The features that matter are ordinary: grouping related items into one case (all listings of a ring, all reports about one account), showing the evidence the detectors used, showing the actor's history across brands where the law permits, prefilled reason templates from the policy registry, service-level timers, and a second-review sample for quality control.

![Diagram: The lifecycle of a case](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/fig05-lifecycle-case-decided-enforced-are-separate.jpeg)

**Figure 5:** *The lifecycle of a case. "Decided" and "Enforced" are separate states because a decision that has not propagated is not yet in effect; an appeal produces a new decision linked to the original, never an edit of it.*

{id: trust-and-safety-architecture--appeals-and-redress}
### Appeals and redress

Article 20 of the DSA requires a free, electronic internal complaint system available for **at least six months** after a decision. Complaints must be handled in a timely, non-arbitrary way, unfounded decisions must be reversed, and decisions must be taken under the supervision of qualified staff, not solely by automated means ([Regulation (EU) 2022/2065, Art. 20](https://eur-lex.europa.eu/eli/reg/2022/2065/oj)). Users can then escalate to certified out-of-court dispute settlement bodies (Art. 21).

Three architectural rules follow:

1. **An appeal creates a new decision linked to the original.** Never overwrite the first decision. The overturn rate depends on keeping both.
2. **Evidence must outlive the complaint window.** The content snapshot, the rule and model versions and the reviewer identity must be retrievable for at least six months, and longer where out-of-court proceedings or litigation follow. Retention is set per data class, which [System of Record and Read Models: Listing Data Management](#listing-data-management) covers alongside erasure.
3. **Reversals are the best labels the platform gets.** A reversed automated decision is a confirmed false positive. Route reversals back to the policy owner and the model owner every week.

{id: trust-and-safety-architecture--statements-of-reasons-as-a-by-product-not-a-project}
### Statements of reasons as a by-product, not a project

Every restriction an EU platform imposes on a user's content or account needs a statement of reasons to that user (Art. 17), and every statement must be submitted, without personal data, to the Commission's DSA Transparency Database (Art. 24(5)). For the 180 days to 19 October 2026 it held about **4.4 billion** statements from 375 platforms, with **41%** of decisions fully automated ([DSA Transparency Database](https://transparency.dsa.ec.europa.eu/), accessed 19 October 2026).

At Tradeyard Netherlands, about 1.9% of new listings were removed for policy or fraud reasons in 2026. With roughly 1.05 million new Dutch listings a week, that is about **20,000 statements of reasons a week from listing removals alone**, before account suspensions and message decisions. Nobody writes those by hand. A platform that has a decision record with policy ID, ground, action, scope, automation flags and source can generate the statement mechanically. A platform without one builds five exporters, as Veldmark had. The [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) chapter follows Veldmark's statement-of-reasons pipeline in detail. The point here is that **the decision record is the upstream design**, and the regulatory output is a view of it.

{id: trust-and-safety-architecture--measuring-trust-and-safety}
## Measuring Trust and Safety

T&S teams are usually measured on activity: items reviewed, listings removed, queue age. Those numbers say how busy the team is. They do not say whether the marketplace is safe, and they can improve while the marketplace gets worse. A model that misses a new scam pattern reduces removals and queue sizes at the same time.

| Metric | Definition | What it tells you | How it misleads |
| --- | --- | --- | --- |
| **Prevalence** | Share of live listings (or delivered messages, or contacts) that violate a policy, estimated from a blind random sample | How much harm buyers actually meet | Needs enough samples per stratum; rare harms need large samples |
| **Exposure-weighted prevalence** | Prevalence weighted by views or contacts | Harm as experienced, not as stored | Hides harm in long-tail categories |
| **Time to action** | Time from first availability (or first report) to enforcement acknowledged by all consumers | Exposure window | Measuring to "decided" instead of "enforced" flatters it |
| **Precision** | Share of enforcement actions that were correct, from second review and appeals | Collateral damage to good users | Appeals undercount false positives: most wrongly blocked users give up |
| **Recall** | Share of violating items the pipeline caught, estimated from the random sample | Detection coverage | Cannot be measured without the sample |
| **Appeal overturn rate** | Reversed decisions as a share of appealed decisions, per policy and per detector | Fairness and model drift | Low appeal rates may mean an unreadable appeal flow, not good decisions |
| **Report rate** | User reports per 1,000 views or contacts | Visible harm and user trust | Falls when users give up reporting |
| **Reviewer agreement** | Agreement between two reviewers on the same item | Guideline clarity | Can be high for unclear policies if reviewers share habits |

Two practices make these numbers trustworthy. First, **compute them from decision records and samples, not from operational logs**, so that the same query produces the same figure for the DSA transparency report, the board and the model owner. Second, **report them per policy and per detector**. "Precision 96%" across all policies hides a phishing rule at 99.5% and a counterfeit rule at 70%.

{id: trust-and-safety-architecture--veldmark-s-numbers-before-and-after}
### Veldmark's numbers, before and after

Aisha's first measurement exercise, in April 2027, drew a blind sample of 4,000 live Tradeyard NL listings per week, stratified by 20 category groups. It found a prevalence of policy-violating listings of about **0.6%**, against the 0.2% the team had assumed from removal counts. Most of the gap sat in two places: phone-repair "services" posted as goods, and electronics listings with contact details hidden in images, which the text filters could not see.

![A busy activity dashboard showing 0.2% beside a magnifying glass over randomly sampled listings revealing 0.6% violations.](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/activity-versus-harm.jpeg)

**Figure 6:** *Removal counts suggested 0.2% of Tradeyard NL's live listings violated a policy; a blind random sample of live listings found about 0.6%, mostly in harms the detectors could not see.*

These weekly queue numbers set the shared platform's design targets:

| Quantity (Tradeyard, weekly) | 2026 baseline | Design target, end of 2028 |
| --- | --- | --- |
| New listings | 2.3 million | about 2.4 million |
| Automated decision rate | 94% | 96% |
| Listings to human review | about 138,000 | about 96,000 |
| Tradeyard moderators (in-house and outsourced) | 158 | about 120, with 15 more on sampling and appeals |
| Reviews per moderator per week | about 870 | about 800 |
| Median time to action on fraud reports | 3 h 10 min | under 30 min |
| Appeal overturn rate on automated removals | not measured | measured per policy, alert above 10% |

The design did not aim to remove moderators. It moved about **15 of them from grey-zone queues to sampling and appeals**, the two activities that produce the labels and the fairness evidence. Raising automation from 94% to 96% at constant precision was expected to come mostly from three sources: re-routing queues that almost always ended in the same outcome to rules, an OCR detector for contact details in images, and actor-level decisions that handle a ring as one case.

{id: trust-and-safety-architecture--in-practice-what-is-publicly-documented}
## In Practice: What Is Publicly Documented

**Classifieds companies publish very little about their T&S architecture**. What is public is enough to anchor the reference design, but not to describe any company's internals.

- **Shared moderation in a portfolio.** Adevinta's 2023 annual report, published in April 2024, says the central technology team's focus had historically been "on consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation" ([Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf)). Moderation was among the first capabilities a multi-country group chose to share. The report does not describe the architecture, and Adevinta's operating model changed after its 2024 take-private.
- **Shared moderation models.** In a March 2023 engineering post, Adevinta described a "Text in Image" OCR service run by a central team across its marketplaces. It detects insults, hidden messages, phone numbers, e-mail addresses and URLs inside ad images. The post reports volume growing from more than 100 million to 330 million requests a month ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/)). A shared detector with one API contract and many tenants is exactly the kind of component a group platform should own.
- **Real-time chat moderation.** OLX's January 2026 post describes real-time moderation of chat messages, a generative-AI image check that blocks suspicious images before delivery, and account bans "as they strike" ([OLX Group, 2026](https://www.olxgroup.com/?p=4590)). It gives no architecture and no human-review detail.
- **Rules as code, deployed in minutes.** Meta's 2015 post on Sigma describes a rule engine that evaluates policies on every interaction at more than a million requests per second, with policies written in Haskell and hot-swapped into production continuously ([Engineering at Meta, 2015](https://engineering.fb.com/2015/06/26/security/fighting-spam-with-haskell/)). The system is more than ten years old and has surely changed since, but the principle, that **a new rule should reach production in minutes, not with the next monolith deploy**, is exactly what Tradeyard Belgium lacked on 7 March.
- **Rule operations.** Stripe's Radar documentation describes backtesting rules on the past six months of data before activation, a 0% traffic allocation that runs a rule in shadow mode and reports what would have happened, gradual rollout, and an audit trail of who changed each rule ([Stripe Radar docs, n.d.](https://docs.stripe.com/radar/rules)). Payments are not classifieds, but rule lifecycle management transfers unchanged.

> **INFERENCE, NOT DOCUMENTED:** Public job postings for Adevinta-group companies in 2025–2026 mention a global fraud detection and moderation component deployed in several countries. That suggests a shared T&S platform serving multiple country marketplaces, but job postings describe intent, not production design. This book does not treat it as a documented architecture.

{id: trust-and-safety-architecture--one-platform-for-four-brands-what-to-share}
## One Platform for Four Brands: What to Share

Veldmark's principle for Common Ground is **share platforms, not products**. Trust and safety tests it hard, because some of T&S is pure machinery and some of it is local law, local fraud patterns and local language.

| Component | Share across the group? | Reasoning |
| --- | --- | --- |
| Decision service and decision record | **Share** | One schema for decisions makes appeals, DSA output and metrics uniform |
| Enforcement events and propagation monitor | **Share** | Rides on the group event backbone; every brand has the same consumer problem |
| Case management and reviewer tooling | **Share**, with per-brand queues and permissions | Tooling is expensive to build well; reviewers can move between brands |
| Evidence and audit store | **Share**, partitioned by brand and country | One retention engine, one place for regulators' and police requests |
| Statement-of-reasons service | **Share** | Same EU law, same database, same schema |
| Block lists and hash lists (phones, IBANs, devices, image hashes) | **Share where lawful**, with documented purpose and retention | Fraud rings cross brands; the Motorvane phone number is the proof |
| Rules engine runtime and rule lifecycle (backtest, shadow, rollout, audit) | **Share** | Machinery; rules themselves are per tenant |
| Policy registry | **Share the registry, localize the content** | Group baseline policies plus country and brand overlays |
| Image, OCR and text models | **Share base models**, fine-tune or threshold per brand | Language and category mix differ; the infrastructure need not |
| Vertical detectors (fake rentals, VIN reuse, discriminatory housing language) | **Local or vertical** | Only meaningful in one vertical |
| Thresholds and risk appetite | **Local**, within group guardrails | A bike marketplace and a rental portal tolerate different exposure |
| Reviewers and their language skills | **Local pools**, shared tooling | Policy judgement needs language and market context |

The table hides one hard constraint: **sharing signals across brands is a data protection question before it is an engineering one**. Lucía Ortega, Veldmark's Data Protection Officer, approved a shared block list of hashed phone numbers, e-mail addresses, IBANs and device identifiers for accounts terminated for fraud, with a documented fraud-prevention purpose (the GDPR recognizes fraud prevention as a legitimate interest), a two-year retention limit and a data protection impact assessment. She did not approve sharing raw message content or behavioral histories between brands. The architecture enforces that line: the shared store holds hashes and decision references, and per-brand stores hold content.

![Diagram: The tenancy split adopted for Common Ground](listing-systems-architecture/posts/24-trust-and-safety-architecture/assets/images/24-trust-and-safety-architecture/fig07-tenancy-split-adopted-common-ground-machinery.jpeg)

**Figure 7:** *The tenancy split adopted for Common Ground. The machinery is shared; policy overlays, vertical detectors and thresholds belong to each brand's tenant. Keybridge, a SaaS tool that does not publish listings to consumers itself, is not a tenant.*

Keybridge's absence is deliberate. It sends agencies' listings to many portals, including Hearthly's competitors, and Veldmark committed in March 2027 not to use Keybridge agency data for Hearthly's advantage. A moderation decision on a Keybridge-originated listing at Hearthly is Hearthly's decision about Hearthly's copy. It is not shared back into Keybridge, and Keybridge does not consume the block lists. The [After the Deal: Consolidating Platforms After Acquisitions](#platform-consolidation) chapter discusses why neutral SaaS businesses inside a marketplace group need explicit data boundaries.

{id: trust-and-safety-architecture--trade-offs}
## Trade-offs

{id: trust-and-safety-architecture--where-to-build-trust-and-safety}
### Where to build trust and safety

| Option | Strengths | Weaknesses | Right when |
| --- | --- | --- | --- |
| **Per-brand stacks** | Local fit; no coordination; fast local decisions | Signals do not cross brands; tooling built four times; DSA output inconsistent | Brands are genuinely unrelated, or the group expects to sell them soon |
| **Shared platform, local policy** (Veldmark's choice) | Shared machinery and evidence; signals cross brands where lawful; one regulatory output | Platform team becomes a bottleneck if overlays are hard; migration cost | A group with several brands under the same law and overlapping fraud |
| **Fully central T&S** (one policy, one team, one queue) | Consistency; scale economies in review | Local law and language suffer; brands lose control of their customer experience | Brands share one product and one market |
| **Vendor platform** (T&S software and outsourced review) | Speed to start; mature tooling; elastic review capacity | Policy knowledge sits with the vendor; signals and labels may not be portable; data protection reviews per vendor | Early-stage marketplaces, or as the review workforce under a group-owned decision record |

A vendor can supply review capacity, but not the records the platform learns from. Outsourced review is normal in the industry, and Veldmark keeps its two review vendors. What it does not outsource is the **decision record, the policy registry and the labels**. A platform whose labels live in a vendor's system cannot retrain its own models or switch vendors without losing its history.

{id: trust-and-safety-architecture--where-to-put-human-judgement}
### Where to put human judgement

| Choice | Benefit | Cost |
| --- | --- | --- |
| More pre-moderation | Less exposure to harm | Slower publication, which costs liquidity, especially for private sellers |
| More automation | Speed, consistency, lower cost per decision | False positives at scale; needs sampling and appeals to stay honest |
| LLMs in the grey zone | Fast policy iteration; better explanations | Cost, latency, adversarial prompts; cannot decide appeals |
| More sampling | Honest prevalence and recall | Reviewer time spent on mostly clean items |

Moderation costs liquidity. Every minute a listing waits is a minute it cannot be found, and the [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects) chapter shows why the first hours of a listing's life matter most. The answer is not a single mode but **risk tiers with explicit time budgets per tier**, reviewed with the marketplace general managers who carry the liquidity targets.

{id: trust-and-safety-architecture--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Main harms | Payment-link phishing, advance-payment scams, counterfeit, prohibited items | Fake rentals with stolen photos, deposit fraud, discriminatory ads | Deposit scams, cloned listings, VIN reuse, mileage misstatement | Fake job offers, money-mule recruitment, data harvesting |
| Supply mix | Mostly private sellers, high volume | Mostly agencies via feeds | Mostly dealers via feeds | Employers and agencies |
| Natural control point | The listing and the message | The lister's identity (agency checks) | The dealer contract and the vehicle identity | The employer's identity |
| Pre-moderation tolerance | Low: sellers expect instant publication | Medium: agency feeds tolerate minutes | Medium | Medium |
| Vertical-specific policy | Product safety, recalls | Energy-class disclosure, fair housing rules | Vehicle disclosure, odometer | Pay transparency, discrimination |
| Typical detector | Brand in URL, keyword, image OCR | Duplicate and stolen-photo search, rent anomaly | VIN decoding, price vs. market value | Contact-detail extraction, salary anomaly |

The table explains why a group platform must allow **vertical detectors and vertical policies** as first-class tenant content. Hearthly's most important detector, stolen-photo matching against existing listings, is close to irrelevant for Tradeyard's second-hand clothes. Motorvane's most important control is not a detector at all. It is dealer verification at onboarding, which [Who Is on the Other Side? Identity and Verification](#identity-and-verification) covers.

{id: trust-and-safety-architecture--failure-modes}
## Failure Modes

1. **Moderation only at creation.** Edits, price changes and new photos are not re-scored, so scammers publish a clean listing and change it afterwards. The Which? test is the public proof.
2. **Several deciders.** The insertion service, the ranking service and the messaging service each enforce their own idea of "suspicious". Their decisions contradict each other, and none of them emits a statement of reasons.
3. **Decided but not enforced.** The decision is recorded, but alerts, recommendations, SEO pages or partner feeds keep the listing. Nobody measures propagation, so nobody notices.
4. **Policies in code.** A rule's intent lives only in a regular expression in a service written six years ago. When law changes, nobody can find all the places to change.
5. **Rules that deploy with the monolith.** A rule written at 20:30 on a Sunday reaches the second country on Wednesday. Fraud adapts in hours.
6. **No random sample.** Precision is estimated from appeals and recall not at all. A model that misses a new scam pattern looks better every week.
7. **Appeals as support tickets.** Complaints are not linked to decisions, reversals do not restore ranking, and overturns are never fed back to model owners.
8. **Labels owned by the vendor.** The review vendor's tool holds the history. Switching vendors, or training a new model, starts from zero.
9. **Silent demotion.** Ranking pushes suspected scams down without a decision record, which is both a DSA problem and an unexplainable experience for sellers who are wrongly affected.
10. **Badges that outlive the account's integrity.** A verified badge stays on an account after it is taken over, and makes the takeover more effective. [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) covers the detection side.

{id: trust-and-safety-architecture--the-chief-architect-s-view}
## The Chief Architect's View

Trust and safety is one of the few capabilities where **sharing pays from the first year**, because fraud rings cross brands and the EU legal regime is the same for all of them. It is also one where centralizing too much destroys value, because policy judgement depends on language, market and vertical. The decisions I would make, and who should make them:

| Decision | Who decides | What to watch |
| --- | --- | --- |
| The decision record schema and the rule that the decision service is the only writer | Chief Architect, with the T&S lead and the DPO | Any service that restricts content without a decision record |
| The enforcement event contract and propagation targets per consumer | Chief Architect and the event platform owner | Propagation time per consumer, p95 and worst case |
| Group baseline policies and the overlay mechanism | Group T&S lead, legal, country policy owners | Number of overlays per policy; policies with no detector or no reviewer guideline |
| What signals may cross brands | DPO, with the T&S lead | Purpose, retention and access logs for shared lists |
| Risk tiers and time budgets per tier | Marketplace GMs with the T&S lead | Publication time vs. prevalence per tier |
| Automation thresholds | Policy owner and model owner jointly | Overturn rate and sampled precision per policy |
| Review vendors and their scope | T&S lead and procurement | Label portability; vendor access to evidence |

Three long-term trends belong on the architecture roadmap.

- **T&S is a consumer of everything.** It needs listing events, message events, login events, payment events and media events. A group without a reliable event backbone cannot build a shared T&S platform, which is why Veldmark's backbone (July 2027) came before its shared T&S platform (November 2027).
- **Regulation will keep adding outputs, not inputs.** The DSA, the UK Online Safety Act and successors mostly ask for evidence, notices and reports derived from decisions. A platform built around a clean decision record absorbs new regulation as new views. One built around queues absorbs it as new projects.
- **Adversaries learn the platform.** Detection thresholds, rule logic and model features must not leak through rejection messages. A statement of reasons must give the ground and the facts. It does not need to disclose the threshold.

The metric I would put in front of the board is not removals. It is **sampled prevalence of fraudulent listings, by brand, with its trend**, next to time to action on fraud reports. Those two numbers say whether buyers can trust what they see, and how long they are exposed when they cannot.

{id: trust-and-safety-architecture--questions-to-ask}
## Questions to Ask

1. Which component writes moderation decisions, and how many other services restrict content without going through it?
2. When a listing is removed, which consumers apply the removal, how do we know they did, and what is the p95 time until the last one acknowledges?
3. Are edits, price changes, photo changes and contact-detail changes re-scored as new submissions?
4. Where are our policies written down, how are they versioned, and can every decision cite the policy version it applied?
5. What is our prevalence of policy-violating listings from a blind random sample, per category, and how has it moved this quarter?
6. What is the appeal overturn rate per policy and per detector, and who receives the reversals?
7. How long does a new rule take to reach production in every country, and can it run in shadow mode first?
8. Which signals do we share across brands, under what legal basis and retention, and who audits access?
9. Does ranking demote listings for trust reasons, and if so, does each demotion produce a decision record and a statement of reasons?
10. If we changed our review vendor tomorrow, would we keep our labels, guidelines and case history?

{id: trust-and-safety-architecture--from-platform-to-adversary}
## From Platform to Adversary

This chapter built the machinery: policies, detection, one decision service, enforcement that reaches every consumer, cases, appeals and metrics. It deliberately treated detection as a slot that detectors plug into. The most demanding detectors are those aimed at people who study the platform and adapt to it within days: phishing crews, fake-rental rings and account-takeover operations. [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention) takes up that adversary, with risk scoring, the signals that expose organized fraud, step-up friction, and Veldmark's encounter with a fake-rental ring in Barcelona.

{id: trust-and-safety-architecture--sources-and-evidence}
## Sources and Evidence

{id: trust-and-safety-architecture--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Adevinta Annual Report 2023](https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2024/04/26/616971_Adevinta%20AR%202023.pdf) — Adevinta, 2024. Chat and moderation among the first capabilities consolidated across marketplaces.
- [Text in Image 2.0: improving OCR service with PaddleOCR](https://adevinta.com/techblog/text-in-image-2-0-improving-ocr-service-with-paddleocr/) — Adevinta Tech Blog, 2023. A shared OCR moderation service across marketplaces; volumes.
- [We fight online fraud with the power of AI](https://www.olxgroup.com/?p=4590) — OLX Group, 2026. Real-time chat moderation and image blocking before delivery.
- [Fighting spam with Haskell](https://engineering.fb.com/2015/06/26/security/fighting-spam-with-haskell/) — Engineering at Meta, 2015. Sigma rule engine; rules as code deployed continuously.
- [Fraud prevention rules (Radar)](https://docs.stripe.com/radar/rules) — Stripe, n.d. (current documentation). Backtesting, shadow mode, rollout, rule audit trail, review-queue guidance.

{id: trust-and-safety-architecture--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065 (Digital Services Act)](https://eur-lex.europa.eu/eli/reg/2022/2065/oj) — Official Journal, 2022. Arts. 16, 17, 20, 21, 22 and 24: notice and action, statements of reasons (including demotion), internal complaints, trusted flaggers, transparency; quotations checked against the Official Journal text retrieved through the EU Publications Office.
- [DSA Transparency Database](https://transparency.dsa.ec.europa.eu/) — European Commission, rolling statistics accessed 19 October 2026. Volume and automation share of statements of reasons.
- [DSA Transparency Database API documentation](https://transparency.dsa.ec.europa.eu/page/api-documentation) — European Commission, n.d. Decision fields including `DECISION_VISIBILITY_CONTENT_DEMOTED`.
- [Fraudulent advertising and account integrity: expert insights on best practice](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf) — Integrity Institute for Ofcom, 2026. Enforcement ladder, random sampling for prevalence.

{id: trust-and-safety-architecture--research-and-practitioner-sources}
### Research and practitioner sources

- [Scam ads slipping through the net too easily on second-hand marketplaces](https://www.which.co.uk/policy-and-insight/article/scam-ads-slipping-through-the-net-too-easily-on-second-hand-marketplaces-which-warns-aqyF66m1TlU1) — Which?, 2024. Edited scam ads passing review in minutes.
- [Leboncoin a prétendu à tort qu'il relisait toutes les annonces](https://www.clubic.com/leboncoin/actualite-789848-leboncoin-condamnation.html) — Clubic, 2015. Court finding on misleading pre-moderation claims; hosting status.
- [Llama Guard: LLM-based input-output safeguard for human-AI conversations](https://arxiv.org/abs/2312.06674) — Inan et al., arXiv, 2023. Policy taxonomy supplied as a prompt.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
