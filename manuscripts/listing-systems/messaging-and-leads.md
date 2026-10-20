{id: messaging-and-leads}
# 28. From Interest to Contact: Messaging and Lead Management

![From Interest to Contact: Messaging and Lead Management — logo](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Take apart the moment a buyer contacts a seller: the contact channels, the conversation service that carries messages, the safety checks that sit on the delivery path, and the lead object that carries a buyer's interest into a dealer's or agency's CRM. You will follow a Rotterdam city bike's fourteen conversations and an Essen Volkswagen Golf's twenty-three leads through each component.

> **WHY THE BUSINESS CARES:** A contact is the first point at which a marketplace produces something a seller can feel. Private sellers judge the platform by whether the messages they receive are real; professionals renew their packages based on how many leads they received, how good those leads were, and whether the portal's count matches their own. Both judgements are made in this part of the system.

> **WHY ARCHITECTS SHOULD CARE:** Messaging is the busiest write path most listing platforms run, the channel where most scams close, and a store of private correspondence that data-protection law treats with suspicion. Lead delivery is an integration with hundreds of external systems the platform does not control. Getting either wrong shows up as fraud losses, billing disputes and churn, not as an outage.

> **KEY POINTS:**
>
> * **A conversation and a lead are two objects, not one.** The conversation is a private exchange between two parties about a listing, held by the platform and governed by privacy and safety rules. The lead is a commercial record of a buyer's interest, delivered to a professional, counted, billed and later matched to an outcome. Platforms that use the chat store as their lead database, or the CRM e-mail as their only lead record, cannot prove, bill or delete either.
> * **Safety checks belong on the delivery path.** Scams close in conversations, often within minutes of first contact. A synchronous gate with a fixed latency budget (links, domain age, payment details, contact details, images and QR codes) decides before the recipient sees the message; slower conversation-level scoring can still withdraw messages and warn recipients afterwards. OLX's 2026 description of blocking fraudulent chat images in real time is the documented direction.
> * **Lead routing is a contract with the professional's systems, and lead value is proven downstream.** Leads must reach the right branch or dealer within minutes, exactly once, with consent and an identifier both sides can reconcile. Their value can be measured only with outcome data the portal does not own (a dealer sale, an agency mandate, a closed deal), so the attribution feedback loop has to be designed in from the start.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Scam Inbox** — a messaging service built for delivery speed alone, with safety checks running after delivery or only on reports, becomes the place where payment-link phishing and deposit scams succeed.
> * **Vanity Liquidity** — counting messages and form submissions instead of qualified, deduplicated leads that reach a professional's workflow sells exposure that professionals cannot convert, and renewals fail.
> * **Ghost Inventory** — contact buttons, saved conversations and lead forms that stay live after a listing is sold keep producing contacts that nobody can satisfy, and charge professionals for them.

Search, ranking and alerts exist to produce one event: a buyer deciding to contact a seller. That event is the marketplace's unit of output. Everything earlier in the funnel is preparation, and almost everything later (the viewing, the test drive, the payment, the handover) happens partly or wholly outside the platform. **The contact is the last moment the marketplace can see both parties at once**, and the last moment it can protect either of them.

Two very different systems meet at that moment. For private sellers, the contact is a **conversation**: a buyer and a seller exchanging messages about a bike, a sofa or a flat. For professional sellers, the same contact is a **lead**: a commercial record that a dealer or agency expects to receive in its own software, act on within minutes, and count when the renewal invoice arrives. Most platforms start with one of these and bolt the other on. General classifieds start with chat and later discover that dealers want leads in their CRM. Vertical portals start with e-mail leads and later discover that buyers want chat, and that the chat is where the fraud is.

This chapter treats both as first-class, and it opens Part VI because the contact is the first thing the marketplace can count and charge for. The lead it defines is the unit that [How Listing Marketplaces Make Money](#monetization-models) prices and [Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements) bills; the offer agreed in a conversation is where [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments) begins. It owns the terms **lead**, **conversation** and **lead routing**. It builds on Part V without re-teaching it: fraud detection belongs to [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention), and the moderation pipeline and enforcement actions to [Trust and Safety as a Platform](#trust-and-safety-architecture); this chapter shows where they attach to the contact path. The professional's side of the screen, the lead inbox and CRM tooling, belongs to [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling).

{id: messaging-and-leads--setting-the-scene-at-veldmark-fourteen-conversations-and-twenty-three-leads}
## Setting the Scene at Veldmark: Fourteen Conversations and Twenty-Three Leads

Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)), ran four contact systems in early 2027. Two cases from that spring set the agenda for the group's messaging work.

**The Rotterdam city bike.** On Sunday **7 March 2027** at 19:42 CET, Femke listed a used city bike on Tradeyard Netherlands for **€240**. It became searchable at 19:48 and matched **312** saved searches. The first message arrived at **19:55**. By the next evening Femke had **14** conversations. At **20:11** on Sunday, one "buyer" sent a message with a link to a fake Tradeyard Safe Deal payment page: "I paid via Safe Deal, confirm here to receive the money." The message was delivered. Tradeyard's messaging checks compared links against a deny list, and the link's domain had been registered that afternoon, so it was on no list. Femke recognized the trick and reported the message at **20:19**. The account was suspended at **20:26**, and a rule written that evening withheld **37** similar messages to other sellers. The bike sold on Monday 8 March for **€225** via Safe Deal "pay at pickup".

