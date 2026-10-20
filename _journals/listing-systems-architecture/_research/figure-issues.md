# Known Figure Errors

The 150 mermaid diagrams were replaced on 2026-10-20 by Gemini illustrations that redraw each rendered diagram. Each image was checked against its source and retried up to three times. These images still differ from their source; the author chose to ship the best attempt. The original mermaid sources are in `mermaid-figures.json`, so any figure can be regenerated or restored.

| Post | Figure | Remaining error |
| --- | --- | --- |
| 05-bounded-contexts | 2 | kept attempt 4: 'decisions' edge runs from Listing catalog toward Trust and safety with no clear arrowhead at Listing catalog (should be Trust and safety → Listing catalog) |
| 06-vertical-requirements | 2 | kept attempt 1: Property entity and valuation 'enricher' goes to Ranking instead of Ingestion; 'signal' label on Job normalization line, no Vehicle→Ranking signal arrow; invented Taxonomy→Ingestion arrow; missing Taxonomy→Search infrastructure and Trust rules→Event backbone |
| 06-vertical-requirements | 3 | kept attempt 1: Property match and Job title normalizer arrows merge into one line into Enrich with no 'enricher' labels |
| 07-listing-aggregate | 4 | kept attempt 1: prints 'START' and 'END' beside the dots; 'seller resumes' arrow points from Paused to Rejected instead of Active |
| 12-sellers-and-accounts | 5 | kept attempt 3: state names joined as 'UnderReview' and 'PendingVerification'; 'enforcement or unpaid contract' (Active to Suspended) branches off the 'limits lifted' line, so it reads as if it starts at Restricted |
| 14-normalization-and-enrichment | 2 | kept attempt 1: the 'ApplyEnrichment with provenance' line into 'Listing service' has no arrowhead (direction not shown) |
| 15-entity-resolution | 3 | kept attempt 4: prints the words 'START' and 'END' beside the start and end dots; structure otherwise correct |
| 17-professional-seller-tooling | 1 | kept attempt 1: invented title 'The professional's lead lifecycle' (structure otherwise correct) |
| 17-professional-seller-tooling | 2 | kept attempt 1: 'Partner software: DMS, CRM' to 'Pro API gateway' arrow has arrowheads at both ends |
| 17-professional-seller-tooling | 5 | kept attempt 4: second 'same listings' label missing on arrow to 'Competing portal B APIs'; dashed 'no access' line ends at 'Portal performance report per agency' instead of 'Agency CRM records' |
| 18-search-architecture | 6 | kept attempt 1: line from 'Shared indexer framework' to 'Amazon OpenSearch Service' merges with the 'Elasticsearch adapter' line at a junction, so it can read as 'Elasticsearch adapter' also pointing to Amazon OpenSearch |
| 19-query-understanding | 1 | kept attempt 3: extra arrow from 'Taxonomy and attribute dictionary, versioned' to 'Synonyms and expansions' |
| 21-recommendations | 3 | kept attempt 4: dashed arrow 'Listing event stream' to 'Embedding nearest neighbors' missing; label 'inserts, updates, removals' printed twice (also on the arrow to Filter) |
| 23-saved-searches-and-alerts | 4 | kept attempt 3: 'sold, removed, reserved, expired' drawn from 'Alert matcher' instead of 'Listing event stream' to 'Retraction handler'; invented arrow 'In-app inbox' to 'Engagement events' |
| 24-trust-and-safety-architecture | 2 | kept attempt 1: 'Case management and review' drawn inside the 'Detection' panel (should be outside both panels) |
| 24-trust-and-safety-architecture | 7 | kept attempt 2: Tradeyard 'Policy overlays NL, BE, PL, PT' arrow ends at the panel edge instead of 'Policy registry with overlays'; 'Policy overlays FR, ES' arrow ends at 'Decision service' instead of the registry; 'Payment-link and counterfeit detectors' scores arrow ends at 'Policy registry with overlays' instead of 'Decision service' |
| 26-identity-and-verification | 2 | kept attempt 1: 'Fraud and T&S platform' drawn inside the 'Veldmark ID' panel; 'Hearthly' → 'Authentication service' (OIDC login) arrow missing; invented arrow 'Profile service' → 'Hearthly'; 'Account recovery' → 'Authentication service' and 'Authentication service' → 'Profile service' drawn without arrowheads |
| 26-identity-and-verification | 3 | kept attempt 1 (structure correct): invented title/caption sentence printed at top; words START and END printed beside the dots |
| 28-messaging-and-leads | 2 | kept attempt 2: extra arrow 'Message safety gate' → 'Lead service' carrying the 'BookingConfirmed' label (the 'Booking service' → 'Lead service' arrow is unlabeled); two parallel lines from 'Call tracking and masked numbers' to 'Lead service' |
| 28-messaging-and-leads | 4 | kept attempt 2: 'Merged' points to 'Acknowledged' instead of the end dot (Merged → END missing) |
| 29-transactions-and-payments | 2 | kept attempt 1: 'availability check' (Listing context → Order context) and 'delivered or returned' (Shipping → Order context) drawn as lines without arrowheads |
| 29-transactions-and-payments | 3 | kept attempt 3: words START and END printed; extra arrow 'Chargeback' → end dot; 'Completed' → end dot missing |
| 30-monetization-models | 2 | kept attempt 4: 'Billing and invoicing' drawn twice (in core panel and beside Delivery metering, joined by a line); arrow goes 'Billing and invoicing' → 'ROI reporting to professionals' instead of → 'Finance ledger' |
| 31-products-and-entitlements | 2 | kept attempt 2: invented title 'Reference Architecture: Commercial Core Flow'; invented label 'delivery evidence flows back into the ledger'; that arrow points 'Entitlement ledger' → 'Metering and delivery evidence' instead of the reverse |
| 31-products-and-entitlements | 4 | kept attempt 1 (structure correct): words START and END printed beside the dots |
| 32-advertising-platforms | 1 | kept attempt 3: extra arrow 'Ad policy service' to 'Consent management platform' carrying 'ad load, exclusions, labels' (the arrow to 'Ad slots' has no label); 'floors, caps, labels' printed twice; arrows both ways between 'Search results' and 'Sponsored listing auction'; extra arrow 'Campaign and budget service' to 'Ad server'; 'impressions, viewability' arrow from 'Ad slots' merged with the 'creative' line |
| 35-web-and-seo-architecture | 2 | kept attempt 1: two arrows 'Search engine crawlers' → 'Edge and CDN: routing, caching, bot rules' instead of one |
| 35-web-and-seo-architecture | 3 | kept attempt 4: structure and arrows correct, but invented sub-captions inside four states ('in sitemaps and linked', 'answer with noindex and stay linked for users', 'answer 301 to their successor, recorded in the redirect registry', 'answer 404 or 410') |
| 38-ml-platform | 2 | kept attempt 2: no arrow 'Offline feature history' to 'Training pipelines'; extra arrow 'Batch feature pipelines' to 'Training pipelines'; feedback arrow into 'Label pipelines' starts at 'Monitoring' instead of 'Prediction log' |
| 39-multi-country-platforms | 3 | kept attempt 2: extra dashed arrow 'Packages, prices and sales' → 'Release rings and flags'; missing 'Packages, prices and sales' → 'Product catalog and entitlements'; 'Market policies and legal texts' arrow ends on the Global components frame, not on 'Trust and safety pipeline' |
| 42-organizing-marketplace-engineering | 2 | kept attempt 2: dashed 'group security standards only' arrow ends on 'Trust and safety pipeline' instead of 'Developer platform' |
| 43-modernization-and-migration | 2 | kept attempt 1: prints the words 'START' and 'END' beside the start and end dots (otherwise correct) |
| 43-modernization-and-migration | 3 | kept attempt 4: 'CDC' arrow dashed instead of solid; 'Yardstick PHP monolith'–'Yardstick MySQL' line has an arrowhead; MySQL box icon is a dolphin resembling the MySQL logo |
| 45-long-term-evolution | 1 | missing arrow 'Contact and transaction' -> 'Trust' labeled 'outcomes and labels' (kept original image; retries were worse) |
| 46-case-adevinta | 3 | Kafka brand logo with extra 'kafka' wordmark beside the 'Kafka' label (kept attempt 2) |
| 49-case-aviv | 4 | invented title 'Seller funnel in AVIV's French moves (2019–2023)'; missing label 'classified as likely sellers' on 'Buyer contacts on portals' -> 'Seller detection' (kept original image) |
| introduction | 2 | kept attempt 4: Discovery box truncated to 'Discovery...' (missing 'search, ranking, alerts') |
| meet-veldmark | 2 | kept attempt 1: brand logos (AWS, Google Cloud, Elastic, Snowflake); arrow into 'Elasticsearch 8 on Elastic Cloud' starts at Tradeyard instead of Motorvane; Hearthly to OpenSearch line routed through Motorvane and Tradeyard so it reads as extra links; third 'ad slots' label (into Hearthly) missing |
| where-listing-systems-go-wrong | 2 | kept attempt 1: Portfolio arrow runs behind 'The Duplicate Echo' and Moderation arrow runs behind 'Measurement and control' and 'Paid-Rank Drift', so both read as wrong links |
| where-listing-systems-go-wrong | 4 | kept attempt 4: label 'new facts go into free keys' missing on Category Straitjacket to Attribute Junkyard arrow; Index-as-Database to Ghost Inventory line runs through The Category Straitjacket box |
