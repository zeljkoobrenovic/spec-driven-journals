Why no single authentication control is ever asked to carry the day alone — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a burglar ignores a heavily locked front door labeled MFA and heads for an unlocked side door labeled password reset while Nadia points.](assets/images/authentication/comic-01-the-side-door.jpeg)
**Panel 1:** *The hook: attackers never fight the strong control — they find its weak sibling, and the weakest login path is the real posture.*

![Comic panel: Vera inspects a cobwebbed, still-glowing drawer labeled contractor access next to a calendar reading 18 months ago.](assets/images/authentication/comic-02-the-immortal-account.jpeg)
**Panel 2:** *The problem: dormant identity — valid credentials, monitored by no one, missed by no one, surviving long after their owner left.*

![Comic panel: a worker types Summer2026! under a complexity policy poster while Nadia facepalms holding a rejected long passphrase card.](assets/images/authentication/comic-03-complexity-theater.jpeg)
**Panel 3:** *The wrong way: complexity theater — rules that produce 'Summer2026!' on schedule while banning the long passphrase that would actually resist attack.*

![Comic panel: Vera and Nadia in front of a five-layer wall labeled least privilege, central IAM, strong passwords, secure protocols, MFA, one layer cracked but the wall standing.](assets/images/authentication/comic-04-the-layered-wall.jpeg)
**Panel 4:** *The principle: layered defense — least privilege, centralized IAM, strong passwords, secure protocols, and MFA together; remove any one layer and the others still hold.*

![Comic panel: as an employee exits, an automated console arm switches off a row of account icons while Nadia watches.](assets/images/authentication/comic-05-access-ends-same-day.jpeg)
**Panel 5:** *Practice: centralize identity — SSO and automated provisioning mean accounts appear and disappear with the people they belong to, the day they leave.*

![Comic panel: a vault labeled password manager with long passphrases beside a database labeled salted slow hashes shrugging off a rainbow table magnet.](assets/images/authentication/comic-06-the-vault-and-the-hash.jpeg)
**Panel 6:** *Practice: length beats complexity, uniqueness beats reuse — passphrases live in a vetted manager, and storage assumes the breach with salted, deliberately slow hashes.*

![Comic panel: a wall diagram says Kerberos while Nadia's magnifying glass over the cable reveals NTLM packets from a sheepish old server.](assets/images/authentication/comic-07-what-it-actually-speaks.jpeg)
**Panel 7:** *Practice: protocol literacy — know NTLM's and Kerberos's attacks, and verify what a system actually speaks in configuration, logs, and packets before believing the diagram.*

![Comic panel: a user buried in approve notifications at night while a hacker grins, and Vera holds up a code-matching phone screen.](assets/images/authentication/comic-08-the-push-bombing.jpeg)
**Panel 8:** *The cost: MFA is necessary and insufficient — push bombing exploits the approve reflex, so the record buys MFA's value at its honest price: code-matching, protected enrollment, reviewed exclusions.*

![Comic panel: a new system waits at a gate while Vera reads three checklist questions and Nadia bars the way.](assets/images/authentication/comic-09-three-questions.jpeg)
**Panel 9:** *The closer: before anything ships — where does its identity come from, how are credentials stored, which protocol does it actually speak? No answers, no launch.*
