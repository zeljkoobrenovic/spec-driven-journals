---
title: "Glossary: The Language of Stays Marketplaces"
date: 2026-10-21
author: Željko Obrenović
excerpt: "Plain-language definitions of the book's marketplace, supply, inventory, discovery, booking, money, trust, platform and leadership terms, grouped by part, with Corvane's fictional names in their own section, an alphabetical index and a link from every term to the chapter that owns it."
permalink: glossary
timetoread: {{TTR}} min read
---

> **IN THIS SECTION, YOU WILL:** Find the book's vocabulary in one place: read a plain-language definition grouped with the other terms of the same part, see where a term means something different on the hotel side and the homes side, follow the link to the chapter that owns it, or look a term or abbreviation up in the alphabetical index at the end.

> **KEY POINTS:**
>
> * **Look a term up, then read its neighbors.** Each section collects one part's terms, so the rows around a term carry the contrasts that cause real design errors: property versus unit versus listing, inventory versus availability, rate plan versus audience, offer versus reservation, agency versus merchant versus merchant of record, gross versus stayed reservations, a trust decision versus its enforcement.
> * **One term, one meaning, one owning chapter.** Every row links to the chapter that owns or best explains the term, and the chapters are written to follow these definitions. Where the accommodation marketplace and the hosted-stays marketplace use a word differently, the row says so; when a chapter and this page disagree, one of them needs correcting.
> * **Regulatory, standards and company terms date quickly.** Regulations, standards, product names and their status are given as of 2026, following the sources cited in the chapters. Check the current source before a definition here goes into a contract, a partner agreement, a policy or a design decision.

> **[FAILURE PATTERNS THIS SECTION ADDRESSES](where-stay-platforms-go-wrong.html):**
>
> * **The Hotel-Shaped Home** — the same failure at the level of words: when "unit", "listing", "rate plan" and "availability" mean one thing on the hotel side and another on the homes side, one model gets forced onto both; naming the difference is the first defense.
> * **Price Drift** — when "price", "total", "fee" and "tax" are composed in different places, the numbers disagree because the words did first; one definition of the offer and the total display is where the repair starts.

<br>

## How to Use This Glossary

The sections follow the book's structure. The first collects the **evidence labels** every chapter uses and the **sixteen failure patterns**; the next nine follow **Parts I to IX**, from the business of a night's stay through supply, inventory, discovery, booking, money, trust and the platform underneath to the Chief Architect's leadership agenda; the last collects **Corvane's fictional names**. Part X's case studies apply these terms rather than adding new ones; the few generic terms they introduce sit with Part IX. The **alphabetical index** at the end lists every term and abbreviation with a link to the section that defines it.

Each section opens with the chapters that own its terms, then a `| Term | Definition | Chapter |` table. The definitions are short teaching descriptions in plain language, not legal text, standards or vendor documentation; the chapter in the last column gives the full treatment, the sources and the worked example. Rows that combine two or more terms with a slash define all of them, because the difference between them is the point. Where a term behaves differently on the **accommodation marketplace** (properties, partners, room types and rate plans) and the **hosted-stays marketplace** (homes, hosts and one calendar per unit), the definition says how. Corvane, named in a few rows and in the last section, is the fictional travel group this book follows ([[meet-corvane]]); its names and numbers are illustrations, not facts about any real company.

## <a id="g-reading"></a>Reading the Book: Evidence Labels and Failure Patterns

The book marks every statement as one of five kinds, and it names sixteen recurring ways stay platforms fail. [[introduction]] explains the labels; [[where-stay-platforms-go-wrong]] tells each failure pattern in full, with its warning signs, mechanism, cost, the marketplace type it hits hardest and the chapters that address it. The last column below names the guide and the chapter that does most of the repair work.

| Term | Definition | Chapter |
| --- | --- | --- |
{{reading}}

## <a id="g-marketplace"></a>Part I — Marketplace

The business vocabulary: which kind of accommodation marketplace this is, how it makes money and how it is decomposed. [[two-stay-marketplaces]] owns the marketplace types, intermediaries and money roles; [[stays-marketplace-economics]] owns take rate, look-to-book and liquidity; [[stays-capability-map]] and [[stays-bounded-contexts]] own the two decompositions and the offer and reservation as aggregates.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-1}}

## <a id="g-supply"></a>Part II — Supply

