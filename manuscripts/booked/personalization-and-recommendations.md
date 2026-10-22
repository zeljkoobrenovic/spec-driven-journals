{id: personalization-and-recommendations}
# 19. Remembering the Traveler: Personalization, Recommendations and Saved Intent

![Remembering the Traveler: Personalization, Recommendations and Saved Intent — logo](stays-marketplace-architecture/posts/19-personalization-and-recommendations/assets/images/19-personalization-and-recommendations/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how stays marketplaces personalize when user history is sparse: trip intent, listing and guest embeddings, recommendation surfaces, wishlists, saved searches and price alerts. You will see the architecture that captures and recovers intent, the rules that keep alerts and recommendations honest about price and availability, and how to measure whether any of it creates bookings.

> **WHY THE BUSINESS CARES:** Most stays bookings follow several sessions spread over days or weeks, and most of those sessions end without a booking. Every guest who leaves and comes back through a paid click is a booking the marketplace pays for twice; a guest who comes back through a wishlist, an alert or a remembered search costs almost nothing. Saved intent is the cheapest demand channel a marketplace owns.

> **WHY ARCHITECTS SHOULD CARE:** Personalization touches identity, consent, search, pricing, notifications and the data platform, and each of those is owned by someone else. Without an explicit owner for trip intent and a rule that every recommendation is re-priced before it is shown, the group ends up with several half-memories of each guest, alerts that quote prices nobody can book, and models whose value nobody has measured.

> **KEY POINTS:**
>
> * **Personalize the trip, not the person.** A guest books a stay once or twice a year, and the family holiday and the business trip are different customers. The unit worth modeling is the **trip intent**: destination, dates, party and budget, inferred from the current journey and kept as a first-class record with a lifecycle that ends at booking or expiry.
> * **Saved intent is a promise about price and availability.** A wishlist, saved search or price alert tells the guest "this is still bookable at this price". Every alert and recommendation must be re-priced against the live availability and pricing path, as a total for the guest's dates and party, at the moment it is sent or rendered, or it becomes a new source of phantom availability and price drift.
> * **Prove incrementality, and keep a path without profiling.** Recommendations claim credit for bookings that would have happened anyway. Long-running holdouts measured on uncancelled bookings separate real lift from attribution, and a non-personalized path that consent, regulation and cold start all need anyway keeps the comparison honest.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Price Drift** — a price alert quotes a nightly rate while checkout shows a total with fees and taxes, so the number that brought the guest back is not the number they pay.
> * **Phantom Availability** — wishlists, "recently viewed" rails and recommendation e-mails show homes and rooms that sold out hours ago, priced from a cache nobody refreshed.
> * **The Unwatched Model** — recommendation models and alert rules send millions of messages and reorder every home page, with no holdout, no owner and no record of which version said what.

A guest planning a summer holiday rarely books in one sitting. They search on a Tuesday evening, look at a dozen homes or hotels, save three, leave, come back on Thursday from a different device, check the prices again, ask their partner, and book on Sunday, sometimes on a different site. In a 2023 paper on its multi-task ranker, Airbnb described guests who "could spend multiple weeks, across dozens of searches" before making a reservation request ([Tan et al., 2023](https://arxiv.org/abs/2305.18431)). **The booking is the last step of a journey, and the marketplace's job between the steps is to remember.**

That memory is harder to build than in retail or media. People book stays rarely, so even loyal customers have a thin history. The same person travels as a parent in August and as a consultant in November, and the August history is noise for the November trip. Booking.com researchers named this the **continuous cold start** problem in 2015: frequent visitors look new because they visit infrequently, their interests shift and they switch personas ([Bernardi et al., 2015](https://arxiv.org/abs/1508.01177)). And the product being remembered is perishable: the apartment a guest saved on Tuesday may be booked by someone else on Wednesday.

Part IV follows a guest from intent to a bookable stay. [Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture) and [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) answer one query; this chapter covers what the marketplace remembers **between** queries, and the rule that keeps that memory honest about price. It owns four terms: **trip intent**, **wishlist**, **price alert** and **listing embedding**. Its quote rule leads into [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection), which owns how the total is displayed; notification routing ([Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging)), accounts ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)) and the feature platform ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)) are the dependencies it names.

{id: personalization-and-recommendations--setting-the-scene-at-corvane-the-novaks-abandon-a-search-twice}
## Setting the Scene at Corvane: The Novaks Abandon a Search, Twice

Corvane, the fictional travel group this book follows (see [Meet Corvane: Two Marketplaces, One Group](#meet-corvane)), runs two marketplaces: **Roomstead**, an accommodation marketplace in the style of an online travel agency (OTA), selling hotel rooms by room type and rate plan, and **Nookaway**, a hosted-stays marketplace selling nights in homes. In March 2027 Mariana Costa, the Group Chief Architect, asked Jonas Weber, who had just become head of search and ranking for both brands, to reconstruct one booking from the guest's side. She picked the Novak family from Prague, because their February booking had produced a customer-service contact and nobody could say which system had brought them back.

The reconstruction took Jonas's team four days and three data warehouses. The local details below are illustrative, like everything about Corvane; the booking itself is the one recorded in the group's scenario ledger.

| When (CET) | Who and where | What happened | What Corvane remembered |
| --- | --- | --- | --- |
| Thu **11 Feb 2027**, 21:10 | Jana Novak, Nookaway iOS app, signed in | Searched Lisbon, **2–9 August**, 2 adults + 2 children (9 and 12). Viewed 19 homes; saved four to a new wishlist, "Lisboa agosto", and shared it with Tomáš | A wishlist in Burrow (the Nookaway monolith), without dates or party; search events in BigQuery |
| Thu 11 Feb, 21:55 | Tomáš Novak, laptop, Roomstead website, not signed in | Searched Lisbon for the same dates; looked at six hotels with family rooms between €240 and €310 a night; closed the tab | An anonymous session in Roomstead's clickstream in Snowflake. Tomáš had declined marketing cookies, so no retargeting |
| Fri 12 Feb, 14:30 | Another guest | Booked one of the four wishlisted homes for 1–8 August | Almanac blocked the nights; the wishlist kept showing the home with its old price "from €150" |
| Sat **13 Feb**, 03:00 | Nookaway's nightly alert job | The Alfama apartment's host had lowered August weekday prices from €165 to **€145** on Friday evening; the job found the drop | A row in the job's snapshot table |
| Sat 13 Feb, 08:05 | Jana's phone | Push notification: "A home in Lisboa agosto dropped to €145 a night" | Notification log, Nookaway only |
| Sun **14 Feb**, 20:30 | Jana, Nookaway app | Booked the Alfama apartment: 7 nights × €145 = €1,015, cleaning €70, guest service fee **€130.20**, Lisbon tourist tax **€56**; total **€1,271.20** | A reservation, attributed by last click to "push notification" |
| Mon 15 Feb | Jana, Nookaway support | "The alert said €145; the total was 25% more" | A case tagged "pricing question" |

Jonas's report treated the successful booking as an indictment. Corvane had known what the Novaks wanted, in four systems, and none of them knew it as a trip:

- **Nookaway's wishlist** knew which homes Jana liked, but not her dates or party, so it could not say that one was gone or what the others would cost for her week.
- **Nookaway's alert job** knew about the price drop, but quoted it as a nightly rate. The **€1,271.20** total was **25%** above the €1,015 the alert implied, and every component of the difference (cleaning fee, service fee, tourist tax) was known when the alert was sent. That is **Price Drift** created by the alert, not by checkout; [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection) covers how the total should be displayed.
- **Roomstead** knew that an anonymous visitor from Prague had looked at Lisbon family rooms, and on Friday showed Tomáš the same "Trending: Paris, Barcelona, Rome" rail it showed everyone.
- **Neither brand** could tell whether the alert had *caused* the booking. The Novaks had shared a wishlist and were still comparing; they might have booked on Sunday anyway.

![Four separate boxes labeled wishlist, alert job, anonymous session and reservation each hold one puzzle piece, while the completed puzzle of the family's trip floats above them only as a dotted outline.](stays-marketplace-architecture/posts/19-personalization-and-recommendations/assets/images/19-personalization-and-recommendations/19-four-systems-no-trip.jpeg)

**Figure 1:** *Corvane knew what the Novaks wanted in four systems, a wishlist, an alert job, an anonymous session and a reservation, and none of them knew it as one trip.*

Rafael Mendes, Nookaway's VP Engineering, defended the nightly job as cheap. Noor van Dijk, Head of Regulatory Affairs and Privacy, set the hard constraint: Tomáš had refused marketing cookies on Roomstead, and Jana's Nookaway consent did not cover Roomstead using her data. Joining the two sessions into "the Novak family" would need a lawful basis neither brand had.

Mariana framed the question for the architecture forum: **"Who owns what a guest is trying to book, how do we keep what we tell them about it true, and how will we know whether remembering it is worth anything?"**

{id: personalization-and-recommendations--concepts-personalizing-a-purchase-people-make-twice-a-year}
## Concepts: Personalizing a Purchase People Make Twice a Year

{id: personalization-and-recommendations--why-stays-personalization-is-different}
### Why stays personalization is different

Beyond rare purchases and switching personas, stays differ from retail and media in three ways: the current session carries almost all the useful context (destination, dates, party, budget), the price is computed per stay, and the signal that matters is an **uncancelled booking** weeks after the first search.

Airbnb's 2026 description of its guest-journey model makes the same contrast: unlike social platforms that optimize for engagement, Airbnb "optimizes for booking conversion", bookings are rare and deliberate, and listing views make up most logged events ([Zha et al., 2026](https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/)). Booking.com's 2019 account of its first 150 production models groups many of them around *traveler context* (is this a family, a couple, a business trip?) rather than long-term taste ([Bernardi et al., 2019, as summarized by Colyer](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/)). So a stays marketplace should invest first in **understanding the current trip** and only second in remembering the person.

{id: personalization-and-recommendations--trip-intent}
### Trip intent

**Trip intent** is the marketplace's best current estimate of a trip a guest is planning: where (a destination or a set of places), when (exact dates, a date window or a month), who (party size and composition, rooms needed), what kind of stay (property types, must-have amenities) and roughly what budget. It is inferred from searches, filters, views, saves and sometimes explicit input, and it has a lifecycle.

Three properties make trip intent a better unit than a user profile:

1. **It is bounded.** It begins with a search and ends with a booking, an explicit dismissal or an expiry date after the trip's latest possible check-in. A profile accumulates forever; an intent can be deleted when it no longer serves the guest.
2. **It is persona-neutral.** The same account can hold a family intent for August and a business intent for November. Each drives its own recommendations and alerts.
3. **It carries the context that prices a stay.** Dates and party are the inputs to every price the marketplace can quote. A recommendation without them can show only "from" prices, which are the root of most price-drift complaints.

A guest can have several open intents, and one intent can span people: the Novaks had one, expressed in two brands by two people, which is normal for families and groups.

![An overstuffed profile sack mixing beach, business and family items, beside two separate bounded trip-intent folders for a family trip in August and a business trip in November.](stays-marketplace-architecture/posts/19-personalization-and-recommendations/assets/images/19-personalization-and-recommendations/19-profile-versus-trip-intents.jpeg)

**Figure 2:** *A profile accumulates forever and mixes personas; a trip intent is bounded, belongs to one trip and carries the dates and party that price a stay, so one account can hold a family trip in August and a business trip in November.*

{id: personalization-and-recommendations--saved-intent-artifacts}
### Saved-intent artifacts

Guests also save intent explicitly, in four common artifacts that differ in what they store and what they promise.

| Artifact | What the guest saves | What the marketplace promises | Typical trigger for contact |
| --- | --- | --- | --- |
| **Recently viewed and recent searches** | Nothing, explicitly; the platform records it | "We remember where you were" | Home-page rail, search-box autofill |
| **Wishlist** | Specific properties or homes, optionally with dates and party, often shared with co-travelers | "Your shortlist stays here, with current prices" | Price change, low availability, a co-traveler's addition |
| **Saved search** | A query: destination, dates, filters | "We will tell you about new or changed results" | New matching supply, price changes across the result set |
| **Price alert** | A watch on a price: one property, a saved search, or a destination and dates | "We will tell you when the price moves" | A price crossing a threshold or changing by a minimum amount |

A **wishlist** in this book is a guest-owned, named list of specific properties or homes, optionally bound to dates and a party, which the guest can share with co-travelers. A **price alert** is a standing request to notify the guest when the bookable price for a defined stay changes in a way they care about.

{id: personalization-and-recommendations--listing-embeddings-and-guest-embeddings}
### Listing embeddings and guest embeddings

A **listing embedding** is a learned vector that places each property or home in a space where listings that guests treat as substitutes sit close together. It is learned from behavior, typically by treating the sequence of listings a guest views in one search session like the sequence of words in a sentence, in the style of word2vec ([Mikolov et al., 2013](https://arxiv.org/abs/1301.3781)), and from content (text, photos, attributes). A **guest embedding** does the same for a guest's history.

Airbnb's 2018 KDD paper is the reference for the first approach in stays: listing and user embeddings for real-time personalization in search ranking and similar-listing recommendations, designed for a marketplace where guests rarely book the same listing twice. The paper reported that search ranking and similar-listing recommendations together drove **99%** of Airbnb's conversions ([Grbovic and Cheng, 2018](https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb)); the 2026 successors are described below. Expedia described a similar idea for hotels in 2024: a word2vec-inspired property embedding among the features of its lodging ranker ([Expedia Group, 2024](https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b)).

Embeddings are **shared infrastructure**: the same listing vectors serve similar-listing rails, retrieval ([Searching Dates, Not Documents: Search Architecture for Stays](#stays-search-architecture)), ranking features ([Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking)), e-mail selection and duplicate detection. Whoever owns their training, versioning and refresh owns a dependency for half the discovery stack.

{id: personalization-and-recommendations--recommendation-surfaces}
### Recommendation surfaces

A **recommendation surface** is any place where the marketplace proposes stays or destinations without a complete query. Surfaces differ in context and failure cost.

| Surface | Context available | Main job | Main risk |
| --- | --- | --- | --- |
| **Home page and app launch** | Open intents, history, location, season | Recover the last trip ("Continue planning Lisbon, 2–9 Aug"), then inspire | Generic rails for unknown guests; stale prices |
| **Similar stays** (on a property page, and when a stay is unavailable) | One anchor listing, dates, party | Offer substitutes for the same trip | Showing alternatives that are also unavailable |
| **Zero- and low-result recovery** | A query that returned too little | Suggest nearby dates, relaxed filters, adjacent areas | Silently changing the guest's query |
| **Destination and category inspiration** | Season, origin, past trips | Turn vague intent into a search | Repeating the same five cities to everyone |
| **E-mail and push** | Open intents, consent, frequency history | Bring the guest back to an open trip | Spam, consent breaches, prices that no longer hold |
| **Cross-sell during the trip** | A confirmed reservation | Add a car, an experience, a second stay | Selling to a guest who has a problem with the first stay |

Airbnb has described the zero-result case as a recommendation problem: a 2025 paper on augmenting search results suggests alternatives such as nearby dates or relaxed filters when narrow searches return few results ([Airbnb Tech, 2025 year in review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)). Expedia described the "property search" case in 2024: a traveler who arrives looking for one specific hotel sees it pinned at the top and alternatives ranked by a blend of relevance and similarity to the searched property; a purely similarity-based model underperformed ([Expedia Group, 2024](https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b)).

{id: personalization-and-recommendations--architecture-capture-remember-recommend-re-price}
## Architecture: Capture, Remember, Recommend, Re-price

Personalization in a stays marketplace is five capabilities with different owners and latency budgets. The common mistake is one "personalization service" that owns everything from the click stream to the push notification and cannot answer for any of it.

![Guest sessions feed intent capture and a trip intent store; embeddings and recommendations propose candidates and an alert evaluator watches saved stays; both pass through live price and availability before surfaces show bookable totals, and alerts go to notifications.](stays-marketplace-architecture/posts/19-personalization-and-recommendations/assets/images/19-personalization-and-recommendations/19-five-personalization-capabilities.jpeg)

**Figure 3:** *Personalization as five owned capabilities. Intent is captured and stored once; embeddings and recommenders propose candidates; nothing reaches a guest until it has passed the same live price and availability path as search.*

| Component | Responsibility | Owns | Must not |
| --- | --- | --- | --- |
| **Intent capture** | Turn journey events into open trip intents: cluster searches into trips, infer dates and party, close intents on booking | Inference rules or models; intent identifiers on events | Store raw click streams as "intent" |
| **Trip intent store** | Hold open intents, wishlists, saved searches and alert watches per account or device, with consent state and expiry | The system of record for saved intent; deletion and export | Hold prices; a stored price is a cached claim |
| **Embeddings and candidate generation** | Train and serve listing and guest vectors; propose candidates for a surface | Model versions, refresh schedule, offline metrics | Decide what is shown without the ranking and pricing path |
| **Recommendation service** | Assemble a surface: pick candidates, apply business rules, rank, enrich | Surface definitions, rules, logging of what was shown and why | Compute prices itself |
| **Alert evaluator** | Re-evaluate watches against live supply; decide whether a change is worth a message | Thresholds, deduplication, frequency caps | Send messages directly; that is the notification platform's job |

Two boundaries do most of the work.

**The intent store holds intent, not prices.** A wishlist row says "Jana saved listing 4471 for 2–9 August, 4 guests". It does not say "€145". Any price shown next to it is fetched at render time from the same price and availability path search uses ([Is It Still Available? Availability Search, Caching and Price Accuracy](#availability-engine)). The Nookaway wishlist that still showed the sold home "from €150" was storing what should have been computed.

**Recommendations are enriched with live price and availability before anyone sees them.** Booking.com described this boundary in a 2025 post on its recommendation platform, which lets teams combine several model providers for recommendations "integrated into every step of the customer journey". A separate enrichment system attaches non-recommendation data on request, including a "Minimum Accurate Pricing" enrichment fetched from a personalized ranker city search system and the number of times a property has been wishlisted; decoupling enrichment from prediction, the authors say, reduces the prediction system's load ([Booking.com Engineering, 2025](https://medium.com/booking-com-development/unlocking-the-power-of-customization-how-our-enrichment-system-transforms-recommendation-data-e71832fc4ef4)). Copy the separation: models propose, and the price comes from the system that search uses.

{id: personalization-and-recommendations--the-lifecycle-of-a-trip-intent}
### The lifecycle of a trip intent

An intent is an aggregate with states, not a row of preferences, so every downstream consumer has a clear rule for when to stop.

![Trip intent states: Inferred becomes Active on a save or alert or Expired; Active and Dormant move back and forth; Dormant can expire; Active ends as Booked or Dismissed.](stays-marketplace-architecture/posts/19-personalization-and-recommendations/assets/images/19-personalization-and-recommendations/19-trip-intent-lifecycle.jpeg)

**Figure 4:** *A trip intent's lifecycle. Booking, dismissal and expiry each end it, and every consumer (recommendations, alerts, e-mail) reads the state rather than guessing whether the guest is still planning.*

The thresholds in the diagram are illustrative; the state names are the contract. Three consequences follow:

- **Booked closes the intent.** A guest who has booked Lisbon should stop getting Lisbon alerts within minutes. That requires the intent store to consume reservation events ([Streams of Nights: Event-Driven Architecture for Stays](#event-driven-stays)), not a nightly job. Alerts for a trip already booked are the most common complaint about stays notifications, the cheapest to prevent, and they invite cancel-and-rebook behavior that costs the marketplace twice.
- **Expiry is a privacy control as well as a product one.** An intent for August 2027 has no purpose after August 2027. Deleting it then is data minimization that costs nothing.
- **A booked intent can open a new one.** The Novaks' confirmed reservation is the context for cross-sell (a car, a day trip) and, a year later, for "Lisbon again?". These are different intents with their own consent and lifecycle.

{id: personalization-and-recommendations--batch-streaming-and-request-time-personalization}
### Batch, streaming and request-time personalization

Personalization runs on three clocks, and the architecture should state which component runs on which: **batch** (daily model training, listing vectors, long-term guest embeddings), **streaming** (session features, intent opening and closing, alert triggers, within seconds) and **request time** (combining stored embeddings with the live query and fetching live prices, within milliseconds).

Airbnb's sequence model is an architecture case, not a modeling one. The 2026 model encodes a **long-term** sequence of up to 80 events over seven years (bookings, reviews, cancellations) and a **short-term** sequence of up to 200 listing views from the past 21 days. Running it at query time was too expensive, so the first design split inference into a daily batch encoder and a request-time ranker; the short-term sequence and a set-wise ranker added +0.55% uncancelled bookers and a further +0.28% uncancelled bookings online ([Zha et al., 2026](https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/)). The batch design left embeddings "up to nearly two days" stale. The follow-up added an event-driven trigger and in-pipeline model inference to Chronon, so the same encoder runs on each new event, often "within 10 to 30 seconds"; offline normalized discounted cumulative gain (NDCG), a ranking-quality metric, rose 1.67% and an online test showed about a third of a percent more uncancelled bookings ([Hou et al., 2026](https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553)).

Two lessons transfer. **Keep heavy models off the request path** by precomputing embeddings. And **freshness is itself a ranking feature**: the same model, fed newer data, booked more stays. Streaming triggers and in-pipeline inference are therefore a feature-platform decision ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)), not a recommendation-team one.

{id: personalization-and-recommendations--cold-start-on-both-sides}
## Cold Start on Both Sides

{id: personalization-and-recommendations--guests-without-history}
### Guests without history

Most visitors are unknown at the moment that matters: logged out, on a new device, arriving from a paid search ad or a metasearch click, or last seen two years ago as a different persona. A personalization design that needs a user identifier serves none of them.

Airbnb described a deliberate answer in September 2026. Its **proximity features** group users by coarse location derived from the IP address into buckets of about 1,000 users, using an adaptive clustering that subdivides dense city areas and widens tiles in rural ones. Features are computed daily per bucket: recent search destinations, room types and median prices; long-term booking patterns; bucket metadata. Any model that conditions on a user identifier can condition on the proximity key instead. The post states that clustering excludes users who have not provided consent, that the pipeline is integrated with consent management and deletion controls, and that the lookup is a "soft dependency": if it times out, the model proceeds without it. On the home page, the autosuggest that used to fall back to a static global list ("Paris, Barcelona, London, Rome") now shows location-aware destinations, with gains concentrated among never-booked and dormant users ([Jiang et al., 2026](https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486)).

The pattern generalizes: **personalize cold-start traffic on group signals that need no identity**, such as origin market, device, entry channel, season and the current query. Tomáš's anonymous Roomstead session from Prague carried enough of these to replace "Trending: Paris" with "Families from Czechia book Lisbon, the Algarve and Mallorca in August", without knowing who he was.

The other half of guest cold start is **the session itself**: a logged-out guest who has searched once has already expressed a trip intent. Storing it against a first-party device identifier, with the consent the market requires, and offering "Save this trip to your account" makes an anonymous session recoverable. It is the cheapest personalization a marketplace can build, and the one most often missing.

{id: personalization-and-recommendations--listings-without-history}
### Listings without history

A new hotel or home has no views, saves or bookings, so behavioral embeddings and engagement features rank it low, so it collects no behavior. In 2020, Airbnb listed cold start for new listings as one of three main areas of improvement to its deep-learning ranker, alongside architecture and position bias ([Haldar et al., 2020](https://arxiv.org/abs/2002.05515)). Three techniques are common:

- **Content-based vectors.** Embed text, photos and attributes so a new listing has a position in the space before anyone clicks it. Airbnb lists text-and-photo listing embeddings among its 2025 papers ([Airbnb Tech, 2025 year in review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)).
- **Neighbor initialization.** Start a new listing's behavioral vector from the vectors of similar existing listings nearby (same type, capacity and price band), then let real behavior replace it.
- **Exposure policy.** Reserve some impressions for new supply so it can collect evidence. That is a ranking-policy decision owned by [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking); recommendations should follow the same policy rather than invent their own.

Listing cold start is deeper on Nookaway than on Roomstead (see the table in the Hotels and Homes section), and more consequential: an individual host whose first listing gets no bookings in its first weeks often does not stay.

{id: personalization-and-recommendations--saved-intent-wishlists-saved-searches-and-price-alerts}
## Saved Intent: Wishlists, Saved Searches and Price Alerts

Saved intent is where personalization makes explicit promises, so it is where it breaks most visibly.

{id: personalization-and-recommendations--wishlists}
### Wishlists

A wishlist looks like a list of listing IDs per user. Four design decisions make it useful or harmful.

1. **Bind the list to a stay.** A wishlist without dates and party can show only "from" prices and cannot say whether a saved home is still available. Ask for dates when the guest saves, inherit them from the current search, and let the guest change them for the whole list.
2. **Render live, never cached.** Every time the list is shown, re-check availability and fetch the total price for the bound stay. Mark unavailable items as unavailable and offer substitutes from the similar-stays recommender, filtered to the same dates.
3. **Make sharing a first-class model.** Families and groups decide together. A shared list needs collaborators with roles, a record of who added and removed what, and notifications to co-travelers. The Novaks' list had two members; group trips can have ten.
4. **Treat saves as signals with care.** Aggregated, saves indicate popularity; Booking.com exposes the number of wishlist additions per property as an enrichment ([Booking.com Engineering, 2025](https://medium.com/booking-com-development/unlocking-the-power-of-customization-how-our-enrichment-system-transforms-recommendation-data-e71832fc4ef4)). Individually they are cheap and noisy, which is one reason ranking labels lean on later milestones such as payment-page views and uncancelled bookings ([Tan et al., 2023](https://arxiv.org/abs/2305.18431)).

{id: personalization-and-recommendations--saved-searches-and-price-alerts}
### Saved searches and price alerts

A saved search stores a query; a price alert watches a price. In practice they are one mechanism: a **watch** with a target (one property and stay, or a query), a condition (any change, a drop of at least X, a price below Y), a frequency cap and an expiry. The alert evaluator re-prices watches and decides whether a change deserves a message.

The architecture question is how the evaluator learns that a price changed.

| Design | How it works | Strengths | Weaknesses |
| --- | --- | --- | --- |
| **Poll** | A scheduled job re-prices every active watch through the price and availability path | Simple; uses the same path as search; easy to reason about | Cost grows with watches × frequency; changes are found late (the Novaks' alert came about ten hours after the host's price change) |
| **Event-triggered** | Price and availability change events (ARI updates, calendar and price edits) are matched against an index of watches; only matching watches are re-priced | Fast; cost follows changes, not watches | Needs an index of watches by property and date; ARI change rates on OTAs are very high; must still re-price through the live path before sending |

Figure 5 shows the event-triggered design as I would build it, with the live re-pricing step that both designs need.

![A swimlane of an event-triggered alert: the host lowers the August price, the calendar emits a change event, the evaluator finds the watch for 2 to 9 August and 4 guests, gets a fresh total of 1,271.20 euros, applies threshold and cap, and sends an alert with the total.](stays-marketplace-architecture/posts/19-personalization-and-recommendations/assets/images/19-personalization-and-recommendations/19-event-triggered-price-alert.jpeg)

**Figure 5:** *An event-triggered price alert. The price change only nominates a watch; the alert is decided on a fresh quote for the guest's exact stay, and the message carries the total, not the nightly rate.*

In the Novak case, the total before the host's change would have been 7 × €165 = €1,155, plus €70 cleaning, a 12% guest service fee of €147.00 and €56 tourist tax: **€1,428.00**. After the change it was **€1,271.20**. An alert that said "Your Lisbon stay, 2–9 August, 4 guests: now €1,271.20 total, €156.80 less than when you saved it" would have been true, specific and impossible to misread. The alert that said "€145 a night" was true and still produced a complaint.

Seven rules for any alert evaluator follow.

- **Re-price through the live path, as a total.** The alert's number is the number the guest will see on the property page for that stay, including mandatory fees and taxes, in the guest's currency ([The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection)).
- **Check availability for every night.** A price drop on a stay that is no longer fully available is Phantom Availability delivered to a phone.
- **Close watches on booking.** Never send a price alert for a trip the guest has already booked, on either brand they have consented to link.
- **Deduplicate and cap.** Several price events for the same stay in an hour are one alert, and one guest gets at most a few alerts per trip per week.
- **Respect the notification platform.** Channel choice, quiet hours, language and consent belong to [Between Booking and Check-Out: Trips, Messaging and Notifications](#trip-and-messaging). The evaluator decides *whether* to alert, not *how*.
- **Log the decision.** Record the watch, the quote, the threshold and the model or rule version for each alert sent and each alert suppressed; without suppressed alerts in the log, nobody can measure whether alerts help.
- **Expire watches.** A watch for a past date, or untouched for months, is closed automatically.

{id: personalization-and-recommendations--sizing-the-alert-load}
### Sizing the alert load

Alert evaluation is a load on the price and availability path, and on an OTA that path is the most expensive one in the system. In 2027 Roomstead had, illustratively, **7.4 million** active saved searches with price alerts, most of them on Roomstead Circle member accounts. Its 2019-era job re-priced each one four times a day with one Pricegrid read per watch: 7.4 million × 4 = 29.6 million reads a day, about **340 a second** on average, under 2% of Roomstead's average **21,000** Pricegrid reads a second. But the job ran in four bursts of about 30 minutes, at roughly **4,100 reads a second** each, and that one of those bursts started at 18:00 CET, in the European evening peak. On Black Friday 2027 (26 November), when lookups peaked at 96,000 a second and Pricegrid's cache hit rate fell from 94% to 71%, the alert job was one of the first workloads Roomstead's degradation mode paused ([Peaks, Regions and Languages: Global Scale and Reliability](#global-scale-and-reliability)).

Event triggering changes the shape of the load. Roomstead receives about **650 million** availability, rates and inventory (ARI) update messages a day, and most touch no watch. Matching changes against an index of watches keyed by property and date, and re-pricing only matches, cut the illustrative evaluation load by about 80% in Jonas's tests and moved it off the evening peak. Nookaway's calendar and price edits are far fewer, so event triggering there was cheap; its nightly job existed only because nobody had wired the events.

{id: personalization-and-recommendations--personalization-in-practice}
## Personalization in Practice

{id: personalization-and-recommendations--the-documented-record}
### The documented record

The public record is uneven: Airbnb has published a long, dated series, Booking.com research and platform material, Expedia ranking posts; Agoda, Trip.com and Vrbo little that could be verified, so nothing here describes their systems. Three observations follow.

First, **the same representations serve many surfaces.** Airbnb reported that its guest embeddings also rank promotional e-mails (+5.04% e-mail clicks, per its 2026 post) and that embedding-based retrieval improved e-mail-promotion bookings by 2.3% ([Zha et al., 2026](https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/); [Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). Search, recommendations and customer relationship management (CRM) consume one set of representations.

Second, **the gains are small per change and large in aggregate.** At Nookaway's 2026 gross booking value of about €2.98 billion, a 0.3% lift in uncancelled bookings is worth roughly €9 million of booking value a year, or about €1.3 million of fee revenue at its realized take rate of about 14.4% ([Liquidity, Take Rates and Look-to-Book: The Economics of Stays Marketplaces](#stays-marketplace-economics)). That pays for a team, not for a platform built on unmeasured claims.

Third, **Booking.com discloses personalization as a ranking factor with an opt-out.** Its "How we work" page lists the user's past searches and interactions among factors that can influence ranking, unless the user has opted out of personalization ([Booking.com, 2025](https://www.booking.com/content/how_we_work.html)). Airbnb's Help Center says past interactions and bookings shape results and that a guest with a home reservation may see nearby experiences and services for those dates ([Airbnb Help Center, n.d.](https://www.airbnb.com/help/article/39)). Personalization in stays is now a disclosed, switchable parameter.

{id: personalization-and-recommendations--corvane-worked-example-one-intent-two-brands}
### Corvane worked example: one intent, two brands

Jonas's proposal to the architecture forum in May 2027 was a **Trip Intent Service** inside the One Stay program, under Corvane ID ([Who Is Booking, Who Is Hosting: Identity, Accounts and Access](#identity-accounts-and-access)), with brand-specific recommendation models on top. The forum argued about what to share, what to re-price, and what to measure.

**What to share.** The intent store, the alert evaluator and the notification platform are shared; recommendation models are not. One Stay had already kept ranking models per brand, and Jonas extended that to recommenders: Roomstead's similar-hotel model and Nookaway's similar-home model learn from different behavior over different supply. The shared contract is the intent record, which carries an optional `brand_scope`. An intent captured on Nookaway is visible to Roomstead only if the guest has linked the two brands under Corvane ID and agreed to see "your trips across Roomstead and Nookaway"; otherwise it stays in the brand where it was captured. Noor van Dijk insisted on this rule, and it cost little: in illustrative 2027 data, about 9% of Nookaway bookers also had a Roomstead account in the same browser, so the cross-brand case was real but not the bulk of the value.

**What to re-price.** Every wishlist render, alert and recommendation e-mail would quote a total through the brand's own pricing path: Pricegrid for Roomstead, Almanac plus pricing rules for Nookaway. Both expose the same quote contract that checkout uses ([Turning an Offer Into a Booking: Checkout Orchestration](#checkout-orchestration)), so an alert total and a checkout total come from the same code.

**What to measure.** Kenji Arai's data team set up a permanent **5% alert holdout** at Nookaway: watches are created and evaluated as usual, decisions are logged, but no message is sent. Six weeks of illustrative results:

| Group | Guests with an active watch | Uncancelled bookings for the watched trip within 30 days | Rate |
| --- | --- | --- | --- |
| Alerts sent | 1,140,000 | 205,200 | 18.0% |
| Holdout (decided, not sent) | 60,000 | 10,200 | 17.0% |

The last-click report had credited alerts with all 205,200 bookings. The holdout says about **1.0 percentage point**, or roughly **11,400** of them, were incremental, about one in eighteen. That is still a good channel: the incremental bookings cost almost nothing, and alerts slightly reduced guest cancellations, because guests booked at a price they had been watching. But it changed two decisions. Nookaway stopped sending alerts for price moves under 5% of the total, which the holdout showed produced no incremental bookings and most unsubscribes, and it moved the budget for a "more alerts" project to cold-start work on Roomstead's anonymous traffic.

{id: personalization-and-recommendations--privacy-consent-and-the-non-profiling-path}
## Privacy, Consent and the Non-Profiling Path

In the EU, personalization runs inside four sets of rules, each of which becomes a system requirement. [Rules of the Stay: Short-Term Rental Regulation, DSA and Consumer Law](#stays-regulation) owns the full map.

| Rule | What it requires | System requirement |
| --- | --- | --- |
| **GDPR**, [Regulation (EU) 2016/679](http://publications.europa.eu/resource/celex/32016R0679) | A lawful basis for processing; **profiling** (Art. 4(4)) is automated evaluation of personal aspects such as preferences; the right to object to processing for direct marketing, including profiling (Art. 21) | Consent and objection state on every intent and profile record; purpose tags; deletion and export of the intent store |
| **ePrivacy Directive**, [2002/58/EC, as amended](http://publications.europa.eu/resource/celex/02002L0058-20091219) | Consent for non-essential storage on the device (Art. 5(3)); consent for e-mail marketing, except that a seller may e-mail its own customers about "its own similar products or services" if they can object at collection and in every message (Art. 13(2)) | Device-level consent read before any identifier is set; marketing-mail eligibility computed per guest, per brand |
| **Digital Services Act**, [Regulation (EU) 2022/2065](http://publications.europa.eu/resource/celex/32022R2065) | Online platforms using **recommender systems** must explain their main parameters and any options to modify them (Art. 27); very large online platforms must offer at least one option "not based on profiling" for each recommender system (Art. 38). The definition (Art. 3(s)) covers ordering search results | A documented parameter list per surface; a user setting that switches every surface to a non-profiling path |
| **Omnibus Directive**, [Directive (EU) 2019/2161](http://publications.europa.eu/resource/celex/32019L2161) | Consumers must be told when a price is **personalized** on the basis of automated decision-making (recital 45, amending Directive 2011/83/EU); this does not cover dynamic pricing that responds to demand without personalization; applies from 28 May 2022 | A hard boundary between personalizing *which* stays are shown and personalizing *what price* is charged |

Three design consequences follow.

**Build the non-profiling path for every surface, whatever your designation.** Booking.com has been a designated very large online platform since 25 April 2023, so Article 38 applies to it directly ([European Commission, list of designated VLOPs](https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses)). A smaller marketplace may not be bound by Article 38 but needs the same path anyway: for guests who refuse consent, for logged-out traffic, as the cold-start fallback and as the control arm of every personalization experiment. Built as a maintained ranking (query relevance, destination popularity, quality), it is one system with four uses; built as an afterthought, it fails all four.

**Separate personalizing the shelf from personalizing the price.** Showing the Novaks family apartments first personalizes ranking. Charging them more for the same apartment because their history suggests they would pay is personalized pricing, with a disclosure duty in the EU and a trust problem everywhere. Disclosed member and closed-user-group rates are a different case, owned by [Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty). My rule is that recommendation and personalization services **never write to a price**; they read prices from the pricing path and can only choose which offers to show.

**Treat sensitive inferences as out of scope.** Travel histories can reveal health (clinic visits), religion (pilgrimage destinations), sexual orientation (properties marketed to particular communities) and family situation. GDPR Article 9 sets a high bar for special categories of data. I would exclude such inferences from features and segments explicitly, review new features against that list, and keep the review record.

{id: personalization-and-recommendations--measuring-whether-personalization-works}
## Measuring Whether Personalization Works

Personalization claims credit by default: rails and alerts sit on the path of guests who were going to book anyway, and last-click attribution gives them the booking. The Nookaway holdout generalizes into five practices.

- **Long-running holdouts per surface.** Keep a small, stable share of guests who see the non-personalized version of a surface (or receive no alerts) for months, not weeks. Booking windows in stays are long; a two-week test misses the bookings that matter. [Testing Everything: Experimentation Platforms for Stays](#stays-experimentation) owns the methods for delayed outcomes and interference.
- **Measure uncancelled bookings for the trip, not clicks on the surface.** A rail that raises clicks and lowers bookings by distracting the guest is common.
- **Count cannibalization.** A recommendation that moves a booking from organic search to the rail creates no value; holdouts see the difference, attribution reports cannot.
- **Measure promise-keeping.** Two operational metrics belong on the personalization dashboard: the share of alerts and recommendation impressions whose quoted total differed from the property-page total for the same stay, and the share pointing to stays that were unavailable when rendered. Both should be near zero by construction.
- **Watch the supply side.** On Nookaway, personalization that concentrates demand on already-popular homes starves new hosts. Exposure share for listings under 90 days old is a guardrail.

Booking.com's 2019 lesson applies directly: improvements in a model's offline metric often do not translate into business value ([Bernardi et al., 2019, as summarized by Colyer](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/)). A recommender's offline recall is a reason to run an experiment, not a result.

{id: personalization-and-recommendations--trade-offs}
## Trade-offs

| Decision | Option A | Option B | When A is right | When B is right |
| --- | --- | --- | --- | --- |
| **Where personalization lives** | Inside the search ranker as features | Separate recommendation service per surface | The surface is a ranked list for a query (search results) | No query or a partial one (home page, similar stays, e-mail) |
| **Guest representation freshness** | Daily batch embeddings | Streaming updates on each event | Long-term taste, early-stage team, modest traffic | Guests plan over days and the platform supports streaming inference; measurable gains justify it |
| **Alert trigger** | Scheduled polling | Event-triggered matching | Few watches, cheap pricing path, no change-event stream | Many watches, expensive pricing path (OTA), reliable change events |
| **Intent ownership** | Per brand | Shared store under group identity | Brands have separate identities and no linking consent | Shared identity exists, guests opt in to linking, and the same families use both brands |
| **Models** | Shared recommender across brands | Separate recommenders per brand | Supply is similar and behavior transfers | Supply models differ (room types vs one-unit homes); the default for Corvane |

I would argue hardest about the second row. Streaming embeddings pay at Airbnb's scale, but without an intent store, live re-pricing and holdouts they optimize the wrong thing first. The order I use: capture intent, keep promises about price and availability, measure, and only then make representations fresher.

{id: personalization-and-recommendations--hotels-and-homes-where-the-two-marketplaces-differ}
## Hotels and Homes: Where the Two Marketplaces Differ

Much of personalization is shared. The differences are in what the guest saves, what changes underneath it, and what a good substitute is.

| Dimension | Accommodation marketplace (OTA-style) | Hosted-stays marketplace |
| --- | --- | --- |
| **What guests save** | Searches and prices: a destination and dates watched for a better rate; hotel favorites for repeat or business travel | Specific homes, in shared wishlists, discussed by a family or group |
| **What changes underneath** | Rates and restrictions per room type and rate plan, very often (Roomstead: about 650 million ARI messages a day); a price alert can fire on any of them | Host price edits and calendar blocks, fewer per unit; but each home is one unit, so "sold" is total and sudden |
| **Alert semantics** | "Cheapest qualifying offer for my party dropped", across room types and rate plans; cancellation terms differ by plan | "This home's total for my dates dropped" or "this home is almost gone"; one calendar, one price set |
| **Good substitute** | Same district, star rating, price band and policy; chains and brands help | Same capacity and bedrooms, layout, amenities and style; location within the neighborhood; host quality |
| **Cold start (listing)** | Deep content: stars, brand, mapped location, reviews from elsewhere | Thin content: host photos and text; behavior must be earned |
| **Persona switching** | Strong: business and leisure trips by the same account; business travel is often repetitive and personalizable | Weaker within one account, but group bookings mix several people's preferences |
| **Repeat behavior** | Repeat stays at the same hotel are common for business travelers; "book again" is a real surface | Repeat stays in the same home are rare; repeat destinations are common |
| **Price personalization risk** | Member and loyalty prices, mobile and country rates must be disclosed as such, not inferred ([Deals, Members and Programs: Promotions and Loyalty](#promotions-and-loyalty)) | Hosts set prices; platform-side personalization of price is rare and should stay so |
| **Two-sided objective** | Partner programs and commission can leak into recommendations; the ranking-transparency rules of [Ordering the Results: Ranking for Guests, Partners and the Marketplace](#stays-ranking) apply to every rail | Host fairness: new listings and individual hosts need exposure; acceptance and cancellation risk matter |
| **What can be shared** | Intent store, alert evaluator, notification platform, consent handling, embedding training infrastructure, holdout framework | Same |

My judgement for Corvane: **share the memory, not the taste.** The trip intent store, the alert evaluator, the quote contract, the notification platform and the measurement framework are the same problem in both marketplaces and should be built once. Sharing the recommendation models would mostly mean that Roomstead's hotel signals dominate Nookaway's homes, a small instance of **The Hotel-Shaped Home**. The convergence that does exist (Roomstead sells apartments from professional managers; Nookaway will pilot boutique hotels in 2028) argues for a shared candidate pool *by consent* across brands, not for one model.

{id: personalization-and-recommendations--failure-modes}
## Failure Modes

The nightly-rate alert, the wishlist that stores prices and the alert after booking are covered above. Three further failures are less visible.

- **Alert storms from supply bugs.** An OTA rate error (the **€12 rate at Hotel Miradouro** on 9 March 2027, when a decimal-mapping error sent €12.00 instead of €120.00 for 38 minutes) is also a price drop of 90%. An event-triggered evaluator that trusts it sends thousands of alerts for an error the marketplace will honor at its own cost. Alerts need the same price-anomaly checks as checkout ([Never Sell the Same Night Twice: Overbooking, Allotments and Concurrency](#inventory-integrity)), and a drop beyond a plausibility bound should be held, not broadcast.
- **Consent drift.** A new feature or segment starts using data collected under a narrower purpose: Nookaway search history used for Roomstead e-mail, or a marketing-consent flag read only at sign-up. Consent must be checked at the point of use.
- **Unowned models.** A similar-stays model trained once in 2024, never retrained, still serving 20% of property-page impressions. **The Unwatched Model** in its quietest form: no one notices because nothing breaks; it just gets worse.

{id: personalization-and-recommendations--the-chief-architect-s-view}
## The Chief Architect's View

Seven decisions belong at group level, each with an owner.

1. **Name the system of record for saved intent.** One trip intent store per group (or per brand, if identities are not shared), owned by one team, with a published contract: intent, wishlist, watch, lifecycle states, consent scope, expiry. At Corvane this is the Trip Intent Service in One Stay, owned by Jonas Weber's group search and ranking organization.
2. **Make "no unpriced promise" a platform rule.** Every surface that shows a price, including e-mails, push notifications, wishlists and rails, obtains it from the quote contract at render or send time, checked automatically by the promise-keeping metrics above.
3. **Keep personalization out of prices.** Personalization services read prices and never write them; member and promotional prices belong to promotions and loyalty.
4. **Own the representations centrally, the surfaces locally.** Embeddings, their training pipelines and versions belong to the ML platform and a central relevance team ([Models in Production: ML Platforms and Use Cases for Stays](#stays-ml-platform)); each surface belongs to a product team accountable for its holdout.
5. **Require a holdout for every surface that claims revenue.** The holdout share is small and permanent; its results are reviewed quarterly next to the attribution numbers.
6. **Maintain the non-profiling path as a product,** with an owner, a quality bar and an experiment of its own.
7. **Decide cross-brand use explicitly.** The privacy lead signs off the scope, and the default is brand-local.

What to watch: generative assistants in front of search ([AI Across the Stay: Agents, Assistants and Automation](#ai-in-travel-stays)) make trip intent the interface. "Two adults, two kids, Lisbon, first week of August, under €1,300 all in" is a trip intent stated directly; a marketplace with a clean intent model and a quote contract that returns totals can answer it, and one with personalization scattered across rails and nightly jobs cannot.

{id: personalization-and-recommendations--questions-to-ask}
## Questions to Ask

1. Where is a guest's trip intent stored, who owns that store, and what closes an intent when the guest books on either brand?
2. When a wishlist, alert or recommendation shows a price, which service computed it, how old can it be, and is it the total for the guest's dates and party?
3. What fraction of alerts sent last month pointed to a stay that was unavailable or more expensive when the guest opened it?
4. How does the alert evaluator learn about price changes, what does it cost the pricing path at peak, and what does degradation mode do to it?
5. What do logged-out and first-time guests see, and what signals personalize it without an identifier?
6. Which recommendation surfaces have a running holdout, and what is each surface's incremental effect on uncancelled bookings?
7. Is there a non-profiling option for every recommender, and is it a maintained ranking or an afterthought?
8. Can any personalization service change a price, and how would we know if one did?
9. Which features or segments could reveal sensitive characteristics, and who reviewed them?
10. Who owns the listing embeddings, how often are they retrained, and which surfaces break if a new version shifts the space?

The Novaks came back because Corvane remembered their trip, imperfectly, and then decided at a property page where the €145 became €1,271.20. That page, where room types, rate conditions, fees and taxes become one total and one decision, is the subject of [The Moment of Decision: Property Pages, Room Selection and Total Price](#property-page-and-room-selection).

{id: personalization-and-recommendations--sources-and-evidence}
## Sources and Evidence

{id: personalization-and-recommendations--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [Real-time Personalization using Embeddings for Search Ranking at Airbnb](https://www.kdd.org/kdd2018/accepted-papers/view/real-time-personalization-using-embeddings-for-search-ranking-at-airbnb) — M. Grbovic and H. Cheng, KDD, 2018. Listing and user embeddings for ranking and similar listings; 99% of conversions.
- [Improving Deep Learning for Airbnb Search](https://arxiv.org/abs/2002.05515) — M. Haldar et al., arXiv, 2020. Cold start for new listings as a main area of ranking improvement.
- [Optimizing Airbnb Search Journey with Multi-task Learning](https://arxiv.org/abs/2305.18431) — C. H. Tan et al., arXiv, 2023. Journeys of weeks and dozens of searches; milestone actions used as labels.
- [Applying Embedding-Based Retrieval to Airbnb Search](https://arxiv.org/html/2601.06873v1) — M. Abdool et al., arXiv, 2026. Two-tower retrieval with daily listing tower; +2.3% e-mail-promotion bookings.
- [Personalizing Airbnb Search by Learning from the Guest Journey](https://airbnb.tech/ai-ml/personalizing-airbnb-search-by-learning-from-the-guest-journey/) — D. Zha et al., Airbnb Tech, 2026. Long- and short-term sequences, daily batch encoder, online gains, e-mail ranking.
- [The Guest Journey, Updated in Real Time: Extending Airbnb's Sequence Recommender with Chronon](https://medium.com/airbnb-engineering/the-guest-journey-updated-in-real-time-extending-airbnbs-sequence-recommender-with-chronon-8f1582578553) — P. Hou et al., Airbnb Tech Blog, 2026. Push Mode and in-pipeline inference; staleness from two days to under a minute.
- [Personalization Without User Identity](https://medium.com/airbnb-engineering/personalization-without-user-identity-8e7891a1d486) — W. Jiang et al., Airbnb Tech Blog, 2026. Proximity features for cold-start guests; consent and soft-dependency design.
- [Academic Publications and Airbnb Tech: 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/) — Airbnb Tech, 2026. Augmenting search results with recommendations; text-and-photo listing embeddings.
- [How Search Results Work](https://www.airbnb.com/help/article/39) — Airbnb Help Center, n.d. (live 2026). Past interactions and reservations as personalization inputs.
- [The Continuous Cold Start Problem in e-Commerce Recommender Systems](https://arxiv.org/abs/1508.01177) — L. Bernardi et al., arXiv, 2015. Infrequent visits and persona switching at Booking.com.
- [150 Successful Machine Learning Models: 6 Lessons Learned at Booking.com (review)](https://blog.acolyer.org/2019/10/07/150-successful-machine-learning-models/) — A. Colyer, The Morning Paper, 2019. Traveler-context model families; model gains vs business gains.
- [Unlocking the Power of Customization: How Our Enrichment System Transforms Recommendation Data](https://medium.com/booking-com-development/unlocking-the-power-of-customization-how-our-enrichment-system-transforms-recommendation-data-e71832fc4ef4) — Booking.com Engineering, 2025. Self-served recommendation platform; accurate-price and wishlist-count enrichments.
- [How We Work](https://www.booking.com/content/how_we_work.html) — Booking.com, 2025. Personalization as a disclosed ranking factor with an opt-out.
- [Learning to Rank at Expedia Group: How to Adapt the Property Search Result Page](https://medium.com/expedia-group-tech/learning-to-rank-at-expedia-group-how-to-adapt-the-property-search-result-page-based-on-f4ebef78c94b) — Expedia Group Tech, 2024. Property embeddings; similar-property alternatives around a pinned hotel.

{id: personalization-and-recommendations--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Regulation (EU) 2022/2065 (Digital Services Act)](http://publications.europa.eu/resource/celex/32022R2065) — EU, 2022. Recommender-system definition (Art. 3(s)), transparency (Art. 27), non-profiling option for very large platforms (Art. 38).
- [List of designated VLOPs and VLOSEs](https://digital-strategy.ec.europa.eu/en/policies/list-designated-vlops-and-vloses) — European Commission, n.d. (live 2026). Booking.com's designation on 25 April 2023.
- [Regulation (EU) 2016/679 (GDPR)](http://publications.europa.eu/resource/celex/32016R0679) — EU, 2016. Profiling (Art. 4(4)), right to object to direct-marketing profiling (Art. 21), special categories (Art. 9).
- [Directive 2002/58/EC (ePrivacy), consolidated 19 December 2009](http://publications.europa.eu/resource/celex/02002L0058-20091219) — EU, 2009. Device storage consent (Art. 5(3)); e-mail marketing to existing customers (Art. 13(2)).
- [Directive (EU) 2019/2161 (Omnibus Directive)](http://publications.europa.eu/resource/celex/32019L2161) — EU, 2019. Disclosure of personalized prices (recital 45); application from 28 May 2022.

{id: personalization-and-recommendations--research-and-practitioner-sources}
### Research and practitioner sources

- [Efficient Estimation of Word Representations in Vector Space](https://arxiv.org/abs/1301.3781) — T. Mikolov et al., arXiv, 2013. The word2vec technique behind session-based listing embeddings.
- [Hybrid Model with Time Modeling for Sequential Recommender Systems](https://arxiv.org/abs/2103.06138) — M. Santana and A. Soares, arXiv, 2021. Describes the Booking.com WSDM WebTour 2021 next-destination dataset.

Corvane is fictional; architectural recommendations and labeled inferences are the author's judgement.
