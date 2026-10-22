{id: query-understanding}
# 19. What Did They Mean? Query Understanding and Autocomplete

![What Did They Mean? Query Understanding and Autocomplete — logo](listing-systems-architecture/posts/19-query-understanding/assets/images/19-query-understanding/logo.jpeg)

> **IN THIS CHAPTER, YOU WILL:** Learn how listing marketplaces turn short, misspelled, multilingual queries into structured searches: language analysis per country, spelling and synonyms, query categorization, attribute extraction, autocomplete, null-result recovery, hybrid retrieval with embeddings, and natural-language search with large language models. You will follow Tradeyard's e-bike queries through the November 2027 bikes split.

> **WHY THE BUSINESS CARES:** A query that returns nothing, or the wrong category, is a buyer who leaves and a seller who gets no contact. Query understanding decides how much of the inventory a buyer can actually reach with the words they use.

> **WHY ARCHITECTS SHOULD CARE:** Query understanding couples search to the taxonomy, the attribute dictionary, the language stack and, increasingly, to ML models and LLM providers. Built as scattered rules and synonyms, it breaks every time a category changes; built as a governed layer with its own evaluation, it becomes the cheapest relevance lever the marketplace has.

> **KEY POINTS:**
>
> * **In listing search, understanding a query mostly means compiling it into filters.** Buyers type "ebike 28 inch" or "T3 balcon Lyon 7"; the marketplace already has categories and attributes for those words. Mapping words to the taxonomy and attribute dictionary does more for relevance than better text matching, and it must be versioned with them.
> * **Every interpretation needs a confidence and a way back.** Apply high-confidence interpretations as filters, weaker ones as boosts, show them as removable chips, and recover from thin results with a defined relaxation order. A wrong filter silently hides inventory; a visible, reversible one costs a tap.
> * **Embeddings and LLMs are layers over the structured core, not replacements.** The documented marketplace cases use dense retrieval to fill low-recall searches and LLMs to compile natural language into the existing filter schema, validated before the engine runs. They need the same per-country evaluation, monitoring and owners as any model.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](#where-listing-systems-go-wrong):**
>
> * **The Attribute Junkyard** — Query tagging can only map words to attributes that exist once, with one meaning; free-form attributes leave queries nothing to compile to.
> * **The Category Straitjacket** — A query categorizer hard-wired to one version of the category tree turns every taxonomy change into a relevance regression.
> * **Set-and-Forget AI** — Query classifiers, spelling models and LLM query compilers decide what buyers see, yet often run without evaluation sets, monitoring or an owner.

A listing query is short, often misspelled, written in whatever language and dialect the buyer speaks, and usually **a request for a filter in disguise**. "ebike gazelle" means category e-bikes, brand Gazelle. "golf 8 automatik" means make Volkswagen, model Golf, generation 8, automatic gearbox. "T3 balcon Lyon 7" means three main rooms, a balcony, Lyon's 7th arrondissement. None of these buyers is asking for text relevance. They are asking the marketplace to recognize its own vocabulary in their words.

**Query understanding** is the set of steps that turns the raw query string into a structured query: normalized and analyzed text, a predicted category, extracted attribute values and locations, corrections, expansions and, increasingly, a semantic representation. This is where Part IV's claim that structure beats cleverness becomes a design: the categories and attributes that queries compile to come from the taxonomy and attribute service of [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies) and [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas). It sits between the search contract and the engine described in [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture), inside a latency budget of about 25 ms at Veldmark. It hands its output to [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), which orders what retrieval finds.

This chapter owns three terms: **query understanding**, **query categorization** (predicting the category a query is about) and **hybrid retrieval** (combining lexical, structured and embedding-based retrieval in one result set). It treats autocomplete as part of query understanding, because a good suggestion is a query the system already understands.

{id: query-understanding--setting-the-scene-at-veldmark-eleven-ways-to-say-e-bike}
## Setting the Scene at Veldmark: Eleven Ways to Say E-Bike

Veldmark is the fictional marketplace group this book follows (see [Meet Veldmark: Four Brands, One Platform to Build](#meet-veldmark)). On **Monday 1 November 2027**, Tradeyard's bike categories (six country leaves in the Netherlands, most of them generic) would be replaced by canonical leaves for city bikes, e-bikes, cargo bikes, kids' bikes and more, the first change to run through the new group taxonomy and attribute service (see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)). In early October, Priya Raman, Head of Data & ML, and Tomasz Wiśniewski, head of the group search platform, sat down with a month of Tradeyard Netherlands query logs to answer one question: *when the e-bikes category exists, will the people looking for e-bikes land in it?*

The logs were sobering. Tradeyard NL had about **380,000** live bike listings across all bicycle categories, of which about **214,000** would land in the new city-bike leaf and about **38,000** were e-bikes. About a quarter of the 1.9 million weekly bike searches expressed e-bike intent, in at least eleven forms: "ebike", "e-bike", "e bike", "e-fiets", "efiets", "elektrische fiets", "elektrischefiets", "fiets met trapondersteuning", "elektrische damesfiets", brand-plus-word forms like "gazelle elektrisch", and, a trap, "speed pedelec", which in the Netherlands is legally a moped with its own license plate, not an e-bike.

The Solr analyzer that Tradeyard Netherlands had used for years treated them very differently. "e-bike" was split into "e" and "bike", and "bike" matched almost every bike listing whose seller had written the English word, so the query returned about 31,000 results, most of them ordinary bikes. "ebike" was one token found in about 2,100 listings. "elektrische fiets" matched about 18,400 listings, because Dutch sellers write it that way but do not write "elektrischefiets" as one word, which returned 140. The same intent produced four result sets that shared less than half their top 50. Contact rates per search differed by a factor of three across the variants.

Belgium added French ("vélo électrique"), Poland "rower elektryczny" and Portugal "bicicleta elétrica". Each country's analyzer had its own history of hand-maintained synonyms that nobody fully owned. The bikes split would make the problem visible: from 1 November, a query that did not resolve to the e-bikes category would miss a category that held every e-bike.

{id: query-understanding--concepts-from-query-string-to-structured-query}
## Concepts: From Query String to Structured Query

**Query normalization and analysis.** Unicode normalization, lowercasing, accent folding, tokenization, stemming and decompounding, per language. Analysis must agree between the query side and the index side, or matching fails silently.

**Spelling correction.** Mapping a misspelled token to an intended one, either automatically ("auto-correct") or as a suggestion ("did you mean"), against the marketplace's own vocabulary of brands, models, place names and category words.

**Synonyms.** Equivalences ("e-bike = elektrische fiets") and one-way expansions ("gazelle → bike brand"), maintained per language and market.

**Query categorization.** Predicting the category, or a ranked list of categories with probabilities, that a query is about. It is a classification problem whose label set is the category taxonomy.

**Query tagging (attribute extraction).** Recognizing spans of the query that name attribute values ("gazelle" → brand, "28 inch" → wheel size, "T3" → rooms 3) or places ("Lyon 7" → an arrondissement). It is named-entity recognition against the attribute dictionary in [Attributes Without Chaos: Schemas, Dictionaries and Validation](#attribute-schemas) and the location model in [Where Is It? Location, Geocoding and Privacy](#location-and-geo).

**Interpretation.** The structured result of all these steps: categories, filters, boosts, corrected text and, optionally, an embedding, each element with a confidence. One query may have several candidate interpretations.

**Null and low-result recovery.** What the system does when an interpretation returns nothing or too little: correct, relax, widen, broaden, or offer a saved search.

**Hybrid retrieval.** Running lexical, structured and dense (embedding-based) retrieval for the same request and fusing the results.

**LLM query compiler.** A large language model (LLM) that turns a natural-language request into the marketplace's existing structured query, which the classic engine then executes.

{id: query-understanding--architecture-shared-vocabulary-local-policy}
## Architecture: Shared Vocabulary, Local Policy

Query understanding runs inside the search API, before retrieval, for every request that has text. The diagram shows the reference architecture I recommend. Steps that need models call them through a cache: the head of the query distribution repeats, so the models do their real work on the tail.

![Diagram: Query understanding as a compiler](listing-systems-architecture/posts/19-query-understanding/assets/images/19-query-understanding/fig01-query-understanding-compiler-each-step-adds.jpeg)

**Figure 1:** *Query understanding as a compiler. Each step adds structure with a confidence, the taxonomy and attribute dictionary supply the vocabulary, and the interpretation is shown back to the buyer as chips and corrections so that wrong guesses can be undone.*

Each step has its own owner and its own reason to change.

| Component | Owned by | Changes when |
| --- | --- | --- |
| Analyzers per language | Group search platform, with marketplace input | Engine migration; language added |
| Spelling vocabulary | Generated from listings and query logs per market | Daily |
| Synonyms | Marketplace search teams, per market | Continuously, with review |
| Query categorizer | Data & ML, per brand | Taxonomy version changes; retraining |
| Attribute and location tagger | Data & ML, built on the dictionary | Dictionary releases |
| Interpretation policy (filter, boost or suggest) | Marketplace search teams | Experiments |
| Evaluation sets and harness | Group search platform | Quarterly refresh |

The table encodes a principle: **the vocabulary is shared, the policy is local**. The taxonomy and attribute service gives every brand one dictionary of what words can mean. How aggressively a marketplace turns those meanings into filters is a product decision each marketplace owns and tests.

{id: query-understanding--language-analysis-per-country}
## Language Analysis per Country

Analysis is the source of most silent failures in query understanding. Four mechanisms matter for European listing marketplaces.

**Tokenization and hyphens.** Product and model names are full of hyphens, digits and units: "e-bike", "1.5 TSI", "28-inch", "T3", "iPhone 13". A tokenizer that splits on every hyphen turns "e-bike" into "e" and "bike"; one that never splits leaves "e-bike" unequal to "ebike". The reliable approach is to index and query several forms: the original token, the joined form ("ebike") and the split parts with lower weight. Units and model codes need explicit patterns: a Dutch seller may write "28 inch", "28\"" or "28 duim" for the same wheel size.

**Accent and character folding.** Vinted's 2026 autocomplete indexes both accented and ASCII-folded forms across 24 languages, so that "z" matches "Zara" and "Žalgiris", while "Ž" matches only the accented form ([Vinted Engineering, 2026](https://vinted.engineering/2026/04/22/personalized-search-autocomplete/)). The asymmetry is deliberate: a buyer who types the accent has asked for the accented form.

**Stemming.** Language stemmers reduce "fietsen" to "fiets" and "appartements" to "appartement". They help recall and occasionally hurt precision, which is why brand and model names should be protected from stemming with a keyword list.

**Decompounding.** Dutch and German build compounds: "damesfiets" (women's bike), "kinderfiets", "Anhängerkupplung" (tow bar). A buyer typing "dames fiets" and a seller writing "damesfiets" must meet. Lucene-based engines provide compound-word token filters; Elastic documents that its hyphenation decompounder "was built for Germanic languages" and keeps only sub-words found in a supplied word list, so "Kaffeetasse" yields "Kaffee" and "tasse" ([Elastic documentation, n.d.](https://www.elastic.co/docs/reference/text-analysis/analysis-hyp-decomp-tokenfilter)). The word list is the asset: for a marketplace it should come from the category vocabulary and attribute values, not from a general dictionary.

**Multilingual markets.** Tradeyard Belgium serves Dutch and French speakers with one inventory. Detect the query language (with a fallback that tries both), analyze with the matching analyzer, and search the language-specific text fields described in [Search Architecture for Listings: Indices, Freshness and Scale](#search-architecture). Category and attribute tagging should work in both languages against the same dictionary, which is one of the strongest reasons to localize the dictionary rather than the index.

**Analyzer parity is a migration risk.** When Vinted moved from Elasticsearch to Vespa, it contributed Lucene text analyzers to Vespa so that existing language analysis carried over ([Vinted Engineering, 2024](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/)). Any engine change, and any analyzer change, should run a test set of real queries per language and compare tokens before and after. Veldmark's set is 5,000 queries per market, sampled across the head, torso and tail of the query distribution.

{id: query-understanding--spelling-and-synonyms}
## Spelling and Synonyms

{id: query-understanding--spelling-correction}
### Spelling correction

The simplest correction is fuzzy matching in the engine. Elasticsearch's `AUTO` fuzziness allows no edits for terms of up to two characters, one edit for three to five, and two for longer terms ([Elastic documentation, n.d.](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html)). It is cheap and useful as a fallback, but it is blind to the marketplace's vocabulary: it will match "golf" to "gold".

A marketplace speller works better because its vocabulary is the marketplace's own. The design I recommend generates a dictionary per market daily from three sources: tokens in live listings weighted by frequency, tokens in successful queries (followed by a click or contact), and the attribute dictionary's values, including brands and models. A correction is applied automatically only when the original returns few results and the corrected form is both close and much more frequent; otherwise it is offered as "did you mean". Brand names and model codes get protection from correction.

Vinted's autocomplete shows that the expensive step is usually not needed. Its fuzzy cascade runs from exact prefix to edit distance 1 to edit distance 2, stopping at ten unique suggestions, and about 62% of requests resolved at exact prefix ([Vinted Engineering, 2026](https://vinted.engineering/2026/04/22/personalized-search-autocomplete/)).

{id: query-understanding--synonyms}
### Synonyms

Synonyms are where hand-maintained search configuration rots. Three rules prevent it.

1. **Apply synonyms at search time, not index time.** Elastic's `synonym_graph` filter is designed for search analyzers, handles multi-word synonyms correctly, and can be made `updateable` so that reloading search analyzers picks up changes ([Elastic documentation, n.d.](https://www.elastic.co/docs/reference/text-analysis/analysis-synonym-graph-tokenfilter)). Changing a synonym should never require a reindex.
2. **Mine candidates from behavior, approve them by hand.** A useful source is reformulation: buyers who search "x", get little, then search "y" and contact. Candidates go to a reviewer per market, because the cost of a wrong synonym is invisible: "speed pedelec = e-bike" would send moped buyers into bicycles and bicycle buyers past the legal difference.
3. **Prefer structure to synonyms where structure exists.** If "e-bike" and "elektrische fiets" both mean the e-bikes category, the better fix is to tag both to the category, not to make them textual synonyms. Synonyms are for text; categories and attributes are for meaning.

{id: query-understanding--query-categorization-and-attribute-extraction}
## Query Categorization and Attribute Extraction

{id: query-understanding--predicting-the-category}
### Predicting the category

Query categorization is usually a text classifier trained on query-category pairs taken from behavior: the categories of listings that buyers clicked or contacted after the query. It outputs a distribution over categories, not a single answer. "golf" on Tradeyard is ambiguous between golf equipment and Volkswagen Golfs in its small car section; "golf tas" (golf bag) is not.

Three properties separate a production categorizer from a demo.

- **It is versioned with the taxonomy.** When a category splits, the categorizer's label set changes. Behavioral labels for the new categories do not exist yet. The bridge is the taxonomy service's mapping events, which state how old categories map to new ones (see [Category Trees That Can Change: Designing Marketplace Taxonomies](#categories-and-taxonomies)), plus the attribute evidence that tells the classifier which old bike listings were e-bikes. Without that bridge, a taxonomy change is a relevance regression: this is how **The Category Straitjacket** reaches search.
- **It is calibrated.** A probability of 0.9 should be right about 90% of the time, because the interpretation policy acts on thresholds.
- **It is monitored like any decision model.** Veldmark's model governance classes search models as "order" models, which decide what buyers see (see [Models in Production: ML Platforms and Use Cases](#ml-platform)). The categorizer needs an owner, a registry entry and monitors on its prediction distribution, which will move sharply on 1 November.

{id: query-understanding--tagging-attributes-and-places}
### Tagging attributes and places

Attribute tagging finds spans that name values: brands, models, sizes, rooms, energy classes, fuel types. A dictionary matcher over the attribute dictionary's values and aliases gets far, because marketplace vocabularies are bounded; a sequence-labeling model on top handles ambiguity and context. Location tagging is its own problem: "Lyon 7" is an arrondissement, "Den Bosch" is the common name of 's-Hertogenbosch, and "Essen" is a city in Germany and a municipality in Belgium. The location model in [Where Is It? Location, Geocoding and Privacy](#location-and-geo) supplies the gazetteer.

The dictionary is the hard dependency. If the attribute service holds one definition of `bike.wheel_size` with its aliases ("28 inch", "28 duim", "28\""), the tagger can map the query to a filter. If wheel size exists as four free-text keys entered by different country teams, there is nothing to map to: **The Attribute Junkyard** defeats query understanding before any model runs.

Verticals change what a tag means. On Hearthly France, "T3" means three main rooms (pièces), which is not three bedrooms; on Hearthly Spain, "3 habitaciones" means three bedrooms. On Motorvane, "golf 8" means the eighth generation, not model year 2008 or eight doors. These meanings belong in the dictionary, per market, not in tagger code.

{id: query-understanding--from-interpretation-to-query-filter-boost-or-suggest}
### From interpretation to query: filter, boost or suggest

The policy I recommend maps each interpretation's confidence to an action, and shows every applied interpretation to the buyer.

| Confidence | Action | What the buyer sees | Risk if wrong |
| --- | --- | --- | --- |
| High (for example ≥ 0.85, calibrated) | Apply as a **filter** | A removable chip: "Category: E-bikes ×" | Hides relevant inventory until the chip is removed |
| Medium | Apply as a **boost** | Results lean toward the interpretation; a suggestion chip | Mild ordering errors |
| Low | **Suggest** only | "Looking for e-bikes?" | None beyond screen space |
| Conflicting interpretations | Show **both** as options, or blend | Two category suggestions | Choice cost for the buyer |

Two invariants keep the policy honest. First, **adding an interpretation must never increase the result count**. Vinted reported in 2025 that approximate retrieval could make results inconsistent with filters, and set the goal that adding a filter should not increase the number of results ([Vinted Engineering, 2025](https://vinted.engineering/2025/11/18/dense-retrieval/)). Second, **an interpretation the buyer removes is a label**: a removed chip is the clearest negative feedback the categorizer will ever get, and it should flow back into training.

{id: query-understanding--null-and-low-result-recovery}
## Null and Low-Result Recovery

A null-result page is a failed match between demand and supply. Some are genuine (nobody sells a cargo bike within 5 km of a small village tonight); many are artifacts of misspelling, over-eager filters or vocabulary mismatch. The recovery ladder should be explicit, ordered from least to most change to what the buyer asked.

| Step | Action | Example |
| --- | --- | --- |
| 1 | Correct spelling | "gazele" to "gazelle" |
| 2 | Drop the least-confident machine-added interpretation | Remove an inferred color filter |
| 3 | Fall back from all-terms to most-terms text matching | Match three of four words |
| 4 | Widen the location radius in steps | 10 km to 25 km, labeled |
| 5 | Broaden to the parent category | E-bikes to Bikes |
| 6 | Fill with dense retrieval | Visually or semantically similar listings, labeled "similar" |
| 7 | Offer a saved search | "Tell me when one appears" (see [Tell Me When It Appears: Saved Searches and Alerts](#saved-searches-and-alerts)) |

The ladder never removes a filter the buyer chose without saying so. Airbnb has published work on augmenting search with recommendations when searches are too narrow ([Airbnb Tech, 2025](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/)); the general lesson is that a thin result set is an opportunity to show close alternatives, labeled as such.

Step 7 matters for liquidity: a buyer who saves a search after a null result is standing demand that alerts can serve when supply appears.

{id: query-understanding--autocomplete-and-query-suggestions}
## Autocomplete and Query Suggestions

Autocomplete is the earliest point at which the marketplace can steer a query toward something it understands. Vinted's April 2026 description is the most complete public account of a marketplace autocomplete system ([Vinted Engineering, 2026](https://vinted.engineering/2026/04/22/personalized-search-autocomplete/)):

- **Candidates.** About 125 million scored suggestions, regenerated twice a week across more than 50 country-language combinations, built from product metadata (category, brand, color, attributes) and search logs. Query-log candidates were about 2% of the pool but drove about half of suggestion clicks.
- **Ranking.** An offline score based on popularity, sell-through rate and suggestion click-through, normalized per country, language and first letter; then online two-phase ranking in Vespa, with a LightGBM LambdaRank model over 63 features, including per-user features from a feature store, re-ranking the top 20 per node.
- **Matching.** Edge n-grams precomputed at index time cut matching p99 from about 220 ms to 25 ms, with the fuzzy cascade described above.
- **Serving.** Per-country indices in three European data centers; about 4,700 queries per second at 31 ms p99. Cutting the client debounce from 350 ms to 100 ms increased usage.
- **Results.** Suggestion use rose from under 8% to over 17% of search sessions; the learning-to-rank change added about 8% suggestion click-through.

![Diagram: Autocomplete as two pipelines](listing-systems-architecture/posts/19-query-understanding/assets/images/19-query-understanding/fig02-autocomplete-two-pipelines-offline-job-builds.jpeg)

**Figure 2:** *Autocomplete as two pipelines. An offline job builds and scores candidates from logs, vocabulary and live inventory; an online path matches prefixes and re-ranks per user within a few tens of milliseconds. Attaching an interpretation to each suggestion turns a click into a structured query.*

Three design rules follow for listing marketplaces.

1. **Suggest only what returns inventory.** A suggestion for a query with no live listings in the buyer's market is a null result delivered faster. Candidate generation should join live counts.
2. **Attach interpretations to suggestions.** "e-bike in Fietsen › E-bikes" is better than "e-bike", because the click lands the buyer in the category with no categorizer guess at all.
3. **Filter the candidate pool for safety.** Query logs contain abusive terms, personal data and the probing queries of fraudsters. A suggestion is the marketplace speaking, not the user.

{id: query-understanding--semantic-and-hybrid-retrieval}
## Semantic and Hybrid Retrieval

Lexical matching fails on vocabulary mismatch ("aquamarine blouse" against listings that say "blue top") and on categories where the photo says more than the text. Dense retrieval, which embeds queries and listings in one vector space and retrieves by approximate nearest neighbor (ANN), addresses both. The public record from 2023 to 2026 shows how marketplaces use it.

- **Vinted, November 2025.** Dense retrieval in main search uses a two-tower model: a frozen multilingual CLIP (Contrastive Language-Image Pre-training) query tower with a trained projection head, and an item tower that fuses brand and category embeddings with precomputed CLIP image embeddings. Hierarchical navigable small world (HNSW) graph indices in Vespa are split by blocs of connected markets, with fallback from approximate to exact search when the 500 ms budget is at risk. Dense matches are merged with keyword matches and metadata-filter "interpretations" using **reciprocal rank fusion (RRF) in the global ranking phase**, with a per-request cap on dense-only matches. Filling **low-recall sessions** first improved metrics. Full rollout came after about 50 A/B tests. The image embeddings for all primary photos took about a month to compute and need about 1 TB of memory ([Vinted Engineering, 2025](https://vinted.engineering/2025/11/18/dense-retrieval/)).
- **Airbnb, January 2026.** Embedding-based retrieval chose an inverted-file (IVF) index over HNSW because HNSW memory grew under frequent real-time updates and made combining discriminative filters difficult; IVF cluster IDs act as a normal filter in Apache Lucene, at the cost of lower recall. The listing tower runs as a daily batch, so only the query tower runs online ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)).
- **leboncoin, 2023.** A press report of a conference talk describes a CamemBERT-based retriever with ANN in Elasticsearch and a neural re-ranker over the top candidates ([Le Monde Informatique, 2023](https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html)); the primary engineering post could not be verified, and the report is about three years old, so the current system may differ.

The two detailed cases reached **different answers to the same problem**, approximate retrieval under heavy filtering with real-time updates, for documented reasons. Neither is generally right; the choice depends on filter selectivity, update rate and the engine already in use. [Recommendations for Inventory That Disappears](#recommendations) covers the same trade-off for candidate generation.

{id: query-understanding--fusion}
### Fusion

Hybrid retrieval needs a way to merge lexical and dense result lists whose scores are not comparable. Two families are available in the Lucene world.

| Method | How it works | Engine support | When to prefer |
| --- | --- | --- | --- |
| Reciprocal rank fusion | Sums `1/(k + rank)` across lists; ignores raw scores | Elasticsearch RRF retriever, `rank_constant` default 60 ([Elastic documentation, n.d.](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion)); OpenSearch score ranker processor, introduced in 2.19, default 60 ([OpenSearch documentation, n.d.](https://docs.opensearch.org/latest/search-plugins/search-pipelines/score-ranker-processor/)); Vespa global phase (Vinted) | Default choice; needs no tuning |
| Score normalization and combination | Rescales each list's scores (min-max, L2, z-score), then combines (arithmetic, geometric or harmonic mean) | OpenSearch normalization processor, introduced in 2.10, `min_max` and `arithmetic_mean` by default ([OpenSearch documentation, n.d.](https://docs.opensearch.org/latest/search-plugins/search-pipelines/normalization-processor/)) | When weights are tuned per market against judged data |

Fusion produces candidates; it does not replace ranking. The fused set goes to [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking), which applies the learning-to-rank model, freshness and paid-visibility policy.

{id: query-understanding--where-dense-retrieval-belongs-in-a-listing-marketplace}
### Where dense retrieval belongs in a listing marketplace

My recommendation follows the evidence: **use dense retrieval to fill recall gaps, not to replace structured retrieval.** Run lexical and structured retrieval first; add dense matches when the session is low-recall, when the query has no strong interpretation, or in image-led categories such as fashion and furniture; cap the share of dense-only results; and make sure dense matches respect every filter the buyer set.

Dense retrieval has real costs: embeddings for every listing, memory for the ANN index, an embedding call per query, and an evaluation burden, because dense results fail in ways lexical results do not. Vinted's tokenizer quirk that flooded a brand-filtered query for "zx750" with about 7,000 extra dense matches is a reminder that the failure modes are new.

![A structured retrieval core with a capped dense-retrieval ring that fills thin results and an LLM translator that compiles language into validated filters.](listing-systems-architecture/posts/19-query-understanding/assets/images/19-query-understanding/structured-core-with-layers.jpeg)

**Figure 3:** *Embeddings and language models are layers over the structured core: dense retrieval fills low-recall sessions under a cap and every buyer filter, and the LLM compiles language into filters that the attribute dictionary validates.*

{id: query-understanding--natural-language-and-conversational-search-with-llms}
## Natural-Language and Conversational Search with LLMs

Since 2023, several listing marketplaces have published natural-language search features, and **none of the documented cases replaces retrieval with generation**. They use the LLM to compile language into the existing structured query, or to orchestrate existing search tools.

| Marketplace | Feature (date) | What the LLM does | Documented results or limits |
| --- | --- | --- | --- |
| coches.net (Adevinta Spain) | Natural-language car search (2024) | A cheap moderation call classifies the query as valid, unethical or invalid; Claude Haiku on Amazon Bedrock converts it into the site's existing filters with few-shot prompts; the frontend validates and applies them | About 6,000 input and 500 output tokens per query, about 20,000 calls a day, about €19 a day; adoption "still limited" ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/)) |
| leboncoin | Conversational shopping assistant (2024) | GPT-3.5 Turbo extracts preferences as JSON matching the product search API's schema, with category prediction merged into the prompt; JSON mode at temperature 0.1; history capped at 5–10 turns; evaluation by structured diff of expected and generated JSON | OpenAI's Assistants API rejected because messages would be stored on OpenAI's servers ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/building-a-smarter-shopping-experience-the-technology-behind-conversational-search-in-e-commerce/)) |
| leboncoin (cars) | AI search assistant (2024) | Maps needs to keywords, categories and filters | User research: users "are not aware of the benefits" ([Adevinta Tech Blog, 2024](https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/)) |
| OLX | OLX Magic agentic assistant (2024) | An agent plans and calls text, visual and web search tools; learning to rank stays underneath | Latency about 5–10 s against 300–500 ms for classic search, per a third-party talk summary ([ZenML LLMOps Database, 2024](https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture)); the talk lists latency, cost and guardrails as challenges ([MLOps Community, 2024](https://home.mlops.community/public/videos/olx-magic-transforming-e-commerce-search-experience-with-ai-agents-nishi-and-beatriz-2024-11-20)) |
| Zillow | Natural-language search (2023; extended 2024; current state not described here) | Commute, affordability, schools and points of interest as criteria; saveable searches | No architecture published ([HousingWire, 2024](https://www.housingwire.com/articles/zillow-artificial-intelligence-search/)) |
| Rightmove | "Ask Rightmove" conversational search (2026) | Not described | Early findings (data to 30 June 2026): about a 40% uplift in average time on site and "roughly double the propensity to send leads", per the company's H1 2026 results ([Rightmove plc, 2026](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf)) |

Model names, prices and feature availability in this table change quickly; treat them as dated evidence, not current product facts.

{id: query-understanding--the-llm-as-query-compiler}
### The LLM as query compiler

In the pattern these cases share, the LLM receives the query, the market, and a compact description of the filter schema (the category list and the attribute keys and values relevant to the predicted vertical, drawn from the attribute dictionary), and returns a structured query. A validator checks every category and attribute value against the dictionary and drops or repairs what does not exist. The classic engine runs the query. The buyer sees the result with the compiled filters as chips.

![Diagram: The LLM compiles, the engine retrieves](listing-systems-architecture/posts/19-query-understanding/assets/images/19-query-understanding/fig04-llm-compiles-engine-retrieves-validation-against.jpeg)

**Figure 4:** *The LLM compiles, the engine retrieves. Validation against the attribute dictionary keeps hallucinated categories and values out of the query, the engine keeps results grounded in live inventory, and the chips make the compiled interpretation visible and editable.*

The pattern has five properties to defend in a design review. Results are explainable, because the buyer sees the filters. No listing can be hallucinated, because the engine retrieves. Output can be cached by normalized query. Keyword queries never touch the LLM, which bounds cost and latency. And the same structured query can be saved as an alert, which is exactly what Zillow made possible for natural-language searches.

Its limits are latency and data protection. Latency is in hundreds of milliseconds at best, so the compiler should run only for queries that need it, typically long queries or those the classic pipeline cannot interpret with confidence. Query text can be personal data, so prompts and logs fall under the same retention rules as search telemetry, and provider terms decide where text may be processed; leboncoin's rejection of a hosted assistant API over message storage is a documented example of that constraint shaping architecture.

{id: query-understanding--external-assistants-as-a-new-client}
### External assistants as a new client

External AI assistants have started to send queries on the buyer's behalf. In two 2026 posts, ImmoScout24 described a Model Context Protocol (MCP) server for its assistant, launched in November 2025, and an app inside ChatGPT over its property data ([Scout24 Engineering, January 2026](https://medium.com/scout24-engineering/shipping-the-first-mcp-in-heyimmo-at-immoscout24-a278214df005); [Scout24 Engineering, March 2026](https://medium.com/scout24-engineering/what-we-learned-from-launching-immoscout24-app-in-chatgpt-efbed0f7375b)); Rightmove's FY2025 results reported an app submitted to the ChatGPT ecosystem ([Rightmove plc, 2026](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf)). When an external assistant calls marketplace search, the search contract becomes an external product, with a published filter schema, rate limits, attribution for leads and freshness obligations. The query-understanding layer does not disappear; the external model does part of the compiling, and the marketplace's validator becomes the line of defense. [AI Across the Listing Lifecycle](#ai-in-listing-systems) covers how Veldmark opens this channel.

{id: query-understanding--evaluating-query-understanding}
## Evaluating Query Understanding

Query understanding fails quietly, which makes evaluation the part teams skip. The evaluation harness should be a shared group asset, with market-specific data.

| Layer | Offline measure | Online measure |
| --- | --- | --- |
| Analysis | Token parity on a fixed query set per language | Not needed if parity holds |
| Spelling | Precision of automatic corrections on labeled misspellings | Rate of buyers undoing a correction |
| Categorization | Precision and recall at the filter threshold; calibration | Chip-removal rate; search-to-contact by category |
| Tagging | Span-level precision and recall per attribute | Chip-removal rate per attribute |
| Recovery | Share of null results recoverable in replay | Null-result rate; saved searches from null results |
| Dense retrieval | Recall against a reference, on replayed traffic | A/B tests on low-recall sessions |
| LLM compiler | Structured diff against expected queries | Adoption, reformulation, contact rate |

Two lessons from the public record apply. Airbnb found that offline recall measured on logged data tracked online results poorly, because logs contain only what users were shown; replaying a slice of production traffic to an offline cluster tracked A/B results better ([Abdool et al., 2026](https://arxiv.org/html/2601.06873v1)). And leboncoin's structured-diff evaluation of its JSON compiler, which its authors called deliberately simple, is still better than no evaluation: comparing expected and generated structured queries is cheap and catches regressions in prompts and model versions.

The query sets must be refreshed on a schedule and after every taxonomy release, because the right answer for "e-bike" changes on the day the e-bikes category appears.

{id: query-understanding--in-practice-tradeyard-s-e-bike-queries-through-the-bikes-split}
## In Practice: Tradeyard's E-Bike Queries Through the Bikes Split

Priya's and Tomasz's plan for 1 November had four parts, each applying a section above.

**One vocabulary.** The attribute service already held the e-bikes category with its Dutch, French, Polish and Portuguese labels. The team added a query-vocabulary entry: aliases per language ("ebike", "e-bike", "e bike", "e-fiets", "elektrische fiets", "fiets met trapondersteuning", "vélo électrique", "rower elektryczny", "bicicleta elétrica") mapping to the category, and an explicit exclusion for "speed pedelec", which maps to the mopeds category instead. The tagger and the categorizer both read this entry.

![Many e-bike query variants funnelled through one vocabulary entry into the e-bikes category, with speed pedelec diverted to mopeds.](listing-systems-architecture/posts/19-query-understanding/assets/images/19-query-understanding/eleven-ways-one-vocabulary.jpeg)

**Figure 5:** *One vocabulary entry, read by both the tagger and the categorizer, sent 10 of the 11 e-bike query variants to the new e-bikes category and routed speed pedelec, legally a moped, to mopeds.*

**Analysis fixes.** The Dutch analyzer was changed to index and query the joined and split forms of hyphenated tokens, and the compound word list was generated from category labels and attribute values, so "elektrischefiets" and "damesfiets" decompose. The Solr analyzer and the target OpenSearch analyzer were checked against the same 5,000-query Dutch test set.

**A categorizer that survives the split.** Old bike listings were relabeled using the taxonomy service's mapping events and the e-bike attributes from the backfill (motor position, battery capacity), giving the categorizer training labels for the new category before any buyer had used it. The model was entered in the group model inventory as an order-tier model, with a prediction-distribution monitor and Priya's team as owner (the group registry decided on 9 November later made that mandatory for every production model).

**Policy and recovery.** An e-bike interpretation with calibrated confidence of at least 0.85 is applied as a category filter with a chip; between 0.5 and 0.85 it becomes a boost and a suggestion. If the e-bikes filter returns fewer than 20 results within the buyer's radius, the recovery ladder widens the radius before it broadens to all bikes.

The outcome in the four weeks after the split, against the four weeks before, measured on Tradeyard NL bike searches with e-bike intent:

| Measure | Before (October 2027) | After (November 2027) |
| --- | --- | --- |
| Query variants landing in e-bike inventory | 4 of 11 | 10 of 11 (speed pedelec correctly excluded) |
| Overlap of top 50 results across the main variants | under 50% | about 90% |
| Null or under-five-result rate | 6.1% | 2.4% |
| Chip-removal rate on the e-bikes filter | — | 3.8% |
| Search-to-contact rate, e-bike intent | baseline | +11% relative |

These are Veldmark illustrations, not industry benchmarks; the shape is what generalizes. The biggest gain came from vocabulary and policy, not from a model. The 3.8% chip-removal rate became a training signal: most removals came from buyers searching "e-bike accu" (battery), who wanted parts, which led to a new interpretation for e-bike parts in the next release.

Two further projects show where Veldmark is going. Hearthly France is testing an LLM compiler for long queries only, about 6% of Hearthly search traffic, with output validated against the French property schema; "T3 balcon Lyon 7 moins de 400k" compiles to rooms 3, balcony, Lyon 7e and a €400,000 price ceiling, and returns the Lyon apartment at €389,000. Motorvane is extending its tagger with generation codes from its vehicle reference data, so that "golf 8" means the generation of the Essen Volkswagen Golf rather than 2008.

{id: query-understanding--trade-offs}
## Trade-offs

| Decision | Option | When it is right | When it is wrong |
| --- | --- | --- | --- |
| Where meaning lives | Synonyms in analyzers | Pure text equivalence; no structure exists | Words that map to categories or attributes |
| Where meaning lives | Tagging to the dictionary | A governed attribute dictionary exists | Free-form attributes; no dictionary |
| Interpretation policy | Aggressive filters | Calibrated, well-monitored models; visible chips | Unmonitored models; no chips |
| Interpretation policy | Boosts and suggestions only | Early models; ambiguous verticals | Filter-heavy verticals where buyers expect structure |
| Spelling | Engine fuzziness | Fallback; small catalogs | Brand-heavy vocabularies; false matches |
| Spelling | Marketplace speller | Large vocabularies; many brands and models | No query logs yet |
| Retrieval | Lexical plus filters only | Structured verticals; tight budgets | Image-led categories; vocabulary mismatch |
| Retrieval | Hybrid with dense fill | Low-recall sessions; fashion and furniture | Small teams without evaluation capacity |
| Natural language | LLM query compiler for long queries | Rich filter schemas; long-tail phrasing | Short keyword traffic; strict latency budgets |
| Natural language | Agentic assistant | Exploratory, advisory journeys | Main search path; cost per query unbounded |

{id: query-understanding--vertical-differences}
## Vertical Differences

| Concern | General classifieds | Real estate | Automotive | Jobs |
| --- | --- | --- | --- | --- |
| Typical query | Short object words and brands | Place plus rooms, price, features | Make, model, generation, fuel, gearbox | Title, skills, place |
| Hardest problem | Vocabulary breadth; category ambiguity | Place semantics (districts, neighborhoods); room-count conventions per country | Model and trim codes; generations | Title synonyms and seniority |
| What tagging maps to | Thousands of categories, sparse attributes | Rich property schema | Dense vehicle reference data | Occupation taxonomy |
| Spelling vocabulary | Brands and colloquial words | Place names | Model codes ("1.5 TSI", "e-tron") | Job titles |
| Natural-language value | Moderate | High: lifestyle and commute criteria | Moderate to high: needs-based car search | High: experience and skills |
| Dense retrieval value | High in image-led categories | Moderate: photos and descriptions | Low to moderate | High: semantic job matching |

Real estate and automotive have the richest structured vocabularies, which makes tagging and LLM compiling most effective there; general classifieds have the broadest vocabulary, which makes categorization and autocomplete the main levers.

{id: query-understanding--failure-modes}
## Failure Modes

**Synonyms as the dumping ground.** Every relevance complaint becomes a synonym, until the synonym file is thousands of lines that nobody can explain and every new entry has side effects. Move meaning into the dictionary; keep synonyms for text.

**Invisible filters.** The system applies a category or attribute filter without showing it. Buyers who were wrong-footed cannot recover, and the team never learns. Every applied interpretation needs a chip.

**Taxonomy changes without a categorizer plan.** The category tree changes on a Monday; the categorizer still predicts the old categories, or none. Version models with the taxonomy and use mapping events to build labels in advance.

**Analyzer drift.** An engine upgrade or a well-meant analyzer change splits hyphens differently, and a share of queries quietly changes results. Keep token-parity tests per language in continuous integration.

**Unvalidated LLM output.** A compiler returns a category or attribute value that does not exist, and the query returns nothing or errors. Validate every output against the dictionary, and log what was dropped.

**Autocomplete that suggests nothing.** Suggestions built from logs without live counts lead buyers to empty results, or surface offensive or personal strings. Join inventory counts and filter the candidate pool.

**Dense results that ignore filters.** Approximate retrieval returns listings outside the buyer's filters or inflates counts. Enforce filters on every retrieval path and test the "adding a filter never increases results" invariant.

{id: query-understanding--the-chief-architect-s-view}
## The Chief Architect's View

Query understanding is a group concern because it is where search meets the group's shared vocabulary. At Veldmark, the decisions I would hold the line on are these.

1. **One vocabulary, many policies.** The taxonomy and attribute service holds what words can mean, in every language, including query aliases and exclusions. Marketplaces own how aggressively they apply interpretations. Marketplaces keep no private vocabularies, and the group does not set their thresholds.
2. **Every model in the query path is an order-tier model.** Categorizers, taggers, spellers, dense retrievers and LLM compilers are registered, owned, evaluated on market-specific query sets and monitored, under the same governance as ranking models (see [Models in Production: ML Platforms and Use Cases](#ml-platform)).
3. **Taxonomy releases include a query-understanding checklist.** No category split ships without updated query aliases, categorizer labels and evaluation sets. This is where The Category Straitjacket is either broken or rebuilt.
4. **LLMs compile; engines retrieve.** Any natural-language feature uses the group's AI gateway (see [AI Across the Listing Lifecycle](#ai-in-listing-systems)), validates against the dictionary and executes through the search contract. Providers, models and prompts are configuration, so they can change as prices and terms change; Lucía Ortega's data-protection review covers where query text may be processed and how long prompts are kept.
5. **Evaluation is a shared asset.** The group search platform owns the harness and the replay tooling; marketplaces own their query sets and judgments.

What to watch: null-result and low-result rates per market and category, chip-removal rates per interpretation, the share of traffic each layer touches, LLM cost per thousand queries, and the age of each market's evaluation set. A rising chip-removal rate after a taxonomy release is the earliest sign that query understanding and the catalog have drifted apart.

{id: query-understanding--questions-to-ask}
## Questions to Ask

1. Which share of our queries is browse, short keyword, long natural language? Do we design for that mix?
2. Where do the meanings of words live: synonym files, analyzer configurations, tagger code or the attribute dictionary?
3. Which interpretations do we apply as filters, at what confidence, and can buyers see and remove them?
4. What happens, step by step, when a query returns nothing?
5. How does our query categorizer learn about a category that was created yesterday?
6. Do we have token-parity tests per language that would catch an analyzer change before buyers do?
7. Do autocomplete suggestions carry interpretations, and do they ever lead to empty results?
8. If we use dense retrieval, can it return a listing that violates a buyer's filter?
9. If we use an LLM, what validates its output, what does it cost per thousand queries, and where is the query text processed and stored?
10. Who owns each model in the query path, and when was its evaluation set last refreshed?

{id: query-understanding--from-retrieval-to-order}
## From Retrieval to Order

Query understanding decides what the engine retrieves; it does not decide the order in which buyers see it. That order is a negotiation between relevance, freshness, seller fairness and paid visibility, and it is the subject of the next chapter, [Ranking for Two Sides: Relevance, Freshness and Paid Visibility](#ranking).

{id: query-understanding--sources-and-evidence}
## Sources and Evidence

{id: query-understanding--company-engineering-and-investor-sources}
### Company engineering and investor sources

- [How Vinted Serves Personalised Search Autocomplete](https://vinted.engineering/2026/04/22/personalized-search-autocomplete/), Vinted Engineering, 2026 — candidates, ranking, folding, fuzzy cascade, latency and results.
- [Dense Retrieval](https://vinted.engineering/2025/11/18/dense-retrieval/), Vinted Engineering, 2025 — two-tower model, HNSW, RRF fusion, low-recall fill, filter invariant, costs.
- [Vinted Search Scaling Chapter 8: Goodbye Elasticsearch, Hello Vespa Search Engine](https://vinted.engineering/2024/09/05/goodbye-elasticsearch-hello-vespa/), Vinted Engineering, 2024 — analyzer parity during engine migration.
- [From Filters to Phrases: Our AI Revolution in Car Search](https://adevinta.com/techblog/from-filters-to-phrases-our-ai-revolution-in-car-search/), Adevinta Tech Blog (coches.net), 2024 — LLM query compiler, moderation step, tokens and cost.
- [Building a Smarter Shopping Experience: The Technology Behind Conversational Search](https://adevinta.com/techblog/building-a-smarter-shopping-experience-the-technology-behind-conversational-search-in-e-commerce/), Adevinta Tech Blog (leboncoin), 2024 — JSON compilation, JSON mode, history limits, structured-diff evaluation, provider data constraints.
- [Why would I need an AI search assistant?](https://adevinta.com/techblog/why-would-i-need-an-ai-search-assistant/), Adevinta Tech Blog (leboncoin), 2024 — user research on assistant adoption.
- [OLX Magic: transforming e-commerce search experience with AI agents](https://home.mlops.community/public/videos/olx-magic-transforming-e-commerce-search-experience-with-ai-agents-nishi-and-beatriz-2024-11-20), MLOps Community, 2024 — agentic assistant challenges.
- [Building a conversational shopping assistant with multi-modal search and agent architecture](https://www.zenml.io/llmops-database/building-a-conversational-shopping-assistant-with-multi-modal-search-and-agent-architecture), ZenML LLMOps Database (secondary summary of an OLX talk), 2024 — latency comparison and architecture.
- [Rightmove H1 2026 results](https://plc.rightmove.co.uk/content/uploads/2026/07/2026.07.31-Rightmove-final-RNS-H12026-unsigned.pdf), Rightmove plc, 2026 — "Ask Rightmove" early engagement and lead figures.
- [Rightmove FY2025 results](https://plc.rightmove.co.uk/content/uploads/2026/02/Rightmove-RNS-27.02.26.pdf), Rightmove plc, 2026 — app submitted to the ChatGPT ecosystem.
- [Shipping the first MCP in HeyImmo at ImmoScout24](https://medium.com/scout24-engineering/shipping-the-first-mcp-in-heyimmo-at-immoscout24-a278214df005), Scout24 Engineering, 2026 — MCP server launched November 2025.
- [What we learned from launching ImmoScout24 app in ChatGPT](https://medium.com/scout24-engineering/what-we-learned-from-launching-immoscout24-app-in-chatgpt-efbed0f7375b), Scout24 Engineering, 2026 — property search app inside ChatGPT.
- [Recherche optimisée pour leboncoin grâce aux LLM](https://www.lemondeinformatique.fr/actualites/lire-recherche-optimisee-pour-leboncoin-grace-aux-llm-91697.html), Le Monde Informatique, 2023 — leboncoin's retriever and re-ranker (press report).
- [Zillow AI search adds commute time, affordability](https://www.housingwire.com/articles/zillow-artificial-intelligence-search/), HousingWire, 2024 — Zillow natural-language search criteria.
- [Academic Publications & Airbnb Tech: 2025 Year in Review](https://airbnb.tech/infrastructure/academic-publications-airbnb-tech-2025-year-in-review/), Airbnb Tech, 2025 — augmenting narrow searches with recommendations.

{id: query-understanding--standards-regulation-and-documentation}
### Standards, regulation and documentation

- [Synonym graph token filter](https://www.elastic.co/docs/reference/text-analysis/analysis-synonym-graph-tokenfilter), Elastic documentation, n.d. — search-time, multi-word and updateable synonyms.
- [Hyphenation decompounder token filter](https://www.elastic.co/docs/reference/text-analysis/analysis-hyp-decomp-tokenfilter), Elastic documentation, n.d. — decompounding for Germanic languages.
- [Common options: fuzziness](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html), Elastic documentation, n.d. — `AUTO` edit distances.
- [Reciprocal rank fusion](https://www.elastic.co/docs/reference/elasticsearch/rest-apis/reciprocal-rank-fusion), Elastic documentation, n.d. — RRF retriever and its rank constant.
- [Score ranker processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/score-ranker-processor/) and [Normalization processor](https://docs.opensearch.org/latest/search-plugins/search-pipelines/normalization-processor/), OpenSearch documentation, n.d. — hybrid fusion options and versions.

{id: query-understanding--research-and-practitioner-sources}
### Research and practitioner sources

- [Applying Embedding-Based Retrieval to Airbnb Search](https://arxiv.org/html/2601.06873v1), Abdool et al. (Airbnb), 2026 — IVF versus HNSW under filters; replay-based evaluation.

Veldmark is fictional; architectural recommendations and labeled inferences are the author's judgement.
