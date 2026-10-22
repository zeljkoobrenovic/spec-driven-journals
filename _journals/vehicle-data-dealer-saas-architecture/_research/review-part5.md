# Editorial review — Part V (SAAS)

Reviewer pass, 22 Oct 2026. Prose words were measured with `awk '/^## Sources and Evidence/{exit} {print}' index.md | sed 's/|/ /g' | wc -w`. No page was over 8,500, so nothing was trimmed. Build is clean and the render check printed OK for all six pages.

| Page | Words before | Words after |
| --- | --- | --- |
| part-5-intro | 1,025 | 1,025 |
| 26 tenancy-and-dealer-groups | 8,141 | 8,183 |
| 27 identity-access-and-entitlements | 7,575 | 7,664 |
| 28 onboarding-and-configuration | 7,893 | 7,936 |
| 29 billing-and-metering | 8,190 | 8,270 |
| 30 data-licensing-and-governance | 7,496 | 7,550 |

## Spot-checks (WebFetch, all confirmed)

- The DVSA MOT history API docs: 60-minute tokens, keys revoked after 90 days without use, client secrets expire every 2 years (ch27).
- Pinewood bought Lithia's 51% stake on 9 June 2025. Lithia committed for five years, with a pilot in H2 2025 and rollout from 2026 to the end of 2028 (ch28).
- Stripe completed its Metronome acquisition on 14 January 2026 (ch29).
- The FTC finalized the GM/OnStar order on 14 January 2026. It requires affirmative express consent before connected-vehicle data is shared (ch30).

## Changes per page

**part-5-intro.** No edits. It is 1,025 words against the 500–800 target for a part intro. I left it because it is under the trim threshold.

**26 tenancy-and-dealer-groups**
- The two Lost Leads of Velto passages now follow the `[editor]` line: hub-sized stock (about 1,100 cars plus central stock) was still advertised under three old rooftop codes.
- Consistency item 32: the Figure 2 caption now says that Velto Noord B.V. and Velto Vlaanderen NV are two of Velto's seven legal entities.
- Velto's stock changed from 2,600 to 2,650, to match the used-car-pricing ledger line.
- "authorisation" changed to "authorization".

**27 identity-access-and-entitlements**
- The Velto Appraise entitlement row said Appraise was bought for Breda only (and the prose said "not for all 46"). Both now say all 46 rooftops with a pooled allowance of 46 × 25 = 1,150, matching the billing-and-metering ledger line, which owns the topic.
- Item 31(d): in both the gates table and the components table, the authority register is now marked as owned by Axleby Trade's register-transactions context and read by the access path as a gate.
- Item 23: "authorized information provider" is introduced as a book term, linked to registers-and-official-data.
- The Lost Leads wording is aligned with the editor line.
- "enrolment" changed to "enrollment".

**28 onboarding-and-configuration**
- "tenant registry" changed to "tenant directory" throughout, the ledger term.
- The register recognition is now held per legal entity, covering its rooftops, in the stages table and the markets table. This matches ch27.
- The declined stand-time request had read as if it became a custom field. It is now declined, and Velto's warehouse feeds the result back through the partner API. This keeps the 17/4/2 split.
- The Lost Leads wording is aligned, and CRM is expanded.
- OEM, MOT and V5C are expanded or glossed.
- Spelling: enrollment, toward, programs.

**29 billing-and-metering**
- Brandsma's October 2027 bill used to show Sales Admin activated on 17 October 2027 and prorated. Brandsma has taken Sales Admin since January 2027 (consistency item 26, journey-sale-to-registration), so it is now a full month at €59. The total changed from €692.35 to €722.80. The proration example still appears in the prose.
- Following the revenue-per-rooftop `[editor]` line, report usage is now counted by the Connect XML invoice run and carried onto the Lotwise invoice. Register transactions are invoiced through Axleby Trade.
- Lookup mix `[editor]` line added: about 70% of the 2.6M daily lookups are internal, and external clients make about 780,000 a day at about €0.13.
- Velto's hub reorganization no longer "moved rooftops between legal entities". Cost centers and reporting follow the hubs, and invoices stay with the legal entities. This is consistent with ch26.
- "authorised" changed to "authorized". "Autotrader Group plc" changed to "Auto Trader Group plc".
- AVK, VIN, DMS, IFRS and ACH are expanded.

**30 data-licensing-and-governance**
- Report-snapshot retention changed from 7 years to 5 years, per the privacy-and-retention retention schedule, which owns that topic.
- The Acquisition Archipelago bullet listed Axleby Data, Wertlauf, Odolo and Lotwise. It now names the four places the vehicle-data-ecosystem map found: Axleby Data procurement, Wertlauf, Lotwise and a shared drive.
- DMS, NMVTIS, KADOE, KBA/StVG, DIV, MOT, VIN and ICO are expanded on first use.

## Open issues for the author or other parts

1. **Number of billing systems.** part-5 and ch29 say Axleby bills from three systems: the Connect XML invoice run, Lotwise Classic and Showroomly's tool. That matches the ledger's systems table. The customer census in `one-platform-from-many-products` counts four billing systems, adding Axleby Trade, and Velto receives separate Axleby Trade invoices. I did not change Part V. An editor should decide whether Axleby Trade invoices are produced by a separate system or by the Connect XML run.
2. **The intro is 1,025 words** against the 500–800 target. It is optional to trim.
3. **Ch28's 12-rooftop Gelderland group** (onboarded with Runway in April 2027, last first advert at 41 days) is a local detail and is not in the ledger. It does not contradict anything.
4. **Ch30's Data Act Art. 4(5) quote and recital 15** were not re-fetched in this pass. They come from the law brief.
5. **"cancelled"** is British spelling. It is used book-wide, in ch27 and in Part IV pages. I left it for a global decision.
