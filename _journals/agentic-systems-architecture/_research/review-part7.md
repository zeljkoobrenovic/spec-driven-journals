# Review log — Part VII (CONTROL), 2026-10-28

Chapters reviewed in full (index.md and spec.md): 26 agent-threat-model, 27 prompt-injection-defense, 28 agent-identity-and-least-privilege, 29 human-oversight-and-bounded-autonomy, 30 policy-enforcement-and-audit. The part-7 intro was not edited (another agent is writing it).

Overall: the five chapters were already consistent with the ledger's Part VII additions (threat model v2, injection redesign, identity redesign, Rubber Stamp details, Bulkhead/Logbook design, interim audit). Rulings 4, 5, 6, 15, 19, 22 and 23 were already applied: approvals hash-bound with expiry and revalidation; intent → execute → receipt with "exactly-once effects"; Bulkhead decides, Toolyard executes; `sub` = principal and `act` = agent run (ch28 names the departure in the interview design); no `2027.10.1` manifest labels. All five are under 8,000 words, so no length cuts were needed beyond the ownership trim in ch27.

## Word counts (front matter to "Sources and Evidence", tables without pipes, no code or mermaid)

| Chapter | Before | After |
| --- | --- | --- |
| 26 agent-threat-model | 7,460 | ~7,390 |
| 27 prompt-injection-defense | 7,121 | ~7,040 |
| 28 agent-identity-and-least-privilege | 7,102 | ~7,050 |
| 29 human-oversight-and-bounded-autonomy | 6,979 | ~6,925 |
| 30 policy-enforcement-and-audit | 7,022 | ~6,960 |

(Raw `wc -w` of whole files after the edits: 9,297 / 8,841 / 8,606 / 8,727 / 8,490. The "after" figures from the counting script came out lower than the raw edits alone explain; all are under 8,000 whichever count is used.)

## Chapter 26 — agent-threat-model

Issues and fixes:
- Forge row in the trifecta register said "default-deny egress to the code host, package mirror and Gateway only; repo-scoped short-lived token". That contradicted ruling 20 and the ledger (one proxy to Keelson Gateway, git proxy, package mirror and Toolyard; only a run token in the sandbox; the git proxy holds the code-host credential). **Changed to:** "default-deny egress through one proxy to Keelson Gateway, the git proxy, the package mirror and Toolyard; only a run-scoped token in the sandbox, the code-host credential held by the git proxy."
- The threat-model YAML template used an invented endpoint name `provider-a-eu-zdr`. **Changed to** the ledger's Gateway routes `[a-large-eu-zdr, a-mid-eu-zdr]`.
- Checked and left as they are: 38 v1 threats, approval date 23 June 2027, 9 session types, 4 full trifectas, 61 exposure paths (14 → 2 uncontrolled, both signed residuals), about 1,100 Clausewise PDFs, the 9-of-400 Scout query sample, data classes D0–D4/DS, credits ≤ €250 at A2 since October 2027.

Sources spot-checked:
- https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/ → published 9 December 2025, as stated. The ASI category names are not on the page; the chapter already gives them via Promptfoo as a secondary source. Supported.
- https://privacy.claude.com/en/articles/7996866-… → dated 1 July 2026; 30-day default deletion for API inputs and outputs. Supported.
- https://developers.openai.com/api/docs/guides/your-data → no training by default, 30-day abuse-monitoring logs, ZDR needs approval and excludes stateful endpoints, storage-only vs storage-and-processing regions. Supported.
- https://arxiv.org/abs/2502.07776 → global cache sharing at seven providers, ICML 2025. Supported.
- MCP revision 2026-07-28 → exists; the authorization page links the 2026-07-28 security-best-practices tutorial. Supported.

## Chapter 27 — prompt-injection-defense

Issues and fixes:
- **Evidence error.** The chapter said Anthropic's Opus-class model scored 1.4% (November 2025) and 17.6% (August 2026) "because the test got harder, not because the model got worse". Verification showed different conditions. The 1.4% was measured *with improved safeguards* against a Best-of-N attacker (100 attempts per environment). The 17.6% was measured *before added safeguards*, on the harder red-team evaluation. **Changed** to say "before added safeguards", and that the two numbers are not a trend: the safeguard condition and the evaluation both differ, so the test, not the model, explains most of the gap.
- **Ownership.** Ch27 re-taught Meta's Rule of Two (three sentences comparing it with the trifecta), which ch26 defines. **Cut** to one sentence plus a link to [[agent-threat-model]]; the "provisional" remark is kept.
- **Ruling 1.** "re-measure in your harness" became "re-measure in your evaluation harness".
- **Year missing.** "Invariant observed that users commonly choose 'Always Allow'" became "Invariant Labs observed in April 2025 …".

