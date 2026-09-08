---
timetoread: "7 min listen"
---

## Why People, Not Just Filters

**Ben:** I'll start where every budget conversation starts. We pay for serious email security — filtering, link rewriting, attachment sandboxing. If those work, phishing awareness is redundant; if they don't, I should fix the filters. Why is the answer "train everyone"?

**Ana:** Because the filters and the training defend against different messages. Filters catch volume — the sloppy campaigns, the known-bad domains. The attack that matters is the one engineered to pass them: clean domain, no malware in the message body, plausible pretext, one link. That one lands in front of a human, every time. This record is the executive commitment behind a checklist the handbook wrote for *every employee* — not for responders. It's the handout: a short verification habit before clicking, plain-language warning signs, and a report-fast path for both the click and the near-miss.

**Ben:** A "verification habit" that people run on hundreds of messages a day? Nobody sustains that.

**Ana:** They don't have to run all of it on everything — that's why the questions are cheap and self-triggering. Was I expecting this? Do I recognize the sender, and does the address actually match who it claims to be? Is it manufacturing urgency? Is it asking for credentials or money? A normal message clears those in a second without conscious effort. The habit only bites on the message that's unexpected, pressured, or asking for something sensitive — which is precisely the profile of the attack the filters missed.

**Ben:** The urgency point interests me, because real work is urgent constantly. How does an employee tell attacker urgency from CFO urgency?

**Ana:** They don't have to tell them apart — that's the trick. The record inverts the attack: pressure itself is the warning sign, and the response to pressure is a thirty-second out-of-band check. Call the known number, message the known handle — never reply to the message that made the request. Real CFO urgency survives thirty seconds of verification effortlessly. Attacker urgency dies there, because the attacker controls the message but not the second channel. Nearly every phish runs on the same engine — manufactured time pressure that switches people from judgment to compliance — so teaching "the harder it pushes, the more suspicious it is" defuses the whole engine at once.

## Feels, Looks, Sounds

**Ben:** The warning signs read almost childishly — "something feels funny," "something looks funny," "something sounds funny." Is that register really appropriate for an operating record?

**Ana:** It's the most deliberate design choice in the chapter. An employee who can say "something sounded funny about that call" reports. An employee who believes reporting requires technical vocabulary — "I observed a suspected credential-harvesting attempt" — stays silent. The sensory language lowers the bar to exactly where it belongs: gut level. And look at what the three families actually cover. Feels funny: you logged in and bounced straight back to the login page — your credentials are already harvested. Looks funny: the macro prompt, the attachment with the weird error, the familiar site on a wrong URL, the USB drive in the parking lot. Sounds funny: the caller from "IT" who needs your password, the vendor probing about your systems.

**Ben:** Half of those aren't email.

**Ana:** That's the second point of the three families. Vishing, smishing, baiting with found media — the same con through different channels. Train only the inbox and the attacker walks around your training with a phone call. The record explicitly covers what must be reported: suspicious calls, messages, websites, and removable media, not just email.

**Ben:** And the one absolute — never give your username or password to another person. Not even IT? That feels dogmatic. Sometimes support genuinely needs access.

**Ana:** Legitimate IT never needs your password — they have administrative paths for everything they legitimately do. That's exactly why the rule can be absolute, and absolute is the point: under stress, people fall back on the simplest rule they know, and stress is when phishing strikes. The moment you allow "unless it's really IT," you've handed the attacker their pretext, because *claiming to be IT is the attack*. It's the first line in the sounds-funny list. A rule with exceptions is a negotiation; this one has to be a reflex. And [[authentication]] backs the reflex technically — MFA bounds the damage when a password leaks anyway.

## The Minutes After the Click

**Ben:** Now the heart of it. Someone clicks, enters their password, realizes. You know what happens in most companies: they change the password quietly, tell no one, and hope. Why would this record's employee behave differently?

**Ana:** Because the record spends its cultural capital on exactly that moment. Walk through what the clicked employee holds: what was clicked, what happened next, and the single highest-value fact in the whole exchange — whether credentials went in. The response needs that intelligence in minutes. The only variable is whether the person surrenders it or sits on it, and that's decided entirely by what happened to the last person who reported. Every ounce of blame added to the reporting path converts directly into attacker dwell time. Hence the record's test: the employee who clicked reports within minutes, because they know they'll be helped, not punished.

**Ben:** "Helped, not punished" — but there are consequences. Password resets, device checks. Doesn't that feel like punishment from the receiving end?

**Ana:** Only if it's framed that way, which is why the record refuses the framing. The resets and checks are the help — they're what stops the stolen credential from becoming a breach. The after-click path is rehearsed in onboarding so it feels like a fire drill, not a confession: stop interacting, enter nothing more, contact the help desk, say what happened, answer the credentials question honestly, follow instructions. People answer that question honestly exactly once: when honesty is safe. The anti-pattern — the shame spiral — buys you an organization where clicks go quiet and attackers get days instead of minutes.

**Ben:** What about the employee who didn't click? They spotted it, deleted it, moved on. No harm done, surely.

**Ana:** That deletion discarded the campaign's earliest warning. Phishing arrives in campaigns — the message one person deleted is sitting unread in thirty other inboxes. So the record insists: no click still means report, keep the message for review, and — the counterintuitive one — never forward it to coworkers as a warning. The helpful forward spreads the live payload faster than the attacker's own send. Warnings travel through IT's channel; one report protects everyone who received the same attack.

## The Blank Lines at the Bottom

**Ben:** The checklist ends with fill-in-the-blank lines. Help desk, phishing report method, after-hours contact. Rather anticlimactic for a defense doctrine.

**Ana:** Those three lines are the executive test of the whole record. Everything above them — the habit, the warning signs, the blame-free reporting — collapses if suspicion has nowhere to go. A reporting culture with an unfilled contact line is a poster, not a defense. And note the third line: after-hours. Phishing doesn't keep business hours, and the employee who realizes at 9 p.m. on a Friday that they entered their password needs a number that answers. Filling those lines, publishing them, keeping them current — that's not formatting, that's the program. My concrete bar: anyone in the organization, asked at random, can name the way to report a phish.

**Ben:** And when a report with a click comes in, this record's job is done?

**Ana:** It hands off. A reported click becomes a suspected incident, and [[incident-response]] takes it — same early-escalation culture, applied to everyone rather than just engineers. This record is that record's front porch. The teaching machinery lives in [[user-education]]; the endpoint hardening that absorbs the clicks that slip through lives in [[endpoints]].

**Ben:** Then here's my concession, and it's a reframe. I came in thinking phishing awareness was training people not to click. It's actually building a sensor network out of the whole organization — cheap verification at every node, plain-language signal definitions, and a reporting channel that people trust enough to use within minutes, especially when they're the ones who tripped.

**Ana:** That's the record. The click will happen — the defense was never "nobody ever clicks." The defense is that the click is reported before it becomes a breach. Filters catch the volume; the culture catches the one that got through. And the whole thing is measured by a single moment: the employee, password already entered, picking up the phone anyway.
