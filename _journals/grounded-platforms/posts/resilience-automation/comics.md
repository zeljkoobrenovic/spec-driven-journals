Why resilience is proven, never assumed — the closed loop, in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: Kai points at an all-green dashboard while Vera asks what proved the resilience claim.](assets/images/resilience-automation/comic-01-what-proved-it.jpeg)
**Panel 1:** *The hook: 'resilient' is a claim — the first question is always what proved it.*

![Comic panel: a dusty vault labeled BACKUPS holds a glowing question mark while a calendar shows years of green check marks.](assets/images/resilience-automation/comic-02-the-schroedinger-backup.jpeg)
**Panel 2:** *The problem: the Schrödinger backup — jobs green for years, restore never attempted, simultaneously working and broken.*

![Comic panel: Kai bows on a Game Day stage with a trophy while a bin of ignored findings overflows behind the stage.](assets/images/resilience-automation/comic-03-chaos-theater.jpeg)
**Panel 3:** *The wrong way: chaos theater — failure injected for the story, findings binned, nothing remediated, nothing retested.*

![Comic panel: Vera draws a five-station circular loop on a whiteboard — objectives, inject failure, measure, remediate, retest.](assets/images/resilience-automation/comic-04-the-closed-loop.jpeg)
**Panel 4:** *The principle: one closed loop — objectives, controlled failure, measurement, remediation, retest — and it closes on every practice.*

![Comic panel: Kai pulls a deploy-freeze lever as an error-budget gauge sits in the red and a developer holds a paused release.](assets/images/resilience-automation/comic-05-budget-with-consequences.jpeg)
**Panel 5:** *How it plays out: budgets with consequences — the exhaustion policy is written before anyone is angry, and the freeze is the SLO doing its job.*

![Comic panel: a restore test inside an isolated glass cluster passes health, logs, and data checks while Vera stamps the result.](assets/images/resilience-automation/comic-06-restore-is-the-product.jpeg)
**Panel 6:** *How it plays out: restore is the product — regular restore tests in an isolated cluster, validated for health, logs, and data integrity.*

![Comic panel: Kai runs a scoped chaos experiment from a console with an abort button in daylight while Vera times it against steady monitors.](assets/images/resilience-automation/comic-07-controlled-science.jpeg)
**Panel 7:** *How it plays out: controlled science, not vandalism — expected steady state, scope, abort conditions, and a communicated business-hours schedule.*

![Comic panel: a DR drill stopwatch overshoots the RTO line while Vera calmly notes the gap and Kai winces.](assets/images/resilience-automation/comic-08-drill-against-the-numbers.jpeg)
**Panel 8:** *What it costs: drills against the numbers — a missed RTO in a rehearsal is a win, because the gap surfaced on a Tuesday, not during the incident.*

![Comic panel: pedestals labeled hypothesis and hope flank Kai holding a card of four dates and four results.](assets/images/resilience-automation/comic-09-hypothesis-and-hope.jpeg)
**Panel 9:** *The closer: a backup never restored is a hypothesis; a failover never run is a hope — 'resilient' means four dates and four results.*
