# Review log — Preface and Reference pages (19 Oct 2026)

Scope: introduction, where-listing-systems-go-wrong, meet-veldmark, part-9-intro, toolkit, glossary. Render check: meet-veldmark, part-9, where-listing-systems-go-wrong OK. introduction, toolkit and glossary flag only `XJ:` for `[[bibliography]]` (the page doesn't exist yet; accepted for now).

## introduction
- Checked the Part I–VII paragraphs against the written part intros: they agree.
- Rewrote the Part VIII paragraph from the PLAN version to match the written part-8 intro: consolidation in an order that protects liquidity, one owning team per journey, context and capability, and "the hard problems are problems of change, not of design".
- Part IX paragraph agrees with part-9-intro.
- Checked the argument against ch. 45: the thesis wording and the stage-to-metric-to-pattern map agree.
- Checked 214 digest e-mails, "twelve templates", eight countries, €1.31B and €140M: all agree.
- Spot-checked the Adevinta 2025 strategic report ("decentralised, standalone operating model") and found it verified.

## where-listing-systems-go-wrong
- Regenerated the pattern matrix from every chapter's FAILURE PATTERNS callout. ● now means "named in the opening callout" and nothing else. A ● that no longer appears in the callout became ○; existing ○ entries were kept.
- Rows changed: industry-evolution, transactions-and-payments, platform-consolidation, organizing-marketplace-engineering, modernization-and-migration, long-term-evolution, case-olx, case-ebay-classifieds, case-aviv, case-property-portals, case-automotive. Removed the "for chapters still in preparation / will be revised" wording.
- Checked the "Where this book helps" lines: none lists a chapter whose callout omits the pattern. Added recommendations (Ghost Inventory), long-term-evolution (Acquisition Archipelago, Platform Mandate, Vanity Liquidity), case-aviv (Platform Mandate) and case-automotive (Unwatched Model). Added a note that the matrix is the complete list.
- Kept the matrix's direct `.html` links on purpose. `[[…]]` would expand to full chapter titles and break the 16-column table, and the links resolve in-journal.
- Checked the Veldmark illustrations against the ledger: they agree.
- Spot-checked the Mercari figures (3B items, US$1M, 1.9 years) and found them verified.
- Changed timetoread from 40 to 45 min. The page is about 10.7k prose words, but it is a structured guide with no clear repetition, so I didn't trim it.
- Changed programme to program.

## meet-veldmark
- The 2009–2014 history said each country was "a configuration of Yardstick". I aligned it with the industry-evolution ledger line: BE and PT run their own copies of Yardstick, each with its own database and deployment, and PL came by acquisition and kept Elasticsearch. I fixed the Country Fork callout and the "layers" sentence to match.
- Named Ruhrblick's Pro 150 package (150 slots, €1,450 a month).
- All other figures agree with the ledger and the [editor] lines: eight countries, Safe Deal 11.6M / €1.02B / €75M, Golf 23 raw and 19 qualified leads, bike reserved at 14:02, sold 18:10, removed 18:11.
- Marked the spec's open question on the country count as resolved.
- Changed programme to program.

## part-9-intro
- Item 25: key point 1 now separates Adevinta's 2023 convergence plan, which was reversed, from AVIV's 2021 goal of "a European real estate marketplace", whose scope was never published. I also softened the failure-pattern line and the comparison-table row ("fully integrated platform" is the interviewer's phrase).
- Re-verified the AVIV quote and its date (Online Marketplaces, 23 Aug 2021).

## toolkit
- Item 24: rebuilt Tool 11 to match the written ch. 41:
  - the integration option is one of six (hold separate … divest);
  - stages 0–4 with gates;
  - a synergy ledger (lines with dated evidence and dependencies, dis-synergies, separation cost);
  - the 3% organic-traffic rule and "migrate to the target, not the sibling";
  - Hearthly.es figures: €18M case, €9.6M achieved, €11M one-off cost, hosting switched off end of 2029;
  - Keybridge federated under group controls, with €7M withdrawn and €1.9M added.
- Tightened two common mistakes to match.
- The bike is version 9 and reserved at 14:02, which is already correct.
- Spot-checked the Kleinanzeigen rebrand press release ("remain accessible for several more years") and found it verified.

## glossary
- Rechecked the contract-written rows against the chapters and corrected:
  - Portfolio model and Copy-paste market entry (industry-evolution);
  - Merchant of record, Hold and release / payout and Order state machine (the actual states) (transactions-and-payments);
  - Consolidation sequence, Integration options (six), Synergy case / synergy ledger and Brand migration (platform-consolidation);
  - Parallel run / shadow / canary, Migration stage gate (G0–G4), Relevance parity, URL migration and Feature parity trap (modernization-and-migration);
  - Stressor analysis, Stressor / residue / attractor (ch. 45's definition of attractor differs from the draft) and Marketplace fitness function (long-term-evolution).
- Added rows for Carve-out / TSA and for Dispute / chargeback, with index entries.
- Fixed the Veldmark Group row from "seven countries" to eight.
- Changed timetoread from 60 to 80 min. Changed programme to program.

## Open issues for others
- multi-country-platforms says Yardstick has about 2,600 "country branches", which suggests one shared codebase. industry-evolution and its ledger line say BE and PT run on separate copies. The two are compatible if the copies share branching code, but the owning chapters should say which it is.
- Once the bibliography page exists, rerun the render check for introduction, toolkit and glossary.
