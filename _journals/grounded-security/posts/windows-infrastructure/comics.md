Why a Windows estate is one security system with the forest as its boundary — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: Nadia shows Vera a wall map of servers joined by glowing lines into a single web labeled one system.](assets/images/windows-infrastructure/comic-01-one-system-not-a-fleet.jpeg)
**Panel 1:** *The hook: a Windows estate is one security system, not a fleet of servers — authentication, trust, and policy connect every machine to every other.*

![Comic panel: an intruder hops across stepping stones labeled shared password, old trust, open share toward a glowing crown.](assets/images/windows-infrastructure/comic-02-walking-the-graph.jpeg)
**Panel 2:** *The problem: an attacker who lands on one workstation walks the graph — shared local passwords, forgotten trusts, writable shares, over-privileged service accounts.*

![Comic panel: a crowned server plastered with file server, print server, and jump box signs as people plug cables in, Vera horrified.](assets/images/windows-infrastructure/comic-03-the-dual-purpose-dc.jpeg)
**Panel 3:** *The wrong way: the dual-purpose domain controller — the estate's root of trust carrying the estate's everyday attack surface.*

![Comic panel: Vera draws a solid wall around a forest with dotted internal fences labeled domains and one tagged bridge through the wall.](assets/images/windows-infrastructure/comic-04-the-forest-is-the-boundary.jpeg)
**Panel 4:** *The principle: the forest is the security boundary, domains are containers — and every trust through the wall is documented, minimized, and removed when it stops earning its risk.*

![Comic panel: a domain controller in a locked museum display case beside a framed compromise recovery plan, Nadia standing guard.](assets/images/windows-infrastructure/comic-05-crown-jewel-controllers.jpeg)
**Panel 5:** *Practice: domain controllers get crown-jewel treatment — dedicated, physically secured, encrypted, logon-restricted, with a tested compromise plan that honestly contemplates forest rebuild.*

![Comic panel: Nadia holds a ring of uniquely name-tagged keys beside a bin of crossed-out shared keys and a log listing named authors.](assets/images/windows-infrastructure/comic-06-every-action-has-an-author.jpeg)
**Panel 6:** *Practice: privilege minimization is an attribution guarantee — minimal Domain Admins, unique managed local passwords, dedicated service accounts, no shared identities.*

![Comic panel: laptops on a conveyor are stamped with shields by a Group Policy machine while a drifting laptop is pulled back by a baseline magnet.](assets/images/windows-infrastructure/comic-07-the-baseline-wins-arguments.jpeg)
**Panel 7:** *Practice: a baseline that is not enforced is a preference — Group Policy built on recognized baselines pulls machines back from drift, and new systems land managed from birth.*

![Comic panel: a legacy computer in a fenced pen with owner and exception tags, and a backup vault an intruder with stolen keys cannot reach.](assets/images/windows-infrastructure/comic-08-legacy-named-backups-tested.jpeg)
**Panel 8:** *The cost: legacy is a signed risk decision — named, isolated, owned — and recovery assumes the credentials are gone: tested AD restores from backups ordinary admin compromise cannot touch.*

![Comic panel: Vera holds a four-question card as Nadia hands over four folders labeled unsupported list, Domain Admins, trust map, last restore test.](assets/images/windows-infrastructure/comic-09-four-questions-one-day.jpeg)
**Panel 9:** *The closer: the record's health check — the unsupported-systems list, Domain Admins membership, the trust map, and the last restore-test date, each producible within a day.*
