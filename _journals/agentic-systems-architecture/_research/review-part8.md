# Review — Part VIII (EVIDENCE), 2026-10-28

Chapters: part-8-intro, 31-evaluating-agentic-systems, 32-building-agent-eval-suites, 33-agent-observability, 34-evidence-for-autonomy. Build OK (agentic built; transient rmtree tracebacks from parallel builds of other journals). `render_check.py` on all five permalinks: 0 problems, 0 mermaid failures, no unresolved links.

## Eval-suite reconciliation (31 / 32 / 34)

| Figure | Before | After (canonical for Part VIII) |
| --- | --- | --- |
| Closewise accrual suite at the Alias Drift | 31: "assume 1,200 entries from the 2026 closes" | 860 cases (v1, April 2027), as in 32 and the ledger; v2 1,244 cases from October 2027 |
| Closewise noise arithmetic (31) | SE 0.56 on 1,200; alert "drop > 2 points across 3 trials" *(assumption)*; drop "about four times the noise band" | SE ≈ 0.66 on 860, drop ≈ 10 SE; canary alert below 93.5% (from 32) |
| Daily canary | 31: k = 3 (ledger [evaluating]); 32: 300-case subset, **1 trial**, alert < 93.5% (ledger [building]); 38: "several trials per case" | 300-case stratified subset, **3 trials per case**, 05:00, alert below 93.5% (earlier-owned chapter 31's k = 3 kept; 32's math restated with clustered SE "at most about 1.1 points", "at most about five false pages a year") |
| Workflow-level k | 31: k = 8; 32/34: Answerdesk credit-policy suite 4 trials, pass^4 | k fixed per suite before the run: 8 by default, 4 for Answerdesk's credit-policy suite |
| Answerdesk pass^k example in 31 | Dated "October 2027" comparison on a credit-and-revisit family: 240 tasks × 8, pass^1 92%, pass^8 81% vs 64% — conflicted with 34's pass^4 0.962 on the 420-case suite that month | Recast as an undated illustration on a revisit-scheduling family (no ledger claim); points to 34 for the real credit-suite case |
| Injection cases in the credit review | 32: "200-case injection suite"; 34 C5: "200 injection cases"; ch27/ledger: Poisoned Ticket + 1,200 variants | Injection suite = Poisoned Ticket + 1,200 variants; Answerdesk's gate runs a fixed **200-case stratified sample** of it (0 of 200) — consistency ruling 26 |
| Closewise close-week volume (31) | "about 380 a day *(assumption)*" | stated as ledger fact (`[editor]` line) |

Unchanged and consistent: Answerdesk suite 420 cases (230/120/70), 4 trials, ~1,700 conversations; pass^4 0.962; null baseline 0.31; audit 7/612, bound 2.3%; €1,680 / €3,520; v2 gate (1,094 × 3 = 3,282 trials, ≥ 94.5% bound, ≤ 1.0 pt paired drop); first v2 score 95.2% → 96.0%.

## Per chapter

**part-8-intro** — No changes. Numbers match ledger. 927 words.

**31** — Changes above, plus SWE-bench Verified paragraph: "recommended others do the same" → "recommended SWE-bench Pro instead" (per The Decoder); the claim that the audit pool was problems models did not consistently solve is now labeled "reportedly … not verified against the primary text" (OpenAI page returns 403). Words 7,035 → 6,995.

**32** — Canary trials and math; injection-suite wording (ruling 26: 200-case stratified gate sample of 1,200 variants); τ²-bench "about 18 to 25 points for the models tested" → "18 and 25 points for the two models the authors report". Words 7,531 → 7,475.

**33** — Lead: rejection rate "began to rise … by Thursday 11%" → "from that day it ran at about 11%" (ledger: ~11% from day 1). Rework: "roughly 90 extra rejected entries" → "165 rejected of 1,498, about 105 above the 4% baseline" (ch30 and ch38; coordinator request). Words 7,662 → 7,595.

**34** — Ruling 21: "the €250 limit and one credit per ticket" → "at most one credit per technician visit and one pending credit proposal per ticket". C5 names the 200-case stratified gate sample of the 1,200-variant suite (ruling 26). Heading "Pre-registration in July" → "in June" (date is 28 June). "author's judgement. built" typo fixed; "The evaluation brief found" → "The research for this book found"; "The October outcome is canonical:" → "The October outcome:". Checked ruling 25: no A1 expiry or prefixless manifest labels in Part VIII (`ad-2027.10.2` already correct). Words 7,151 → 7,091.

Specs 31–34: Changelog review lines added (revised already 2026-10-28); success criteria and non-goals still match.

