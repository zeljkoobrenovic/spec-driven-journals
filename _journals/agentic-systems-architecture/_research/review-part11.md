# Review — Part XI (Domains), 2026-10-28

Scope: 41-domain-coding-agents, 42-domain-customer-operations, 43-domain-back-office, 44-domain-high-stakes-decisions. The part-11-intro was not touched; another agent is writing it. Rulings applied: 1–27 (including the coordinator's mid-review items 24–27).

## Word counts (front matter to "Sources and Evidence", without tables' pipes, code or mermaid)

| Chapter | Before | After |
| --- | --- | --- |
| 41 domain-coding-agents | 7,449 | 7,456 |
| 42 domain-customer-operations | 7,108 | 7,120 |
| 43 domain-back-office | 7,739 | 7,737 |
| 44 domain-high-stakes-decisions | 7,521 | 7,584 |

All four were already under 8,000 words, so no length cuts were needed. Format checks passed in all four: exact callout labels, three KEY POINTS, 2–3 failure patterns with exact names, "What Transfers to Other Domains", Questions to ask, a hand-off, grouped sources and the closing disclaimer. The domain chapters link to the mechanism owners and do not re-teach them; each incident is retold in one or two sentences with a link, except the Fixture Purge, which chapter 41 owns.

## 41 domain-coding-agents

Issues found and fixes made:
- The rule "repository content never grants authority" cited "consistency issue 7", which is the wrong ruling (7 is the deterministic rule layer). Removed the citation.
- The AmPermBench result was misdescribed. Before: "81% end-to-end false-negative rate on 128 … prompts". After: "built from 128 deliberately ambiguous DevOps prompts … 81% … over 253 state-changing actions; 36.8% of those actions in-project edits". The Sources entry now carries the paper's real title, *Measuring the Permission Gate: A Stress-Test Evaluation of Claude Code's Auto Mode*, v3 dated 2026-10-22.
- Added METR's 95% interval (5–40 h) to the 11-hour estimate. Replaced "treats none … as robust" (a banned word in the author's own voice) with METR's own quoted wording.
- Hand-off sentence. Before: "the reviewer is a support lead with six seconds per approval". After: dated to Q2 2027 as a median, since the Q3 R1 median was 18 s.
- Checked and left unchanged:
  - Fixture Purge dates (5, 8, 13, 14, 16 and 19 July; 9 August) and counts (9 PRs, 2 merged, about 1,100 order lines) match ruling 24 and the ledger.
  - The split harness matches ruling 20.
  - The merge tier is A0.

