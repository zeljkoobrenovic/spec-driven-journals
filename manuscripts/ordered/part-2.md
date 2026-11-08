{class: part, id: part-2}
# Part II — CATALOG: Products, Prices and Promises

![Part II — CATALOG: Products, Prices and Promises — logo](commerce-platform-architecture/posts/part-2-intro/assets/images/part-2-intro/logo.jpeg)

> **KEY POINTS:**
>
> * **Catalog facts have different owners and different clocks.** Content tolerates a day's lag, prices carry legal weight, discounts are decided in the cart and stock changes by the second.
> * **Every channel shows a copy, and a copy needs a source and a reconciliation.** The €179 German price and the marketplace selling an empty shelf were copies nobody compared with their source.
> * **A promise is computed once, in one place, and then frozen.** The price is copied to the invoice, the discount allocated to every line, and the last unit committed to exactly one order.

A shopper reads a jacket's description, price and stock badge on the same page. The description may stay unchanged for a season; the last sellable unit can disappear while the page is open. Updating both on the same schedule can leave the page accurate about the product but wrong about whether it can be bought. This part explains how product facts, prices, discounts, availability and search reach the shopper with the timing each needs.

This part explains those responsibilities through **Kestrel & Pine, a fictional outdoor brand** whose product and pricing copies diverged across systems. Each chapter starts with the business cost of one such disagreement.

![A product page whose description, price, discount and stock indicator connect to a season calendar, a daily calendar, a cart and a stopwatch.](commerce-platform-architecture/posts/part-2-intro/assets/images/part-2-intro/part-2-four-facts-four-clocks.jpeg)

**Figure 1:** *Four facts that sit side by side on one product page run on four different clocks, which is why each needs its own owner and its own path to every channel.*

**Where we are in the order's journey.** Before Eva orders on 13 April 2027, the Ridgewalker women's M in moss needs a description, image and identifiers. Search must find it, pricing must select €199, and availability must confirm a unit can be sold. Her €235 basket also qualifies for free shipping. [Follow the Order: What Happens Between “Buy” and “Delivered”](#journey-of-an-order) provides the wider route.

![Diagram: The shape Part II recommends](commerce-platform-architecture/posts/part-2-intro/assets/images/part-2-intro/fig01-shape-part-ii-recommends-four-kinds.jpeg)

**Figure 2:** *The shape Part II recommends: four kinds of catalog fact with four owners and four clocks, a search index that is openly a copy of all of them, every channel a consumer, and a reconciliation that compares each copy to its source on a schedule.*

{id: part-2--chapters-in-this-part}
## Chapters in this part

[What Are We Selling? Products, Variants and the Catalog](#product-information) explains **which system owns product content and identifiers**. A season entered four times motivates a **product information management system (PIM)**. The chapter distinguishes the product, its sellable variants, internal stock codes and global barcode identifiers.

[What Does It Cost? Price Lists, Contract Prices, Currencies and Tax](#pricing-architecture) establishes **who selects a price and how channels receive it**. A failed update left the German storefront at €179 for nine days instead of €199, losing about €8,200. Ownership, dated prices and comparisons address the failure.

[Discounts, Coupons and Loyalty: Promotions Without Chaos](#commerce-promotions) explains **how offers combine and how discounts reach invoices and refunds**. A Black Friday setting let two discounts combine on 2,860 orders, costing about €52,000. The chapter separates promotional rules from gift-card and loyalty balances.

[Finding the Product: Search, Navigation and Merchandising](#commerce-search-and-discovery) treats **the search index as a maintained copy** of product, price, stock and review data. Missing attributes and synonyms make a waterproof jacket hard to find; correcting them improves the fictional search results without replacing the engine.

[Is It in Stock? Inventory, Availability and the Promise You Can Keep](#inventory-and-availability) distinguishes **physical stock from what a channel may still sell**. The Black Friday oversell of 1,340 jackets shows the cost of delayed copies. The remedy assigns owners to stock and commitments, then calculates availability from both.

Begin with [What Are We Selling? Products, Variants and the Catalog](#product-information).

{id: part-2--sources-and-evidence}
## Sources and Evidence

Sources are cited in each chapter; this introduction makes no factual claim of its own. Kestrel & Pine is fictional, and its figures are the same in every chapter.
