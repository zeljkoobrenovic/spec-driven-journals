# Final editorial pass — 2026-10-22

Surgical fixes only; each edited page's spec.md has a "Final editorial pass" Changelog line.

## Open items fixed

1. **Item 34, billing systems** — `one-platform-from-many-products`: key-point bullet, census paragraph and census table now count **three** business billing systems (Connect XML monthly invoice run for Axleby Data and Axleby Trade, Lotwise Classic subscription billing, Showroomly's SaaS billing tool). The webshop and Odolo's consumer accounts are named as out of scope. `part-5-intro` already said three.
2. **Item 37, Horizon expiry** — `data-products-and-insights` ("Scores die" bullet) and `privacy-and-retention` (system table row and retention schedule row): the redesign was approved March 2027, the 90-day expiry was enforced from **September 2027**, and the old scores were purged then.
3. **Item 38, toolkit batch gate** — `toolkit` data-contract example: the per-workshop-chain check is the fix; the median gate is called insufficient (the September 2027 replay would not have fired on the May batch).
4. **March 2027 board** — `market-data` and `valuation-engine` now say the *company board* (One Dossier approval, March 2027). The architecture forum first met on 22 April 2027.
5. **Offer validity** — `journey-inventory-to-portal`: offer v2 is "valid for seven days or to 61,740 km (500 km beyond the appraisal reading)", in line with `vehicle-acquisition`.
6. **Odometer unit** — `provenance-and-data-quality`: the envelope example showed version 2 (66,337 km) with `value_as_delivered` `41220`, unit `km`. That was version 1's erroneous unit. It now reads unit `mi`, with a note that version 1 carried `km`. The same error in the `toolkit` example is fixed too. The k1/k2 table was already consistent (41,220 mi = 66,337 km).
7. **AI Act timetable** — `ai-in-dealer-workflows` no longer says `valuation-engine` is out of date (it says the amended dates apply there). No edit needed.
8. **meet-axleby revenue** — the brand table (€71M split 38/17/16, €96M with the ~€1,110 per rooftop breakdown, €12M, €27M, €8M = €214M; shares 45/33/13/6/4) and the VAT note on Odolo prices agree with the ledger and its editor lines. No edit needed.
9. **Spelling** — there was no "Licence Blindness" left in any index.md or spec.md. `bib-tools/render.py` still generated it (and "licences" and "help centres"), so the script is fixed to stop the next run reintroducing them. Fixed in the book's own prose: towards → toward (`journey-sale-to-registration`, `inventory-and-vehicle-dossier`); enrolment → enrollment (`connected-vehicle-data`, `case-cox-automotive`); tyres → tires (`journey-inventory-to-portal`); licence → license (`provenance-and-data-quality` key sentence); labelling → labeling (`merchandising`, `listing-syndication`); kilometres → kilometers and License in the A–Z index (`glossary`); neighbouring/neighbours/defence in 8 spec.md files. Left as is: quotations, link titles, source entries, proper names (Polish Labour Code, Worldwide Harmonised…), and code identifiers (`licence_ref`, `module-licence-*`).
10. **Hard-coded links** — no `](<permalink>.html)` links to this book's pages remain apart from the callout link to `where-vehicle-platforms-go-wrong.html`.

## Checks

- Bibliography rerun: **610** entries (R1–R610), with no "Licence Blindness".
- Build: no errors; `[built] vehicle-data-dealer-saas-architecture`.
- Render check (all pages): **70/70 OK**, **168** mermaid diagrams, 0 failed, 0 unresolved links.

## Remaining for the author

- **"judgement"** (about 360 uses, including the RDW term "odometer judgement") is still spelled the British way. The style guide itself requires the closing sentence "…are the author's judgement", so it was not changed. To switch to "judgment" book-wide, change the style guide first.
- **Item 33**: `vehicle.fact.disputed` is still missing from the domain-event catalog in `events-webhooks-and-sync`. It was not in this pass's scope.
- The glossary A–Z index was edited directly. If `glossary-tools/assemble.py` is rerun, check that its sources (`h2.txt`, `tables.txt`) carry the American spellings.