Sources spot-checked:
- anthropic.com/engineering/claude-code-auto-mode → **verified** (25 Mar 2026; 93% of prompts accepted; 0.4% false positives at n = 10,000; 17% false negatives at n = 52; quote verified).
- metr.org/blog/2026-06-26-gpt-5-6-sol → **verified** ("packaging exploits" quote; 11.3 h vs "beyond 270hrs"; METR's not-robust caveat).
- arxiv.org/abs/2604.04978 → **partly wrong; fixed** (n = 253 actions, not 128 prompts; title corrected).
- stripe.dev/blog/minions… → **verified** (9 Feb 2026; over 1,000 PRs a week, human-reviewed, isolated from production and the internet, at most two rounds of CI).

## 42 domain-customer-operations

Issues found and fixes made:
- **Ruling 19 (turn vs exchange).**
  - Before: "in every turn" / "Inside a live turn" / "inside a turn" / "in the turn" (×2) / "No turn budget".
  - After: "reply" / "exchange" / "within the exchange" / "No exchange latency budget".
- **Second-reviewer sampling.** Before: "One in twenty A2 credits" and, in the controls table, "5% second reviewer weekly". After: "One in ten executed A2 credits" and "10% second-reviewer sample of executed credits", per the ledger line for human-oversight-and-bounded-autonomy (10% after the October 2027 A2 promotion). The link now goes to human-oversight-and-bounded-autonomy.
- **Ruling 26.** Before: "200 injection cases". After: "200-case injection gate sample (of the 1,200-variant suite)".
- **Date logic error in the end-to-end conversation.** The conversation was dated Monday 22 November 2027, but the customer's Assure contract ends 31 January 2028. That is 70 days away, outside the 60-day reminder window the chapter itself uses, and the reminder was only in shadow mode then. Changes:
  - Chat date: 22 Nov → Mon 6 Dec 2027.
  - Missed visit: Fri 19 Nov → Fri 3 Dec.
  - Resolution counted: 29 Nov → 13 Dec.
- **τ²-bench.** Before: "cut pass^1 by about 18 to 25 points for the models tested". After: "in its telecom domain … by 18 and 25 points for the two models compared" (the paper gives 18% for gpt-4.1 and 25% for o4-mini).
- **Promised Credit re-audit.** The chapter had added detail not in the ledger, and it contradicted itself ("scan flagged both, regeneration failed, … approved"). Replaced with the ledger's facts: 2 premature statements in 500; no customer told of a credit that did not happen.
- **Double Credit row.** Before: "212 duplicate credits, €31,400, reversed". After: "212 customers with duplicate credits, €31,400", linked to [[retries-idempotency-and-concurrency]]. No chapter records a reversal, and chapter 40 treats clawback as an open decision for the risk owner.

Sources spot-checked:
- mltaikins.com (Moffatt v Air Canada, 2024 BCCRT 149) → **verified** (negligent misrepresentation; CA$650.88; "no reason why the customer should know" quote). It is still secondary; the chapter already labels it that way.
- klarna.com press release, 27 Feb 2024 → **verified** (2.3 million conversations, two-thirds, 700 FTE, 25% fewer repeat inquiries, 11 → under 2 minutes, $40 million).
- arxiv.org/html/2406.12045 (τ-bench) → **verified**:
  - retail pass^1 61.2;
  - pass^8 below 25%;
  - policy ablation: retail 61.2 → 56.8, airline 33.2 → 10.8. Note that the paper's Table 2 gives airline as 35.2; the chapter uses the ablation table's 33.2 baseline, which is correct for that comparison.
- arxiv.org/html/2506.07982 (τ²-bench) → **imprecise; fixed** (see above).
- Regulation (EU) 2026/1744 → OJ metadata fetched: publication 24 July 2026, in force 27 July 2026. Corroborated by euaiact.com, the CSA and Gibson Dunn: Annex III → 2 Dec 2027, Annex I → 2 Aug 2028, Art. 50(1) unchanged (only 50(7) amended; the 50(2) legacy transition runs to 2 Dec 2026). The chapter's claims hold. The articles of the OJ text were not read directly.

## 43 domain-back-office

Issues found and fixes made:
- Removed "*(Ostrell, illustrative date)*" from 23 November 2027. It is a canonical ledger date (from the domain-back-office additions).
- Peoplepoint tool-change example. Before: a hypothetical "suggest a development rating draft for managers". After: the People team's November 2027 request to draft performance-review summaries, linked to [[domain-high-stakes-decisions]], to match chapter 44 and ruling 27.
- Checked and left unchanged:
  - Employment decisions are already A0 (ruling 27).
  - 380 entries a day, 48-working-hour timer and the September 2027 close figures (1,912; 44 of 61; 9; 3; 6) match the ledger.
  - The interim audit figures (2 h vs 2.5 days) and the Quiet Failover (46 calls, 9 contracts; 23 held on 19 Oct) match.
  - Day-of-week check: Mon 1 Nov 2027 and Tue 23 Nov 2027 are correct.

Sources spot-checked:
- blogs.mcguirewoods.com (*United States v. Heppner*) → **verified** (Rakoff J; bench ruling 10 Feb 2026; written opinion 17 Feb 2026; about 31 documents; the privacy-policy reasoning; counsel-directed use left open). It is still a secondary account, and the chapter already says so.
- federalreserve.gov SR 26-2 letter and attachment → **verified** (17 Apr 2026; Fed, OCC and FDIC; "supersedes and replaces" SR 11-7; quote "Generative AI and agentic AI models are novel and rapidly evolving. As such, they are not within the scope of this guidance"; "effective challenge" retained).
- judiciary.uk *Ayinde / Al-Haroun* [2025] EWHC 1383 (Admin), 6 June 2025, full PDF → **verified**:
  - five fake cases in *Ayinde*;
  - 45 citations, 18 non-existent in *Al-Haroun*;
  - all three quotes;
  - contempt threshold met but proceedings not initiated, partly because of training and supervision questions.
- Regulation (EU) 2026/1744 dates → **consistent** (see chapter 42).

## 44 domain-high-stakes-decisions

Issues found and fixes made:
- **Ruling 27.**
  - Scene, before: "Employment decisions are already capped at A1 in Ostrell's register". After: A0 for decisions about an employee; a summary the manager rewrites is not a decision.
  - Closing, before: "Summaries would stay at A1 with the manager as accountable author". After: an internal draft the manager rewrites and signs, outside any action class until Legal approves one.
  - Spec source line changed from "A1 cap" to "A0 rule (ruling 27)".
- Before: "That request moves Peoplepoint into Annex III". After: "could move", with the date attributed to Regulation (EU) 2026/1744.
- The decide/veto/screen sentence claimed that ruling 7 *separates* the roles; ruling 7 calls them one pattern. Reworded.
- Back to Ostrell. Before: "samples 5% of approved credits". After: "10% of executed credits up to €250".
- Robodebt. Before: "A class-action settlement exceeded A$720 million and covered about 430,000 debts". After: "about 430,000 debts were reimbursed, worth more than A$720 million before damages and costs" (the LSJ wording).

Sources spot-checked:
- APRA Robodebt overview PDF → **verified** ("produced inaccurate results and did not comply with the income calculation provisions of the Social Security Act"; report released 7 July 2023).
- lsj.com.au → **verified with a correction** (57 recommendations; about 430,000 debts reimbursed for more than A$720 million; wording fixed).
- University of Michigan STPP MiDAS PDF → **verified** (about 40,000 wrongly accused; quote verified; $20 million *Bauserman* settlement approved by the Court of Claims in late January 2024).
- jamanetwork.com (Goh et al., 2024) → **verified** (50 physicians; 76% vs 74%; adjusted 2 points, 95% CI −4 to 8; LLM alone +16 points).
- cooley.com FDA CDS → **verified** (revised final guidance 6 Jan 2026; a single recommendation can be non-device CDS; automation bias under criterion 4; time-critical recommendations; nothing on LLMs).
- Regulation (EU) 2026/1744 → **consistent** (24 July 2026; Annex III 2 Dec 2027; Annex I 2 Aug 2028).

## Interview-derived designs

All four chapters label the interview material as design examples, give the path and step, and cite it in a separate Sources group. Chapter 44 uses step numbers plus names (e.g. "step 4 `safety`"); chapters 41–43 use step ids. No change was needed.

## Verification

- `python3 _wiring/build.py` → `[built] agentic-systems-architecture`.
- `render_check.py`: all four pages have 0 mermaid failures. The only unresolved link is `[[source-coverage]]` in chapter 44, a reference page not yet written; this is allowed.

## Cross-part issues for the editor

1. **Ledger line for [agent-runtime] contradicts ruling 20.** It reads: "Forge's loop runs in Keelson Runtime outside the sandbox (consistent with sandboxes-and-execution-environments); only its tool calls execute in the microVM." Ruling 20, chapter 07 (line 245: "the inner coding loop runs *inside* a per-run mic[roVM]"), chapter 21 and chapter 41 all put the inner loop inside the microVM. The ledger line needs an `[editor]` correction; the chapters are consistent.
2. **Second-reviewer sample rate.** The ledger's Rubber Stamp entry says "a **5% random sample** audited by a second reviewer" (Q3 2027). The [human-oversight-and-bounded-autonomy] addition says 10% of executed credits ≤ €250 after the October 2027 A2 promotion. Part XI now uses 10% for post-October. Chapters in other parts that say 5% for the post-October A2 regime should be checked.
3. **Approval expiry.** The [side-effects-and-external-actions] ledger line still says "Answerdesk A1 credit approvals expire after **24 h** *(local rule)*", which contradicts ruling 25 (4 h). Part XI does not state a figure. Chapter 22 should be checked against ruling 25.
