# Review log — Part III (SUPPLY)

Editorial pass, 19 Oct 2026. Scope: part-3-intro, 13-listing-ingestion, 14-normalization-and-enrichment, 15-entity-resolution, 16-publication-pipeline, 17-professional-seller-tooling. Render check: all six pages OK (no failed mermaid, no unresolved links, no XJ entries).

## Verified against primary sources (spot checks)

- Bundeskartellamt mobile.de/Carwow clearance: published 8 Oct 2026; the multi-homing and data-export statements are in the text (ch. 13, 17).
- P2B Regulation Art. 7 and Art. 9 quotes (ch. 17): checked against the Official Journal text through the EU Publications Office (CELEX 32019R1150). Correct. Applies since 12 July 2020; the Commission's repeal proposal of 19 Nov 2025 is confirmed on its policy page (updated 2 Jul 2026).
- DSA Art. 17 (statement of reasons; recital 55 counts demotion as a restriction of visibility), Art. 30 (trader traceability), Art. 31 (compliance by design), 17 Feb 2024: checked against the OJ text (CELEX 32022R2065).
- IETF Idempotency-Key draft: version 07, 15 Oct 2025, expired (ch. 13).
- Vinted 2024 Vespa post: 5-second visibility; 4.64 s p99 is "from Apache Flink to Vespa" / after upload, not a strict end-to-end figure. Reworded (ch. 16).
- Zillow FY2025 10-K: 173 million homes, 46 million user-updated records, Follow Up Boss features. Correct (ch. 15, 17).
- OLX causal-inference post (4 Aug 2026): +97.4% confirmed, but the matched estimates were *consistently higher* than the randomized test, not validated by it. Corrected (ch. 17).

## Changes per page

### part-3-intro
- Restored `[[part-1]]` and `[[part-5]]` in "How this part connects", where the text had plain "Part I" and "Part V".
- spec: replaced the literal `[[permalink]]` in a success criterion (it would have rendered as an unresolved link); added a Changelog line.

### 13-listing-ingestion
- Golf leads labeled as **23 raw leads**, with 19 after deduplication (consistency item 11).
- Expanded PKCE and DVLA on first use; licence → license (×2).
- timetoread 32 → 35 min.
- Changelog line in spec.

### 14-normalization-and-enrichment
- Expanded DMS, VIN and OCR on first use.
- "Together with the five confirmations above" → "the values the decoder confirmed above". The table lists four confirmations, and the total stays 31, which matches the ledger.
- licence → license (×2, plus spec).
- Changelog line in spec.

### 15-entity-resolution
- Barcelona ring: "the perceptual-hash index caught" was reworded to agree with fraud-prevention and its ledger line. Hash matches fired from day one but went to a separate queue from the price flags, and 11 photo-match items were closed as legitimate multi-agency duplicates before an analyst linked the cluster. Hearthly's local matching is meant here; the group PDQ index arrives only in Q1 2028.
- Expanded UPRN and GTIN.
- Changelog line in spec.

### 16-publication-pipeline
- The bike digest was "assembled from a cache" in the text; it now says "from a database replica snapshot", to match the ledger (listing-aggregate, event-driven-listings).
- "Template in the toolkit at the end of the book" now links `[[toolkit]]` (consistency item 7).
- programme → program; licences → licenses; TTL expanded.
- Vinted p99 claim worded as the source states it.
- timetoread 33 → 30 min.
- Changelog line in spec.

### 17-professional-seller-tooling
- Autohaus Ruhrblick moved to the canonical **Pro 150, €1,450/month, 150 slots** (consistency item 12). The downgrade proposal is now "a smaller package", and "90 slots produced 1,610 leads" became "150 slots". Links to `[[products-and-entitlements]]` added. The spec decision-log line is updated.
- Golf sale record is now "exported the next morning" after the 29 Apr sale. Ingestion and its ledger line say the sale was recorded in the DMS on 30 Apr.
- Agence Rhône Habitat: "whose 14 branches listed the Lyon apartment" → "a 14-branch network whose Lyon branch listed". Entity-resolution names one branch, Lyon Jean-Macé.
- OLX claim corrected to the source (see above).
- AVIV Ultimmo (2022, more than 3 years old) is now flagged as possibly changed.
- "Autotrader and OLX have shipped apps inside ChatGPT" now carries "As of 2026".
- Expanded DMS, SaaS, PKCE, DVLA and P2B on first use.
- Linked `[[case-adevinta]]`.
- Hand-off fixed: the last chapter of Part III now hands off to `[[part-4]]` (then search-architecture).
- catalogue → catalog in spec. Changelog line in spec.

## Open issues for the author / other parts

- The `[professional-seller-tooling]` ledger line still says "€1,240/month for 90 listing slots". The `[editor]` line supersedes it; the append-only rule stops me rewriting it.
- ch. 15 and ch. 17 use illustrative figures: the Lyon review numbers (31% fewer cards, precision 98.6%) and Ruhrblick's 1,610 quarterly leads. They are labeled illustrative but are not in the ledger. Add them if other chapters will reuse them.
- ch. 13's "Rightmove dropped XML in 2019" and the claim that Autotrader, OLX and Rightmove have ChatGPT apps (ch. 17) carry no inline source. Not re-verified in this pass.
- The Etsy figures in ch. 14 rest on a ZenML third-party summary. They are hedged in the text, but the original post was not verified.
