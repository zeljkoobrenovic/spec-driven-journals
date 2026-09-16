# Revision log — OWNED editorial revision of 14 September 2026

This log records how each recommendation in `REVIEW.md` (the collection review) and the per-post `REVIEW.md` files was handled. The review files are unchanged and remain the baseline. "Implemented" means the recommendation was applied as written; "Adapted" means the intent was met a different way; "Declined" means it was not applied, with the reason; "Unresolved" means work or verification that could not be completed in this pass.

## Collection-level decisions

**Structure (collection review §"Reading order, combinations and worthwhile additions")**

- Split the handover material out of "The Roadmap Did Not Slip, the Financing Did" → **Implemented.** New Part V chapter `31-handover-of-obligations` ("Hand Over the Obligations, Not Just the Company", permalink `handover-of-obligations`). Chapter 18 keeps its permalink and title and is now a focused delayed-financing chapter with a completed, dated funding decision.
- Move "Fix the Decision Problem Before Adding People" directly after "Can the Software and the Team Deliver What Was Promised?" → **Implemented** in `config.yaml`; Part III introduction groups the nine chapters into three moves; handoffs rewritten (09→13→27→10).
- Optional fund-economics reference for waterfalls and fund ratios → **Implemented.** New reference page `fund-economics` ("Fund Economics: Fees, Distributions and Performance Reports") receives the €160 waterfall from chapter 2 and DPI/RVPI/TVPI material from chapter 4; both chapters link to it as optional depth.
- Combine "Find the Help" and "Useful Engagement" for a shorter edition → **Declined.** Kept separate with sharpened jobs (sourcing decision vs filled charter and scope change); repeated provider/charter advice removed instead.
- Keep Hilton/Skype paired; keep Visma and TeamSystem separate; keep acquisition and separation in one chapter with visible substructure → **Implemented.**
- Add a documented venture funding delay / minority case and a corporate ownership case → **Declined for this pass.** No documented case with adequate evidence was available without inventing facts; the evidence-scope disclosure is preserved in the guide, Part VI introduction and bibliography. Recorded as an open item.
- Companion evidence essay for healthcare/research methods → **Declined.** The finale keeps the material findings and shortens the methodological exposition instead.
- Three short reading routes in the guide → **Implemented** (plus the previous situation routes, consolidated into one table).
- Complete finding-to-funded-plan-to-review example → **Implemented** as a shared fictional chain (finding D-3, initiative ONB-1) through chapters 22–25 (diligence, first hundred days, financing slipped, handover) and the toolkit; figures and assumptions are stated in each chapter and labelled fictional.

**Titles (collection review §3)** — permalinks and ids unchanged: "Match the Funding to the Work" (raise-what-you-need); "Find the Cash Behind Your Technology Budget" (obligations-before-budget); "Toys R Us: Positive Operating Earnings, Too Little Cash" (toys-r-us); "TeamSystem: Each New Owner Inherits Progress and Unfinished Work" (teamsystem). Visma's title decision is recorded in its entry.

**Terminology (collection review §"Voice, readability and terminology")** — a terminology sheet (investor/firm/fund/company; shareholder vs accountable leader; financial sponsor vs investor-side sponsor vs company sponsor; funding states from expression of interest to cash received; named profit measures; financial vs causal contribution; end-to-end work lead time vs DORA change lead time; continuing service as a legitimate outcome; thesis and durable value) governed every chapter revision and the glossary.

**Categorical ownership contrasts (collection review §1)** — the "companies without investors do X; under investors Y" pattern was removed from every opening, summary and comic introduction listed in the review and replaced by the conditional pattern ("this arrangement changes the conditions of the decision; establish the actual funding, authority and deadline before committing", then the specific condition).

**Companion formats** — summaries were rewritten to carry the revised argument and checked against a 300–500-word prose convention (front matter absent; figure lines and `[S..]` citation tokens excluded). Comic text (introductions, captions, dialogue, JSON prompt/alt/caption fields) was edited; no panel images could be regenerated in this pass (no image-generation key available). Panels whose new text the existing image cannot fully carry are flagged `needs_regeneration` in their JSON and listed per post below.

**Not changed** — `REVIEW.md` files; permalinks; ids; image files; `_research/` provenance (except a new `bibliography-revision-history.md` receiving the editorial chronology moved out of the public bibliography).

## Coordinator-level pages

### config.yaml, README.md, STRUCTURE.md, index.md (workspace)

- Part III reordered; `31-handover-of-obligations` added to Part V; `fund-economics` added to Reference Material; Part V and Reference section descriptions updated. README, STRUCTURE (decision record entry dated 2026-09-14) and the workspace book index synchronized to 30 main chapters / 41 pages and current permalinks (the workspace index previously used stale permalinks).

### reading-guide — OWNED — Reading Guide (`reading-guide`)

**Files changed:** index.md, spec.md
**Implemented:**
- Align audience and accessibility promise → primary reader stated in the second paragraph; "no accounting or technical background is required" replaced with "assumes no finance training and explains the financial terms needed…; does assume an interest in fairly detailed questions about software delivery, architecture, organization and evidence".
- One immediate route before the full tour → "Start With the Decision in Front of You" now precedes the four-question frame and carries the three review routes plus the earlier situation routes in one table; the ownership-event table was folded into the frame section.
- Correct the Part IV heading and format-length promise → heading now matches the configured title; formats described accurately (30 chapters with article and TL;DR, 29 with a comic).
- Keep contents as secondary lookup → contents retained at the end, introduced as a lookup aid; numbering reflects the new Part III order and the new chapter.
**Adapted:**
- "Short statement of the first decision to bring to the book" → added as the closing sentence of the routes section rather than at the end of the explanatory portion.
**Unresolved:** none.
**Verification:** all `[[…]]` targets resolve at build; the Larkspur paragraph now discloses the one deliberate cross-chapter continuity (the D-3 chain).

### part-1 … part-6 introductions

**Files changed:** index.md, spec.md for each.
- Part I: contractual framing sentence replaces the deterministic opening; one repetition removed; refresher note for experienced readers; link to the optional fund-economics reference. (High/medium/low all implemented.)
- Part II: bridge sentence "Knowing where the cash sits does not yet tell you who can authorize the work" added as the opening highlight; repeated promise trimmed; source-of-approval-right sentence added. (All implemented.)
- Part III: learning path grouped into three moves; organization chapter now sits after team delivery and the introduction says so; one concise alternative-scenario paragraph kept and referenced by chapters that shortened theirs. (All implemented.)
- Part IV: category recap shortened to one paragraph; three distinct chapter jobs stated; continuing-service allowance kept; "accountable company leader" wording; title identical to configuration. (All implemented.)
- Part V: four destinations after the split; nonlinearity stated once; amount of change qualified; the evidence trail promised is the D-3 chain the chapters now demonstrate. (All implemented.)
- Part VI: concrete opening contrast; case-purpose map (case, window, decision); finale introduced as synthesis; "Documented Ownership Cases" part title → **Declined** (stylistic option; the existing title is kept because the configuration, guide and README use it).


## Coordinator follow-ups after the chapter agents finished

- Bibliography: added **S62** (Hg 2017 Visma buyout announcement, now cited from the Visma chapter and summary in `[S62: …]` form) and **S63** (OECD AI-system definition memorandum, cited from the glossary). Every entry's "Used in" line was recomputed from the current chapter citations after all moves (S02/S24/S30 now cite from the handover chapter, S05 from fund-economics, S32 only from Visma, P01 only from the adviser chapter).
- Glossary: added an "Audited financial statements" entry, which chapter 1 now links to for audit and reporting detail.
- Chapter 1 comic panel 6: the existing image shows investor-label cards and a company-budget folder, so the alt text and prompt were aligned to the image; the caption (three money destinations) still fits. No regeneration needed.
- Chapter 25 (handover) KEY POINTS block formatting repaired; toolkit reading time normalized to the "N min read" form.
- Chapter 18's adaptation of the brief's "mid-November" figure to "late November" (the stated numbers give €390,000 at 30 November) is accepted; no other chapter cites the earlier phrasing.
- Chapter 17's closing handoff was checked: it now points to the delayed-financing decision and names the handover chapter, so no further change was needed.


## Per-post records (reading order)


