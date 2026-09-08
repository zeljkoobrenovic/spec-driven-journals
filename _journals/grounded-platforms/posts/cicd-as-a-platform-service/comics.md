Why CI/CD stops being a per-team craft and becomes a product the platform ships — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an engineer unrolls an enormous scroll of pipeline code across the floor while an executive watches and says it is not that team's problem.](assets/images/cicd-as-a-platform-service/comic-01-the-growing-workflow.jpeg)
**Panel 1:** *The hook: a team's workflow file keeps growing — and that is not that team's problem to solve.*

![Comic panel: an engineer pushes a cart of identical pull requests toward a wall of near-identical filing cabinets, one per repository.](assets/images/cicd-as-a-platform-service/comic-02-copy-paste-estate.jpeg)
**Panel 2:** *The problem: copy-paste is how pipeline debt compounds — every improvement becomes N pull requests, every bug becomes immortal.*

![Comic panel: a scanner flags containers on a conveyor belt that still carries them into the registry, under a dashboard full of warnings.](assets/images/cicd-as-a-platform-service/comic-03-the-advisory-scanner.jpeg)
**Panel 3:** *The wrong way: the advisory scanner — a scan that ships anyway just fills the registry with known-vulnerable images and the dashboard with guilt.*

![Comic panel: an executive presents a versioned product box labeled platform pipelines, connected by threads to many small team desks.](assets/images/cicd-as-a-platform-service/comic-04-cicd-as-a-product.jpeg)
**Panel 4:** *The principle: one platform repository, run like a product — semantically versioned, tested by its own CI, consumed by reference.*

![Comic panel: an engineer holds a small thirty-line card labeled what, in front of a glass machine room labeled how.](assets/images/cicd-as-a-platform-service/comic-05-the-thirty-line-wrapper.jpeg)
**Panel 5:** *How it plays out: the thirty-line wrapper — teams declare what their service needs; everything about how lives in platform templates.*

![Comic panel: a closed gate blocks a container marked critical from the registry while clean containers pass through.](assets/images/cicd-as-a-platform-service/comic-06-the-scan-gate.jpeg)
**Panel 6:** *How it plays out: the build gate — HIGH or CRITICAL fails the build, and a vulnerable image never reaches the registry.*

![Comic panel: a mechanical arm lifts a canary carrying a new-release flag back to a stable platform as a metric gauge dips red.](assets/images/cicd-as-a-platform-service/comic-07-the-canary-retreats.jpeg)
**Panel 7:** *How it plays out: progressive delivery — the platform watches every release against live metrics and retreats automatically, no 2 a.m. heroics.*

![Comic panel: two people study a dashboard tracing a pipeline from trigger to deploy, with one slow stage highlighted and improving bars.](assets/images/cicd-as-a-platform-service/comic-08-the-measured-pipeline.jpeg)
**Panel 8:** *What it proves: an instrumented pipeline — stage timings, DORA metrics, and adoption on a dashboard rather than in a slide.*

![Comic panel: an executive pins a piece of team pipeline code onto a roadmap board under next platform capability.](assets/images/cicd-as-a-platform-service/comic-09-the-missing-capability.jpeg)
**Panel 9:** *The closer: the test that keeps running — a growing team pipeline is not that team's problem; it is a platform capability we have not built yet.*
