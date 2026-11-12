---
title: "Part II — CATALOG: Products, Prices and Promises"
date: 2026-11-07
author: Željko Obrenović
excerpt: "What the shop offers and what it can promise: the product, the price, the discount, the search result and the words “in stock”. Part II argues that these facts look alike but have different owners, different clocks and different legal weight, so each needs its own system of record and its own path to every channel, and that a copy nobody reconciles is a promise nobody can keep."
permalink: part-2
timetoread: 4 min read
icon: "assets/icons/part-2-intro.png"
logo: "assets/images/part-2-intro/logo.jpeg"
---

> **KEY POINTS:**
>
> * **Catalog facts have different owners and different clocks.** Content tolerates a day's lag, prices carry legal weight, discounts are decided in the cart and stock changes by the second.
> * **Every channel shows a copy, and a copy needs a source and a reconciliation.** The €179 German price and the marketplace selling an empty shelf were copies nobody compared with their source.
> * **A promise is computed once, in one place, and then frozen.** The price is copied to the invoice, the discount allocated to every line, and the last unit committed to exactly one order.

<br>
A shopper reads a jacket's description, price and stock badge on one page. The description may stay unchanged for a season; the last sellable unit can disappear while the page is open. Updating both on the same schedule can leave the page accurate about the product but wrong about whether it can be bought.

![A product page whose description, price, discount and stock indicator connect to a season calendar, a daily calendar, a cart and a stopwatch.](assets/images/part-2-intro/part-2-four-facts-four-clocks.jpeg)
**Figure 1:** *Four facts that sit side by side on one product page run on four different clocks, which is why each needs its own owner and its own path to every channel.*

Part I ended on a rule: each fact has one record, and every other value is a copy. Part II applies it to the facts a shopper reads before buying, arguing that product content, price, discount and stock status need four owners, not one catalog, because they do not change together: content changes by the season, a price by the day, a discount with each cart and stock by the second. A channel that can ask the owner at the moment of sale should ask it. A channel that cannot ask shows a copy, and so does search, which owns none of the four facts. A copy is safe to show only if it names its source and is compared with that source on a schedule.

![Diagram: The shape Part II recommends](assets/images/part-2-intro/fig01-shape-part-ii-recommends-four-kinds.jpeg)
**Figure 2:** *The shape Part II recommends: four kinds of catalog fact with four owners and four clocks, a search index (the copy of the catalog that search reads) that is openly a copy of all of them, every channel receiving those facts, and a reconciliation that compares each copy to its source on a schedule.*

The claim has one more part: once an order is placed, the price, the discount and the unit promised to it are fixed on that order, so invoices and refunds read the same values.

**Where we are in the order's journey.** All four facts are needed before "add to cart". Before Eva, whose order [[journey-of-an-order]] followed, orders on 13 April 2027, her jacket, the Ridgewalker women's M in moss, needs a description, image and identifiers. Search must find it, pricing must select €199, availability must confirm a unit can be sold, and the discount rules must find that her €235 basket qualifies for free shipping.

Eva's order needs each of those facts to be right. The part tests its claim on cases in which one of them was wrong, at **Kestrel & Pine, the fictional outdoor brand** that sells her jacket. Each chapter starts with one disagreement between that company's copies.

Part II takes those disagreements as five questions in order, one chapter each: who owns product content and identifiers, who selects a price and how channels receive it, how discounts and other offers combine and reach invoices and refunds, what feeds the search index, and what "in stock" means. The fourth question concerns search; the other four take one fact each. Each chapter uses what earlier ones settled; stock follows search because the search chapter leaves open what its "in stock" means.

## Chapters in this part

[[product-information]] explains **which system owns product content and identifiers**. At Kestrel & Pine four teams entered one season four times and no version was the owner's, which motivates a **product information management system (PIM)**. The chapter distinguishes the product, its sellable variants, internal stock codes and global barcode identifiers.

[[pricing-architecture]] then establishes, per variant, **who selects a price and how channels receive it**. A failed update left the German storefront at €179 for nine days instead of €199, losing about €8,200. Ownership, prices with a start date, and a comparison of each copy with its source address the failure.

[[commerce-promotions]] starts from the selected price and explains **how offers combine and how discounts reach invoices and refunds**. A setting left over from an earlier campaign let two discounts combine on 2,860 Black Friday orders, costing about €52,000, part of it in wrong refunds: nobody owned how offers combine. The chapter separates discounts from gift-card and loyalty balances, which are money the merchant owes.

[[commerce-search-and-discovery]] treats **the search index as a maintained copy** of product, price, stock and review data; the index owns none of it. Missing attributes and synonyms make a waterproof jacket hard to find; correcting them improves Kestrel & Pine's search results without replacing the engine.

[[inventory-and-availability]] comes last and solves a problem the search chapter leaves open: a results page can say "in stock" from an old copy of the stock figure. The chapter distinguishes **physical stock from what a channel may still sell**. The Black Friday oversell of 1,340 jackets shows the cost of delayed copies. The remedy assigns owners to stock and to commitments (units already promised to orders), then calculates availability from both.

## What the Five Answers Add Up To, and Where to Begin

Together, the five answers give the description, the price, the discount and the stock badge on the opening's product page each an owner and a path to every channel. Each copy, the search result that led to the page included, gets a named source and a comparison with it. So when a page or listing is wrong, ask first which fact is wrong and who owns it, and only then for faster synchronization.

With one decision in front of you, start with the chapter for its fact. Otherwise read the five in order, beginning with [[product-information]]: product content changes slowest, and prices, discounts and stock figures are recorded against its identifiers.

## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Kestrel & Pine is fictional, and its figures are the same in every chapter.
