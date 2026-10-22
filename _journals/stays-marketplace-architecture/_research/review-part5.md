# Review log — Part V (BOOKING)

Editorial pass, 21 October 2026. Scope: part-5-intro, 21–25. Word counts are measured with `awk '/^## Sources and Evidence/{exit} {print}' index.md | wc -w`.

| Page | Before | After | timetoread |
| --- | --- | --- | --- |
| part-5-intro | 1,094 | ~1,100 | 5 (unchanged) |
| 21 checkout-orchestration | 9,679 | 8,492 | 38 → 37 |
| 22 reservation-lifecycle | 10,191 | 8,499 | 38 → 37 |
| 23 changes-and-cancellations | 9,902 | 8,488 | 40 → 37 |
| 24 trip-and-messaging | 9,046 | 8,482 | 36 → 37 |
| 25 customer-service | 8,457 | 8,467 | 34 → 37 (it was too low) |

Build: no errors. Render check: all six pages print `OK` (mermaid 1/3/3/3/4/3, failed 0, no unresolved links, no XJ entries). The first runs of part-5 and changes-and-cancellations timed out while loading from the CDN and passed on rerun.

## part-5-intro
- Added "the fictional travel group this book follows" (the intro never said Corvane was fictional).
- Checked the callouts, figure, chapter list and hand-off to `checkout-orchestration`. No other changes.

## 21 checkout-orchestration
- Trimmed: the five-point redesign list (it repeated the idempotency section) is now one paragraph; the Performance and Conversion section is condensed; the eligibility bullets became one sentence; the Stripe, IETF, Orpheus, Expedia and SCA passages are shorter; the "client gives up first" failure mode is gone (the timeout-budget paragraph covers it); the "Hold timing" trade-off row and the "Supplier delivery" hotels-vs-homes row are gone; the "watch four numbers" paragraph is gone (it repeated the dashboard metrics); the questions went from 10 to 8.
- **States aligned with 22:** the compensation for the step-5 pending reservation is now "close it as expired", to match reservation-lifecycle's `Pending → Declined or expired` transition (it was "mark it abandoned"). "Abandoned" stays only as a checkout-attempt state in Figure 3.
- Checkout-attempt contract timings (30 s Unknown, 35 s client wait, 5 min polling, reconciliation queue) now match the ledger line exactly.
- PSD2 is now expanded; the Package Travel amendment carries its date (29 April 2026, checked on the Commission page).
- The Lisbon under-13 exemption is hedged with a pointer to taxes-on-stays' verification caveat (consistency issue 4).
- Spot-checked: Expedia Rapid error-response page (90-second timeout, 13–30 seconds, 30-minute retrieval, `affiliate_reference_id` duplicate text) and Commission PTD page (2026/1024, 28 months). Both confirmed.

## 22 reservation-lifecycle
- Trimmed: the terms table lost its "Confirmation numbers" and "Stayed" rows and shorter definitions; the five state-machine choices are condensed; the event-sourcing paragraph is folded into the design-rules paragraph (Trade-offs still compares it); the delivery rules and the hosted-stays paragraph are shorter; the Booking.com reporting detail is shorter (ch. 23 had repeated it); the 10-K paragraph is shorter; the four-row "public record" evidence table is now one paragraph; the replay epilogue, the Dubrovnik paragraph and the Chief Architect's view are condensed; the "Guest confirmation" trade-off row and two failure-mode rows are merged or removed; the questions went from 10 to 8.
- **Contradiction fixed with event-driven-stays (owner of the event backbone):** 22 listed a family of event types (`ReservationConfirmed`, `StayStarted`, `ArrivalDue`, …), which 37 explicitly rejects in favor of one `reservation.versioned` event with change types. The table now lists the change types `created`, `modified`, `cancelled`, `no-show`, `stayed` and `completed`, plus separate delivery events. Arrival day is computed from the dates.
- Pending now says that an abandoned checkout attempt closes as expired, which matches 21.
- DAC7 and GDPR are now expanded; "programme" is now "program".
- Spot-checked: Booking.com B.XML no-show window (00:00 on check-in date to 48 h after check-out) and invalid-card window. Both confirmed.

