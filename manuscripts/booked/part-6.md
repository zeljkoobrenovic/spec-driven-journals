{class: part, id: part-6}
# Part VI — MONEY: Who Pays Whom, When and How Much

![Part VI — MONEY: Who Pays Whom, When and How Much — logo](stays-marketplace-architecture/posts/part-6-intro/assets/images/part-6-intro/logo.jpeg)

> **IN THIS PART, YOU WILL:** Design the money side of both marketplaces: merchant, agency and facilitated payment models, payments for nights weeks or months away, payouts and commission settlement, taxes on stays and platform reporting, and the refunds, chargebacks and reconciliation that close the books.

> **WHY THE BUSINESS CARES:** The payment model decides revenue recognition, licensing, chargeback exposure and cash. An unexplained payout, tax collection or quarter-end gap costs trust, fines and audit findings.

> **WHY ARCHITECTS SHOULD CARE:** Money in stays moves over time and in several directions at once: collected now or later, held for months, paid to hotels by card and to hosts by transfer, owed to cities, and returned when plans change.

> **KEY POINTS:**
>
> * **Decide the money facts once per booking and freeze them.** A payment arrangement record says who collects, when, how the supplier is settled and which way commission flows. A versioned payment plan schedules charges, holds, cards and refunds. A tax determination says who is liable and who remits. Every other system reads these records and never re-derives them.
> * **One ledger says who is owed what, and everything else is a report on it.** Bookings, changes, check-ins, fees, taxes, refunds and recoveries post to the same double-entry ledger. Payouts pay only what it shows as available, and statements, invoices and tax reports are queries over it.
> * **Reconcile against the reservation, not only the bank.** A ledger can balance and match every bank statement while being wrong about the world. The third leg is the reservation and its arrangement version, and every refund records its payee and its funder separately.

> **[FAILURE PATTERNS THIS PART ADDRESSES](#where-stay-platforms-go-wrong):**
>
> * **Ledgerless Money** — Moves receivables, payables, host balances, tax liabilities and refunds into one ledger with typed, approved adjustments.
> * **The Tax Patchwork** — Replaces tourist-tax constants and finance spreadsheets with a tax engine, effective-dated rules and reporting built from the ledger.
> * **Policy Spaghetti** — Stops checkout, invoicing, issuing, scheduling and support from each inferring the payment model, charge date or refund funder.

Part V kept the reservation true from checkout to check-out. Part VI follows **the money attached to it**, which takes a different path and a longer time. A guest may pay in February for August, the marketplace may hold the money for months, the property may charge a virtual card at its own terminal.

The argument of this part is that **money is a set of decisions that must be recorded before it moves**: who collects, when, who is owed, who is liable for the tax, who funds the refund. Left in code branches, they are made again by each system and drift apart. When they live in versioned records and one ledger, a new payment option, payout rail or tax regime becomes configuration.

![A booking folder with five stamped decision tags, after which a cart of coins rolls through a gate into one ledger book.](stays-marketplace-architecture/posts/part-6-intro/assets/images/part-6-intro/6-decisions-before-money-moves.jpeg)

**Figure 1:** *Money in a stays marketplace is a set of decisions recorded before it moves: who collects, when, who is owed, who owes the tax and who funds a refund.*

Hotels and homes differ here more sharply than anywhere outside supply. An online travel agency (OTA) runs **agency** bookings, where the hotel collects at the desk and the marketplace must invoice and chase its commission, beside **merchant** bookings settled by single-use virtual cards. The risk sits in collection, and the hotel's controller needs value-added tax (VAT) documents and a monthly statement. A hosted-stays marketplace **facilitates**: it collects everything, holds it, and pays individuals 48 hours after check-in, before chargeback windows close. The risk sits in release rules, tax-identity gates and recoveries from hosts already paid. Corvane shares the arrangement contract, the payment orchestration, the Fathom ledger, the tax engine and reconciliation. Rails, release policies, statements and recoveries stay per marketplace.

![Guest payment and the payment arrangement feed Corvane Payments, which posts to the Fathom ledger along with the tax engine; the ledger pays hotels, hosts and cities, and reconciliation checks it.](stays-marketplace-architecture/posts/part-6-intro/assets/images/part-6-intro/6-money-at-corvane.jpeg)

**Figure 2:** *Money at Corvane: the arrangement and the payment plan decide how the guest pays, every movement posts to one ledger, the supply side and the tax authorities are paid from it, and reconciliation checks it against the reservation as well as the bank.*

{id: part-6--chapters-in-this-part}
## Chapters in this part

[Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models) decides **who stands in the money flow for each booking**. One payment arrangement record, resolved on the offer and frozen on the reservation, replaces seven places in Roomstead that each decided agency or merchant. Growth toward Corvane's 40% merchant target pauses at 35% until it exists.

[Paying for a Future Night: Payment Orchestration for Stays](#stay-payments) decides **how money for a future night is collected**: a versioned payment plan, deferred charges that survive Strong Customer Authentication (SCA), virtual cards for hotels and one orchestration layer that runs them all. Nookaway's Pay Later charges for Semana Santa 2027, with about €228 million promised to hosts and not yet collected, are the case.

[Paying the Supply Side: Payouts, Commissions and Settlement](#payouts-and-settlement) decides **who is owed what and when it is paid**. The settlement ledger, not the payout engine, holds partner balances, with explicit release rules and holds, a beneficiary graph for co-hosts and managers, and commission invoicing. Carmen Ruiz's €244.40 payout is the case.

[The Tax Patchwork: VAT, Tourist Taxes and Platform Reporting](#taxes-on-stays) decides **which part of the guest's money belongs to a city or a state**. Levy, the group tax engine, answers jurisdiction, amount, liability and collector at quote time, freezes the answer and posts tax liabilities to the ledger. ViDA (VAT in the Digital Age) is the forcing date. The Novaks' €56 Lisbon tourist tax is the case.

[Closing the Books: Refunds, Chargebacks and Reconciliation](#refunds-and-reconciliation) decides **how money moving backwards is funded and proven**: refunds with a payee and a funder, typed finance adjustments, and Plumbline, the reconciliation service that compares the ledger, the bank and the reservation. The €1.8 million gap between virtual-card statements and Roomstead merchant reservations is the case.

Begin with [Who Takes the Money? Merchant, Agency and Facilitator Models](#merchant-and-agency-models).
