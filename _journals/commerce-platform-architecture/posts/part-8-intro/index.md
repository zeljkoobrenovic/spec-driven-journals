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
Every part so far has asked how a shop works when everyone means well. **This part asks what happens when someone does not, and what the law requires regardless.** A shop is three public forms: a payment form that takes money from anyone with a valid card number, a login that lets anyone with the right password act as a customer, and an admin that lets them act as the merchant. None of it has to be broken to be abused. The same shop holds a name, an address and a purchase history in a dozen systems from a dozen vendors, each copy made for a reason and each reason with its own rule for how long it may stay. And much of what the shop must show, record and refund is written in the Official Journal of the European Union, with a date.

![A shop front with three intact doors labeled Payment form, Login and Admin, with a small robot walking in through them as built.](assets/images/part-8-intro/part-8-three-public-forms.jpeg)
**Figure 1:** *A shop is three public forms, a payment form, a login and an admin, and none of them has to be broken to be abused.*

Part VIII sits at the checkout and payment steps of the order's journey, then alongside every step after them. Eva Janssen's jacket, the order this book follows, met the law four times without anyone noticing: the price she saw had to include VAT and sit in a price history that any later reduction is measured against, the checkout button carried prescribed words ("order with obligation to pay" or an equivalent), the product page carried a manufacturer's address, and her exchange request on 19 April 2027 started two 14-day clocks, one for sending the goods back and one for any refund. Her name went to the platform, the warehouse system, the carrier, the payment provider and the ERP (the enterprise resource planning system that keeps the books and issues invoices), each under its own retention rule. And the 48,000 requests that hit the same checkout one night in August 2026 looked like hers to every system except the one that counted them.

Kestrel & Pine, the fictional outdoor brand this book follows, learned the three lessons of this part one incident at a time: the Card-Testing Night of 18–19 August 2026, the Request From Ghent in May 2027, and four rules that arrived through a marketplace's error log, an agency audit, a customer's refused PDF and an auditor's newsletter. **The claim of this part is that the three have one remedy: the ownership map built from Part I's system-of-record map and Part VI's integration inventory, one row per system, integration and app with its owner, gains three more columns.** Who holds the key to each integration. Which legal role and retention clock each system has. Which rule lands in which system of record, by when, and whose name is on the row.

![Diagram: Three things reach a shop from outside, a script, a person with rights and a rule with a date, and each is answered by a list with owners](assets/images/part-8-intro/fig01-three-things-reach-shop-outside-script.jpeg)
**Figure 2:** *Three things reach a shop from outside, a script, a person with rights and a rule with a date, and each is answered by a list with owners; the three lists are columns of the same ownership map, not a separate discipline.*

![Diagram: Where Part VIII meets Eva's jacket](assets/images/part-8-intro/fig02-where-part-viii-meets-eva-s.jpeg)
**Figure 3:** *Where Part VIII meets Eva's jacket: security at the checkout and the payment, regulation at the price, the button, the product page and the clocks, privacy in every system her name reaches and in the request that one day asks for it back.*

## Chapters in this part

[[commerce-security]] decides **what attackers want from a shop and which controls matter most**: keep the card number out of your systems with a hosted checkout or hosted fields (card boxes served by the payment provider inside your page), challenge and rate-limit every endpoint that can trigger a payment or a login, own every script on the checkout page, and give every person, app and integration its own identity and restricted key. The case is the Card-Testing Night: 48,000 attempts in one night, about 260 live cards and 21 disputes; then the April 2027 baseline, with a decline-rate alert at three times the 30-day median, a kill switch, multi-factor authentication (MFA) enforced and no shared accounts, one key per integration in a vault, a script inventory and three runbooks.

[[privacy-and-customer-data]] decides **where personal data lives, under which rules, and how to design consent, retention and deletion**: every integration is a data flow with a legal role, consent is recorded on the customer master with its evidence, and a deletion request is a fan-out with a one-month deadline that needs an identity index, an orchestrator and a decided action per system, erase, pseudonymize, retain or refer. The case is the Request From Ghent of Monday 10 May 2027: a customer found in nine of the thirteen systems and seventeen working days before the reply on 4 June; from October 2027 an orchestrator on the integration platform, and a second request answered in two working days.

[[commerce-regulation]] decides **which laws change what a platform must do, by when, and how to read them as requirements**: scope first, then the field, history, document or clock the article demands, the system of record that owns it, the channels that show it, a test in the release process and a calendar row with an owner. The case is four rules through four doors, product-safety listing fields rejected by a marketplace in December 2024, an accessibility audit of May 2025 with about 140 findings, Belgian e-invoicing through a refused PDF in December 2025 and the ban on destroying unsold apparel from 19 July 2026, and then the regulatory calendar Noor Visser and Sanne de Wit write in March 2027, where most rows are maintenance, the owners are mostly not engineers, and the few projects land in systems Waypoint builds anyway.

Begin with [[commerce-security]].

## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
