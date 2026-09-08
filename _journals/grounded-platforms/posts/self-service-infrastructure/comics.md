Why infrastructure self-service means a small claim on top of a platform-owned blueprint — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a developer stands between a long ticket queue and Kai offering a single small card labeled CLAIM.](assets/images/self-service-infrastructure/comic-01-the-database-request.jpeg)
**Panel 1:** *The hook: 'I just need a database' — and the answer is either a queue or a claim.*

![Comic panel: a developer waits by a crossed-out calendar while an engineer hand-cranks a manual provisioning machine behind a curtain.](assets/images/self-service-infrastructure/comic-02-the-waiting-queue.jpeg)
**Panel 2:** *The problem: the ticket behind the curtain — the interface changed, the queue did not, and the platform team is still the bottleneck.*

![Comic panel: Kai unrolls a huge YAML scroll covered in knobs and dials that buries a small developer while Vera watches.](assets/images/self-service-infrastructure/comic-03-thousand-knob-yaml.jpeg)
**Panel 3:** *The wrong way: the thousand-knob blueprint — every provider parameter exposed 'for flexibility' is the cloud console relocated, not complexity managed.*

![Comic panel: an iceberg with a small five-field claim card above the waterline and a huge blueprint block of platform standards below it.](assets/images/self-service-infrastructure/comic-04-the-blueprint-iceberg.jpeg)
**Panel 4:** *The principle: the blueprint is the product — the developer declares intent in a handful of parameters, and the composition compiles the organization's standards into everything beneath.*

![Comic panel: near-identical claim cards, differing only in tier, pass through doors labeled dev, staging, and prod, with the prod door automatically adding armor and a padlock.](assets/images/self-service-infrastructure/comic-05-defaults-are-policy.jpeg)
**Panel 5:** *How it plays out: policy that lives in defaults cannot be forgotten under deadline pressure — production gets Multi-AZ and deletion protection because the composition says so.*

![Comic panel: an admission gate stops a production-tier claim at a sandbox area and points it toward the approved namespace with a helpful sign.](assets/images/self-service-infrastructure/comic-06-the-gate-that-teaches.jpeg)
**Panel 6:** *The gate runs before anything is created — and a rejection that explains trains teams to fix the claim, not to route around the platform.*

![Comic panel: a cleanup robot sweeps expired dev databases into a bin while a production database on a pedestal is left untouched.](assets/images/self-service-infrastructure/comic-07-the-immortal-dev-database.jpeg)
**Panel 7:** *What easy provisioning costs: resources nobody remembers creating — so owner labels are required, dev and staging expire automatically, and production keeps human judgment.*

![Comic panel: a connection secret travels by conveyor from a database into an application that lights up a green healthy indicator, while a chat window with a pasted password is crossed out.](assets/images/self-service-infrastructure/comic-08-the-loop-closes.jpeg)
**Panel 8:** *Provisioning is not the product; a connected application is — credentials arrive by generated secret, never by Slack.*

![Comic panel: Vera ticks two checkboxes in her notebook while a developer walks an unattended path from claim to running app and every resource wears a name tag.](assets/images/self-service-infrastructure/comic-09-the-two-question-test.jpeg)
**Panel 9:** *The test that never stops running: claim to connected application without a human — while every resource can still answer who owns it and why it exists.*
