# Plan — Investor Impact on Hiring, Headcount and Layoffs

**Date:** 2026-09-16  
**Status:** implemented 2026-09-16; validation recorded below; artwork generation blocked (see Completion record)  
**Manuscript:** OWNED: Product & Engineering Leadership Under Investors

Expand the leadership material, add one chapter on headcount reductions, and connect the existing coverage into a clear reading route.

The coverage review found strong treatment of hiring budgets, headcount approvals and staffing diagnosis. Investor-driven executive appointments and product/engineering layoffs need more complete treatment. The existing support-location consolidation provides a substantial foundation for discussing employee consequences.

1. **Expand “Fix the Decision Problem Before Adding People.”**

   Keep the staffing diagnosis and CTO assessment in [the organization chapter](../posts/13-fix-decisions-before-hiring/index.md). Add a section on investor involvement in key appointments: proposing roles, introducing candidates, influencing selection, approving compensation, and assessing incumbents. Work through a fictional proposal to appoint a CPO, comparing recruitment with developing the existing leader or adding narrower support. Specify who decides, what authority the role receives, how it is funded, and how success will be assessed. Include the implications for product management, design, research, and engineering responsibilities.

2. **Add “When the Headcount Plan Shrinks.”** (Published title after the author’s later retitle: “Anatomy of a Layoff”; folder `32-anatomy-of-a-layoff` and permalink `anatomy-of-a-layoff`, both renamed from the headcount-plan-shrinks names the same day, before deployment.)

   Place it in **Part V, after “The Roadmap Did Not Slip, the Financing Did,”** with links from the organization chapter. This preserves the existing assessment → organization → design sequence.

   Follow a product and engineering reduction from the investor’s request to an operating plan. Cover the reason for the target, the actual decision authority, alternatives such as hiring freezes, contractor reductions and redeployment, and the consequences of layoffs. Show the resulting team structure, work stopped, customer commitments revised, knowledge transferred, and responsibilities retained. Include communication, employee treatment, and the workload of those remaining.

   Extend the delayed-financing scenario into its unresolved deeper reduction decision. Establish the missing staffing and payroll baseline first, then reconcile notice periods, severance, transition spending, recurring savings, and cash by date. Keep this scenario separate from the main shared Larkspur operating-plan ledger, as the existing financing chapter does. Add short variations for a profitable company pursuing higher margins and acquisition-related consolidation.

3. **Make focused changes to supporting chapters.**

   | Chapter | Planned change |
   | --- | --- |
   | [Decide Who Decides](../posts/05-decide-who-decides/index.md) | Explicitly map authority for executive appointments, headcount changes, and restructuring; distinguish formal rights from funding pressure and informal influence. |
   | [Different Bets](../posts/06-different-bets/index.md) | Retain the support-location consolidation and link to the new chapter for the operating consequences of reductions. |
   | [Find the Help That Changes What Your Team Can Do](../posts/29-help-that-changes-capability/index.md) | Connect investor recruiting support to candidate assessment, conflicts of interest, and company accountability. |
   | [The Roadmap Did Not Slip, the Financing Did](../posts/18-the-financing-slipped/index.md) | Hand the deeper workforce decision to the new chapter. |
   | [An Acquisition Adds Work Before It Adds Value](../posts/14-acquisition-adds-work-first/index.md) | Connect proposed staffing synergies to the new chapter’s transition and capability checks. |

4. **Add practical navigation and tools.**

   Add reading routes in [the introduction](../posts/introduction/index.md) for “the investor wants a leadership change” and “we must reduce headcount.” Extend [the toolkit](../posts/toolkit/index.md) with a workforce-decision record covering the investor request, decision authority, alternatives, roles and capabilities affected, cash timing, work stopped, employee consequences, and review date.

5. **Implement through the existing authoring workflow.**

   Update specifications before articles. Research and cite new factual claims, clearly label fictional examples, and keep employment-process details tied to their jurisdiction. Synchronize summaries, six-panel storyboards, illustrations where affected, bibliography, chapter order, introductions, and book indexes.

