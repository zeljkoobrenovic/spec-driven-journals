---
status: accepted
revised: 2026-09-23
---

# Spec: Toys R Us: Positive Operating Earnings, Too Little Cash

## Intent

Use the documented fiscal 2016 measures (positive operating earnings, a net loss, almost no operating cash flow) and the management-reported supplier cash shock to show why a technology transition needed funding, without claiming the proposed work was sufficient to restore competitiveness. Distinguish a transferable funding-dependency question from a causal claim about venture-backed or strategically owned companies.

## Audience

Product and engineering leaders inside companies working under investors, including leaders who inherit an ownership arrangement. Assume no specialist finance background; explain necessary terms before use. Investor-side readers are secondary.

## Success criteria

- Add one whole-post overview visual to the TL;DR after its opening paragraph, generated with the Nano Banana article illustrator. Keep the summary prose concise (about 300–650 words; the band was widened from 500 on 23 September 2026 so the TL;DR can carry its own plain-language definitions of the three central measures, including the full earnings-to-loss bridge with interest income, working capital as stock plus customer debts less supplier bills, subsidiaries, and the composition of the bankruptcy financing), with bold emphasis and citations; provide alt text and a concise numbered caption.
- Provide a distinctive article header logo and a simple navigation icon with unique asset paths. Keep both consistent with the journal’s visual style.
- Include two explanatory article figures with accurate short labels, alt text and numbered captions. Use restrained bold emphasis for key claims; preserve the words, citations and historical data. The comic modality is a set of comic pages — each image one page of three stacked strips with the dialogue, labels and reported figures lettered in the artwork with their periods and scopes — generated from the `comic-page` blocks in `comics.md`, with consistent fictional characters, a caption and a transcript per page.
- Make the company leader’s decision, authority and funding assumptions explicit. Distinguish the stated ownership arrangement from a claim about every investor.
- Keep historical findings within their source scope and label new comparative scenarios as fictional.
- Introduce necessary terms in ordinary language before using them in explanations, examples, tables, or diagrams; keep opening key points readable without prior study.
- Move from a concrete question through explanation and example to a practical conclusion; connect the conclusion to the next chapter in the configured reading order.
- Make summaries and comic storyboards understandable on their own; preserve source limits and label fictional scenarios, including changes in example assumptions. Where a short format glosses operating cash flow, name its scope: cash received and paid in day-to-day trading, interest included here, with new borrowing and purchases of long-lived assets counted separately.
- Define the three central measures (operating earnings, net loss, operating cash flow) in ordinary language before the financial table, explain why accounting income and cash differ, and print the earnings-to-loss reconciliation (including interest income) beside the table, visually separate from the cash measures. Keep EBITDA and adjusted EBITDA secondary and explained, showing the company's own EBITDA calculation from its actual starting point (the attributable net loss) rather than a simplified one that gives a different figure. Explain that sales are recorded as revenue rather than profit and that stock can be paid for before or after it is sold, depending on supplier terms, so the definitions connect to the supplier shock. Describe operating earnings as the reported result before interest and income tax, including other operating income and expenses, and note beside the table that the fiscal 2016 figure included a one-time gain on a brand sale, so the $460 million is not read as profit from ordinary retail trading alone.
- Bridge the September 2017 filing to the March 2018 liquidation plan: court-authorized financing during bankruptcy (a combined package of several facilities including the Canadian business, with borrowing ceilings subject to lenders' conditions, part of it used to repay existing loans, and repayment priorities set by the court orders and loan terms, not fresh free cash), authorized payments, continued operation, then the failure to find a buyer or agree a restructuring. Gloss the financing vocabulary (term loan, notes, security, repayment order) in ordinary words at first use. Keep a shorter version in the TL;DR, with one main idea per paragraph in both: the TL;DR separates the attempted reorganization, the later US liquidation and the supplier consequence into distinct paragraphs. The comic's consequence panel carries a two-sentence version of the same bridge (filing, court-permitted borrowing with limits and continued trading, then the March 2018 US liquidation plan after no buyer or agreed restructuring emerged) so the supplier shock is not shown closing the stores directly.
- Explain ownership and sale vocabulary in ordinary words where it first carries the explanation: shareholders as owners of a company's shares, the buyers as companies associated with the named investment firms, the $6.6 billion share transaction as the purchase of all the company's shares, net sales as sales after returns and discounts, and buyouts as purchases of a controlling ownership stake.
- Name every profit measure with its scope and period; the financial table carries both the consolidated net loss and the net loss attributable to Toys “R” Us, Inc., and the debt-service and technology-program figures are labelled by period and scope rather than netted.
- Present the supplier feedback loop once, as management-reported links, and preview it in the opening.
- Explain the title question and its implications for a concrete company decision.
- Distinguish sourced observations, the manuscript's analysis, and explicitly fictional examples.
- Include a meaningful trade-off or counterargument and identify the evidence that would change the judgment.
- Link related chapters and cite substantive external factual claims close to the text.
- Keep the TL;DR and the comic page scripts consistent with the full article; inspect every generated page against its script.

## Non-goals

Universal prescriptions, invented evidence, promises of investment performance, or disclosure of confidential inputs. The chapter is not a legal or tax opinion.

## Modalities

- Full Article: index.md, the substantive argument.
- TL;DR: summary.md, the practical implications in concise prose.
- Comic: comics.md, seven illustrated pages of three strips each, with alt text, visible captions and per-strip transcripts rendered from the page blocks that are also the artwork scripts; the fictional team reads the documents and never reenacts the history.

## Open questions

Evidence gaps and chapter-specific next research are tracked in the separate editorial backlog. The book uses the author’s accepted working title; evidence and role questions remain open.

## Decision log

- 2026-09-13: The author requested Owned and substantive comparative treatment of leadership under investors; this supersedes the previous private-equity-first framing.
- 2026-09-12: Use an explanatory essay rather than the repository's ADR template. Preserve per-post folders and stable permalinks. User explicitly requested varied chapter structures.

## Sources

The supplied book brief establishes scope. Public citations appear in the article and bibliography. Private provenance is recorded separately in _research/input-reading.md and is excluded from the site configuration.

## Changelog

- 2026-09-23 (comic pages): The six single-scene panels replaced by seven comic pages of three strips each, so the three measures in ordinary words and the 2005 purchase, the fiscal 2016 online growth against falling net sales and the court declaration's subscription gap and $90.4 million programme, the earnings calculation from $460 million to the $29 million and $36 million losses beside the cash side (operating cash flow about zero, $252 million of capital expenditure, $566 million as a balance), the declaration's figures with their scopes and management's four-step supplier chain, the filing-to-liquidation bridge with the financing ceilings, the employee and supplier consequences including Hasbro's $60.4 million with the $49 million inside it, and the four practices are drawn into the artwork rather than carried by captions. Every short-format gloss of operating cash flow keeps its scope. Page images live under `assets/images/36-toys-r-us/`; the previous panel comic is archived under `_research/comic-pages-pilot/`. No figure, date or claim changed; permalink unchanged.
- 2026-09-23: In-depth review round 6 (TRU-012): one measure or calculation step per sentence in the short formats. The TL;DR ends its earnings bridge at the $29 million group loss, then gives the $7 million belonging to outside owners of partly owned subsidiaries and the $36 million attributable loss in their own sentences (prose about 657 words, within the band). Comic panel 3 states operating earnings, net loss and operating cash flow in one sentence each, keeping the fiscal period, the interest treatment and the borrowing and long-lived-asset exclusions; caption, prompt and panel text changed together, artwork unchanged. Permalink and id unchanged.
- 2026-09-23: In-depth review round 2 (TRU-002): the comic must stand alone on its bankruptcy vocabulary; panel 5 explains the filing as entering a court process for dealing with debts, the sought agreement as one to reorganize debts and business, and liquidation as selling assets and closing the US stores. No artwork regenerated.
- 2026-09-23: In-depth review round 4 (TRU-002, TRU-003, TRU-012, TRU-015): comic glosses of operating cash flow now carry the operating scope (day-to-day trading, interest included, borrowing and long-lived-asset purchases outside); comic panel 5 opens with the filing-to-liquidation bridge before the shutdown consequence; the post-table reconciliation paragraph is split into loss scopes, composition of operating earnings with the brand-sale gain, and the conclusion; shareholders, the buying companies, the share transaction, net sales and buyouts glossed in ordinary words. No artwork carries the changed words. Permalink and id unchanged.

- 2026-09-23: In-depth review round 3 (TRU-012 to TRU-014): operating earnings redefined as the reported result before interest and tax including other operating income and expenses, with the release's build-up (4,108 − 3,480 − 317 + 149 = 460) and the one-time $45 million FAO Schwarz brand-sale gain noted beside the earnings table; term loan, notes, security and repayment order glossed in the bankruptcy-financing passage; TL;DR bankruptcy paragraph split into reorganization, US liquidation and supplier consequence. No artwork affected. Permalink and id unchanged.
- 2026-09-23: In-depth review round 2 (TRU-001, TRU-002, TRU-005, TRU-008 to TRU-012): the company's EBITDA calculation is shown from the attributable net loss (−36 + 34 + 455 + 317 = 770) with the $777 million operating-earnings alternative explained; the accounting-versus-cash explanation is split into a timing paragraph (sales as revenue, stock paid before or after sale depending on supplier terms, an illustrative 60-days-versus-on-delivery example) and a funding paragraph; the bankruptcy passage is split into filing, financing and payment authority, and continued operation, and the financing is described as a combined four-facility package including Canada, partly used to repay existing loans, with priorities set by the court orders (new source S118, the financing note); private-equity firms defined more broadly; opening highlights and preview trimmed of repeated thesis statements; TL;DR earnings and cash explanations separated, interest income added to its bridge, working capital and subsidiaries defined, financing package described; comic panel 3 caption drops the unexplained ownership qualifier and panel 4 says supplier and stock; Figure 2 regenerated so the central arrow reads CAN LEAD TO. Summary band widened to 650 words. Permalink and id unchanged.
- 2026-09-23: In-depth review round 1 (TRU-001 to TRU-008): plain-English definitions of the central measures added before the table, with the loss reconciliation printed beside it; the opening no longer implies a fixed payment schedule set at purchase; a bankruptcy-financing bridge (filing, court-authorized financing of up to $3,125 million, authorized payments, continued operation) added before the liquidation plan; the closing checklist distinguishes principal repayments from interest already inside operating cash flow; summary rewritten as three explained statements (prose about 570 words, so the 500-word band was widened to 600); comic introduces Larkspur and glosses earnings versus cash; TL;DR overview and Figure 2 regenerated with distinct plain labels and a stated direction of effect. Permalink and id unchanged.
- 2026-09-15: Editorial review follow-up: comic panel 3 dialogue changed to “Positive operating earnings; almost no operating cash flow.” and flagged for regeneration (image still shows the original bubble); the proposed technology program is described as multi-year/four-year throughout; debt service tied to management's September 2017 account; year-end cash balance ($566m) and total liquidity ($1.5bn) added as a balance distinct from operating cash flow; repeated transfer cautions compressed. Permalink and id unchanged.
- 2026-09-14: Retitle to “Toys R Us: Positive Operating Earnings, Too Little Cash” and revise per the editorial review: corrected causal opening, labelled net-loss lines, period-labelled debt and technology figures, single supplier feedback loop, leverage ratio removed, cash-flow question separated, application sections combined; permalink and id unchanged.
- 2026-09-14: Retitle the post from “Toys R Us: Technology Plans Under Cash Pressure” to “Toys R Us: Profitable on Paper, Out of Cash in Practice”. Permalink and id unchanged; body unchanged.
- 2026-09-13: Add the requested single Nano Banana overview visual to the TL;DR modality.
- 2026-09-13: Extend the illustrated edition to post logos, navigation icons and, where applicable, the existing six-panel comics.
- 2026-09-13: Define the requested article-illustration and bold-emphasis pass before implementing the illustrated edition.
- 2026-09-13: Reconcile the revised article and applicable reading formats with the Owned contract; specification accepted as matching the draft manuscript.
- 2026-09-13: Revise the contract for Owned before adapting the article and its reading formats.
- 2026-09-13: Apply the agreed company-leader perspective, private-equity focus with wider applications, and revised part structure.
- 2026-09-13: Revise for readers starting from scratch; define terms before use, explain reasoning steps, and connect the configured chapter sequence.
- 2026-09-12: Add the author-requested ai-notes KEY POINTS opening; preserve article-specific conclusions and caveats.
- 2026-09-12: Research pass two adds selected first-day court declaration evidence on technology constraints, debt and vendor terms, plus supplier financial evidence; preserves the unresolved complete financing-history and full 10-K access limits.
- 2026-09-12: Initial spec, status draft; supports a substantial first manuscript and later evidence-led revision.
