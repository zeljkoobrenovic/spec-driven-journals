# Review log — Part IV (editorial pass, 19 Oct 2026)

Scope: part-4-intro, 18-search-architecture, 19-query-understanding, 20-ranking, 21-recommendations, 22-map-search, 23-saved-searches-and-alerts. The build is clean, and the render check prints OK for all seven pages: no failed mermaid, no unresolved links, no XJ entries. Every spec.md has a changelog line for this pass.

## part-4-intro
- The Ranking policy v1 summary now matches the ledger: at most four paid listings in the first 20 positions, and top listings only above a relevance floor.
- The decision list now credits the brands as well as the search platform, because the carousel rebuild was Motorvane's.
- Format matches the other part intros. Hand-off to [[search-architecture]] is correct.

## 18-search-architecture
- timetoread 32 → 36. "programme" → "program". Expanded AGPL, SSPL and Elastic License v2.
- Corrected the Vinted 2023 facet cap: the source gives 100,000 documents per shard, not 100,000 matches.
- The Rightmove 2021 busiest-minute claim is now flagged as more than three years old, and its quote is fixed to match the source.
- The Zillow "200+ attributes" figure (2020) is hedged as "current figure not public".
- Spot-checks confirmed: Vinted 2024 Vespa post, Vinted 2023 facets post, Rightmove 2021, Elastic license post (2024).
- **Open (author):** the Zillow source is cited as a Medium RSS feed URL. Replace it with the post's own URL.

## 19-query-understanding
- Bike figures follow the editor line (items 21/23): about 380,000 bike listings across all categories, of which about 214,000 fall in the new city-bike leaf and about 38,000 are e-bikes. The text before the split now describes the six generic NL leaves.
- Model registration timing is fixed: the model is in the inventory in October 2027, and the 9 Nov 2027 registry decision made registration mandatory.
- Vinted wording now matches its source. Rightmove figures are dated as early findings to 30 Jun 2026. The Scout24 RSS citation is replaced with the two specific 2026 posts. The leboncoin 2023 evidence is flagged.
- Expanded HNSW and CLIP. Fixed colour/licence spellings. Added two [[ai-in-listing-systems]] links.
- Spot-checks confirmed: coches.net, leboncoin GPT-3.5, Airbnb embedding paper, Vinted dense retrieval, Rightmove H1 2026.
- **Open (ledger):** the [query-understanding] ledger line still says "about 214,000 live bike listings". The [editor] line overrides it, and the line was left unchanged because the ledger is append-only.

## 20-ranking
- timetoread 32 → 36.
- Checked the P2B Art. 5, Omnibus/UCPD (Annex I 11a, Art. 7(4a), Art. 2(m)) and DSA Arts. 17/26/27/38 quotes against the Official Journal texts from the EU Publications Office. The truncated Omnibus "ranking" definition is now quoted in full. Links now point to the OJ instead of legislation.gov.uk or an unofficial mirror (item 4 resolved for this page).
- Expanded VAS, LTR, P2B and UCPD. The P2B review sentence is aligned with the Commission page of 2 Jul 2026.
- Spot-checks confirmed: eBay 2020, Airbnb interleaving 2025, Etsy 2023, Airbnb map ranking 2025, OLX 2025 and 2026 posts.

## 21-recommendations
- The Essen Golf is now "23 raw leads, 19 after deduplication" (item 11), and the sale time is added (15:10, 29 Apr).
- DSA Arts. 27/38 checked against the OJ text. Corrected an overstatement: Art. 27 does not apply "regardless of size", because micro and small enterprises are exempt. The citation now points to the OJ.
- The Zillow RSS link is replaced with the 24 Feb 2021 post. FINN.no 2018 and Adevinta 2022 are flagged as possibly superseded.
- Expanded ALS, ANN, kNN, NDCG, GBDT and VIN. The Vinted latency baseline is dated 2023.
- Spot-checks confirmed: Vinted 2023, OLX 2023, Airbnb KDD 2018, Zillow 2021.
- **Open (other parts):** any page saying DSA Art. 27 applies to all platforms needs the small-enterprise exemption, especially recommender passages in Parts V and VII.

## 22-map-search
- timetoread 31 → 36. "licence" → "license" (proper names kept).
- Removed "schools" from the Zillow claim, because the HousingWire 2024 source does not support it.
- Hearthly agency precision now follows [location-and-geo]: P3, P4 or P5, with the coarsest choice applying to clustered properties. Valuo now trains on DVF transactions only, with medians per H3 res-8 cell. The H3 res-7 size is now given as an edge length. Linked [[ml-platform]].
- The Rightmove 2025 Elastic case study is flagged as describing a 2014 decision. Mapbox limits are marked "as of 2026". Expanded GTFS and DPE. Removed writer-facing wording.
- Spot-checks confirmed: Mapbox Isochrone limits, TravelTime and Rightmove licensing, Airbnb map share, Elastic geotile precision.

## 23-saved-searches-and-alerts
- timetoread 30 → 35.
- The hand-off now goes to [[part-5]] as the last chapter of the part, with [[trust-and-safety-architecture]] named.
- Ledger-backed figures are no longer labeled "illustrative": the baseline table, the Golf's ~640 saved searches and the Barcelona ring's ~41,000 alerts.
- The "6.5 min at worst" claim is corrected, because the targets are p95, not worst case.
- The Tradeyard cutover is aligned with ch. 43's Yardstick exit waves: comparison mode from Q4 2027, then sending market by market with search, PT first in Q2 2028, and the cron job off with BE/NL in Q4 2028. Added a [[modernization-and-migration]] link.
- The leboncoin RSS link is replaced with the 3 Jun 2026 post. Expanded SPF, DKIM, DMARC, SLO and LLM. The ePrivacy citation now reads "as amended in 2009".
- Spot-checks confirmed: Gmail bulk-sender rules (2024), FCM quotas, Homegate percolator post (2024), leboncoin 2026, ePrivacy Art. 13 (official text).
