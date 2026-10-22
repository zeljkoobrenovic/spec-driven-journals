{id: ai-in-travel-stays}
# 46. AI Across the Stay: Agents, Assistants and Automation

![AI Across the Stay: Agents, Assistants and Automation — logo](stays-marketplace-architecture/posts/46-ai-in-travel-stays/assets/images/46-ai-in-travel-stays/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Map where generative AI and agents act in a stays marketplace (trip planning, conversational search, support, host tools, trust and third-party agents that book on a traveler's behalf), and design the layer that keeps them grounded, authorized, evaluated and affordable: tools over domain contracts, an agent-facing gateway, booking authority and group AI governance.

> **WHY THE BUSINESS CARES:** AI assistants are becoming a front door to travel. Booking Holdings warns that "AI agents may further evolve into full-service booking platforms", and the marketplaces that answer agents well will keep the booking, while the ones that do not will become anonymous suppliers behind them. Inside the platform, assistants already handle support contacts and draft hosts' listings, so their mistakes are now the marketplace's liabilities.

> **WHY ARCHITECTS SHOULD CARE:** A language model cannot be trusted with a price, a place, a cancellation rule or a booking. The architecture decides whether it has to be: whether those facts come from the systems of record through tools, whether every action carries a traceable authority, and whether anyone can reconstruct who decided what when an agent books the wrong night in the wrong town.

> **KEY POINTS:**
>
> * **Put AI in front of the marketplace's contracts, never in place of them.** The model interprets intent and explains results. Places, prices, availability, policies and bookings come from the same services that serve the website, called as tools. An assistant is only as good as the offer, policy and reservation contracts underneath it.
> * **Agentic booking needs an explicit booking authority.** When software books for a traveler, the marketplace must know who acted, for whom and under what limits: a human final click on a marketplace-hosted confirmation by default, or a signed mandate with the place, dates, total and refundability spelled out. Ambiguity is resolved with the human, not by the model.
> * **Govern AI by the consequence of its actions, not by the model inside it.** Classify each use by what it can change (a read, a draft, a reversible write, money or a decision about a person), give each class its controls, evaluate continuously against the systems of record, and keep one register of every AI use with an owner.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **The Unwatched Model** — an agent channel or assistant goes live as a pilot, with neither a named owner nor a way to reconstruct its decisions, and nobody notices its errors until a guest arrives in the wrong town.
> * **Price Drift** — assistants that quote prices from their own context, a cached feed or a summary instead of a binding quote give the traveler a fifth price to compare with the four the platform already shows.
> * **Policy Spaghetti** — an assistant that answers cancellation and refund questions from help articles creates another copy of the rules, and the marketplace is liable for whatever it said.

Every stays marketplace now runs AI in at least four places: a support assistant, some form of natural-language search or trip planning, generated content for properties and homes, and models inside trust and fraud. A fifth is arriving from outside: **general-purpose AI assistants that search, compare and book on a traveler's behalf**, through interfaces the marketplace exposes or tolerates. The fifth changes who the customer of the platform's APIs is.

The public record is clear about the direction and thin on architecture. What it does show is consistent: **every documented launch keeps the language model in front of the existing search, pricing and booking stack**, not inside it, and the companies that have written about failure name the same cause: answers that were not grounded in live inventory and reservation data. This chapter takes that observation and turns it into an architecture.

This chapter owns two terms: **agentic booking** and **AI governance (stays)**. It sits in [Part IX — LEADERSHIP: The Chief Architect's Agenda](#part-9), after [Changing the Engine in Flight: Modernizing a Live Stays Marketplace](#modernizing-a-live-marketplace). It builds on the ML platform and model governance of [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform), the support assistant of [When Something Goes Wrong: Customer Service and Recovery](#customer-service), the offer kernel of [Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine), the cancellation engine of [When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations), the delegation model of [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) and the demand channels of [Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels). It does not re-teach them.

{id: ai-in-travel-stays--setting-the-scene-at-corvane-the-agent-that-booked-the-wrong-porto}
## Setting the Scene at Corvane: The Agent That Booked the Wrong Porto

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs **Roomstead**, an accommodation marketplace in the style of an online travel agency (OTA) with 640,000 properties sold by room type and rate plan, and **Nookaway**, a hosted-stays marketplace with 1.15 million listings. On **1 July 2027** Roomstead opened a pilot called **Frontdoor**: an agent-facing interface, built as a Model Context Protocol (MCP) server over its affiliate distribution API, offered to two third-party AI assistant providers under a pilot agreement. Frontdoor exposed three tools: search stays, get an offer, and create a booking. A traveler linked their Roomstead account to the assistant once, granted it a "book on my behalf" scope, and the assistant could then book with the card on file, up to €1,000 per booking.

On Tuesday **14 September 2027** at 21:04, Ruth Ellison, a traveler from Bristol, asked her assistant to "book us two nights in Porto, 1 to 3 October, under €200 a night, near the river, refundable if possible". Earlier that summer she had used the same assistant to plan a hiking week on the west coast of Corsica, around the village of **Porto** in Corse-du-Sud, which sits at the mouth of a river of the same name. The assistant sent Frontdoor the text "Porto" with a location bias taken from its memory of that conversation. Roomstead's legacy destination resolver, which Waypoint (the group destination graph, see [Where Exactly? Destinations, Geo and Map Search](#destinations-and-maps)) was due to replace in 2028, ranked the Corsican village first because of the bias. Frontdoor returned 14 hotels. The assistant picked a 22-room hotel "near the river" and booked its non-refundable rate, **€152 a night, €304 in total**, treating "refundable if possible" as a preference it could trade for price. Corvane Payments charged the card at 21:12. The confirmation e-mail said "Porto, Corse-du-Sud, France". The assistant's chat summary said "Booked: 2 nights in Porto near the river, €304".

Ruth found out at Porto airport on 1 October, when she opened the confirmation for the address. Roomstead refunded the €304 as goodwill; the hotel kept its payment under the non-refundable terms. The money was small; the questions at the incident review on 6 October were not.

![Two places called Porto side by side; an assistant points the booking at the Corsican village while the traveler stands at the airport of the Portuguese city.](stays-marketplace-architecture/posts/46-ai-in-travel-stays/assets/images/46-ai-in-travel-stays/46-which-porto.jpeg)

**Figure 1:** *One name, two places: the assistant booked Porto in Corsica for a traveler bound for Porto in Portugal, and no record showed who had made the choice.*

**Who decided Porto?** Frontdoor's logs held the tool calls and the coordinates, but not the conversation. The assistant provider held the conversation, but not Roomstead's resolver output. Neither could show Ruth a record of the choice. **Who authorized a non-refundable rate?** The scope she granted said "book", with a price cap; it said nothing about refundability, place or the need to ask when a name was ambiguous. **Who owned Frontdoor?** It had been launched by the affiliate team as a channel experiment. It had no entry in the model and AI registry that Kenji Arai's Data and ML Platform team had just started in Kiln, the group ML platform ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)), because it contained no Corvane model.

A sweep of the pilot's numbers followed. From 1 July to 30 September Frontdoor served **4.6 million** shopping requests and produced **1,610** bookings, about **2,860** shopping requests per booking: twice Roomstead's average of about 1,400, though well below the legacy affiliate API's 6,300. Of the bookings, **1,190** were made autonomously by assistants and **420** through a handoff to a Roomstead page. **64** autonomous bookings were for place names with more than one plausible match (Porto, Valencia and Valence, Santiago, Mérida, Córdoba, San Sebastián); support confirmed **9** as wrong-place bookings, with **€2,870** refunded in total. Mariana Costa, Group Chief Architect, put the question to the architecture forum: "What contract do we owe software that books for people, and what do we require from it?"

{id: ai-in-travel-stays--what-ai-does-in-a-stays-marketplace}
## What AI Does in a Stays Marketplace

"AI" in a stays marketplace covers very different systems. The useful distinction is not the model but **who the AI acts for and what it can change**. Four definitions keep the rest of the chapter precise:

| Term | Definition here |
| --- | --- |
| **Assistant** | A conversational system that answers and explains; it may call tools to read data |
| **Agent** | A system that works toward a goal over several steps, choosing and calling tools, some of which change state. Expedia Group's 2026 definition: "an AI-powered system that works toward a goal", which "can use context and memory, draw on skills, reason across multiple steps, and use tools" |
| **Tool** | A deterministic service an agent may call. Booking.com's 2026 definition: tools "do not learn or adapt; they provide reliable, structured operations" |
| **Agentic booking** | A reservation created, changed or canceled by software acting for a traveler, where the software, not the traveler, made at least one of the choices (place, property, rate, dates) |

With those terms, the portfolio sorts by consequence:

| Use | Acts for | Reads | Can change | Consequence class |
| --- | --- | --- | --- | --- |
| Trip planning, conversational search, property Q&A | Guest | Places, offers, content, reviews | Nothing; hands off to the funnel | Read |
| Review summaries, generated property descriptions | Marketplace, for guests | Reviews, structured content | Published content | Draft (partner or host approves), or published claim |
| Support assistant | Guest, host or partner | Reservation, policy, messages | Cancellations, messages, refunds within limits | Reversible write; money |
| Host and partner assistants: listing drafts, reply drafts, pricing | Host or partner | Listing, calendar, messages | Content, replies, prices under delegation | Draft or delegated write |
| Trust and fraud models, message scanning | Marketplace | Accounts, messages, payments | Holds, blocks, removals | Decision about a person |
| Third-party agents that book | Guest, through another company's AI | Search and offers | Reservations and payments | Money; a contract |
| Internal copilots (engineering, analytics, operations) | Employees | Code, logs, warehouse | Through employees | Internal |

The first five are AI the marketplace builds and runs. Trust models belong to [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety) and [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud), the support assistant to [When Something Goes Wrong: Customer Service and Recovery](#customer-service) and generated content to [Describing a Stay: Content, Media and Property Mapping](#content-and-media). The last two rows are new. **The third-party agent is a new kind of client and a new kind of actor, and the platform has to treat it as both.**

{id: ai-in-travel-stays--what-the-companies-have-documented}
## What the Companies Have Documented

The record from 2023 to 2026 shows a fast shift from planners that suggest to agents that act:

| Date | Company | What was launched or described | Source |
| --- | --- | --- | --- |
| June 2023 | Booking.com | AI Trip Planner beta for selected US travelers, built on its own recommendation models and OpenAI's ChatGPT API; results as a list of properties with Booking.com prices | [Booking Holdings, 2023](https://www.bookingholdings.com/press-releases/booking-com-launches-new-ai-trip-planner-to-enhance-travel-planning-experience/) |
| July 2023 | Trip.com | TripGenie: text or voice input; opens app pages with filters already applied | [Trip.com Group, 2023](https://www.trip.com/newsroom/introducing-tripgenie-groundbreaking-ai-travel-assistant) |
| October 2024 | Booking.com | Smart Filter (a description in the traveler's words becomes filters), Property Q&A, Review Summaries in test | [Booking Holdings, 2024](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/) |
| November 2024 | Anthropic | Model Context Protocol published as "an open standard" for connections between AI applications and data sources | [Anthropic, 2024](https://www.anthropic.com/news/model-context-protocol) |
| 2025 | Airbnb | AI customer-service agent to all US users (Q2); lets users cancel or change dates "directly from the chat" (Q3) | [Airbnb Q3 2025 letter](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf) |
| September 2025 | Google and partners | Agent Payments Protocol (AP2): signed "Intent Mandates" and "Cart Mandates" as "verifiable proof of a user's instructions" | [Google Cloud, 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) |
| October 2025 | OpenAI | Apps inside ChatGPT, with Booking.com and Expedia among the launch apps; OpenAI said the system is built on MCP | [TechCrunch, 2025](https://techcrunch.com/2025/10/06/openai-launches-apps-inside-of-chatgpt/) |
| February 2026 | Airbnb | Natural-language search tested with a small share of traffic | [Airbnb Q4 2025 letter, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm) |
| August 2026 | Airbnb | Assistant in "more than 50 languages"; "nearly 45%" of issues that begin with it resolved without a human | [Airbnb Q2 2026 letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm) |
| September 2026 | Expedia Group | Operating model for agents: registration and risk rating of every live AI initiative, MCP governance, and "the traveler should retain the final click for decisions such as completing a booking" | [Expedia Group Tech, 2026](https://medium.com/expedia-group-tech/building-the-operating-model-for-agentic-ai-at-expedia-group-f7555fcce506) |
| October 2026 | Booking.com | AgentHub: configurable agents across the funnel; every interaction traced with OpenTelemetry, judged by large language models (LLMs), guarded against prompt injection and personal-data leakage | [booking.ai, 2026](https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50) |

Three readings of this record matter for architecture.

**The model sits in front of the stack.** Booking.com's 2023 planner showed "Booking.com pricing" from its own systems; Trip.com's assistant opens app pages with filters applied; Smart Filter turns words into the platform's own filters. When Booking.com moved its trip planner's property Q&A from a deterministic flow to an agent in 2026, the agent's steps were property resolution, retrieval over property content, structured property data from internal services and a geospatial tool, and it reported answer relevance up 53% and factual accuracy up 3.3%. The gain came from better tool use, not from a model that knew more about hotels.

**Ungrounded answers are the documented failure.** A 2026 secondary report says Expedia discontinued Romie, the assistant it launched in alpha in May 2024, and quotes its product chief on the difficulty of keeping traveler trust when answers were not grounded in accurate, real-time inventory and reservation data ([Let's Data Science, 2026](https://letsdatascience.com/news/expedia-group-shares-ai-chatbot-lessons-learned-239f348a)). Treat that report as low confidence. The lesson matches everything else in the record.

**The front door may move.** Booking Holdings' 10-K for 2025 warns that AI features of third-party platforms may "satisfy user intent without directing users to our services", and that "AI agents may further evolve into full-service booking platforms, increasing competitive pressure and disintermediating" online travel companies ([Booking Holdings 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm)). The 2025 launch of apps inside ChatGPT, with two of the largest OTAs present from day one, shows that marketplaces have chosen to be inside the assistants rather than wait outside. [Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics) discusses what that does to marketing spend. This chapter covers what it does to the platform.

{id: ai-in-travel-stays--architecture-an-ai-layer-over-the-marketplace-s-contracts}
## Architecture: An AI Layer Over the Marketplace's Contracts

The architecture follows one rule: **business facts and business decisions stay in the services that already own them.** The AI layer adds three things: a way to call those services as tools, a way to know who is acting, and a way to watch and pay for what the models do.

![Own assistants pass through the AI platform and third-party agents through the agent gateway; both reach a tool registry, governed by the AI register, which is the only path to the domain contracts.](stays-marketplace-architecture/posts/46-ai-in-travel-stays/assets/images/46-ai-in-travel-stays/46-ai-layer-over-contracts.jpeg)

**Figure 2:** *Assistants and agents reach the marketplace only through registered tools over the existing domain contracts. The AI platform watches the models; the agent gateway knows who is acting and under what authority.*

| Component | Responsibility | Interfaces | Owner (reference) |
| --- | --- | --- | --- |
| **AI platform** | Model access and routing, cost metering, guardrails (prompt injection, personal data), tracing of every prompt, tool call and response, evaluation pipelines | Model gateway API; trace store; evaluation jobs | ML platform team, beside the classic ML platform |
| **Tool registry** | The list of domain operations an AI may call, each with a schema, a side-effect class, required scopes and an owner | Tool definitions published to internal agents and, as MCP servers, to external ones | Each domain team for its tools; platform for the registry |
| **Agent gateway** | Identifies the agent platform and the traveler behind each call, verifies booking authority, enforces quotas and look-to-book budgets, records the actor chain | MCP server and plain HTTP API for agents; token exchange with identity | Distribution or demand-channel team |
| **Domain contracts** | Place resolution, offer and price composition, policy evaluation, reservations, trust decisions | The same contracts the website and apps use | Their existing owners |
| **AI use-case register** | Every AI use, with owner, consequence class, approved tools, evaluation and approval | Read by the tool registry and gateways at runtime | Architecture governance with legal and privacy |

{id: ai-in-travel-stays--tools-carry-the-rules}
### Tools carry the rules

The design choice that matters most is **what a tool returns**. A search tool that returns "14 hotels in Porto" hides the decision that went wrong in September. A tool designed for agents returns the decision as data:

- **Place resolution returns candidates, not one answer.** Each candidate has a canonical place ID, country, region and a share of bookings for that name. When the top candidates are close, the response is marked ambiguous and the agent must ask the human. A location bias from the agent's memory is recorded as an input, not silently applied.
- **Offers return binding quotes.** The price an agent sees comes from the same offer kernel as checkout ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)), with a quote ID, a validity window (Roomstead holds quotes for 15 minutes), itemized fees and taxes, and the cancellation terms rendered by the policy engine. An agent that tells a traveler a price without a quote ID is quoting its own memory.
- **Every quote carries a canonical summary** written by the platform, not the model: "2 nights, 1–3 October 2027, Hotel X, Porto, Corse-du-Sud, France, non-refundable, €304.00 total". Agents are required to show it verbatim before booking. A summary the platform writes cannot be paraphrased into "near the river".
- **Policies are evaluated, never generated.** "Can I cancel for free?" is a call to the cancellation engine with the reservation, not a retrieval over help articles ([When Plans Change: Modifications, Cancellations and Policies](#changes-and-cancellations)). Booking.com's 2026 partner onboarding agent keeps a separate retriever of "pre-approved static" answers for legally restricted questions ([booking.ai, 2026](https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7)), the same principle applied to content.

![An assistant at a counter pulls answers from drawers labeled price, place, policy and booking instead of answering from memory.](stays-marketplace-architecture/posts/46-ai-in-travel-stays/assets/images/46-ai-in-travel-stays/46-in-front-not-in-place.jpeg)

**Figure 3:** *The model interprets and explains; prices, places, policies and bookings come from the systems of record through tools.*

{id: ai-in-travel-stays--side-effect-classes}
### Side-effect classes

Every tool is registered with one of five classes, and the class, not the model, decides the controls:

| Class | Examples | Required controls |
| --- | --- | --- |
| **Read** | Search, get offer, get reservation, get policy | Caller identity, rate limits, data minimization in responses |
| **Draft** | Listing description, reply draft, review summary | Provenance (model, version, inputs); a human approves before it is published or sent |
| **Reversible write** | Send an arrival-time message, add a wishlist item, cancel inside a free-cancellation window | Idempotency key, actor recorded, undo path, per-actor limits |
| **Money or contract** | Create a booking, refund outside policy, change a price in a host's calendar | Explicit authority (final click or mandate), binding quote, audit trail, limits per actor |
| **Decision about a person** | Block a reservation, remove a listing, restrict an account | Human review or contest path, statement of reasons, registered tier 3 model ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)) |

The classes are deliberately the same for humans and machines. Corvane's support assistant already acts "within an actor limit" through the recovery-decision service of [When Something Goes Wrong: Customer Service and Recovery](#customer-service); a third-party agent gets the same treatment with a lower limit. **An AI can never do what a first-line human with the same role could not.**

{id: ai-in-travel-stays--agentic-booking-when-software-books-for-the-guest}
## Agentic Booking: When Software Books for the Guest

Agentic booking is the hardest case because it combines a contract, money and a choice the traveler did not make directly. Three questions define it: **who is acting, under what authority, and with what record.**

{id: ai-in-travel-stays--who-is-acting}
### Who is acting

Each agent call carries two identities: the agent platform (a client credential, as for an affiliate) and the traveler (a delegated token). The OAuth token-exchange standard's `act` claim expresses exactly this "acting for" relation ([RFC 8693](https://www.rfc-editor.org/rfc/rfc8693), 2020), and [Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access) uses it for property-management systems acting for hotels. The reservation stores the **actor chain**: traveler, agent platform, agent session and authority ID. Without it, support, fraud and finance see an ordinary booking and cannot tell why it went wrong.

Agent traffic has its own economics. At Roomstead's run cost of about **€0.0007 per shopping request**, the pilot's 2,860 requests cost about €2 per booking against about €40 of revenue per stayed reservation ([Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics)): affordable if it converts, not if an agent polls every property in a city to keep its own price cache. **Quotas per agent platform and a look-to-book budget in the pilot agreement are part of the product**, as they are for metasearch ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)).

{id: ai-in-travel-stays--under-what-authority}
### Under what authority

There are two workable models of booking authority, and the September incident used neither:

| Authority | How it works | Fits | Breaks when |
| --- | --- | --- | --- |
| **Human final click (handoff)** | The agent searches and gets a quote; the traveler confirms on a marketplace-hosted confirmation step, in the app, a web view or an embedded checkout | Every booking type; any rate; new travelers | The agent's product promise is "done for you" and the handoff loses the traveler |
| **Mandate** | The traveler signs, in advance, specific constraints: place ID, dates, party, maximum total, refundability, property class; the gateway verifies each booking against them | Repeat, well-specified bookings: business travel, a known hotel, a rebooking after disruption | Constraints are vague ("Porto, under €200"), or the agent fills gaps with assumptions |

Expedia Group's 2026 operating model states the first as a principle: agents "can inform, compare, recommend, and help a traveler decide", and "the traveler should retain the final click for decisions such as completing a booking" ([Expedia Group Tech, 2026](https://medium.com/expedia-group-tech/building-the-operating-model-for-agentic-ai-at-expedia-group-f7555fcce506)). The second follows the shape of Google's Agent Payments Protocol, whose signed Intent Mandate "specifies the rules of engagement—price limits, timing, and other conditions" and whose Cart Mandate records "the exact items and price" the user approved ([Google Cloud, 2025](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)). What Frontdoor's pilot had was a third, unworkable model: **a broad scope with a price cap**, which delegated every other choice to the model.

![Swimlanes for traveler, AI agent, gateway and reservations: an ambiguous Porto search goes back to the traveler, who chooses Portugal; a binding quote and summary are shown, the traveler confirms, and the gateway books.](stays-marketplace-architecture/posts/46-ai-in-travel-stays/assets/images/46-ai-in-travel-stays/46-agentic-booking-porto.jpeg)

**Figure 4:** *Agentic booking as Corvane redesigned it: ambiguity goes back to the traveler, the price comes from a binding quote, the platform writes the summary, and the booking records who acted under which authority.*

Payment authority sits under booking authority. A mandate that allows a booking does not by itself satisfy strong customer authentication (SCA), the two-factor rule for European card payments; whether a given agent-initiated charge can use an exemption or a merchant-initiated transaction is a question for the payments team and the acquirer, not for the agent ([Paying for a Future Night: Payment Orchestration for Stays](#stay-payments)). My reading as of 2026 is that the rules for agent-initiated payments are still settling, and that a marketplace should design for a step-up to the traveler rather than assume it can be avoided.

{id: ai-in-travel-stays--with-what-record}
### With what record

Of the three records that must agree (the traveler's instruction, the agent's choice, the reservation), the marketplace holds only the last two. My rule is that **the reservation stores everything the marketplace showed the agent and everything the agent sent**: the resolution candidates and the chosen ID, the quote and its summary, the authority (confirmation event or mandate) and the actor chain. Pilot agreements should require agent platforms to keep the instruction and make it available in disputes. With that record, the Porto case is answerable in minutes.

{id: ai-in-travel-stays--hosted-stays-harder-than-it-looks}
### Hosted stays: harder than it looks

A night in a home is a harder thing for an agent to book than a hotel room. Request-to-book listings need a message to the host. House rules (no parties, quiet hours, pets) are accepted by the guest, and an agent cannot accept them on a person's behalf in any meaningful way. Reservation screening ([Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety)) uses signals about the guest's account and behavior that an agent session distorts: a new device, booking for someone else, many searches in one session, the same profile that [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) treats as risky.

{id: ai-in-travel-stays--ai-for-hosts-and-partners}
## AI for Hosts and Partners

On the supply side, AI writes, replies and prices. The documented examples are partner tools: Booking Holdings' 10-K lists partner-facing "Smart Messenger" and "Auto-Reply" ([Booking Holdings 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm)), Airbnb's 2026 evaluation post lists "smart communication features for guests and hosts" ([Airbnb, 2026](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788)), and Booking.com's onboarding agent targets self-managed partners without an account manager, mostly homes and small properties.

The architectural rules are short because the domain chapters already own the objects:

- **A generated listing or reply is a draft the host owns.** It records provenance and is approved before publishing, and every claim in it must exist in the structured listing data ([Describing a Stay: Content, Media and Property Mapping](#content-and-media)). An extracted amenity ("crib available") becomes a filter that guests rely on, so it needs the same evidence as a typed one.
- **A delegated writer acts under a grant.** An assistant that changes prices or replies to guests for a host is a delegate with scopes, like a co-host or a property-management system ([Running the Supply Side: Extranets, Host Tools and Operations](#extranets-and-host-tools)). It inherits the rate limits, precedence and provenance of the connectivity layer ([Plugging Into the Hotel Stack: Connectivity, Channel Managers and Standards](#connectivity-and-channel-managers)) and the guardrails of automatic pricing ([Setting the Price of a Night: Revenue Management and Smart Pricing](#dynamic-pricing)).
- **Message assistants respect stage.** A reply drafted before booking must pass the same contact-detail and payment-link checks as a human message; a reply after booking must not be blocked by them. Corvane learned the second rule the hard way in August 2027, when a detector aimed at pre-booking scams redacted check-in codes ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)).

{id: ai-in-travel-stays--ai-in-trust-both-sides-of-the-contest}
## AI in Trust: Both Sides of the Contest

Trust and safety is where AI helps defenders most and attackers too. Airbnb's 2025 10-K says "AI capabilities now assist in risk assessment and rapid fraud and scam detection" ([Airbnb 10-K, 2026](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm)). Language models are good at reading messages, listing text and reviews for intent: a payment request disguised as a "verification step", a listing copied from another city, a cluster of reviews written in one voice. Attackers use the same tools: AI-written phishing is fluent in every language, which is why [Stolen Cards, Hijacked Extranets and Fake Homes: Fraud in Travel](#travel-fraud) argues for defenses based on structure (new payment destinations, links in post-booking messages, bursts of activity) rather than bad grammar. Fake reviews generated at scale are banned outright in the United States by the Federal Trade Commission's 2024 rule on consumer reviews ([Trustworthy Reviews: Collection, Integrity and Quality Operations](#reviews-and-reputation)).

The architecture adds one rule to [Trust as a Platform: Trust and Safety for Stays](#stays-trust-and-safety): **a language model can classify, summarize and propose, but an enforcement decision goes through the decision service** with a policy reference, a statement of reasons and a contest path, like any tier 3 model.

{id: ai-in-travel-stays--evaluation-cost-and-liability}
## Evaluation, Cost and Liability

{id: ai-in-travel-stays--evaluate-against-the-systems-of-record}
### Evaluate against the systems of record

Evaluation of generative features is now documented practice. Airbnb samples "5% of live de-identified traffic daily, run[s] programmatic checks + virtual judges, and surface[s] flagged outputs for human review" ([Airbnb, 2026](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788)). Booking.com's AgentHub scores factual accuracy, context and answer relevance, instruction following and user frustration with model judges. Expedia Group calls evaluations "the new PRD" (product requirements document), the place where expected behavior and unacceptable failures are written down before building.

Stays add a cheaper and stronger check: **many claims an assistant makes can be verified deterministically.** A price can be compared with the quote it should have come from; a cancellation statement with the policy engine's answer for that reservation; a place with the resolved place ID; an amenity with the listing data. I would build a **claim checker** that extracts prices, dates, places and policy statements from sampled conversations and compares them with the systems of record, and keep model judges for tone and helpfulness. A golden set of hard cases belongs in every release gate: ambiguous place names, stays across a daylight-saving change, children's ages and tourist taxes, non-refundable rates, mixed currencies.

{id: ai-in-travel-stays--cost}
### Cost

Generative AI changes unit costs in both directions. Corvane's illustrative figures for the fourth quarter of 2027:

| Unit | Cost (illustrative) | Compared with |
| --- | --- | --- |
| Support assistant conversation (model calls plus tools) | about **€0.21** | €9.80 per Roomstead support case handled by people |
| Conversational search session in the Nookaway app (average 7 model calls) | about **€0.05** | €0.0031 per ordinary Nookaway search request |
| Agent shopping request through Frontdoor | about **€0.0007** (platform cost only) | Same as any shopping request; the agent platform pays for its own model |
| Generated listing draft | about **€0.02** | One-off per listing version |

Support assistants pay for themselves only if they resolve, which is why [When Something Goes Wrong: Customer Service and Recovery](#customer-service) measures verified resolution, not containment. Conversational search costs about 16 times an ordinary search request per session, so it is worth running where intent is vague and value is high, not as the default search box. The AI platform's gateway should meter cost per use case and per model, and route simple tasks to cheaper models. Expedia Group's 2026 principles put it as "optimize for return on cost" and "justify complexity against strong baselines" ([Expedia Group Tech, 2026](https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9)).

{id: ai-in-travel-stays--liability-and-regulation}
### Liability and regulation

The legal position is simpler than the technology. **A company is responsible for what its assistant tells customers.** In *Moffatt v. Air Canada* (2024 BCCRT 149, decided 14 February 2024), British Columbia's Civil Resolution Tribunal rejected the airline's argument that its chatbot was "a separate legal entity that is responsible for its own actions" and found the airline liable for the chatbot's wrong statement about a bereavement-fare refund ([Civil Resolution Tribunal, 2024](https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do)). The award was about C$812; the principle covers every refund, cancellation and fee statement a stays assistant makes.

In the EU, four sets of rules apply:

| Rule | What it requires of a stays marketplace's AI (my reading, as of October 2026) |
| --- | --- |
| **AI Act** ([Regulation (EU) 2024/1689](http://publications.europa.eu/resource/celex/32024R1689)) | Article 50, applicable from 2 August 2026: systems "intended to interact directly with natural persons" must inform them that they are interacting with an AI system unless that is obvious. Most stays uses are not high-risk; [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) covers the classification, including the Annex III exception for fraud detection and the possible high-risk status of AI that allocates work to and evaluates support agents. Obligations on general-purpose models fall mainly on their providers |
| **General Data Protection Regulation (GDPR)** ([Regulation (EU) 2016/679](http://publications.europa.eu/resource/celex/32016R0679)) | A lawful basis and minimization for conversation data, which is rich in personal data; Article 22 safeguards for solely automated decisions with significant effects, such as blocking a booking |
| **Consumer law** | Price and policy statements by an assistant are commercial practices of the marketplace; total-price rules apply to what it quotes ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)) |
| **Digital Services Act** ([Regulation (EU) 2022/2065](http://publications.europa.eu/resource/celex/32022R2065)) | Recommender transparency and statements of reasons for content decisions apply whether a person, a rule or a model made them ([Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation)) |

For agentic booking, the open question is the contract. The traveler is the party to the booking, and the agent platform is acting for them; but when the agent chose a wrong place under a vague grant, the commercial answer is set by the pilot agreement, not by settled law. I would write the allocation into the agreement: the marketplace answers for its tools' outputs (a wrong price in a quote, a place resolver that hid ambiguity), the agent platform answers for choices outside the authority it was given, and the reservation record decides which happened.

{id: ai-in-travel-stays--in-practice-at-corvane-frontdoor-v2-and-one-register}
## In Practice at Corvane: Frontdoor v2 and One Register

On **19 October 2027** the architecture forum took the Porto review, the pilot sweep and a proposal from Mariana Costa, Kenji Arai and Noor van Dijk, Head of Regulatory Affairs and Privacy. It agreed six things.

**1. One AI use-case register, in Kiln.** Every AI use, built or bought, internal or external, gets a register entry with an owner, a consequence class, approved tools and an evaluation plan, extending the model registry of [Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform) rather than creating a second one. Frontdoor was registered as a money-or-contract use with Roomstead's head of distribution as owner. The first inventory found **23** generative AI uses across the group, **8** of them without a named owner; one, a vendor's reply-suggestion feature switched on in Roomstead's support desk software, sent conversation text to a model provider outside the group's data agreements and was switched off the same week.

**2. A group AI gateway.** Kenji's team adds a model gateway to Kiln: routing across model providers, cost metering per use case, guardrails for prompt injection and personal data, and traces of every prompt, tool call and response, retained for 90 days and linked to case and reservation IDs.

**3. A tool registry with side-effect classes.** Tools are owned by the domain teams: place resolution by Jonas Weber's search team (backed by Waypoint from 2028), offers by the offer kernel's owners, cancellation answers by the Clause policy engine, recovery by Harbor, enforcement by Warden. No AI use may call a domain service except through a registered tool.

**4. Frontdoor v2, live 15 November 2027**, rebuilt over **Gangway**, the group partner distribution API the forum had approved a week earlier ([Where Guests Come From: Web, Apps, Metasearch and Partner Distribution](#demand-channels)), so agents share its quotas and offer contract. Place resolution returns ranked candidates and an ambiguity flag; the agent must ask when the flag is set. Quotes are binding for 15 minutes and carry a canonical summary that agents must show verbatim. **Handoff is the default**; mandate bookings are allowed only for refundable rates, with the place ID, dates, party and maximum total signed by the traveler. The reservation stores the actor chain and everything Frontdoor returned. Each agent platform has a quota and a look-to-book budget of 3,000 shopping requests per booking, reviewed quarterly.

**5. Nookaway: search and handoff only.** Rafael Mendes, VP Engineering at Nookaway, argued that agents cannot accept house rules or send a meaningful request to a host, and that reservation screening was not designed for agent sessions. The forum agreed: through 2028, agents may search Nookaway and get quotes, and every booking is completed by the guest on a Nookaway page.

**6. Claim checking before scale.** Every assistant that states prices, policies or places runs a daily claim check on a 5% sample against the systems of record; a use case cannot widen its scope while its claim-error rate is above 0.5%.

The illustrative first weeks of Frontdoor v2:

| Measure | Pilot (July–September 2027) | Frontdoor v2 (15 November–31 December 2027) |
| --- | --- | --- |
| Bookings | 1,610 | 1,240 |
| Share completed through handoff | 26% | 83% |
| Searches flagged ambiguous | not measured | 3.4% |
| Confirmed wrong-place bookings | 9 | 0 |
| Shopping requests per booking | about 2,860 | about 2,350 |
| Quoted price differing from booked price | not measured | 0.2% |

Bookings per week fell: the handoff loses some travelers, and that is the price of the final click. A mid-2028 review will decide whether to widen mandates to non-refundable rates.

![A new AI use is registered, its consequence class routes it to light review, limits and authority, or human review, it goes live with traces, and claim errors loop back to the register.](stays-marketplace-architecture/posts/46-ai-in-travel-stays/assets/images/46-ai-in-travel-stays/46-ai-governance-loop.jpeg)

**Figure 5:** *AI governance at Corvane: every use is registered with an owner and a consequence class, the class sets the controls, and production evidence feeds back into the register.*

{id: ai-in-travel-stays--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Where the traveler meets AI | Own assistant in the marketplace's apps | Expose tools to third-party assistants | Brand, loyalty and data matter most; high direct traffic | Assistants are becoming the front door; the marketplace wants the booking wherever intent starts |
| Booking authority for agents | Human final click on a marketplace-hosted step | Signed mandate verified by the gateway | Default; new agents, ambiguous or non-refundable bookings | Repeat, well-specified bookings; business travel; disruption rebooking |
| Agent interface | MCP server for agent platforms | Plain HTTP API, as for affiliates | The main agent platforms speak MCP and the marketplace wants to be inside them | A few large partners with negotiated integrations |
| AI platform | One group gateway, register and tool registry | Each team picks its models and tools | More than a handful of AI uses; shared tools; regulation | Very early exploration; one team, one use |
| Models | Frontier models via API, routed | Self-hosted or fine-tuned models | Quality and speed of change matter more than unit cost | High-volume, narrow tasks where a smaller model meets the claim-check bar |
| Grounding | Tools over live services | Retrieval over documents | Prices, availability, policies, reservations | Help content, house manuals, long-form property descriptions |

For a group like Corvane I would take option A on the second, fourth and sixth rows, both on the first and third, and route models per task. For a single marketplace with one assistant, a group register is premature; tool discipline and claim checking are not.

{id: ai-in-travel-stays--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

AI does not change the basic difference between the two marketplaces: it makes it more visible.

| Aspect | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| Content for AI to ground on | Standardized room types and amenities, large review corpora | Unique, host-written listings; attributes must be extracted from text and photos first |
| Natural-language search | Words become filters over a standard vocabulary | Soft preferences ("quiet", "good for kids") need extracted attributes with evidence |
| Agentic booking | Instant confirmation, rate-plan terms, binding quotes: well suited to agents with authority | Request-to-book, house rules and screening make autonomous agent booking unsafe for now |
| Support assistant's hard part | Actions that need a supplier: changes, cancellations, waivers through connectivity | Judgement between two private parties: failed check-in, accuracy, damage |
| What can be shared | AI gateway, register, tool registry, claim checker, agent identity | Same |

**My judgement: share the whole AI layer and none of the booking authority rules.** The gateway, register, tool registry, traces, claim checker and agent identity are the same machinery for both brands. What an agent may do differs, because a hotel room under a binding quote is a well-defined contract and a night in someone's home is not yet one that software can accept for a person.

{id: ai-in-travel-stays--failure-modes}
## Failure Modes

**The pilot without an owner.** An agent channel launched as a distribution experiment, with no register entry, no evaluation and no incident path, until a guest arrives in the wrong town. Every AI use needs an owner on day one.

**Broad scopes with a cap.** "Book on my behalf, up to €1,000" delegates place, rate and refundability to the model. Authority must name the decisions it covers.

**The model as source of truth.** An assistant that states prices, fees or cancellation terms from its context, a summary or a cached feed adds another price and another policy to the platform, and the marketplace owns both.

**Silent disambiguation.** Place names, dates near midnight, party size and children's ages are all resolved somewhere. When a tool resolves them silently, nobody can show the traveler what was chosen.

**Unbounded agent traffic.** Agents that poll to keep their own price caches turn a channel into a load problem; agreements without quotas repeat the early years of metasearch.

**Shadow AI in vendor tools.** A feature switched on inside bought software sends conversation text to a model provider outside the group's agreements. The register must cover what is bought.

{id: ai-in-travel-stays--the-chief-architect-s-view}
## The Chief Architect's View

**What to decide.** Five decisions are mine to frame, with the owners named. First, **the AI use-case register and the consequence classes**, with legal, privacy and the ML platform: one register for built and bought AI. Second, **the tool contracts**: which domain services are exposed to AI, with what responses and side-effect classes, owned by the domain teams. Third, **booking authority for agents**: handoff by default, mandates by exception, decided with the brand leaders and payments. Fourth, **the agent channel's commercial terms**: quotas, look-to-book budgets, the record each side keeps and the liability split, with distribution and legal. Fifth, **the AI platform's scope**: what is shared, which models are approved for which data, and cost allocation, with the ML platform lead.

**Who decides.** The architecture forum approves classes, tool contracts and authority rules; the register's owner (at Corvane, Kenji Arai) runs it; regulatory affairs (Noor van Dijk) is a mandatory reviewer for any use that talks to guests or decides about people; the brand leaders decide where AI meets their customers.

**What to watch.** The claim-error rate per assistant; the share of agent bookings completed by handoff and the drop-off at handoff; wrong-place, wrong-date and wrong-rate contacts from agent bookings; agent shopping requests per booking; cost per resolved conversation; and the number of AI uses without an owner, which should be zero.

**The long view.** A large share of travel intent will arrive through assistants the marketplace does not control. The marketplaces that do well will be those whose contracts software can use directly: a place resolver that admits ambiguity, a binding quote, a precise policy engine, a reservation record that says who acted. That is the investment this book argues for in every part. **AI does not reduce the need for clean marketplace contracts; it removes the humans who used to hide their gaps.**

{id: ai-in-travel-stays--questions-to-ask}
## Questions to Ask

1. Can we list every AI use in the group, built or bought, with an owner and a consequence class?
2. Does every price, availability, policy or place an assistant states come from a tool over a system of record, with a quote or decision ID we can check?
3. When a place name, a date or a party is ambiguous, does the tool say so, and does the agent have to ask the human?
4. What authority does a third-party agent need to book, and does the authority name the place, dates, total and refundability?
5. Does every agent-made reservation record the actor chain and everything our tools returned, so that a dispute can be settled from our records?
6. Do we measure claim errors against the systems of record, or only judge-scored helpfulness?
7. What can an AI do that a first-line human in the same role could not? The answer should be nothing.
8. Who answers to a guest, a regulator or a court for what our assistant said yesterday?

The architecture in this chapter rests on contracts that will outlive any model: places, offers, policies, reservations and authority. [Built for the Next Disruption: Evolving a Stays Platform Over a Decade](#evolving-the-platform) closes Part IX by asking how a Chief Architect keeps those contracts coherent over a decade of disruptions, of which AI is only the most recent.

{id: ai-in-travel-stays--sources-and-evidence}
## Sources and Evidence

{id: ai-in-travel-stays--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Booking.com Launches New AI Trip Planner](https://www.bookingholdings.com/press-releases/booking-com-launches-new-ai-trip-planner-to-enhance-travel-planning-experience/) — Booking Holdings, 2023. Trip planner on own ML models and the ChatGPT API, showing Booking.com prices.
- [Booking.com Enhances Travel Planning with New AI-Powered Features](https://www.bookingholdings.com/press-releases/booking-com-enhances-travel-planning-with-new-ai-powered-features-for-easier-smarter-decisions/) — Booking Holdings, 2024. Smart Filter, Property Q&A, Review Summaries.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1075531/000107553126000009/bkng-20251231.htm) — Booking Holdings Inc., 2026. AI agents as disintermediation risk; partner-facing Smart Messenger and Auto-Reply.
- [Introducing AgentHub: Booking.com Platform for Modular Travel AI Agents](https://booking.ai/introducing-agenthub-booking-com-platform-for-modular-travel-ai-agents-68bc521a0f50) — Beladev, Harush and Ross, Booking.com, 2026. Agent and tool definitions, tracing, LLM judges, guardrails, Q&A agent results.
- [From Static Help Content to a RAG-Based Onboarding Agent for Partners](https://booking.ai/from-static-help-content-to-a-rag-based-onboarding-agent-for-partners-f7d5a789c4f7) — Barchukova et al., Booking.com, 2026. Grounding in help content; templated answers for legally restricted questions.
- [Introducing TripGenie](https://www.trip.com/newsroom/introducing-tripgenie-groundbreaking-ai-travel-assistant) — Trip.com Group, 2023. Assistant opening app pages with filters applied.
- [Building the Operating Model for Agentic AI at Expedia Group](https://medium.com/expedia-group-tech/building-the-operating-model-for-agentic-ai-at-expedia-group-f7555fcce506) — Expedia Group Technology, 2026. Agent definition, evals as requirements, registration and risk rating, MCP governance, the traveler's final click.
- [How Expedia Group Builds AI That Lasts at Scale](https://medium.com/expedia-group-tech/how-expedia-group-builds-ai-that-lasts-at-scale-434677770fe9) — Expedia Group Technology, 2026. Return on cost, strong baselines, agentic release tollgates.
- [Q3 2025 Shareholder Letter](https://s26.q4cdn.com/656283129/files/doc_financials/2025/q3/v2/Airbnb_Q3-2025-Shareholder-Letter.pdf) — Airbnb, Inc., 2025. Assistant cancels and changes dates from chat.
- [Q4 2025 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312526048670/d58192dex991.htm) — Airbnb, Inc., 2026. Natural-language search test.
- [Q2 2026 Shareholder Letter](https://www.sec.gov/Archives/edgar/data/1559720/000119312526337928/d70413dex991.htm) — Airbnb, Inc., 2026. Assistant in 50+ languages; nearly 45% resolved without a human.
- [Form 10-K for fiscal year 2025](https://www.sec.gov/Archives/edgar/data/1559720/000155972026000004/abnb-20251231.htm) — Airbnb, Inc., 2026. AI in risk assessment and scam detection.
- [Eval-driven development: Lessons from evaluating GenAI at scale](https://medium.com/airbnb-engineering/eval-driven-development-lessons-from-evaluating-genai-at-scale-e817e5ae5788) — Airbnb Engineering, 2026. Daily 5% sampling, programmatic checks and model judges; GenAI features for guests and hosts.
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anthropic, 2024. MCP as an open standard for connecting AI applications to data and tools.
- [Powering AI commerce with the new Agent Payments Protocol (AP2)](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) — Parikh and Surapaneni, Google Cloud, 2025. Intent and Cart Mandates as signed evidence of user instructions.

{id: ai-in-travel-stays--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2024/1689 (Artificial Intelligence Act)](http://publications.europa.eu/resource/celex/32024R1689) — European Parliament and Council, 2024. Article 50 transparency; Annex III high-risk list.
- [AI Act implementation timeline](https://ai-act-service-desk.ec.europa.eu/en/ai-act/timeline/timeline-implementation-eu-ai-act) — European Commission AI Act Service Desk, live October 2026. Application dates as amended, including Article 50 from 2 August 2026.
- [Regulation (EU) 2016/679 (GDPR)](http://publications.europa.eu/resource/celex/32016R0679) — European Parliament and Council, 2016. Article 22 safeguards for automated decisions.
- [Regulation (EU) 2022/2065 (Digital Services Act)](http://publications.europa.eu/resource/celex/32022R2065) — European Parliament and Council, 2022. Recommender transparency and statements of reasons.
- [RFC 8693: OAuth 2.0 Token Exchange](https://www.rfc-editor.org/rfc/rfc8693) — IETF, 2020. The `act` claim for delegated actors.
- [Moffatt v. Air Canada, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/crtd/en/item/525448/index.do) — Civil Resolution Tribunal of British Columbia, 2024. A company is liable for its chatbot's statements.

{id: ai-in-travel-stays--research-and-practitioner-sources}
### Research and practitioner sources

- [OpenAI launches apps inside of ChatGPT](https://techcrunch.com/2025/10/06/openai-launches-apps-inside-of-chatgpt/) — TechCrunch, 2025. Booking.com and Expedia among launch apps; system built on MCP.
- [Expedia Group shares AI chatbot lessons learned](https://letsdatascience.com/news/expedia-group-shares-ai-chatbot-lessons-learned-239f348a) — Let's Data Science, 2026. Secondary, low-confidence report on Romie's discontinuation and grounding.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