6. **Validate the completed revision.**

   Check financial calculations, staffing totals, approval consistency, scenario continuity, links, navigation, and rendered reading formats. Review specifically for duplication and unsupported assumptions about investor types.

**Acceptance criterion:** a reader should be able to handle an investor-proposed executive appointment, a changed hiring budget, and a product/engineering reduction—from the initial request through an authorized, funded plan and its consequences for people and delivery.


---

## Completion record (2026-09-16)

Implemented by an AI-mediated session against the working tree at commit `1d9b0c3` (the author’s staged `manuscripts/owned/resources/title_page.jpg` was left untouched). Dispositions per page are in `posts/REVISION_LOG.md` (section “investor impact on hiring, headcount and layoffs”). Every affected specification was revised before its article.

| Step | Status | Where |
| --- | --- | --- |
| 1. Expand “Fix the Decision Problem Before Adding People” | Done | `posts/13-fix-decisions-before-hiring/` spec, index (new section “When the Investor Proposes an Appointment”: five forms of involvement; formal right / funding condition / influence; CPO proposal compared as recruit / develop / narrower support and decided with authority, funding and success evidence; responsibility table for product management, design, research and engineering), summary, comic panel 4 caption |
| 2. Add “When the Headcount Plan Shrinks” (retitled “Anatomy of a Layoff”) in Part V after the financing chapter | Done (text); artwork blocked | `posts/32-anatomy-of-a-layoff/` (spec, index, summary, comics), `config.yaml`; permalink `anatomy-of-a-layoff` |
| 3. Supporting chapters | Done | `05-decide-who-decides` (table rows, three-pressures passage, summary), `06-different-bets` (link), `29-help-that-changes-capability` (recruiting-support passage), `18-the-financing-slipped` (handoff, summary), `14-acquisition-adds-work-first` (synergy link), `31-handover-of-obligations` (opening, recap, summary) |
| 4. Navigation and tools | Done | `introduction` (two routes, counts, contents), `toolkit` (Tool 13 and its navigation row), `part-5-intro`, `part-3-intro`, journal `index.md`, `README.md`, `STRUCTURE.md`, `PLAN.md` |
| 5. Authoring workflow: specs first, sources, labels, synchronization | Done except artwork | Specs revised first (13 changelogs dated 2026-09-16); S77–S78 registered and S76 widened in the bibliography with `_research/bibliography-revision-history.md` updated; glossary terms added; summaries and storyboards synchronized; prompts staged for the new chapter’s logo, icon, TL;DR visual, two figures and six panels |
| 6. Validation | Done with the limits below | This record |

### Scope reconciliation

- The new chapter continues the delayed-financing scenario and keeps it separate from the shared Larkspur ledger (stated in the article, the TL;DR and the storyboard; `_research/shared-scenario-record.md` section A unchanged). Its baseline reproduces the earlier chapter’s figures: €324,000 payroll + €50,000 contractors + €76,000 non-payroll − €250,000 revenue = €200,000 burn; €150,000 after R1; €500,000 on 31 December without the bridge.
- Cash by date under R2 (eight roles, €63,000 payroll + €9,000 non-payroll = €72,000 a month from February; €120,000 one-off paid November–January): 31 Oct €800,000; 30 Nov €1,220,000 (bridge €600,000 received); 31 Dec €1,045,000; 31 Jan €895,000; then −€78,000 a month to €505,000 on 30 June and €427,000 on 31 July, reserve reached in the second week of August. Without R2: €200,000 on 30 June, reserve in mid-May (matches the earlier chapter’s “about mid-May”). Without the bridge: €295,000 on 31 January with R2 (breach about 9 January) against €350,000 without it (breach about 20 January, as the earlier chapter says). Recomputed by script during the session.
- The CPO options use fictional figures (€180,000 + equity; €15,000 coaching; €95,000 senior product manager) and the existing chapter’s trace evidence; the second team remains conditional as before.

### Validation evidence