## 00-customers-lenders-investors — Customers, Lenders and Investors: What Each Expects in Return (`customers-lenders-investors`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Complete the opening example (high) → New "Larkspur Needs €100,000" section names the company and cast; new "The Same €100,000, Three Ways" table shows customer prepayment vs bank loan vs new shares with one obligation per route that changes the delivery promise; decision paragraph gives chosen option (prepayment), rejected alternatives (loan, share issue) with reasons, funding, scarce capacity (8 engineer-weeks of a four-person team), authority (board approves multi-year customer contracts; Ines signs) and the evidence that would reopen it (fewer than three signatures by 15 January, or estimate above 12 engineer-weeks). Every figure labelled fictional. Summary and comic panels 1 and 6 carry the same decision.
- Remove the "amount is the less important half" ranking (high) → Replaced in article opening, KEY POINTS, summary opening and comic introduction with the review's suggested "a budget tells you how much; the funding terms tell you when, which approvals and what obligations" formulation, plus "affordability depends on both".
- Shorten "Public and Private Ownership" (medium) → Section cut to three paragraphs; IPO paragraph and audit-frequency/reporting-category detail removed and replaced by a link to [[glossary]]; secondary-market cash distinction and one reporting sentence with S55 kept; S54 kept in the shares section.
- Investor labels as orientation only (medium) → Five paragraphs collapsed into one four-row table (label / typical arrangement / what to check) titled "Investor Labels Are Orientation, Not Terms", citations S58/S59/S60/S01 kept in one line, consequences handed to [[raise-what-you-need]].
- Curate the ending (low) → Questions cut from five to four; reading list cut from five to four with "Start here" (Brealey) and "Go deeper" (Myers) labels; capital-structure note moved from the shares section to a short note after the funding comparison, as the review suggested.
- Verify Myers and Robb–Robinson annotations (evidence) → Both fetched 2026-09-14. Myers 2001 (AEA page): abstract states "there is no universal theory of the debt-equity choice" and reviews tradeoff, pecking-order and free-cash-flow theories as conditional; annotation narrowed accordingly. Robb–Robinson (NBER w16272 page): Kauffman Firm Survey, US firms in their first year; finding is heavy reliance on external debt such as bank financing (often on the founder's personal balance sheet) and less on friends-and-family funding; annotation narrowed to that population and finding, dropping "mostly on bank debt rather than equity".
**Adapted:**
- "Move audit frequency and the fuller IPO discussion to the glossary" → Removed from this chapter and linked to [[glossary]]; the glossary already defines IPO but has no audit entry, and I may not edit the glossary. Coordinator note below.
- Reading list → Dropped the OECD scoreboard entry (its annotation was the weakest link to the chapter's argument) rather than keeping five entries; the remaining four are within source scope.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Glossary: add a short "audited financial statements" entry (and, optionally, a note on public-reporting categories) so the chapter's [[glossary]] link lands on the promised detail.
- Figures 1 and 2 unchanged and still valid. No comic panel needs regeneration; panels 1 and 6 captions/prompts/alt rewritten within what the existing images show.
- The Larkspur €100,000 figures (6% loan ≈ €3,000/month over 36 months; 111 new shares ≈ 10% of 1,111) do not reconcile with other chapters' Larkspur scenarios, per the brief's instruction that each example states its own assumptions.
**Verification:** arithmetic rechecked (€100,000 at 6% over 36 months ≈ €3,042/month; 111/1,111 = 9.99%; 10/1,000 = 1%); all [[…]] targets resolve to existing permalinks; comic JSON parses, six panels, status unchanged; summary word count 499; article prose 1,599 words → timetoread 8 min; build not run.


## 01-announcement-is-not-a-budget — An Investment Announcement Is Not a Budget (`announcement-is-not-a-budget`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Correct the founder-owned/earnings-to-budget opening across formats (high) → Article second paragraph, summary opening and comic introduction now use the review's suggested formulation ("An announcement describes a transaction. To turn it into a hiring plan, establish how much cash reaches the business, when it arrives and who can authorize its use. These questions matter under every ownership arrangement") followed by the brief's conditional pattern ("a transaction changes the conditions of the answer…"). The "in a company with no outside investor…" sentence is gone from all three formats.
- Make one completed funding map the payoff (high) → New section "Alex's Hire: The Completed Funding-and-Authority Record": seven-row table (proposed commitment, paying entity, cash state, approver, conditions, runway effect, decision date) with a column naming the information source (Alex / finance: subscription agreement, bank statement, closing statement, cash plan / board minutes / legal: shareholders' agreement consent schedule). Decision paragraph gives the chosen option (three hires authorized by Ines on 12 October within the board-approved plan), alternatives rejected (five hires — above plan, needs investor director consent; the "innovation budget" — exists in no agreement), funding (€7.6m net received vs €8m announced), scarce capacity (recruiting time, team absorption), authority (CEO within plan; board/investor director for changes) and evidence that would reopen it. One paragraph shows how the record changes under the €40m purchase of existing shares. Summary and comic panel 6 carry the same record.
- Move the detailed waterfall to an optional fund-economics note (medium) → "How Fees and Profit Sharing Work" replaced by "Fees and Profit Sharing Shape Incentives": management fee, carry and waterfall named in one paragraph, with the incentive point and links to [[different-bets]], [[three-different-returns]] and [[fund-economics]]; the €160 table, preferred return, catch-up and clawback definitions moved verbatim to fund-economics; the SEC conflicts paragraph (S01) kept here. Summary's waterfall arithmetic replaced by the same brief statement and links. Metrick–Yasuda annotation adjusted to point at the fund-economics reference.
- Bring the entity diagram forward and label the sale route (medium) → Mermaid map moved from the end of the chapter to directly after the entity table; buyer arrow relabelled "Payment for the portfolio company's shares"; new paragraph states that in this diagram the buyer purchases the portfolio company's shares from the holding vehicle (payment lands in the holding vehicle, repays lenders, remainder to the fund) and that in other transactions the buyer purchases the holding vehicle from the fund; either way it is payment for existing shares, not new company money. Summary carries the same "ask which" sentence.
- Qualify the GP/manager sentence (clarity) → Now: "In the common partnership form, the general partner… holds the management responsibilities and powers under the fund arrangements. The investment firm often acts as the fund's manager under a separate agreement, and 'GP' is used informally for the firm; which body actually approves an investment is whatever those agreements say." Matches the glossary's GP entry. Summary aligned.
- Reduce the reflection list (low) → Six questions cut to four; questions 1 and 4 (cash commitments and entity identity) combined into one that points at the completed record; the "which body, exercising which right" question kept.
- Terminology → "sponsor" in the entity table now "financial sponsor"; Technology Principal sentence reworded to "investor's technology adviser… this book's example of such a role is the Technology Principal, Morgan"; "portfolio leader" → "company leader".
**Adapted:**
- Review's proposed structure placed the fees section last as "optional" → Kept it before "Owning a Company Does Not Mean Running It" so the record section is the chapter's payoff and the handoff to [[valuation-is-an-estimate]] follows it; the fees section is now short enough not to interrupt.
- Figure 1 (four organizations) now sits at the end of the entity section, after the mermaid map and the two consequences, to avoid two adjacent diagrams of the same structure. Image unchanged and still valid.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Comic panel 6: the previous `alt` text described a different scene (ownership cards) from the `prompt` (three money paths); alt is now aligned to the prompt, which is what generated the image. If the rendered image actually shows ownership cards, the panel needs regeneration; otherwise no regeneration needed. No other panel changed scene.
- Figure 2 caption unchanged; image still valid.
- The record's dates and amounts (€8m gross, €0.4m costs, €7.6m net, €250,000 consent threshold, four planned hires) are fictional and separate from the D-3/first-hundred-days chain, per the brief.
**Verification:** €160 arithmetic preserved in fund-economics (100 + 12 + 48 = 160); record arithmetic checked (8.0 − 0.4 = 7.6); all [[…]] targets resolve, including fund-economics; comic JSON parses, six panels, status unchanged; summary word count 500; article prose 2,133 words → timetoread 11 min; build not run.


## 26-valuation-is-an-estimate — A Valuation Is an Estimate, Not a Fact (`valuation-is-an-estimate`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: two explicitly named learning stages → article now has `## Stage 1: Read the Business’s Numbers` (revenue/earnings/cash, EBITDA, income-statement table) ending in `### Checkpoint: What Can You Now Ask About the €60 Million?` (three questions on the opening number), then `## Stage 2: Interpret a Valuation` (EV/equity bridge applied to the €60m, three methods, funding round, one assumption to challenge). The €60m question is revisited at the checkpoint, the bridge, the multiples and the closing section.
- High: correct the Gornall–Strebulaev annotation → now “a study of 135 US unicorns whose modeled fair values, derived from each share class’s contractual terms, average about 50% below the reported post-money valuations; … can overstate the estimated value of the whole company”. No longer presented as evidence about private companies generally.
- Medium: soften deterministic ownership claims → “assumptions decide which … results the company must deliver” replaced in the article intro, KEY POINTS, summary opening and comic introduction (and panel 5 caption) with “can become growth, margin and cost targets that leaders must examine / test whether the operating plan can support”.
- Medium: one engineering-facing conclusion → new `### One Assumption to Challenge: Cost to Serve Falls as Sales Grow` (which change produces the reduction, when it becomes usable, who funds the transition), linking [[growth-into-design]] and [[roadmap-to-revenue]]; mirrored in the summary’s closing paragraph. Uses the shared 80-hour onboarding figure; the doubling/one-third assumption is labelled a separate fictional assumption.
- Low: prioritize further reading → SEC primer annotated “Start here if Stage 1 was new to you”; Damodaran survey and Koller marked “Optional depth”; the Damodaran annotation no longer claims evidence on which method is more precise.
- Move the double-deduction warning nearer the methods table → now a paragraph directly under the three-methods table, also noting which methods yield EV versus equity-type answers.
- Label DCF treatment as an introduction → methods section says multiples get the fullest treatment and DCF a single-payment illustration.
- Cut repeated “a valuation is not cash” reminders → one remains at the bridge (with the [[announcement-is-not-a-budget]] link) plus the funding-round calculation; removed from KEY POINTS, the corporate-buyer paragraph and the conclusion.
- “What to Carry Forward” recap → shortened to two paragraphs; handoff now poses the next question ([[three-different-returns]]).
- Questions to Consider trimmed 6 → 4.
- Comic: intro rewritten to the two-stage framing; panel 1 and 3 captions name the stages; panel 2 adds the adjusted-figure question; panel 5 carries the “can become a target” qualification. Captions, dialogue, JSON caption/alt/prompt agree; JSON validated; six panels, images unchanged.
- Spec: Intent rewritten for the two-stage structure, three success criteria added, `revised:` 2026-09-14, Changelog line added, status accepted.
**Adapted:**
- Review’s suggested one-sentence rewrite of the unicorn annotation → used a slightly longer sentence to name both the population (135 US unicorns) and the modeled-fair-value basis, plus the “about 50%” figure now scoped to that sample.
**Declined:**
- Split into two chapters (financial-statements primer + valuation) → the review offered this only if audience testing shows beginners still struggle; the two named stages plus checkpoint implement the first-line recommendation, and no new chapter was authorized by the brief.
**Unresolved / needs separate action:**
- The Tuck-hosted PDF link cited in the review (centers.tuck.dartmouth.edu/…/SSRN-id2955455.pdf) now redirects to a generic Tuck centers page; the article cites the NBER page (unchanged URL), which was fetched and confirms the population and findings. Bibliography agent may want to note the broken Tuck mirror.
- Figures 1 and 2 kept; captions unchanged; images still valid.
- Summary figure kept; caption unchanged.
- Cross-chapter: new section names other agents may link: “Checkpoint: What Can You Now Ask About the €60 Million?” and “One Assumption to Challenge: Cost to Serve Falls as Sales Grow”. `timetoread` recomputed to 16 min (3,247 prose words at 200 wpm, excluding tables, figures and citations).
**Verification:** arithmetic rechecked (€20m→€4m→€3m→€2m→€1.5m; 20% margin; €60m−€20m=€40m; 3× and 15× on €60m; 12×€4m=€48m; 1.1/1.10; €8m+€2m=€10m, 20%); Gornall–Strebulaev verified via WebFetch of https://www.nber.org/papers/w23895 (135 US unicorns, post-money valuations average 50% above fair value, fair values computed from share-class terms in legal filings, 65 of 135 lose unicorn status); links checked ([[obligations-before-budget]], [[announcement-is-not-a-budget]], [[acquisition-adds-work-first]], [[roadmap-to-revenue]], [[growth-into-design]], [[three-different-returns]] all exist); summary word count 493; comic JSON valid; build not run.


## 02-three-different-returns — Same Company, Same Performance, Three Different Returns (`three-different-returns`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: lead toward the title’s comparison sooner → new `## One Operating Result, Three Investor Outcomes` directly after the opening previews the 7×/10×/12× table (fund receives €65m/€110m/€140m; 1.6×/2.75×/3.5×); the measures and the base buyout are merged into `## The Base Buyout: Measures and Arithmetic`; the full table with annual returns returns in `## Vary the Multiple, the Timing and the Direction` (which also holds the timing comparison and the downside leverage scenario). No second parallel example added.
- High: align shorter formats with the title → summary now carries the fixed-performance three-multiple comparison and the interaction decomposition instead of the DPI/RVPI/TVPI paragraph; comic panels 2, 3 and 4 now show the same operating result at 10×, 12× and 7× with the assumptions stated in the intro and panel 1.
- Medium: relocate fund-reporting detail → `## Reading a Fund Performance Report` (DPI/RVPI/TVPI table, gross/net, subscription line, S05 ILPA citation) deleted from this chapter; the destination page is being built from the git HEAD version. Left in “What Technology Can and Cannot Claim Credit For”: two sentences distinguishing cash already returned from estimates of unsold holdings, plus “[[fund-economics]] (optional depth)”. Also linked from the summary.
- Medium: retain the interaction term, connect it to one claim → new `## Why the Bridge Can’t Say “Engineering Created €30 Million”` keeps the €50m/€20m/€10m table and adds a paragraph asking how such a claim would be justified: the bridge separates earnings from price, not engineering from the other things that moved EBITDA.
- Low: fix the two shortcuts → “in this fully realized example, MOIC is proceeds divided by total capital invested”; “The operating assumptions are unchanged … Varying only the exit multiple produces markedly different investment results”; “market mood” removed everywhere, with a sentence that a multiple can reflect company prospects and buyer-specific expectations as well as market conditions. “IRR tells you how fast” now reads “how fast, given those payment dates”.
- Dilution and corporate benefits demoted to `## Two Extensions: Dilution and a Corporate Owner` (brief extensions, per the proposed structure); the “remaining fund-reporting concepts” sentence folded into the corporate-owner paragraph.
- Handoff rewritten to answer the reader’s next question (how much borrowing and which investor fit the work) → [[raise-what-you-need]]; link text will pick up that chapter’s new title at build time.
- Questions to Consider trimmed 6 → 4 (fund-report question dropped with the moved section; Q3 now asks for evidence gathered along the way).
- Excerpt updated to the title’s promise; `timetoread` recomputed to 14 min (2,721 prose words at 200 wpm).
- Spec: Intent rewritten (fixed-performance comparison leads; fund reporting lives in [[fund-economics]]), three success criteria added, Changelog line added, status accepted, `revised:` already 2026-09-14.
**Adapted:**
- Review: “use three comic panels to show the same operating result and three investor outcomes” → panels 2 (10×, Sam moving earnings/valuation/debt blocks) and 3 (12×, Alex proud beside a rising valuation) were re-captioned so the existing images can carry them; panel 4 (previously two clocks for MOIC/IRR timing) could not plausibly carry the 7× outcome, so its prompt/alt/caption were rewritten and it is flagged `needs_regeneration: true`. The timing point moved into the article text and the comic dropped it; panel 6 now also carries the “sale price cannot say how much engineering contributed” conclusion.
- Figure numbering: the sources-of-return figure now appears before the dilution figure, so captions were renumbered (sources-of-investor-return = Figure 1, dilution-and-fresh-funding = Figure 2); images unchanged and still valid.
- To Probe Further: Kaplan–Sensoy and Schillinger entries kept (their content is accurate and verified previously) but re-annotated as “Optional depth” pointing at [[fund-economics]] and at the chapter’s timing point, since the chapter no longer discusses DPI/RVPI/TVPI or subscription lines. The fund-economics agent may prefer to adopt them there.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Comic panel 4 needs regeneration (7× outcome scene); panels 2 and 3 re-captioned only.
- Bibliography: S05 (ILPA performance guidance) is no longer cited from this chapter; it should now be cited from `fund-economics`. S03 (Kaplan & Strömberg) still cited here.
- Cross-chapter: chapters 01 and 06 were asked by the review to link the fund-reporting reference; that is the [[fund-economics]] page, not this chapter. New section names other agents may link: “One Operating Result, Three Investor Outcomes”, “Why the Bridge Can’t Say ‘Engineering Created €30 Million’”.
**Verification:** arithmetic rechecked (7×15=105−40=65, 1.625× → 10.2%; 10×: 110/40=2.75 → 22.4%; 12×: 180−40=140, 3.5× → 28.5%; 2× in 3 yrs ≈ 26.0%, in 7 yrs ≈ 10.4%; downside 80−60=20 vs 40; €80m = 50+20+10; 200/1,000=20%, 200/1,250=16%, 16%×€20m=€3.2m=1.6×); links checked ([[valuation-is-an-estimate]], [[obligations-before-budget]], [[roadmap-to-revenue]], [[raise-what-you-need]] exist; [[fund-economics]] is a brief-authorized target not yet created); summary word count 496; comic JSON valid, six panels, images unchanged; no leftover DPI/RVPI/TVPI/subscription-line/S05 text in index.md; build not run.


## 03-raise-what-you-need — Match the Funding to the Work (`raise-what-you-need`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: decide which question the chapter owns / retitle → retitled to "Match the Funding to the Work" (title, excerpt, spec heading and Intent); permalink and id unchanged.
- High: add an actual sizing decision (base work, transition, uncertainty allowance, decision runway, consequences of raising more or less) → new section "Size the Work Before You Name the Investor" with a fictional €610,000 need table (€180,000 build, €30,000 maintenance, €90,000 transition, €150,000 interim specialist, €70,000 allowance, €90,000 runway), reusing the pilot figures from `roadmap-to-revenue` / `cannot-fund-everything`; the counterarguments (reserve for uncertainty; a later round may be unavailable) are stated as the case for the larger raise; raising only the €180,000 build is shown as the under-raise consequence.
- High: give the inherited-arrangement reader an action → "Who is authorized" paragraph: Alex and Priya bring the revised scope, the €610,000 requirement with components, the alternative (two implementation specialists, ~€300,000 a year recurring) and the review date; Ines and Sam negotiate and bring terms to the board; the shareholders' agreement governs shareholder consent. Key point 3, the summary and comic panel 6 carry the same split.
- Medium: develop one Larkspur case with two feasible arrangements and a choice → Arrangement A (€2.5m growth equity with approval rights and an 18-month second-country expectation) vs Arrangement B (€750,000 three-year term loan at 8%, staged work); B chosen under stated assumptions (€350,000 operating cash, customer evidence for the setup constraint, no second-country evidence); example ends with chosen option, alternatives rejected, funding, scarce capacity, who is authorized and the evidence that would reverse it (signed second-country customers; cohort effort still above 70 hours).
- Medium: move detailed control and partnership questions to Part II → compressed to one paragraph "Control and Partnership Are Separate Questions" with links to [[decide-who-decides]] and [[investor-under-pressure]]; the Gompers/Kaplan/Mukharlyamov survey (S04) kept in one sentence with its stated-practice qualification.
- Low: replace category determinism → "The terms of the funding and the investor's expectations affect the pace, the tolerated losses and the time available for the plan" now governs the intro, key points, summary opening and comic introduction; "the type of capital sets the pace" removed from all formats.
- Compress the category comparison → recap table reduced to two columns with links to [[customers-lenders-investors]] and the [[reading-guide]]; the four Larkspur category sketches removed.
- Keep "a business that decides against outside ownership hasn't failed a test" → kept, in "Revisit the Fit When the Plan Changes".
- Keep the €4m vs €1m interest comparison but integrate it → now closes the chosen case ("the scale of the financing matters more than its label"; the €3m difference is five times the onboarding need) with the link to [[obligations-before-budget]].
- Drop the readiness checklist → removed; "any of three answers can be correct" folded into the revisit section.
- Prevalence wording → "rarely choose the investor" / "usually inherit" replaced with "may not choose the investor" / "leaders who inherit the arrangement" per the terminology sheet.
- Questions to Consider trimmed to four; handoff to [[obligations-before-budget]] now states the reader's next question (how much of earnings is cash the work can use).
**Adapted:**
- Review suggested the €4m/€1m comparison be tied to the chosen case → the chosen case is at €610,000 scale, so the comparison is framed as "suppose Larkspur were instead carrying acquisition borrowing" and sized against the onboarding need rather than folded into the loan arithmetic; the chapter still states that the examples do not reconcile with the annual bridge.
- Comic panels 2 and 6 → captions, dialogue-adjacent JSON `caption`/`alt`/`prompt` rewritten to carry the sizing and the two-arrangement choice; dialogue lines unchanged because the existing images can support the new captions.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Figure 1 caption changed to "The same onboarding work needs a different plan under different funding, authority and expected outcomes"; the image (one proposal under four arrangements) still supports the text, no regeneration needed. Figure 2 unchanged.
- No comic panels flagged for regeneration; existing images carry the revised captions.
- The bibliography/S04 entry is still cited from this chapter; the To Probe Further annotation for Bhidé reworded to "one legitimate outcome of a sized comparison rather than a rule" (within source scope; no URLs added or fetched).
- Cross-chapter fact for other agents: this chapter now contains a distinct fictional funding scenario (€610,000 need; €2.5m growth equity vs €750,000 term loan; €350,000 annual operating cash). It reuses the €180,000 / €30,000 / 12 engineer-week pilot and 80→62/50-hour effort figures but is otherwise its own scenario, as the reading guide allows.
**Verification:** arithmetic rechecked (610 = 180+30+90+150+70+90; 25% of 270 = 67.5 ≈ 70; year-two payment 250+60 = 310 vs 350+135 = 485; €2.5m − €0.61m ≈ €1.9m surplus; 80→62 h frees 18 h × 100 × €75 = €135,000, 80→50 h frees €225,000); all 8 `[[…]]` targets resolve to existing permalinks; comics JSON valid with captions/alt in sync across the six panels; summary word count 477 (figure line excluded); timetoread recomputed 2,178 prose words → 11 min; build not run.


## 04-obligations-before-budget — Find the Cash Behind Your Technology Budget (`obligations-before-budget`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: rewrite the title and opening → retitled "Find the Cash Behind Your Technology Budget"; opening now "Positive EBITDA does not establish cash available for a new initiative. Reconcile it with investment, taxes, financing payments, working-capital needs and the cash already on hand, then check the dates and restrictions"; the universal payment hierarchy ("paid before a migration or a new team is funded") and the "without outside investors the gap is mostly an accounting matter" contrast removed from the article, summary and comic introduction; replaced with the conditional pattern (the arrangement changes the conditions of the reconciliation; borrowing adds contractual dates, a shareholders' agreement may add distributions or thresholds, a parent may set an allocation). Permalink and id unchanged.
- High: distinguish obligations from choices at the first bridge → new table beside the bridge listing payroll (already inside EBITDA), cash interest and principal (contractual; only the lender can change them, by waiver, amendment or refinancing), cash tax (statutory), capital expenditure (a management choice, partly contracted), working capital (growth and payment terms) and owner distributions (absent from the model; a proposal unless an agreement requires them). The closing qualification ("planning calculation, not a universal payment priority; engineering salaries are already in operating costs") moved to sit directly under the bridge.
- Medium: finish the €1m initiative example → new section "Three Priced Options for the €1 Million Initiative": minimum continuity (€150,000, 3 engineer-weeks, mid-year review, Ines and Sam within the delegated budget), staged pilot (€200,000, 12 engineer-weeks, month-six cohort review, Ines within the delegated limit with the board deciding the second stage), full request (€1,000,000, 36 engineer-weeks, board meeting before the budget is fixed; lender under the covenant or shareholders for new equity). Option 2 chosen under stated added assumptions (€0.3m opening cash above the reserve, year-end covenant test); alternatives rejected, funding, scarce capacity, authority (Ines; Sam confirms timing; board informed; Priya accountable) and the evidence that would change it are stated; links to [[cannot-fund-everything]].
- Medium: tighten the setback section → reduced to the Bernstein/Lerner/Mezzanotti conditional-support finding (S10), the committed-vs-hopeful distinction, the Toys R Us earnings-vs-cash sentence (S35), and links to [[the-financing-slipped]] and [[help-that-changes-capability]]; the capability-loss and reversible-savings paragraph removed.
- Low: clarify the amortization sentence → now "the cash outflow is the same. Capitalization changes when costs enter profit; later amortization is excluded from EBITDA, so the EBITDA difference does not reverse in a later period, although other profit measures carry the amortization charge."
- Kept intact: the €10m→€0.5m bridge, the 12→8.6-month runway table and the €3.6m/€5.4m (€1.8m) floating-rate example.
- Commitment states → "An investor's intention to join another round" now described as an expression of interest, not a contractual commitment with understood conditions and not cash received (terminology sheet).
- Closing section renamed "Which Plan Can the Company Actually Carry?"; handoff to [[part-2]] / [[decide-who-decides]] now states the reader's next question (where the authority named in each option comes from); Questions to Consider trimmed to four.
**Adapted:**
- Review's proposed structure ("complete the staged-investment decision, then teach runway and financing downside") → the options section is placed directly after the bridge and before the runway scenario, as proposed; the accounting comparison stays as a bounded subsection, now opened with the "more effective, accounting changed, or both" question so the definitions arrive after the reader sees why they are needed.
- Comic panels 2 and 6 → caption/alt/prompt rewritten (obligations vs choices; three priced options and the funded pilot); dialogue lines unchanged; existing images can carry the new captions.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Article length grew from about 2,500 to 3,000 prose words (timetoread 10 → 15 min) because the completed options decision was added while only the setback section was cut; a later pass could shorten the debt-downside and adjusted-earnings paragraphs if the coordinator wants the chapter nearer its previous length.
- Figures 1 and 2 captions unchanged; both still support the text. No comic panels need regeneration.
- The options example adds fictional assumptions (€0.3m opening cash above reserve; year-end covenant test; 36 engineer-weeks for the full program) that belong to this chapter's annual model only; they do not reconcile with the Larkspur chains in chapters 16–18 or the €610,000 scenario in `raise-what-you-need`, per the brief.
- The To Probe Further Paul Graham annotation reworded from "the second Larkspur scenario" to "this chapter's runway scenario" (section order changed); no entries added or removed, no URLs fetched.
**Verification:** arithmetic rechecked (10 − 4 − 1 − 2 − 1 = 2; 2 − 1.5 = 0.5; 0.5 + 0.3 = 0.8; 0.8 − 0.2 = 0.6; 3m/250k = 12; 3m/350k ≈ 8.6; 60m × 6% = 3.6m, × 9% = 5.4m, difference 1.8m); all 10 `[[…]]` targets resolve to existing permalinks; comics JSON valid with captions/alt in sync across the six panels; summary word count 496 (figure line excluded); timetoread recomputed 3,004 prose words → 15 min; build not run.


## 05-decide-who-decides — Decide Who Decides, Before You Disagree (`decide-who-decides`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Organize around the filled decision record → the opening is now Morgan’s cloud remark to Alex; “Establish What Has Changed” resolves it against Ines’s €500,000 delegation (Morgan holds no approval right); the filled €1m onboarding record (with an added “evidence that would change the recommendation” row) now precedes the generic role table, which follows as “read as roles”.
- Missed-deadline branch → new section “Make a Conditional Commitment Explicit, and Plan the Missed Deadline”: if hiring approval has not arrived by May, Alex brings the January option back to Ines, Ines escalates to the board chair or confirms January, the team is told in writing, customer commitments tied to October require an explicit decision; ends with the full decision-record fields (chosen, rejected, funding, capacity, authorized, evidence).
- Move support boundaries to Part IV → “Support Can Become a Shadow Hierarchy” and the coaching-confidentiality paragraph cut; replaced by the short “Parallel Instructions Need One Accountable Leader” linking [[investors-adviser]] and [[useful-engagement]]. Confidentiality question removed from Questions to Consider.
- Reporting focused on the decision request → three-sentence fictional board update (80→62 hours, ~40% data quality, €40,000 + 4 engineer-weeks from the reserve, decision requested this meeting) linking [[toolkit]]; generic reporting-framework text cut.
- Consistent responsibility language → “Who owns each result” → “Who is accountable for each result”; “Executives own the integration plan” → “are accountable for”; comic panel 4 “finding its owner” → “the person authorized to act”; founder-vs-investor framing removed from summary and comic intro.
- Founder-owned before/after paragraph → replaced with the conditional pattern (“Informal influence and unclear delegation exist under any ownership… An investment changes the conditions of the decision… Establish the actual authority, funding and deadline before committing”).
- Reduce Principal column prominence → column renamed “Investor adviser’s possible contribution”, table cut to four rows and moved after the filled record; “Technology Principal” retained once as the book’s example role name; adviser referred to as “the investor’s technology adviser” elsewhere.
- Questions to Consider trimmed to four.
**Adapted:**
- Board-update figures → reused the shared Larkspur day-100 numbers from the brief (80→62 hours, ~40% data quality, €40,000 / 4 engineer-weeks from the reserve) so this chapter agrees with 17 and the toolkit, even though 05 is not formally part of the chain.
- Review’s note that “the board must resolve the choice” is an aspiration → one clause added: which body resolves shareholder disagreement, and what happens in a deadlock, depends on the actual agreements.
**Declined:**
- none.
**Unresolved / needs separate action:**
- Figures 1 and 2 unchanged and still valid. No comic panel needs regeneration (captions rewritten within what the existing images show; panel 5 now carries the parallel-instructions warning instead of coaching confidentiality).
- Chapters 15 (`investors-adviser`) and 30 (`useful-engagement`) absorb the shadow-hierarchy and confidentiality material from `git show HEAD:_journals/private-techuity/posts/05-decide-who-decides/index.md`; 05 now only links to them.
**Verification:** arithmetic rechecked (€1m > €500,000 delegation; 80/62/40%/€40,000 match the brief chain); all `[[…]]` targets exist; comic JSON valid, sha256 and asset paths unchanged, six panels; summary word count 500; timetoread 10 min (2,051 prose words); build not run.


## 06-different-bets — Management Equity, Fund Carry and Employee Jobs Are Different Bets (`different-bets`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Complete the title’s comparison → new section “One Consolidation, Four Different Bets” (fictional, own assumptions): closing an acquired add-on product’s second support location (€600,000/yr saving, €350,000 severance, 14 employees, 30 add-on customers). Table compares executives’ equity (~€6m more equity value at an assumed 10× multiple; ~€300,000 for the 5%-above-€100m manager), the fund’s carry (same €6m under the fund waterfall, on the exit clock), employees (11 leave, 3 relocation offers, now) and customers (30 renewals in the two-quarter window). Recorded decision: staged 12-month consolidation, three specialists retained (~€120,000), ~€550,000 from operating cash approved by the board because it exceeds Ines’s €500,000 delegation, six engineer-weeks, pause triggers (renewal rate below last year’s, waiting time breached two months running). “Who Carries the Unresolved Burden” states that the eleven job losses are not compensated and the fund’s timing pressure remains.
- Move leadership replacement → “A Leadership Change Needs a Hypothesis” deleted; one sentence kept in “How to Review a Decision That Incentives May Have Shaped” linking [[fix-decisions-before-hiring]].
- Guardrail list → one worked incentive choice: bonus on 25% revenue growth counted only on contracts with positive first-year contribution; paired with net revenue retention ≥95% and the onboarding waiting-time target; Sam prepares, Ines and the board pay committee review quarterly, Priya accountable for the service measure; growth component withheld and discounted-contract commissions deferred when the guardrail fails; explicit statement that measurement cannot fix a payout rule that rewards the damaging choice.
- Opening generalization → replaced with “An investment may add new equity terms, exit expectations and fund-level incentives to the rewards and risks already shaping company decisions” in index, summary and comic intro.
- Company vs fund waterfall → “company payout waterfall” defined in the equity section; fund waterfall linked to [[fund-economics]] (index, summary, comic panel 2, consolidation table).
- Research annotation context → Leslie & Oyer annotation now states US firms, 1996–2006, 144 PE-owned companies that later went public (verified from the NBER w14331 PDF abstract and introduction).
- Compact worked comparison → three-row table (rollover / purchased shares / options: paid in, at risk, can pay) added before the €2m example.
- “Make Bad News Reportable Early” → compressed into the closing review section (decision quality / execution / result retained, so the Duke annotation still applies).
- Questions to Consider trimmed to four; €2m and option arithmetic kept unchanged.
**Adapted:**
- Optional title shortening → not applied; the review itself calls the existing title justified.
**Declined:**
- none.
**Unresolved / needs separate action:**
- Chapter 13 (`fix-decisions-before-hiring`) must absorb “A Leadership Change Needs a Hypothesis” from `git show HEAD:_journals/private-techuity/posts/06-different-bets/index.md`.
- Figures 1–2 unchanged and still valid. No panel regeneration: panels 3–5 captions retargeted to the worked guardrail and the consolidation, which the existing metaphors (metric race, exit calendar, transition boxes) support.
**Verification:** arithmetic rechecked (5% × €40m = €2m; €30,000 − €20,000 = €10,000; €600,000 × 10 = €6m and 5% of it = €300,000; €350,000 + €120,000 + €80,000 = €550,000 > €500,000; 14 = 11 + 3); all `[[…]]` targets exist; comic JSON valid, sha256 and asset paths unchanged, six panels; summary word count 497; timetoread 11 min (2,224 prose words); build not run.


## 07-investor-under-pressure — Judge an Investor by Their Behavior Under Pressure (`investor-under-pressure`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Resolve the two-investor setup → new section “Compare Both Investors Against the Same Needs” (fictional, own assumptions): Investor A (€5m, higher valuation, broad platform) vs Investor B (€4.5m, one operator, reserved follow-on); table rows: evidence obtained, remaining uncertainty, effect on Larkspur’s next decisions, negotiated commitment. States that either could be right and that the evidence changed which uncertainty Larkspur carries. Recorded decision: B chosen (€4.5m at closing, €1.5m conditional on pilot evidence, ten operator days a quarter); A and delaying the round rejected; capacity; authorized by the board with required shareholder consents; evidence that would reopen it (a second former executive with the same CFO-replacement story, or A writing its follow-on criteria).
- Inherited-relationship route forward → the suggested transition sentence added to the opening; new section “When the Investor Is Already in Place” demonstrates one changed dependency (June hire → dated July board decision after the co-investor commits or declines; pilot funded from operating cash; AI help labelled unconfirmed).
- Missing-evidence outcome → new section “When the Evidence Is Missing”: label support unconfirmed, no funding-dependent commitments, review date (October board meeting), with Larkspur’s plan entries shown.
- Consolidate the last three sections → “Observations to Investigate, and One Reassessment Process”, linking [[decide-who-decides]]; “Test the Relationship You Have” and “Fit Is Not Settled at Signing” folded in.
- Cut detailed engagement design → “Make the Support Offer Reviewable” shortened to one question list plus links to [[help-that-changes-capability]] and [[useful-engagement]].
- “Who owns the decision?” → “who has authority to decide” (index and summary).
- Balanced reference-check paragraph → kept verbatim.
- Comic compares two alternatives → intro and all six captions/dialogue/JSON prompt/alt fields now name Investor A and Investor B and end with Ines’s choice and Alex’s changed dependency.
- Industry-experienced-partner annotation → scoped to US restaurant chains, 2002–2012, health-inspection records, “a relationship in one sector and period, not a guaranteed effect of assigning an experienced adviser” (verified via the Harvard Law School Forum summary).
- Questions to Consider trimmed to four (next three decisions; who worked with the investor when a plan went wrong; unconfirmed dependencies; one change within reach).
- Handoff to Part III now answers the next question (which company initiatives the written-down money and capacity can fund at once): [[part-3]] and [[cannot-fund-everything]].
**Adapted:**
- Corporate-exclusivity example → reduced to one sentence in the inherited section (so the Chesbrough annotation remains accurate) rather than deleted.
- Review’s pacing note (opening details unused later) → “Begin With the Work the Company Needs” now tabulates Larkspur’s three needs and the comparison table reuses them.
**Declined:**
- none.
**Unresolved / needs separate action:**
- Figures 1–2 unchanged and still valid. No comic panel needs regeneration; existing scenes support the new A/B captions.
- The financing figures here (€5m; €4.5m + €1.5m conditional; a €600,000 bridge in a reference’s story) are a separate fictional scenario from chapter 18’s €4m round and the toolkit chain; the text labels them as such.
**Verification:** no historical numbers changed; two annotation scopes verified by WebFetch (Bernstein & Sheen; Leslie & Oyer used for chapter 06); all `[[…]]` targets exist; comic JSON valid, sha256 and asset paths identical to HEAD after correcting a typo I had introduced in panel 3’s hash, six panels; summary word count 466; timetoread 9 min (1,870 prose words); build not run.


## 28-cannot-fund-everything — You Cannot Fund Every Good Project at Once (`cannot-fund-everything`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: bring the resource table forward → new opening section "Three Requests, Two Limits" puts the €500,000 / 24-engineer-week table directly after the three requests; obligations, evidence, dependencies and the experiment row are then explained in "Sort the Rows by What They Rest On" as the team chooses among the rows. "Start With the Result", "Establish the Commitments" and "Compare Complete Options" (including the six-question table) were folded into that section.
- Medium: clarify the funding boundary → exact wording used: "Routine operating work is already budgeted. The following change budget must also fund the improvement needed to meet the agreed recovery requirement." Restoration stays in the change pool (€80,000 / 4 weeks); same model in summary and comic panel 2.
- Medium: one review that changes the selection → the day-45 restoration test fails (eleven hours against four; missing credential and unavailable database version, consistent with the brief's chain and [[prove-you-can-restore]]); correction and retest by day 85 take €20,000 and two engineer-weeks from the reserve. Revised commitment stated: €300,000 / 20 weeks committed, €200,000 / 4 weeks remaining, portal still deferred, retest as next review point. Both the original and the revised selection carry chosen option, rejected alternatives, funding, scarce capacity, authority (board envelope; Ines decides; Alex/Priya accountable) and the evidence that would change the decision.
- Medium: compress the investor-scenario table → replaced by "The Condition That Applies Here": the growth-funding condition (onboarding volume rises without proportional implementation staff) plus links to [[raise-what-you-need]] and [[reading-guide]]; the conditional "this arrangement changes the conditions of the decision" pattern replaces the two-ways framing in article, summary and comic intro.
- Low: end with a usable record and three questions → "Keep the Record" links the [[toolkit]] Tool 12 record (Compare Investment Choices and Capacity); questions cut from six to three; "overruled or unfunded" replaced with the missing-constraint explanation.
- Evidence note on real-options annotation → Luehrman annotation now says the option is only worth what it costs to exercise.
- Investment-thesis wording aligned to the terminology sheet (investor's explanation; revisable prediction, not an instruction).
**Adapted:**
- Review offered "customer research invalidates the portal need" as the alternative review event → chose the failed restore retest per the coordinator's instruction, so the chapter's reserve use matches the shared chain.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Comic panel 6 caption/alt/prompt rewritten to the revised-combination scene; dialogue kept ("Which combination can we actually deliver?") because it is baked into the image; existing image (three people, two option sheets) can plausibly carry it — no regeneration flagged. Panel 2 and 4 captions updated; images still valid.
- Figures 1 and 2 unchanged; captions still fit.
- The €20,000 / 2-week correction figures are this chapter's own fictional exercise (separate from the €300,000 first-hundred-days envelope in `17`); `17` and `11` agents should not need to reconcile them, but they now share the day-45 failure / day-85 retest dates.
- Reading time rose from 8 to 10 min because the two complete decision records were added; the preliminary sections were cut to offset.
**Verification:** arithmetic rechecked (€80k+€180k+€20k = €280k; 4+12+2 = 18; €500k−€280k = €220k; 24−18 = 6; revised €300k / 20 weeks, €200k / 4 weeks left); all six cross-link targets resolve to existing permalinks; comic JSON blocks parse, six panels, no regeneration flag; summary word count 496; spec 56 lines, shorter than the post; build not run.


## 08-roadmap-to-revenue — The Chain From Roadmap to Revenue Breaks Easily (`roadmap-to-revenue`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: finish the pilot decision → new section "What the Pilot Showed, and What Changed" uses the brief's chain result (cohort of eight; 80→62 hours; ~40% of remaining hours from customer data quality; waiting time unchanged). Answers the three conversions explicitly (waiting customers: no, another bottleneck binds; external invoice/hire: no), includes €180,000 build and €30,000/yr maintenance against €135,000 of modelled capacity (100 × 18 h × €75), and states the decision: data-quality step funded from the reserve (€40,000, 4 engineer-weeks), expansion deferred a quarter, hiring deferred; rejected alternatives, funding, scarce capacity, authority (board on Priya's proposal) and the evidence that would change it are all stated. Links [[first-hundred-days]] for the same pilot and the toolkit's Tool 6 ledger.
- High: customer-need test before the business case → "Test Whether the Product Serves a Useful Need" became "Start With a Need Worth Serving" and now sits first, with Larkspur's actual queue (customers sold and waiting; one specialist's manual configuration) as the need, before the chain and the arithmetic.
- Medium: narrow the opening's deadline claim → exact suggested sentence used ("An investor may expect this change to support a particular growth, margin or retention target. Make that expectation explicit, then test whether the benefit and its timing are credible."); summary and comic intro carry the same framing.
- Medium: simplify causal terminology → "financial contribution" for the measure (table and definitions), "helped produce" / "contributed to" for causal claims; the separate "Attribution" label was dropped; baseline, cohort and counterfactual kept. One small-company comparison added: eight pilot customers vs. the previous twelve implementations, with unresolved differences named (sales chose the pilot customers; same specialist, practice effect; quarter-end rush in the earlier period; baseline reconstructed from time records).
- Low: tighten the ending and align the comic → chapter ends on the pilot result and a handoff naming the next constraint; questions cut from six to four, the last about the next constraint; comic panel 2 dialogue changed to "Do customers reach value sooner?" with caption stating it is a hypothesis and the pilot's waiting-time result.
- Investor-introduction passage compressed into the need section (lead, not strategy; displaced work explicit) rather than a standalone section repeating the corporate-exclusivity scenario; comic panel 6 caption aligned (drops "corporate channel"/exclusivity emphasis).
- Handoff to [[can-the-team-deliver]] written to answer the next question, noting that [[fix-decisions-before-hiring]] now follows it in Part III.
- Arithmetic 100 × 80 × €75 / 100 × 50 × €75 kept verbatim; "€1 million program discussed earlier" now cross-links [[obligations-before-budget]], where it is defined.
**Adapted:**
- Review's suggested structure "guardrails and revised decision" → "Protect the Product You Have Not Built Yet" trimmed and placed immediately before the pilot result so the guardrail indicators are named before the review reads them.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Comic panel 2 needs regeneration: dialogue changed from "They reach value sooner." to "Do customers reach value sooner?" and the existing image carries the old bubble text; `"needs_regeneration": true` set in its JSON. Panels 4, 5 and 6 caption/prompt edits keep the existing dialogue and are supported by the existing images.
- Visma reality-check paragraph (with S32 citation) removed from this chapter as an off-topic aside; the S32 source is still cited in [[visma]]. Bibliography agent may want to confirm S32 is still referenced elsewhere.
- Figures 1 and 2 unchanged; captions still fit.
- Reading time rose from 9 to 12 min because of the completed pilot decision and the comparison; the Visma aside and the standalone investor-introduction section were cut to offset.
**Verification:** arithmetic rechecked (€600,000 / €375,000 / €225,000 / 3,000 h; 18 h × 100 × €75 = €135,000); all seven cross-link targets resolve to existing permalinks; comic JSON blocks parse, six panels, one regeneration flag (panel 2); summary word count 497; spec 67 lines, shorter than the post; build not run.


## 09-can-the-team-deliver — Can the Software and the Team Deliver What Was Promised? (`can-the-team-deliver`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Give this chapter ownership of the assessment (high) → new closing section "The Finding" with a six-element table for the second-country plan (required capability, current evidence, preserved strength, constraint, uncertainty, transition resources); the Constraint row is the exact text 27 quotes.
- Correct the broad opening (high) → "In normal operations, engineering constraints are handled as they arise…" replaced with the reviewer's transition ("The expansion date has been proposed before the dependencies were assessed. … Alex's task is to establish what the systems and the team can support, and what must change in the plan"), framed as a condition, not a contrast; applied to index, summary and comic intro.
- Distinguish lead-time measures (high) → new paragraph defining DORA change lead time (commit → production, under two days at Larkspur) vs end-to-end work lead time (request → customer use, about three weeks); DORA's five-metric count kept; section retitled "Evidence About Delivery and Knowledge".
- Clarify the €1.3m table's timing (medium) → total row relabelled "Total transition spending before benefit offsets"; parallel-running row shows months 7–18; text states spending is spread over eighteen months, first benefit (second-country invoicing on the new core) around month twelve, maintenance saving only after retirement.
- "The transition costs behave the same way" → replaced with shared cost categories (capacity, parallel running, migration) and a statement that contracts, exit rights and vendor timing differ for bought systems and need their own plan line.
- Enterprise architecture presented as one relevant question ("one of the questions enterprise architecture exists to answer"), not its whole purpose.
- Relocate standardization detail (medium) → "Standardization Helps at the Right Boundary" section removed; one question remains (what constraints a mandated billing platform / cloud / toolchain creates and who funds compliance) with links to [[acquisition-adds-work-first]] and [[growth-into-design]].
- Fewer fictional projects (low) → the scheduling-engine rewrite became the replacement of the billing and configuration core for the same country case; pricing/invoicing module used only as a named dependency of the second country; closing pricing example folded into the finding.
- Handoff → rerouted to [[fix-decisions-before-hiring]] (organizational response to the two-person queue) and then [[growth-into-design]] (design choice), each phrased as the reader's next question.
- Comic panel 4 (low) → rewritten as an assessment beat (strengths column beside constraints column; dialogue "What do we keep, and what blocks the plan?"); panels 2, 5, 6 captions/prompts aligned with the country case, transition timing and the handed-over finding; comic intro corrected.
- Questions to Consider trimmed to four; "Fund Learning Before Scaling" compressed into the finding section (engineers take part in the diagnosis kept).
**Adapted:**
- "Match the Commitment to the Next Funding Decision" (review: enters next chapter's territory) → kept as one paragraph under the transition section (bounded trial vs repeatable capability) because the spec's success criteria still require it; the four-arrangement scenario list was cut.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Comic panel 4 (`comic-04-scene.jpeg`) needs regeneration: JSON marked `"needs_regeneration": true`; the existing image shows a modular application vs separate services and cannot carry the new caption.
- Figure 1 and Figure 2 captions unchanged; images still valid.
**Verification:** arithmetic rechecked (900,000 + 240,000 + 160,000 = 1,300,000); all `[[…]]` targets resolve to existing permalinks; comic JSON validated, six panels; summary word count 491; timetoread recomputed to 13 min (2,684 body words at 200 wpm); build not run.


## 13-fix-decisions-before-hiring — Fix the Decision Problem Before Adding People (`fix-decisions-before-hiring`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Show the diagnosis producing a staffing decision (high) → new trace table for one Larkspur pricing change (16 working days: 3 commercial decision, 7 specialist queue, 2 build, 3 CEO invoice sign-off, 1 release); "Change the Decisions First" removes six waiting days by delegation (Priya's rule catalogue, Ines's sign-off moved to finance); "Decide What Hiring the Gap Needs" compares full second team / no hiring / reshaped hire and chooses one billing engineer now (about €90,000 a year, operating budget) with protected specialist time, second team deferred — with alternatives rejected, funding, scarce capacity, authority (Alex accountable; Ines takes the changed shape to the board) and three reversal triggers.
- Make this the home for leadership assessment (high) → "A Leadership Change Needs a Hypothesis" from 06 (HEAD) adapted into "Assess Leaders in Their System", combined with the existing role assessment; added a fictional case where the conditions were changed and unused, making added or replacement leadership the justified response; accountability preserved; one-sentence link to [[different-bets]] on compensation/exit distortion.
- Remove the role brief as support (medium) → both P01 citations removed from index and summary; Principal-as-coordinator sentence generalized to "an investor's adviser".
- Consolidate repeated boundaries (medium) → standardization/autonomy cut to "One Boundary Question" (whether the invoicing module stays Larkspur's to change under a group billing platform) with links to [[acquisition-adds-work-first]] and [[growth-into-design]]; full knowledge-transfer test kept and given the Larkspur month-six release test as its exit condition.
- Correct summary cost description and generalizations (low) → "Investment plans usually fund what can be counted… rarely fund" removed from index, summary and comic intro; replaced with "The plan funds new resources, but it has not funded the management time and decision changes needed to use them"; summary now says the comparison starts from €1 million of external development spending, not salaries.
- Nearshoring → "near" defined by geographic or time-zone proximity; cultural similarity "often assumed alongside it and has to be checked separately".
- "An organization chart … hides these dependencies" → "does not capture these dependencies".
- Arithmetic kept and made explicit (€650,000 + €150,000 = €800,000 recurring; €200,000 saving; €1.05m first year).
- Handoff → rerouted from [[acquisition-adds-work-first]] to [[growth-into-design]], phrased as the reader's next question (which system change to fund) with the constraint still open.
- Comic: intro corrected; panel 3 caption aligned to external development spend; panel 4 caption states the leadership hypothesis and its accountability edge; panel 6 caption shows the reshaped hire; dialogue lines unchanged so images remain valid.
- Questions to Consider trimmed to four.
**Adapted:**
- Review's "founder queue" → the traced queue uses Ines (CEO) and Priya as the decision holders rather than introducing a founder, to stay within the fixed Larkspur cast.
**Declined:**
- None.
**Unresolved / needs separate action:**
- None; Figures 1 and 2 captions unchanged, images still valid; no comic panel needs regeneration.
**Verification:** arithmetic rechecked (trace 3+7+2+3+1 = 16; waits 13, six removed, ten remaining; location example as above); all `[[…]]` targets resolve; comic JSON validated, six panels; summary word count 495; timetoread recomputed to 13 min (2,667 body words); build not run.


## 27-growth-into-design — Turn “We Expect Growth” Into a Design Decision (`growth-into-design`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Complete one design decision (high) → new section "Three Options for One Requirement": supplier configuration (A: €60,000 + €40,000/yr, month 4–5), company-owned boundary (B: €140,000, 16 engineer-weeks incl. six specialist-weeks, month 8), core replacement (C: €1.3m/18 months from 09) compared against the same need, date (twelve months), ongoing responsibility and cash limit (€300,000); B chosen under three stated assumptions, A held as fallback, C rejected; funding, scarce capacity, authority (board envelope; Ines authorizes; Alex/Priya accountable) and three reversal triggers named.
- Correct the opening across formats (high) → "The missing connection is specific to investor-backed companies… Under stable ownership…" replaced in index, summary and comic intro with "An investor's growth assumption has reached the team as a request for flexibility. Recover the business requirement before comparing designs."
- Replace the rare-failure rule (high) → last overview row now reads "Compare the dependency's possible impact and likelihood with the cost and effectiveness of the alternatives; include consequences the company cannot accept", linked to [[prove-you-can-restore]]; summary carries the same rule.
- Reformat the build/buy table (medium) → one short overview (priority → trade-off) plus two smaller tables (built system / bought system), with terms defined beside the option that uses them; bought-system depth preserved.
- Make the boundary with 09 explicit (medium) → opening paragraph quotes 09's Constraint row verbatim, states what 13 settled, and says this chapter does not repeat the assessment; former repeated assessment explanations removed.
- Reduce generalization (low) → "Most companies" → "A common arrangement"; "the common way" → "one common way".
- Payback and 10× sensitivity kept as a separately labelled bounded illustration, explicitly not added to the design decision.
- Five-answer decision record filled with the chosen design and stress-tested against slower growth, lower sale valuation and longer ownership.
- Handoff → [[cheaper-cloud-bill]], phrased as the next operating-cost line an investor will question after a design that adds operating responsibility.
- Comic: intro corrected; panel 3 caption/prompt now "compare the designs that meet the same requirement by date and cash limit"; panel 5 labelled as the separate payback illustration; panel 6 shows the completed record; dialogue lines unchanged so images remain valid.
- Questions to Consider trimmed to four; spec open question on Part III ordering closed (decision log entry).
**Adapted:**
- Reviewer's suggestion that option C "exceeds the date" → worded as "far exceeds the cash limit and leaves no margin against the twelve-month date", because 09 puts C's first benefit at about month twelve.
**Declined:**
- None.
**Unresolved / needs separate action:**
- None; Figures 1 and 2 captions unchanged, images still valid; no comic panel needs regeneration. Article is long (3,139 body words, 16 min) because the completed decision and the split tables were added while preserving bought-system depth; a later pass could trim "Other Owners, Other Hypotheses" if length matters.
**Verification:** arithmetic rechecked (€140,000 + €60,000 fallback ≤ €300,000; B − A = €80,000; €200,000 / €100,000 payback ≈ three years after investment; 10 × €100,000 = €1m); all `[[…]]` targets resolve; comic JSON validated, six panels; summary word count 491; timetoread recomputed to 16 min; build not run.


## 10-cheaper-cloud-bill — Why a Cheaper Cloud Bill Can Be Bad News (`cheaper-cloud-bill`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: make the comparison basis explicit → new section "Put Every Figure on the Same Basis" with a four-row table (cash paid / cost assigned to the period / credits / commitment usage); the article states it uses cost assigned to the period, and the €35,000 commitment paragraph says the figure is the monthly cost assigned, so cash timing does not affect the comparison. Summary and comic panel 1 carry the same point.
- Medium: complete the commitment decision → new subsection "The Decision Larkspur Makes": stated demand range (€30,000–€60,000 next year, €20,000 kept as a stress test), stated funding condition (no new financing assumed for twelve months; plan approved for that period only), three options compared on one basis in a table (A flexible; B three-year €35,000 commitment; C one-year commitment covering €30,000 of demand at €21,000 fixed, remainder flexible). Larkspur chooses C (€9,000/month saved across the whole range, €1,000 worse in the stress case, expires with the funded horizon); B and A rejected with reasons; Alex proposes, Sam confirms cash timing and contract terms, Ines approves within delegated authority for contracts of one year or less; four triggers that reopen the decision. Explicit sentence that a company with stable demand and multi-year committed funding might reasonably choose B, so no single result is prescribed. Comic panel 4 caption reflects the decision.
- Medium: group temporary and contractual pricing effects → new section "Credits, Minimum Spend and Ownership-Change Conditions" combines the credits example, minimum spend / signing entity, renewal, carve-out stranded cost and the acquisition synergy point; "Protect the Service the Customer Bought" follows it as the final test. Comic panel 6 caption now names signing entity, minimum spend and ownership change.
- Medium: align savings vocabulary across formats → article, summary and spec use opportunity → change implemented → observed net effect; run-rate projection (€9,000 × 12 = €108,000) is a separately labelled estimate with its assumption stated. Summary's "four different amounts" replaced with the three-term taxonomy plus the labelled projection.
- Low: trim cross-chapter repetition → acquisition paragraph reduced to one sentence plus [[acquisition-adds-work-first]]; peer-network paragraph reduced to one sentence plus [[help-that-changes-capability]]; "Portfolio Comparisons Need a Cohort" folded into a short note after the unit-economics example; questions cut to three (unit and cost basis; explanation for the change; remaining commitment).
- Investor overgeneralization in the introduction → replaced with the specific Larkspur situation (board-approved plan assumes flat spending while volume grows by half; Morgan asks why the bill rose 20%); the "large, visible, adjustable cost that improves the earnings measures" sentence is gone from article, summary and comic introduction.
- End firmly with the contractual choice → the closing paragraph gives Larkspur's answer to Morgan (unit cost fell, one-year commitment saves €9,000/month across the approved range, stress case €1,000, revisit triggers) and the handoff to [[prove-you-can-restore]] answers "what about spending whose benefit you cannot observe on the bill?".
- All three numerical comparisons (€0.10→€0.08, €0.16, €35,000 commitment at €50,000 and €20,000 demand) preserved unchanged.
**Adapted:**
- Reviewer's suggested order (bill change → unit and basis → causes → commitment and credits → full costs and service guardrails → verified result) → followed, except "Prove the Saving Actually Arrived" is placed last so the chapter can end on the verified result and the contractual choice rather than on service guardrails.
**Declined:**
- None.
**Unresolved / needs separate action:**
- No comic panels need regeneration; captions/prompts for panels 1, 4 and 6 changed within what the existing images show. Figures 1 and 2 unchanged and still valid.
- Part III introduction and the reading guide should reflect that this chapter now contains a completed contract decision (coordinator task).
**Verification:** arithmetic rechecked (option table: B €35k/€35k/€45k/€35k, C €21k/€41k/€51k/€21k against flexible €30k/€50k/€60k/€20k; savings €9k across range for C, €6k extra for B at €50k; €9k×12=€108k); all four [[…]] targets resolve; summary word count 497 by the brief's formula; comic JSON validated, six panels; timetoread recomputed to 11 min (2,205 words of body prose before the questions at ~200 wpm); build not run.


## 11-prove-you-can-restore — Prove You Can Restore, Not Just That You Back Up (`prove-you-can-restore`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: make the failed restore the chapter's spine → article now opens with the 6am dispatch scene, defines the recovery objective ("Dispatch must resume within four hours of a failure, with no more than fifteen minutes of lost schedule updates", labelled fictional and not a legal standard, agreed by Priya, the customer team and Alex, approved by Ines), shows the day-45 restore failing it (eleven hours vs four; a night of lost updates vs fifteen minutes; missing credential; unavailable database version), selects the funded corrective item (REC-1: the €80,000 / four-engineer-week "improve and test service restoration" item from [[cannot-fund-everything]] and [[first-hundred-days]]), shows the day-85 retest passing the objective end to end with the customer team, and records residual exposure (regional cloud failure, weekday rehearsal outside the dispatch window, two-person credential procedure) accepted by Ines on the board's behalf with a quarterly retest. Decision example ends with chosen option, two rejected alternatives (defer until funding; two-region redesign), funding, capacity, approver chain (Alex proposes, Sam confirms the €300,000 envelope, Ines approves under the board's plan) and the evidence that would change it.
- High: identify the appropriate authority → "investment committee" removed from article, summary and comic introduction; decision-maker is the Larkspur board (plan and funding), Ines authorizing within it, Alex accountable; Morgan described as the investor's technology adviser who helps obtain specialist judgment but does not decide what Larkspur funds. New paragraph states that documented acceptance records a decision and cannot make an unmet mandatory obligation disappear; specialist interpretation governs and should precede the signature.
- Medium: state recovery objectives in ordinary language → the objective is given as a quoted line, each number explained in dispatcher terms, and the restore test is defined by what it must demonstrate (consistent data, access, dependencies, a dispatcher assigning a job within the objective) rather than an acronym checklist. Summary and comic panel 2 carry the same objective.
- Medium: keep quantified risk as a bounded inset → "Inset: Put a Number on Risk Without Faking a Profit" keeps 5%×€4m=€200,000, 2%→€80,000, €120,000 difference against the €80,000 cost, labels the 2% as an illustrative assumption not measured effectiveness, keeps the tail-risk warning and the "not a booked operating gain" line, and closes with "the arithmetic supports the decision; the agreed objective is the reason for it". Shared-service and data-access detail compressed to one paragraph linking [[useful-engagement]]; exit/data-room material compressed to one sentence linking [[handover-of-obligations]].
- Low: start with the scene and shorten the conclusion → done; the line "Backups running is evidence about backups. Restoring the service is evidence about the business." is kept in the body and echoed in the conclusion and key points.
- "A company under no pressure to show earnings" comparison → removed; replaced with the conditional pattern (ownership arrangement changes the conditions of the decision; recovery competes for the same board-approved cash and engineer-weeks; D-6 recorded in diligence).
- "Security Work Needs an Owner" → retitled "Every Finding Needs an Accountable Leader"; "accountable operating owners" → "accountable leader"; "the Principal" → "the investor's technology adviser".
- "Funding Pressure" and "Shared Support" sections → merged into one short "Shared Support and Changing Owners" section with links to Part IV ([[useful-engagement]]) and Part V ([[handover-of-obligations]]).
- Comic introduction → rewritten around the restore spine; explicitly states the decisions are the company's (board, CEO, CTO), not an investment committee's. Panels 1–6 captions/prompts updated so the six panels follow objective → failed restore → funded fix and retest → residual risk.
- Handoff → to [[ai-strategy-three-questions]], framed as "recovery could be judged by a test the company could run; the next chapter turns to spending whose benefit is harder to observe and easier to assert".
- Questions trimmed from six to four.
**Adapted:**
- Review's proposed final section "implications for shared services and changing owners" → kept, but as one short section rather than two, since the brief assigns that material to Parts IV and V.
- NIST six functions → retained as a one-paragraph orientation with a sentence saying the chapter stays inside Recover (plus Govern and Respond where needed), rather than removed.
**Declined:**
- None.
**Unresolved / needs separate action:**
- No comic panels need regeneration: panel 4 (backup box opening to an untested restore), panel 5 (team practicing restoration and customer communication) and panel 6 (Alex identifying service, decision-maker and support boundary) carry the new captions with the existing images. Figures 1 and 2 unchanged and still valid.
- Fictional details added to the shared chain that other agents (17-first-hundred-days, toolkit) may wish to mirror: the missing credential belonged to an engineer who had left; the backup could only load into its original database version; restored data was as of the previous night's backup; REC-1 buys a version-matched restore environment, managed credentials with a two-person emergency procedure, fifteen-minute backups of schedule data and a rehearsal the operations lead can run; residual risks recorded at day 100 are a regional cloud failure, a weekday rehearsal outside the dispatch window and the two-person credential dependency, accepted by Ines with a quarterly retest. None contradicts the brief's chain; all are labelled fictional.
- Whether "Retest, Then Record What Remains" and "Fund the Corrective Work" should be linked by name from 17-first-hundred-days is a coordinator decision.
**Verification:** arithmetic rechecked (5%×€4m=€200,000; 2%×€4m=€80,000; difference €120,000; €80,000 within the €300,000 envelope); all six [[…]] targets resolve (including the new handover-of-obligations); summary word count 497 by the brief's formula; comic JSON validated, six panels; timetoread recomputed to 12 min (2,384 words of body prose before the questions at ~200 wpm); no historical claims changed, so no WebFetch verification needed; build not run.


## 12-ai-strategy-three-questions — An AI Strategy Hides Three Investment Questions (`ai-strategy-three-questions`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Make the three investment questions the headings, each with a decision, evidence required and one local example → three `## Question N` sections; each ends with chosen option, alternatives rejected, funding, scarce capacity, who is authorized and the evidence that would change it (Q1 paid three-customer classification pilot €45,000 / 6 engineer-weeks with a 95% and 1.5-hour quality threshold; Q2 eight-week support pilot €6,000 / 1 engineer-week with a comparison group and a 20%/10% decision rule; Q3 five-customer substitution test €15,000 / 2 engineer-weeks with the suggestions feature paused). A closing table "Three Funded Decisions and Their Review Triggers" totals €66,000 and nine engineer-weeks.
- Move the coding-study comparison into the internal-work section as a compact evidence box → done as a single blockquote; dates and limits preserved (Copilot experiment run 2022, published 2023, bounded JavaScript server task, 55.8% among completers; METR early-2025 study, 19% longer; METR February 2026 update on selection and concurrent agents). The "excluded cases likely benefit more" statement is attributed to the researchers as their inference, not a measured property.
- Recast the operating model as a proportionate proposal and integrate it earlier → new section "Decide Who Coordinates the Three Questions" placed before Q1: who coordinates (Priya, with Alex for platform/evaluation/data permissions and Sam for expenditure tests), which functions participate (implementation, support, finance first; sales and legal when a question reaches them), which decisions are shared; champions are an option with time and authority, not a requirement for every function. The old "every function can state its goal, its owner and its evidence" test now applies to participating functions only; the two-or-three-functions starting point is restored in the summary.
- Remove "almost every investor now", "most companies make their first mistake", "a valuation question dressed as a technology question" → all removed from article, summary and comic introduction; replaced by the specific growth investor's thesis (paid AI feature before the next round, lower cost per customer, no displacement by a general-purpose assistant). "One common pattern" is used where prevalence cannot be established.
- Develop the competitive-threat example → Q3 names one customer task (weekly maintenance schedule from an asset list), the switching constraint (dispatch integration and regulator records), and the evidence mapping to defend / partner / reprice / stop.
- Shorten repeated capacity-to-cash instruction → cut to two sentences with a link to [[roadmap-to-revenue]]; AI-specific complications (review absorbing saved time, plausible errors, removing reviewers) kept.
- Summary must fit 300–500 prose words → rewritten to 487 words carrying the revised argument; figure line kept.
- Comic must reflect the coordination decision → panel 1 caption/prompt now adds "decide who is accountable for answering each"; panel 2 adds "dates"; panel 6 ties the demonstration to the pilot's quality threshold and price; comic intro corrected. All four fields agree; JSON validated.
- Handoff → now to [[acquisition-adds-work-first]], framed as the sharpest form of the capacity collision; [[cannot-fund-everything]] linked for the trade.
- Questions to Consider trimmed 7 → 4. Spec Intent and success criteria updated (org-wide model criterion replaced by three-question structure + proportionate coordination + no prevalence claims); changelog line added; revised 2026-09-14; status accepted.
**Adapted:**
- "Add the coordination decision to the comic if it remains central" → coordination is no longer the central thesis (it is a proportionate proposal), so it was folded into panel 1's caption, which the existing image (Alex beside three work problems) can carry, rather than displacing one of the six panels.
- ISO/IEC 42001 further-reading annotation ("maps closely to the org-wide AI operating model this chapter argues for") → reworded as the more formal arrangement to compare against the proportionate coordination proposed here.
- "Owner" language ("an owner who outlasts the demonstration", "a champion who owns those goals") → "accountable leader" / "accountable person" per the terminology sheet.
**Declined:**
- Review's option to split the operating-model material into a companion post → not needed; the material was compressed into one section instead of expanded.
**Unresolved / needs separate action:**
- No comic panel needs regeneration; Figures 1 and 2 unchanged and still valid.
- Reading time rose from 8 to 15 minutes (body 3,080 words) because three completed decision examples were added as the review required; restatement layers were cut (questions 7 → 4, data and experiment sections folded into the question sections) but the coordinator may want a further trim.
- Fictional figures introduced (€45,000, €6,000, €15,000, €120,000 suggestions feature, six support agents / 1,200 tickets a month, €64,000 hire cost) belong only to this chapter's scenario; nothing was tied to the Larkspur chain in the brief beyond the shared cast.
**Verification:** arithmetic rechecked (€45,000 + €6,000 + €15,000 = €66,000; 6 + 1 + 2 = 9 engineer-weeks; €32,000 ≈ half of a €64,000 annual hire); all `[[…]]` targets checked against the permalink list; study figures and dates unchanged from the reviewed text, which the review had already confirmed against the primary sources, so no WebFetch was needed; summary word count 487; comic JSON validated; build not run.


## 14-acquisition-adds-work-first — An Acquisition Adds Work Before It Adds Value (`acquisition-adds-work-first`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Give the two processes a visible structure under a shared boundary-and-continuity principle → new `## One Principle: A New Boundary, a Continuing Customer Promise` stating both completion tests, then `## Combining Businesses` (thesis, depth, capacity decision) and `## Separating a Business` (independence bill, completed bridge), each with its own fictional Larkspur example and completion test.
- Add a capacity decision for an acquisition → "Decide What Waits": the add-on's identity/data integration (16 engineer-weeks) collides with the promised customer portal (10) and the fund's next-target diligence (3) on the same two scheduling-engine engineers (29 vs 26 weeks); board puts the priced integration first, moves the portal one quarter with customers told, delays the diligence six weeks; synergy date stays at month nine; contractors and delaying the integration rejected; investment committee informed; evidence that reopens the order stated.
- Complete the carve-out bridge → closing 1 July 2026, TSA end 30 June 2027 with one three-month extension at 150%, milestones 31 Oct 2026 / 31 Jan 2027 / 30 Apr 2027, Alex accountable for technology services and Sam for finance, two months parallel running, and a May 2027 independent-service test (month-end close, customer onboarding, release, restore against the recovery objective with no parent access). Decision record ends with chosen option, rejected alternatives, funding (€300,000 one-time + €300,000 recurring), scarce capacity, authority and change evidence.
- Correct the opening across formats → article, summary and comic introduction now open with "The transaction plan can assume savings or independence before the operating teams have validated the work. Bring those dependencies into the discussion while scope, price and timing can still change." "Both are usually investor decisions" and "on the investor's timetable" removed; the specific Larkspur approval path (deal team proposes, investment committee approves terms, Larkspur board approves plan and budget, seller and regulator affect timing) replaces the generalization.
- Keep the €400,000 → €700,000 standalone-cost bridge and the TSA explanation → retained verbatim in substance.
- Absorb the group-vs-local standardization boundary point from chapter 09 → one paragraph in "Choose the Depth of Integration": a standard needs a stated problem, cost of compliance, exceptions process and a named funder of the transition; links [[growth-into-design]].
- Responsibility language → "who owns them" → "who is accountable for each"; "an accountable owner" → "an accountable leader"; "who owns and can use the code" → "who holds and can use"; "share an owner" → "under common ownership".
- Shorten repeated minority-vs-controlling comparisons → the separate "The New Owner Changes the Integration Question" section removed; the buyout-fund vs corporate-buyer contrast is now two sentences keyed to the depth table's rows with a link to [[decide-who-decides]].
- Keep the Skype IP lesson bounded → retained with "The bounded lesson is to inspect the capability boundary, not just the source code."
- Handoff to Part IV → answers where the specialists the examples relied on come from and how to keep decision authority inside the company: [[part-4]] and [[investors-adviser]]; [[handover-of-obligations]] linked for obligations open at an ownership change.
- Comic: intro corrected; panel 2 adds "which roadmap work waits"; panel 5 adds the replacement milestone and independence test; panel 6 replaces "a sponsor's shared reporting" with "a buyout fund's shared reporting" and adds an accountable leader per replaced service. All four fields agree; JSON validated.
- Summary rewritten (499 prose words) carrying both examples and the corrected opening; figure line kept. Questions to Consider trimmed 6 → 4. Spec Intent and success criteria updated; changelog line added; revised 2026-09-14; status accepted.
**Adapted:**
- Review's proposed structure put rights/pre-closing constraints before the completion tests → kept as `## Investigate Rights and Dependencies Before the Purchase` followed by `## Measure the Customer and Cash Results`, with the two completion tests referenced back to the principle section rather than restated.
- "Finish on evidence that one chosen boundary now works" → the May 2027 independence test is the evidence design; the chapter does not narrate a passed test because the scenario is dated after this chapter's analysis date.
**Declined:**
- None.
**Unresolved / needs separate action:**
- No comic panel needs regeneration; Figures 1 and 2 unchanged and still valid.
- Reading time rose from 8 to 14 minutes (body 2,714 words) because two completed decision examples were added as the review required.
- The carve-out scenario's dates (closing 1 July 2026, TSA to 30 June 2027) are new fictional assumptions labelled "separate assumptions"; they do not reconcile with the Part V chain and are not meant to.
- Chapter 09's agent is shortening its standardization section in parallel; the coordinator should confirm the one-paragraph version here is the surviving home of the "stated problem / cost of compliance / exceptions / funder" test alongside `growth-into-design`.
**Verification:** arithmetic rechecked (16 + 10 + 3 = 29 engineer-weeks vs 26 available; €700,000 − €400,000 = €300,000 recurring plus €300,000 one-time; TSA extension priced, not summed); all `[[…]]` targets checked against the permalink list plus `handover-of-obligations`; no historical claim changed (Skype filing wording unchanged), so no WebFetch was needed; summary word count 499; comic JSON validated; build not run.


## 15-investors-adviser — Is the Investor’s Adviser Helping, Assessing or Deciding? (`investors-adviser`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Make dual-role conflict the central case → new section "When a Coaching Conversation Becomes an Assessment": Morgan coaching Alex for three months, then the deal team asks for a written leadership view; covers what Alex can ask before sharing sensitive information, what Morgan must explain, who can authorize the changed assignment (Ines/board, not the firm alone; same for an interim delivery assignment), how employees are informed (written note from Ines); confidentiality explicitly limited to agreed obligations.
- Correct the uniqueness claim across formats → opening, summary and comic intro now use the "reports to the investment firm, so the company needs to understand both the operating assignment and how findings may inform the investor’s decisions" framing; "no such person exists" and the consultant contrast removed everywhere.
- Introduce "investor’s technology adviser" as the general term; keep "Technology Principal" as the supplied example → done in article, summary and comic panel 1.
- Absorb "Support Can Become a Shadow Hierarchy" and coaching-confidentiality material from chapter 05 → adapted into "Separate Influence From Authority" (parallel reporting line, hands-on is not taking over) and the role-change section (no unlimited promise of secrecy; escalation under engagement obligations).
- Assignment table as a diagnostic → fourth column "What employees should hear" (assessment finding / recommendation / authorized instruction); "Deciding is not a sixth kind of help" stated in the reporting-relationship section.
- Move engagement mechanics to Useful Engagement → availability, internal resources, ongoing service and handover sections removed; two link sentences to [[useful-engagement]] remain; "Distinguish Advice from Delivery Help" folded into the table row.
- Replace the reused three-week billing-code example → replaced by the D-3 disagreement (Alex’s data-quality explanation vs Morgan’s structural reading, resolved by the pilot cohort’s measured split), linked to [[diligence-corrects-the-plan]].
- End with the agreed purpose and authority of the opening meeting → new closing section "Back to the Planning Meeting"; "Judge What the Company Can Do Better" removed.
- Consolidate comic panels 1 and 6 → panel 6 now shows the role change and its consequence (Morgan moves from the coaching card to the assessment card; Ines holds the note for the team).
- "Who is authorized to decide?" wording → article, summary and comic panel 2.
- ICF annotation → reworded so the code binds only coaches who adopted it.
- Questions to Consider trimmed to four.
**Adapted:**
- Availability as a planning input → kept as one sentence in the assignment section (and comic panel 4, whose image exists) rather than a section, because the reader still needs the pointer before the engagement chapter.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Comic panel 2 needs regeneration (speech bubble in the image reads "Who owns this decision?"; new dialogue "Who is authorized to decide?").
- Comic panel 6 needs regeneration (image shows fund adviser / introduced specialist / corporate function cards with the old bubble; new scene is the role change).
- Comic panel 3: caption and alt made generic; the existing image still shows a paper labelled "pricing-change example". Usable, optional regeneration.
- Figures 1 and 2 unchanged and still supported by the text.
- Chapter 05’s agent should remove its shadow-hierarchy section and coaching-confidentiality detail and link here (per brief §1.5).
**Verification:** no numeric claims changed; all `[[…]]` targets checked against the current permalink list (decide-who-decides, diligence-corrects-the-plan, help-that-changes-capability, useful-engagement); comic JSON parsed and captions/dialogue/alt matched across all six panels; summary word count 486; article body 2,241 words → timetoread 11 min; build not run.


## 29-help-that-changes-capability — Find the Help That Changes What Your Team Can Do (`help-that-changes-capability`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Correct the opening across formats → "An investor may give Larkspur faster access to relevant people and experience. Compare that access with the help the company could obtain elsewhere, including the time and obligations each route brings" now governs the article opening, key points, summary and comic intro; "exists only because of the investor" / "a single company couldn’t reach" removed everywhere; investor motives allowed to be mixed (holding value, service economics, portfolio relationships, reputation).
- Show a selection among credible alternatives → new section "Compare Credible Alternatives for the Same Need": table of peer conversation / investor’s specialist / independent specialist / permanent hire with availability, company effort, cost category, relevant experience and verdict; followed by chosen option, alternatives rejected, funding (ONB-1 budget), scarce capacity (six engineer-days from portal research), who is authorized (Priya within the pilot budget; Alex commits the engineer), and the evidence that would change it. Figures consistent with the brief’s chain (ten days over six weeks; €300,000 for two hires → ~€150,000 each; hiring deferred pending pilot evidence).
- Keep one support map → company-need table kept; corporate shared-service/channel conditions folded in as one row; investor-category catalogue ("Compare the Offer With the Investor’s Actual Position") removed; summary’s matching paragraph removed.
- Absorb the peer-network material from chapter 18 → compressed into "Peer Communities Are One Source" (decisions participants actually face; information boundaries in a small portfolio; context kept with the practice).
- End with the actual written request → blockquote "Help our customer team make one setup path repeatable, using a specialist who can work alongside our engineer for six weeks; Priya will assess customer outcomes", with what it fixes and what it leaves open for [[useful-engagement]].
- Move charter and coaching detail to links → hiring/development section compressed into "Use Connections With Care" with a link to [[investors-adviser]]; availability section folded into the comparison; continuing-service allowance kept with a link to the engagement review.
- Billing-code example replaced → the onboarding gap now uses the D-3 sample (three of five implementations, ~80 hours) so the opening problem is not changed mid-chapter.
- "Borrow experience with its context attached" kept as a section heading and bolded sentence.
- Research annotations qualified → Hellmann & Puri (Silicon Valley sample), Bernstein et al. (airline-route travel-time design, population-level estimate for venture-backed firms, cannot judge one engagement), Sørensen (matching model).
- Questions to Consider trimmed to four.
**Adapted:**
- Reviewer’s "Start Small and Transfer the Work" anchor scene → merged into the comparison and the "Borrow experience" section rather than kept as its own section, to avoid a second bounded-assignment description before the engagement chapter.
**Declined:**
- Combining with useful-engagement → the brief keeps the chapters separate with distinct jobs.
**Unresolved / needs separate action:**
- No comic panel needs regeneration: panels 2, 5 and 6 carry new captions that the existing images and baked-in speech bubbles support; alt/prompt updated to match.
- Figures 1 and 2 unchanged and still supported by the text.
- Chapter 18’s agent should remove "Portfolio Collaboration Must Earn Its Time" and may link here (per brief §1.5).
**Verification:** arithmetic rechecked (€300,000 for two hires → about €150,000 each; ten specialist days over six weeks and six engineer-days match chapter 30’s charter); Bernstein, Giroud and Townsend abstract verified via the Semantic Scholar record for DOI 10.1111/jofi.12370 (identification through new airline routes reducing VC travel time to existing portfolio companies) — Wiley and doi.org returned 403/redirect; Hellmann & Puri and Sørensen descriptions reworded only within what the existing annotations already claimed plus the study type, not re-fetched; all `[[…]]` targets checked against the permalink list (diligence-corrects-the-plan, first-hundred-days, investors-adviser, useful-engagement); comic JSON parsed and captions/dialogue/alt matched across six panels; summary word count 488; article body 2,304 words → timetoread 12 min; build not run.


## 30-useful-engagement — Turn an Offer of Help Into a Useful Engagement (`useful-engagement`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Fill in the charter for the opening engagement → twelve-field table completed for the ONB-1 pilot support using the brief’s facts: need (D-3, ~80 hours), result, Priya accountable, investor-side sponsor (the firm’s partner responsible for the Larkspur holding; Morgan introduced the specialist and is not the sponsor), ten specialist days over six weeks, six engineer-days released from portal research, two customer-team sessions, funding (specialist days charged to Larkspur from the €180,000 ONB-1 budget), authority, information use, baseline by day 20, scope boundary, week-six review, handover test.
- Carry the same engagement through a scope change → new section "Week Three: the Evidence Changes the Problem": data quality decides completion time for imperfect-data customers; Priya proposes, sponsor agrees, Alex confirms; templating of less common customer types and the second template session stop; remaining five specialist days go to a data-intake check, engineer days to a validation; ten days / six engineer-days / no extra cash / review date unchanged; alternatives rejected (continue, extend by four weeks, stop and hire) and the evidence that would reverse it; full data-quality step deferred to the day-90 board review.
- Correct the opening and the sponsor label → "The specialist also reports to the investor. Before work starts, agree how that responsibility relates to the company’s priorities and who can direct the assignment" in article, summary and comic intro; "engagement sponsor" renamed "investor-side sponsor" with a separate accountable company leader throughout.
- Absorb chapter 05’s charter-related governance boundary → one governance paragraph (parallel reporting line, charter names accountable leader/role/boundaries, two advisers = one company question, required group service).
- Let investors-adviser own role/confidentiality and roadmap-to-revenue own causal measurement → "Keep Investor Support Within One Company Plan", "Agree How Information Will Be Used" and "Begin with Evidence You Can Compare Later" replaced by one applied paragraph each under "Apply the Boundaries Other Chapters Own", with links.
- Move Figure 2 before the Part V handoff → done; three-way ending kept.
- Comic ends on the handover/changed decision → panel 6 rewritten (engineer completes a setup with the specialist observing; data-quality finding to the board); panels 2–5 captions aligned to the completed charter and scope change.
- Handoff to [[part-5]] / [[diligence-corrects-the-plan]] → rewritten to answer the reader’s next question (where the finding came from and how it became a funded plan).
- Questions to Consider trimmed to four.
**Adapted:**
- Corporate-investor and two-adviser material (spec’s former intent) → compressed into the governance paragraph rather than kept as a section, so the chapter stays on one engagement.
**Declined:**
- Combining with help-that-changes-capability → the brief keeps the chapters separate with distinct jobs.
**Unresolved / needs separate action:**
- Comic panel 6 needs regeneration (image shows two adviser assignments with the bubble "One company plan, with clear responsibilities.").
- Figures 1 and 2 unchanged and still supported by the text.
- Chain facts other agents may rely on: investor-side sponsor = the firm’s partner responsible for the Larkspur holding (named by role); specialist days charged to the company from the ONB-1 budget; week-three change redirects the remaining five specialist days to a data-intake check without new cash; the engagement ends at week six with no continuing service, and the data-quality finding feeds the day-90 review (consistent with the day-100 results in the brief). Chapter 17 and the toolkit may want to reference these.
**Verification:** arithmetic rechecked (5 + 5 specialist days = 10; six engineer-days unchanged; no cash added to the €180,000 ONB-1 budget; baseline ~80 hours matches D-3); all `[[…]]` targets checked against the permalink list; comic JSON parsed and captions/dialogue/alt matched across six panels; summary word count 494; article body 2,448 words → timetoread 12 min; build not run.


## 16-diligence-corrects-the-plan — Diligence Is Your Chance to Correct the Plan Before It Is Signed (`diligence-corrects-the-plan`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: add a complete finding and negotiated implication → new section "Finding D-3: Onboarding Depends on One Specialist’s Manual Configuration" with a 12-field record (observed / reported / inferred / not established / consequence / options / agreed response / approvers / accountable company leader / recorded disagreement / evidence to resolve / handoff) using the brief's exact figures, followed by a paragraph on the three changes to the growth plan (2×→1.5×, second country conditional, pilot funded) and the full decision statement (chosen option, rejected alternatives, funding, scarce capacity, who is authorized, evidence that would change it). D-5 and D-6 named as further findings that travel with D-3.
- High: clarify the leader's access and timing → new section "What You Can Do Depends on When You Have Access" directly after the opening, a three-row table (before signing / between signing and closing where that gap exists / after closing when earlier participation was impossible), stated as operating opportunities, not universal rights; Larkspur's stage (before signing) named.
- Medium: merge the two opening method sections → "Match the Evidence…" and "Start With an Investment Question" merged into "One Investment Question, Matched to the Transaction"; the seven-dimension table moved after the finding as "Seven Things to Examine: A Coverage Check" with D-3/D-5/D-6 mapped onto its rows.
- Medium: distinguish the two records → "The One-Page Thesis Summarizes the Findings" states that the finding record holds evidence and response for one issue while the thesis summarizes and links the findings; links [[toolkit]].
- Low: rewrite the exclusive definition across formats → article, summary and comic intro now read "In this transaction, technical diligence tests the product, technology and team assumptions behind the proposed investment"; secondary-purchase money recipient made explicit with a link to [[customers-lenders-investors]].
- Further reading: Mao & Renneboog annotation scoped to a UK management-buyout sample and accruals-based measurement limits, explicitly not a claim that every presenter manipulates every number.
- Handoff to [[first-hundred-days]] names D-3, Priya's ten-day acceptance and the day-90 review; "Questions to Consider" trimmed from six to four.
- Comic: intro rewritten; panels 3–6 now carry D-3 (observed/reported/inferred, the plan change, approvers and disagreement, access by stage and handoff); caption, alt, prompt and dialogue agree; six panels, images and sha256 unchanged.
**Adapted:**
- "Use the thesis as a short summary of linked findings in the toolkit" → the article states that relationship and links [[toolkit]]; the toolkit page itself is the coordinator's.
**Declined:**
- None.
**Unresolved / needs separate action:**
- No panels flagged for regeneration: the existing scenes (labelling, a finding moving toward a decision, annotation, a funding condition) plausibly carry the new captions. Figure 2 caption changed "someone responsible" to "someone accountable"; image still valid.
- Coordinator: the toolkit should show the same D-3 record and thesis link this chapter now promises; part-5 intro may want to mention that chapter 16 now completes D-3.
**Verification:** arithmetic rechecked against the brief (€300,000/yr hire option; €180,000 + €30,000/yr + 12 engineer-weeks pilot; 2×→1.5×); cross-links checked against existing permalinks (customers-lenders-investors, cannot-fund-everything, roadmap-to-revenue, hilton-and-skype, toolkit, first-hundred-days); comics JSON parsed and caption/alt/dialogue agreement checked by script; summary word count 488; timetoread 10 min (2086 prose words at 200 wpm, same rule as the original 9-min label); protected front matter unchanged; build not run.


## 17-first-hundred-days — The First Hundred Days: Turn Expectations Into a Funded Plan (`first-hundred-days`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: build one genuinely funded example → "A Funded Plan for the First Hundred Days" carries the brief's table verbatim (ONB-1 / KNW-1 / REC-1 with accountable person, additional cash, engineer-weeks, decision date, prerequisite; total €260,000 / 20 engineer-weeks inside the €300,000 / 24-week board envelope; reserve €40,000 / 4 weeks), labelled fictional, with the three deferrals (portal research-only, second country, two hires) each with a recorded decision, and a full decision statement (chosen plan, rejected alternatives, funding, scarce capacity, who is authorized, evidence that would change it). The recovery objective is quoted from the brief and labelled an agreed fictional objective.
- High: carry a finding from diligence into the plan → "Confirm the Inherited Finding With the People Who Will Deliver It" holds a D-3 table: original thesis assumption, diligence evidence, management's confirmation after closing (dependency confirmed; sampled 80 hours rejected as baseline; baseline from actual records by day 20; Alex's data-quality explanation kept as the recorded disagreement), funded response ONB-1. D-5 and D-6 named as the sources of KNW-1 and REC-1.
- Medium: show the hundred-day review changing something → "Review the Plan, Not Its Completion Rate" gives the brief's results (REC-1 fails at day 45, passes at day 85; KNW-1 passes at day 60; ONB-1 80→62 hours vs 50 assumed, ~40% data quality, waiting time unchanged) and the board decision (expansion deferred one more quarter; €40,000 / 4-week data-quality step from the reserve; hiring stays deferred; handover record carries D-3/ONB-1 forward).
- Medium: shorten the ownership and support recaps → the investor-category table replaced by "What Actually Changed" (chosen growth-investment scenario, board envelope, IC vs board authority) plus a link to [[raise-what-you-need]]; the support-charter section reduced to "Investor Support Inside the Plan" (ONB-1's support summarized, link to [[useful-engagement]]). Warning that unselected material risks still need a decision kept.
- Low: align the opening and shorter formats → "A new investor replaces that rhythm with its own" replaced in article, summary and comic intro by "The transaction introduces new assumptions and review dates, and it can introduce a new review timetable and expectations…"; "Confirm which of them change the company's existing plan" added.
- Repeated plan-field lists removed from the former "Few Priorities" section and the close; "Sequence the Dependencies" and "Measure Before the Story Hardens" merged into "Sequence the Dependencies and Accept Imperfect Baselines" and applied to the three priorities.
- Summary now says "The plan is worked through" and carries the full table figures and day-100 results.
- Handoff to [[the-financing-slipped]] answers the next question (what if the plan's money arrives late) and names [[handover-of-obligations]] for continuing obligations, including D-3.
- Further reading: EBRD annotation softened to "associated with returns; it does not show that any planning template causes them". "Questions to Consider" trimmed from six to four.
- Comic: intro and all six captions/prompts rewritten around the funded plan and day-100 results; caption, alt, prompt and dialogue agree; six panels, images and sha256 unchanged.
**Adapted:**
- Review's "management's updated evidence" → the brief supplies no separate post-closing measurement before day 100, so management's confirmation is shown as: dependency confirmed, sampled figure rejected as baseline, baseline due from actual records by day 20, disagreement kept; the updated evidence itself arrives at the day-100 review. No new figures invented.
**Declined:**
- None.
**Unresolved / needs separate action:**
- No panels flagged for regeneration: panel 3 (three priorities beside limited capacity) and panel 6 (trophy replaced by a revised decision) carry the new captions; panel 5's alt now says "accountable leader" instead of "owner" (image unaffected). Figures 1 and 2 unchanged.
- Coordinator: chapter 30 should match the ONB-1 support figures (ten specialist days, six company engineering days, two customer sessions, week-six review) this chapter now references by description; chapter 31 receives the handover record for D-3/ONB-1 (baseline, actual cost, observed result, open work); chapter 18 is linked as "what changes when financing slips".
**Verification:** arithmetic rechecked (180,000 + 0 + 80,000 = 260,000; 12 + 4 + 4 = 20; reserve 40,000 / 4; envelope 300,000 / 24); cross-links checked (diligence-corrects-the-plan, raise-what-you-need, prove-you-can-restore, roadmap-to-revenue, useful-engagement, the-financing-slipped, handover-of-obligations); comics JSON parsed and caption/alt/dialogue agreement checked by script; summary word count 494; timetoread 10 min (1978 prose words at 200 wpm, same rule as the original 7-min label); protected front matter unchanged; build not run.


## 18-the-financing-slipped — The Roadmap Did Not Slip, the Financing Did (`the-financing-slipped`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: split immediate replanning from handover preparation → the chapter now ends at the authorized financing fallback and hands off to [[handover-of-obligations]]; "Exit Readiness Is Evidence Readiness", "Avoid Exit-Period Distortions", "A Sale Is Not Always the End of Ownership Work", "A Handover Does Not Always Mean a New Controlling Owner" and "Learn After the Handoff" removed here (adapted into 31); Figure 2 (evidence-carried-through-ownership.jpeg) moves to 31 by path, image file untouched.
- High: complete the funding decision → dated cash table (€1.6m on 1 July, €200,000 burn, €400,000 reserve reached 31 December); commitments sorted into protected / committed / still reversible (hires +€30,000 a month, €120,000 portal at signature); alternatives A/B/C priced by reserve date (late November / 31 December / 31 March); latest useful decision date 15 August; board decision 10 August recorded with chosen option, alternatives rejected, funding, scarce capacity, who is authorized, review 1 October and the evidence that would change it; two short variations (refinancing that leaves less cash; corporate parent withdrawing budget).
- Medium: move general support material to Part IV → "Portfolio Collaboration Must Earn Its Time" deleted (goes to 29 per brief); "A Regular Conversation With a Purpose" and "Escalate Through a Defined Path" cut to the single escalation step the decision needs (decision required, latest useful date, consequence of delay), linked to [[decide-who-decides]].
- Medium: correct the non-investor contrast across formats → "In a company without investors, a plan can be revised quietly" and the fund-life / prospect-of-sale framing removed from article, summary and comic intro; the reviewer's suggested opening is used verbatim; the conditional pattern names the specific condition (the date offers and a signature make the plan irreversible).
- Low: keep transaction definitions in the handover article → IPO / secondary sale / continuation definitions moved to 31; the conclusion here names what continues if the money never arrives (continued ownership as a real scenario, the named reduction list).
- Preserve the blame distinction (failed hypothesis vs poor execution vs unfunded dependency) → kept in "The Funding Slipped, Not the Roadmap" and in the summary.
- Terminology sheet: commitment states (expression of interest → approval pending → contractual commitment with conditions → cash received) used throughout; bridge approval assigned to the existing investors' investment committees, the operating plan to the Larkspur board; "accountable" / "authorized" wording.
- To Probe Further: Bain 2026 and ILPA continuation-funds entries moved to 31; Brown/Gredil/Kaplan and Baik kept with annotations narrowed to reporting incentives (Baik described as an analogous reporting incentive, not direct evidence about delayed rounds).
- Questions trimmed from 6 to 3; excerpt updated to the financing promise; timetoread recomputed (2,244 body words at 200 wpm → 11 min read); title, permalink, date, logo, icon unchanged.
- Summary rewritten to the financing decision (484 words); comic intro, captions, dialogue, alt and prompt rewritten so the six panels tell the delayed-financing story.
**Adapted:**
- Brief §3 gives "A, proceed as planned → reserve breached mid-November" → with the listed figures the breach falls in late November (baseline €600,000 at 30 November less €120,000 portal less 3 × €30,000 hires = €390,000, below the €400,000 reserve). Article, summary and comic say "late November" and show the arithmetic rather than assert a date the figures do not produce. If another chapter or the toolkit cites mid-November, an extra assumption (e.g. portal payment timing or recruiting costs) would need to be stated there.
- Figure 1 (ownership-paths-and-replanning.jpeg) kept with a reworded caption (review junction after a funding delay; the plan needs a fallback on every path); image still valid.
- Summary figure (summary-at-a-glance.jpeg) kept with a new caption (observe / decide / act / record; the record serves continued ownership or a change); image still valid.
**Declined:**
- Collection review's "documented venture funding delay case" → not added; no evidence base is available and brief §1.6 records this as a declined recommendation.
**Unresolved / needs separate action:**
- Comic panels 2, 3 and 4 need regeneration: their baked-in speech bubbles ("Clarify the conversation's purpose", "Share the learning appropriately", "Can a buyer examine this claim?") and scenes belong to the old cadence / confidentiality / buyer story; their JSON now carries the new prompt/alt/caption and `"needs_regeneration": true`. Panels 1, 5 and 6 keep their artwork with new captions; panel 6's visible "Support agreement" document label is from the old scene and is tolerable, optional regeneration.
- Chapter 17's closing handoff at HEAD ("through revised funding, changing investor expectations and possible ownership transitions") now overstates 18's scope; whoever owns 17 or the coordinator may tighten it to the delayed-financing decision.
- Part V intro, the reading guide's "ownership change is imminent" route and any toolkit / glossary pointers to this chapter's handover content should point to [[handover-of-obligations]] (coordinator).
- Bibliography "cited in" notes: [S02], [S24], [S30] are no longer cited from 18; they are cited from 31.
**Verification:** arithmetic rechecked (six months from €1.6m to the €400,000 reserve at €200,000 a month = 31 December; A = €390,000 at 30 November; C = +€600,000 = reserve at 31 March); all [[…]] targets resolve against current permalinks plus `handover-of-obligations`; comic JSON parsed with json.loads, six panels, image references unchanged; summary word count 484; build not run.


## 31-handover-of-obligations — Hand Over the Obligations, Not Just the Company (`handover-of-obligations`)

**Files changed:** index.md, summary.md, spec.md (new folder `31-handover-of-obligations/`; no comics.md; no assets folder; not added to config.yaml)
**Implemented:**
- Brief §1.1 / collection review "explicit handover destination" → new chapter created with the prescribed structure: Keep the Evidence During the Work (with "The Larkspur record at day 100") → Avoid Exit-Period Distortions → Who Receives Cash and Who Keeps an Interest → Authority Changes Even When the Name Does Not → Unfinished Obligations Travel With the Company → The Accepted Handover Record → Permitted Follow-Up and Learning → Questions to Consider (3) → To Probe Further.
- Chapter 18 review "secondary sale should name company shares or a fund interest" → a transaction table separates funding round, secondary sale of company shares, sale of a fund interest, continuation transaction, IPO and sale of control by who receives cash, who keeps an interest and what the company receives; the continuation transaction's price and conflict questions are kept with [S02].
- Material adapted (not pasted) from the HEAD sections of 18; citations [S02], [S24], [S30] preserved with their original links; cross-links to [[three-different-returns]], [[hilton-and-skype]], [[visma]], [[teamsystem]], [[toolkit]] (Tool 10, "Prepare a Funding or Ownership Handover") kept; added [[the-financing-slipped]], [[diligence-corrects-the-plan]], [[first-hundred-days]], [[decide-who-decides]], [[acquisition-adds-work-first]], [[cheaper-cloud-bill]], [[ai-strategy-three-questions]], [[part-6]].
- Brief §3 handover record → Larkspur D-3/ONB-1 table: baseline 80 hours (measured by day 20), actual cost €180,000 build / €30,000 a year / 12 engineer-weeks, observed result 62 hours in an eight-customer cohort with ~40% of remaining hours traced to data quality and waiting time unchanged, open work (data-quality step €40,000 and 4 engineer-weeks from the reserve; second-country expansion deferred a quarter; two hires deferred), accountable leader Priya, evidence that would change the next decision; D-5 (second engineer demonstrated at day 60) and D-6 (restore failed day 45, passed day 85) named as further entries. Labeled fictional.
- Figure 2 of old chapter 18 reused via the merged asset path `assets/images/18-the-financing-slipped/evidence-carried-through-ownership.jpeg` with its original caption; no file copied.
- To Probe Further: Bain 2026 and ILPA continuation-funds entries moved from 18, annotations kept within scope (Bain read as an interested publisher's view; ILPA as the fund-investor side of continuation transactions). No new entries; no URLs fetched because nothing was added.
- Handoff: Part V recap (investigation, early plan, delayed financing, handover) and Part VI via [[part-6]] and [[hilton-and-skype]].
- Front matter as in 18 minus logo / logo_credit / icon; date 2026-09-14; one-sentence excerpt; timetoread 11 min (2,132 body words at 200 wpm); KEY POINTS with exactly three bullets.
- summary.md: 497 words of prose plus the reused figure line; spec.md: status accepted, revised 2026-09-14, Intent / Success criteria for this chapter, Changelog "2026-09-14: Created by splitting handover material out of the delayed-financing chapter."
**Adapted:**
- Figure numbering → the reused image is captioned "Figure 1" here because it is this chapter's only figure (it was Figure 2 in old chapter 18); caption text unchanged.
- The old "Learn After the Handoff" paragraph on later deterioration / later success is kept but shortened; the old "A Sale Is Not Always the End of Ownership Work" definitions are recast as the transaction table plus one paragraph on the two forms that need care.
**Declined:**
- Collection review's "documented corporate ownership case" and "documented venture case" → not added (brief §1.6; no evidence base).
**Unresolved / needs separate action:**
- comics.md (six panels), the post logo and the navigation icon need image generation; no image key was available. The front matter deliberately has no logo / icon fields until they exist.
- config.yaml entry (Part V, after `18-the-financing-slipped/index.md`) — coordinator.
- Bibliography "cited in" notes for [S02], [S24], [S30] should now name this chapter.
- Tool 10 is referenced by number and current name; if the toolkit revision renumbers or renames it, update the sentence in "The Accepted Handover Record".
**Verification:** all Larkspur figures match brief §3 (80 h → 62 h, €180,000 / €30,000, €40,000 + 4 engineer-weeks, day 20 / 45 / 60 / 85 / 90 dates); all [[…]] targets resolve; citation links identical to the HEAD text of 18; summary word count 497; build not run.


## 21-hilton-and-skype — Hilton and Skype: A Successful Exit Still Needs Explaining (`hilton-and-skype`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Preview the contrast in one sentence before the first chronology → opening paragraph now states "Hilton needs a financing explanation; Skype needs an explanation of technology rights and of what one particular buyer valued"; KEY POINTS bullet 1 carries the same contrast.
- Short comparison table near the beginning (holding period, financing issue, technology issue, type of exit) → added after the intro; values stay in the case sections; the old end-of-chapter comparison table was removed as duplicate.
- High impact: explicit technology chronology (inherited / documented change / remaining uncertainty) per company → one three-row table per company, drawn only from S23 and S27. The Hilton S-1 was re-downloaded and grepped: it names OnQ as proprietary and describes "strengthening and expanding" the commercial platform in a transformation "since 2007" but attaches no date to any system's creation; the article now says so explicitly and states that nothing in the sources supports reading Blackstone as the creator of OnQ or dates a technology change to ownership. Skype's dated change is the November 2009 Joltid settlement; Qik/infrastructure investments are marked as described but undated in the consulted material.
- Consolidate repeated evidence limits into one closing paragraph → "Read an Ownership Transition" and "What the Comparison Teaches" merged into "Two Operating Questions"; the employee/customer and counterfactual limits now appear once at the end; qualifications stayed next to the $14bn, adjusted EBITDA, $2.75bn/$8.5bn and retirement figures.
- Finish with the two operating questions → chapter ends with the prescribed bolded sentences, then the handoff to [[visma]] phrased as the reader's next question (secondary sale, familiar manager, changed money).
- Move the final figure before the prose handoff → Figure 2 now precedes the closing evidence paragraph, the two questions and the handoff.
- eBay 2007 annotation → verified by WebFetch against the SEC release: €375m earn-out settlement plus an additional €630m impairment, total €1,005m (about $1.43bn at €1 = $1.41). Annotation now names the €630m as the additional impairment component distinct from the earn-out settlement.
- Keep 2013 IPO vs 2018 realization, the $8.5bn/$2.75bn warning and the IP settlement → all retained.
- Comic last panel names the two decisions → panel 6 caption/alt/prompt/dialogue rewritten ("Two cases, two different decisions."); the existing image (team placing decision maps beside documents) supports it, no regeneration needed. Panel 2 caption adds that the filing does not date the systems. Intro updated.
- Questions to Consider trimmed from six to four.
**Adapted:**
- Review suggested keeping Skype's later history as a short bounded subsection → kept "The Afterlife, and Its Limits" but compressed to two paragraphs.
**Declined:**
- None.
**Unresolved / needs separate action:**
- S25 (PEI retrospective PDF on blackstone.com) could not be refetched (Cloudflare 403 to WebFetch and curl); no claim sourced to it was changed.
- Figures 1 and 2 kept with unchanged captions; images still valid. No panels need regeneration.
**Verification:** eBay 2007 charge components verified against the SEC release; Hilton S-1 grepped for OnQ / $4.0 billion / April 2010 (all present; no system dates); summary word count 471 (figure and [S..] excluded); comic JSON parsed, captions and dialogue match across the four fields; cross-links [[visma]] resolve; timetoread recomputed to 10 min (about 2,070 prose words); build not run.


## 22-visma — Visma: Continuity of Manager Is Not Continuity of Money (`visma`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High impact: correct the ESMA annotation → replaced with the prescribed wording ("useful model … formal scope depends on the issuer, securities and disclosure; private share ownership alone does not establish an exemption"); scope paragraphs 1–5 of ESMA/2015/1415 read from the PDF (issuers with securities on a regulated market publishing regulated information under the Transparency Directive, and persons responsible for prospectuses; APMs inside financial statements excluded). No statement about Visma's legal status.
- Medium: transaction map → title KEPT. A five-row map (2006, 2014, 2017, 2023 plus a sources line) built only from S30 and Hg's June 2017 announcement, which is already in the article's To Probe Further. Hg's own text supplies Hg5 (2006, £101m), Hg7 (2014), KKR realizing its entire stake in 2017, Hg at 41% after 2017, management 7%, Cinven c.17%, GIC/Montagu/ICG committing direct capital, c.£1.4bn equity, NOK 45bn / $5.3bn EV; S30 supplies the €19bn valuation, >€1bn from ~20 new investors, ~€3bn from existing shareholders incl. Hg, ICG, TPG, management, Hg majority. Every cell neither document fills is marked "Not stated" (who sold in 2006/2014/2023, whether Hg5 sold in 2014, Hg fund names for 2017/2023, TPG entry date, money reaching the company in every round, how Hg went from 41% to a majority). The 2017 announcement is cited inline by title and link because it has no S-number; see Unresolved.
- Medium: connect the two lessons → the exact sentences "Continuity needs checking in the numbers as well as the ownership. The same year now appears under a different earnings definition." open the reconciliation section; the 33-acquisitions section now ends by making the acquisition pace the reason to read definitions.
- Medium: follow the bridge with the budget decision the adjustment cannot resolve → new paragraph after "Costs can be exceptional…" states the decision (recurrence of the €11.665m, integration funding, lender measure, cash plan in transactions/cost/engineer-weeks, accountable leader, approval authority), explicitly not an assertion about Visma's internal planning; links [[obligations-before-budget]].
- Medium: narrow the shared-services claim → now "a question the case raises, not a demonstrated success mechanism", with the corporate-group vs manager caution retained; comic panel 3 aligned.
- Low: shorten repeated evidence-boundary paragraphs → "What the Evidence Supports About Technology" and "Employees, Customers and Acquired Companies" merged into "What the Documents Cannot Establish"; "Recheck Authority…" and "What the Case Supports" merged into "One Authority-and-Budget Check".
- Home of the recurring-acquisition-adjustment lesson → explicit sentence "This chapter is the book's home for that lesson" with a link to [[teamsystem]].
- Comic panel 6 shows the specific resources/authority rechecked → caption/alt/prompt/dialogue rewritten to "which fund, which budget, which definition" (majority fund and horizon; shared-service and integration budget with accountable leader; earnings definition used by board, lenders and plan). Existing image (manager folder with three notebook tabs) supports it; no regeneration. Panel 2 now cites the two named funds and one exit; intro updated.
- Handoff to [[toys-r-us]] → phrased as the next question (positive operating earnings, too little cash after interest and capital spending).
- Questions to Consider trimmed from six to four; definitions kept beside the numbers; excerpt updated.
**Adapted:**
- Review's alternative title "Visma: Check What Continues Behind the Familiar Name" → not needed: the cited sources support a partial map with the manager/vehicle distinction visible (two named Hg funds, one full investor exit, changing stakes).
**Declined:**
- None.
**Unresolved / needs separate action:**
- Coordinator: the Hg June 26, 2017 announcement (https://hgcapital.com/insights/hg-leads-usd5-3bn-buyout-of-visma) is now used as evidence in the article and summary, not only as further reading; it needs a numbered bibliography entry (evidence type: interested investor transaction announcement; consulted for fund names, stakes, KKR exit, equity amounts, EV) and the two inline citations can then be converted to the [Sxx: …] form. WebFetch verbatim quotes were obtained on 2026-09-14.
- Figures 1 and 2 kept; Figure 2 caption extended with "and its cash plan"; images still valid. No panels need regeneration.
**Verification:** 892.646 + 11.665 = 904.311 rechecked; ESMA scope read from the PDF; S30 and Hg 2017 quoted verbatim by WebFetch; summary word count 492 (figure and [S..] excluded; the unnumbered Hg link counts as prose); comic JSON parsed, captions and dialogue match; cross-links [[acquisition-adds-work-first]], [[obligations-before-budget]], [[teamsystem]], [[toys-r-us]] resolve; timetoread recomputed to 12 min (about 2,330 prose words); build not run.


## 23-toys-r-us — Toys R Us: Positive Operating Earnings, Too Little Cash (`toys-r-us`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: correct the title and causal opening → retitled (permalink `toys-r-us`, id unchanged); the opening now uses the reviewer's formulation ("The documents consulted describe technology gaps and proposed investment alongside severe financing and liquidity pressures. They show why a transition needed funding; they do not establish that the proposed work was sufficient to restore competitiveness"); "its technology plans were reasonable in isolation" and "what constrained them was the financing" removed from index, summary and the comic introduction.
- High: add the net-loss measure with scope and period → financial table now carries both "Net loss, consolidated" (−$29m, after $34m income tax expense) and "Net loss attributable to Toys “R” Us, Inc." (−$36m, after $7m earnings attributable to noncontrolling interests), labelled fiscal 2016, year ended January 28, 2017, consolidated, US$ million; a paragraph explains the two scopes. Summary carries both figures. Comic panel 3 caption/prompt/dialogue now name the measure.
- High: repair the final cash-flow question → question 1 now asks for operating cash flow for the period, whether it already includes interest paid and working-capital movements, and capital expenditure separately; the body's warning against subtracting interest twice is kept.
- Medium: center the supplier feedback loop → new section "The Supplier Feedback Loop" gives the chain once as a numbered list (concern about survival → suppliers require earlier payment → immediate cash need rises → less room to fund the transition), each link labelled as management's report, not a court finding; the loop is previewed in the opening and in KEY POINTS; comic panel 4 caption/prompt updated to the chain.
- Medium: label the periods/scopes of the ~$400m debt service vs $90.4m technology program → compact table with amount, period and scope (funded debt at petition date; annual cash debt service as stated September 2017; $90.4m as a 2018–2021 total for one program; >$1bn liquidity estimate); the text says the point is a sequence, not a ratio.
- Medium: subordinate or remove the gross-debt/EBITDA ratio → the 6.8× illustration is removed; one sentence keeps the caution that no leverage multiple is computed and that any result would not be comparable to Visma's ratio ([[visma]] link kept).
- Low: combine the two application sections → "Transfer the Funding Question Carefully" and "Lessons for Product and Engineering Leaders" merged into "A Funded Transition Is Necessary, Not Sufficient", with links to [[obligations-before-budget]] (cash bridge) and [[the-financing-slipped]] (dated cash plan); necessary-vs-sufficient kept as the closing distinction; handoff to [[teamsystem]] now answers the reader's next question.
- Kept as the review asked: Hasbro's $49m bad-debt expense treated as included within the $60.4m; the court declaration described as the debtor's account, not a causal finding; e-commerce growth as evidence of online work, not competitive parity; the 2005–2017 evidence gap stated explicitly.
- Questions to Consider trimmed from 6 to 4.
**Adapted:**
- "Preview the cash shock earlier" → previewed in the third opening paragraph and KEY POINTS rather than restructuring the chronology, so the transaction → plan → finances → shock order the review called coherent is kept.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Figures 1 and 2 kept with captions unchanged; both still support the revised text. Summary figure kept.
- No comic panel needs regeneration; all edits are caption/prompt/alt/dialogue text the existing images can carry (panels 1, 3, 4, 6 edited; panels 2 and 5 unchanged).
- The 10-K (S34) remains partially accessed, as the bibliography states; nothing new was claimed from it.
**Verification:** Fiscal 2016 figures verified against the SEC earnings release (Exhibit 99.1, https://www.sec.gov/Archives/edgar/data/1005414/000100541417000010/truq4-16earningsreleaseexh.htm, fetched raw): operating earnings $460m; interest expense $457m; EBITDA $770m; Adjusted EBITDA $792m; net earnings (loss) $(29)m; net earnings attributable to noncontrolling interest $7m; net earnings (loss) attributable to Toys “R” Us, Inc. $(36)m; income tax expense $34m; net cash (used in) provided by operating activities $(1)m; capital expenditures $(252)m; net sales $11,540m, down $262m (2.2%); consolidated e-commerce sales +11%; fiscal year ended January 28, 2017. The release's own headline bullet uses the attributable $36m. Declaration figures ($5.265bn funded debt, ~$400m annual cash debt service, $90.4m 2018–2021 program, ~40% of vendors, >$1bn) are carried over from the already-cited S50 paragraphs, not re-fetched. Arithmetic rechecked. Cross-links: obligations-before-budget, the-financing-slipped, valuation-is-an-estimate, visma, teamsystem (all valid permalinks). Summary word count 490. timetoread recomputed at 200 wpm on body prose excluding To Probe Further (2,834 words → 14 min). Comic JSON validated (6 panels). Build not run.


## 25-teamsystem — TeamSystem: Each New Owner Inherits Progress and Unfinished Work (`teamsystem`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High: correct the 2024 further-reading annotation → now describes an agreed sale to Hellman & Friedman valuing the trust's investment at £24.3 million, completion subject to closing conditions, "an agreed value, not cash received, for a holding that had been added to since 2016". The body's partial-exit section adds a paragraph stating that the 2021 announcement (Hg's earlier fund sold its minority; the Trust invested ~£14.3m of new money) means the post-2021 holding is not the 2016 stake, so the 2024 figure does not close the 2016 retained-value question; a documented cash-and-holdings history would be needed. The 2021 annotation was rewritten to say the same. Comic panel 3 caption adds "a later agreed sale value is still not cash received".
- High: complete the adjusted-EBITDA-to-loss bridge → new table built only from the report's own reconciliation and income statement (S49, PDF pp. 10–11, 23 and 45): Adjusted EBITDA 113.010; less management "non-core" costs −20.342 (eight named lines plus four smaller items); less bad-debt allowance −3.896; less other provisions −7.028; less impairment −0.150; less D&A −72.459; operating result 9.137; less net finance cost −72.039 (finance income 7.618, finance cost 79.674, associates 0.016); loss before tax −62.903; plus net tax credit +6.115 (current −5.971, deferred +12.086); consolidated loss −56.788; attributable to owners −57.134 (after 0.346 NCI). Noncash charges vs cash needs distinguished, with the cash-flow statement's €15.7m tax paid, €61.8m operating cash flow and €25.3m capex (PDF p. 26). The directors' own explanation (amortization from the 2016 purchase-price allocation and finance costs on higher debt) is quoted as management's explanation. Summary carries the bridge in condensed form.
- Medium: ownership-episode table → added (owner, documented event, date/status, what the evidence establishes) for Palamon 2000–2004, Bain 2004–2010, Hg 2010, H&F 2015/2016, plus 2021, 2023 and 2024 rows explicitly marked as announcement-only and outside the 2000–2017 window; no multiples or ranking in the table.
- Medium: narrow the opening claim → "A buy-and-build strategy is set by investors and financed largely with debt…" removed from index, summary and comic introduction; replaced with the reviewer's formulation ("Each ownership change creates a new financial starting point. Product work carries on across it: migrations, integrations and dependencies remain somebody's responsibility").
- Low: title → retitled to "Each New Owner Inherits Progress and Unfinished Work" (permalink `teamsystem`, id unchanged).
- Structural (brief §1.5): recurring-acquisition-adjustment discussion shortened to one paragraph that links [[visma]] as the owner of that lesson; the chapter now concentrates on reporting periods and inherited work.
- Kept: 37.7% vs 8.9% comparable-period lesson with the warning that 8.9% is still not organic growth; capitalized development (€13.4m) vs cash; retained stake vs cash proceeds.
- Ending: "Keep the Operating History When the Owner Changes" and "What Company Leaders Can Take From This Case" combined into "What Each New Owner Inherits", linking [[handover-of-obligations]]; handoff to [[success-for-whom]] answers the next question; final sentence is the accumulation of products, knowledge, dependencies and continuing work. Comic panels 1, 4, 5, 6 captions updated to match; questions trimmed from 6 to 4.
**Adapted:**
- "Complete the bridge before interpreting why the gap matters" → the section order is comparable-period growth first, then the bridge, then the interpretation, so the two reporting-basis lessons sit together; the interpretation paragraph follows the completed table.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Completion of the 2021 co-investment, the 2023 Silver Lake investment and the 2024 sale was not verified; all three are labelled "completion not checked here" / "subject to closing conditions". The Silver Lake row rests on the buyer's announcement already cited in To Probe Further (not re-fetched in this pass).
- Interest actually paid in 2017 is not isolated in the cash-flow statement; the text says so rather than estimating it.
- Figures 1 and 2 and the summary figure kept; captions unchanged and still valid. No comic panel needs regeneration (text-only edits to panels 1, 3, 4, 5, 6; panel 2 unchanged).
- The chapter now links [[handover-of-obligations]] (new chapter) and expects it to carry the "consistent record of commitments, costs and actual outcomes across the handover".
**Verification:** S49 PDF downloaded and text-extracted; every bridge line, the 2016 statutory (229,395) and pro forma (290,143) revenue, 315,977 total revenue, the capitalized-development split (11,078 + 2,307 = 13,385) and the cash-flow lines were read from the report; arithmetic rechecked (component sums reproduce 113,010 and 169,798 to within €1–2 thousand of rounding, noted in the table). HgCapital Trust 8 July 2024 and 18 January 2021 announcements fetched: 2024 = agreed sale, £24.3m value vs £22.1m carrying value, "completion is subject to applicable closing conditions"; 2021 = Genesis 6 selling its minority to H&F IX, HGT investing ~£14.3m via Genesis 8, existing investment valued at £21.3m, Hg remaining a minority investor. Cross-links: acquisition-adds-work-first, valuation-is-an-estimate, obligations-before-budget, visma, handover-of-obligations, success-for-whom. Summary word count 483. timetoread recomputed at 200 wpm on body prose excluding To Probe Further (3,093 words → 15 min). Comic JSON validated (6 panels). Build not run.


## 24-success-for-whom — Success for Whom, and for How Long? (`success-for-whom`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Rebuild the opening around the cases and one final company decision → new lead names the five cases; new section "What the Cases Establish and Leave Unknown" carries a case × (investor result / company result / stakeholder evidence / not established) matrix filled only from the HEAD case chapters, with unknown cells stated as unknown; Toys R Us row names a reported net loss beside positive operating earnings and TeamSystem's 2024 stake sale is "announced", matching the parallel retitles.
- Apply the standard to a fictional decision with a real trade-off → new section "One Final Larkspur Decision": Option A (90-day cut-off of the manual onboarding path, about €220,000 a year saved; ten to twelve of thirty customers, the support team and the specialist lose), Option B chosen (two-quarter migration after the data-quality step, specialist retained then a funded half-time data service at about €70,000 a year, net saving about €150,000 a year from the following year), Option C rejected; the Larkspur board authorizes (not the investment committee), Priya/Alex/Sam accountable, Morgan advises; funded mitigation; recorded disagreement (Sam, Morgan vs Priya) with review evidence; closing decision-record table with chosen/rejected/funding/scarce capacity/authorized/evidence. All figures fictional and labelled; continuity with the shared D-3 → ONB-1 → day-100 chain.
- Correct "Investors measure success at the moment they realize value" → replaced in article lead, KEY POINTS, summary and comic intro with: an exit is a decisive reporting event for some investors, not their only measurement horizon; remaining estimated value and continued ownership are also measured (link [[three-different-returns]]; Visma and TeamSystem as sponsors staying invested).
- Keep employment and healthcare findings, shorten methodology → −12%/+15% (Davis et al. 2024 revision, 1980–2013), establishment vs firm boundary, Bernstein et al., Gupta et al., Kannan et al. 2023 (4.6 per 10,000; 25.4% relative, not percentage points), Bruch et al. 2020 and Kannan & Song 2025 (small-sample financial comparison, not patient outcomes) all retained; "What Wider Studies Add" and "Follow Outcomes Beyond the First Exit" compressed, definitions of comparison group / instrumental variable / generalizability reduced to one clause each; no separate evidence essay.
- Add a supplier row to the "Success for Whom?" table → row added (payment reliability; continuing obligations honored; terms that hold under stress; overturning question; Toys R Us tightened vendor terms and Hasbro bad debt named as the shape of the evidence).
- Fix source annotations → BMJ entry now "July 2023 … searches closed in April 2023 … maps the earlier literature … predates the December 2023 hospital study and the 2025 hospital-sale letter, so it does not synthesize them"; Cohn–Hotchkiss–Towery now "complementary evidence on buyouts of already private firms, the transaction type behind the +15% estimate the post takes from Davis and colleagues … with a limited role for financial engineering" (no "rather than").
- Clarify durable capability can include a deliberately funded continuing specialist service → stated in "What Durable Success Requires" with link [[useful-engagement]], and applied in the Larkspur decision (the specialist becomes a funded continuing service).
- Add a process for unresolved disagreement → subsection "When the Standard Does Not Settle the Question": authorized decision-maker ([[decide-who-decides]]), affected groups and who loses, funded or explicitly unfunded mitigation, review date and reopening evidence.
- Final call as a consequence of the worked judgment; concrete final sentence → closing section opens from the Larkspur decision; article and summary end with "The next team should inherit a company that can serve its customers, fund its obligations and explain what still needs to change."
- Link the new handover chapter → [[handover-of-obligations]] linked twice (Larkspur handover record; "Follow Outcomes Beyond the First Exit").
- Comic intro drops the realization-only framing → rewritten (text-only); Panel 1 caption adds suppliers, Panel 4 adds "Hand over the obligations with the company", Panel 5 adds "name who is authorized to decide and whose interests lose"; caption, prompt "Convey:" text and visible lines kept in agreement; JSON validated; six panels, images and "status": "generated" unchanged.
- Questions trimmed to four; excerpt updated; timetoread recomputed (2,561 prose words excluding tables and To Probe Further → 13 min).
- Spec: Intent rewritten for the synthesis + final decision; three success criteria added; changelog line added; status stays accepted; spec remains shorter than the post.
**Adapted:**
- "Relocate methodological exposition to a linked evidence essay" → shortened in place instead, per brief §1.6 (no separate essay); material findings and citations all kept.
- "Do not fill unknown cells with inferences" → matrix uses a "Not established" column with explicit gaps; the Toys R Us investor-result cell says the chapter reconstructs no sponsor return rather than estimating one.
**Declined:**
- None of the per-post recommendations declined.
**Unresolved / needs separate action:**
- No comic panel needs regeneration; existing images plausibly carry the revised captions. Figures 1 and 2 kept with unchanged captions (Figure 1 already depicts suppliers).
- Toys R Us net loss is named without a figure (the parallel Toys R Us revision supplies the number); Visma ESMA wording and TeamSystem "announced" status taken from the brief, not re-verified here.
- Article prose grew from about 1,760 to about 2,560 words (matrix and worked decision); coordinator may want a further trim if the finale should stay under 12 minutes.
**Verification:** Larkspur arithmetic rechecked (€220,000 − €70,000 = €150,000; 8 engineer-weeks; 30 customers, 10–12 nonstandard, 15-customer review threshold); all twelve [[…]] targets resolve against current permalinks plus handover-of-obligations; case figures in the matrix cross-checked against the HEAD case chapters (Hilton 3.1×/$14bn/$4.0bn; Skype $2.75bn/$8.5bn/$860m/$264m/−$7m; Visma €19bn/€2,804m/€893m/€904m/2.5×/33; Toys R Us $460m/$770m/−$1m/$5.265bn/$400m/33,000/40%/$60.4m/$49m; TeamSystem 4.1×/£39m/£6.1m/1.8×/€315.977m/€113.010m/−€56.788m/€13.4m/€80m); BMJ review verified via PMC copy (published 19 July 2023, 55 studies, searches 9 June 2022 and 16 April 2023; bmj.com returned 403); Cohn–Hotchkiss–Towery abstract verified at OUP ("relaxing financing constraints … improving the performance of weak firms, while financial engineering plays a limited role"); research numbers unchanged from the reviewed text (review confirmed them against NBER/JAMA); summary word count 499; comic JSON parsed; build not run.


## toolkit — Practical Tools for Ownership and Technology Decisions (`toolkit`)

**Files changed:** index.md, spec.md
**Implemented:**
- Remove the orphan "optional appendix" sentence → removed from the introduction; no destination substituted.
- Supply one completed chain using existing tools (high) → new section "One Finding, Followed Through" (fictional, Larkspur): Stage 1 finding D-3 as a filled Tool 3 record (observed / reported / inferred / not established, agreed response, approvers, Priya handoff, day-90 review); Stage 2 Tool 12 option rows (hire two specialists ≈ €300,000 a year; pilot €180,000 + €30,000 a year + 12 engineer-weeks; narrow segment) with the authorized combination, authority and evidence that would change it; Stage 3 Tool 5 shown as a two-column table, **pending** (the old proposal, relabelled) beside **authorized** (Priya accountable; €180,000 committed, about €90,000 in the period; 12 of 24 engineer-weeks; baseline from actual records by day 20; day-90 cohort review; board approval recorded at the meeting that authorized the envelope; options rejected; evidence that would change it); Stage 4 Tool 6 ledger at day 100 (cohort of eight, 80 → 62 hours, ~40% of remaining hours from customer data quality, waiting time unchanged, capacity not cash, no financial line changed); Stage 5 revised decision (data-quality step €40,000 / 4 engineer-weeks from the reserve, expansion deferred a quarter, hiring deferred, alternatives rejected, evidence to change); Stage 6 Tool 10 handover entry carrying D-3/ONB-1 with baseline, actual cost, observed result and open work; closing "What Each Stage Added" paragraph.
- Clarify sponsor terminology (high) → Tool 4 now names the "investor-side sponsor" and a separate "accountable company leader"; "engagement sponsor" removed.
- Reconcile responsibility terms → "decision owner", "funding owner", "responsible person", "knowledge owners", "contract owner", "owner of the next decision" replaced with "accountable company leader" / "who commits the cash" / "people who hold critical knowledge" / "who is accountable for the next decision"; "Owners" row and Tool 1 heading changed to "Shareholders"; the definitions paragraph states that "shareholder" is ownership and no person is the "owner" of a decision.
- Organize tools by decision stage and add section links (medium) → "Minimum Use" paragraph plus a stage-grouped table (map → investigate → compare options → commit → obtain help → measure → revise or hand over) with the teaching chapter per row; Tool 12 precedes Tool 5 and the text says why; tool numbers and physical section order unchanged.
- Show which records can be combined (medium) → "Minimum Use" (one evolving page per finding/initiative), "What Each Stage Added", and a closing "Combining and Revising Records" section that says which fields Tools 2/3/5, 6/7 and 10/1 share and to reference by identifier instead of copying.
- Make Tool 4 usable for a continuing service (medium) → added recurring cost and budget, accountable company leader, review cadence and evidence, and an exit/continuity plan; states that a deliberately funded continuing specialist service is a legitimate outcome and that capability left with the company does not require internalizing every specialty.
- Link Tool 11 to Growth Into Design (low) → Tool 11 now names [[growth-into-design]] as its main application, with [[valuation-is-an-estimate]] as vocabulary; navigation table row added.
- Tool 10 links → now links [[handover-of-obligations]] (what travels with the work) and [[the-financing-slipped]] (delayed-event plan), plus [[diligence-corrects-the-plan]].
- Spec → revised 2026-09-14, Intent widened to the completed chain, success criteria extended (terminology, navigation, example chain, combination guidance, no new templates), Changelog line added; status stays accepted.
**Adapted:**
- Direct section links in the navigation table → `_templates/post.html` renders headings as plain `<h2>` without ids (line ~479: `'<h' + level + '>' + inline(text)`), so no anchors were used; the table says "see Tool N below" as instructed. Anchors would need a template change (heading id generation) or raw-HTML `<a id>` markers in headings; not done here.
- Tool 11 "belongs near the initiative/design decision" → moved in the grouped navigation (Compare options stage) rather than renumbered, to keep tool numbers stable.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Figure 1 and Figure 2 kept; captions extended to point at the pending → authorized move and the D-3/ONB-1 loop. Images still valid; no regeneration needed.
- Board approval "date" for ONB-1 is expressed as "the board meeting that authorized the first-hundred-days envelope" with Priya's acceptance within ten days of closing — no calendar date exists in the brief, so none was invented. If chapter 17 fixes a date, the toolkit's Stage 3 row can copy it.
- Chapter 16 says the toolkit "shows the finding record, the thesis page and the initiative record moving through the same stages"; the toolkit chain shows the finding and initiative records in full and mentions the thesis (Tool 2) only as the page whose constraint line points at D-3. Acceptable as written; flag if chapter 16 expects a filled thesis example.
- Front matter `timetoread:` added ("30 min", 6,036 body words at 200 wpm); the toolkit previously had none.
**Verification:** arithmetic rechecked (envelope 180 + 0 + 80 = 260 of 300; 12 + 4 + 4 = 20 of 24; reserve 40 / 4 fully used by the data-quality step; 80 − 62 = 18 hours × 8 = 144; 1,800-hour figure labelled a projection); all 18 `[[…]]` targets are current permalinks or the new `handover-of-obligations`; stale terms grep-checked (decision owner / funding owner / engagement sponsor / responsible person / appendix: 0 hits); spec (≈600 words) shorter than post; build not run.


## fund-economics — Fund Economics: Fees, Distributions and Performance Reports (`fund-economics`)

**Files changed:** index.md (new), spec.md (new). No summary.md or comics.md by design. Not added to config.yaml (coordinator).
**Implemented:**
- Create the optional reference (brief §1.2) → Front matter: title, date 2026-09-14, author "Owned working manuscript", one-sentence excerpt, permalink `fund-economics`, timetoread 7 min; no logo/icon. Opens with a three-bullet KEY POINTS block and a paragraph stating it is optional depth for the fund-side mechanics behind [[announcement-is-not-a-budget]] and [[three-different-returns]] in Part I, with a [[glossary]] pointer.
- Section "How Fees and Profit Sharing Work" → Text and €160-on-€100 waterfall table taken from HEAD of 01-announcement-is-not-a-budget ("How Fees and Profit Sharing Work"), definitions of preferred return, catch-up and clawback and the S01 SEC conflicts paragraph preserved. Added a labelled sub-section "How the Three Terms Change the Example" that extends the same €160 with an illustrative €8 hurdle: no catch-up → LPs €149.60 / GP €10.40; full catch-up → LPs €148 / GP €12; clawback explained in words.
- Section "Reading a Fund Performance Report" → Text and €100/€60/€90 DPI 0.6× / RVPI 0.9× / TVPI 1.5× table taken from HEAD of 02-three-different-returns, gross/net and subscription-line paragraphs preserved with [S05: ILPA performance guidance]; one added clause defines IRR in passing and points to [[three-different-returns]] since the moved text used the term.
- Section "What This Means for the Company Leader" → Three short paragraphs: fund incentives can shape the timing and kind of requests (link [[different-bets]], [[announcement-is-not-a-budget]]); a valuation increase pays nobody until realized, with the brief's commitment states (expression of interest / contractual commitment with conditions / received); received vs estimated value in the company's own plans.
- spec.md → toolkit/spec.md structure; status accepted; revised 2026-09-14; Changelog "2026-09-14: Created as an optional fund-economics reference receiving material moved from the announcement and returns chapters."
**Adapted:**
- None.
**Declined:**
- None.
**Unresolved / needs separate action:**
- Coordinator: add `fund-economics/index.md` to config.yaml under Reference Material after the toolkit; glossary already defines every term used here.
- The 02-three-different-returns agent is expected to remove "Reading a Fund Performance Report" and link [[fund-economics]]; this page does not depend on that.
- No figures or images; none needed.
**Verification:** waterfall arithmetic rechecked (base: 100 + 12 + 48 = 160; hurdle without catch-up: 100 + 8 + 41.60 + 10.40 = 160; with full catch-up: 100 + 8 + 2 + 40 + 10 = 160, GP 12 = 20% of 60); DPI/RVPI/TVPI rechecked (0.6 + 0.9 = 1.5); all [[…]] targets resolve; body 1434 words including tables, 1312 prose → timetoread 7 min; build not run.


## glossary — Glossary (`glossary`)

**Files changed:** index.md, spec.md (no summary.md or comics.md exist)
**Implemented:**
- Establish and apply a collection-wide terminology sheet (high) → glossary now defines, once each, every entry in the brief's §2 sheet: Investor / Investment firm (manager) / Fund / The company; Shareholder vs Accountable company leader; Financial sponsor / Investor-side sponsor / Company sponsor (plus a general "Engagement sponsor" row that says to name which); the four funding states (Expression of interest → Approval pending → Contractual commitment → Cash received) with Conditional commitment as the company-side promise; Earnings / profit, Operating profit, Consolidated / attributable and a section rule "name the measure, scope and period"; Financial contribution vs Causal contribution (each cross-references the other); End-to-end work lead time vs DORA change lead time; Capability left with the company and Continuing specialist service as a legitimate outcome; Investment thesis as a revisable prediction; Durable value labelled as the author's proposed standard; Investor's technology adviser (general) vs Technology Principal (this book's supplied example, Morgan); Investment committee vs Board of directors; Announced transaction value / received proceeds; Retained investment value. The how-to-use paragraph states that the glossary is the standard and chapters are corrected to match it.
- Split overloaded rows and add alphabetical access (medium) → "How to Use This Glossary" paragraph plus an alphabetical index (279 entries, grouped by letter, abbreviations listed under their own letters) inserted before the thematic sections. In-page links are supported: `post.html` passes raw HTML through and its hash handler preserves non-tab anchors, so each section heading carries an explicit `<a id="…">` and index entries link to `#funding`, `#arrangements`, `#organizations`, `#roles`, `#earnings`, `#returns`, `#transactions`, `#choosing`, `#technology`, `#evidence`, `#proposed`. Split rows: Preference / Dilution / Leaver provisions; AI system / Generative AI / Model inference; SaaS / IT / IP; Management rollover / Management equity; Turnaround / Restructuring; Chapter 11 / Liquidation; Investment period / Fund term; Maturity / Refinancing; Deployment / the two lead times; SPACE / DORA; Cloud / Managed service; FinOps / Unit economics; Rightsizing / Latency; Security / Resilience-recovery; Architecture / Interface; Governance / Decision rights / Reserved matters; Baseline / Cohort; Materiality / Confidence; Attribution / Causal contribution. Close contrasts kept paired (Gross return / net return, Pre-money / post-money, Modularity / coupling, Correlation / causation, Percentage / percentage point, Observation / assertion / inference).
- Broaden or qualify AI (medium) → AI system row now follows the OECD wording ("machine-based system that, for explicit or implicit objectives, infers from the input it receives how to generate outputs such as predictions, content, recommendations or decisions"), states that it covers learned and knowledge-based approaches and that the book mainly discusses learning-based systems; Generative AI and Model inference are separate rows.
- Remove unsupported scope remnants (medium) → "Productscapes / accelerator" row deleted; it remains in the bibliography as P02 provenance.
- Add targeted chapter links beside easily confused terms (low) → Cash conversion → [[toys-r-us]], [[obligations-before-budget]]; Conditional commitment → [[the-financing-slipped]], [[decide-who-decides]]; Adjusted EBITDA → [[teamsystem]], [[valuation-is-an-estimate]]; Retained investment value and Announced value → [[teamsystem]], [[fund-economics]]; DPI/RVPI/TVPI, waterfall, preferred return, catch-up, clawback, subscription line → section-level pointer to [[fund-economics]]; Handover → [[handover-of-obligations]]; lead times → [[can-the-team-deliver]]; Recovery objective → [[prove-you-can-restore]]; Unit economics → [[cheaper-cloud-bill]]; Buy-and-build → [[acquisition-adds-work-first]].
- "Asset / liability" kept as a labelled teaching description; Microservices row no longer implies every service is automatically independently operable.
- Avoid repeating citations per row → the SPACE, DORA, FinOps and NIST citations moved from rows to the Technology section note; the Visma ARR citation stays on its single row because it is the only row that needs it.
- Retitled chapters → the glossary names chapters only via [[…]] links, which update automatically; no prose title mentions needed fixing.
- spec.md → revised 2026-09-14; Intent, Success criteria, Decision log and Changelog updated; status stays accepted.
**Adapted:**
- "Alphabetical index linking to sections or entries" → links go to sections, not individual rows (the renderer generates no per-row ids and per-row anchors would bloat 270 table cells); each index entry names the section so the reader lands within one screen of the term.
- "Existing thematic sections with smaller entries → author's evaluative terms" → added one new thematic section, "Roles, Authority and Sponsors", so the sponsor trio, investment committee vs board, adviser vs Technology Principal and shareholder vs accountable leader sit together; ended with "Terms This Book Proposes" (Durable value, Ownership cycle, Engagement charter).
- Engagement sponsor consistency → general "Engagement sponsor" row kept and two labelled variants added; the "Investor-side sponsor" row notes that Tool 4 names this role explicitly (the toolkit/engagement chapter should adopt the "investor-side sponsor" label — coordinator to confirm after those agents finish).
**Declined:**
- None.
**Unresolved / needs separate action:**
- The OECD citation is a plain link, not an S-numbered entry; the bibliography owner should register it (Explanatory Memorandum on the Updated OECD Definition of an AI System, OECD AI Papers No. 8, March 2024) if S-numbering is wanted.
- Entries for [[handover-of-obligations]] and [[fund-economics]] assume those posts exist at build time (config.yaml already lists them); if either folder is missing at build, the links render as literal `[[…]]`.
- "Retained investment value" is defined here but does not yet appear verbatim in any chapter (grep at HEAD); the TeamSystem agent should use this phrase.
- Front matter has no `timetoread:`; none was present before, so none was added.
**Verification:** OECD memorandum fetched and read (pages 1–8 of the saved PDF): the updated definition on p. 4/6 matches the row wording, and p. 6 states the term encompasses "machine learning and knowledge-based approaches"; all 30 distinct [[…]] targets checked against current permalinks plus the two new ones — none unresolved; all 279 index links resolve to the 11 section anchors; `_ASSET_REF` confirmed not to rewrite `href="#…"`; no summary (no word count); build not run.


## bibliography — Bibliography and Evidence Guide (`bibliography`)

**Files changed:** index.md, spec.md; created `_journals/private-techuity/_research/bibliography-revision-history.md` (outside the site build) and added one link line to `_journals/private-techuity/_research/README.md`
**Implemented:**
- Replace process history with present-tense scope (medium) → opening now reads "Sources were consulted on September 12–13, 2026. Each entry states the version and the material consulted; access to a document does not imply that every page was reviewed"; "What Supports the Broader Ownership Frame" replaced by a present-tense paragraph under the topic index. Entry-level dates that affect interpretation retained (S01, S06, S07, S19, S22, S33, S34, S52 rechecks); "research pass two" / "editorial review" wording inside those entries reworded to dated rechecks without changing substance. Chronology (which revision added S54–S57, S58–S61, which rechecks) moved to `_research/bibliography-revision-history.md`.
- Add a topic index and "Used in" chapter links (medium) → topic-index table near the top (valuation and returns; cash and financing; governance and incentives; delivery, architecture and cloud; security and resilience; AI evidence; support and advisers; the four cases; wider research on outcomes) with identifiers and start-with chapters; every S/P entry now ends with a `**Used in:**` line of `[[permalink]]` links derived by grepping `[S<nn>:` across `posts/*/index.md` (glossary included where it cites). Identifiers unchanged; S38 left absent and the page says so.
- Separate proposed methods from empirical validation once (medium) → new one-paragraph section "Proposed Methods and Empirical Evidence"; the repeated warnings in the opening, the ownership-frame section and the closing section removed. Entry-level notes (S05, S16, P02) untouched.
- Harmonize entry formatting and remove duplicate closing instructions (low) → S58–S61 citation lines unbolded, "Consulted scope and limits" → "Consulted scope", dates in the September-13-2026 style of S54–S57; "How to Read an Entry" and "How to use the evidence" merged into "How to Read and Use an Entry"; residual limits kept in a short "Remaining Research Limits" section.
- P01/P02 role (review detail) → both kept with their limits; P02 gets one sentence stating it is an intellectual input to the support/role chapters, not a reader-facing model, and that no chapter cites it directly.
**Adapted:**
- Bring the further-reading claims under the same evidence discipline (high) → on this page: added "Evidence Used Versus Further Reading", stating that chapter-end lists are optional reading whose annotations were checked for scope, are not part of the register unless an S identifier exists, and that listing does not mean the author consulted them. The chapter-side annotation corrections (TeamSystem 2024 note, unicorn study, ESMA scope, finale notes) are being made by the chapter agents; no entries were added or registered from those lists, per the brief.
**Declined:**
- None.
**Unresolved / needs separate action:**
- "Used in" lines list both old and new homes where the citing text is moving in this revision; coordinator to recheck after the build: S01 ([[announcement-is-not-a-budget]] / [[fund-economics]] — fee section), S05 ([[three-different-returns]] / [[fund-economics]] — fund-report section), S02, S24, S30 ([[the-financing-slipped]] / [[handover-of-obligations]] — the "A Sale Is Not Always the End" section). If a chapter drops its citation, remove that link. A one-line grep to regenerate the map is in the scratchpad script `rewrite_bib.py` (the `used` dict).
- Topic-index "Start with" column links [[fund-economics]]; valid only once that post exists in config.
- No timetoread field exists on this page; none added.
**Verification:** 62 entries, 62 "Used in" lines; no "revision / research pass / editorial review" wording remains outside the S08 title and the closing pointer to working notes; all consultation-note substance preserved (diff limited to formatting, date style and the seven rewordings listed above); cross-link targets checked against current permalinks plus the two new ones; spec revised 2026-09-14 with Changelog line; build not run.


## Open items after this pass

- **Images that need regeneration** (text updated, `needs_regeneration: true` in the panel JSON; no image-generation key was available in this pass): three-different-returns panel 4; roadmap-to-revenue panel 2; can-the-team-deliver panel 4; investors-adviser panels 2 and 6; the-financing-slipped panels 2, 3 and 4; useful-engagement panel 6.
- **New pages without visual assets:** `handover-of-obligations` needs its six-panel comic, header logo and navigation icon; `fund-economics` needs a header logo and icon. Both are configured and build correctly without them.
- **Verification that could not be completed:** completion of the 2021, 2023 and 2024 TeamSystem transactions (described as announced only); S25 (PEI Hilton retrospective) could not be refetched (no claim sourced to it was changed); the interest actually paid by TeamSystem in 2017 is not isolated in the cash-flow statement (stated, not estimated).
- **Declined for lack of evidence:** a documented venture funding-delay or corporate-ownership case (collection review). The evidence-scope disclosure remains in the guide, Part VI introduction and bibliography.
- **Optional further trims:** several articles grew because the reviews asked for completed decisions (AI strategy 15 min, growth-into-design 16 min, valuation 16 min, obligations 15 min, TeamSystem 15 min). Restatement was cut, but a further length pass is at the author's discretion.


---

# Revision log — OWNED editorial revision of 15 September 2026

This pass implements the reassessed reviews dated 14–15 September 2026 (collection `REVIEW.md` and the 41 per-post `REVIEW.md` files, which are unchanged and remain the independent baseline). It was coordinated as one pass with one agent per post, run in dependency order: standalone chapters first, then the shared-scenario clusters after a canonical record was fixed, then the reading guide, Part V introduction, toolkit and bibliography. Every per-post entry below is the agent's own report of what changed, what was adapted or declined, what stays unresolved and what was verified; the coordinator checked cross-links, summary lengths, comic metadata, the build and the shared figures across posts.

## Collection-level decisions

- **One canonical shared-scenario record.** Two read-only inventories of every passage carrying the shared Larkspur examples showed the chain could not be reconciled sentence by sentence, so the coordinator fixed one dated ledger before any of those chapters was edited. It is kept in `_journals/private-techuity/_research/shared-scenario-record.md` (outside the site build). The decisions that changed text: the first-hundred-days envelope is **€500,000 and 24 engineer-weeks** (the allocation chapter's figure), so the allocation, early-plan, recovery, toolkit and handover chapters now describe one plan; KNW-1 is four protected specialist-weeks outside the 24; portal research (€20,000 / 2 weeks) is a funded plan line; the REC-1 correction and retest cost **€20,000 / 2 weeks from the reserve, approved by the board around day 47**; the day-100 data-quality step uses the last four weeks and €40,000, leaving **€160,000 and no uncommitted weeks**; ONB-1 is **€180,000 committed, about €90,000 incurred by day 100, €90,000 payable over the next two quarters**, with €30,000/yr maintenance from the operating budget from the next financial year; the day-20 baseline is reconstructed from the twelve implementations of the previous two quarters; Priya measures the cohort at day 90 and the board decides at day 100 under one pre-set rule (**< 60 h green, 60–70 h amber, > 70 h or no reduction red**; 62 h is amber); gate 2 at month six is ≤ 50 h with waiting time down; the expansion decision moves to the next quarterly review (≈ day 190) and expansion is not before month 13; the delegation rule is that Ines authorizes spending inside the approved plan while reserve draws, changes to what the envelope funds and hires outside the headcount plan are the board's.
- **Pilot cost basis and the funding-choice loan.** €75/h fully loaded, 2,000 hours per FTE-year, so an implementation specialist costs €150,000 a year and two cost €300,000; the pilot is €180,000 build plus €30,000/yr maintenance everywhere (the obligations chapter's €200,000 aligned); released staff time is capacity until a dated conversion is evidenced. The funding-choice loan is a **four-year** €750,000 term loan at 8% with a one-year principal holiday (payments €60,000 / €310,000 / €290,000 / €270,000, closing at zero) tested against €350,000 of operating cash alone.
- **Finale cost split.** The €220,000 is €150,000 of specialist payroll (cash, ending only when protected customer contracts allow) plus €70,000 of released support time (capacity); Option A as written is inadmissible under the scenario's own contract rule; Option B saves €80,000 of cash from year two after ≈€75,000 of one-off specialist retention.
- **The financing-delay chapter is a separate scenario.** It keeps its own cash, burn, hires and dates, no longer uses the shared identifiers or ledger figures, and says so; the reading guide, Part V introduction, handover chapter and toolkit describe the chain as diligence → early plan → handover, with earlier pilot and support episodes in Parts III–IV.
- **Investor callouts.** Kept where they name a financing or governance consequence, shortened or reworded where they restated the learning outcome or reintroduced a universal claim; "the investor reports to its investors" became a fund manager reporting to its fund's investors where that is the actor.
- **Confirmed factual corrections.** Unicorn study: reported valuations average about 50% above modelled fair value (NBER version; the published JFE version says 48%). Fund catch-up: a slower catch-up changes timing, not necessarily the final split. TeamSystem: the €72.0m net finance charge is an accounting figure; €52.1m of finance costs were paid (Note 10), and the 2024 £34.189m gross realization proceeds are reported separately from the £24.3m July announcement, neither a net distribution. Hilton's OnQ is dated to 2003/2005 pre-buyout filings; Skype's Qik acquisition and group video calling to January 2011 (S-1/A).
- **Summaries.** All 30 are within 466–500 words by the collection's counter after the pass (the coordinator trimmed the adviser and financing-delay summaries by a few words at the end).
- **Rate-limit interruptions.** Two waves of agents were terminated mid-task by API session limits; the coordinator relaunched each post with an instruction to inspect the diff and complete the work, and the per-post entries describe the total change against the manuscript at `ab7a8f4`. The author's intermediate commit `4bd1d51` ("private techuity first draft", 12:32) captured part of the work in progress, including a site build; later agents verified that work against the canonical record rather than redoing it.

## Coordinator-level pages

### Journal workspace
- `_research/shared-scenario-record.md` created and listed in `_research/README.md`.
- No change to `config.yaml`, `README.md`, `STRUCTURE.md` or `index.md` of the journal.

## Per-post records (reading order)

## reading-guide — OWNED — Reading Guide (`reading-guide`)

**Files changed:** index.md, spec.md
**Implemented:**
- Medium — correct the shared-scenario promise → "How the Parts Build": Part V follows one finding from diligence into a funded early plan, its review and a handover; its delayed-financing chapter is a separate illustration. "Meet the Fictional Company": a paragraph maps the chain by chapter (16 → 17 → 31; the same initiative and recovery test in 11, 29, 30; the toolkit's stage record) and names 18 as separate with its own cash, burn, hires and dates; the "figures do not combine into one set of accounts" rule leads the paragraph with "One chain is a deliberate exception, and it is the only one."
- Medium — format equivalence → formats are companions, not substitutes; each keeps the conditions that decide whether the decision holds; a sentence records that summaries and comics are still being reconciled and the article governs on disagreement (to be removed once the sibling comic corrections land); the 29-of-30 comic disclosure kept.
- Low — To Probe Further reconciled with the bibliography's policy (a few resources appear in both places).
- Low — immediate routes selective ("If your decision is…"); customer-versus-investor route extended to [[success-for-whom]].
- Spec revised 2026-09-15 with two success-criteria lines.
**Adapted:** scenario correction written as a paragraph rather than the review's single sentence; format caveat made a reader-facing precedence rule.
**Declined:** none.
**Unresolved / needs separate action:** remove the "still being reconciled" caveat once 18 panel 3 and 23 panel 3 artwork is regenerated; 31 still has no comic.
**Verification:** chain checked against chapters 16, 17, 31, 18 and identifiers in 11, 29, 30, toolkit; 30 summaries / 29 comics recounted; bibliography policy line 65 confirmed (S62 dual listing); 77 cross-links, 0 unresolved; contents list re-derived from config.yaml (40 links in configured order). Body 1,654 → 1,887 words. Build not run.

## part-1-intro — PART I (`part-1`)
**Files changed:** index.md, spec.md
**Implemented:** Low — name the parties in the fund-commitment wording → "capital that a fund's investors have committed to the fund, and that its manager may not yet have called, is not cash in the company's budget". Low — conditional framing preserved. Spec revised 2026-09-15.
**Adapted:** folded into the existing three-part list. **Declined:** none. **Unresolved:** none.
**Verification:** seven links resolve; 468 words.

## part-2-intro — PART II (`part-2`)
**Files changed:** index.md, spec.md
**Implemented:** Medium — distinguish an advisory role from authority → "an adviser may have access and weight without any decision right … establish what authority, if any, accompanies the role". Low — broaden the source-of-right check → "identify the agreement, delegation or applicable rule that establishes the right; a job title settles nothing". Spec revised.
**Adapted:** merged into one passage. **Declined:** none. **Unresolved:** adviser chapter's High finding handled by its own agent; no conflicting claim remains here.
**Verification:** three links resolve; 05's authority-source wording checked; 412 words.

## part-3-intro — PART III (`part-3`)
**Files changed:** index.md, spec.md
**Implemented:** Low — widen the handoff to Part IV → "help from the investor or another source". Low — learning path kept at its present level of detail (no figures on the page). Spec revised.
**Adapted/Declined:** none. **Unresolved:** none; chapter one-liners hold under CANONICAL.md.
**Verification:** nine links resolve; 485 words.

## part-4-intro — PART IV (`part-4`)
**Files changed:** none.
**Implemented:** three distinct chapter jobs and the continuing-service allowance confirmed intact.
**Declined:** the conditional shortening of the "By the end" paragraph (review judges the repetition small; spec requires the outcome statement).
**Verification:** three links resolve.

## part-6-intro — PART VI (`part-6`)
**Files changed:** index.md, spec.md
**Implemented:** Medium — recheck the case windows → Hilton 2007–2018 with OnQ dated by 2003/2005 filings; Skype 2009–2011 with dated technology steps and later product history to 2025; Visma ownership episodes 2006 to the December 2023 secondary sale, financial comparison centered on 2024; Toys R Us transaction 2005, evidence mainly fiscal 2016 and the September 2017 filing; TeamSystem 2000–2017 in detail, later events to 2024 including the realization reported by the selling trust. Low — "kept apart throughout" → "Read management's account, sponsor claims and the author's inference separately." Spec revised.
**Adapted:** windows stated as periods and evidence types; no figures repeated. **Declined:** none.
**Unresolved / needs separate action:** body now 543 words including the case-map table; the spec's under-400-word cap on framing prose was already exceeded before this pass — flagged for the author.
**Verification:** windows checked against chapters 21, 22, 23, 25 and their cited primary sources; six links resolve.

## part-5-intro — PART V — Leading Through Funding and Ownership Changes (`part-5`)
**Files changed:** index.md, spec.md
**Implemented:** Medium — correct the learning outcome, the Learning Path and the conclusion together → highlight uses the review's wording verbatim ("One onboarding finding travels from diligence into a funded plan and its handover. A separate financing-delay example shows how to revise commitments when the expected money moves."); Learning Path says the pilot and support chapters of Parts III and IV and the toolkit follow the same finding and the financing-delay chapter uses a separate scenario with its own cash and dates; the [[the-financing-slipped]] bullet drops "September to December" for the chapter's job; the [[handover-of-obligations]] bullet carries the record into the next event; conclusion: "carry one body of evidence from diligence to handover". Low — one nonlinearity statement kept. Spec revised 2026-09-15.
**Adapted:** chapters described at job level only. **Declined:** none.
**Unresolved / needs separate action:** reading guide lines 60 and 73 still state the old integration (reading-guide agent). Body 468 words vs the spec's ~400 cap, which HEAD already exceeded.
**Verification:** four cross-links resolve; 18's separate-scenario sentence confirmed.

## 00-customers-lenders-investors — Customers, Lenders and Investors: What Each Expects in Return (`customers-lenders-investors`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — correct the new investor callout → "Lenders are investors too. Equity investors expect the share rights they negotiated; lenders expect the repayment and protections in their contracts; each prices those terms in negotiation." Borrowing definition cites Investor.gov's bond page; one sentence reconciles the book's usage with the title (unqualified "investor" usually means a shareholder or the fund behind one). Summary matched.
- Medium — repair the decision's authority and fallback logic → authority follows the instrument: borrowing and share issues are board decisions (share issue also needs shareholders' consent); the customer contracts sit within Ines's delegation, and she takes the comparison to the board voluntarily. Loan rejected on numbers (≈€3,040/month is twice the €1,500/month surplus). New "What would reopen it": fewer than three signatures by 15 January or an estimate above twelve engineer-weeks pauses the commitment; with two signatures (€66,700) Larkspur borrows the gap only if repayments fit the surplus (a €35,000 loan ≈ €1,065/month fits; the full €100,000 does not), and that borrowing is the board's decision. Summary and comic panel 6 caption match.
- Medium — make the share and prepayment assumptions explicit → 1,000 shares before the issue, investor holds 111 of 1,111 (≈10%); prepayment assumptions stated (standard annual price, no discount, exposure one month's refund ≈€8,300; a 10% discount ≈€10,000 would exceed the loan's ≈€9,500 interest and change the ranking); loan "36 months … excluding fees".
- Low — tighten the setup (asset sale explicitly drops out; intro no longer restates KEY POINTS).
- Robb–Robinson annotation → "often supported by founders' personal assets or guarantees". timetoread 8 → 10 min. Spec revised.
**Adapted:** cash/payroll reconciliation (the €100,000 covers finishing and onboarding before subscriptions pay; surplus has nothing for new work); Investor.gov cited as a plain link; summary trimmed from 546 to 499 words.
**Declined:** Low — comic payoff (show competing obligations earlier); no dialogue changed.
**Unresolved / needs separate action:** bibliography could S-number the Investor.gov bonds link; glossary "audited financial statements" entry (now added by the glossary agent); title juxtaposition reconciled in the body rather than by retitling.
**Verification:** annuity arithmetic (€100,000 at 6%/36 months → €3,042; interest ≈€9,500; €35,000 → €1,065; ⅔ × €100,000 ≈ €66,700; €100,000/12 ≈ €8,333; 111/1,111 = 9.99%). Investor.gov page fetched via curl. 05 and 04 terminology read and consistent. Summary 499 words. Four cross-links resolve. Six comic JSON blocks parse. Build not run.

## 01-announcement-is-not-a-budget — An Investment Announcement Is Not a Budget (`announcement-is-not-a-budget`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — stop changing the meaning of the €100 million → opening now says the headline may be a value placed on the whole company or the amount that changes hands, that the two can differ, and that only the primary part (newly issued shares; glossary terms primary share issue / secondary share sale), after costs, reaches the company at closing. Closing: "A headline may name transaction consideration, new funding or a valuation, and the three can differ." Summary and comic intro match.
- Medium — reconcile the hiring record and its decision paragraph → one chronology: subscription agreement signed 20 September (commitment, not cash); €8m received at closing 3 October; €0.4m costs; €7.6m net; board approves the year-one plan 10 October (four hires); record 11 October; Ines authorizes three offers 12 October. Two reserved matters named: spending above €250,000 outside the plan, and any increase in approved headcount. A fifth hire at ≈€100,000 is below the spending threshold, so the headcount rule required investor-director consent. Summary and comic panel 6 caption match.
- Medium — define the cash trigger as a forecast variance → "cash at a quarter end more than €300,000 below the approved cash plan's forecast for that date". Runway row reproducible: ≈€300,000/month net spending; €400,000 minimum reserve; €7.6m − €0.4m = €7.2m ÷ €0.3m = 24 months.
- Medium — revise WHY INVESTORS CARE → names the governance consequence (consent rights exercised against the plan, not the announcement). Seller-payment paragraph: "out of existing earnings" → available cash, forecast cash generation or a separate funding commitment.
- Low — remove editorial explanation from the diagram commentary.
- Spec revised 2026-09-15 with Changelog line.
**Adapted:** callout extended with the consent-rights clause; runway labels placed inside the Runway row.
**Declined:** none.
**Unresolved / needs separate action:** no comic speech changed; no flags; all six image hashes match. Per-hire cost (≈€100,000 onboarding engineers) differs from the canonical €150,000 specialist FTE; the article states this scenario is separate. timetoread 12 min.
**Verification:** arithmetic above; summary 497 words; seven cross-links resolve; glossary defines the two share terms; backlinks in 00, 26, part-1-intro, reading-guide and glossary do not assert the €100m was a valuation. Build not run.

## 26-valuation-is-an-estimate — A Valuation Is an Estimate, Not a Fact (`valuation-is-an-estimate`)

**Files changed:** index.md, spec.md (summary.md and comics.md unchanged — neither carries the unicorn figure, the "price" wording, the year-one timing rule or the deterministic callout language).
**Implemented:**
- High — Correct the percentage denominator in "To Probe Further" → annotation now reads "In 135 US unicorns, reported post-money valuations averaged about 50% above the authors' modeled fair values, which were derived from each share class's contractual terms"; sample and model qualifications kept; citation extended to Journal of Financial Economics 135(1), 2020, pp. 120–143. Only one occurrence existed in the post.
- Medium — Restore the qualification in both opening callouts → WHY YOU SHOULD CARE: "A valuation may shape the growth, margin and cost targets proposed for your team. Identify its purpose and read how the estimate was built before adopting them." WHY INVESTORS CARE now names the governance consequence (the investor reports the valuation to its own funders and must defend its assumptions). Stage 1 checkpoint: "€60 million is a price" → "is an estimated value".
- Medium — Fix the calendar claim in "One Assumption to Challenge" → "the model cannot assume a full year of savings; phase the benefit from the expected validation date and check what that does to the early margins."
- Low — Closing competence claim → "You can now ask which value is being quoted and which assumptions need testing."
- Spec: revised 2026-09-15, Changelog line added.
**Adapted:** WHY YOU SHOULD CARE keeps the "how the estimate was built" hook instead of "test the assumptions"; WHY INVESTORS CARE rewritten to a consequence rather than the review's wording; JFE volume/pages added to the citation (NBER link kept as the accessible URL).
**Declined:** chapter split (already Superseded); no timetoread change (net +10 words on ~3,300).
**Unresolved / needs separate action:** no comic dialogue changed, no flags added. Source-version nuance for the bibliography: NBER w23895 says 50% above fair value (15 unicorns >100%); the published JFE version says 48% (14 >100%). "About 50%" is accurate for the cited NBER page; if the bibliography cites the JFE version specifically, it should say 48%. SSRN and ScienceDirect returned 403; confirmed via NBER and Stanford GSB pages. The Tuck PDF mirror is still broken.
**Verification:** NBER w23895 and Stanford GSB working-paper page fetched; denominator arithmetic (fair 100, reported 150 → 50% above; fair is 33⅓% below reported; old "50% below" would imply 2×). Article arithmetic rechecked (€20m − €16m = €4m EBITDA; €3m EBIT; €2m PBT; €1.5m net; 20% margin; €40m equity; 3× revenue, 15× EBITDA; €48m; €10m post-money, 20%; €1.6m vs €1.4m). 80-hour onboarding baseline matches 08-roadmap-to-revenue (80/50/62). Six cross-link targets exist. Summary body 493 words, unchanged. Build not run.

## 02-three-different-returns — Same Company, Same Performance, Three Different Returns (`three-different-returns`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — scope WHY INVESTORS CARE to a fund manager → "A fund manager reports investment returns to its fund investors, and those returns combine company performance with entry price, financing and exit terms; that is why it works the price, leverage and timing levers, and why it needs management's claims about engineering to be ones it can defend in that report." "Its own investors" removed.
- Medium — complete the comic's format alignment → panels 2, 3 and 4 read against their images (embedded speech "Several mechanisms change the return." / "Which change caused which result?" / "The payment dates matter too."); dialogue is now 10×/12×/7× "Same team, same numbers." → `needs_regeneration: true` on panels 2 and 3; panel 4 stays flagged. Prompts for the three rewritten as one triptych (same earnings chart, same debt stack, only the price tag changes).
- Low — simplify the conditional upper-bound wording → "At the entry multiple, the bridge attributes €50 million to higher earnings. Allocating the €10 million interaction row differently changes that accounting attribution; none of those conventions identifies engineering's causal share." Interaction table (€50m + €20m + €10m = €80m) preserved.
- Low — name the return measure in the headline comparison → "the fund's proceeds and its MOIC more than double, from €65m and 1.6× to €140m and 3.5×, while the annual rate rises from about 10% to about 28%"; EBITDA defined in a parenthesis beside the preview; "IRR exposes the speed, given the dates of the payments".
- Collection review — fund manager as actor; link [[fund-economics]] rather than duplicate → the "What Technology Can and Cannot Claim Credit For" paragraph names the manager reporting to limited partners, notes a corporate owner or individual has no such report, and points to fund-economics for fees, profit share and distribution rules.
- Summary aligned (proceeds and multiple; manager reports to fund investors; IRR accounts for payment dates) and trimmed to the cap. Spec revised 2026-09-15 with Changelog line.
**Adapted:** comic prompts for panels 2–4 rewritten since regeneration is required anyway; callout keeps a clause on why price/leverage/timing are the manager's levers.
**Declined:** none.
**Unresolved / needs separate action:** artwork regeneration for panels 2, 3 and 4 (flagged). 1.6× shown for the 7× row is 1.625× rounded (consistent across formats).
**Verification:** 7× → EV €105m, equity €65m, 1.625×, IRR 10.20%; 10× → €150m/€110m/2.75×/22.42%; 12× → €180m/€140m/3.5×/28.47%; bridge 50 + 20 + 10 = €80m; 2× in 3 years 25.99%, in 7 years 10.41%; dilution 20% → 16%, €3.2m = 1.6× on €2m. Summary 500 words (496 before). Five cross-links resolve. No "its own investors", "at most", "generous reading" remain. timetoread 14 min unchanged. Build not run.

## 03-raise-what-you-need — Match the Funding to the Work (`raise-what-you-need`)

**Files changed:** index.md, summary.md, spec.md (comics.md untouched)
**Implemented:**
- High — remove capacity value from the cash available for debt service → the €350,000 + €135,000 = €485,000 line is gone; every payment tested against €350,000 of operating cash alone (margins €290,000 / €40,000 / €60,000 / €80,000); the canonical sentence on released staff time added verbatim; €135,000 / €225,000 labelled projections; Sam's dated downside (operating cash −15% to €300,000 from year two → year two €10,000 short; years three/four clear by €10,000 / €30,000); three dated cash mechanisms named (contract specialist not extended beyond month 12; two-specialist hire deferred = avoided, not reduced; additional contribution only after gate 2).
- High — complete the loan terms → four-year loan at 8% with a schedule table (Y1 €60,000; Y2 €310,000; Y3 €290,000; Y4 €270,000; closing balance 0; total interest €180,000; payments €930,000). New paragraph on why the requirement cannot simply be carried from operating cash (build €180,000 + transition €90,000 + two quarters of specialist €75,000 = €345,000 front-loaded into two quarters, against €350,000 arriving over twelve months before year-one interest and the minimum cash balance).
- Medium — make the decision reviewable → Priya measures the cohort of eight at day 90; the board decides at day 100; thresholds < 60 green / 60–70 amber (62 h here; data-quality step €40,000 from the €140,000 reserve) / > 70 or no reduction red (reopen hiring, narrow the target, or reopen the equity conversation); the €140,000 headroom explicitly excludes financing costs; Arrangement A "does not remove the risk".
- Medium — qualify the callout ("can force"; trade-off between ownership, reserve and future financing risk).
- Low — rounding labelled ("25% of €270,000 is €67,500, rounded up to €70,000").
- Scenario separation stated (own financing scenario; imports only the pilot cost basis and the 62-hour result).
- Summary shortcut fixed; timetoread 11 → 14 min; spec revised 2026-09-15.
**Adapted:** downside uses a fictional 15% fall; amber's data-quality step charged to this scenario's €140,000 headroom.
**Declined:** Low — comic pacing (deferred by the review itself); no panel text needed changing.
**Unresolved / needs separate action:** no comic flags; summary at 496 words by the agent's count.
**Verification:** schedule arithmetic (60/60/40/20 interest; 60 + 310 + 290 + 270 = 930 = 750 + 180); margins; downside; front-load 345; 610 = 180 + 30 + 90 + 150 + 70 + 90; headroom 140; 08 and 28 linked passages checked; eight cross-links resolve. Build not run.

## 04-obligations-before-budget — Find the Cash Behind Your Technology Budget (`obligations-before-budget`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — explain the pilot's local cost basis → option 2 aligned to the shared basis: €180,000 build (12 engineer-weeks) + €30,000 first-year maintenance = €210,000; €200,000 removed from all formats; basis sentence added. Option 1 fixed to two peak quarters = €75,000 (half of €150,000/yr); rejection wording corrected ("buys two quarters of capacity … the €75,000 recurs at the next peak"). Funding: €210,000, of which €180,000 committed at approval; ≈€0.6m discretionary capacity untouched (0.8 − 0.21 = 0.59).
- Medium — show the cash condition for the fallback → by day 90 ≈€90,000 spent, €90,000 committed and payable over the following two quarters, €30,000 maintenance not yet started; nothing of the build cancellable; a one-quarter specialist costs €37,500 and fits within the ≈€0.6m; trigger = cohort > 70 h or first-half collections behind plan.
- Timing → day-90 cohort of eight, board decision at day 100, second-stage gate at about month six (≤ 50 h with waiting time down); thresholds < 60 / 60–70 / > 70 used.
- Own-scenario statements added for the annual model (€0.3m opening cash, covenant test) and the €3m / €600,000 − €350,000 runway example.
- Medium — make the payment-authority table conditional (interest/principal under the loan's terms or a waiver, amendment or refinancing agreed with the lender; distributions under the agreements and applicable rules). KEY POINTS and summary match.
- Low — trim repeated setup; repair the onward links to [[the-financing-slipped]] and [[help-that-changes-capability]].
- Summary rewritten to agree; comic panel 6 caption/prompt updated (dialogue unchanged; image viewed, no euro figure). Spec revised 2026-09-15.
**Adapted:** "€Y remains cancellable" stated honestly as nothing of the build cancellable; two-peak-quarter duration chosen over twelve months (matches the "same two quarters" scarce-capacity sentence).
**Declined:** none.
**Unresolved / needs separate action:** no comic flags. timetoread 15 min unchanged (+≈150 words).
**Verification:** bridge 10 − 4 − 1 − 2 − 1 = 2; 2 − 1.5 = 0.5; 0.5 + 0.3 = 0.8; 0.8 − 0.21 = 0.59; 150,000 ÷ 2 = 75,000; ÷ 4 = 37,500; runway 3m ÷ 250k = 12, ÷ 350k ≈ 8.57; interest 60m × 6% / 9%. Day numbers and thresholds match CANONICAL. No "200,000" remains. Ten cross-links resolve. Summary 498 words. Build not run.

## 05-decide-who-decides — Decide Who Decides, Before You Disagree (`decide-who-decides`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — establish that the January fallback is authorized and resourced → the board declined the €1 million program in one year, endorsed the direction and confirmed the first stage Ines approved within her delegation in [[obligations-before-budget]]: €180,000 build + €30,000 first-year maintenance = €210,000 and twelve engineer-weeks (freed by deferring a reporting refresh). The two hires are the board's decision (≈€175,000 for June–December; ≈€300,000/yr), decided at the May meeting on Sam's collections and Priya's report on the first three pilot implementations. "What is unfunded is only the acceleration." Missed-deadline branch: January is the plan with the cash and weeks already authorized; options are renegotiate, a contract specialist for the peak quarter within Ines's delegation, or take hiring back to the board. Decision block carries all fields.
- Medium — mark the changes of example → intro names the three Larkspur illustrations; "In a separate illustration" and "Back to the onboarding proposal" mark the switches. Summary and comic intro match.
- Medium — explain why the €40,000 board request needs that forum → canonical delegation rule recorded: Ines approves up to €500,000 inside the approved plan; any reserve draw, any change to what an envelope funds, and permanent hires outside the headcount plan are reserved to the board. The €40,000 is a reserve draw and funds a step the plan did not contain; the same path [[cannot-fund-everything]] follows for its retest; figures point to the shared record in the [[toolkit]].
- Low — WHY INVESTORS CARE conditional ("Where an investor has negotiated approval rights or reserved matters…"); role recap shortened.
- timetoread 10 → 12 min; spec revised 2026-09-15.
**Adapted:** first-stage cost uses the canonical €180,000 + €30,000 (the interrupted agent had copied 04's €200,000); headcount clause added to the delegation rule; summary trimmed from 602 to 498 words.
**Declined:** none.
**Unresolved / needs separate action:** depends on 04 aligning to €210,000 (in progress). The "reporting refresh" displacement is this chapter's own detail. No comic speech changed; panel 6 caption extended; no flags.
**Verification:** €1m > €500,000; 2 × €150,000 = €300,000; 7/12 × €300,000 = €175,000; €800,000 − €210,000 = €590,000 ≈ 04's "about €0.6 million"; day-100 figures match CANONICAL §A, 17 and toolkit; 28 already routes its reserve draw to the board citing this chapter. Summary 498 words. Six cross-links resolve. Comic JSON parses. Build not run.

## 06-different-bets — Management Equity, Fund Carry and Employee Jobs Are Different Bets (`different-bets`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — correct the fund-risk row → row is now "The fund's stake and its manager's carry"; scenario assumption: the fund holds 70% of Larkspur's ordinary equity; its share of the €6m incremental equity value ≈ €4m (70% × €5.7m after the €300,000 executive pool); the manager's carry is a share of fund profit, about €800,000 at 20%, and less or nothing if the whole fund has not returned capital and cleared the preferred return (whole-fund unless deal-by-deal; [[fund-economics]]). Risk: the fund's capital in Larkspur; other holdings spread exposure but do not shrink a loss on Larkspur. €6m labelled incremental company equity value, not a payout. "The executive on the 5% plan" and "the fund's manager" no longer conflated; callout aligned.
- Medium — reconcile transition costs with first-year saving → staged plan dated (six of eleven leave at month six, the rest at month twelve); nine-month closure saves €150,000 in year one against €350,000 severance (net −€200,000), €600,000 from year two; staged plan saves €150,000 against €550,000 (net −€400,000); staging costs €200,000 more and moves the full saving from month ten to month thirteen.
- Medium — define retention and design the guardrail → gross revenue retention ≥ 90% (defined; net revenue retention reported beside it); worked contrast €10m base, −€1.2m, +€1.5m → net 103%, gross 88%; Fastly Q4 2020 shareholder letter cited for the definitions; commission rule prospective (half at signature, half at first renewal, written before the year begins).
- Medium — repair comic panels 4–5 captions (exit two to four years away; renewals in the next two quarters; closing "could raise the sale price if the saving survives the renewals and a buyer pays the assumed multiple"; eleven employees lose their jobs now). Summary matches.
- Low — separate options from share awards (two table rows); editorial sentence "The title's comparison needs a decision to bite on" removed.
- timetoread 11 → 14 min; spec revised 2026-09-15.
**Adapted:** "at most about €800,000" → "about €800,000 … and less or nothing if" (marginal carry inside a catch-up band can exceed 20%); summary option example compressed.
**Declined:** no new S-numbered entry for the Fastly letter (inline link).
**Unresolved / needs separate action:** no comic speech changed; no flags. The 70% holding is stated inside this separate scenario only.
**Verification:** all arithmetic listed (5% × €40m = €2m; 10,000 × €1 = €10,000; €600,000 × 10 = €6m; €5.7m × 70% = €3.99m; 20% × €4m; retention ratios; €550,000 > €500,000 delegation matches chapter 05). Fastly letter fetched from SEC. Summary 498 words. Five cross-links resolve; fund-economics carry mechanics agree. Build not run.

## 07-investor-under-pressure — Judge an Investor by Their Behavior Under Pressure (`investor-under-pressure`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — show the protection that makes the choice of B credible → "both can be bounded by a governance term" removed; the written follow-on narrows only the next funding decision; B's management-change practice and year-seven exit pressure "remain risks the board accepts" (new "Risks accepted" line in the decision record; reopening trigger names the approval route for management changes in the shareholders' agreement). Fund-term qualification kept (ten-year term fixes no sale date; extension needs LP approval per ILPA Principles 3.0 p. 17).
- Medium — distinguish reserved from contractually committed follow-on → B's fund reserve is an internal allocation on which Larkspur has no claim; the negotiated clause: payer = the same fund, with written confirmation that uncalled commitments cover it; €1.5 million at the round's share price; released when Larkspur calls it; lapses fifteen months after closing; the pilot result is the only performance condition; state "agreed in the term sheet, not yet signed"; even signed it is a right to call, not cash. All formats carry the same state.
- Follow-on gate aligned with the shared chain → "65 hours or less, with customer waiting time no worse than the baseline, across a measured cohort of at least eight, confirmed by the board", deliberately below the board's own 60-hour expansion threshold so the shared 62-hour amber result keeps the follow-on callable while expansion stays deferred. Scenario declaration: round, valuations and follow-on belong to this chapter alone; the pilot is the shared one.
- Medium — remove "the only guide" from WHY YOU SHOULD CARE; WHY INVESTORS CARE names the governance consequence (a written follow-on removes committee discretion).
- Low — keep the two scenarios distinct in "When the Evidence Is Missing" (term-sheet vs inherited-investor entries).
- Low — comic panel 4 evidence integrated into the article; panel 5 caption ("a count alone is not a verdict"); panels 3 and 6 captions updated.
- Summary rewritten to the funding state and the 65-hour gate (500 words). timetoread 9 → 13 min. Spec revised 2026-09-15.
**Adapted:** gate set at ≤ 65 h rather than "its own gate", with the reasoning stated.
**Declined:** summary's opening inherited-investor sentence dropped for length.
**Unresolved / needs separate action:** no comic speech changed; no flags. The article cites the board's 60-hour rule with links to 08 and 17 — depends on those agents implementing CANONICAL §A thresholds (coordinator to confirm).
**Verification:** ILPA Principles 3.0 p. 17 fetched and extracted; gate arithmetic (62 ≤ 65; cohort 8 ≥ 8; lapse at 15 months covers month 6 and ≈ day 190). Eight cross-links resolve. Six comic JSON blocks parse; hashes unchanged. Build not run.

## 28-cannot-fund-everything — You Cannot Fund Every Good Project at Once (`cannot-fund-everything`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — reconcile the shared recovery expenditure → one sequence per the canonical record: the envelope is the first-hundred-days plan (€500,000 / 24 engineer-weeks, the same plan [[first-hundred-days]] follows); KNW-1 row added (€0 / 4 protected specialist-weeks outside the 24); "aren't additions to the programs in other chapters" and "over the next two quarters" deleted; REC-1 €80,000 / 4 weeks all spent by the day-45 failure (environment, access, fifteen-minute backups, the test) → correction and retest by day 85 = €20,000 / 2 weeks approved by the board on Ines's request → REC-1 €100,000 / 6 total; committed €300,000 / 20, reserve €200,000 / 4; closing paragraph carries the chain to day 100 (€40,000 / 4 draw → €340,000 / 24; reserve €160,000 / 0). Deferred items recorded.
- Medium — explain why the reserve draw returns to the board → Ines proposes, the board approves the plan and envelope; inside the plan Ines authorizes spending; any reserve draw or change to what the envelope funds stays with the board ([[decide-who-decides]]).
- Medium — correct "The option is only worth what it costs to exercise" → Luehrman annotation reworded (keeping an option open has a cost; its value depends on the choices it preserves and the cost of taking them).
- Low — shorten the explanation after the worked choice (score paragraph merged); WHY INVESTORS CARE sharpened; "Sort the Rows" names KNW-1.
- Summary rewritten to the same sequence (500 words); comic intro and panels 3, 4, 6 captions aligned (speech unchanged). Spec revised 2026-09-15.
**Adapted:** canonical delegation rule used instead of a recovery-specific reservation; the 14 September log's "separate from the €300,000 envelope" claim withdrawn in text.
**Declined:** none.
**Unresolved / needs separate action:** no comic flags. 17, toolkit and 11 being reconciled by their agents. timetoread 10 min unchanged.
**Verification:** full ledger arithmetic recomputed (280/18 → 300/20 → 340/24; reserve 220/6 → 200/4 → 160/0; requests 500 / 30); seven cross-links resolve; comic JSON parses; leftover-phrase grep empty. Build not run.

## 08-roadmap-to-revenue — The Chain From Roadmap to Revenue Breaks Easily (`roadmap-to-revenue`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — keep observed capacity separate from cash and future benefits → cost basis stated once (€75/h; 2,000 h/FTE-year ⇒ €150,000 per specialist; 100 × 80 h = €600,000; at 50 h €375,000; Δ €225,000 = 3,000 h). "Observed versus projected": 144 h observed (≈€10,800) vs 1,800 h / €135,000 a year labelled a projection with the comparison caveats. "Cash and commitments at day 100": €180,000 committed, about €90,000 incurred, €90,000 payable over the next two quarters; €30,000/yr maintenance a commitment from the next financial year, none incurred by day 90. "No contractor to cancel" → the contract specialist's twelve-month term ([[raise-what-you-need]]) had not run by day 100; the deferred hire is spending avoided, not reduced. Day 90 = Priya's measurement; day 100 = board decision.
- Medium — justify the €40,000 next stage prospectively → the €90,000 incurred argues neither way; the case is a named bottleneck and the cheapest test of it; gate 2 stated (second cohort at about month six ≤ 50 h with waiting time down); "stopping the pilot" no longer rejected on sunk cost; the pre-set rule (< 60 green, 60–70 amber, > 70 red; 62 in the middle band) is stated.
- Medium — distinguish observed hours from an annual extrapolation → KEY POINT 3, closing paragraph ("held as far as the comparison can show") and the Tool 6 ledger sentence.
- Medium — remove unsupported prevalence from the introduction → WHY YOU SHOULD CARE uses the mechanism framing; WHY INVESTORS CARE kept and reworded (released capacity enters a model only with an explicit, dated conversion).
- Low — let the comic end on the tested outcome → panel 6 rewritten to the day-100 review ("We saved hours; we have not yet served more customers.") and flagged.
- Canonical alignment: expansion decision at the next quarterly review (≈ day 190), not before month 13; reserve €160,000 / 0 weeks; baseline reconstructed at day 20.
- timetoread 12 → 15 min; spec revised 2026-09-15.
**Adapted:** the High about the financing chapter is 03's job; this chapter supplies the qualification 03 imports. Panel 5 caption updated, dialogue unchanged.
**Declined:** none.
**Unresolved / needs separate action:** artwork regeneration for comic panels 2 (still flagged) and 6 (newly flagged). Cross-post facts in 03, 17 and 04 are being reconciled by their agents.
**Verification:** all arithmetic recomputed and matches CANONICAL A and B (reserve 500 − 280 − 20 − 40 = 160; 24 − 18 − 2 − 4 = 0). Summary 499 words. Eight cross-links resolve. No leftover "no contractor" / "As cash, the pilot has cost" / "deferred one more quarter". Build not run.

## 09-can-the-team-deliver — Can the Software and the Team Deliver What Was Promised? (`can-the-team-deliver`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — do not infer that all time outside the DORA measure is waiting → the "spent waiting, not building" assessment replaced: most elapsed time falls outside commit-to-production, and the difference does not say what that time is made of (pre-commit work includes implementation as well as approvals and queues); a trace of one recent change is needed and [[fix-decisions-before-hiring]] supplies it. Same correction in the technical-debt section ("three weeks per change"), the finding table's Uncertainty row, the conclusion, Question 2 and the summary; telemetry paragraph lists slow implementation as a fourth possible cause. Numbers unchanged (commit-to-production under two days; request-to-production about three weeks).
- Medium — qualify the new investor callout → WHY YOU SHOULD CARE: "If the investment plan assumes a country launch before the systems have been assessed, the assessment tests whether the date and budget are credible, and gives the board its first grounded view of what the plan will cost and when it can arrive." WHY INVESTORS CARE unchanged (names a reprice/resequence consequence).
- Medium — finish the comic's assessment scene in the artwork → panel 4 image still shows "Modular application" vs "Separately deployed services" with "Which option fits our work?"; prompt now states explicitly that the board shows an assessment, not an architecture comparison; `needs_regeneration: true` retained. Panels 1, 2, 3, 5, 6 checked against the revised article — no change needed.
- Low — reduce repeated explanation after the finding → closing paragraphs collapsed; handoff now names the three-weeks-vs-two-days question and hands it to [[fix-decisions-before-hiring]], then [[growth-into-design]].
**Adapted:** the review's "correct the corresponding shortcut in the linked organization chapter" left to chapter 13's own agent (its review rec 2 covers the "build itself takes under two days" claim and the 3 + 7 + 2 + 3 + 1 = 16 working-day trace); chapter 9 now says nothing about build time, only commit-to-production time.
**Declined:** none.
**Unresolved / needs separate action:** panel 4 artwork mismatch persists (flagged). Chapter 13 line "the build itself takes under two days" depends on that chapter's agent. Chapter 27's quotation of this chapter's Constraint row still matches. No D-3/ONB-1 numbers in this chapter.
**Verification:** DORA metrics guide fetched (five metrics; change lead time = commit to production). Transition table 900,000 + 240,000 + 160,000 = 1,300,000 rechecked. Summary 498 words. Six cross-links resolve. timetoread 13 min unchanged. Build not run.

## 13-fix-decisions-before-hiring — Fix the Decision Problem Before Adding People (`fix-decisions-before-hiring`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — keep both conditions attached to the deferred team → the five-person team is deferred "until two conditions are both met: second-country demand is evidenced, and the next round is committed and the board has approved the roles"; faster sales satisfy the demand condition only. Summary and comic panel 6 caption match.
- Medium — correct the opening's description of build time → takes only what chapter 09 states (three weeks request-to-production; under two days commit-to-production) and lets the trace supply the split: sixteen working days (3 + 7 + 2 + 3 + 1), two building, one release, thirteen waiting; the six saved days are a forecast to be confirmed by the next three traces.
- Medium — distinguish a failed result from a disproved diagnosis → the sixty-day trigger calls for a new trace, not a hire; the capacity diagnosis is revisited only if approvals are gone and the queue persists.
- Medium — complete the leadership and capacity tradeoffs → operations lead's displaced work named; authority split explicit (Ines authorizes within the operating budget; Alex accountable for engineer and transfer; Priya for the catalogue); leadership case names the evidence and the remedy (head of engineering owning release process, or replacement if Alex refuses the narrowed role). Comic panel 4 caption: "added leadership with authority, or replacement".
- Low — soften the blanket claim about adviser dependence (a chosen continuing service vs a failed transfer), linking [[useful-engagement]].
- timetoread 13 → 14 min; spec revised 2026-09-15 with success criterion updated.
**Adapted:** leadership counterfactual rewritten so Alex's approval is inserted before the delegated finance check ("the sign-off wait has moved rather than gone"); comic panel 3 alt text "salary savings" → "a cheaper team's cost".
**Declined:** none.
**Unresolved / needs separate action:** no comic speech changed; no flags. The €90,000 billing engineer is funded from the operating budget, outside the shared €500,000 envelope.
**Verification:** 3 + 7 + 2 + 3 + 1 = 16; waiting 13; delegation removes 6 → 10 forecast. Staffing 5 × €90,000 ≈ €450,000; location €650,000 + €150,000 = €800,000; €1,050,000 first year. Chapter 09 checked for agreement. Five cross-links resolve. Summary 500 words. Six comic JSON blocks parse. Build not run.

## 27-growth-into-design — Turn "We Expect Growth" Into a Design Decision (`growth-into-design`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — compare costs on the same basis → options table now has "Additional cash, first year" (A €100,000 = €60,000 setup + first €40,000 subscription; B €140,000; C €1.3m, ≈€720,000 in the first twelve months before migration) and "Recurring cost and responsibility after the first year" (A €40,000/yr per country plus reconciliation staff; B maintenance inside the billing engineer's ≈€90,000/yr role; C saving only after retirement). €80,000 labelled the upfront difference, €40,000 the first-year difference; A cumulative €100,000 / €140,000 / €180,000 vs B flat €140,000, so B is cheaper only beyond year two or with a third country. Fallback priced everywhere as €60,000 + €40,000/yr.
- Medium — make the failure state reviewable → the existing module stays authoritative until the invoice replay passes; on a month-four failure ≈€80,000 of B is sunk, €60,000 unspent; incremental fallback €60,000 + €40,000/yr; €300,000 − €80,000 = €220,000, €120,000 left after A's first year; Ines authorizes (pre-recorded trigger inside the board's envelope) and reports at the next board review; first supplier invoice about month 9–10.
- Medium — correct the summary's description of the options → "on one basis, first-year cash then recurring cost; two fit the limit; C exceeds both the cash limit and the date". Comic intro and panels 3/6 captions match.
- Medium — preserve the distinction between changed timing and available cash → under slower growth B's €80,000 premium is recovered only beyond year two; a longer holding period does not change C's €1.3m requirement against a €300,000 envelope; C needs a financing decision of the kind compared in [[raise-what-you-need]].
- Low — specify specialist weeks; reduce table repetition (six specialist-weeks, three from each, plus ten from the billing engineer; several restatements cut).
- Separate-scenario sentence: this is a later scenario from the hundred-day plan, whose €500,000 envelope deferred the expansion beyond year one and whose own €300,000 was the annual cost of two deferred hires; the €300,000 here is a fresh envelope. Summary matches.
- Body 4,032 words (net shorter); timetoread 16 min kept; spec revised 2026-09-15.
**Adapted:** Ines kept as authorizer of the fallback (reports to the board) rather than "the board can fund"; C's first-year cash stated "before migration costs".
**Declined:** none.
**Unresolved / needs separate action:** no comic speech changed; no flags. Chapter 17 line "€260,000 of the €300,000" must be reconciled by the 17 agent (in progress). Chapters 09 and 13 figures agree.
**Verification:** all arithmetic listed (A/B/C first-year and cumulative; C 900,000 × 12/18 + 240,000 × 6/12 = 720,000; fallback ledger; timing; payback unchanged). Summary 497 words. Eight cross-links resolve. Build not run.

## 10-cheaper-cloud-bill — Why a Cheaper Cloud Bill Can Be Bad News (`cheaper-cloud-bill`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — close against the plan as well as the prior period → three-row monthly table: prior year €100,000 / 1,000,000 = €0.100; plan €100,000 / 1,500,000 = €0.067; actual €120,000 / 1,500,000 = €0.080. Unit cost fell 20% against the prior year; the flat-spend plan was missed by €20,000 a month and unit cost is 20% above the plan's implied figure. All three rows on one cost-assigned-to-the-period basis. Other-direction case added (€90,000 / 1.2m = €0.075); the €0.16 case states it is 60% worse than last year and 2.4× plan. Closing: the one-year commitment closes €9,000 of the €20,000 monthly gap; Alex still owes an explanation of the remaining €11,000. WHY INVESTORS CARE keeps ab7a8f4's wording plus "and the approved plan turns that expectation into a number to test".
- Low — label the hypothetical pricing assumptions once (30% discount and commitment floors are example assumptions); Option B's extra €6,000 a month exists only at €50,000 of demand or above and becomes a €14,000 disadvantage at €30,000.
- Low — let the closing formats carry the chosen commitment → comic intro, panel 2 and panel 4 captions/prompts carry the plan comparison and the chosen one-year commitment; summary separates "unit cost improved 20%" from "plan missed by €20,000 a month".
- timetoread 11 → 13 min; spec revised 2026-09-15 with Changelog line.
**Adapted:** the €90,000 secondary case is in the article only (summary length); one-sentence basis cross-reference rather than reordering sections.
**Declined:** none.
**Unresolved / needs separate action:** no comic speech changed (verified byte-identical); no flags. 27-growth-into-design line 132 hands off with "improves the earnings measure directly" — coordinator's call. Minor period tension between flat plan this year and €60,000 demand "next year" left as is.
**Verification:** all ratios and option-table figures recalculated (B €35k/€35k/€45k/€35k; C €21k/€41k/€51k/€21k vs flexible €30k/€50k/€60k/€20k; C saves €9,000 at every range point, −€1,000 in stress). Summary 499 words. Four cross-links resolve. Six comic JSON blocks parse. Build not run.

## 11-prove-you-can-restore — Prove You Can Restore, Not Just That You Back Up (`prove-you-can-restore`)

**Files changed (this session, total vs pre-revision state):** index.md, comics.md, summary.md, spec.md (the article/comic work landed in the user's 12:32 commit 4bd1d51; the Opus pass verified it and fixed the summary)
**Implemented:**
- High — reconcile REC-1's cost, sequence and envelope → REC-1 €80,000 / 4 weeks bought the restore environment, backup-store access work, fifteen-minute backups and the failed day-45 test (sunk); correction (version-matched environment, managed credentials with a two-person procedure, written rehearsal) costed at €20,000 / 2 weeks from the reserve; Ines could not approve a reserve draw, so the board approved at about day 47 with a retest by day 85; ledger €280,000/18 → €300,000/20, reserve €220,000/6 → €200,000/4; one €500,000 / 24-week envelope (the stray €300,000 envelope claim removed); REC-1 closes at €100,000 / 6 weeks.
- Medium — define what the accepted recovery objectives cover → pass scoped to loss of the application environment in this region; residual (regional failure, weekday-only rehearsal, two-person credential dependence) accepted by Ines on the board's behalf with a quarterly retest; regional exposure carried to the day-190 review.
- Low — WHY YOU SHOULD CARE without categorical shorthand; conclusion closes on the next accountable test.
- Summary and comic panels 5–6 captions carry the reconciled sequence; summary trimmed from 518 to 497 words and its risk inset now compares €120,000 against REC-1's €100,000 total.
**Adapted/Declined:** none.
**Unresolved / needs separate action:** no comic flags (panel 5 bubble "Test the whole response." read from the image and unchanged).
**Verification:** ledger arithmetic; risk inset (5% × €4m = €200,000; 2% = €80,000); cross-post agreement read in 28, 17 and toolkit; seven cross-links resolve. Build not run.

## 12-ai-strategy-three-questions — An AI Strategy Hides Three Investment Questions (`ai-strategy-three-questions`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — connect the support experiment to the deferred hire → baseline (six agents, 1,200 tickets/month), forecast (1,320 by April 2027; seventh agent at €64,000/yr planned 1 April 2027), pilot 5 October–27 November 2026, throughput model (3 × 1.25 + 3 = 6.75 agent-equivalents ≈ 1,350; full rollout ≈ 1,500). The hire moves 1 April → 1 October 2027 only after a rollout check ending 29 January 2027, monthly volume under ~1,400 and reopen rate held: €32,000 gross less €10,000 recurring 2027 costs (licenses €3,600, review upkeep €4,400, rollout €2,000) = about €22,000 net.
- Medium — consistent customer-pilot gate → stop rule at week five (6 November 2026) and release gate at week ten (11 December 2026) with three separately checked conditions (95% sample accuracy; no missed safety-relevant document as its own check; review below 1.5 h/week, justified against the €300/month price).
- Medium — show all three questions in the comic → panel 3 replaced by the substitution test ("What did the customer lose?"); panel 4 replaced by the support pilot's hire condition ("Twenty percent faster is not a seventh agent."); both flagged for regeneration; panel 6 caption adds the gates.
- Dated gates for all three questions (Q3: customer test October 2026, renewal tracking to 31 December 2026, decision 15 January 2027); closing table column "Gate and date".
- Low — substitution example tied to an assumed configuration (general assistant via web interface with spreadsheet upload; a tense slip corrected); Low — evidence box split into two blockquotes.
- Separation: the three tests have their own budgets and dates, not a draw on the hundred-day envelope; "inside the approved operating plan" replaces the envelope reference.
- Body trimmed from 3,945 to 3,831 words (timetoread 15 min); summary rewritten (499 words); spec revised 2026-09-15.
**Adapted:** replaced panel 3 rather than panel 2; WHY INVESTORS CARE kept (names a financing consequence).
**Declined:** none.
**Unresolved / needs separate action:** artwork regeneration for panels 3 and 4. Peng et al. completer wording left as previously confirmed by the reviewer.
**Verification:** arithmetic and calendar checks listed (week 5/10 Fridays, 6/12 × €64,000); arXiv 2302.06590 and METR July 2025 post fetched; six cross-links resolve. Build not run.

## 14-acquisition-adds-work-first — An Acquisition Adds Work Before It Adds Value (`acquisition-adds-work-first`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — reconcile parallel running with the May independence test → one dated calendar: closing 1 Jul 2026, TSA to 30 Jun 2027; identity/email/devices live 31 Oct 2026, parallel Nov–Dec, parent off 31 Dec; finance/procurement/payroll live 31 Dec, parallel Jan–Feb, off 28 Feb 2027; network/security monitoring/licences live 28 Feb, parallel Mar–Apr, off 30 Apr; May 2027 test with every parent service off; June reconnection buffer under the live TSA; extension Jul–Sep only on failure. TSA scope and cost: three bundles €10,000 + €10,000 + €15,000 = €35,000/month; charge stops at switch-off; €5,000/month standby; extension 150% = €52,500 × 3 = €157,500. Planned TSA cost €320,000 vs €420,000 if nothing were switched off. Funding sentence separates €320,000 TSA, €300,000 one-time, €157,500 contingency, €300,000/yr recurring. Slip cases recalculated. Summary carries the corrected schedule.
- Medium — make completion depend on the chosen benefit (combining complete when the chosen integration works, the benefit is evidenced and duplicated cost has ended; separating complete with no temporary parent service; a retained priced supplier contract is not a failed separation).
- Medium — explain the two engineers' capacity (2 × 26 − 6 leave − ≈20 operating = 26 project weeks vs 29 needed).
- Low — restore "can price in" / "can assume" in the callouts.
- Separate-scenario sentence added (both Larkspur examples use their own dates and figures, separate from the Part V record). Comic panel 5 caption carries the dated test. Spec revised 2026-09-15.
**Adapted:** kept the May test and the two-month rule and moved the last milestone earlier (test must run inside the TSA); payroll added to the finance bundle.
**Declined:** optional decision table; WHY INVESTORS CARE kept (names the priced synergy/independence date).
**Unresolved / needs separate action:** no comic speech changed; no flags; panel 5 caption carries dates the artwork does not depict. timetoread 14 min unchanged.
**Verification:** arithmetic rechecked (capacity; €700,000 − €400,000; TSA totals; extension; slip cases); calendar internally consistent. Summary 499 words. Nine cross-links resolve. Comic JSON parses. Build not run.

## 15-investors-adviser — Is the Investor's Adviser Helping, Assessing or Deciding? (`investors-adviser`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- High — distinguish a newly agreed company assignment from existing investor rights → the categorical "only the company can authorize an assessment of its executive" removed from all formats. Authority comes from an executive role, board responsibilities, agreed shareholder rights or an explicit assignment; a role change first asks what the investor's existing rights cover (example: §3.2 Inspection Rights of Avalyn Pharma's April 2025 investors' rights agreement, cited as an example that does not establish Larkspur's terms). A company-sponsored assessment with new access, manager interviews or coaching material needs Ines/board in Larkspur's agreed arrangement; directing company work needs authority the company granted. WHY INVESTORS CARE names the adviser as a channel for the investor's information rights. Summary and comic panels 2 and 6 captions match.
- Medium — separate oversight from instructions in the diagnostic table → "Formal oversight" (findings reported to whoever commissioned the review; an instruction only where a decision is delegated) and "Interim leadership" (authorized instruction, announced by the company) are now separate rows; "sixth kind of help" wording fixed.
- Medium — finish the visual role change → all six images inspected: panels 1, 4, 5 agree; panel 2 image "Who owns this decision?" vs dialogue "Who is authorized to decide?"; panel 6 image "Which role are you doing here?" with the wrong scene; panel 3 prop still shows a pricing-change example → flags kept on 2 and 6, panel 3 now flagged too with a corrected prompt.
- Low — remove editorial scaffolding; one connected confidentiality paragraph (coaching agreement plus engagement obligations; ICF code binds only an adviser who adopted it).
- Authority definition kept local in one line and attributed to [[decide-who-decides]].
- timetoread 11 → 12 min; spec revised 2026-09-15.
**Adapted:** "Inès" spelling not adopted (journal uses "Ines" in 74 places).
**Declined:** none.
**Unresolved / needs separate action:** artwork regeneration for panels 2, 6 and (optional) 3. 30-useful-engagement line 97 ("the firm requests one separately and the company announces it") is now slightly narrower than this chapter — align. Larkspur's engagement agreement is stated as a scenario assumption.
**Verification:** Avalyn Pharma IRA §3.2 fetched from SEC; ICF Code of Ethics page fetched (effective 1 April 2025). Summary 499 words. Four cross-links resolve. Six comic JSON blocks parse; hashes match. Build not run.

## 29-help-that-changes-capability — Find the Help That Changes What Your Team Can Do (`help-that-changes-capability`)

**Files changed:** index.md, comics.md, spec.md (calendar, €1,500 cap, €15,000 cost table and the day-21/40/63/90/100 chain landed in commit 4bd1d51; the Opus pass verified and corrected)
**Implemented:**
- Medium — one calendar for the provider comparison → arithmetic corrected: the independent route's seven-to-nine-week lead time runs from the day-7 request, so it starts day 56–70 and a six-week assignment ends day 98–112 (not "day 91 to 105"); the gap to the investor's specialist (start day 21) is five to seven weeks (not four to six); the request date is now stated in the table.
- Medium — price or cap for the selected engagement → verified (10 × €1,500 = €15,000; 6 engineer-days × 8 h × €75 = €3,600 capacity, not cash; €150,000/yr per FTE; two hires €300,000).
- Recommendations 3 and 4 verified satisfied (no editorial scaffolding; callout scoped to "Where a fund manager promises operating support").
**Adapted:** comic panel 5 caption/prompt corrected to "five to seven weeks later" (spoken text unchanged; no flag).
**Declined:** none (merger with 30 stays superseded).
**Unresolved / needs separate action:** none; toolkit Tool 4 and glossary labels verified consistent.
**Verification:** lead-time arithmetic recomputed; nine cross-links resolve; comics JSON valid; summary 497 words unchanged. Build not run.

## 30-useful-engagement — Turn an Offer of Help Into a Useful Engagement (`useful-engagement`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — identify which clock each date uses; make the specialist cost inspectable → verified: two clocks named; charter dated day 21 → ~day 63; €1,500 cap / €15,000 inside ONB-1's €180,000 and the ≈€90,000 incurred; "the budget is intact in that sense" after "All ten specialist days are used and invoiced at €15,000, within the agreed cap"; cost table identical to chapter 29's.
- Adviser-chapter alignment → the firm may form its own view under its existing reporting and information rights without asking; what it cannot take from this engagement is new access for that purpose; a company-sponsored assessment is a separate request agreed with Ines and announced by the company; stated as Larkspur's local arrangement. Propagated to the summary and comic panel 4 caption.
- Medium — finish the handover across formats → verified: panel 6 dialogue "Our team ran it without the specialist. The rest goes to the board." with `needs_regeneration: true`.
- Summary retrimmed from 513 to 498 words; spec changelog.
**Adapted/Declined:** none.
**Unresolved / needs separate action:** comic panel 6 artwork regeneration (image still shows two competing adviser assignments). Toolkit line 221 and glossary rows 146/148/356 verified consistent — no changes needed.
**Verification:** sixteen numeric/date tokens checked against CANONICAL §A; chapter 15 lines 86–106 read before rewriting; cross-links resolve; comics JSON valid. Build not run.

## 16-diligence-corrects-the-plan — Diligence Is Your Chance to Correct the Plan Before It Is Signed (`diligence-corrects-the-plan`)

**Files changed:** index.md, summary.md, comics.md, spec.md (most of the pass landed in commit 4bd1d51; the Opus pass verified and closed one gap)
**Implemented:**
- Medium — define the 80-hour denominator and preserve both explanations → mean across all five sampled implementations (one country, last two quarters; three needed the specialist's manual work), "the sample's figure, not yet a baseline for all twelve"; the Observed row now states what the ≈80 h averages (every recorded hour from signed contract to go-live) and that the time records do not split by activity, which is why the shares are unestablished; Alex's ~40% and Morgan's structural dependency recorded as compatible.
- Medium — make the pilot's decision rule agree with the later evidence → "the largest actionable share of remaining effort that has a costed step behind it", explicitly not "only if most hours trace to customer data"; 1.5× carried as a conditional forecast in three places; day-100 thresholds < 60 / 60–70 / > 70.
- Transaction terms → "management's immediate operating levers are the plan and its funding; any price adjustment depends on the signed terms" (SEC purchase agreement §2.11 true-up fetched to confirm the hedge).
- Handoff row names the day-20 baseline (twelve implementations) and Priya's day-90 measurement with the board decision at day 100. Summary at 500 words; comic captions updated; spec changelog.
**Adapted:** a first attempt attributing the configuration/data split to the five-case sample was reverted, since chapter 17 introduces that split at day 20.
**Declined:** Low callout item (already satisfied); no timetoread change.
**Unresolved / needs separate action:** no comic flags (all bubbles read from images and unchanged).
**Verification:** capacity arithmetic (100 × 80 = 8,000 h; 150 × 50 = 7,500; 150 × 80 = 12,000); cross-chapter consistency with 17, 08, 31; six cross-links resolve; comics JSON valid. Build not run.

## 17-first-hundred-days — The First Hundred Days: Turn Expectations Into a Funded Plan (`first-hundred-days`)

**Files changed:** index.md (in commit 4bd1d51), comics.md, summary.md, spec.md
**Implemented:**
- High — envelope, plan table, reserve ledger → €500,000 / 24 engineer-weeks; plan table with the portal-research row (€20,000 / 2, Priya) and KNW-1 as four weeks of the scheduling specialist's protected time outside the 24; totals €280,000 / 18 (+4 protected); reserve €220,000 / 6; day-45 paragraph carries the board-approved €20,000 / 2-week correction and retest around day 47 (→ €300,000 / 20; reserve €200,000 / 4); day-100 data-quality step €40,000 / 4 (→ €340,000 / 24; reserve €160,000 / 0); a per-period envelope table repeats the rows with ≈€190,000 incurred.
- High — preserve actual spending through the handover → about €90,000 of ONB-1's €180,000 by day 100, about ten of twelve engineer-weeks, €90,000 payable over the next two quarters, €30,000/yr maintenance from the operating budget from the next financial year.
- Medium — "a day-45 pass would have been a worse result" removed; "should change something" → "confirm or revise the plan on evidence".
- Medium — day-20 baseline reported (all twelve implementations of the previous two quarters, ≈80 h, configuration under half, data cleaning the largest remaining share); expansion decision dated (next quarterly review around day 190; expansion no earlier than month 13).
- Low — D-5 wording (understood by two people, only one of whom can release and recover it; the day-60 demonstration made that two).
- Comic: panel 1 €300,000 → €500,000; panel 3 the four-line plan totalling €280,000 / 18 with €220,000 / 6 in reserve; panel 6 the day-47 draw, the €40,000 / 4 step to €340,000 / 24 and the day-190 review; panel 2 the measured baseline. Applied to prompt, JSON caption and rendered caption.
- Summary rewritten from 597 to exactly 500 words keeping every canonical figure. Spec changelog.
**Adapted:** none beyond the summary rewrite.
**Declined:** none.
**Unresolved / needs separate action:** no artwork mismatch (all four affected panel images read: no euro figure, week count or date appears; speech bubbles unchanged). Panel 3 artwork shows generic "Priority A/B/C" boxes and panel 1 a blank calendar — generic before and after.
**Verification:** full ledger arithmetic; line-for-line agreement with revised 28 and 31; eight cross-links resolve; timetoread 10 min unchanged. Build not run.

## 18-the-financing-slipped — The Roadmap Did Not Slip, the Financing Did (`the-financing-slipped`)

**Files changed:** index.md and comics.md (in commit 4bd1d51), summary.md, spec.md
**Implemented:**
- High — correct comic panel 3's commitment/cash conflation → "It is not cash until it is committed in writing" removed from all files; panel 3 now ends "a written commitment still has conditions and is not cash received".
- Medium — one explicit restart rule → cash received, or a conditional commitment the board has specifically authorized counting, against a dated cash forecast and a funded downside; reaching the forecast date does not establish that closing conditions were satisfied. Stated identically in article, summary and comic panel 6.
- Medium — funded continuation beyond December → Reduction R1 (contract engineering agreements ending 31 October not renewed, notice due 1 October, saving €50,000/month from 1 November); the deeper level left open for the 1 October board decision.
- Medium — bridge assumptions → existing investors, €600,000 in one drawdown on account by 30 November, convertible, no arrangement fee, interest settling in the round; sensitivity rule (a fee or cash interest brings the date forward by amount ÷ burn).
- Separation: no ONB-1 / D-3 / REC-1 / KNW-1 identifier or €180,000 ledger figure in the prose; the separation sentence in article, summary and comic intro; "the onboarding pilot and the recovery work continue" only.
- Summary trimmed from 604 to 501 words; figure caption shortened; spec changelog.
**Adapted:** verification rather than re-editing for the four items already in place.
**Declined:** Low causation/tone item (already satisfied); adding a further primary financing document (NVCA term sheet already serves).
**Unresolved / needs separate action:** comic panels 2, 3 and 4 still need regeneration (images show the superseded scenario); panel 1's background art (whiteboard "INITIATIVE BLOCKER – SUPPLY CHAIN") is a partial mismatch left unflagged (bubble correct); panel 6's "Support agreement" label a tolerable artifact.
**Verification:** cash arithmetic recomputed (A breaches in late November at €390,000; C to 31 March; R1 without bridge ≈ 20 January; R1 with bridge ≈ mid-May); NVCA model term sheet re-downloaded and the quoted sentence confirmed verbatim; five cross-links resolve; six comic JSON blocks parse and image hashes match; timetoread 13 min. Build not run.

## 31-handover-of-obligations — Hand Over the Obligations, Not Just the Company (`handover-of-obligations`)

**Files changed:** index.md (in commit 4bd1d51), summary.md, spec.md
**Implemented:**
- High — correct the day-100 actual-cost record → Committed €180,000 / 12 weeks; Incurred ≈€90,000 (specialist €15,000, tooling, contractor) with ~10 of 12 weeks used; Remaining ≈€90,000 payable over the next two quarters (≈ day 280); Continuing €30,000/yr maintenance from the operating budget, nothing incurred yet; reconciled reserve (€160,000 cash, 0 weeks after the day-47 REC-1 draw and the day-100 data-quality draw); expansion decision at the next quarterly review ≈ day 190, not before month 13.
- Medium — qualify control and retained interests by transaction form (IPO share classes; sellers may keep a minority; "nothing changes" for fund interests is stronger than the fact supports; Facebook S-1 fetched for the ten-votes-per-share basis).
- Medium — distinguish obligations from deferred choices (contractual obligations, funded work, accepted risks, options awaiting evidence).
- Medium — complete one accepted handover (receiver Ines; board nominee received for information; Priya's continuing accountability; exception = the €30,000/yr maintenance against a budget the new board has not adopted; acceptance signed day 130; next review ≈ day 190).
- Low — universal opening claims trimmed. Separate-scenario statement for the financing-delay chapter present in article and summary.
- Summary trimmed from 545 to 500 words. Spec changelog.
**Adapted:** none.
**Declined:** Medium — comic (not created per instruction); header logo still absent; icon now exists.
**Unresolved / needs separate action:** comic and logo for this page remain open. Sibling summaries over 500 at that moment: 17 (597, since fixed), 18 (604, agent running), 11 (511, since fixed), 15 (503), 24 (501, since fixed).
**Verification:** full ledger arithmetic; cross-post agreement with 17 and toolkit; thirteen cross-links resolve; reused figure resolves via the asset merge. Build not run.

## 21-hilton-and-skype — Hilton and Skype: A Successful Exit Still Needs Explaining (`hilton-and-skype`)

**Files changed:** index.md, summary.md, comics.md, spec.md; cross-post: bibliography/index.md (new entries S64, S65 and the Hilton/Skype topic-index row)
**Implemented:**
- High — correct the Skype "not dated" claim → from the S-1/A (S27): Qik acquired January 2011 (~$121m); group video calling January 2011; Citrix GoToMeeting partnership March 2011; Joltid rights November 2009; headcount 733 → 911 during 2010. The Skype IP paragraph, the "Documented change" row and the opening table now carry these dates, with "A date places each event inside the ownership window; it does not isolate that event's contribution to the sale price."
- Medium — establish OnQ's inherited baseline → Hilton 10-K FY2003 (OnQ introduced 2003, substantially all hotels) and FY2005 (virtually all hotels as of 31 Dec 2005), cited as new S64 and S65. Chronology paragraph and "Inherited capability" row state that Blackstone inherited OnQ; "Remaining uncertainty" now concerns only what changed during ownership and its contribution.
- Medium — separate missing attribution from missing chronology throughout → KEY POINTS bullet 2 ends "a filing that dates a system or an acquisition does not measure what it added to the sale price"; summary Hilton and Skype paragraphs carry the dates and the attribution limit; comic panel 2 caption updated (dialogue unchanged, no flag); closing common-limit paragraph opens with what the material does date.
- Low — consolidate closing qualifications → removed three repeated "does not show/prove" sentences; structure kept.
- Low — proportionate investor callout → "cite exits like these as evidence that their approach works; … judge whether it can be repeated."
**Adapted:** "Inherited" wording expanded to cite both filings and the end-2005 full deployment; bibliography entries S64/S65 appended (IDs never reassigned; S63 was the last used) because S-numbered citations require register entries.
**Declined:** none.
**Unresolved / needs separate action:** comic panel 6 artwork mismatch confirmed (image bubble "Which question transfers to our situation?" vs dialogue "Two cases, two different decisions.") → `needs_regeneration: true`, not regenerated. The 2013 S-1's separately named reservation and guest-profile systems are not individually dated by the 2003/2005 filings; the article dates OnQ only.
**Verification:** Skype S-1/A (0001193125-11-096544), Hilton 10-K FY2003 (0001047469-04-007535) and FY2005 (0001104659-06-016388) fetched from SEC. eBay €375m + €630m = €1,005m annotation unchanged. Summary 495 words (trimmed from 501). Article prose 2,384 → 2,518 words; timetoread 10 min unchanged. Six comic JSON blocks parse; only panel 6 flagged. [[visma]] resolves. Build not run.

## 22-visma — Visma: Continuity of Manager Is Not Continuity of Money (`visma`)

**Files changed:** index.md, summary.md, comics.md, spec.md
**Implemented:**
- Medium — replace "no exit" in the opening → opening now contrasts outright sales with "a continuing company-and-manager relationship through repeated investor entries and exits"; KEY POINTS, post-map paragraph and comic panel 2 caption say "one investor's announced complete exit"; the 2017 map row reads "announced June 26, 2017 with completion stated as subject to regulatory approval"; the sources line says the map records what was announced, not what was confirmed to have completed. Summary matched.
- Medium — do not assume one fund holds the majority → authority-and-budget check asks which vehicles hold the interests and how their rights are exercised "without assuming that one fund holds the majority (the map leaves Hg's 2023 vehicles unnamed)"; post-map paragraph explains a manager's aggregate stake can sit in several vehicles. Summary and comic panel 6 ("Which vehicles, which budget, which definition?") matched.
- Medium — qualify "the right basis for comparing product lines" → "one basis for comparing operating performance, alongside the full cost of the strategy; an acquisition-heavy product line can also need recurring integration resources that the adjusted figure leaves out." WHY INVESTORS CARE now asks for the earnings definition and its reconciliation to the budget measure rather than an identical metric.
- Low — remove editorial navigation language → "This chapter is the book's home for that lesson" replaced by a substantive handoff to [[teamsystem]].
- Comic panel 6 verified against the image: embedded speech is "What changed behind the familiar name?" (tabs OWNER/COMPANY/SUPPORT), matching neither the previous nor the new text → `needs_regeneration: true`.
- spec.md revised 2026-09-15 with Changelog line.
**Adapted:** panel 2 caption changed, dialogue unchanged, no flag. All verified historical figures and the €892.646m + €11.665m = €904.311m bridge left as they were; no Visma CDN download attempted.
**Declined:** none.
**Unresolved / needs separate action:** panel 6 artwork mismatch (flagged, not regenerated). Bibliography S62 could add "completion stated as subject to regulatory approval" for consistency (not required). Fund-level cash flows, which Hg vehicles hold the 2023 stake and whether the 2017 completion occurred remain unestablished, as the article now states.
**Verification:** Hg's 26 June 2017 announcement fetched (completion subject to regulatory approval; £101m via Hg5 in 2006; Hg7 in 2014; 41% / c.17% Cinven / 7% management; £238m further; c.£1.4bn equity; NOK 45bn / £4.2bn / US$5.3bn) — all map cells agree. Summary 499 words (down from 518). Four cross-links resolve. Dependent posts (part-6-intro, 24, 31, 21) checked for "no exit"/"majority fund" language — consistent, no edits. timetoread 12 min unchanged (+~140 words). Build not run.

## 23-toys-r-us — Toys R Us: Positive Operating Earnings, Too Little Cash (`toys-r-us`)

**Files changed:** index.md, comics.md, spec.md (summary.md unchanged)
**Implemented:**
- Medium — say "negative operating cash flow" in comic panel 3 → panel 3 speech is now "Positive operating earnings; almost no operating cash flow."; comic intro "almost no operating cash" → "almost no operating cash flow"; `needs_regeneration: true` added (image still shows the 13 September bubble "Earnings do not fund every obligation."). Article table gained "Cash and cash equivalents at year end (a balance, not a flow) | 566" and a paragraph on $566m cash / $1.5bn liquidity: a year of operations added nothing to it while $252m of capex was spent.
- Medium — one duration for the technology program → "three-year technology program" → "multi-year"; "over three years" → "over several years"; table row stays "One specified program across 2018–2021, in total"; no "three-year" remains in any format.
- Low — debt-service observation tied to its period → "Debt service is an annual cash demand in this account; the technology figure is the total of one proposed program across four years."
- Low — compress repeated transfer cautions → removed two of three restatements near the ending; kept one common limit and the transfer scope sentence.
- WHY INVESTORS CARE shortened to a financing consequence (debt service fixed at purchase consumes the room for the transition); removed loose "runs out of cash".
- spec.md revised 2026-09-15 with Changelog line.
**Adapted:** added the year-end cash balance and liquidity to the article (fetched) so the "not a negative cash balance" distinction is visible to readers.
**Declined:** no cash balance added to summary.md (already states operating cash flow correctly; 490/500 words).
**Unresolved / needs separate action:** comic panel 3 artwork mismatch (flagged, not regenerated); fiscal 2016 10-K (S34) access gap remains; no cross-post edits.
**Verification:** S35 earnings release fetched (operating earnings $460m; interest $(457)m; net loss $(29)m / $(36)m attributable; operating cash flow $(1)m vs $238m prior; capex $(252)m; cash $566m; liquidity $1.5bn = 566 + 905). Panel 3 image read and sha256 matched metadata; comics JSON parses for six panels. Summary 490 words. Five cross-links resolve. timetoread unchanged. Build not run.

## 25-teamsystem — TeamSystem: Each New Owner Inherits Progress and Unfinished Work (`teamsystem`)

**Files changed:** index.md, summary.md, comics.md, spec.md; cross-post: bibliography/index.md (S66–S71 appended; TeamSystem topic row extended)
**Implemented:**
- High — correct the finance-cost/cash explanation and the claimed evidence gap → bridge row "Less net finance cost, an accounting charge"; the €72.039m net charge's non-cash items named (vendor-loan remeasurement €15.290m, discounting €5.376m, amortized fees €6.859m, offset by a €7.467m gain); Note 10 cash figures reported (€52.1m finance costs paid, including €49.8m note interest = €13.5m + €36.3m); the cash-flow statement nets payments against €31.8m new borrowing (−€20.393m); the chapter's rough check 72.039 − 15.290 − 5.376 − 6.859 + 7.467 = 51.981 ≈ €52.0m labelled as the chapter's, not the company's; €2.026m fees and €11.149m vendor-loan payments on separate lines. KEY POINTS, section close, Question 3, summary and comic panel 5 caption agree.
- Medium — update the 2024 verification limit using the later report without merging unlike figures → July 2024 announcement (£24.3m agreed vs £22.1m carrying; completion subject to conditions) kept; the 2024 annual report's £34.189m gross proceeds under "Full realisations" and "£34.2m returned" added separately with the footnote's scope; the report does not reconcile with £24.3m; net investor cash not stated anywhere. "Retained investment value" used (index, summary, comic panel 3).
- Medium — keep announced and completed events distinct → 2021 completion verified from the 2021 annual report; August 2023 partial sale described as announced and listed among post-year-end realizations (≈£8m); Silver Lake row reworded (€600m minority from H&F, closing expected end-2023, completion not verified here).
- Medium — remove universal payment timing from the accounting explanation ("Capitalization does not eliminate the underlying cash cost; it changes when the cost reaches profit"); amortization wording corrected. Summary matches.
- Low — heading "From Adjusted EBITDA to the Statutory Loss"; nine non-core components moved below the table.
- Spec revised 2026-09-15; timetoread 15 min unchanged.
**Adapted:** primary sources cited as S66–S71 rather than inline links; two annual-report entries moved out of To Probe Further into the body citations.
**Declined:** none.
**Unresolved / needs separate action:** no comic flags (captions only). Bibliography S49 consulted scope should add Notes 7, 8 and 10 and the cash-flow statement (pp. 26, 48–49). Completion of the Silver Lake purchase and the August 2023 partial sale not verified (labelled). The £34.2m vs £24.3m gap is not reconciled by any source.
**Verification:** TeamSystem 2017 report text-extracted (finance income/costs, Note 10, cash-flow lines); HgT annual reports 2021, 2023, 2024 downloaded and quoted (pages listed); HgT January 2021 and July 2024 announcements and Silver Lake May 2023 release fetched. Summary 499 words. Six cross-links resolve. Build not run.

## 24-success-for-whom — Success for Whom, and for How Long? (`success-for-whom`)

**Files changed:** index.md, summary.md, spec.md (comics.md already rewritten in commit 4bd1d51: panels 5 and 6 carry the thirty-customer decision, the refused breach, the two feasible options, the €80,000 cash / €70,000 capacity split and the month-nine review, both flagged `needs_regeneration: true`)
**Implemented:**
- High — distinguish a genuine trade-off from an option that fails the stated constraint → Option A inadmissible; consent-based A′ introduced and now costed ("service credits and the data work come out of the same year's saving, and neither can be priced until the board knows how many customers consent").
- High — establish which part of the €220,000 is an actual saving → €150,000 cash payroll (contract-dependent end date) + €70,000 released support capacity; the half-time role tied to the same person and cost basis: 1,000 h × €75 = €75,000, budgeted at €70,000 (rounding labelled).
- Medium — fund and date the transition → step built months four to six, migration months seven to twelve, Option A's cut-off at the close of month six, so B's ≈€75,000 retention is exactly the two quarters A would have cut; no separate migration cash line; savings from year two; eight engineer-weeks displace the finance-reporting integration.
- Medium — temper the "best documented" claim → "Transaction headlines are the most prominently reported outcome and they answer the fewest questions."
- Medium — carry the corrected TeamSystem verification → case row now gives £24.3 million agreed value and £34.189 million gross proceeds separately, unreconciled, neither a net distribution.
- Summary 498 words; spec changelog.
**Adapted:** comic and Low terminology items verified already done.
**Declined:** none.
**Unresolved / needs separate action:** artwork regeneration for comic panels 5 and 6 (flagged).
**Verification:** €75 × 2,000 = €150,000; 1,000 × €75 = €75,000; €150,000 ÷ 4 × 2 = €75,000; €150,000 − €70,000 = €80,000; calendar against CANONICAL §A; fifteen cross-links resolve; TeamSystem figures checked against 25 and bibliography. Build not run.

## toolkit — Practical Tools for Ownership and Technology Decisions (`toolkit`)

**Files changed:** index.md, spec.md
**Implemented:**
- High — reconcile the whole reserve before calling Stage 5 funded → Stage 2 envelope corrected to €500,000 / 24 engineer-weeks with the day-0 plan itemised (ONB-1 €180,000/12 + REC-1 €80,000/4 + portal research €20,000/2 = €280,000/18; reserve €220,000/6; KNW-1 €0 and four protected specialist-weeks outside the 24). Stage 5 opens with a three-row reserve-reconciliation table (day 0 → day 47 REC-1 retest €20,000/2 → day 100 data-quality €40,000/4: €340,000/24, reserve €160,000/0) and the delegation rule (Ines inside the plan; board for reserve draws and plan changes).
- High — one dated spending record into the handover → Stages 3, 4 and 6: €180,000 committed, ≈€90,000 incurred by day 100, €90,000 payable over the next two quarters (≈ day 280), €30,000/yr maintenance from the operating budget from the next financial year, ≈10 of 12 weeks used; Stage 6 adds the post-day-100 envelope position and a "Receiver and acceptance" row.
- Medium — repair the evidence interpretation and expansion calendar → the two explanations are not exclusive; 40% is "the largest remaining share of effort, not the whole of it"; "binding constraint" removed everywhere (Tool 4 now states the week-three finding and the scope-change path); Stage 5 dates the expansion decision at the next quarterly review ≈ day 190 and retains the not-before-month-13 restriction; gate 2 stated.
- Medium — qualify the avoided-hiring sentence ("No hiring reduction or avoidance has been demonstrated here").
- Medium — complete section navigation → 12 "see Tool N" references are links; 19 anchors added (12 tools, 6 stages, followed-through); 0 dangling.
- Low — minimum-use explanation corrected (one record shown in successive states) and the duplicate closing line removed.
- Tool 4: ten specialist days at €1,500 = €15,000 at most, charged to ONB-1 (no reserve draw); "investor-side sponsor" label. Day-90 measurement / day-100 decision throughout; Stage 3 carries the < 60 / 60–70 / > 70 rule.
- Spec revised 2026-09-15; timetoread 30 min unchanged.
**Adapted:** fictional-scenario disclaimer names the full shared set and flags [[the-financing-slipped]] as separate; Stage 6 gains a KNW-1/REC-1 paragraph with the accepted residual.
**Declined:** none.
**Unresolved / needs separate action:** no comic modality. 31's record confirmed reconciled by its own agent.
**Verification:** full ledger arithmetic recomputed; 30-useful-engagement lines confirm the €1,500 cap and calendar; ten cross-links resolve; anchors 19 defined / 18 referenced / 0 dangling. Build not run.

## fund-economics — Fund Economics: Fees, Distributions and Performance Reports (`fund-economics`)

**Files changed:** index.md, spec.md (no summary or comic by design)
**Implemented:**
- High — correct "a partial catch-up lands between the two cases" → one worked example (committed and contributed €100; sold for €160 after one year; profit €60; carry 20%; 8% preferred return = €8) through four arrangements with a comparison table: capital back then 80/20 → LPs €148 / GP €12 (20%); pref, no catch-up → €149.60 / €10.40 (17.3%); pref + 100% catch-up → band €2, then €50 split → €148 / €12 (20%); pref + 80% catch-up (ILPA model rate) → band €2.6667 (GP €2.1333 / LPs €0.5333), then €49.3333 split → €148 / €12 (20%). Closing paragraph separates the rate during the catch-up from the final entitlement; only no catch-up or a catch-up that never completes changes the final split (worked: sale at €109 → LPs €108, GP €1 = 11%). KEY POINTS bullet 1: "A slower catch-up changes when the manager is paid, not necessarily how much."
- Medium — limit the cash-only definition to its example → "DPI measures distributions relative to paid-in capital; in this example all distributions are cash. RVPI measures remaining net value", with securities and net-asset-value qualifications (ILPA §14.4.1).
- Medium — present deal-by-deal distributions as one arrangement → deal-by-deal vs whole-fund waterfall; ILPA publishes models for both; clawback reconciles interim carry with the whole-fund entitlement.
- Medium — keep receipt, valuation and legal commitment separate without universal rules → "A higher valuation is not itself a cash distribution"; a term sheet sets out proposed terms and does not by itself establish an unconditional commitment to fund; a signed agreement is a contractual, usually conditional, commitment until completion and payment; what can fund a commitment now is the cash held and the facilities authorized to draw.
- Low — GP and LP defined before the first table.
- Spec: body-length criterion raised to about 1,800 words (body 1,809; HEAD 1,342); Sources line updated; Changelog extended. timetoread 7 → 8 min.
**Adapted:** ILPA catch-up citation re-pointed to the whole-of-fund model LPA PDF §14.3.3–14.3.4; §14.4.1 added.
**Declined:** none.
**Unresolved / needs separate action:** the two inline ILPA model-LPA links are not S-numbered bibliography entries (coordinator/bibliography).
**Verification:** every waterfall figure recomputed with exact fractions; ILPA whole-of-fund model LPA (October 2019) fetched and extracted (§14.3.1–14.3.4, §14.4.1, §14.7); deal-by-deal resource URL resolves. DPI 0.6× + RVPI 0.9× = TVPI 1.5×. Chapter 01's year-three row confirmed. Four cross-links resolve; glossary definitions agree. Build not run.

## glossary — Glossary (`glossary`)

**Files changed:** index.md, spec.md
**Implemented:**
- High — replace "A budget can rely only on the last state" / "Only this state funds a budget" → arrangements intro now records each commitment against the state its money has reached: cash held, an authorized facility, or forecast operating receipts in a dated cash plan; an expected round or a commitment with unmet conditions is none of those. Cash-received row: the only state that is money, but not all of it available; do not describe an announced value as received until it arrives. Contractual-commitment row: a written commitment is not cash received; a plan may rely on it only where the decision-maker authorized that reliance with a dated forecast and a funded fallback.
- Medium — term sheet / transaction status → term sheet does not by itself establish an unconditional commitment to fund; announced value: an announcement does not establish receipt or realization; expression of interest "supplies no money".
- Medium — accountability and approval as separate roles → accountable company leader answerable within a remit (Priya accountable for the pilot; the board approves its expansion); investment committee approves the fund's investments, not company operating work; shareholder approval rights come from the agreements.
- Collection item 5 — advisory involvement is not authority → new Authority row (sources: executive role, board responsibilities, agreed shareholder rights, explicit assignment, applicable rule or law; influence and proximity create none); adviser and operating-team rows aligned.
- Collection item 5 — debt investors are still investors → Investor row covers ownership interests and contractual rights to repayment; new Lender row; Debt row notes the lender's return.
- Medium — certification → editorial objective: the glossary states the terminology the chapters aim to follow; a definition cannot make a worked example accurate by declaration.
- Fund terms aligned with [[fund-economics]]: catch-up rate sets speed, final share set by the end condition and whether proceeds suffice; waterfall by investment or whole fund as the agreement specifies; RVPI as remaining net asset value.
- Low — index entries added: Audited financial statements, Term sheet, Terminal value, Authority, Lender (284 links).
- spec revised 2026-09-15 with Decision-log and Changelog lines.
**Adapted:** SBA credit-line citation not added; principle stated without a source.
**Declined:** per-row anchors (optional).
**Unresolved / needs separate action:** chapters must land on the same conditions (18's restart rule and comic panel 3; 15 / part-2-intro authority wording). The Priya/board parenthetical follows CANONICAL.md section A. No timetoread.
**Verification:** 284 index links, 0 unresolved, all to the 11 section anchors; 26 distinct cross-link targets resolve; 253 two-cell rows. Home-chapter wording read at the working tree (00, 05, 15, 04, fund-economics). Build not run.

## bibliography — Bibliography and Evidence Guide (`bibliography`)

**Files changed:** index.md, spec.md, `_research/bibliography-revision-history.md`; cross-post: one inline link each in 00-customers-lenders-investors, 06-different-bets, 15-investors-adviser and three in fund-economics, switched to the `[Sxx: …](url)` form.
**Implemented:**
- High — finish verification of consequential annotations → paragraph added to "Evidence Used Versus Further Reading" recording the unicorn study's version difference (NBER w23895: 50% above modelled fair value, 15 of 135 >100%; JFE 135(1) 2020: 48%, 14 >100%) and that "reported values 50% above fair value" is not "fair values 50% below reported values".
- High — update the evidence limits used in the historical cases (S49) → consulted scope now cites PDF pages 9–15, 23, 26, 45 and 48–49 and records Note 8 finance costs €79.674m, Note 7 finance income €7.618m and Note 10's €52.1m finance costs paid (€49.8m note interest = €13.5m + €36.3m; €1.9m other), and why interest paid is not on the face of the cash-flow statement.
- Medium — reconcile the opening date and topic map → "consulted between September 12 and September 15, 2026; each entry carries its own consultation date"; S62 added to the Visma row, S63 to the AI evidence row.
- Medium — register newly relied-on evidence → S64–S71 (added by the Hilton/Skype and TeamSystem agents) verified for format, "Used in" lines and topic rows; new S72 Investor.gov bonds page, S73 ILPA whole-of-fund model LPA, S74 ILPA deal-by-deal model LPA, S75 Fastly Q4 2020 shareholder letter, S76 Avalyn Pharma investors' rights agreement §3.2, each dated 15 September 2026; "The register currently runs to S76."
- Low — repeated method disclaimer reduced; "Every chapter ends with a To Probe Further list" corrected to the main chapters.
- S62 note adds "completion is subject to regulatory approval" (verified live).
- "Used in" lines regenerated by script across posts/*/index.md and the glossary: S02 gained [[investor-under-pressure]]; five entries reordered to chapter order; no entry lost a chapter, none uncited.
- One dated row added to `_research/bibliography-revision-history.md`.
**Adapted:** the unicorn correction lives in the further-reading section (the study carries no S number, per the register's policy); topic-index entry anchors left as plain text because the renderer emits no heading ids.
**Declined:** DORA guide (already S14); ICF Code of Ethics (To Probe Further, not body evidence).
**Unresolved / needs separate action:** no Facebook S-1 or SEC purchase-agreement citation exists in chapters 31 or 16 (those agents fetched them for verification only) — nothing to register. `_research/sources.json` stops at S63 and now lags the register (S64–S76); needs a separate reconciliation. Topic-index anchors await renderer support.
**Verification:** NBER and Stanford GSB pages fetched; S49 figures re-extracted from the cached 2017 report text (page split confirmed: cash-flow p. 26, Notes 7–8 p. 48, Note 10 p. 49; 13.5 + 36.3 = 49.8); S62 live; S64–S71 figures re-extracted from cached HgT PDFs (34,189 under "Full realisations", "Secondary sale"); S72–S76 each verified before registering; 77 identifiers, zero duplicates, S38 the only gap, ascending order, every S entry complete, zero broken cross-links, "Used in" regeneration idempotent. Build not run.

## Open items after this pass

- **Comic panels regenerated (15 September, later the same day):** the twenty panels flagged above were regenerated with the journal's generator (`_research/generate_comics.py`, shared cast reference) after every prompt was realigned with its caption; a read-back of each image found all twenty speech bubbles textually correct and eleven artwork defects (mirrored labels, an inverted debt chart, invented calendar months and tab labels, a missing second person, MORGAN off-model in six panels). Those eleven were regenerated with tightened scene prompts and skin tones added to the generator's cast descriptions; four went through a third pass. Final read-back: nineteen panels match their dialogue and scene. **Residual:** visma panel 6 keeps upright, legible VEHICLES / BUDGET / DEFINITION tabs but its secondary MANAGER folder label renders mirrored (three attempts; the best version kept). Cosmetic slips left as is: toys-r-us 3 shows four document labels on three objects; three-different-returns 4 has a skewed chart panel; investors-adviser 2 has an ambiguous bubble tail. Superseded images are archived in `_research/discarded-comic-variants/`. No `needs_regeneration` flags remain.
- **New pages' visual assets:** `handover-of-obligations` received its six-panel comic and header logo later on 15 September (comics.md written from the revised article; all six bubbles verified exact; panels 2 and 6 keep upside-down prop text on the binder tabs and the handover sheet, re-rolls were worse); the reading guide now says all thirty main chapters have a comic. `fund-economics` still needs a header logo and icon.
- **Reading-guide caveat to remove later:** the guide now says summaries and comics are still being reconciled and the article governs; drop that sentence once the flagged artwork is regenerated.
- **Lengths flagged for the author's discretion:** part-6 introduction (543 words including its case-map table, above the spec's ~400 prose cap, as before this pass); part-5 introduction (468 words); several articles grew by 10–35% to carry completed decisions (funding choice 14 min, adviser 12 min, investor-under-pressure 13 min, decision rights 12 min, roadmap 15 min, organization 14 min, different bets 14 min).
- **Verification that could not be completed:** completion of Silver Lake's 2023 TeamSystem purchase and of the August 2023 HgT partial sale (labelled as announced); the £34.2m vs £24.3m TeamSystem gap is unreconciled by any source; Hg's 2017 Visma completion and which Hg vehicles hold the 2023 stake; the Toys R Us fiscal 2016 10-K remains inaccessible (earnings release used); SSRN/ScienceDirect refused the unicorn paper (NBER and Stanford pages used).
- **Research files lagging the register:** `_research/sources.json` stops at S63 while the bibliography now runs to S76; reconcile separately. Topic-index entry anchors remain plain text until the renderer emits heading ids.
- **Declined for lack of evidence:** a documented minority/venture or corporate-ownership case (collection review); the evidence-scope disclosure stays in the guide, Part VI introduction and bibliography.