Sources spot-checked:
- https://claude.com/blog/claude-in-chrome-generally-available → dated 26 August 2026. Retired saturated evaluation; 17.6% for Opus 4.5 before added safeguards; 0.3% and zero results with probes and classifier; "Prompt injection remains a moving target". Supported after the fix above.
- https://www.anthropic.com/research/prompt-injection-defenses → 24 November 2025; Opus 4.5 8.0% → 1.4% with improved safeguards; 100 attempts per environment; "1% … still represents meaningful risk". Supported. "Moving target" is in the 2026 post, not this one; the chapter's wording does not tie it to the 2025 post.
- https://www.anthropic.com/engineering/claude-code-auto-mode → 25 March 2026; 93% of prompts accepted. Supported.
- MCP security best practices (protocol version 2026-07-28) → exists. Supported.

## Chapter 28 — agent-identity-and-least-privilege

Issues and fixes:
- **Evidence error.** The standards table said the NIST AI Agent Standards Initiative had "no outputs listed as of 14 August 2026". The page, last updated 14 August 2026, lists a request for information and a National Cybersecurity Center of Excellence (NCCoE) draft concept paper on software and AI agent identity and authorization. **Changed** the row to name both, and its "what it does not settle" cell to "any final guidance yet". The Chief Architect's view now says "no final agent-specific guidance"; the Sources entry was updated to match. "Announced 17 February 2026" became "Announced February 2026": the page creation date is 17 February, but the announcement date is not stated.
- Checked and left as they are: 27 / 16 / 11 credentials, 38 tenant-mismatch denials, 14 ms mint p95, ~40,000 mints a day (labeled assumption), 6 refused self-edited approvals in the September 2027 close, 1,912 entries, Forge run token ≤ 90 min, installation token ≤ 1 h, local CLI SSO ≤ 8 h, 3 service-wide credentials in November 2027. RFC 8693 `sub`/`act` per ruling 22.

Sources spot-checked:
- https://datatracker.ietf.org/doc/draft-ietf-wimse-aims/ → draft-00, 15 September 2026, WIMSE WG. `sub` carries the represented user or system; the LLM "MUST NOT have access to an agent's credentials"; local UI confirmation alone is not sufficient authorization. Supported.
- https://datatracker.ietf.org/doc/draft-ietf-oauth-v2-1/ → draft-16, 3 September 2026, still an Internet-Draft. Supported.
- https://datatracker.ietf.org/doc/draft-ietf-oauth-transaction-tokens/ → draft-11, 30 July 2026, WG state Waiting for Write-Up. Supported.
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization → authorization optional; stdio uses environment credentials; RFC 8707 required; "MCP servers MUST NOT accept or transit any other tokens"; `insufficient_scope` step-up. Supported.
- https://www.nist.gov/artificial-intelligence/ai-agent-standards-initiative → partly contradicts the original claim; fixed as above.
- https://learn.microsoft.com/en-us/entra/agent-id/… → updated 2026-06-15; autonomous vs delegated access; sponsor; separate from service principals and users. Supported. The URL redirects to a canonical page `what-are-agent-identities`; it is left as is.
- https://neuraltrust.ai/blog/pocketos-railway-agent → token found in an unrelated file, created for domain operations, broad permissions, volume and same-volume backups deleted. Supported. The Euronews report confirms the deletion, the backups and the founder's X post as the source, but not the token details; the chapter already labels those details as founder-sourced and relayed by a security vendor.

## Chapter 29 — human-oversight-and-bounded-autonomy

Issues and fixes:
- **Ruling 21.** "with a €250 per-action limit, one credit per ticket" became "… at most one service credit per technician visit and one active credit proposal per ticket".
- **Evidence.** "Regulation (EU) 2026/1744 of 8 July 2026": the adoption date could not be verified, so it was removed. The OJ publication date (24 July 2026) and the application dates (2 December 2027 Annex III, 2 August 2028 Annex I) are confirmed by the OJ metadata and several law-firm summaries. "It did not amend Article 14's text" could be verified only against the amending provisions visible in the OJ record (Articles 2, 3, 4, 10, 11, 17, 40, 57, 60, 63, 75, 77, 95 …; the record was truncated). It **now reads** "Its amending provisions, as listed in the Official Journal record, leave Article 14's text unchanged".
- Checked and left as they are: 4,812 / 99.3% / 6 s / 38 approvers / 15 of 480; Q3 R1/R2/R3 figures; 612 audited, 7 unjustified, 1.1%, bound 2.3%; seeded-card catch rate 64% → 86%; 31 of 38 approvers; 450 cards in November 2027 at 83% and 51 s; 48-working-hour Closewise timer; 9 escalations; 3 voided approvals. The arithmetic was checked: about 42 review-hours in Q3 vs 8 in Q2, and about 1,690 cards a month.