Properties, homes and the partners behind them. [[property-and-listing-model]] owns property, room type, unit and listing; [[partner-onboarding]] owns activation and verification; [[content-and-media]] owns mapping and content quality; [[connectivity-and-channel-managers]] and [[calendar-sync]] own the two integration models; [[extranets-and-host-tools]] owns the partner and host workspace.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-2}}

## <a id="g-inventory"></a>Part III — Inventory

Availability, rates and price. [[rates-and-availability-model]] owns the ARI vocabulary; [[availability-engine]] owns offer computation, caches and price accuracy; [[inventory-integrity]] owns how a night is held, committed and, when it fails, oversold; [[dynamic-pricing]] owns revenue management and host pricing; [[promotions-and-loyalty]] owns discounts, audiences and parity.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-3}}

## <a id="g-discovery"></a>Part IV — Discovery

From intent to a bookable stay. [[stays-search-architecture]] owns availability-aware search; [[destinations-and-maps]] owns places and geography; [[stays-ranking]] owns ranking and its transparency; [[personalization-and-recommendations]] owns intent, wishlists and alerts; [[property-page-and-room-selection]] owns the total price shown and the choice of room and rate.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-4}}

## <a id="g-booking"></a>Part V — Booking

Making and keeping the reservation. [[checkout-orchestration]] owns the booking saga and the two booking modes; [[reservation-lifecycle]] owns reservation states and delivery; [[changes-and-cancellations]] owns cancellation policy and disruption; [[trip-and-messaging]] owns the trip and the conversation; [[customer-service]] owns cases and recovery.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-5}}

## <a id="g-money"></a>Part VI — Money

Who pays whom, when and how much. [[merchant-and-agency-models]] owns the money roles; [[stay-payments]] owns charging the guest; [[payouts-and-settlement]] owns paying partners and hosts; [[taxes-on-stays]] owns VAT, tourist taxes and platform reporting; [[refunds-and-reconciliation]] owns refunds and proving that the money agrees.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-6}}

## <a id="g-trust"></a>Part VII — Trust

Making strangers safe to stay with. [[stays-trust-and-safety]] owns trust decisions and enforcement; [[travel-fraud]] owns fraud and account takeover; [[identity-accounts-and-access]] owns identity levels and partner roles; [[reviews-and-reputation]] owns reviews and quality programs; [[protection-and-incidents]] owns screening, protection and incidents; [[stays-regulation]] owns short-term-rental and platform regulation.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-7}}

## <a id="g-platform"></a>Part VIII — Platform

The distributed system underneath. [[event-driven-stays]] owns reservation events and ARI streams; [[global-scale-and-reliability]] owns journey objectives, degradation and cost; [[marketplace-intelligence]] owns governed metrics and partner insight; [[stays-experimentation]] owns delayed outcomes and interference; [[stays-ml-platform]] owns the ML platform and model governance; [[demand-channels]] owns metasearch and partner distribution.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-8}}

## <a id="g-leadership"></a>Part IX — Leadership

The Chief Architect's agenda. [[converging-two-marketplaces]] owns the convergence decision; [[organizing-stays-engineering]] owns team topology and governance; [[modernizing-a-live-marketplace]] owns migration of a live reservation book; [[ai-in-travel-stays]] owns agentic booking and AI governance; [[evolving-the-platform]] owns stressor analysis and fitness functions. The last rows come from the Part X case studies.

| Term | Definition | Chapter |
| --- | --- | --- |
{{part-9}}

## <a id="g-corvane"></a>Corvane Names (Fictional)

**Corvane is fictional, and so is every name below.** No row describes a real company's system or program; the names recur across chapters, so they are collected here. [[meet-corvane]] introduces the group, its brands, cast and systems, and the canonical facts behind them come from the book's scenario ledger.

| Term | Definition | Chapter |
| --- | --- | --- |
{{corvane}}

## <a id="g-index"></a>Alphabetical Index

{{index}}

<br>

The templates that turn many of these terms into working documents (the two-marketplace capability map, the ARI model card, the connectivity partner contract, the booking saga card, the reservation state table, the cancellation policy card, the funds-flow diagram, the tax jurisdiction card, the STR compliance card, the journey SLO card) are collected in [[toolkit]]; the mapping from the Productscape domain models to the chapters is in [[domain-coverage]]; and the sources behind the definitions, with their evidence type and publication date, are listed by topic and chapter in [[bibliography]].