Rulings check: turn/exchange, harness, approval model, unknown outcome, exactly-once effect, authorization vs execution — no deviations found in Part VIII.

## Sources spot-checked (WebFetch / gh)

| URL | Verdict |
| --- | --- |
| metr.org/blog/2026-06-26-gpt-5-6-sol/ | **Verified.** OpenAI's GPT-5.6 Sol; 11.3 h (95% CI 5–40 h) cheating-as-failure, > 270 h cheating-as-success; packaging exploits for hidden tests, hidden source code extracted; "we do not consider any of these numbers to represent a robust measurement". Kept in 31, 32, 34 (chapters name it "an OpenAI model"/"a frontier model" in prose; the model name appears only in the source title). |
| metr.org/blog/2026-10-06-ai-systems-could-cover-up-misbehavior/ | Verified (D. Rein, 6 Oct 2026; ~10 min, patched in a day, not seen exploited; "security-critical infrastructure"). |
| metr.org/time-horizons/ | Verified (updated 2026-09-08; > 16 h unreliable). |
| developers.openai.com evaluation-best-practices | Verified (read-only 31 Oct 2026, shutdown 30 Nov 2026; nondeterminism; vibe-based anti-pattern). Note: page says "data precision", chapters say "argument precision" — acceptable paraphrase. |
| the-decoder.com SWE-bench Verified | Partly: 59.4%, memorization, Feb 2026 verified; "recommended others do the same" not supported → fixed; audit-pool detail not in source → labeled unverified. openai.com primary: 403. |
| anthropic.com eval-awareness-browsecomp | Verified (6 Mar 2026; 1,266; 11; 2; 0.24%/0.87%; blocklists insufficient). |
| anthropic.com infrastructure-noise | Verified (5 Feb 2026; 6 pts; < 3 pts; 1–2 pt binomial CIs). |
| arxiv 2305.17926 (Wang) | Verified (66 of 80). |
| arxiv 2506.07982 (τ²-bench) | Verified with correction (18% gpt-4.1, 25% o4-mini). |
| arxiv 2601.11868 (Terminal-Bench) | Verified (Merrill, Jan 2026; environment, human-written solution, tests). |
| arxiv 2411.00640 (Miller) | Verified (clustered SEs, paired SEs, power analysis). |
| GitHub open-telemetry/semantic-conventions-genai | Verified (created 2026-05-05; 0 releases, 0 tags). |
| arxiv 2505.00212 (Who&When) | Verified (127 systems; 53.5% / 14.2%). |
| anthropic.com postmortem-of-three-recent-issues | Verified (17 Sep 2025; evals missed it; privacy controls; continuous production evals). |
| code.claude.com monitoring-usage | Verified (OTEL_LOG_USER_PROMPTS, OTEL_LOG_TOOL_DETAILS defaults off). |
| anthropic.com responsible-scaling-policy | Verified (v3.4 effective 8 Jul 2026). |
| anthropic.com research/measuring-agent-autonomy | Verified (18 Feb 2026; 20%/40%; 9%/5%; 87%/67%; caveats). |
| anthropic.com engineering/claude-code-auto-mode | Verified (25 Mar 2026; 93%). |
| arxiv 2503.14499 (Kwa) | Verified ("80% time horizons are 4-6x shorter"; NeurIPS 2025). |

## For the editor (cross-part / ledger)

1. **Ledger line `[building-agent-eval-suites]`** says the daily canary is "1 trial"; Part VIII now uses 3 trials per case (matching `[evaluating-agentic-systems]` k = 3 and ch38 line 247 "several trials per case"). Please add an `[editor]` line.
2. **Ledger line `[evaluating-agentic-systems]`** says workflow level "k = 8 trials"; Part VIII now says k is fixed per suite (8 default; 4 for Answerdesk's credit-policy suite, per `[building-agent-eval-suites]` and `[evidence-for-autonomy]`). ch41 line 266 uses "Workflow suite, k = 8 trials" for Forge — consistent with the default.
3. **Injection suite size:** ch27 and ledger `[prompt-injection-defense]`: Poisoned Ticket + 1,200 variants; ledger `[building-agent-eval-suites]` / `[evidence-for-autonomy]`: "200-case injection suite", "0 of 200". Resolved by ruling 26: Part VIII now calls the 200 the fixed stratified gate sample of the 1,200-variant suite. Other parts that quote "200-case injection suite" should match.
4. The Answerdesk 31 illustration (240 tasks, pass^8 81% vs 64%) is no longer an Ostrell fact; no other chapter should cite it.
