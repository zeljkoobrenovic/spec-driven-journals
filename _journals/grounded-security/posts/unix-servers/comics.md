How a Unix application server earns its place on the network — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a server on a podium at a network checkpoint under spotlights labeled runs, listens, writable, as Nadia holds a checklist.](assets/images/unix-servers/comic-01-earning-its-place.jpeg)
**Panel 1:** *The hook: a server's attack surface is what runs, what listens, and what is writable — everything else is noise to remove, so every server earns its place on the network.*

![Comic panel: a dusty server covered in small ajar doors tagged enabled 2019 and purpose unknown, Nadia shining a flashlight.](assets/images/unix-servers/comic-02-the-everything-daemon.jpeg)
**Panel 2:** *The problem: the everything daemon — services enabled years ago and never inventoried since, each an unattended door, none with a known purpose.*

![Comic panel: a frazzled engineer spray-paints 777 on a file cabinet and bins a SELinux shield labeled temporary while Vera watches.](assets/images/unix-servers/comic-03-777-and-setenforce-0.jpeg)
**Panel 3:** *The wrong way: world-writable and working — permissions loosened to fix a deployment and never tightened, SELinux disabled as troubleshooting and never re-enabled.*

![Comic panel: Vera shows a bloated server shrinking to a clean cube with four slots labeled running, reachable, writable, privileged.](assets/images/unix-servers/comic-04-shrink-and-verify.jpeg)
**Panel 4:** *The principle: shrink and verify — only what the application requires is running, reachable, writable, and privileged, and the server still does its job.*

![Comic panel: Nadia walks small patch-labeled steps while another engineer faces a cracked cliff labeled big-bang upgrade.](assets/images/unix-servers/comic-05-small-steps-beat-heroics.jpeg)
**Panel 5:** *Practice: a small patching cadence beats patching heroics — deferred updates pile into the risky big-bang upgrade, and software the package manager cannot see gets its own advisory subscriptions.*

![Comic panel: a gremlin tagged web app account fenced into a small circle of files, unable to reach shelves labeled customer data.](assets/images/unix-servers/comic-06-blast-radius-filesystem.jpeg)
**Panel 6:** *Practice: the filesystem is least privilege made concrete — what the application account can read and write is the blast radius, so a compromised app becomes a contained nuisance, not a data breach.*

![Comic panel: a server holding a host-firewall shield with one open slot while a file-integrity tripwire bell rings and Nadia investigates.](assets/images/unix-servers/comic-07-the-host-defends-itself.jpeg)
**Panel 7:** *Practice: the host defends itself — a firewall permitting only required traffic, and file-integrity monitoring against a trusted baseline whose alerts are investigated, not muted.*

![Comic panel: an app in a clear container watched by a MAC guard robot as a dial is turned from permissive to enforce under a sign reading app still works.](assets/images/unix-servers/comic-08-contained-and-still-working.jpeg)
**Panel 8:** *Practice: applications run isolated, non-root, and confined by mandatory access control — permissive mode during testing, then enforcement, with every restriction verified against required function so it survives the 2 a.m. rollback.*

![Comic panel: Vera holds two question cards while Nadia points at a large zero on a board next to a tidy humming server.](assets/images/unix-servers/comic-09-the-two-questions.jpeg)
**Panel 9:** *The closer: two questions for any server — what is listening that the app does not require, and what can its account read that it does not need? Both should answer: nothing. And the review repeats; it is never archived.*