When Ingrid Halvorsen, the Group Chief Architect, reviewed the case with Aisha Rahman, the Group Head of Trust & Safety, the seven minutes from report to suspension were not the problem. The problem was the sixteen minutes from first contact to phishing link, and the fact that the safety check ran in the wrong place: after the message had been stored and pushed to Femke's phone. The suspended account had already reached nine other sellers before Femke's report, and none of them was warned (the enforcement side is in [Trust and Safety as a Platform](#trust-and-safety-architecture)).

**The Essen Volkswagen Golf.** On Wednesday **14 April 2027**, the dealer Autohaus Ruhrblick published a 2021 Volkswagen Golf on Motorvane Germany at **€21,900** through its dealer management system (DMS) feed. In ten days the listing produced **23 raw leads**: **14 e-mail enquiries**, **7 phone calls** and **2 test-drive bookings**. The car sold on Thursday 29 April. At the dealer's quarterly review, Autohaus Ruhrblick's sales manager put a different number on the table: the dealership's CRM showed **14** leads from Motorvane for the car. The nine missing were the seven phone calls and the two test-drive bookings. Motorvane recorded calls and bookings in Dealer Hub, its dealer portal, but exported only e-mail enquiries into the dealer's CRM. And the dealer's sales team was sure two of the fourteen were the same person. Neither side was wrong. They were counting different things in different systems, with no shared lead identifier.

The gap mattered beyond one car, because Motorvane was about to charge per lead. It earns **€40 million** a year from leads and financing referrals, and its monetization team was proposing a per-lead charge above a monthly allowance in dealer packages (see [How Listing Marketplaces Make Money](#monetization-models)). A per-lead charge on a number the dealer cannot reconcile is a dispute generator.

Ingrid took two questions to the architecture advice forum in May 2027: **where should safety checks sit in a message's life, and what is a lead, as an object both Veldmark and a dealer can count?**

{id: messaging-and-leads--concepts-contact-conversation-lead}
## Concepts: Contact, Conversation, Lead

The industry uses these terms loosely; this book uses the definitions below.

- A **contact** is any action by which a buyer reaches a seller about a listing: a chat message, an e-mail form, a phone call, a callback request, a booking, an application. A contact is an event.
- A **conversation** is the platform-held thread of messages between a fixed set of participants about one listing (occasionally several). It has participants, messages, attachments, read state and safety state. This chapter owns the term.
- A **message** is one immutable unit of content within a conversation, plus mutable metadata: delivery state, read receipts, safety verdicts, redactions.
- A **lead** is a record that a specific prospective buyer expressed interest in a specific professional's listing or service, created by a defined rule, delivered to that professional, and tracked to an outcome. A lead has an identifier, a source channel, a timestamp, consented contact data, qualification data, a delivery history and, eventually, a disposition. This chapter owns the term.
- **Lead routing** is the decision of which professional entity (dealer, rooftop, agency branch, individual agent) receives a lead, through which delivery channel, and with what service-level expectation. This chapter owns the term.
- A **connection** is the term some portals use for a counted contact. CarGurus' FY2025 10-K defines connections as "interactions between consumers and dealers on our marketplace through phone calls, email, managed text and chat, and clicks to access the dealer's website or map directions to the dealership" ([CarGurus, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)). Zillow's 10-K describes Premier Agent as the delivery of "validated customer connections, or leads" ([Zillow, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). The published definitions differ: a click on directions counts as a connection at one portal and would not be a lead at most others. Always ask which definition a number uses.
- **Disintermediation** is buyers and sellers moving off the platform once they have met, to avoid fees or friction. It is defined in [Liquidity Is the Product: Network Effects, Local Markets and Marketplace Metrics](#liquidity-and-network-effects). For classifieds, some disintermediation is the business model; for transactional and pay-per-lead models, it is revenue leakage.

The central distinction is between the conversation and the lead: they often begin with the same click, but almost every property differs.

| Property | Conversation | Lead |
| --- | --- | --- |
| Purpose | Let two parties talk safely | Give a professional a buyer to act on, and count it |
| Primary owner of the data | The platform (controller for the messaging service) | Shared: the platform creates it; the professional receives a copy and becomes responsible for its use (legal view needed per market) |
| Lifecycle | Open, active, dormant, closed, deleted | Created, delivered, acknowledged, responded, qualified, outcome, disputed |
| Identity of the record | Thread ID, stable for the conversation's life | Lead ID, stable across every system that receives it |
| What counts | Messages delivered, reply rate, time to first reply | Leads delivered, deduplicated, qualified, converted |
| Retention driver | Data minimization; safety evidence | Contract, billing, attribution, the professional's own obligations |
| Main risk | Fraud, harassment, privacy | Disputes, double counting, misrouting, consent |
| Monetization link | Indirect (liquidity, trust) | Direct (pay per lead, share of voice, pay at close, ROI for renewals) |

**A lead is created from a contact by a rule**, and that rule is a business decision encoded in software. Typical rules: the first message from a buyer in a new conversation with a professional creates a lead, later messages do not; a phone call creates a lead only if it connects and lasts longer than a threshold; a booking always creates a lead; repeated contacts from the same buyer about the same listing within a window update the existing lead instead of creating a new one. Each rule changes the number a professional will see on an invoice or ROI report, so the rules need an owner and a version, like a pricing rule.

![One buyer contact forking into a private, safety-guarded conversation and a counted, delivered lead record.](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/one-click-two-objects.jpeg)

**Figure 1:** *One click, two objects: the conversation is private correspondence held under safety and privacy rules, while the lead is a commercial record, created by a versioned rule, that the professional receives and that is counted and billed.*

{id: messaging-and-leads--contact-channels-what-the-platform-sees}
## Contact Channels: What the Platform Sees

Each way a buyer may reach a seller gives the platform a different view of the exchange, a different lever for safety, and a different quality of attribution.

| Channel | What the platform sees | Safety leverage | Attribution quality | Typical fit |
| --- | --- | --- | --- | --- |
| **In-app chat** (platform-held conversation) | Every message, attachment and reply time | Highest: can check, warn, withhold and withdraw messages | High: every contact and reply is an event | General classifieds; private sellers; increasingly professionals |
| **E-mail form or e-mail relay** | The first message; replies only if relayed through platform addresses | Medium on the first message; low afterwards unless relayed | Medium: first contact is counted, follow-up is not | Real estate and automotive enquiries to professionals |
| **Visible phone number** | Only that the number was revealed | Low: can rate-limit reveals | Low: a reveal is not a call | Professionals, legacy listings |
| **Masked or tracked phone number** | That a call happened, its duration, sometimes a recording | Medium: can block numbers, cap calls from new accounts | High for calls; the strongest signal of intent in automotive | Dealers, agencies; private sellers who want privacy |
| **Callback or contact request** | The request and consented contact data | Medium | High | Professionals with sales teams |
| **Booking** (viewing, test drive, appointment) | The slot, the parties, confirmations and no-shows | Medium: identity and history of both sides | Very high: a booking is close to a deal | Real estate, automotive, local services |
| **Offer or reservation in conversation** | Price agreement, sometimes a deposit or payment | High, if the payment stays on-platform | Very high | Recommerce with payments; automotive reservations |
| **Application** (rental dossier, job application) | Applicant documents and profile | High for documents; fraud via fake landlords persists | High | Rentals, jobs |

Three observations follow from the table.

First, **every channel the platform cannot see is a channel it cannot protect.** Fraud prevention in classifieds is mostly pre-payment: the platform usually does not see the payment, so the conversation is its last chance to intervene (the threat model is in [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). Moving contact off the platform, through visible phone numbers or unrelayed e-mail, removes that chance.

Second, **channels with more friction produce better leads.** A booking or reservation carries more intent than a chat message. Autotrader's FY26 results report **137,000** deals with a full reservation placed through its Deal Builder product (49,000 the year before), which it calls "the very best enquiries in terms of conversion to sale"; it states that Deal Builder enquiries "convert at double the rate into sales" ([Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)). The same document shows the cost of pushing a channel too fast: Autotrader attributed part of a fall in retailer numbers to "concerns with the speed and nature of our Deal Builder product roll-out".

Third, **channels evolve away from what the platform cannot attribute.** Rightmove's Real Time Datafeed specification, the API through which UK agency software exchanges data with Rightmove, records in its change log that version 1.3.6 (April 2021) removed the `GetBranchPhoneLeads` and `GetBrandPhoneLeads` calls, leaving e-mail lead exports ([Rightmove RTDF v1.4.1, 2023](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)). The specification does not say why; the general point is that whatever a portal cannot deliver into the professional's system, it reports only in its own dashboards, where it is easy to dispute.

{id: messaging-and-leads--architecture-the-contact-path}
## Architecture: The Contact Path

The contact path has eight components of its own, listed in the table below. Figure 2 shows the reference architecture Veldmark adopted; it is not a description of any real company's systems.

![Diagram: The contact path at Veldmark](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/fig02-contact-path-veldmark-contact-policy-decides.jpeg)

**Figure 2:** *The contact path at Veldmark. Contact policy decides who may reach whom and how; the conversation service owns messages and calls the safety gate before delivery; the lead service derives leads from conversations, calls and bookings; routing delivers leads to professionals' systems and brings their outcomes back. Only the conversation service stores message content.*

What each component owns, and what it must not own:

| Component | Responsibility | Owns | Does not own |
| --- | --- | --- | --- |
| **Contact policy service** | Decides whether this user may contact this seller about this listing now, through which channels, and with what friction (verification step, rate limit, masked number) | Contact eligibility rules per country, category and seller type; rate limits | Identity levels ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)); risk scores ([Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)) |
| **Conversation service** | Creates conversations, accepts and stores messages, orders them, tracks delivery and read state, enforces retention | Message content, threads, participants, attachments references | Push infrastructure; moderation policy |
| **Message safety gate** | Synchronous verdict per message within a latency budget | The call contract and the verdict vocabulary | Policies and detectors (the T&S platform) |
| **Real-time gateway** | Holds connections to online clients; fans out to devices; falls back to push and e-mail | Connection state, device registry | Message storage |
| **Call tracking** | Allocates tracked numbers, connects calls, records duration and outcome | Number pools, call records | Lead rules |
| **Booking service** | Slots, confirmations, reminders, no-shows | Appointments | Calendars inside dealer or agency software |
| **Lead service** | Applies lead-creation rules, deduplicates, qualifies and enriches leads | The lead object, its state machine and its store (the lead ledger in [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)) | Billing ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)) |
| **Lead routing and delivery** | Chooses the recipient and delivers through the professional's channel; ingests acknowledgements and outcomes | Routing rules, delivery adapters, delivery log | The professional's CRM |

Contact policy is where friction for new accounts lives. Experts interviewed for an Ofcom-commissioned report in 2026 recommend "creating delays between creating an account and reaching a large audience" ([Integrity Institute for Ofcom, 2026](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf)); for messaging, that means capping how many sellers a new account may contact per hour and masking contact details until the account has history.

Two boundaries cause most of the trouble when they are blurred.

**The listing is referenced, not copied.** A conversation refers to a listing by its identifier and keeps a small snapshot (title, price, first image) for display, because the listing will change and eventually disappear. When the listing is sold, removed or expired, the listing events from [Every Change Is an Event: Event-Driven Listing Architecture](#event-driven-listings) must reach the contact path: the contact button must close, open conversations must show the new state, and the lead service must stop creating leads. The city bike's "marked sold at 18:10" on Monday should close new contact within seconds. A platform that checks listing state only when rendering the listing page will keep accepting messages from the conversation screen, where the button is cached: Ghost Inventory in the inbox.

**Only one component stores message content.** Leads carry the buyer's first message and consented contact details, because the professional needs them. They do not carry the whole conversation, and analytics events carry neither. Every additional copy of message text is a copy that has to be found, secured and deleted. The data platform should receive message *events* (sent, delivered, replied, withheld, reported) with identifiers and timings, not content; [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) owns the tracking plan.

{id: messaging-and-leads--storing-conversations}
### Storing conversations

A conversation store has a simple access pattern and a demanding volume. Users read their own inbox, newest first, and open one thread at a time. Writes are small and frequent; messages are immutable in content but their metadata changes (delivered, read, withheld, redacted).

Even "immutable" messages carry metadata that changes, and that shapes the store. In a **2021** engineering post, OLX described storing chat on Cassandra: "At OLX chat we need to save the user chats for a long time." Because users "can log in from multiple frontend clients", history must be held on the server, and the data is partitioned by user, since "each user only needs his data". The post describes separate tables for chats and for threads ("where we store the state of a conversation"), and explains why the team moved from a time-window compaction strategy to leveled compaction: messages are not immutable, because "additional states have to be associated with the messages", so updates spread across files and slowed reads ([OLX, 2021](https://tech.olx.com/cassandra-compaction-trade-offs-848ba51c64c0)). The post is more than three years old and the current state of OLX chat is not public, but the lesson about mutable metadata on "immutable" messages is general.

Outside marketplaces, Discord's **2023** account of storing "trillions of messages" is the most detailed public description of the problem at scale. Messages are partitioned by channel plus a fixed time bucket, identifiers are time-sortable, and the hard problem was **hot partitions**: busy channels concentrating reads on a few nodes. Discord added a data-service layer that coalesces identical concurrent requests and routes by channel, and moved from 177 Cassandra nodes to 72 ScyllaDB nodes, with p99 historical-fetch latency falling from 40–125 ms to 15 ms ([Discord, 2023](https://discord.com/blog/how-discord-stores-trillions-of-messages)).

For a listing marketplace the hot partition is not a busy thread; threads are short. It is the **busy inbox**: a dealer with hundreds of open conversations, an agency branch receiving every enquiry for a popular new-build development, a private seller whose underpriced phone attracts eighty messages in an hour. The reference design I recommend:

- Partition **messages by conversation**, with a time-sortable message ID, so a thread is one partition read.
- Keep a separate **inbox index per participant** (conversation ID, last message time, unread count, listing snapshot), partitioned by participant and bucketed by time, so a dealer's inbox is a bounded read rather than a scan.
- Treat **professional inboxes as a different product**: paginated, filterable by listing and status, and fed to the lead service rather than read by people one thread at a time.
- Give every client-submitted message an **idempotency key**, because mobile clients retry; a duplicated "Is it still available?" is harmless, a duplicated offer is not.
- Store **attachments** through the media pipeline ([Photos Sell: Media Pipelines for Listings](#media-pipeline)) as references, never inline, so they get the same scanning, resizing and deletion as listing images.

{id: messaging-and-leads--delivering-in-real-time}
### Delivering in real time

Delivery has three tiers: an open connection to a client that is online (typically WebSockets through a gateway), a push notification to devices that are not, and an e-mail fallback for users who have neither the app nor an open session. The conversation service should not know which tier was used; it records delivery state as reported by the gateway.

Delivery speed earns money. A buyer who gets an answer in minutes is far more likely to stay than one who gets it the next day; a seller's response time is one of the most useful quality signals a marketplace has, and several portals expose it as a badge or ranking input (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)). But **speed and safety pull against each other on exactly one step: the moment between "stored" and "shown"**. Figure 3 shows how Veldmark resolved it.

![Diagram: A message's life with the safety gate on the delivery path](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/fig03-message-s-life-safety-gate-delivery.jpeg)

**Figure 3:** *A message's life with the safety gate on the delivery path. The synchronous check decides before the recipient sees anything; asynchronous detectors can still withdraw a delivered message and warn the recipient. The sender of a withheld message is not told it was withheld, so the check does not become a free testing tool for fraudsters.*

{id: messaging-and-leads--safety-on-the-delivery-path}
## Safety on the Delivery Path

The moderation pipeline, with its synchronous gate and asynchronous detectors, is described in [Trust and Safety as a Platform](#trust-and-safety-architecture), and the fraud signals in [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention); this section covers only what is specific to messages.

**Why the gate must sit before delivery.** The scam scripts that matter in classifieds close in the conversation. A fake buyer sends a seller a link to a counterfeit "payment received" page that harvests card details; a fake seller asks for a deposit by bank transfer; a fake landlord asks for money before a viewing. Once a phishing link is on the seller's screen, the platform depends on the seller's judgement.

Large classifieds operators are moving the decision earlier. In a **2026** post, OLX described a "Chat Images GenAI" system that detects and blocks suspicious images in chat in real time, live in Poland, Portugal, Bulgaria, Romania and other countries; it reports that in Poland "fraudulent images make up about 30% of fraud cases", and that its detection of fraudulent QR codes in chat, which can lead to card-harvesting pages, runs at "80% precision" ([OLX Group, 2026](https://www.olxgroup.com/?p=4590)). An earlier pattern, reported for OLX South Africa in **2018**, was **warn-in-context**: payment keywords and attempts to move a conversation to e-mail or WhatsApp triggered safety tips, and users chatting with a flagged account received an alert ([ITWeb, 2018](https://www.itweb.co.za/article/olx-blocks-scammers-using-advanced-algorithms/nWJadvb8APOMbjO1)); that system is eight years old and certainly replaced, but the pattern is current. Kleinanzeigen's safety page warns users that "Kleinanzeigen" messages inside the chat can be written by the chat partner ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicherheitshinweise/)), which is why a platform's own brand inside a message is itself a risk signal.

**What the gate can afford.** The gate runs on every message, so it must be deterministic, cheap and bounded: Veldmark set a budget of **150 ms at p99**, with a fail-open rule for low-risk conversations and fail-closed for messages containing links or payment details from accounts less than 24 hours old. The checks that fit the budget:

| Check | What it catches | Typical verdict |
| --- | --- | --- |
| URL extraction, allow and deny lists | Known phishing and payment-lookalike domains | Block or withhold |
| **Domain age** and registration data | Phishing domains registered hours before use (the city bike case) | Withhold if young and the message mentions payment or the platform brand |
| Platform brand in a link or text from a counterparty | Impersonation of Safe Deal, shipping or support | Withhold or warn |
| IBAN, phone, e-mail and messaging-app handles | Moving payment or conversation off-platform | Warn the recipient; mask for new accounts |
| Image hashes and QR decoding | Known fake payment screenshots; QR codes pointing to phishing pages | Block or withhold |
| Velocity per sender | One account sending the same text to many sellers | Throttle, withhold |
| Counterparty and listing risk | Messages from high-risk accounts, or about high-risk listings | Warn, withhold |

Slower checks, such as conversation-level text models, large language model (LLM) classifiers on the uncertain band, graph features linking accounts, and image models, run **asynchronously** on message events. Their outputs can withdraw a delivered message, replace it with a safety notice, warn every counterparty of the sender, and feed account-level enforcement. Using LLMs only on the uncertain band is a cost decision: at Veldmark's volume of about **14 million messages a day**, sending every message to an LLM would cost more than the fraud it prevents, while sending the 1–2% the cheap classifier is unsure about is affordable.

**The verdict vocabulary matters.** "Block" and "allow" are not enough. Veldmark's gate returns four verdicts: *deliver*; *deliver with warning* (the recipient sees a banner such as "Tradeyard never asks you to confirm a payment through a link"); *withhold* (stored, not delivered, queued for review or automatic release, and shown to the sender as sent); *block* (rejected, with an enforcement action on the account). Withholding silently is deliberate: a sender told that a message was blocked learns which words to change. It is also an enforcement decision that, under the EU Digital Services Act (DSA), may require a statement of reasons to the affected user; [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation) covers when.

**Privacy constrains the design.** Automated scanning of private messages engages the General Data Protection Regulation (GDPR): purpose limitation, data minimization and transparency. Many platforms rely on legitimate interest for fraud prevention, which needs a documented balancing test and usually a data-protection impact assessment, and the terms of service should say that automated tools check messages. Whether a marketplace's chat is also an "interpersonal communications service" under the European Electronic Communications Code, and therefore subject to the confidentiality rules of the ePrivacy framework, is a legal question for each platform. The Code's definition excludes services where communication is "merely a minor ancillary feature that is intrinsically linked to another service" ([Directive (EU) 2018/1972, Art. 2(5)](https://eur-lex.europa.eu/eli/dir/2018/1972/oj)), and a marketplace whose chat exists only to discuss listings has a reasonable argument that it is ancillary. That is a reading to confirm with counsel, not a settled fact. **Get a written legal position before building message scanning, not after**, because the answer changes what you may scan, store and keep.

{id: messaging-and-leads--retention-what-to-keep-and-for-how-long}
## Retention: What to Keep, and for How Long

Messages are the most sensitive data most listing platforms hold that users did not mean to publish: addresses, phone numbers, bank details, arguments, sometimes photos of identity documents. Retention should therefore be set per data class.

| Data class | Example | Retention driver | Veldmark rule (2027) |
| --- | --- | --- | --- |
| Message content | Text and attachment references | Usefulness to participants; minimization | Deleted **24 months** after the conversation's last message, or on account deletion |
| Message metadata | Sender, timestamps, delivery and read state | Abuse investigation, metrics | Pseudonymized after 24 months; aggregates kept |
| Safety evidence | Withheld or reported messages, verdicts, reviewer notes | Enforcement, appeals, DSA records, law enforcement requests | Kept with the T&S case under the case's retention policy |
| Lead record (platform copy) | Lead ID, channel, timestamps, recipient, disposition | Billing, disputes, attribution | Kept for the contract term plus the dispute window; contact details removed after 13 months |
| Lead copy delivered to the professional | Name, contact details, first message | The professional's own obligations | Outside Veldmark's control once delivered; minimized at source |

The last row is the reason **lead payloads must be minimized at design time**. Once a buyer's details are in a dealer's CRM, the platform cannot delete them. Rightmove's lead exports illustrate the platform side of the bargain: each brand-level call returns "a maximum of 24 hours within the last 28 days", so leads older than 28 days cannot be retrieved through the API at all ([Rightmove RTDF v1.4.1, 2023](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)). A bounded export window keeps the portal from becoming an indefinite lead archive and pushes the long-term record into the professional's system, where it belongs.

{id: messaging-and-leads--leads-creation-qualification-and-lifecycle}
## Leads: Creation, Qualification and Lifecycle

The lead service turns contacts into leads. It subscribes to conversation, call and booking events and applies the lead-creation rules, deduplication and enrichment.

**Creation and deduplication.** At Veldmark the rule is: a lead is created by the first buyer message in a new conversation with a professional, by a tracked call that connects and lasts at least 30 seconds, by a confirmed booking, or by a callback request. Further contacts from the same buyer about the same listing within 30 days attach to the existing lead and update its channel history. "One buyer, three channels, one lead" is the principle, because it is the one a professional will accept; anything else invites the argument Autohaus Ruhrblick started.

**Qualification and enrichment.** A lead's value depends on what the professional learns from it. The published examples all add structured information at the moment of contact:

- Rightmove says its upgraded **Enhanced Leads** for lettings agents "enriches tenant enquiries with additional, pre-qualification information", is "integrated into partners' CRMs, delivering lead data in real time", is used by "50% of all letting lead senders", and that "over 80% of lead senders are signed in when submitting a lead". The same 2026 report says 60% of consumers attach a property to their Mortgage in Principle ([Rightmove, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)).
- CarGurus' FY2025 10-K describes **Digital Deal**, which captures "purchase intent signals such as trade-in interest and financing preferences", and **Pre-Qualified Leads** from automotive lending partners ([CarGurus, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)).
- Autotrader launched **Buying Signals** in January 2026, "a proprietary machine learning model trained on verified but anonymised sales transactions and consumer interactions". It had featured on more than 800,000 enquiries, and "early results indicate that leads flagged as high-intent convert at twice the average rate" ([Autotrader, 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf)).

The pattern is consistent: **a signed-in buyer, a structured enquiry and a model score make a lead worth more than a free-text e-mail**, and portals use them both to raise lead value and to justify package prices. The architectural requirement is that qualification data travels in the lead contract as typed fields (financing interest, trade-in, move-in date, budget, verified identity level), not as prose appended to the message, so CRMs can act on it. Lead scoring is a model like any other and needs the ownership and monitoring described in [Models in Production: ML Platforms and Use Cases](#ml-platform).

**The lead lifecycle.** A lead needs states that both sides recognize, because each state is a potential dispute.

![Diagram: The lead lifecycle Veldmark adopted](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/fig04-lead-lifecycle-veldmark-adopted-portal-controls.jpeg)

**Figure 4:** *The lead lifecycle Veldmark adopted. The portal controls the states up to Delivered; everything after Acknowledged depends on data from the professional's systems. Billing rules and ROI reports must say which state they count.*

Two things in Figure 4 are easy to miss. First, **"delivered" means the recipient's system accepted it, not that Veldmark sent an e-mail.** Second, the states after Acknowledged are reported by the professional, so they are only as good as the integration. A portal that cannot receive outcomes cannot measure lead value except through surveys and renewals.

{id: messaging-and-leads--lead-routing-and-delivery}
## Lead Routing and Delivery

**Routing rules.** Most leads have an obvious recipient: the professional who owns the listing. CoStar describes Homes.com as working on a "your-listing your lead basis", a deliberate contrast with models that resell buyer interest to other agents ([CoStar, 2026](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm)). Other models route by commercial rules. Zillow distributes Premier Agent connections "in proportion to their share of voice, or a Premier Agent partner's share of total advertising purchased in a particular zip code", and "do[es] not promise any minimum or maximum share of connections" ([Zillow, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). Within a dealer group or agency network, routing usually goes one level further: to the rooftop or branch that holds the vehicle, then to a salesperson by rotation, territory or availability. Zillow says its Follow Up Boss CRM has added "intelligent lead routing" ([Zillow, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)), which places part of the routing decision inside the professional's own software.

The routing decision should be a separate, versioned rule set with its inputs logged, for three reasons. It is commercially sensitive (who gets the buyer), it is subject to transparency obligations where paid placement affects which professional a buyer reaches (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)), and it is the first thing examined in a dispute.

**Delivery channels.** Professionals receive leads in systems the portal does not control: dealer management systems, automotive CRMs, agency transaction software, applicant-tracking systems for jobs. The delivery adapter is the anti-corruption layer between the lead contract and each of them.

| Delivery channel | How it works | Strengths | Weaknesses | When to use |
| --- | --- | --- | --- | --- |
| **E-mail** (human-readable, sometimes parseable) | Formatted e-mail to a branch address, often parsed by the CRM | Universal; no integration | No acknowledgement; parsing breaks; no outcomes; easy to lose | Fallback only |
| **Structured e-mail or file** (an industry XML or CSV convention) | Machine-readable payload by e-mail or file drop; in the US, dealer CRMs commonly accept the ADF (Auto-lead Data Format) XML convention | Widely supported in automotive | One-way; versioning by convention | Long tail of dealer CRMs |
| **Pull API** | The professional's software polls the portal for new leads | Simple for the portal; the client controls load | Latency; at-least-once delivery that the client must deduplicate | Many small software vendors |
| **Push webhook or API** | The portal posts each lead to the recipient's endpoint, retries until acknowledged | Seconds of latency; acknowledgement; idempotent with a lead ID | Every recipient must run an endpoint; retries and dead letters to manage | Large CRMs and dealer groups |
| **Portal pro inbox** | Leads shown in the portal's own professional tools | Full control; rich features | One more inbox; duplicates the CRM | Small professionals without a CRM |

**A pull contract shifts the exactly-once problem to the client.** Rightmove's published specification, the clearest public example, advises software providers to call the brand or branch lead exports "at regular intervals (maximum suggested frequency is every 15 minutes) to build up a local database", and to overlap export windows, for example "every 15 minutes, and always request the last 20 minutes' worth of data", because the response's `Replication_Lag` field reports how long data takes to replicate "between the three Rightmove datacentres", and data within that lag may be missing ([Rightmove RTDF v1.4.1, 2023](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf)). Overlapping windows mean every lead arrives at least once and often twice, so **the receiving system must deduplicate on the lead identifier**. A push contract keeps the problem at the portal, which must retry until the recipient acknowledges and must send the same lead ID every time.

Push delivery through a lead API is where the larger portals are heading: in a July 2026 platform update, mobile.de described its Lead API as transferring leads "directly and securely into existing CRM systems" ([mobile.de, 2026](https://newsroom.mobile.de/plattform-update-sommer-2026/)).

My recommendation for a multi-brand group is to define **one lead contract** (a versioned event and API schema, with a stable lead ID, source channel, timestamps, listing and seller references, consented contact data, typed qualification fields and the routing decision), and to implement each delivery channel as an adapter on top of it. Veldmark's Golf disagreement disappears when the calls go through the same contract as the e-mails, and when the dealer's CRM acknowledges each lead ID: both sides then count the same list.

{id: messaging-and-leads--attribution-roi-and-disintermediation}
## Attribution, ROI and Disintermediation

A professional pays for outcomes and is sold contacts. **Attribution** is the work of connecting the two: matching a lead to a sale, mandate, lease or hire, and reporting the result in a way both sides accept.

The portal rarely owns the outcome. A dealer's sale is recorded in the DMS; an agency's mandate and completion in its transaction software; a property sale, in some countries, in public records months later. The only reliable attribution comes from the professional's systems sending outcomes back (CRM status updates, DMS sales matched to the vehicle identification number), or, for pay-at-close models, from transaction matching over long periods. Zillow's pay-at-close program charges a fee "when a real estate transaction is closed with one of the leads, generally within two years", and treats the fee as variable consideration estimated from "the conversion rate of a lead to a real estate transaction" ([Zillow, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). That model only works with an outcome pipeline; [How Listing Marketplaces Make Money](#monetization-models) discusses the economics.

Lead counts are also an operational signal: **a broken contact button looks like a quiet day unless someone watches lead counts per platform, channel and country against a forecast.** Adevinta's Benelux analysts described in **2024** an anomaly-detection tool, Artemis, that monitors more than 140 product metrics and caught a drop in iOS leads of about 100,000 a day, valued at about €41,000 a day, within a day ([Adevinta, 2024](https://adevinta.com/techblog/artemis-fostering-autonomy-in-monitoring-data-quality/)).

Disintermediation is the other side of attribution. Buyers and sellers who meet on the platform can continue by phone, WhatsApp or in person. For a classifieds business that charges for visibility, this is acceptable: the value was the match. For pay-per-lead and transactional models it is leakage, and the temptation is to fight it by hiding contact details and blocking phone numbers in messages. That works up to the point where it damages the experience that created the match.

The defensible position, in my view, is to **keep users on-platform with value rather than walls**: protected payment ([Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments)), booking and reservation flows, verified identity, and a conversation history users trust, with contact details masked only where safety requires it (new accounts, high-risk categories). Marktplaats' buyer-protection product, launched in 2022, can be used only when the deal is arranged through in-platform messaging ([AVROTROS Radar, 2022](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677)); Kleinanzeigen's "Sicher bezahlen" starts from an agreement in chat ([Kleinanzeigen, n.d.](https://themen.kleinanzeigen.de/sicher-bezahlen/)). Both tie the protection to the conversation, which gives users a reason to stay in it.

![Left: a walled marketplace that users climb out of. Right: an open square where users stay for protected payment, booking, verified identity and chat history.](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/value-not-walls.jpeg)

**Figure 5:** *Hiding contact details and blocking numbers works only until it damages the match; protected payment, booking, verified identity and a trusted conversation history give users a reason to stay on-platform.*

{id: messaging-and-leads--in-practice-the-public-record}
## In Practice: The Public Record

Marketplaces publish little about messaging and lead architecture, and most of it is cited above (OLX's 2021 chat storage and 2026 chat-image blocking, Rightmove's lead-export contract, Autotrader's, CarGurus' and Zillow's lead products). Two further documents place contact systems in a group's strategy and in its legal exposure.

Adevinta's 2023 annual report names chat among the capabilities the group consolidated first: "Historically, the team's focus was on consolidating enabling capabilities such as cloud and data, and overarching elements such as chat and moderation" ([Adevinta, 2024](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm)). No architecture post on Adevinta's shared messaging service has been published, so how it was built is not public. The strategic reading is still useful: **messaging is generic enough to share across countries and brands, and close enough to trust and safety that sharing it pays twice.**

CarGurus' 10-K adds a reminder that channels carry their own law. Because its platforms "enable us, dealers, and users to send and receive text messages and other mobile phone communications", CarGurus lists compliance with the US Telephone Consumer Protection Act, which restricts calls and texts without prior express consent, as a risk ([CarGurus, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)). A contact channel is also a consent record.

{id: messaging-and-leads--veldmark-worked-example-one-messaging-platform-four-brands}
## Veldmark Worked Example: One Messaging Platform, Four Brands

The architecture advice forum adopted the reference design in Figure 2 in **May 2027** as part of the Common Ground program. The baseline it replaced:

| Brand | Contact channels (2027) | Message store | Safety | Lead delivery |
| --- | --- | --- | --- | --- |
| Tradeyard (NL, BE, PL, PT) | Chat; phone reveal for professionals | Yardstick module on MySQL; WebSocket gateway on AWS since 2021 | Deny-list check at send; NL message model asynchronous | Pro inbox in Yardstick; e-mail |
| Motorvane | E-mail form; tracked calls; test-drive booking; chat since 2024 | Kotlin service on AWS | Keyword rules | E-mail export to dealer CRMs; calls and bookings only in Dealer Hub |
| Hearthly (FR, ES) | Contact form; agency phone; viewing requests | Forms only, no chat | Manual review of new agencies | E-mail; exports to real-estate software vendors, including Keybridge |
| Keybridge | Receives leads from many portals for its agencies | — | — | Inbound side of the problem |

**Volumes.** About **14 million messages a day** group-wide, **11 million** of them on Tradeyard. The average is about 160 messages a second; Veldmark planned for about **600 a second** at the Sunday-evening peak, a little above search's peak-to-average ratio of about 3.4. At an average of about 1 KB per stored message including metadata, Tradeyard alone writes about 11 GB of message data a day, about 4 TB a year before replication, which is modest. The capacity problem is not storage. It is the safety gate (one synchronous call per message, so about 600 calls a second at peak inside a 150 ms budget) and the inbox fan-out for professional accounts.

**The city bike, replayed.** Under the new design, the 20:11 message would have gone through the gate with three signals: a link to a domain registered that day, the words "Safe Deal" in the text, and a sender account created on Saturday. The domain-age rule alone triggers *withhold*. The message is stored, not delivered, and Femke never sees it. The same rule withholds the account's messages to the nine other sellers it had contacted that evening, the asynchronous message model scores the account's history, the account is suspended, and each of those sellers receives a safety notice in the affected conversation instead of the link. The **37** messages withheld on 7 March by a hand-written rule are withheld by the standing domain-age rule within seconds of being sent, not after an analyst writes a rule. Femke's 13 genuine conversations continue unaffected, and the sale happens on Monday as before.

**The Golf, replayed.** Under the lead contract, each of the 23 contacts produces either a new lead or an update. The **14 e-mail enquiries** come from 13 buyers, so they make 13 leads; one buyer wrote twice and later booked a test drive, and all three of that buyer's contacts sit on one lead. Of the **2 bookings**, that one merges and the other is a new buyer: 1 lead. The **7 calls** go through tracked numbers and all last longer than 30 seconds, but two come from buyers who had already e-mailed: 5 new leads. That gives **19 leads** from the 23 contacts that Motorvane's 2027 reporting counted as leads; the other four were repeat contacts from the same buyers. The 19 are delivered by webhook to Autohaus Ruhrblick's CRM with acknowledgements. Under the old delivery, the dealer saw 14 records, including the duplicate e-mail, and Motorvane reported 23; under the contract, both sides see the same 19 lead IDs, and the dealer's CRM reports the sale on 29 April against one of them. The proposed per-lead charge can now be priced on a number the dealer can audit.

![Before: portal counts 23 and dealer CRM counts 14 with no shared identifier. After: contacts merge into 19 lead IDs that both systems show.](listing-systems-architecture/posts/28-messaging-and-leads/assets/images/28-messaging-and-leads/golf-one-set-of-lead-ids.jpeg)

**Figure 6:** *Under the lead contract, the Golf's 23 contacts merge into 19 leads with stable IDs, so Motorvane and Autohaus Ruhrblick count the same records instead of arguing over 23 against 14.*

**The decisions.** The forum recorded four decisions, each with a decision record:

1. One **group conversation service** for all brands, with brand-specific user interfaces, delivered in stages: Tradeyard NL and BE first, with the shared trust-and-safety platform, from **November 2027**; Motorvane and Hearthly in 2028. Hearthly gains chat for the first time in that step.
2. The **message safety gate** is a T&S platform service with a contract owned by Messaging: four verdicts, 150 ms p99, fail-closed for links and payment details from new accounts.
3. A **Lead event contract v1** on the group event backbone, with a stable lead ID, live from **Q1 2028**; every delivery channel becomes an adapter; e-mail-only delivery is retired for professionals with a CRM integration by end of 2028.
4. **Keybridge stays on the receiving side only.** Leads from Hearthly reach Keybridge agencies through the same lead contract and delivery adapters as leads to agencies using competing software, and Hearthly does not read lead outcomes from Keybridge beyond what any software vendor's integration returns. This applies the March 2027 neutrality decision to leads.

{id: messaging-and-leads--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Build or buy messaging | In-house conversation service | Commercial chat API or SaaS | Messaging volume is large, safety must sit inside the delivery path, and retention rules are strict | Small or new marketplace; chat is secondary to forms; vendor offers synchronous moderation hooks |
| Safety placement | Synchronous gate plus asynchronous withdrawal | Asynchronous only | Payment scams and phishing are material; peak load is predictable | Low-fraud vertical (most B2B leads); latency budget is very tight |
| Contact details | Masked by default (relay e-mail, tracked numbers) | Shown after a click | Private sellers; high-fraud categories; pay-per-lead models that need counting | Established professionals who insist on direct contact; low-fraud categories |
| Lead delivery | Push with acknowledgement | Pull API | Large CRMs and dealer groups; billing depends on counts | Long tail of small software vendors; portal cannot run per-recipient retries |
| Lead definition | Strict (deduplicated, qualified) | Generous (every contact counts) | Pay per lead; dealer disputes are costly | Pure subscription; volume reporting supports renewals and nobody is billed per lead |
| Group platform | One conversation service, brand UIs | One per brand | Shared T&S, shared identity, overlapping users across brands | Brands with no shared users and very different contact flows, or a brand about to be sold |

Masking protects private sellers and makes counting possible, but professionals often experience it as the portal standing between them and their customer. CarGurus' free tier offers "capped anonymous leads and connections" ([CarGurus, 2026](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm)), which shows the other use of masking: as a paid entitlement, where full contact details are part of what the package buys. If masking is an entitlement, it is enforced in the contact policy service from the entitlement service's read model, not in the conversation code ([Packages, Bumps and Quotas: Products, Pricing and Entitlements](#products-and-entitlements)).

{id: messaging-and-leads--vertical-differences}
## Vertical Differences

| Aspect | General classifieds | Real estate | Automotive | Jobs | Recommerce with payments |
| --- | --- | --- | --- | --- | --- |
| Dominant channel | Chat between private parties | Enquiry form, phone, viewing request | E-mail enquiry, phone, test drive, reservation | Application | Chat with offer and checkout |
| Who receives | Private seller | Agency branch, agent; developer sales office | Dealer rooftop, salesperson | Employer, recruiter, applicant-tracking system | Private seller |
| Lead object needed? | Rarely, except for professional sellers | Yes, central | Yes, central | Yes (application) | No; the order replaces it |
| Main fraud in contacts | Payment-link phishing, fake buyers | Fake landlords and deposits (the Barcelona ring in [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)) | Deposit scams, fake escrow | Fake job offers, data harvesting | Phishing impersonating the platform's payment |
| Qualification data | Little | Budget, financing, move-in date, rental dossier | Financing, trade-in, delivery preference | CV, skills, right to work | Not needed |
| Routing complexity | None | Several agencies per property (the Lyon apartment); multi-branch networks | Dealer groups, rooftops, sales teams | Recruiter versus employer | None |
| Outcome data | Sold flag, payment if on-platform | Mandate, offer, completion; public records months later | DMS sale, often within days | Hire, rarely reported | Order completed |

In **real estate**, **the lead goes to the agency whose listing the buyer contacted**, even when entity resolution has clustered several agencies' listings of one property into one canonical record (the Lyon apartment, listed by three agencies, in [One Property, Three Listings: Duplicates and Entity Resolution](#entity-resolution)). The buyer contacts a listing, not the cluster, even if the canonical view showed another agency's photos first. Routing a lead to a paying agency instead of the one the buyer chose would be a ranking decision disguised as routing, and a fairness problem with every agency involved.

In **automotive**, outcome data is closest to the portal: a dealer sale appears in the DMS and in the feed's removal within days (the Golf's removal arrived 26 hours after the sale), which makes automotive the vertical where lead attribution can be most precise, if the dealer agrees to share it.

{id: messaging-and-leads--failure-modes}
## Failure Modes

- **Safety after delivery.** Checks that run on stored messages or only on reports. The fraud succeeds before the check runs. Symptom: report-to-action times look good while losses rise.
- **The chat store as lead database.** Lead counts computed by querying conversations. Every change to chat (merging threads, a new message type) changes billing numbers retroactively.
- **E-mail as the lead contract.** Leads delivered only as e-mails parsed by CRMs. No acknowledgement, no stable ID, no outcomes; every renewal starts with an argument about counts.
- **Duplicate leads from retries and overlaps.** Pull exports with overlapping windows, or push retries without a stable lead ID, create duplicates in the recipient's CRM, and the portal is blamed for "fake" leads.
- **Contacts on gone listings.** Conversation screens and cached contact buttons that keep accepting messages after a sale; lead forms that still route to a dealer for a car sold yesterday. Ghost Inventory, now billed.
- **Copies of message content everywhere.** Message text in analytics events, search logs, support tools and data-warehouse tables. Deletion requests become impossible to honor, and a breach exposes private correspondence.
- **Routing rules hidden in code.** Who gets a lead decided by conditions scattered across services. Nobody can explain a misrouted lead, and paid routing cannot be disclosed accurately.
- **Lead volume treated as success.** Products optimized for more contact submissions (pre-filled messages, one-tap "Is it still available?") that raise counts and lower the professional's reply rate. Vanity Liquidity in the lead funnel.

{id: messaging-and-leads--the-chief-architect-s-view}
## The Chief Architect's View

At group scale, messaging and leads raise five decisions that belong to the Chief Architect's agenda rather than to a single team.

**Share the conversation platform early.** Messaging is generic across brands and countries, it is where trust and safety pays off most, and it is a natural client of the group identity ([Who Is on the Other Side? Identity and Verification](#identity-and-verification)). Adevinta's record suggests the same priority. The brand experience (wording, layout, quick replies, offer flows) stays local; the conversation model, storage, delivery, retention and safety gate are shared. This follows Veldmark's principle of sharing platforms, not products.

**Make the lead contract a governed interface.** The lead contract is as important as the listing event contract, because money depends on it. It needs a schema registry entry, a versioning policy, an owner in the platform organization, and a change process that includes monetization, the sales organization and the largest CRM partners. Changing the lead-creation rule is a pricing change and should be reviewed as one.

**Assign ownership explicitly.** At Veldmark: Messaging owns the conversation service, the gate contract and retention; Trust & Safety owns policies, detectors and verdict logic; Monetization owns which lead states are billable; the Data Protection Officer, Lucía Ortega, signs off the scanning and retention design; the Professional Tools teams own the pro inbox and CRM integrations. The architecture advice forum reviews any change that crosses two of these.

**Measure the path, not the volume.** The metrics I would put on the group dashboard: time to first reply and reply rate (buyer experience); scam reports per 10,000 conversations and the share of withheld messages later released on review (safety and its precision); gate p99 and fail-open rate (operability); lead delivery latency p95 and acknowledgement rate; the **reconciliation gap** between portal and CRM lead counts per professional (trust in the numbers); and lead-to-outcome rate where outcome data exists. [Data Platform for Marketplaces: Events, Lakehouse and Data Products](#data-platform) should make these governed metrics with one definition across brands.

**Plan for AI on both sides of the conversation.** Professionals already use AI to answer enquiries; Zillow reports "AI-supported smart message suggestions" in its CRM ([Zillow, 2026](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm)). Buyers will increasingly reach listings through assistants that send enquiries on their behalf. The conversation model should be able to mark machine-generated messages and agent-initiated contacts, the lead contract should record them, and lead-creation rules should decide whether an assistant's enquiry is a lead. [AI Across the Listing Lifecycle](#ai-in-listing-systems) takes this further.

{id: messaging-and-leads--questions-to-ask}
## Questions to Ask

1. Where in a message's life does the first safety check run: before delivery, after storage, or only on report? What is its latency budget and what happens when it times out?
2. What verdicts can the gate return, and what does the sender see for each?
3. How many systems hold message content, and can you delete a user's messages from all of them within the deadline your privacy policy promises?
4. What is your written legal position on scanning messages, and when was it last reviewed?
5. What exact rule turns a contact into a lead, who owns that rule, and when did it last change?
6. If a dealer and the portal count leads for the same listing, do they get the same number? If not, can you explain the difference lead by lead?
7. How is a lead delivered to a professional's system, how do you know it arrived, and what happens when the recipient is down for six hours?
8. Who decides which professional receives a lead, are the inputs logged, and is any part of that decision paid?
9. When a listing is sold or removed, how many seconds pass before contact is closed in every channel, including open conversation screens and tracked numbers?
10. Which outcome data (sales, mandates, hires) flows back from professionals, and which ROI claims depend on it?

{id: messaging-and-leads--from-contact-to-transaction}
## From Contact to Transaction

A contact that turns into an agreement leaves the marketplace with a choice: step aside and let the parties pay each other, or carry the deal through payment, shipping and buyer protection. Tradeyard's Safe Deal began in the conversation, with an offer accepted in chat, and the phishing link that reached Femke imitated exactly that flow. The next chapter, [Beyond the Contact: Payments, Shipping and Buyer Protection](#transactions-and-payments), follows the money: when a classifieds marketplace should move into transactions, and what it takes architecturally.

{id: messaging-and-leads--sources-and-evidence}
## Sources and Evidence

{id: messaging-and-leads--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Cassandra Compaction Trade-Offs](https://tech.olx.com/cassandra-compaction-trade-offs-848ba51c64c0), OLX Tech Blog (Satish Chandra), 2021 — chat storage on Cassandra, partitioning by user, chats and threads tables, mutable message metadata.
- [How Discord Stores Trillions of Messages](https://discord.com/blog/how-discord-stores-trillions-of-messages), Discord (Bo Ingram), 2023 — message partitioning, hot partitions, request coalescing, migration results.
- [AI fraud prevention at OLX](https://www.olxgroup.com/?p=4590), OLX Group, 2026 — real-time chat image blocking, QR-code phishing detection, share of image fraud in Poland.
- [OLX blocks scammers using advanced algorithms](https://www.itweb.co.za/article/olx-blocks-scammers-using-advanced-algorithms/nWJadvb8APOMbjO1), ITWeb, 2018 — warn-in-context pattern in chat.
- [Adevinta Annual Report 2023](https://www.sec.gov/Archives/edgar/data/1065088/000106508824000094/ex9901adevinta2023annualre.htm), Adevinta ASA (exhibit to eBay filing), 2024 — chat and moderation as early group-wide components.
- [Artemis: fostering autonomy in monitoring data quality](https://adevinta.com/techblog/artemis-fostering-autonomy-in-monitoring-data-quality/), Adevinta Tech Blog, 2024 — lead-volume anomaly detection.
- [Rightmove Real Time Datafeed Specification v1.4.1](https://media.rightmove.co.uk/ps/pdf/guides/adf/Rightmove_Real_Time_Datafeed_Specification.pdf), Rightmove, 2023 — lead export calls, export windows, overlapping polling, replication lag, removal of phone-lead calls in 2021.
- [Rightmove plc results for the year ended 31 December 2025](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), Rightmove, 2026 — Enhanced Leads, signed-in lead senders, Mortgage in Principle attachment.
- [Full year results for the year ended 31 March 2026](https://plc.autotrader.co.uk/media/usjleen0/full-year-press-release-fy26.pdf), Autotrader Group, 2026 — Deal Builder reservations and conversion, Buying Signals, retailer feedback on roll-out.
- [CarGurus Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1494259/000119312526059435/carg-20251231.htm), CarGurus, 2026 — connection definition, capped anonymous leads, Digital Deal, Pre-Qualified Leads, TCPA risk.
- [Zillow Group Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1617640/000161764026000015/z-20251231.htm), Zillow Group, 2026 — validated connections, share-of-voice routing, pay at close, Follow Up Boss routing and message suggestions.
- [CoStar Group Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1057352/000105735226000020/csgp-20251231.htm), CoStar Group, 2026 — Homes.com "your-listing your lead" model.
- [Sicherheitshinweise](https://themen.kleinanzeigen.de/sicherheitshinweise/) and [Sicher bezahlen](https://themen.kleinanzeigen.de/sicher-bezahlen/), Kleinanzeigen, n.d. — warnings about impersonation in chat; payment flow starting from chat.
- [Plattform-Update Sommer 2026](https://newsroom.mobile.de/plattform-update-sommer-2026/), mobile.de newsroom, 2026 — Lead API into dealers' CRM systems.
- [Dit is de vervanger voor de Gelijk Oversteken-functie van Marktplaats](https://radar.avrotros.nl/artikel/dit-is-de-vervanger-voor-de-gelijk-oversteken-functie-van-marktplaats-52677), AVROTROS Radar, 2022 — buyer protection tied to in-platform messaging.

{id: messaging-and-leads--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Directive (EU) 2018/1972, European Electronic Communications Code](https://eur-lex.europa.eu/eli/dir/2018/1972/oj), *Official Journal*, 2018 (Article 2(5) checked against the Publications Office text, October 2026) — definition of interpersonal communications service and the ancillary-feature exclusion.
- [Regulation (EU) 2016/679, General Data Protection Regulation](https://eur-lex.europa.eu/eli/reg/2016/679/oj), 2016 — purpose limitation, minimization, legitimate interest.
- [Regulation (EU) 2022/2065, Digital Services Act](https://eur-lex.europa.eu/eli/reg/2022/2065/oj), 2022 — statements of reasons for restrictions, including of messages.

{id: messaging-and-leads--research-and-practitioner-sources}
### Research and practitioner sources

- [Fraudulent advertising and account integrity: expert insights on best practice](https://www.ofcom.org.uk/siteassets/resources/documents/research-and-data/online-advertising/fraudulent-advertising-and-account-integrity_expert-insights-on-best-practice.pdf), Integrity Institute for Ofcom, 2026 — friction for new accounts and account-integrity signals relevant to contact policy.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
