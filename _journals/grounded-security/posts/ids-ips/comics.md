Why detection is a capability you operate, not a product you bought — in nine panels.

<!-- comic-style
{
  "cast": "VERA: a calm, seasoned engineering executive, short gray-streaked hair, dark blazer over a plain t-shirt, carries a small black notebook. NADIA: a hands-on defensive-security lead, shoulder-length dark hair tied back, navy utility jacket over a plain shirt, an access badge on a lanyard, laptop with a padlock sticker under one arm.",
  "style": "Clean two-tone explainer comic, thick ink outlines, flat colors with deep blue and green accents on a light background, generous white space, hand-lettered speech bubbles with SHORT readable text, no photorealism."
}
-->

![Comic panel: a dusty IDS appliance with an audit-passed ribbon blinks alerts at an empty chair while Vera points at the chair.](assets/images/ids-ips/comic-01-the-shelfware-sensor.jpeg)
**Panel 1:** *The hook: the shelfware sensor — bought for the audit, racked, blinking at an empty chair. Detection hardware is easy to buy; someone reviewing it is the actual control.*

![Comic panel: a searchlight labeled perimeter points outward while an intruder moves between internal buildings in the dark behind it.](assets/images/ids-ips/comic-02-silent-lateral-movement.jpeg)
**Panel 2:** *The problem: the perimeter-only story — inbound and outbound covered, while an attacker already inside moves laterally in a coverage hole shaped exactly like the network's interior.*

![Comic panel: a robot gate labeled IPS block-all stops workers carrying orders and payroll parcels while a small villain slips past.](assets/images/ids-ips/comic-03-day-one-auto-block.jpeg)
**Panel 3:** *The wrong way: day-one auto-block — an IPS switched inline before false positives were measured becomes an outage engine with a security badge.*

![Comic panel: an owl labeled IDS with a detect-log-alert notepad beside an IPS gate whose lever unlocks only after a false-positive checklist.](assets/images/ids-ips/comic-04-detect-then-earn-blocking.jpeg)
**Panel 4:** *The principle: an IDS detects, logs, and alerts; an IPS actively blocks — and the two are held apart, with blocking enabled only where false positives are understood.*

![Comic panel: a periscope labeled NIDS, a stethoscope on a server labeled HIDS, and a cloud radar labeled cloud-native each light a different corner.](assets/images/ids-ips/comic-05-layers-see-differently.jpeg)
**Panel 5:** *Practice: layer the coverage — network sensors watch the wire, host monitoring sees what the network cannot, cloud-native detection moves at cloud speed; each layer's blind spot is another's field of view.*

![Comic panel: an intruder touches a decoy server labeled totally real payroll server in a glass room and a giant bell alerts Nadia.](assets/images/ids-ips/comic-06-the-honeypot-tripwire.jpeg)
**Panel 6:** *Practice: the honeypot economy — a decoy has no legitimate users, so nearly every interaction is signal: the cheapest high-fidelity alert in the estate, isolated and watched.*

![Comic panel: an analyst drowning in alerts reaches for a mute switch while Nadia adjusts a console with threshold, range, and severity sliders.](assets/images/ids-ips/comic-07-tune-dont-silence.jpeg)
**Panel 7:** *Practice: alert fatigue is an engineering defect, not analyst weakness — noisy rules get thresholds, ranges, and exclusions adjusted or demoted to log-only; tuning never ends.*

![Comic panel: sealed envelopes pass a scanner showing question marks while Vera weighs a TLS inspection key against privacy and legal weights and Nadia dusts an envelope for JA3 fingerprints.](assets/images/ids-ips/comic-08-the-encrypted-blind-spot.jpeg)
**Panel 8:** *The cost: encryption forced a choice — inspect deliberately where it is worth the performance, privacy, and legal price, and read the envelope's fingerprints everywhere else. The worst option is pretending the blind spot isn't there.*

![Comic panel: Nadia works a tidy alert queue with reviewed stamps and a named owner while Vera checks her notebook.](assets/images/ids-ips/comic-09-who-reviewed-this-week.jpeg)
**Panel 9:** *The closer: the first review question is never 'do we have an IDS?' — it is 'who reviewed its alerts this week, and what did they do about them?' Alerts only have value when someone reviews them and knows how to respond.*
