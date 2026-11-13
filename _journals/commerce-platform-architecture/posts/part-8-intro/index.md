---
title: "Part VIII — TRUST: Security, Privacy and Regulation"
date: 2026-11-07
author: Željko Obrenović
excerpt: "What can go wrong on purpose, and what the law requires: card testing, skimmers and leaked keys; the personal data a shop holds and the person's rights over it; and the consumer, payment, invoicing and platform rules that arrive with a date. Part VIII argues that on a hosted platform trust is an inventory problem before it is a technology or a legal one: every identity with its key, every system with its legal role and retention clock, every rule with its owner and date, kept on the map the earlier parts built."
permalink: part-8
timetoread: 8 min read
icon: "assets/icons/part-8-intro.png"
logo: "assets/images/part-8-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **Attackers use the shop as built.** Card testing, credential stuffing and skimming are the checkout and login at machine speed; the merchant secures every identity, key, app and script it adds.
> * **The order and the person are different things in law.** The order stays for years under contract and tax law; the profile goes when the person asks, so the transaction must outlive the person.
> * **Most rules are data requirements with a date.** Each belongs in a system of record, with a test and a calendar row that names an owner.

<br>
The checkout that accepts a real purchase can also receive automated payment attacks. The address used for delivery can remain in a forgotten export, and a pricing rule can require data the shop has never collected.

![A shop front with three intact doors labeled Payment form, Login and Admin, with a small robot walking in through them as built.](assets/images/part-8-intro/part-8-three-public-forms.jpeg)
**Figure 1:** *The attacker's way in: a payment form, a login and an admin, none of which has to be broken to be abused.*

Kestrel & Pine, the fictional outdoor brand, met all three: **48,000 abusive checkout attempts** with stolen cards one August 2026 night; a customer's May 2027 request to delete her data; and four rules that reached engineering through unrelated channels, such as listings a marketplace rejected.

**Where we are in the order's journey.** Eva's jacket, the order this book follows, meets all three: security at its checkout and payment, privacy in every system her name reaches, and regulation at its price, product page, invoice and return.

![Diagram: Where Part VIII meets Eva's jacket](assets/images/part-8-intro/fig02-where-part-viii-meets-eva-s.jpeg)
**Figure 2:** *Where Part VIII meets Eva's jacket: security at the checkout and the payment, privacy in every system her name reaches and in the request that one day asks for it back, regulation at the price, the order button, the product page and the refund clocks.*

Part VII found that a merchant renting its platform keeps or breaks its promises in the layer it owns around the platform. Part VIII adds demands made on that layer by attackers, people with rights over their data and rules with a date. The vendor covers its own service, checkout and defaults, not the accounts, keys and scripts the merchant adds.

The response to these demands begins with the earlier parts' map of systems, integrations and owners. Each chapter adds a column: credentials with their owners; personal data with who decides its use, its purpose and retention; and requirements with their system, deadline and owner. The map makes responsibilities actionable; each topic still needs its own controls.

![Diagram: Three things reach a shop from outside, a script, a person with rights and a rule with a date, and each is answered by a list with owners](assets/images/part-8-intro/fig01-three-things-reach-shop-outside-script.jpeg)
**Figure 3:** *Three things reach a shop from outside, an attacker's script, a person with rights and a rule with a date, and each is answered by a list with owners; the three lists are columns of the same ownership map, not a separate discipline.*

## Chapters in this part

[[commerce-security]] examines **card testing, account takeover, checkout scripts and integration credentials**. The August attack cost €2,900 in declined-payment fees and interrupted sales. It assigns controls to the merchant and provider and sets out incident recovery.

[[privacy-and-customer-data]] then maps **customer records, their purposes and the actions required by a request**. The May requester, in Ghent, appears in nine systems. Her orders stay for years under tax law but her profile goes on request, so the chapter separates the person from the transaction. Linked records and a coordinated workflow make later requests easier to complete and verify.

Last, [[commerce-regulation]] turns **an applicable rule into owned implementation work**. It names scope, required data or behavior, authoritative system, verification and deadline. Its worked calendar covers product information, accessibility, electronic invoicing and unsold goods.

## Where to Begin

The opening's checkout takes a stolen card as it takes a real purchase. Each demand is answered by a list the merchant keeps, not by the vendor. The other lists rely on the first, the owners of identities and keys. Begin with [[commerce-security]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
