Why logging is the ability to answer questions during the worst hour, not storage — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: an incident room at 3 AM with question bubbles raining down over Nadia at a console while Vera asks if they can answer.](assets/images/logging-and-monitoring/comic-01-the-worst-hour.jpeg)
**Panel 1:** *The hook: the worst hour — an incident is a stream of questions under time pressure, and the logging estate either answers them or it does not.*

![Comic panel: Nadia with a tiny flashlight inside a colossal warehouse of unlabeled log boxes while a cash meter spins.](assets/images/logging-and-monitoring/comic-02-the-log-warehouse.jpeg)
**Panel 2:** *The problem: the write-only SIEM — terabytes ingested, licensing paid, nothing read; collecting everything is a decision to find nothing.*

![Comic panel: an exhausted analyst bulk-stamps a mountain of red alerts while one card with a burglar icon slides past unnoticed.](assets/images/logging-and-monitoring/comic-03-the-thousand-alert-morning.jpeg)
**Panel 3:** *The wrong way: the thousand-alert morning — untuned rules train analysts to bulk-acknowledge, and the real intrusion drowns in ignored red.*

![Comic panel: Vera places a crown-jewel gem on a map and draws cameras around it while Nadia pins a coverage grid with circled gaps.](assets/images/logging-and-monitoring/comic-04-risk-backwards.jpeg)
**Panel 4:** *The principle: design from risk backwards — highest-value systems and explicit use cases first, mapped to a framework so the gaps have names.*

![Comic panel: an intruder shreds local logs while a pneumatic tube whisks copies to a distant vault guarded by Nadia.](assets/images/logging-and-monitoring/comic-05-beyond-the-attackers-reach.jpeg)
**Panel 5:** *Practice: centralize under a Record of Authority — attackers delete local logs, so the copy the investigation relies on lives beyond their reach, with location and retention written down.*

![Comic panel: an intruder's footprint trail passes login, endpoint, DNS, cloud, and database stations, each watched by a lit camera.](assets/images/logging-and-monitoring/comic-06-the-attackers-path.jpeg)
**Panel 6:** *Practice: coverage follows the attacker's path — identity, endpoints, applications, cloud, databases, DNS, and the perimeter each get a camera, because a gap in any one is an unrecorded corridor.*

![Comic panel: Nadia triggers a mock attack in a glass lab while Vera checks off a log light and a ringing alert bell.](assets/images/logging-and-monitoring/comic-07-pull-the-alarm.jpeg)
**Panel 7:** *Practice: tested, not trusted — a detection that has never fired in a test is a hypothesis, so the behavior is reproduced and both the log and the alert are confirmed.*

![Comic panel: Nadia prunes a cobwebbed alert bell-flower and waters new sprouts while Vera records the changes.](assets/images/logging-and-monitoring/comic-08-the-decaying-garden.jpeg)
**Panel 8:** *The upkeep: the SIEM decays by default — noisy rules pruned, detections updated with new systems and threats, retention and capacity reviewed, every change documented.*

![Comic panel: an analyst answers a ringing alert with its chained playbook while an alert without a playbook lies in the bin.](assets/images/logging-and-monitoring/comic-09-what-happens-when-it-fires.jpeg)
**Panel 9:** *The closer: the bar the estate is held to — every enabled alert is one analysts know how to investigate, and every claimed detection has been proven to fire.*
