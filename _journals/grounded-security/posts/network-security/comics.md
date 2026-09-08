Why the network is inventoried, hardened, patched, and watched — and proven by a scan, not a diagram — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: Nadia shines a flashlight on a cobwebbed switch tagged not in inventory while Vera checks a clipboard.](assets/images/network-security/comic-01-the-unknown-switch.jpeg)
**Panel 1:** *The hook: the unknown device — a switch no inventory lists, unpatched for years, discovered only when it shows up in an incident timeline.*

![Comic panel: rack devices with factory tags reading admin/admin, public, private while a door opens itself for an attacker.](assets/images/network-security/comic-02-defaults-everywhere.jpeg)
**Panel 2:** *The problem: factory defaults — credentials, community strings, and Telnet still on mean the estate answers to anyone who asks.*

![Comic panel: a framed diagram stamped hardened 2019 hides a real rack with glowing open ports and creeping weeds as Nadia looks behind it.](assets/images/network-security/comic-03-the-diagram-says-secure.jpeg)
**Panel 3:** *The wrong way: the hardened-once network — baselines applied at deployment, never revalidated, while drift quietly un-hardens the estate and the documentation stays green.*

![Comic panel: Vera scans a rack with a beam, devices show green checks except one red open port that Nadia moves to fix.](assets/images/network-security/comic-04-proven-by-a-scan.jpeg)
**Panel 4:** *The principle: inventoried, hardened, patched, watched — and the claim is proven by a scan, not asserted in a diagram, then re-proven after every change.*

![Comic panel: a fortified room labeled management network reached only by a bastion drawbridge with MFA keypad, Nadia crossing with her badge.](assets/images/network-security/comic-05-the-management-vault.jpeg)
**Panel 5:** *Practice: the management plane is the crown jewels — dedicated network, never internet-exposed, entered through a hardened MFA bastion with individual, centrally authenticated accounts.*

![Comic panel: midnight CLI changes vanish into smoke on one side; on the other a reviewed config template pipeline with a separate secrets safe.](assets/images/network-security/comic-06-config-is-code.jpeg)
**Panel 6:** *Practice: configuration is code — version-controlled templates, peer review, tested deployment; secrets live in a dedicated store, never in the repository.*

![Comic panel: a burglar with a data sack blocked at an exit turnstile labeled egress filter while a denied-log lamp lights on Nadia's desk.](assets/images/network-security/comic-07-egress-catches-the-thief.jpeg)
**Panel 7:** *Practice: filter outbound as strictly as inbound — a host repeatedly denied an unexpected connection is one of the cheapest, highest-signal alerts the organization will ever get.*

![Comic panel: attackers probe a rusty VPN gate, a fake Wi-Fi antenna, and an unguarded tunnel labeled IPv6 while Vera watches from a tower.](assets/images/network-security/comic-08-the-soft-edges.jpeg)
**Panel 8:** *The cost: the perimeter's soft edges — unpatched VPN appliances, evil-twin access points, and an IPv6 network nobody guards are where compromise walks in.*

![Comic panel: a sweating network device interrogated under a lamp as Vera reads four questions and Nadia holds a work-order pad.](assets/images/network-security/comic-09-four-questions.jpeg)
**Panel 9:** *The closer: every device answers four questions — who inventoried it, which baseline hardened it, when it was patched, when its hardening was last re-verified. No answers, next work item.*