- **Build:** `python3 _wiring/build.py` → `[built] private-techuity`; `docs/private-techuity` now has 87 files (was 85): `anatomy-of-a-layoff.html` and `.spec.html` added. No output changed outside `docs/private-techuity`.
- **Configuration and links:** 42 configured posts = 42 folders; 0 unresolved `[[…]]` links across all post files and the journal index; toolkit and glossary anchors all resolve (glossary index 294 links); every cited `[S..]` identifier is registered (79 identifiers); “Used in” lines for S76–S78 match the citing chapters.
- **Reading formats:** all 31 TL;DRs are 300–500 words (the four edited ones were trimmed back to ≤ 500); the new storyboard passes the skill validator (`generate_comic_panels.py --dry-run`) and the journal generator’s assertions (`_research/generate_comics.py --dry-run --post 32-anatomy-of-a-layoff`: 6 panels, captions in prompts, panel text present); the two article placeholders and the TL;DR placeholder pass the illustrator’s and the summary-visual generator’s dry runs.
- **Manuscript:** `manuscripts/_scripts` unit tests 11/11 OK; export with the committed options (`--journal _journals/private-techuity --output manuscripts/owned --max-manuscript-mb 40`) → 42 articles, 31 main chapters, 23.78 MB; `validate_manuscript.py --source` → `[valid]`, 968 internal links; `Book.txt` places `anatomy-of-a-layoff.md` between the financing and handover chapters; 21 generated files changed, all attributable to this revision; the exporter notes the missing logo for `anatomy-of-a-layoff` (and `fund-economics`, as before).
- **Rendered pages:** headless Chrome (`--headless=new --dump-dom`) rendered `anatomy-of-a-layoff.html`: Article / TL;DR / Comic tabs present, eleven `h2` headings, previous/next navigation to the financing and handover chapters, spec link, four tables, summary and comics payload keys, article text present, no JavaScript errors in the Chrome log; a 1440px-equivalent DOM check and a 390px screenshot were taken. The 390px screenshot shows the same right-edge cropping on an unchanged existing chapter, so it reflects a headless-viewport limitation rather than new overflow; the template’s tables are `width: 100%` with wrapping cells, and the new chapter adds no `.table-wrap` tables wider than existing ones. A DevTools-driven overflow measurement was not possible in this session (no browser automation available). A sequential headless-Chrome check of ten further built pages (index, introduction, toolkit, fix-decisions-before-hiring, decide-who-decides, part-5, glossary, bibliography, the-financing-slipped, handover-of-obligations; after the rename to `anatomy-of-a-layoff`) rendered each page in about 41 seconds with no page JavaScript errors; the single console error logged on the glossary page came from a browser extension’s service worker, not the page. The rendered financing and handover chapters carry the new chapter’s link under its final permalink; the index and Part V pages were rendered before the rename and carried it under the earlier one, and the rebuilt sources of both now reference `anatomy-of-a-layoff` only. The rendered toolkit, glossary, bibliography and introduction pages carry Tool 13, the new glossary rows, S78 and the new reading routes.
- **Sources:** Directive 98/59/EC articles 1(1)(a), 2(1), 3(1) and 4(1) read in the legislation.gov.uk copy (EUR-Lex refused automated access; recorded in S77); 29 U.S.C. §§ 2101–2102 read in the Cornell LII copy (S78); the Avalyn Pharma agreement §5.4(g) read on sec.gov (S76 widened). Reading-list items verified: HBR 2018 (page fetched), Wasserman 2008 (page fetched; used only to check the ch13 list, not added), Trevor and Nyberg 2008, Datta et al. 2010 and Brockner 1992 (Crossref metadata; publisher pages returned 403).
- **Diff review:** `git diff` over `_journals/private-techuity` (41 modified files, 240 insertions, 99 deletions, plus the new chapter folder and this plan) read in full against steps 1–6; no permalink or `id` changed; no chapter figure in the shared ledger changed.

### Review response (16 September 2026, later the same day)

