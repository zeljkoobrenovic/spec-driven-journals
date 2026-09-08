Why the last, unglamorous mile — mail, DNS, obscurity in its place, and a team that keeps learning — decides whether the program is finished — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a celebration around shiny security machines upstairs while Nadia peers into a basement at two dusty pipes labeled MAIL and DNS.](assets/images/the-extra-mile/comic-01-the-basement-pipes.jpeg)
**Panel 1:** *The hook: the last mile is unglamorous — mail and DNS carry every alert, invoice, and login flow, and nobody watches them.*

![Comic panel: rejected envelopes pile up under a crooked signpost while workers inside shrug, weeks crossed off a calendar.](assets/images/the-extra-mile/comic-02-the-quiet-failure.jpeg)
**Panel 2:** *The problem: quiet failures — a wrong record or stale blocklist entry costs deliverability for weeks; these services never page anyone while merely misconfigured.*

![Comic panel: a castle gate hidden behind a bush with no lock, found instantly by a burglar with a beeping scanner.](assets/images/the-extra-mile/comic-03-the-hidden-port-fortress.jpeg)
**Panel 3:** *The wrong way: the hidden-port fortress — SSH on 2222 standing in for patching and MFA is one scan flag away from undefended.*

![Comic panel: a meal with portions labeled Patch, Auth, Access, Monitor gets a tiny pinch from a shaker labeled Obscurity.](assets/images/the-extra-mile/comic-04-seasoning-not-the-meal.jpeg)
**Panel 4:** *The principle: obscurity is only ever an additional layer — patching, authentication, access control, and monitoring are the meal; a plate of pure seasoning goes in the bin.*

![Comic panel: a test parcel labeled NOT OURS is stamped DENIED at a mail counter where three matching ID cards hang.](assets/images/the-extra-mile/comic-05-provably-not-a-relay.jpeg)
**Panel 5:** *Practice: email provably correct — no open relay (confirmed, not assumed), and HELO, forward DNS, and PTR agreeing so the internet can tell our server from a spoof.*

![Comic panel: a cert-renewal envelope slides under a departed employee's dark door on one side and lands on a shared team desk on the other.](assets/images/the-extra-mile/comic-06-mail-to-a-function.jpeg)
**Panel 6:** *Practice: continuity engineering — certificates, licenses, and alerts route to role-based aliases and shared groups, so the function outlives whoever fills it.*

![Comic panel: Nadia closes a valve leaking a network map to an outside hand and mounts a listening sensor that flags an infected host.](assets/images/the-extra-mile/comic-07-dns-leak-and-sensor.jpeg)
**Panel 7:** *Practice: DNS as a security control — recursion restricted, zones no longer leaking the estate's map, and the same ubiquity wired up as a sensor: the sinkhole log is a self-reporting list of infected machines.*

![Comic panel: a balance scale weighs one shield token against a tangle of keys, a fragile clock, and a megaphone of oversized packets.](assets/images/the-extra-mile/comic-08-the-dnssec-scale.jpeg)
**Panel 8:** *The trade-off: DNSSEC is a decision, not a virtue — complexity, botched-rollover risk, and amplification exposure on one pan; deploy only when the benefits clearly outweigh them.*

![Comic panel: Nadia prunes bookmarks by a curated shelf, a teammate solves a CTF puzzle, the skyline shifts outside, Vera checks a final list.](assets/images/the-extra-mile/comic-09-the-team-keeps-learning.jpeg)
**Panel 9:** *The closer: learning is standing work — books, trusted feeds, NVD tracking, CTFs, sources pruned — because a team that stops learning defends last year's threat model; and the Final Review is run, not skimmed.*
