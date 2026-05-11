---
layout: post
title: "What Digital Marketplaces Sell? A Short Memo"
date:   2021-10-21 21:12:01 +0100
categories: architecture
author: by Željko Obrenović (obren.io)
permalink: digital-marketplaces
icon: assets/icons/market.png
timetoread: 15 min
excerpt: Digital marketplaces facilitate transactions between buyers and sellers. The marketplace is not the seller (nor a buyer), but it sells a reduction in transaction costs. .
---
![](assets/images/markets/floating-market.jpg)

> **KEY POINTS:**
> * When referring to digital marketplaces, we refer to the entities facilitating transactions between buyers and sellers. The marketplace is not the seller (nor a buyer). 
> * Marketplaces sell a reduction in transaction costs. 
> * There are three types of transaction costs: Search and Information Costs; Bargaining and Negotiation Costs; and Policing and Enforcement Costs.

## Basic Terminology

What do we mean when we use the term digital marketplace? What do we not mean when we use this word? Here I summarize some of the answers to this question from an excellent essay [History of Online Marketplaces](https://web.stanford.edu/class/msande238/projects/2014/Marketplaces.docx) by Andrew Adams and Lance Martin.

When referring to digital marketplaces, we refer to the entities ***facilitating transactions between buyers and sellers***. Marketplaces act as a third party to the principal transaction at hand. The marketplace is not the seller (nor a buyer), and as such, it does not own the inventory or services transacted on the platform. The entities that own the inventory or services would be ***traditional retailers*** rather than ***marketplaces***.

Accordingly, it would be incorrect to state that recognized digital marketplaces like **Uber**, **Etsy**, and **Airbnb** sell transportation, handcrafted goods, or lodging. Instead, they ***facilitate transactions*** between drivers and riders, artisans and buyers, hosts and lodgers. 

## What Online Marketplaces Actually Sell?

Many marketplaces are very profitable. So how do marketplaces earn money by facilitating transactions? What do they sell? ***Marketplaces sell a reduction in transaction costs.*** 

Costs relate to effort, time and other resources needed to prosecute a transaction. The marketplace expert [Ramesh Johari](https://profiles.stanford.edu/ramesh-johari) defines three types of these transaction costs:

* **Search and Information Costs**: Search cost captures the cost of buyers and sellers finding each other. Information cost concerns finding information relevant to either party in making an informed decision about whether they should execute the transaction.
* **Bargaining and Negotiation Costs**: Bargaining and Negotiation costs are the cost of determining what exactly is being sold, for what price, and under which conditions and guarantees.
* **Policing and Enforcement Costs**: Policing and Enforcement Costs are the costs of ensuring transactions are prosecuted fairly, favorably for both parties, and according to agreed conditions.

![](assets/images/markets/costs.png)
  <br>
**Figure 1:** *Marketplaces sell a reduction in transaction costs: Search and Information Costs, Bargaining and Negotiation Costs, Policing and Enforcement Costs.*

## Few Examples
 
A marketplace need not mitigate costs from all three dimensions. But it is difficult to imagine a marketplace that does not reduce costs along at least one dimension. 

For example, ***[Craigslist](https://en.wikipedia.org/wiki/Craigslist)*** (the web’s original marketplace) mitigates ***Search, and Information Costs*** by serving as a central repository for buyers and sellers to connect. Craigslist, however, does not reduce costs along the other two dimensions, as they provide no infrastructure to minimize bargaining and negotiation costs or policing and enforcement costs. 

Another example is ***Uber***, a mobile transportation marketplace that reduces ***Search and Information Costs*** by automatically making matches between riders on the demand side and drivers on the supply side. It further automatically sets fares bringing ***Bargaining and Negotiation Costs*** practically to zero. Uber also provides significant liability insurance to drivers and reimbursements to riders if drivers take inefficient routes (both of these measures minimize ***Policing and Enforcement Costs***).


## Monetizing Online Marketplaces

With the value of marketplaces defined as “*reduction in transaction costs*,” it is also more apparent how marketplaces can monetize their usage. 

In essence, they aim at creating a ***win-win proposition***, e.g., paid subscriptions, where people are ready to pay to get an additional reduction in their transactions costs. For example, a seller may want to pay extra so that buyers can find them more quickly, reducing their Search and Information Costs compared to other means. Sellers and buyers can opt for paid subscriptions to get better customer support, reducing their costs and risks of Policing and Enforcement. 

Marketplaces can also offer extra paid services, such as price recommenders or sanity checkers, reducing Bargaining and Negotiation costs.

---begin mermaid---
gantt
    title A Gantt Diagram
    dateFormat YYYY-MM-DD
    section Section
        A task          :a1, 2014-01-01, 30d
        Another task    :after a1, 20d
    section Another
        Task in Another :2014-01-12, 12d
        another task    :24d
---end mermaid---
**Figure 1:** *Example mermaid graph.*

---begin mermaid---
mindmap
  root((mindmap))
    Origins
      Long history
      ::icon(fa fa-book)
      Popularisation
        British popular psychology author Tony Buzan
    Research
      On effectiveness<br/>and features
      On Automatic creation
        Uses
            Creative techniques
            Strategic planning
            Argument mapping
    Tools
      Pen and paper
      Mermaid

---end mermaid---
**Figure 1:** *Example mermaid graph.*

---begin force-graph---

nodes:
  A: 10
  B: 4

links:
    A --> B
    A --> C
    B --> D
    C Test --> [D]
    B --> E
    B --> F
    E --> F
    D --> A

---end force-graph---
**Figure 1:** *Example mermaid graph.*


---begin buble-chart---

nodes:
  A: 10
  B: 4
  C: 4
  D: 4
  E: 23

---end bubble-chart---
**Figure 1:** *Example mermaid graph.*

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQgtCZ3eAHcLUedxpOAtu5mXV1cbpUrhzSHQqwn8hf4_OJQiRXFs44vNMO1At3leGdEBsy1epqtANxd/pubembed?start=false&loop=false&delayms=3000" frameborder="0" width="800" height="486" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>

## To Probe Further

* [History of Online Marketplaces](https://web.stanford.edu/class/msande238/projects/2014/Marketplaces.docx), 2014, by Andrew Adams and Lance Martin
* [Marketplace](https://en.wikipedia.org/wiki/Marketplace), 2021, Wikipedia
* [A History of Shopping, Marketplaces, and Experiences](https://www.starkenterprises.com/a-history-of-shopping-marketplaces-and-experiences/), 2021, by Ezra Stark
* [Ezra Stark](https://www.sutherlandlabs.com/blog/history-repeating-how-digital-marketplaces-conquered-retail/), 2018, sutherlandlabs.com
* [Search, Matching, and the Role of Digital Marketplace Design in Enabling Trade: Evidence from Airbnb](https://ide.mit.edu/sites/default/files/publications/SearchMatchingEfficiency.pdf), 2017, by Andrey Fradkin
* [Digital Marketplaces](https://andreyfradkin.com/assets/econ_of_digital.pdf), 2017, by Andrey Fradkin
