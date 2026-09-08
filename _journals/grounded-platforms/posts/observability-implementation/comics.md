Why observability is done when the loop closes, not when the stack is installed — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an engineer proudly presents a wall of mismatched dashboards during an incident while an executive asks which one shows the users.](assets/images/observability-implementation/comic-01-the-wall-of-dashboards.jpeg)
**Panel 1:** *The hook: a dozen excellent dashboards answer a dozen local questions — and fail the one that matters: what is happening to users right now?*

![Comic panel: three disconnected towers labeled metrics, logs, and traces with broken bridges between them while an engineer runs between carrying papers.](assets/images/observability-implementation/comic-02-three-silos.jpeg)
**Panel 2:** *The problem: metrics say what, logs say how, traces say why — and without common identifiers, the three answers can never be joined into one investigation.*

![Comic panel: an engineer brands a vendor logo onto a row of services while an executive asks what happens when the price changes.](assets/images/observability-implementation/comic-03-the-vendor-tattoo.jpeg)
**Panel 3:** *The wrong way: the vendor tattoo — instrumenting directly against a commercial SDK couples every service to a backend decision that pricing will eventually reopen.*

![Comic panel: an executive draws a circular loop on a whiteboard connecting deploy, telemetry, SLO, alert, and fix while an engineer takes notes.](assets/images/observability-implementation/comic-04-the-closed-loop.jpeg)
**Panel 4:** *The principle: observability is a closed loop — deploy, telemetry, SLO violation, actionable alert, remediation — not a shopping list of tools.*

![Comic panel: a platform engineer beside shared pipeline plumbing hands a starter kit to developers who attach gauges to their own services.](assets/images/observability-implementation/comic-05-pipes-and-instruments.jpeg)
**Panel 5:** *How it plays out: the platform owns the shared pipeline and the contract; teams instrument their own code — with starter kits making the paved path the easy path.*

![Comic panel: a CI/CD conveyor gate passes an instrumented crate and blocks a bare one while the platform engineer says no telemetry, no ship.](assets/images/observability-implementation/comic-06-the-pipeline-gate.jpeg)
**Panel 6:** *How it plays out: CI/CD is the gate — builds fail on missing metrics endpoints, structured logs, or trace spans, so uninstrumented code never reaches production.*

![Comic panel: a cobwebbed wiki SLO contrasted with SLO definitions in Git driving a lever that governs deployment speed via an error budget gauge.](assets/images/observability-implementation/comic-07-slos-in-git.jpeg)
**Panel 7:** *How it plays out: an SLO in a wiki is an opinion; an SLO in Git — reviewed, versioned, deployed through GitOps — is a control system with the error budget as governor.*

![Comic panel: a responder in earmuffs is flooded by pager alerts while one actionable alert goes unnoticed and an executive holds pruning shears.](assets/images/observability-implementation/comic-08-the-pager-firehose.jpeg)
**Panel 8:** *What it costs: every alert that fires without producing action trains responders to ignore the pager — so alerts answer 'what action should I take', or they get pruned.*

![Comic panel: an engineer shows a dashboard with MTTD and MTTR trending down while the executive checks her notebook approvingly.](assets/images/observability-implementation/comic-09-the-receipts.jpeg)
**Panel 9:** *The closer: the build is done when the loop closes and the numbers prove it — MTTD and MTTR trending down, on a dashboard whose definition lives in Git.*
