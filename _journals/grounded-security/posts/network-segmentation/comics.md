Why lateral movement is minimized by design, not by hope — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an intruder on one workstation in an open floor with servers and a domain controller all one hop away, Nadia alarmed at a monitor.](assets/images/network-segmentation/comic-01-one-hop-from-everything.jpeg)
**Panel 1:** *The hook: the flat network — the attacker who lands on one workstation has landed everywhere; the file servers, database, and domain controller are all one hop away.*

![Comic panel: a castle with a massive gate labeled firewall but a single open hall inside where an intruder strolls between treasure rooms.](assets/images/network-segmentation/comic-02-castle-with-open-halls.jpeg)
**Panel 2:** *The problem: a hard perimeter around one big trusted interior — the firewall at the front, and nothing between the first phished workstation and everything the organization owns.*

![Comic panel: paper curtains labeled VLAN 10, 20, 30 divide a room while an intruder hops over one marked trunk port and Nadia lifts an edge.](assets/images/network-segmentation/comic-03-the-vlan-curtain.jpeg)
**Panel 3:** *The wrong way: the VLAN mistaken for a wall — tags without ACLs or hopping protections are separation that ends at the first misconfigured trunk port.*

![Comic panel: Vera shows a floor plan of sealed compartments with a few permit-stamped doors under a sign reading default deny.](assets/images/network-segmentation/comic-04-least-privilege-for-packets.jpeg)
**Panel 4:** *The principle: segmentation is least privilege applied to traffic — segments drawn by risk, function, sensitivity, and business need; every approved flow documented, everything else denied.*

![Comic panel: a fortified island labeled DMZ between a stormy internet sea and the mainland, connected only by a narrow guarded checkpoint bridge.](assets/images/network-segmentation/comic-05-the-dmz-island.jpeg)
**Panel 5:** *Practice: internet-facing systems live in a DMZ — deny by default, only required ports in, no free path inward, and watched more closely because they absorb more risk.*

![Comic panel: devices queue at a NAC gate; a badged laptop passes, an unknown gadget is diverted to a quarantine room, a guest phone gets internet-only.](assets/images/network-segmentation/comic-06-admission-is-earned.jpeg)
**Panel 6:** *Practice: admission is earned — 802.1X authentication and posture checks before access, quarantine for the unknown, internet-only paths for guests; trust moves from the jack to the device.*

![Comic panel: an admin with separate standard and privileged key cards, doors labeled dev and prod, and a create/approve two-person desk.](assets/images/network-segmentation/comic-07-people-are-segmented-too.jpeg)
**Panel 7:** *Practice: duty separation is segmentation of people — dev apart from prod, creation split from approval, separate standard and privileged accounts, no shared generic admin.*

![Comic panel: a ghostly cobwebbed bridge labeled ANY-ANY temp fix 2024 spans two zones as an intruder crosses and Nadia arrives with shears.](assets/images/network-segmentation/comic-08-the-any-any-ghost.jpeg)
**Panel 8:** *The cost: the ANY-ANY that never died — a rule base that only grows decays default-deny into a deny-list, one 'temporary' exception at a time; pruning is part of the design.*

![Comic panel: Nadia fires a test dart labeled prohibited traffic that bounces off a segment wall with a blocked-verified stamp while Vera nods.](assets/images/network-segmentation/comic-09-prove-it-blocked.jpeg)
**Panel 9:** *The closer: an untested boundary is a diagram — pick a segment, attempt the traffic that should be impossible, and watch it fail. Lateral movement is minimized by design, not by hope.*