Sources spot-checked:
- Regulation (EU) 2026/1744 (OJ metadata via publications.europa.eu, plus a web search of law-firm summaries) → published 24 July 2026, in force 27 July 2026; Annex III 2 December 2027; Annex I 2 August 2028. Supported; adoption date removed.
- https://www.anthropic.com/research/measuring-agent-autonomy → 18 February 2026; auto-approve ~20% → >40%; interrupts 5% → ~9%; 87% vs 67%. Supported.
- https://www.anthropic.com/engineering/claude-code-auto-mode → 0.4% false positives on 10,000; 17% false negatives on 52, "the honest number"; escalation after 3 consecutive or 20 total denials. Supported.
- https://doi.org/10.2495/SAFE050411 (Hofer and Schwaninger 2005, WIT Trans. Built Env. 82) → TIP data usable for individual screener assessment with large samples and adjustment for difficulty. Supported.
- https://arxiv.org/abs/2506.12469 (Feng, McDonald, Zhang) → the approver level, and "How can users be engaged … to avoid meaningless rubber stamping?". Supported.

## Chapter 30 — policy-enforcement-and-audit

Issues and fixes:
- **Hand-off.** The chapter ended with a "## Next" heading that linked to [[evaluating-agentic-systems]]. As the last chapter of Part VII it must hand off to the next part. **Replaced** with a closing paragraph (no heading) that hands off to [[part-8]].
- **Label consistency within the part.** Bulkhead policy versions were written `bulkhead/answerdesk@2027-10-08.1` in ch30 but `bulkhead/answerdesk@2027.08.3` in ch28. Ch30 is aligned to `bulkhead/answerdesk@2027.10.1` (two places).
- Checked and left as they are: interim audit week of 18 October 2027; 40 entries (30 + 10); ~2 hours vs 2.5 days; the Alias Drift window 2–5 August; 1,498 proposals at ~380/day ([editor] line applied); 165 rejected; 1,333 approved; 1,281 agreed; 52 re-examined; 4,410 credits in the decision-replay diff; p99 ≤ 5 ms labeled as an assumption; 7-year Closewise retention.

Sources spot-checked:
- https://metr.org/blog/2026-10-06-ai-systems-could-cover-up-misbehavior/ → David Rein, 6 October 2026; recording and display systems are "security-critical infrastructure". Supported.
- https://aws.amazon.com/about-aws/whats-new/2026/03/policy-amazon-bedrock-agentcore-generally-available/ → 3 March 2026. The gateway intercepts agent–tool traffic and evaluates it against policies before allowing tool access; natural-language policies are converted to Cedar. Supported.
- Regulation (EU) 2026/1744 → dates supported (see ch29).
- Claude Code auto mode → supported (see ch29).

## Cross-part issues for the editor (not fixed: outside Part VII)

1. **Answerdesk credit-approval expiry.**
   - Ch29 (and ledger `[human-oversight-and-bounded-autonomy]`): "an R1 or R2 request expires after **4 working hours** into the billing desk's queue … An approval itself is valid for **4 hours**".
   - Ch22 `posts/22-side-effects-and-external-actions/index.md` line ~302 (an example dated 2027-11-16, a €420 → €280 credit, which is R2 under ch29): "The team lead approves after 20 hours, close to the approval's 24-hour expiry *(local rule)*". The ledger `[side-effects-and-external-actions]` also says "Answerdesk A1 credit approvals expire after 24 h (local rule)".
   - Suggested fix: ch22 adopts ch29's 4-hour rule (the request would have escalated to the billing desk well before 20 hours), or the ledger states the 24-hour rule applied only before the July 2027 redesign. Either way, ch22's November 2027 example needs a new timing.
2. **Size of the injection suite.**
   - Ch27 (and ledger `[prompt-injection-defense]`): "Sounding gained an injection suite, starting with the Poisoned Ticket and **1,200** generated variants across email, attachment and chat channels".
   - Ch32 line ~364: "The **200-case** injection suite derived from the Poisoned Ticket"; ch34 line ~243: "Zero policy-violating credits from 200 injection cases"; ledger `[evidence-for-autonomy]` and `[building-agent-eval-suites]` also say 200.
   - Suggested fix: the editor states that the 200 cases are the curated credit-relevant subset that runs in the Answerdesk simulator, or aligns one side.
3. **Fixture Purge dates in the ledger (outside Part VII, for awareness).** `[partial-failure-and-compensation]` says the reviewer flagged it on Thu 22 July 2027 and the hold was lifted on Mon 2 August. `[domain-coding-agents]` says it was noticed on Fri 16 July and the trigger re-enabled on Mon 9 August. Part VII chapters do not use these dates.
