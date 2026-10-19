---
status: accepted
revised: 2026-10-18
---

# Spec: Unreconciled: Fourteen Ways Finance Architecture Goes Wrong

## Intent

Give readers a shared vocabulary of fourteen named failure patterns that recur in enterprise finance estates before they enter Part I, so that every later chapter can point back to them in its FAILURE PATTERNS callout. Each pattern is explained by mechanism (incentives, organization, vendor dynamics), not by blame, and connected to the chapters whose designs prevent or repair it. The page closes by showing how the patterns reinforce each other, so readers look for the upstream cause before funding a downstream fix.

## Audience

Chief and enterprise architects, finance-systems and integration architects, and finance-transformation leaders. Also usable by controllers and internal-controls leads as a shared language with architects. Assumes architectural experience; defines finance terms (clearing and suspense accounts, master data, EUC, significant deficiency) on first use.

## Success criteria

- [ ] Uses the fourteen pattern names from the style guide exactly, in style-guide order, each as a `###` heading so callouts and anchors match.
- [ ] Opens with IN THIS SECTION and exactly three KEY POINTS; no failure-pattern callout.
- [ ] A summary table of all fourteen patterns and their warning signs precedes the pattern sections.
- [ ] Each pattern has an italic quote, what it looks like, why it happens, what it costs (control, cost, speed, audit risk), a Northmere vignette labeled fictional, a one- or two-sentence remedy direction, and "Where this book helps:" with 2–4 valid cross-links.
- [ ] Northmere figures match the scenario ledger (€14m suspense, 1.9%, €2.1m >90 days, 1,100 interfaces, ~240 flat files, ~70 EUCs, 2,300 custom objects, seven-month upgrades, 71 entities, 38,000 GL lines from 3 million subledger lines, the FY2026 significant deficiency).
- [ ] A closing section shows the reinforcing chains with a mermaid diagram (Doppelgänger Record → Spreadsheet Glue → The Suspense Swamp among them) and a diagnostic table of first indicators per pattern.
- [ ] Any regulatory definition is sourced (PCAOB AS 2201 for deficiency severity).
- [ ] Roughly 5,000–6,500 words of prose.

## Non-goals

- Detailed remedies: these belong to the linked chapters (for example payments-to-ledger design in [[payments-to-ledger]], clean core in [[sap-s4hana]], waivers in [[architecture-governance]]).
- Prevalence statistics or claims about real companies' failures.
- An introduction to Northmere (owned by [[meet-northmere]]) or a reading guide (owned by [[introduction]]).

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only for now. Pattern illustrations (one per pattern, as in OWNED) are a candidate for a later pass.

## Open questions

- Should each pattern get an explanatory illustration, as in the OWNED opening guide?
- Northmere vignettes add local details (Wayfare payout-engine balance gap, a dormant entity rename, pre-2025 batch-mapping retention, a Tablekin usage-revenue mapping miss, the reclassification bot, the early 1 January 2029 cut-over proposal, the RISE renewal timing). They are illustrative and not added to the ledger; promote any that later chapters reuse.

## Decision log

- **2026-10-18** — Modeled on OWNED's `where-investment-goes-wrong`, but with a fixed seven-part anatomy per pattern because the RECONCILED audience wants mechanism and cost explicitly, not only a warning question.
- **2026-10-18** — Kept the style guide's order rather than regrouping sections by family; families are named in one paragraph so headings and callout links stay stable.
- **2026-10-18** — Added a diagnostic table of first indicators so the patterns can be used in reviews with evidence; rejected numeric thresholds as unsupportable across enterprises.
- **2026-10-18** — Identified The Permanent Exception and The Borrowed Roadmap as root patterns, to motivate Part IV's governance and strategy focus.

## Sources

- **Internal**
  - `_research/style-guide.md` — pattern names and warning signs.
  - `_research/scenario-ledger.md` — Northmere facts.
  - `_research/productscape-digest.md` — challenges, misconceptions and stressors that inform the mechanisms.
  - [[meet-northmere]], [[introduction]] — neighboring preface pages.
- **External**
  - PCAOB, AS 2201 Appendix A — definitions of material weakness and significant deficiency.
  - Martin Fowler, *Strangler Fig* — incremental replacement behind the Big-Bang Bravado remedy.

## Changelog

- **2026-10-18** — Initial spec and article. Status `accepted`. *(author, AI-mediated session)*
- **2026-10-18** — Editorial review pass: added canonical outcomes (Wayfare €1.3M gap, $41M mapping error, Dec 2027 accounting-hub decision) to illustrations; added [[case-uber-payments]] and [[sap-s4hana]] to "Where this book helps"; removed a buzzword. *(AI-mediated session)*
- **2026-10-18** — Added 2 inline illustrations (article-illustrator); figures renumbered. *(AI-mediated session)*
- **2026-10-18** — Renamed the pattern Vendor Gravity to **The Borrowed Roadmap** at the author's request (book-wide, 61 mentions; style guide updated). *(AI-mediated session)*
- **2026-10-18** — Renamed the pattern Automation Without Accountability to **Nobody's Bot** at the author's request (book-wide; style guide updated). *(AI-mediated session)*
- **2026-10-18** — Renamed the pattern Tool Overlap Creep to **Capability Creep** at the author's request (book-wide; style guide updated). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern Suspense Gravity to **The Suspense Swamp** at the author's request (book-wide; style guide updated). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern The Many Masters to **The Doppelgänger Record** at the author's request (book-wide; style guide updated; plural verb agreements fixed). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern The Many Masters to **The Doppelgänger Record** at the author's request (book-wide; style guide updated; plural verb agreements fixed). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern Summarized Into Silence to **Lost in Aggregation** at the author's request (book-wide; style guide updated). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern The Brand Exception to **The Permanent Exception** at the author's request (book-wide; style guide updated; redundant "becomes permanent" phrasings reworded in ch. 10, 11, 16, 29). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern Audit Afterthought to **Audit Archaeology** at the author's request (book-wide; style guide updated; one sentence added to the section explaining the name). *(AI-mediated session)*
- **2026-10-19** — Renamed the pattern The One-ERP Dream to **The Swiss-Army ERP** at the author's request (book-wide; style guide updated; ch. 28 definition reworded; one sentence added to the section explaining the name). *(AI-mediated session)*
- **2026-10-19** — Title renamed to "Unreconciled: Fourteen Ways Finance Architecture Goes Wrong" at the author's request. *(AI-mediated session)*
