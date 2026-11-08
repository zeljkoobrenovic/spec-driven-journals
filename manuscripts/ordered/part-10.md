{class: part, id: part-10}
# Part X — EVOLUTION: Decisions That Change With Scale

![Part X — EVOLUTION: Decisions That Change With Scale — logo](commerce-platform-architecture/posts/part-10-intro/assets/images/part-10-intro/logo.jpeg)

> **KEY POINTS:**
>
> * **At a growing merchant the problems live in the joins.** Build what customers choose you for, buy what every merchant needs, own the joins, and price every option over three years.
> * **A stage is a shape, and a migration crosses between stages one seam at a time.** Old and new run side by side, with the old owner kept operable through one peak.
> * **Ownership is what makes any of it hold.** A named owner for every system, integration and app, one writer per fact, and AI agents treated as integrations with no write scope on stock, prices or orders.

A merchant adds a store, wholesale channel, marketplace, warehouse or second brand. Its existing systems still run, but they may now need to share stock or coordinate orders in ways their original design never required. Leaving those assumptions unchanged can create overselling and manual work; replacing everything can exceed the team's capacity. This part examines how to choose and sequence the changes that address the new demands.

![A four-step staircase of business growth with euro coins falling at each step edge.](commerce-platform-architecture/posts/part-10-intro/assets/images/part-10-intro/part-10-growth-in-jumps.jpeg)

**Figure 1:** *A merchant grows in jumps, not smoothly: each jump adds a place where stock sits or a channel where it sells, and the money is lost at the jumps rather than between them.*

At Kestrel & Pine, the fictional outdoor brand, a jacket order crosses systems introduced between 2016 and 2025. Their purchase dates explain today's responsibilities and gaps. A new decision must account for that history, the team available to operate it and the customers who still need orders fulfilled during change.

The company faces five questions in 2027: whether to rebuild, how to introduce new order and product systems, which growth stage to design for, who owns the integrations, and whether to add shopping agents. Each requires an explicit choice about ownership, timing and capacity. The chapters use **Waypoint**, Kestrel & Pine's improvement program, to make those choices concrete.

![Diagram: The five decisions of Part X as one loop](commerce-platform-architecture/posts/part-10-intro/assets/images/part-10-intro/fig01-five-decisions-part-x-one-loop.jpeg)

**Figure 2:** *The five decisions of Part X as one loop: a change of shape is read as a stage, answered by a platform review, carried out as a migration, held in place by an ownership map, and extended to the newest writer, until the shape changes again.*

![Diagram: Kestrel & Pine's 2027 as this part sees it](commerce-platform-architecture/posts/part-10-intro/assets/images/part-10-intro/fig02-kestrel-pine-s-2027-this-part.jpeg)

**Figure 3:** *Kestrel & Pine's 2027 as this part sees it: the decisions are made in the first quarter, carried out seam by seam from July, frozen around the peak, and dated for review rather than treated as final.*

{id: part-10--chapters-in-this-part}
## Chapters in this part

[Build, Buy or Assemble: Choosing and Changing Platforms](#build-buy-or-assemble) compares **bundled products, separate services and custom software by their full cost**. The platform review includes people, integration, migration and exit over three years. It leads to keeping the platform and adding missing capabilities, with a 2029 review.

[Moving Without Burning the Bridge: Replatforming and Migration](#replatforming-and-migration) plans **limited transitions with comparison and recovery at every step**. Product publication moves gradually in 2027. Order channels move on separate dates, with a freeze around Black Friday so migration and peak risk do not compound.

[What Changes at Each Scale: From First Store to Group](#commerce-scaling-stages) identifies **the business changes that invalidate an earlier design**. Channels, stock locations and brands matter alongside revenue. The stage map separates current coordination problems from possible future group-wide needs.

[Who Builds and Who Owns: Teams, Vendors, Agencies and Governance](#organizing-commerce-engineering) assigns **business and technical responsibility for systems, integrations and apps**. The January inventory finds thirteen of 34 integrations unowned. The chapter addresses supplier contracts, internal ownership and practices a small team can maintain.

[Assistants and Agents: AI in Commerce and What Is Real in 2026](#ai-and-agentic-commerce) compares **AI that recommends an action with AI authorized to perform it**. Both need reliable product and stock answers; actions also need permissions and accountability. A dated review of emerging protocols leads to improving the merchant's data and interfaces before building a shopping agent.

Begin with [Build, Buy or Assemble: Choosing and Changing Platforms](#build-buy-or-assemble).

{id: part-10--sources-and-evidence}
## Sources and Evidence

Every public claim in this part is sourced and dated in the chapter that makes it, under that chapter's Sources and Evidence. Kestrel & Pine is fictional; recommendations and labeled assumptions are the author's judgement.