Five review findings were fixed with specifications revised first (`posts/32-anatomy-of-a-layoff/spec.md`, `posts/13-fix-decisions-before-hiring/spec.md`); dispositions are in `posts/REVISION_LOG.md` under “Review response”. In brief: the second second-country customer’s contractual 30 June date is met by sequencing its configuration first, with a funded contingency as the fallback and its termination right kept as a recorded risk (the TL;DR no longer says both customers were renegotiated); the CPO decision carries the full consent requirement and places the senior product manager in a board-approved second-team role, stating that cash alone does not establish hiring authority; the cash-timing conclusion is conditional on Larkspur’s notice, severance and dates in every format; the knowledge-transfer fallback is a funded, bounded fixed-term extension (up to €17,000, 1 February to 31 March, by agreement, retest 15 January, re-planning 1 April) whose full use leaves €488,000 on 30 June and moves the reserve date from the second to the first week of August, recomputed by script; the employment-law summary, S77, S78 and the glossary row were corrected against the re-read statutes. Validation after the fixes: build `[built]`, 87 output files; 0 unresolved cross-links; all citations registered; all 31 TL;DRs within 300–500 words; comic and illustrator dry runs pass; manuscript re-exported and `[valid]`; the corrected examples keep the book’s rules (the board with the investor director’s consent approves the plan change, Ines appoints within the approved headcount plan, no customer contract is breached without consent, and the contingency is funded inside the plan). Headless Chrome re-rendered the corrected reduction chapter, the organization chapter and the index after the fixes (about 42 seconds each, no page JavaScript errors; the corrected passages present in the rendered text). Mobile overflow could not be measured in this session for the reason given above. At the author’s request the chapter now opens with the two-sided effect of outside investment on a team.

### Second review response (16 September 2026)

Four findings remained after the first response, whose customer-sequencing, December-test and 15 January entries above are superseded. The second customer’s first-quarter promise is now kept by retaining one second-country specialist to 31 March under an agreement recorded before the notices (the €17,000 is in the plan, not a contingency); the first customer’s amendment moves both its go-live and its termination deadline to 30 September; the transfer test runs on the real work in March with a single funded further month as the only fallback and board re-planning on 1 May; the reviews are re-dated to the evidence available; the employment-law passage is split into four paragraphs and corrected to 33 percent and to hours exclusive of overtime. Recomputed by script: savings €20,000, €45,000, €63,500, €63,500 then €72,000 from April; one-off €30,000, €45,000, €32,000, €13,000; cash €908,000 (January), €821,500, €722,000, €644,000, €566,000, €488,000 (30 June), €410,000 (July); reserve reached in the first week of August; contingency case about €480,000 at 30 June; without the bridge the reserve is breached in January about ten days earlier than under R1 alone. Validation after the fixes: build `[built]`; 0 unresolved cross-links; all citations registered; all 31 TL;DRs within 300–500 words; comic and illustrator dry runs pass; manuscript re-exported and `[valid]`; the corrected chapter re-rendered in headless Chrome after the fixes (about 42 seconds, the corrected passages present in the rendered text, no page JavaScript errors; the one console error logged came from a browser extension’s service worker). Mobile-width overflow still could not be measured with the tooling available. The corrected examples keep the book’s rules: no customer promise is reinterpreted without a signed amendment, the retention is funded inside the adopted plan, the board with the investor director’s consent approves the plan, and Ines gives notices within it.

### Blocked or open

- **Artwork for the new chapter** (six comic panels, two article figures, the TL;DR overview visual, the header logo and the navigation icon): prompts are staged in the files and in `_research/logo-and-icon-prompts-20260913.json` and `_research/summary-visual-prompts-20260913.json`; generation needs `GEMINI_API_KEY`, which was not available in this session. Until then the chapter page renders without a hero image and its Comic tab shows captions and dialogue only; `README.md` and the journal `index.md` say so.
- `_research/sources.json` still stops at S63 (pre-existing lag; S77–S78 not added there to avoid a partial update).
- The introduction’s caveat that summaries and comics are “still being reconciled” remains, as before.
