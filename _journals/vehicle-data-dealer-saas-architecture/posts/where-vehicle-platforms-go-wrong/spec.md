---
status: accepted
revised: 2026-10-22
---

# Spec: Wrong Car, Wrong Price: Fifteen Ways Vehicle Platforms Go Wrong

## Intent

Give the book its shared vocabulary of failure. The page names the fifteen failure patterns that recur in vehicle data services and dealer software, so every chapter can open with a "failure patterns this chapter addresses" callout that links here, and so design reviews can say "this is Borrowed Uptime" and move straight to the mechanism and the owner. For each pattern the reader gets a short fictional quote, warning signs, the mechanism, the cost (with dated public evidence where it exists), a labeled Axleby illustration consistent with the ledger, which half it hits hardest and why, and the chapters that address it. After reading, an architect can recognize the patterns in their own platform, ask for the first number that reveals each, place each on the Identify → Insight chain and trace a symptom to its upstream pattern.

Productscape bricks covered: none as a topic; the page cuts across all bricks by naming how they fail.

## Audience

Chief and enterprise architects, principal engineers and engineering leaders of vehicle-data companies, dealer-software vendors, portals, lessors and dealer groups. They have lived through some of these incidents; they need names, mechanisms and a map to the chapters.

## Success criteria

- [x] Uses the fifteen exact names, warning signs and "hits hardest" values from the style guide, in its order, in one summary table with a first indicator per pattern.
- [x] Every pattern has a quote, warning signs, mechanism, cost, an Axleby illustration (or an explicit note that the ledger has none), a "Hits hardest" line with the reason, and a "Where this book helps" list of valid permalinks derived from PLAN contracts.
- [x] Real-world evidence is dated and sourced (EP odometer resolution 2018, 49 CFR 565, GDPR Art. 19, DPPA § 2721(c), Authenticom v. CDK 2017, CDK 2024 via AutoNation 8-Ks and CyberScoop, Cox fact sheet 2018, OWASP API Top 10 2023, Zillow 2021); the one inference about a real company (Bridge ID) is labeled.
- [x] Includes a "patterns by journey stage" table and a mermaid diagram of the chains between patterns.
- [x] Hands off to [[meet-axleby]].
- [x] Length 5,000–6,500 words before Sources (about 6,300).

## Non-goals

- Remedies in depth — each "Where this book helps" line points to the chapter that designs the fix.
- The book's argument and routing — [[introduction]]; Axleby's landscape and cast — [[meet-axleby]].
- A chapter-by-pattern matrix built from the chapters' callouts — deferred until the chapters exist (see Open questions).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- Once all chapters are written, add a chapter-by-pattern matrix built mechanically from their "FAILURE PATTERNS THIS CHAPTER ADDRESSES" callouts, as BOOKED does, and reconcile the "Where this book helps" lists with it.
- The Zillow figure rests on a press report (The New York Times, 2021); replace with Zillow's Q3 2021 shareholder letter if a fetchable copy is found.
- Spec Guesswork, Provenance Amnesia, The Zombie Listing, Feed Roulette, The Leaky Lead, The Unmetered Call and Customization Creep have no dated public example; add one if the research briefs surface it.

## Decision log

- **2026-10-22** — Mirrored BOOKED's `where-stay-platforms-go-wrong` per-pattern shape, but replaced its chapter matrix with a "patterns by journey stage" table, because the chapters do not exist yet and the stage view connects the patterns to the book's Identify → Insight chain.
- **2026-10-22** — Grouped the patterns into four families (vehicle facts, dealer workflow, commercial, platform) while keeping the style guide's order, and named four chains, with The Acquisition Archipelago as the root of the portfolio chain.
- **2026-10-22** — Left quotes unattributed (no role), as the brief asked, and kept each pattern near 350 words to fit the 6,500-word cap.
- **2026-10-22** — Web search quota was exhausted during research; external evidence was fetched directly from known primary URLs or taken from the VERIFIED entries of `brief-case-cox-cdk.md`.

## Sources

- **Internal**
  - `_research/style-guide.md` — pattern names, warning signs and "hits hardest" values.
  - `_research/scenario-ledger.md` — Axleby incidents and numbers.
  - `PLAN.md` — chapter contracts, from which the "Where this book helps" lists are derived.
  - `_research/brief-case-cox-cdk.md` — Authenticom, CDK 2024 and Cox evidence.
  - BOOKED's `where-stay-platforms-go-wrong` page — structure.
- **External**
  - European Parliament resolution of 31 May 2018 on odometer manipulation; 49 CFR Part 565; GDPR (Regulation (EU) 2016/679); 18 U.S.C. § 2721; OWASP API Security Top 10 2023.
  - Authenticom v. CDK Global (7th Cir., 2017); AutoNation Forms 8-K (2024); CyberScoop (2024); Cox Automotive fact sheet (2018) and Bridge ID page; The New York Times (2021).

## Changelog

- **2026-10-22** — Initial spec and article. *(AI-mediated session)*
- **2026-10-22** — Editorial review pass: rechecked every pattern's chapter mapping against the chapters' failure-pattern callouts (added owners, removed weak ones, fixed the gateway-metering contradiction), updated Customization Creep and Sticky Error examples from the ledger, preface callout label. *(AI-mediated session)*
- **2026-10-22** — Visual layer: converted 1 mermaid diagram to illustrations and added 1 conceptual figure (article-illustrator). *(AI-mediated session)*
