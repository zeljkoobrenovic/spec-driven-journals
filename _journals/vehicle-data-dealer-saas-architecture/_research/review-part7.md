# Editorial review — Part VII (OPERATIONS)

Reviewer pass, 2026-10-22. Prose word counts measured with `awk '/^## Sources and Evidence/{exit} {print}' index.md | sed 's/|/ /g' | wc -w`. No page was over 8,500, so nothing was trimmed. Build passed after one rerun (the first run hit a transient OSError from a parallel build in another journal). Render check: all six pages print `OK`, with 0 mermaid failures and 0 unresolved links.

| Page | Words before | Words after |
| --- | --- | --- |
| part-7-intro | 1,113 | 1,116 |
| 35-reliability-and-dependencies | 7,598 | 7,614 |
| 36-scale-and-cost | 6,873 | 6,875 |
| 37-observability-and-data-operations | 7,635 | 7,775 |
| 38-vehicle-platform-security | 7,731 | 7,739 |
| 39-privacy-and-retention | 6,953 | 7,003 |

## part-7-intro
- WHY THE BUSINESS CARES now gives the Saturday Batch's full cost (€105,490, of which €96,140 was build data). Before, it read as if the batch had broken even.
- Format, callouts, the Chapters list and the hand-off to `reliability-and-dependencies` all pass.
- Open: at 1,116 words, the intro is above the style guide's 500–800 range for part intros. It was not trimmed because the brief sets the trim threshold at 8,500.

## 35-reliability-and-dependencies
- **Consistency item 10:** I fetched the AutoNation Form 8-K of 15 July 2024. It says earnings "will be negatively impacted by approximately $1.50 per share", "without taking into account any potential recoveries". The text and the source entry now quote this and give the filing date.
- **Month-End Register Outage times** agree with the ledger line of `registration-and-trade-services` (23): unavailable 14:20–20:00; the doubles fell in the first 45 minutes (14:20–15:05) and the first 20 minutes after recovery (20:00–20:20). They also agree with the reliability ledger line (stopped answering about 15:05, banner about 15:20) and with the text of chapter 23. No change needed.
- Other figures checked against the ledger, all consistent: the dependency map (75 entries), the appraisal budget (0.83%), the DriveDesk figures (16,000 / 19,000 / 34,000 / 3,900 / 2,140) and the rooftop and client counts.
- I also verified the AutoScout24 SLO post (3 September 2024, Terraform and Datadog, the CUI example).

## 36-scale-and-cost
- I recomputed the arithmetic: the Saturday Batch table, the call-path table (€0.0240 direct, 45% share of the cost), the €29M a year, and the per-rooftop volumes. All are consistent with the ledger and the price table.
- The Odolo price is now marked "VAT included", following the editor ledger line.
- timetoread changed from 32 to 30.
- I verified the AutoScout24 Karpenter post (9 September 2024: EC2 cost down almost 50%, observability cost up).

## 37-observability-and-data-operations
- **Consistency item 17:** the Odometer Correction section had presented the median batch gate as the fix and claimed the median would fall to 62%. It now says:
  - The median gate is the insufficient first version: the September 2027 replay showed it would not have fired, because 2,870 wrong readings among about 34,000 UK-import records moved no median by more than 5%.
  - The per-workshop-chain check is the fix: 94% of the chain's 3,050 records failed. The section links to `ingestion-and-entity-resolution`.
  - The gate table has a new per-chain row, which quarantines that chain's segment and releases the rest.
  - One added sentence: "A distribution check is only as sharp as its segments."
- The 2027 Lotwise Classic path now says "a RabbitMQ message" instead of "an outbox record, a Kafka message". This matches the ledger: RabbitMQ in Lotwise Classic, with the outbox and Debezium arriving in 2028.
- timetoread changed from 32 to 34.
- I verified the OpenTelemetry CNCF graduation date (11 May 2026).

## 38-vehicle-platform-security
- The NIS2 early warning now names its criterion in words. Before, it said "criterion (c)" without saying what that was.
- "leverage" (a style-guide buzzword) is replaced.
- timetoread changed from 32 to 34.
- Ledger figures are all consistent: dates, 17 keys, 09:40 and 11:05, 860,000 answers, 41,000 fetches, €19,000, 212 corrected values, ISO since 2019, 31 h against 12 h, the Connect XML sunset, Velto's 61% shared logins.
- I verified the Cbw entry into force (15 August 2026, NCSC page) and the Sam Curry Kia write-up. Note that the post is dated 20 September 2024 but its own timeline gives public disclosure as 26 September 2024; the chapter uses the dateline.

## 39-privacy-and-retention
- **Consistency item 22:** the trade-in scores are now named **Horizon** throughout: the scene table, the controller table, the DPIA list, the suppression list, the replay table and the failure table.
- The scene row now says the 14 scores went back to 2024 and were kept without expiry, as all scores were before the 2027 redesign.
- The retention schedule has a new row: Horizon scores, 90 days, void on a new registration. The existing deliveries row is relabeled "Horizon deliveries".
- American spelling fixed: defense, behavior, anonymized.
- timetoread changed from 32 to 31.
- I verified the FTC GM/OnStar order (14 January 2026, express consent, five-year ban on disclosure to consumer reporting agencies) and the EU's UK adequacy renewal (19 December 2025).

## Ledger
- I appended one `[editor-review]` line recording the item 17 resolution (median gate first, per-chain check as the fix) and the Horizon naming in `privacy-and-retention`.

## Open issues for the author or other parts
1. **Horizon timing:** the ledger dates the Horizon DPIA and match-in redesign to March 2027, but the August 2027 erasure request still found 14 scores kept indefinitely. Chapter 39 now words this neutrally ("before the 2027 redesign"). The owner of `data-products-and-insights` should state when the 90-day expiry actually took effect, for example "rolled out in Q3 2027".
2. **Toolkit:** the toolkit (`toolkit/index.md`, around line 228) still lists the median gate first, though it does mention the per-chain check. Its reviewer may want to label the median gate "first, insufficient" as well.
3. **Part VII intro length:** 1,116 words, above the 500–800 guideline.
