Why security is built into software, not tested onto it at the end — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a worker bolts padlocks onto a finished glass building labeled APP while Vera and Nadia watch.](assets/images/secure-software-development/comic-01-bolted-on.jpeg)
**Panel 1:** *The hook: bolted-on security — locks added to a finished building protect the walls, not the design.*

![Comic panel: the same defect fixed cheaply on a whiteboard versus expensively as a burning production incident.](assets/images/secure-software-development/comic-02-the-cost-curve.jpeg)
**Panel 2:** *The problem: the cost curve — a defect found at design costs a meeting; the same defect in production costs an incident.*

![Comic panel: Nadia finds a crack in a building foundation while a manager with a LAUNCH FRIDAY calendar holds a WAIVED stamp.](assets/images/secure-software-development/comic-03-the-security-sprint.jpeg)
**Panel 3:** *The wrong way: the pre-release security sprint — deep flaws found when the architecture is poured concrete, then waived to protect the date.*

![Comic panel: a six-station factory line from Train to Release with a green shield at every station.](assets/images/secure-software-development/comic-04-every-stage.jpeg)
**Panel 4:** *The principle: build security in — training, requirements, threat-modeled design, coding, testing, and release each carry the shield.*

![Comic panel: Nadia as a bouncer checks a queue of data parcels at four doors labeled Network, File, CLI, USB and turns one away.](assets/images/secure-software-development/comic-05-validate-every-door.jpeg)
**Panel 5:** *Practice: the one rule with no safe exception — no user-supplied input, on any channel, is processed without validation first.*

![Comic panel: Nadia weighs a guarded saw labeled memory-safe against a bare blade with a warning tag while Vera points at price tags.](assets/images/secure-software-development/comic-06-the-sharp-tool.jpeg)
**Panel 6:** *Practice: language choice is risk allocation — memory-safe where practical, the sharper tool only with its risks named and countered.*

![Comic panel: three flashlight beams labeled Static, Dynamic, Review overlap in a dark cave of code, one catching a glowing API key.](assets/images/secure-software-development/comic-07-three-flashlights.jpeg)
**Panel 7:** *Practice: the testing trio — static in the pipeline, dynamic against the running app, systematic peer review — none suffices alone, and secret detection catches the committed key.*

![Comic panel: a truck of code boxes waits at a gate labeled PRODUCTION while Vera holds a checklist with green check marks.](assets/images/secure-software-development/comic-08-the-final-gate.jpeg)
**Panel 8:** *The gate: standards followed, input validated, testing complete, fixes retested — known vulnerabilities remediated or formally addressed, before production.*

![Comic panel: a calm night-shift operator holds a runbook during an alert storm as Nadia hands over and waves goodbye.](assets/images/secure-software-development/comic-09-shipped-is-not-done.jpeg)
**Panel 9:** *The closer: shipped is not done — a release is finished when someone else can operate it under attack, runbook, incident response, and handoff included.*
