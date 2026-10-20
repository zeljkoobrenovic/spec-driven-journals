{id: ai-in-listing-systems}
# 44. AI Across the Listing Lifecycle

![AI Across the Listing Lifecycle — logo](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Walk the listing lifecycle from creation to search, moderation, pro tooling and valuation, see where AI and agents have actually shipped at marketplaces between 2023 and 2026, design the layer that controls them, and follow Veldmark's photo-to-listing assistant from a cargo-bike photo to a published, validated listing.

> **WHY THE BUSINESS CARES:** AI can cut the effort of listing an item from minutes to seconds, turn vague buyer wishes into searches that find something, and help pros answer leads faster, all of which is liquidity. It also creates new costs per call, a new channel where buyers search inside other companies' assistants, and new ways for fraudsters to produce convincing fakes at scale.

> **WHY ARCHITECTS SHOULD CARE:** Generative models produce plausible output, not valid output. Without a layer that validates every suggestion against the taxonomy, the attribute dictionary and the trust rules, AI fills the catalog with confident errors. And once external agents call the marketplace's search, search becomes an API product with contracts, quotas and attribution.

> **KEY POINTS:**
>
> * **Let AI propose and the platform decide.** Every documented success in classifieds uses the model to translate intent into existing structures (category and attributes from a photo, filters from a sentence, a policy label from a message) while the structured systems remain the system of record. Validate every proposal against the schema, record its provenance, and keep humans in the loop where the law or the consequence requires it.
> * **Discovery is leaving the marketplace's own surfaces.** In 2026 marketplaces ship their search as apps inside ChatGPT and as tools for external agents, while AI crawlers harvest listing data without asking. Structured, API-grade inventory, a bot and licensing policy, and attribution for leads that arrive through assistants are now architecture.
> * **Govern AI uses by autonomy, cost and consequence.** Keep a register of every AI use with its autonomy level, owner, evaluation set, cost per outcome and kill switch. The EU AI Act adds dated obligations: disclosure for conversational systems and marking of generated content from 2026, and high-risk duties for recruitment and credit uses from 2 December 2027.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Attribute Junkyard** — Generative listing assistants that write free text into attributes, unchecked against the dictionary, produce the junkyard faster than any seller could.
> * **Moderation as an Afterthought** — An assistant that makes listing easier also makes fake listings easier, so trust and safety has to sit inside the assisted flow, not after it.
> * **The Unwatched Model** — Prompts, model versions and providers change weekly; an AI feature without an evaluation set, a cost monitor and an owner degrades without anyone noticing.

For most of their history, listing marketplaces asked people to do the work of structure. A seller had to choose a category from a tree of 1,400 leaves, fill twenty attribute fields and write a description. A buyer had to translate "a family car that fits a dog and costs less than twenty thousand" into make, body type, price and mileage filters. Every chapter in Parts II to IV of this book is, in part, about the cost of that translation. **Generative AI is the first technology that can do much of the translation for them**, and that is where its value in listing systems lies.

The same property makes it dangerous. A language model asked to fill attributes will fill them, whether or not the photo shows what it claims. A conversational assistant will answer, whether or not the inventory supports the answer. This chapter's argument is that the architecture must treat AI output as **a proposal to be validated**, never as data, and that the marketplace's structured assets (the taxonomy, the attribute dictionary, the index, the trust rules) become more valuable, not less, when AI arrives.

![An AI assistant turns photos into proposal cards that pass through a stencil checkpoint; fitting cards reach an orderly listing shelf after the seller confirms, misfits are set aside.](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/ai-proposes-platform-decides.jpeg)

**Figure 1:** *The model proposes and the platform decides: every AI output is a proposal checked against the taxonomy, the attribute schema and the trust rules before it becomes listing data.*

The chapter builds on two earlier designs: [Models in Production: ML Platforms and Use Cases](#ml-platform), which owns model governance, decision tiers and the platform for predictive models, and the taxonomy and attribute schemas of Part II ([Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies), [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas)), which AI output compiles into. It adds what generative models and agents change, and links to the chapters that own LLM-based enrichment ([From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment)), natural-language search ([What Did They Mean? Query Understanding and Autocomplete](#query-understanding)), moderation ([Trust and Safety as a Platform](#trust-and-safety-architecture)) and SEO for AI answer engines ([Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)). The next chapter, [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution), treats AI as one of the stressors the platform must absorb over a decade. The worked example belongs to Veldmark, the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)).

{id: ai-in-listing-systems--setting-the-scene-at-veldmark-six-ai-requests-in-one-quarter}
## Setting the Scene at Veldmark: Six AI Requests in One Quarter

By **November 2027**, Noor Hassan, Veldmark's Group Chief Product Officer, has six AI proposals on her desk, each from a different team and each with a vendor demo behind it.

1. **Tradeyard** wants a photo-to-listing assistant: a private seller takes photos and the app proposes category, attributes, title, description and price. Tradeyard publishes about **2.3 million** new listings a week, **78%** from private sellers, and its insertion flow is its biggest conversion funnel.
2. **Hearthly** wants conversational search in France and Spain ("three rooms near a metro, under €400,000, quiet street") and an app inside a third-party AI assistant.
3. **Motorvane** wants a dealer copilot in Dealer Hub: drafted replies to leads, price recommendations and descriptions in the dealer's tone, for its **21,400** dealers.
4. **Trust and safety** wants large language models (LLMs) in the moderation gray zone, after the July 2027 Barcelona fake-rental ring showed how fast fraudsters reuse stolen photos.
5. **Hearthly's valuation team** wants Valuo to explain its estimates in plain language.
6. **Tradeyard's SEO team** wants to know what to do about AI crawlers: about **46%** of Tradeyard's web sessions start from organic search, and bot traffic from AI companies has risen through 2027.

Aisha Rahman, Group Head of Trust & Safety, asks what happens when fraudsters use the listing assistant. Lucía Ortega, the Group Data Protection Officer and regulatory lead, asks which of the six fall under the EU AI Act. Tomasz Wiśniewski, head of the group search platform, asks who pays for an external assistant's queries at the Sunday-evening peak of 31,000 queries per second. Ingrid Halvorsen, the Group Chief Architect, asks a fourth question of each proposal: **what structured thing does the model produce, and what checks it?** The answer to that question decides the architecture, and it turns out to be the same for all six.

{id: ai-in-listing-systems--concepts-generative-ai-agents-and-autonomy}
## Concepts: Generative AI, Agents and Autonomy

- **Generative AI** — models that produce text, images, structured output or actions from prompts, typically large language models (LLMs) and vision-language models. Predictive models that score or classify are covered in [Models in Production: ML Platforms and Use Cases](#ml-platform); generative models reuse that platform for registration, logging and monitoring.
- **AI listing assistant** — a feature in the insertion flow that proposes listing content (category, attributes, title, description, price) from photos, voice or short text, for the seller to accept, edit or reject.
- **Structured-output compiler** — the pattern in which a model translates unstructured input into a structure the marketplace already has: an attribute set, a filter query, a policy label. The structure is validated deterministically before use. It is the central pattern of this chapter.
- **Agentic search** — search in which a model plans steps and calls tools (keyword or vector search, filters, comparisons, external lookups) over several turns, rather than returning one ranked list for one query.
- **Agent-to-marketplace interface** — an interface through which external AI agents call the marketplace's capabilities as tools. The most widely used such protocol as of 2026 is the Model Context Protocol (MCP). Anthropic introduced it in November 2024 as an open standard for connecting AI assistants to data sources ([Anthropic, 2024](https://www.anthropic.com/news/model-context-protocol)) and donated it to the Agentic AI Foundation under the Linux Foundation in December 2025 ([Anthropic, 2025](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation)).
- **Autonomy level** — how far an AI feature acts without a person: it *suggests*, *drafts* for confirmation, *acts with confirmation*, or *acts autonomously*.
- **AI governance for marketplaces** — the register, rules and controls that decide which AI uses may run, at what autonomy, with which data, evaluated how, at what cost, and with whom accountable.

{id: ai-in-listing-systems--the-autonomy-ladder}
### The autonomy ladder

| Level | What the AI does | Listing example | Who confirms | Typical controls |
| --- | --- | --- | --- | --- |
| Suggest | Offers options the user may pick | Category suggestions; query suggestions | User, implicitly | Offline accuracy; acceptance rate |
| Draft | Produces a complete artifact the user reviews | Description and attributes from photos; reply draft for a dealer | User, explicitly, before publication | Schema validation; provenance per field; audit sampling |
| Act with confirmation | Performs a change after a person approves | Copilot applies a price change to 40 dealer listings after the dealer clicks "apply" | User, per action or batch | Preview of effects; undo; rate limits |
| Act autonomously | Performs a change or decision without approval | Auto-withholding a suspicious message; auto-renewing listings | Nobody at the time; reviewed later | Gate-tier governance (see [Models in Production: ML Platforms and Use Cases](#ml-platform)); appeals; legal duties |

The rule I use for listing systems: **anything that changes what buyers see about a seller's listing stays at "draft" or below unless the seller has opted in**, and anything that restricts a user's rights follows the trust-and-safety rules for automated decisions.

{id: ai-in-listing-systems--where-ai-has-shipped-the-lifecycle-in-public-evidence}
## Where AI Has Shipped: The Lifecycle in Public Evidence

Between 2023 and 2026, marketplaces shipped AI at every stage of the listing lifecycle. Most entries are company announcements rather than engineering accounts; where a source is trade press or a third-party summary, it is labeled.

| Lifecycle stage | Documented example | Date | What it shows |
| --- | --- | --- | --- |
| Listing creation | eBay's "magical listing": generative descriptions from title and category, then photo-to-listing filling title, description, category and item specifics with price and shipping suggestions; iOS beta first; built on Azure OpenAI ([eBay, 2023](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/)) | September 2023 | Text assist first, photo second |
| Listing creation | Kleinanzeigen: AI description helper (August 2025), then photo-to-listing proposing title, description and category across almost all categories except vehicles, jobs and services ([mobiflip, trade press, 2025](https://www.mobiflip.de/kleinanzeigen-fuehrt-ki-gestuetzte-anzeigenerstellung-per-foto-ein/amp/)) | November 2025 | High-structure verticals excluded at first |
| Listing creation | OLX Auto Description: draft from a photo plus basic details, reviewed by the seller; human evaluation of 98% for style and relevance and 89% for faithfulness ([OLX Group, 2026](https://www.olxgroup.com/news/how-olx-uses-ai-to-reduce-repetitive-work/)) | August 2026 | Faithfulness is measured separately from fluency |
| Enrichment | OLX extracted job roles from job-ad text with an LLM service subscribed to ad events; about 4,000 requests a day cost "approximately 15K per month" (currency unstated), which prompted evaluation of self-hosted models ([OLX Tech, 2024](https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659)) | January 2024 | Event-driven enrichment; cost per call matters |
| Search | coches.net (Adevinta Spain): natural-language car search converted to the site's existing filters by Claude Haiku on Amazon Bedrock, after a cheap moderation pre-classifier; about 20,000 calls a day for about €19 a day ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/)) | November 2024 | The LLM compiles filters; it does not run the search |
| Search | leboncoin: conversational assistant turning preferences into JSON for its product search API; guardrail prompts replaced by fine-tuning for latency; a hosted assistant service rejected because conversations would be stored by the vendor ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/building-a-smarter-shopping-experience-the-technology-behind-conversational-search-in-e-commerce/)) | March 2024 | Data residency of conversations is a design input |
| Agentic search | OLX Magic: an agent calling text, visual and web search tools over hybrid retrieval, with latency of about 5–10 seconds against 300–500 ms for classic search; a blank chat interface was replaced by the familiar search bar and filters with AI built in ([ZenML LLMOps database, third-party summary of a 2024 talk](https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture)) | 2024 | "Only as good as your search" |
| Off-platform agents | OLX CompassGPT (property, Imovirtual) and AutoGPT (cars, Otomoto first) run as apps inside ChatGPT, built with OpenAI; OLX reports buyers finding a vehicle "at least 20% faster" ([OLX Group, 2026](https://www.olxgroup.com/news/olx-launches-autogpt-agentic-ai-assistant-transforming-automotive-search-across-europe/)) | February and April 2026 | Discovery on someone else's surface; company-reported outcome |
| Off-platform agents | ImmoScout24 shipped an MCP server for its assistant in November 2025 and an app in ChatGPT; the MCP server was designed to be "completely stateless", and cached tool descriptors forced a rotation of production environments ([Scout24 Engineering, 2026](https://medium.com/scout24-engineering)) | January and March 2026 | Agent channels have their own release mechanics |
| Moderation | OLX "Chat Images GenAI" detects suspicious images and QR codes in chat in real time; fraudulent images are "around 30% of all fraud cases on the platform in Poland" ([OLX Group, 2026](https://www.olxgroup.com/?p=4590)) | January 2026 | Generative models in the gate tier, on a narrow task |
| Pro copilots | OLX AutoIQ for Otomoto dealers: listing creation, lead dashboard, follow-up and pricing recommendations, descriptions in the dealer's tone; dealers publish "up to 36% faster" ([OLX Group, 2026](https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/)) | February 2026 | Copilots sit on pro tooling, not on buyer surfaces |
| SEO | Adevinta's SEO team used AI to classify keywords, generate related searches and write meta titles and descriptions ([Adevinta Tech Blog, 2023](https://adevinta.com/techblog/how-we-attract-users-with-seo-from-ten-blue-links-to-ai-generated-answers/)) | June 2023 | Predates Google's AI answers; do not extrapolate |

Three patterns run through the table. **Every implementation keeps the structured system of record**: the filters, the category tree, the index and the ranking model remain, and the model translates into them. **Rollouts are staged by structure**: text help first, photos second, high-structure verticals such as vehicles last. And **the biggest 2026 change is distribution, not modeling**: marketplaces now publish their search into assistants they do not control, which reverses the long-held assumption that discovery happens on the marketplace's own surfaces.

{id: ai-in-listing-systems--architecture-the-control-layer-between-models-and-listings}
## Architecture: The Control Layer Between Models and Listings

{id: ai-in-listing-systems--four-components-the-ml-platform-lacks}
### Four components the ML platform lacks

An AI feature in a listing system has four parts that the predictive-ML platform does not already provide, plus the guardrails that sit around them.

1. **An AI gateway** through which every model call passes: authentication, routing between providers and self-hosted models, rate limits, cost metering per feature and per tenant, logging of prompts and outputs (with personal data handled per the retention rules), and a kill switch per feature.
2. **A prompt and configuration registry**: prompts, few-shot examples, output schemas and model choices versioned like code and registered like models, so that "the assistant got worse on Tuesday" can be traced to a change.
3. **Tools over the marketplace's own capabilities**: the taxonomy and attribute service, the search API, the price models, the trust-and-safety checks. Models call these rather than guessing.
4. **An evaluation harness**: golden sets per language, category and use, run before every prompt or model change and continuously on sampled production traffic.

Around them sit **validators**: deterministic checks that an output conforms to the attribute dictionary, the filter schema or the policy taxonomy, and **guardrails** that block outputs containing contact details, payment instructions, prohibited items or unsupported claims.

![Diagram: Models never write to systems of record directly](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/fig02-models-never-write-systems-record-directly.jpeg)

**Figure 2:** *Models never write to systems of record directly: every output passes a deterministic validator and a guardrail, and reaches listings, search or catalog only through the same tools and contracts that the rest of the platform uses.*

{id: ai-in-listing-systems--boundaries-that-matter}
### Boundaries that matter

- **Model output is never a listing field until a validator and a person accept it.** The listing aggregate's invariants (see [The Listing Aggregate: Identity, Lifecycle and Invariants](#listing-aggregate)) apply to AI-suggested values exactly as to typed ones.
- **Every field carries provenance.** The attribute-provenance model from [From Raw Supply to Usable Listings: Normalization and Enrichment](#normalization-and-enrichment) gains values for `ai_suggested`, `seller_confirmed` and `seller_edited`, so that search, trust and analytics can tell what a seller asserted from what a model inferred. This matters legally too: a seller is responsible for a description they confirmed, and the marketplace for one it published unconfirmed.
- **The search index stays the retrieval layer.** Conversational and agentic search compile into the same filter schema and call the same search API; generated answers never describe listings the index did not return (see [What Did They Mean? Query Understanding and Autocomplete](#query-understanding)).
- **Trust and safety runs on assisted content too.** An assisted listing goes through the same moderation pipeline as any other, with the assistant's own signals added (see below).

{id: ai-in-listing-systems--model-choice-and-hosting}
### Model choice and hosting

| Option | Strengths | Weaknesses | Fits |
| --- | --- | --- | --- |
| Frontier model through a provider API | Best quality on open-ended tasks; no infrastructure | Cost per call; data-processing terms; latency; provider changes | Low-volume, high-value tasks: pro copilots, explanation, conversational search pilots |
| Small or mid-sized model through an API | Low cost; fast | Weaker on hard cases | High-volume structured tasks: filter compilation, category proposals |
| Self-hosted open model, possibly fine-tuned | Cost control at volume; data stays in-house | GPU operations; evaluation is yours | Steady, high-volume extraction and classification once the task is stable |
| Distilled classical model | Cheapest at scale; predictable | Needs labels; narrow | Tasks where LLM outputs have produced enough labels to train on |

The documented trajectory matches the table: leboncoin moved guardrails from prompts into fine-tuning for latency, and OLX's job-role extraction cost prompted an evaluation of self-hosted models. My rule: **start with an API to learn the task, then move volume down the table as the task stabilizes and labels accumulate**, keeping the gateway so that the move is a routing change, not a rewrite.

{id: ai-in-listing-systems--veldmark-worked-example-the-photo-to-listing-assistant}
## Veldmark Worked Example: The Photo-to-Listing Assistant

{id: ai-in-listing-systems--five-steps-before-the-seller-confirms}
### Five steps before the seller confirms

Tradeyard's assistant was approved for a pilot on **Monday 15 November 2027**: Tradeyard Netherlands, iOS first, goods categories only, excluding vehicles, property, jobs and services, for 5% of private sellers. The exclusions follow the documented sequence at eBay and Kleinanzeigen and Tradeyard's own constraint: vehicles need decoded vehicle data, not photos, and property needs addresses and mandatory disclosures.

It depends on two Common Ground capabilities that went live just before it: the **group taxonomy and attribute service** (October 2027), which publishes the category tree and each category's attribute schema as machine-readable reference data, and the **shared trust-and-safety platform** for Tradeyard Netherlands and Belgium (November 2027). Without the first, the model would have nothing to compile into; without the second, nothing would check what it produced.

1. **Screen the photos before generating anything.** Perceptual hashes are compared against live listings and known scam images, and an image classifier checks for prohibited items. A match stops the assistant: the seller continues manually and the listing is flagged for review. The assistant never makes a stolen photo easier to list.
2. **Propose a category** from the photos with a vision-language model, constrained to the current leaf categories returned by the taxonomy service. The model ranks candidates; it cannot invent a category.
3. **Propose attributes** for that category's schema only, each with a confidence, returning `unknown` rather than a guess where the photos do not show the value. Values must come from the attribute dictionary's enumerations or pass its type and unit rules.
4. **Propose a price range** from Tradeyard's existing price-hint model (a predictive model registered in the group registry; see [Models in Production: ML Platforms and Use Cases](#ml-platform)), not from the language model. **The language model never produces a number that a buyer will rely on.**
5. **Draft a title and description** from the confirmed category and attributes, in the seller's language, with guardrails that strip contact details, URLs, payment instructions and claims not supported by the attributes.

The seller sees all five as an editable form and must confirm before publishing. The published listing carries a small label, "Description drafted with AI and checked by the seller", and per-field provenance.

![Diagram: The language model ranks categories from an allowed list, fills a schema it is given, and writes prose last](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/fig03-language-model-ranks-categories-allowed-list.jpeg)

**Figure 3:** *The language model ranks categories from an allowed list, fills a schema it is given, and writes prose last; the price comes from a registered predictive model and the photos are screened before any generation starts.*

{id: ai-in-listing-systems--one-listing-a-utrecht-cargo-bike}
### One listing: a Utrecht cargo bike

On **Monday 6 December 2027 at 19:05 CET**, a private seller in Utrecht photographs his electric cargo bike four times. The trust check finds no hash matches. The assistant proposes **Bikes › Cargo**, one of the canonical leaves of the bikes split released on 1 November 2027, with a confidence of 0.94. For the schema it fills seven of nine attributes: brand (read from the frame decal), electric assist (yes), box position (front), number of wheels (two), color, frame size and condition (good). It returns `unknown` for battery capacity and model year, which the photos do not show; the seller adds the year. The price-hint model proposes **€1,450–€1,700** for the attributes and Utrecht; the seller sets **€1,600**. He publishes at 19:07, **2 minutes 10 seconds** after the first photo, and the listing enters the standard moderation pipeline like any other.

{id: ai-in-listing-systems--the-pilot-s-numbers}
### The pilot's numbers

By **Monday 17 January 2028**, after nine weeks, the pilot has produced about **154,000 assisted listings**. The evaluation report Priya Raman's team presents to the architecture advice forum shows:

| Measure | Result | How it is measured |
| --- | --- | --- |
| Uptake | 62% of eligible sellers used the assistant | Assistant started / eligible insertion starts |
| Category accepted unchanged | 92.4% | Final category equals top suggestion |
| Attribute suggestions accepted unchanged | 78%; edited 15%; removed 7% | Per-field provenance |
| Unsupported claims in descriptions | 1.9% of a 2,000-listing audit sample | Human reviewers compare text with photos and attributes |
| Median insertion time | 2 min 50 s assisted, against 6 min 40 s manual in the same categories | Insertion-flow events |
| Started-to-published rate | +9 percentage points against the control group | Seller-randomized experiment |
| Contacts per listing in the first 7 days | +4% | Same experiment; a weak signal, since sellers who finish faster may differ |
| Model cost | €0.0062 per assisted listing | AI gateway metering |

Two findings change the design. First, **assisted listings fill more attributes**, which improves filter coverage: the share of cargo-bike listings with electric assist recorded rose from 61% to 88%. That is the Attribute Junkyard running in reverse, but only because values were constrained to the dictionary; an earlier internal prototype that let the model write free-text attributes had produced 1,100 distinct "colors" in two weeks. Second, the 1.9% of unsupported claims cluster in a few phrases ("barely used", "like new") that the model infers from clean photos. The guardrail is changed to strip condition superlatives unless the seller selects the matching condition value.

![Left, an AI robot dumps a junkyard of mismatched color tags that break the filter; right, it places values into a tidy swatch cabinet that feeds a working filter.](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/junkyard-in-reverse.jpeg)

**Figure 4:** *Assisted listings filled more attributes only because values were constrained to the dictionary; a prototype that let the model write free-text attributes produced 1,100 distinct colors in two weeks.*

At full rollout, model cost is not the constraint: the gateway forecasts about **€230,000 a year** in model calls across Tradeyard's four countries, before evaluation and platform costs, which is small against the conversion gain on the insertion funnel. The constraint is **evaluation in four languages across the group tree's 1,640 leaf categories**. The forum approves the extension to 25% of Netherlands sellers and Belgium on both iOS and Android from **Monday 24 January 2028**, with Poland and Portugal once Polish and Portuguese evaluation sets exist, and keeps the category exclusions.

{id: ai-in-listing-systems--what-fraudsters-did-with-it}
### What fraudsters did with it

Fraudsters used the assistant like everyone else, and **an assistant that writes good descriptions removes a weak scam signal** (bad spelling, generic text). Aisha's team tracked accounts later removed for fraud: they had used the assistant at the same rate as other sellers, and their assisted listings were as polished as anyone's. The trust model must therefore rely less on text quality and more on account, device, image and price signals (see [Scams, Fakes and Account Takeovers: Fraud Prevention for Listings](#fraud-prevention)). The photo screen in step 1 blocked 2,300 attempts to list with photos matching existing listings during the pilot. It cannot catch what the Barcelona ring would do next: generated photos of apartments that exist nowhere, which have no hash to match. For generated imagery the defense is behavioral and economic (new accounts, below-market prices, requests for payment outside the platform), not visual.

![Two equally polished listing cards; text quality no longer separates them, but account, device, image and price signal lamps light up for the fraudulent one.](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/polished-scams-new-signals.jpeg)

**Figure 5:** *An assistant that writes good descriptions for everyone removes a weak scam signal, so the trust model must lean less on text quality and more on account, device, image and price signals.*

{id: ai-in-listing-systems--search-agents-and-the-new-channel}
## Search, Agents and the New Channel

{id: ai-in-listing-systems--conversational-search-as-a-query-compiler}
### Conversational search as a query compiler

Hearthly's conversational search follows the coches.net and leboncoin pattern: the model translates a sentence into Hearthly's existing filter schema, the filters are validated against the schema and shown to the user, and the normal search runs. The user can edit any filter, so the search stays explainable and the result set is the index's, not the model's. The compiler pattern also keeps cost low (one short call per query, cacheable by normalized output) and keeps the LLM off the hot path for the majority of keyword queries. The design and evaluation of query understanding belong to [What Did They Mean? Query Understanding and Autocomplete](#query-understanding).

Natural-language input is useful mainly where filters are many and vocabulary is vague. "Quiet", "bright" and "near a good school" have no filter, and the honest answer is to say so. **A conversational layer that cannot say "we have no filter for that" will invent one.**

Agentic search, in which the model plans several steps and calls tools, costs an order of magnitude more latency. OLX's account puts it at 5–10 seconds against 300–500 ms for classic search, and records that a blank chat interface failed and was replaced by the familiar search page with AI built in. My judgement for Veldmark: **agentic flows belong in high-consideration journeys** (a home, a car) where buyers spend weeks, not in the default search of a general classifieds site where they spend seconds.

{id: ai-in-listing-systems--external-agents-search-as-an-api-product}
### External agents: search as an API product

When an external assistant calls the marketplace, search becomes an API product with its own contract. ImmoScout24's account of its ChatGPT app shows that the mechanics differ from web releases: the assistant platform caches tool descriptors, so a deploy can break references that the platform still holds. Rightmove's FY2025 results, published in February 2026, described conversational search going live and an app submitted to the ChatGPT ecosystem ([Rightmove plc, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). In both cases the assistant does not get the website; it gets **tools**: search with a structured filter schema, listing summaries, and links back.

![Diagram: An external assistant gets tools, not pages](listing-systems-architecture/posts/44-ai-in-listing-systems/assets/images/44-ai-in-listing-systems/fig06-external-assistant-gets-tools-not-pages.jpeg)

**Figure 6:** *An external assistant gets tools, not pages: authenticated, rate-limited search over the same index, public fields only, and tracked links that bring contacts back to the marketplace and attribute them to the channel.*

The decisions Veldmark records for the channel in its **February 2028** decision record are the ones every group will face:

| Question | Veldmark's answer | Reason |
| --- | --- | --- |
| Which brands first | Hearthly France and Motorvane Germany | High-consideration journeys where conversational shortlists help; Tradeyard's buyers mostly browse |
| What the tool returns | Public listing fields, price, location at the listing's published precision, a tracked link | Contact happens on Veldmark's surfaces, where messaging safety runs (see [From Interest to Contact: Messaging and Lead Management](#messaging-and-leads)) |
| Contact through the assistant | Not offered | Moving contact off-platform recreates the Scam Inbox outside Veldmark's controls |
| Quotas | Per partner, with lower limits during Sunday 20:00–22:00 CET | Agent traffic must not compete with the peak (see [Sunday Evening Peaks: Reliability, Performance and Cost](#reliability-and-scale)) |
| Attribution | Leads from assistant links tagged by channel and partner | Pros pay for leads and will ask where they came from |
| Ranking | The same organic ranking as on site; paid placements labeled as such | Ranking transparency duties do not disappear in another company's interface (see [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking)) |
| Data use by the partner | Contract forbids training on returned listings and caching beyond a short window | Listings, photos and descriptions are the sellers' and agencies' content as well as Veldmark's asset |

{id: ai-in-listing-systems--ai-crawlers-and-data-licensing}
### AI crawlers and data licensing

The other half of the channel is involuntary. AI companies crawl listing sites to train models and to answer questions about inventory, prices and neighborhoods. For a listing marketplace, its inventory is its product, and a crawler that copies it delivers no traffic in return.

The architecture has three levers. **Technical**: robots directives per crawler, bot management at the CDN, and rate limits by behavior rather than by user agent, since user agents lie. On 1 July 2025 Cloudflare began blocking AI crawlers by default for new domains and announced a pay-per-crawl model in beta ([Cloudflare, 2025](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/)), which shows the infrastructure market moving the same way. **Legal**: in the EU, the text-and-data-mining exception for commercial use applies only where rights holders have not reserved their rights in a machine-readable way, and the AI Act obliges general-purpose AI model providers to have a policy that identifies and respects such reservations under Article 4(3) of Directive (EU) 2019/790 ([AI Act, Article 53](https://artificialintelligenceact.eu/article/53/)). A machine-readable reservation in robots directives and terms is therefore worth publishing; how strongly listings data is protected by database rights depends on the case and is a question for counsel. **Commercial**: licensed feeds or APIs for answer engines and partners who want the data, with attribution and freshness terms.

Crawler policy trades data protection against search traffic: the search engines that bring 46% of Tradeyard's web sessions also build AI answers, so blocking the crawler that feeds those answers may also cost classic search traffic. The decision belongs to the brand's GM with the SEO and legal leads, and it should be revisited each quarter; the architecture's job is to make each lever a configuration, not a project (see [Found by Google: Web, App and SEO Architecture for Listings](#web-and-seo-architecture)).

{id: ai-in-listing-systems--ai-in-trust-and-safety}
## AI in Trust and Safety

Generative models are useful in moderation where policy changes faster than labels accumulate. A new scam script can be described in a prompt the same day and later distilled into a cheap classifier once moderators have labeled enough cases. Three rules keep this controlled.

1. **Use LLMs in the gray zone only.** Run the cheap classifier on all traffic and the LLM on the uncertain band and the human-review queue. Tradeyard sends about 138,000 new-listing decisions a week to human review; that is where an LLM's triage and summarization pays, not on the 94% decided automatically.
2. **Keep a deterministic floor.** Hash lists, blocked domains and hard rules run before and regardless of any model, because fraudsters probe the gate and prompt injection can manipulate a model reading a listing or a message.
3. **Respect the law on automated decisions.** Under the Digital Services Act, decisions on users' complaints must not be taken "solely on the basis of automated means" (Article 20(6)), and statements of reasons must explain each restriction (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)). An LLM can draft the explanation from the decision facts; a template or a person must constrain it, because the statement is a legal document.

OLX's chat-image model (2026) shows a well-scoped gate-tier use: one fraud vector (images and QR codes in chat), real-time, measured precision. Aisha's gray-zone design for Veldmark follows the same scope discipline, and every model in it is registered at the gate tier with sampled labels (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).

{id: ai-in-listing-systems--pro-copilots-and-valuation-explanations}
## Pro Copilots and Valuation Explanations

**Motorvane's dealer copilot** sits inside Dealer Hub, where dealers already manage inventory and leads (see [Serving the Pros: Dealer, Agent and Merchant Tooling](#professional-seller-tooling)). It drafts replies to leads from the listing and the dealer's past replies, suggests price changes using Motorvane's registered market-value model, and writes descriptions in the dealer's tone. Its autonomy is "act with confirmation": a dealer can apply a suggested price change to forty cars in one action, after a preview that shows each car's new price rating. Two constraints are specific to marketplaces. The copilot may use only the dealer's own data and Motorvane's market data, never another dealer's leads or prices; and price suggestions must be explainable in the same terms as the public price rating, or dealers will see the marketplace as steering them. The equivalent for Keybridge is stricter: any copilot in Keybridge's agent CRM runs inside Keybridge's tenancy, under the March 2027 neutrality decision, and nothing it sees reaches Hearthly.

**Valuo explanations** follow a retrieve-then-narrate pattern. The explanation for the canonical Lyon apartment (68 m², Lyon 7e, energy class D, estimate €372,000–€401,000) is generated from structured inputs that Valuo already produces: the comparable sales used, their dates and prices per square meter, and the effect of the energy class. The language model writes sentences around those facts; it may not introduce a comparable, a number or a trend that is not in the input, and a validator checks every number in the output against the input. **An explanation that invents a comparable is worse than no explanation**, because it turns an estimate into a misrepresentation.

{id: ai-in-listing-systems--cost-and-evaluation}
## Cost and Evaluation

{id: ai-in-listing-systems--cost-per-outcome}
### Cost per outcome

Generative AI cost is per call, which makes it visible in a way predictive ML rarely is. The public numbers are few and old by model-pricing standards.

| Source | Volume | Reported cost | Year | Note |
| --- | --- | --- | --- | --- |
| coches.net natural-language car search | ~20,000 calls a day | ~€19 a day | 2024 | About 6,000 input and 500 output tokens per call |
| OLX job-role extraction | ~4,000 calls a day | "approximately 15K per month", currency unstated | 2024 | Prompted evaluation of self-hosted models |
| Veldmark photo-to-listing (illustration) | ~154,000 listings in the pilot | €0.0062 per assisted listing | 2027–2028 | Forecast €230,000 a year at four-country rollout |

The unit matters more than the figures, which fall as model prices fall: **cost per outcome**, such as cost per published listing, per successful search or per qualified lead. The AI gateway should report it per feature and per brand, with a budget and an alert, so that a prompt change that triples tokens is noticed the same day.

{id: ai-in-listing-systems--evaluation-before-and-after-launch}
### Evaluation before and after launch

| Stage | What it checks | Listing example |
| --- | --- | --- |
| Golden sets before launch | Accuracy and faithfulness per language, category and edge case | 2,000 photographed items per country with known categories and attributes |
| Regression on every change | No degradation from a prompt, model or provider change | Golden sets rerun automatically; the change is blocked if category accuracy drops more than 1 point |
| Adversarial testing | Guardrails hold under abuse | Photos with phone numbers in the image, prompt-injection text in descriptions, scam scripts |
| Online experiments | Effect on liquidity, not only on usage | Started-to-published rate, contacts, removals for policy reasons |
| Sampled production audit | Drift in real traffic | Weekly human review of assisted listings and conversational queries |

Faithfulness, whether the output is supported by the input, deserves its own metric, separate from fluency; OLX's reporting of 98% for style and 89% for faithfulness shows why. **Fluent and wrong is the characteristic failure of generative models**, and it is invisible to usage metrics.

{id: ai-in-listing-systems--regulation-the-eu-ai-act-for-marketplaces}
## Regulation: The EU AI Act for Marketplaces

The EU Artificial Intelligence Act (Regulation (EU) 2024/1689) applies in phases, and the Digital Omnibus on AI, published as Regulation (EU) 2026/1744 on 24 July 2026, moved some of them ([European Parliament Legislative Train, updated September 2026](https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-digital-omnibus-on-ai); [implementation timeline, updated August 2026](https://artificialintelligenceact.eu/implementation-timeline/)). As verified in October 2026:

| Obligation | Applies from | Marketplace relevance |
| --- | --- | --- |
| Prohibited practices and AI literacy | 2 February 2025 | Manipulative or exploitative designs in assistants; staff training |
| General-purpose AI model obligations, including the copyright policy | 2 August 2025 | Applies to model providers; relevant to crawler and licensing policy |
| Article 50 transparency: people must be informed they are interacting with an AI system unless it is obvious; generated content must be marked in a machine-readable way | 2 August 2026; marking for generative systems placed on the market before that date by 2 December 2026 | Conversational search, chat assistants, generated descriptions and images |
| High-risk obligations for stand-alone Annex III systems | 2 December 2027 | Candidate selection and job-ad targeting; creditworthiness of natural persons |
| High-risk systems embedded in regulated products | 2 August 2028 | Rarely relevant to listings |

Annex III point 4(a) lists AI systems "intended to be used for the recruitment or selection of natural persons", in particular "to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates" ([AI Act, Annex III](https://artificialintelligenceact.eu/annex/3/)). Any jobs marketplace that ranks candidates or targets job ads with AI is in scope, and so is Tradeyard's small jobs section in Poland and Portugal if it builds such features. Point 5(b) covers creditworthiness evaluation of natural persons, which matters if a valuation or affordability model feeds a lender's decision (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).

Article 50's marking duty applies to providers of systems that generate synthetic text, images, audio or video, with an exception for systems that only assist standard editing or do not substantially alter the input ([AI Act, Article 50](https://artificialintelligenceact.eu/article/50/)). Whether a marketplace that builds a listing assistant on a third-party model is a provider of that system, and whether a seller-confirmed description falls under the exception, are questions for counsel. Veldmark's architectural answer is not to depend on the answer: assisted descriptions and AI-edited images carry machine-readable provenance metadata and a visible label from launch, and every conversational surface says it is an AI assistant.

The AI Act sits alongside the rules this book covers elsewhere: the DSA's limits on automated complaint handling and its statements of reasons, the P2B Regulation's ranking transparency, consumer law on misleading claims, and the GDPR for prompts and conversations that contain personal data (see [Rules of the Marketplace: DSA, DAC7 and Vertical Regulation](#marketplace-regulation)).

{id: ai-in-listing-systems--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| Where AI writes | Into a draft the user confirms | Directly into the listing | Almost always for seller-owned content | Internal metadata the seller never sees, such as search keywords, with provenance |
| Output form | Constrained to schema and enumerations | Free text | Anything searchable, filterable or used by trust rules | Descriptions only, behind guardrails |
| Search interface | Query compiler over existing search | Agentic multi-step assistant | Default search; latency-sensitive journeys | High-consideration journeys with long sessions |
| External channel | Own surfaces only | Tools for external assistants | Brands whose buyers browse and whose SEO is strong | Verticals where buyers ask assistants for shortlists |
| Model hosting | Provider API | Self-hosted or distilled | Learning a new task; low or variable volume | Stable, high-volume tasks with labels |
| Crawler policy | Allow and license | Block and reserve rights | Partners that bring traffic or pay | Crawlers that copy inventory without return |
| Moderation | LLM in gray zone | LLM on all traffic | Large platforms with millions of decisions a week | Small markets where volume is low and policy changes fast |

{id: ai-in-listing-systems--vertical-differences}
## Vertical Differences

| Dimension | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Listing assistant value | Highest: private sellers, sparse attributes, many categories | Moderate: agents list via feeds; value is in descriptions and disclosures | Low from photos; vehicle data comes from VIN decoding and DMS feeds | Moderate: structuring job ads; risky when applied to candidates |
| Main AI risk in creation | Unsupported condition claims; prohibited items | Wrong mandatory disclosures (energy class, fees) | Wrong specification or history claims | Discriminatory wording |
| Conversational search fit | Low for browsing; useful for vague goods queries | High: many filters, vague preferences | High: many filters, comparisons | Moderate |
| External agent channel | Weak fit | Strong fit (documented: ImmoScout24, OLX CompassGPT) | Strong fit (documented: OLX AutoGPT) | Emerging |
| Copilots | Pro sellers in some categories | Agency CRM, listing descriptions | Dealer lead replies and pricing | Recruiter tools |
| AI Act exposure | Article 50 transparency | Article 50; credit-adjacent valuation uses to review | Article 50; finance referrals to review | **High-risk** for candidate selection and job-ad targeting (Annex III point 4) |

{id: ai-in-listing-systems--failure-modes}
## Failure Modes

- **Free-text attributes from a model.** Values outside the dictionary pour into the catalog; filters, facets and feeds disagree. The Attribute Junkyard, automated.
- **The assistant that helps scammers.** Generation runs before the trust checks, so stolen photos become polished listings. Screening photos first and moderating assisted listings like any other prevents it; **Moderation as an Afterthought** is the default if nobody designs it in.
- **Numbers from the language model.** A price, mileage, surface or valuation that a model generated rather than retrieved. Prices come from registered predictive models; explanations narrate retrieved facts.
- **Prompt changes without regression tests.** Quality drops after a "small" prompt edit or a provider's model update, and nobody notices for weeks: **The Unwatched Model** in its generative form.
- **Agentic search as the default.** Five-to-ten-second responses on a browse-heavy site, with costs that scale with sessions instead of outcomes.
- **Contact through the assistant.** Leads that start in an external assistant and move to e-mail or phone outside the marketplace, where messaging safety and attribution do not reach.
- **Conversation data at the vendor.** Buyers' preferences, budgets and sometimes addresses stored by a model provider under terms nobody reviewed; leboncoin's documented rejection of a hosted assistant API for this reason is the right instinct.
- **Crawler policy by accident.** A CDN default, a robots line copied from a blog, or no decision at all decides whether the inventory trains other companies' models.
- **AI-washed explanations.** Valuation or ranking explanations that sound plausible but do not match what the model did, which is worse for trust and transparency duties than a plain table of inputs.

{id: ai-in-listing-systems--the-chief-architect-s-view}
## The Chief Architect's View

**Extend the model register into an AI use register.** Every AI use (not every model) is registered with its autonomy level, decision tier, owner, model and prompt versions, data sources and their use rights, evaluation sets, cost per outcome, AI Act classification and kill switch. At Veldmark this extends the registry decided on 9 November 2027 for predictive models rather than creating a parallel one. A feature that cannot fill in the register is not ready to launch.

**Make the structured assets the AI strategy.** The taxonomy and attribute service, the search API with a clean filter schema, the price models and the trust platform are what AI features compile into. Groups that skipped that work will find their AI features produce the mess faster. At Veldmark, the photo-to-listing assistant was possible in November 2027 only because the taxonomy service went live in October; **the order of Common Ground's deliveries was also the order of what AI could do**.

**Own the gateway centrally, own the features locally.** One AI gateway and evaluation harness for the group, with routing, metering, logging and kill switches; features built by brand teams on top. That splits the work the same way as the rest of Common Ground: share platforms, not products.

**Decide the channel strategy per brand, explicitly.** Whether to publish search as tools for external assistants, which partners, with which data, and how leads are attributed are product and commercial decisions with architectural consequences. Put them in decision records with a review date, because the channel is moving faster than any other part of the business.

**Write the data-use rules down and enforce them in pipelines.** Which data may be sent to which provider, which data may train which model, which content external partners may cache or train on, and what the Keybridge neutrality commitment means for every AI feature. Rules that live only in policy documents are broken by the first prototype.

**Budget AI by outcome.** Approve features with a cost per outcome and a monthly budget per brand, reported by the gateway. Move high-volume stable tasks to cheaper hosting as labels accumulate.

**Watch these indicators:** share of AI uses registered; faithfulness on audit samples; attribute acceptance and edit rates; share of AI-suggested values outside the dictionary (should be zero); cost per outcome per feature; latency at peak; share of leads from external assistants and their quality; crawler traffic by declared and undeclared agents; and the number of AI features with an AI Act classification still marked "to review".

{id: ai-in-listing-systems--questions-to-ask}
## Questions to Ask

1. For each AI feature, what structured output does the model produce, and which deterministic validator checks it before anything is stored or shown?
2. Can any model output reach a listing field, a buyer-visible number or a user restriction without a person or a validator in between?
3. Do listing fields record whether a value was AI-suggested, seller-confirmed or seller-edited, and do search, trust and analytics use that provenance?
4. Which trust checks run before generation, and how does the assistant change the signals our fraud models rely on?
5. What is the cost per outcome of each AI feature, who sees it daily, and what happens when it doubles?
6. Which evaluation sets guard each feature, in which languages and categories, and do they run on every prompt and model change?
7. Which brands expose search to external assistants, what data do the tools return, and how are leads from that channel attributed and protected?
8. What is our crawler and licensing policy per brand, and is it a decision or a default?
9. Which of our AI uses are covered by Article 50 of the AI Act, and which could become high-risk from 2 December 2027, especially in jobs and credit-adjacent uses?
10. Which data may we send to which model provider, and where is that rule enforced?

{id: ai-in-listing-systems--from-ai-to-the-long-view}
## From AI to the Long View

AI arrives in listing systems as a translator between people and the structures the marketplace already has. Where those structures are clean (a versioned taxonomy, an attribute dictionary, a search API with a filter schema, registered price models, a trust platform) AI makes listing faster, search more forgiving and pros more productive, and the control layer keeps every proposal checked, attributed and costed. Where they are not, AI accelerates the mess. The final chapter of this part, [Built to Be Replaced: Evolving a Marketplace Platform Over a Decade](#long-term-evolution), takes the longer view: how a Chief Architect keeps a marketplace platform coherent over a decade in which AI will be only one of the stressors, alongside acquisitions, regulation and the swing between central and local control.

{id: ai-in-listing-systems--sources-and-evidence}
## Sources and Evidence

{id: ai-in-listing-systems--company-engineering-and-investor-sources}
### Company engineering and investor sources

- ['Magical' listing tool harnesses the power of AI](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/) — eBay Inc., 2023. Text-assisted and photo-based listing creation, adoption figures, iOS beta.
- [Kleinanzeigen führt KI-gestützte Anzeigenerstellung per Foto ein](https://www.mobiflip.de/kleinanzeigen-fuehrt-ki-gestuetzte-anzeigenerstellung-per-foto-ein/amp/) — mobiflip.de (trade press), 2025. Photo-to-listing scope and category exclusions.
- [How OLX uses AI to reduce repetitive work](https://www.olxgroup.com/news/how-olx-uses-ai-to-reduce-repetitive-work/) — OLX Group, 2026. Auto Description and its human evaluation.
- [Extracting job roles in job ads: a journey with generative AI](https://tech.olx.com/extracting-job-roles-in-job-ads-a-journey-with-generative-ai-e8b8cf399659) — OLX Tech, 2024. Event-driven LLM enrichment, volumes and cost.
- [From Filters to Phrases: Our AI Revolution in Car Search](https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/) — Adevinta Tech Blog (coches.net), 2024. Filter compilation, pre-classifier, tokens and cost.
- [Building a Smarter Shopping Experience: Conversational Search in E-Commerce](https://adevinta.com/techblog/building-a-smarter-shopping-experience-the-technology-behind-conversational-search-in-e-commerce/) — Adevinta Tech Blog (leboncoin), 2024. JSON output, fine-tuning for latency, rejection of a hosted assistant API.
- [Building a conversational shopping assistant (OLX Magic)](https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture) — ZenML LLMOps database (third-party summary of an OLX talk), 2024. Agent tools, latency, interface lesson.
- [OLX launches AutoGPT agentic AI assistant](https://www.olxgroup.com/news/olx-launches-autogpt-agentic-ai-assistant-transforming-automotive-search-across-europe/) — OLX Group, 2026. ChatGPT app for car search; company-reported outcome.
- [OLX launches agentic AI products at CLAIM AI in Lisbon](https://www.olxgroup.com/news/olx-launches-agentic-ai-products-to-transform-property-search-and-car-sales-at-claim-ai-in-lisbon/) — OLX Group, 2026. CompassGPT and the AutoIQ dealer agent.
- [OLX chat images GenAI](https://www.olxgroup.com/?p=4590) — OLX Group, 2026. Real-time image and QR-code fraud detection in chat.
- [Scout24 Engineering](https://medium.com/scout24-engineering) — Scout24, 2026. "Shipping the first MCP in HeyImmo" (January) and "What we learned from launching ImmoScout24 app in ChatGPT" (March).
- [FY2025 results announcement](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf) — Rightmove plc, 2026. Conversational search and an app submitted to the ChatGPT ecosystem.
- [How We Attract Users with SEO: From Ten Blue Links to AI-Generated Answers](https://adevinta.com/techblog/how-we-attract-users-with-seo-from-ten-blue-links-to-ai-generated-answers/) — Adevinta Tech Blog, 2023. AI in SEO operations.
- [Cloudflare just changed how AI crawlers scrape the internet at large](https://www.cloudflare.com/press/press-releases/2025/cloudflare-just-changed-how-ai-crawlers-scrape-the-internet-at-large/) — Cloudflare, 1 July 2025. Default blocking of AI crawlers; pay-per-crawl beta.

{id: ai-in-listing-systems--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol) — Anthropic, 2024. MCP as an open standard for connecting assistants to data sources.
- [Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation) — Anthropic, 2025. MCP governance under the Linux Foundation.
- [Article 50: Transparency obligations](https://artificialintelligenceact.eu/article/50/) — EU AI Act (Regulation (EU) 2024/1689), 2024. Disclosure and marking duties.
- [Article 53: Obligations for providers of general-purpose AI models](https://artificialintelligenceact.eu/article/53/) — EU AI Act, 2024. Copyright policy and Article 4(3) reservations.
- [Annex III: High-risk AI systems](https://artificialintelligenceact.eu/annex/3/) — EU AI Act, 2024. Employment and creditworthiness points.
- [Digital Omnibus on AI](https://www.europarl.europa.eu/legislative-train/theme-a-europe-fit-for-the-digital-age/file-digital-omnibus-on-ai) — European Parliament Legislative Train, updated September 2026. Regulation (EU) 2026/1744 and postponed dates.
- [AI Act implementation timeline](https://artificialintelligenceact.eu/implementation-timeline/) — Future of Life Institute, updated August 2026. Application dates.

{id: ai-in-listing-systems--research-and-practitioner-sources}
### Research and practitioner sources

- [Llama Guard: LLM-based input-output safeguard for human-AI conversations](https://arxiv.org/abs/2312.06674) — Meta researchers, 2023. Policy-as-prompt safety classification with a customizable taxonomy.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
