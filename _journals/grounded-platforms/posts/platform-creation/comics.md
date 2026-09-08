Why the platform must exist in Git, not in the clusters — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. KAI: a hands-on platform engineering lead, short dark hair, gray zip-up hoodie with a small gear pin, laptop covered in infrastructure stickers under one arm, a coil of cable slung over the shoulder.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and teal accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: at night, Vera asks Kai whether glowing server clusters could be rebuilt by morning if they vanished.](assets/images/platform-creation/comic-01-the-midnight-question.jpeg)
**Panel 1:** *The hook: the only test that matters — if the clusters vanished tonight, could the pipeline rebuild every environment by morning?*

![Comic panel: a patched, snowflake-shaped production server no longer matches the clean configuration file Kai is holding.](assets/images/platform-creation/comic-02-the-snowflake.jpeg)
**Panel 2:** *The problem: the snowflake environment — patched by hand until production no longer resembles what was tested, and Git history is fiction.*

![Comic panel: version labels float away as balloons while Kai rebuilds a platform that no longer matches the original photo.](assets/images/platform-creation/comic-03-the-floating-latest.jpeg)
**Panel 3:** *The wrong way: floating latest tags and wildcard versions — a platform that cannot be rebuilt, only re-discovered, one incident at a time.*

![Comic panel: Vera shows a Git cabinet with two drawers, one building clusters and one feeding running services.](assets/images/platform-creation/comic-04-the-platform-lives-in-git.jpeg)
**Panel 4:** *The principle: the platform exists in Git, not in the clusters — provisioning in one repository, runtime configuration in another.*

![Comic panel: a change crate rides one conveyor through sandbox, dev, and a stamped approval gate before prod.](assets/images/platform-creation/comic-05-one-pipeline-promotes.jpeg)
**Panel 5:** *How it plays out: one pipeline promotes every change — sandbox first, then dev, then a recorded approval before production.*

![Comic panel: a mechanical arm from a Git book reverses Kai's manual dial change and prints a log slip.](assets/images/platform-creation/comic-06-drift-reconciled.jpeg)
**Panel 6:** *How it plays out: drift is corrected, visibly — a Git commit is what changes the cluster, and break-glass fixes are reversed and logged.*

![Comic panel: a robot bouncer turns away a manifest tagged latest at the GitOps repository door while a pinned one enters.](assets/images/platform-creation/comic-07-the-policy-bouncer.jpeg)
**Panel 7:** *How it plays out: misconfiguration dies in the pipeline — policy-as-code rejects floating tags before they ever reach the GitOps repository.*

![Comic panel: Kai installs mTLS padlocks and a gateway in an empty platform while Vera weighs a proxy on a scale.](assets/images/platform-creation/comic-08-locks-before-tenants.jpeg)
**Panel 8:** *What it costs: the mesh goes in before the tenants — mTLS is configuration on an empty platform, a migration on a full one — and its overhead is measured from day one.*

![Comic panel: at sunrise a pipeline rebuilds three environments from a Git tag while Vera and Kai look on satisfied.](assets/images/platform-creation/comic-09-rebuilt-by-morning.jpeg)
**Panel 9:** *The closer: a semantic version tag rebuilds every environment by morning — a platform you cannot rebuild is a platform you do not own.*
