Why the front door of a platform is an API and not a portal — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a shiny portal door opens onto a ticket-counter queue while Vera points and Kai looks embarrassed.](assets/images/self-service-onboarding/comic-01-the-ticket-behind-the-portal.jpeg)
**Panel 1:** *The hook: the ticket behind the portal — a shiny front door with a queue hidden inside is self-service theater, not self-service.*

![Comic panel: developer teams queue at a toll booth staffed by Kai while a calendar shows weeks passing.](assets/images/self-service-onboarding/comic-02-the-queue-tax.jpeg)
**Panel 2:** *The problem: every new team pays the queue tax — the platform team becomes the bottleneck it was built to remove.*

![Comic panel: a bloated portal screen has swallowed provisioning machinery while a CLI and a script wait outside a velvet rope.](assets/images/self-service-onboarding/comic-03-the-portal-that-ate-the-platform.jpeg)
**Panel 3:** *The wrong way: the portal that ate the platform — logic buried in the portal is untestable, unswappable, and closed to every other client.*

![Comic panel: Kai shows a doorway labeled Onboarding API v1 with equal paths from a portal, a CLI, and a script.](assets/images/self-service-onboarding/comic-04-api-first-front-door.jpeg)
**Panel 4:** *The principle: API-first, portal second — provisioning logic lives behind a versioned, schema-validated API, and the portal is one swappable client.*

![Comic panel: one button press delivers a crate containing namespace, RBAC, quota, groups, repo, and catalog to a new team.](assets/images/self-service-onboarding/comic-05-one-call-whole-bundle.jpeg)
**Panel 5:** *How it plays out: a team is one call, fully provisioned — namespace, RBAC, quotas, identity groups, repository, and catalog entry arrive together.*

![Comic panel: duplicates pile up on one side while on the other a retry neatly completes a half-finished bundle.](assets/images/self-service-onboarding/comic-06-retry-converges.jpeg)
**Panel 6:** *The safeguard: every step idempotent — retrying a partial failure converges on the desired state instead of minting duplicates.*

![Comic panel: a pre-fenced yard with quota and policy fence sections, three labeled gate keys, and an audit ledger on the gate.](assets/images/self-service-onboarding/comic-07-guardrails-in-the-crate.jpeg)
**Panel 7:** *The guardrails ship in the bundle: tiered quotas, three standing roles, network policies, and an audit trail arrive with the namespace — never retrofitted.*

![Comic panel: a developer with a lone repo box and a long to-do list next to Kai's complete project kit crate.](assets/images/self-service-onboarding/comic-08-repo-is-not-a-project.jpeg)
**Panel 8:** *The unit: a repository is not a project — a project ships repo, namespaces, pipeline, catalog entry, and docs together, from a template, in one go.*

![Comic panel: Vera holds a stopwatch at five minutes as a developer's first deploy launches and Kai checks a small dashboard.](assets/images/self-service-onboarding/comic-09-the-five-minute-test.jpeg)
**Panel 9:** *The closer: the five-minute test — portal form to first deployment, no ticket, no platform engineer in the loop, re-run whenever the path changes.*