## 23 changes-and-cancellations
- **ATC strike figures** agree with the ledger, 24 and 25: 17,000 Roomstead and 2,600 Nookaway affected; 6,200 requests = 2,950 self-service + 3,250 contacts (750 + 2,500); macro on 1,860 (1,140 agency, 610 charged, €167,900; 720 merchant, 290 VCCs, €31,200); Nookaway 1,480 = 1,050 flag + 430; 310 complaints; the replay matches the ledger. The dates are correct as well (announced Thursday 3 June; Saturday 5 to Monday 7 June 2027). €167,900 + €31,200 = €199,100 ("almost €200,000"). The arithmetic of both worked examples checks out.
- Trimmed: the Airbnb tier list, the PTD quotation, the engine rules, the modification evidence (the SiteMinder bullet now links to reservation-lifecycle), the two product rules, the self-service bullets (an unsupported Airbnb forum anecdote is gone), the host and property cancellations, the no-show paragraph (now a pointer to 22), the pandemic and voucher evidence, the batch rules, the Clause decisions, the failure modes and the Chief Architect's view. The "Host penalties" trade-off row is gone, and the questions went from 10 to 9.
- Removed four sources that the body no longer cites (the Airbnb Community thread, the SiteMinder reference, the Booking.com Reservations overview and the B.XML Reporting API).
- "help-centre" is now "help-center" and "programme" is now "program".
- Spot-checked: Airbnb article 475 (Flexible 24 h, Moderate 5 d, Limited 14 d from 1 Oct 2025, Firm 30 d, 24-hour grace if booked ≥7 days ahead). Confirmed.

## 24 trip-and-messaging
- Trimmed: the concepts list, the AgentHub and Romie paragraph, the smart-lock passage, the Airbnb messaging statistics, translation, retention, the pipeline steps, the WhatsApp paragraph, the phishing-wave follow-up, the end-of-trip bullets, and the "What can be shared" row (the judgement paragraph that follows covers it).
- Fixed "The completion event drives money": the payout is triggered 48 h after check-in, not at completion. It now reads "the same stay events drive money".
- PMS is now expanded at first use in the body (it was used in a callout before its definition). "travelling" is now "traveling", "programme" is now "program", and "robust" is replaced.
- The ATC figures (17,000 reservations, 6,200 requests, median 3 h 10 min) and the 7 August incident figures match the ledger.

## 25 customer-service
- **ATC deadline rendering aligned with 23** (the owning chapter): it was "the disruption e-mail showed deadlines in Irish time"; it now reads "the confirmation e-mail showed deadlines in Irish time and the app in property time". The ledger line says only "the e-mail".
- "€1,600, four times the €400 cap" could be read as four times above the cap. It now reads "the €400 cap per relocated reservation … for each of the four guests".
- timetoread raised from 34 to 37. No trimming was needed (8,467).
- Spot-checked: the Airbnb Q2 2026 letter (50+ languages, nearly 45% resolved without a human, cost per booking down about 16%) and the Hotel Dive report of Expedia's Q1 2026 call (250M interactions, over half self-service, more than 30% AI). Both confirmed.

## Open issues for the author or other parts
- **Ledger wording:** the [changes-and-cancellations] ledger line says "the e-mail rendering deadlines in Irish time". Chapters 23 and 25 now both say it was the *confirmation* e-mail. An `[editor-review]` line was not added; add one if other chapters cite this detail.
- **04-stays-bounded-contexts** uses `ReservationConfirmed` as a generic example of a domain event. That is harmless, but Corvane's contract uses a single `reservation.versioned` event (ch. 37), so the owner may want to align the example.
- **Lisbon under-13 exemption** is still unverified (consistency issue 4). 21 now hedges it; 22 and 24 do not rely on the age.
- The Miradouro walked family "from Lyon" (22) and the Seville family "from Lyon" (23) are two different illustrative families with the same origin. That is harmless, but the author may want to vary one.
- The part-5 intro is about 1,100 words including callouts, above the 500–800 guideline for part intros. Its prose is close to the limit and was left as it is.
