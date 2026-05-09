---
layout: post
title:  "Uber's Payments Platform"
date:   2019-11-19 21:12:01 +0100
categories: finance
icon: uber.png
author: by Željko Obrenović (zeljkoobrenovic.com)
permalink: uber-payments-platform
excerpt: Recently, Uber has announced deeper push into financial services with Uber Money, a new division, including products such as a digital wallet and upgraded debit and credit cards. It is expected that Uber could soon offer a bank account to consumers on its platform. While many of the news articles focus on the business side of Uber move, limited resources are available to understand better the payment technology that Uber is building. I believe that we can learn from looking under the hood of Uber payment technologies, as the Uber approach may be the way how we will make the banks of the future.
---

> **KEY POINTS:**
>
> * Conceptually, the Uber payment platform can be described as a generalized **payment order processing system**, based on the ideas of double-entry bookkeeping.
>   
> * At a deeper level, Uber Payments platform is a collection of **microservices** organized in a **stream-processing architecture**. 
>   
> * The key technology used by Uber Payments is **Apache Kafka** - an open-source stream-processing software platform.
> 
> * Processing in distributed systems at scale comes with several challenges, including **error handling**, **validation**, and  **integration with external systems**. 
>
> * Mentioned technologies: Apache Kafka, Go, Java, NodeJS, Python, Cerberus, Grafana, Elasticsearch, Kabana 

## Intro

Recently, Uber has announced [deeper push into financial services](https://www.cnbc.com/2019/10/28/uber-announces-deeper-push-into-financial-services-with-uber-money.html) with Uber Money, a new division, including products such as a digital wallet and upgraded debit and credit cards. It is expected that Uber could soon offer a bank account to consumers on its platform.

While many of the news articles focus on the business side of Uber move, limited resources are available to understand better the payment technology that Uber is building. I believe that we can learn from looking under the hood of Uber payment technologies, as the Uber approach may be the way how we will make the banks of the future. 

Uber has been, to some extent, open and transparent about the payment technology they are making. Uber engineers shared publicly lessons they had learned on two occasions in the past year, during: 

* the  [Uber Payments Platform Engineering team Meeting](https://eng.uber.com/payments-platform/) at the end of 2018 in San Francisco, and 
* the [MoneyCon’19 conference](https://eng.uber.com/moneycon/), where Uber hosted its first FinTech engineering conference. 

Talks from these two events have been recorded and shared on YouTube. While short, the talks include some in-depth reflection on the challenges of building a reliable payments platform at scale. 

In this article, I summarize key technical insights from mentioned resources. This brief overview only scratches the surface of internals of Uber Payments platforms. Many of the relevant topics, such as security and privacy, are not covered. Nevertheless, I believe that the presented material and referenced resources can provide some insights and ideas about the challenges of building modern payment systems.

**DISCLAIMER:**
* This article is the result of my curiosity. I have not validated any findings with Uber. No Uber persons have been actively involved in the writing of this article.
* All information is solely based on the publicly available sources about Uber Payments: the Uber engineering blog, Uber YouTube videos, and news articles. I recommend watching/reading the sources (see the [The Further Probe](#to-probe-further) section at the end of the article). My analysis summarizes these sources, and consequently, many details are "lost in translation". 
* Things are changing fast, so the information presented here may already be significantly outdated.


## The Payments Platform: General Idea

The focus of this article will be on the idea and some technical details behind the Uber Payments Platform. While the payment functionality has been a part of Uber from the beginning, with the Payments Platform, Uber has created a more powerful, flexible solution for all of its lines of business (LoBs). 

The Payments Platform is the culmination of Uber's development of payment functionality, from initial ad-hoc solutions for each business line, towards a powerfull, fully automated, generic money system  (see the [keynote](https://www.youtube.com/watch?v=rp7_7HcqmKA&feature=emb_logo) by Mathieu Chauvin for more details). Figure 1 illustrates my understanding of what creating a single integrated business-independent money 
system means:

* The payments platform is a centralized entity, serving as a bridge between Uber lines of business 
  (LoBs, e.g. Ride, Eats, Fraight, Rush...), payment service providers (PSPs) and banks. 
* The platform enables a new line of business to, with minimal configuration done in a self-service manner, 
  reuse all payment features, instantly benefits from full power of all payments options.
* Business independent nature of the platform also means that any improvement or additons in payment mechanisms 
  are almost instantly available to all business.
  
The presented model is a powerful idea that, if appropriately implemented, can enable Uber to develop its payment technology and introduce new lines of business with unprecedented speed. 

![](../assets/images/uber_payments/overview.png)
**Figure 1**: *Uber Payment Platform hourglass model: bridge Uber lines of business, payment service providers (PSPs) and banks*
  
## Key Functionality of the Payments Platform

From what I could gather from the Uber presentations (e.g. see [Payments Integration at Uber: A Case Study](https://www.youtube.com/watch?v=yooCE5B0SRA&feature=emb_title), by Gergely Orosz), the Uber Payments Platform aims at supporting a whole palette of payment functionality, including:

* Common payment flows, 
* Additional more Uber specific use cases,
* Error detection, prevention, and recovery, and
* Digital wallet and cash payments.

The common functionality of the Uber Payments platform includes the following flows:

* **Onboarding** of payment options, facilitating users in adding new payment profiles,
* **Authorization** of payments for transactions, to guarantee that a specific amount of funds will be available for charging later,
* **Voiding** of payments, refunding a previously authorization of payments,
* **Charging and capturing** the customer account, moving (previously authorized) money from a user to Uber, 
* **Deleting** payment options and profiles.

Additional use cases include:
* **Tipping**,
* **Scheduled service** (e.g., payments of scheduled rides),
* **Promotions**,
* **Scheduled dunning** of unsettled payments,
* **Switching** payment methods during a service (e.g., on a trip),
* **Default payment method fallback/selection**.

The platform also offers mechanisms for error detection, prevention, and recovery for situations such as:
* **Duplicate payments**,
* **Incorrect currency conversion**,
* **Incorrect payment**,
* **Lack of payment**, and
* **Dangling authorization**.

Lastly, the payment platform of Uber supports **flows around digital wallet cash payments**. Due to its worldwide operations, Uber frequently works in economies where cash payments are used a lot, frequently the preferred or the only available payment mechanism. The main challenge of cash payments is capturing the actual money movement, as the exchange of money happens outside the digital systems. It is also challenging to do risk assessments as the real money situation is only indirectly known. For more interesting details on cash payments see [**Scaling Cash Payments in Uber Eats**](https://eng.uber.com/driver-app-cash-payments/), by Steven Austin and [**Re-Architecting Cash and Digital Wallet Payments for India with Uber Engineering**](https://eng.uber.com/india-payments/), by Yijun Liu and Mrina Natarajan. 


## Conceptual Model: A Generalized Payment Order Processing

To support diverse lines of business in a uniform way, Uber Payments Platforms implements a more generic way of handling payments. The conceptual model of the Uber Payments Platform is based on the ideas of the 
[double-entry bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system) (for more details, see [the presentation](https://www.youtube.com/watch?v=Dz6dAZs8Scg&feature=emb_logo) by Nimish Sheth and Steven Karis). 

The Payments Platform inherits three key principles from double-entry bookkeeping: 

* **Immutability** of orders (once created, the payment orders are immutable: if an order was created in error, a new corrective order needs to be created),
* **Audatibility** of all money movements (reliably stored and cannot be changed),
* **Error detection** based on the **zero-sum** principle. Every entry to an account requires a corresponding and opposite entry to a different account.

The implementation of payments in Uber platform centers around three key concepts (Figure 2):

* **Entry** - describes a single instance of a money movement to or from an entry (a customer, partner or Uber business),
* **Account** represents the entity in payments, capturing all entries of that entity. The sum of money amounts in the account entries represents its balance,
* **Order** - captures the payments for encapsulating all money movements among the involved parties (customers, partners, and Uber businesses). 

These concepts are generic, not tight to any specific country or business, enabling the core of the Payment Platform to stay relatively stable as new businesses or payment mechanisms are introduced.

![](../assets/images/uber_payments/order_account_entry.png)
**Figure 2**: *Conceptual model - orders, accounts, and entries. An account represents a financial state of an entity (customer, partner, Uber business). An entry describes the amount to be added or reduced from an account. An order is a collection of entries covering all account changes in one business transaction.  The sum of the amounts in entries of an order should be zero. A sum of entries in an account represents the account balance. (based on [Evolution of Payments at Uber](https://www.youtube.com/watch?v=Dz6dAZs8Scg&feature=emb_title) by Nimish Sheth & Steven Karis).*

Conceptually, the Uber payment platform can be described as a generalized **payments order processing system**, based on the **zero-sum principle** (Figure 3). The processing of a payment order results in money movements to and from accounts. The zero-sum principle also originates from the [double-entry bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping_system) and [zero-proof bookkeeping](https://www.investopedia.com/terms/z/zero-proof-bookkeeping.asp), and in this context it means that sum of amounts (+ vs -) in each order has to be zero. For instance, a typical Uber payment order will involve the collection of the money from a customer for a service (e.g., ride-sharing), paying (disbursement) of a partner (e.g., a driver), as well as obtaining a service charge for a Uber business. These three entries will constitute an order, and the amount of money collected from the customer has to equal the amount of money obtained by partners and Uber businesses.

![Test](../assets/images/uber_payments/order_processor.png)
**Figure 3:** *A order processor. The processor changes the state of account based on the entries in the order according
to the zero-sum principle.*

The zero-sum principle is a simple error detection mechanism, especially useful it in a loosely coupled distributed systems at the Uber scale. Processing of the order will results in several transactions, each potentially involving integration with different payment service providers and banks. As delays, network, and other failures will unavoidably happen, zero-sum principle provides a solid method to detect if any errors happened.

## Functional Architecture

The Uber Payments Platform is a part of a broader ecosystem of Uber's internal and external systems (Figure 4). Each of Uber businesses (Rides, Eats, Freight ...) has its specific systems and apps. These systems obtain access to the functionality of the Payments Platform through the self-serviced, payment platform configuration layer. The Uber Payment platform also interacts with Uber internals systems for service such as reporting, invoicing, or tipping.

![Uber Payments Platform in Context](../assets/images/uber_payments/context.png)
**Figure 4:** *The Uber Payments Platform in context. The Platform is a part of an ecosystem of internal and external systems.*

Zooming in the Uber payment architecture, we can distinguish several key components (Figure 5):

* **API** (a part of Uber.com API), providing a uniform interface to the payment functionality,
* **Risk Engine**, making decisions about payment-related risks,
* **Payment Profile Service**, providing the details of payment mechanisms,
* **User Profile Service**, providing details about user payment and other settings,
* **Payment Auth Service**, providing services for authentication of payments,
* **PSP Gateways**, implementing the integration with payment service providers (PSPs),
* **Order store**, storing data about orders, and 
* **Account store**, storing data about the accounts of payment parties.

![Uber Payments Platform in Context](../assets/images/uber_payments/modules.png)
**Figure 5:** *Key modules of the Payments Platform.*

To get some more concrete idea how these components interact, I drafted the following two sequence diagrams (Figure 6 and Figure 7) illustrating  possible interactions among the modules for the frequently used authorization and charging functionalities (this diagrams are my speculation about how these flows work, at very abstract and idealized level, see [Payments Integration at Uber: A Case Study](https://www.youtube.com/watch?v=yooCE5B0SRA&feature=emb_title) by Gergely Orosz for a more specific case):

![Uber Payments Platform in Context](../assets/images/uber_payments/flow_preparation.png)
**Figure 6:** *The interaction among payment components for authorization of the payment amount (to be charged later).*

![Uber Payments Platform in Context](../assets/images/uber_payments/flow_payment.png)
**Figure 7:** *The interaction among payment components for charging a previously authorized amount.*

## Implementation: Distributed Stream-Processing

At a deeper level, the Uber Payments platform is implemented as a collection of microservices organized as a stream-processing architecture. Streaming data refers to data that is continuously generated, typically in high volumes and at high velocity. Uber handles dozens of millions of transactions daily, making a streaming-based architecture a natural choice.
 
### Key Technology: Apache Kafka

The key technology used by Uber Payments Platform is [Apache Kafka](https://kafka.apache.org/) - an open-source stream-processing software platform (the [talks](https://www.youtube.com/watch?time_continue=1011&v=5TD8m7w1xE0&feature=emb_logo) by Uber engineers Emilee Urbanek and Manas Kelshikar, give useful insights on Uber Payments Kafka implementation).


![Uber Payments Platform in Context](../assets/images/uber_payments/streaming_architecture.png)

Kafka has several key capabilities, inherited by the Uber Payments platform:

* **[Publishing and subscribing](http://www.enterpriseintegrationpatterns.com/patterns/messaging/PublishSubscribeChannel.html)** to streams of records, similar to message queues or enterprise messaging systems.

* **Storing streams** of records in a **fault-tolerant durable** way.

* **Asynchronously processing** streams of records as they occur. Asynchronous processing maps well on the transactions in the payments domain: payment processing requires high reliability, but can afford to be implemented asynchronously (within a time-bound).

* **Horizontal scaling** to handle changing load.

Nodes connected via Kafka are typically microservices, mostly built in Go and Java, with some services are written in NodeJS or Python (see the [presentaiton](https://www.youtube.com/watch?v=yooCE5B0SRA&feature=emb_title) by Gergely Orosz).

<!--
Using a streaming architecture and Kafka features provides the following key benefits:

* Dependency Failures: We should assume there will be some failures and bugs and respond accordingly. Techniques leveraging streaming can be used for handling of failures.

* Processing all requests: Without fail, all requests must be processed. At scale and with unpredictable traffic spikes, this can be difficult to accomplish. 

* Many consumers: Uber has a large number of consumers, and more are added regurarly. 
-->

### Performance and Scalability

One of the key technical challenges that Uber faces in the implementation of payments platform is the scale of its operations. For illustration, here are some [recent stats](https://www.businessofapps.com/data/uber-statistics/):
* 65 countries, 600 cities,
* 75 million Uber passengers,
* 3.9 million Uber drivers,
* 14 million Uber trips per day (well over [10 billion trips](https://www.uber.com/newsroom/10-billion/) have been completed worldwide).

In addition to the worldwide scale, the load is not uniform and may have unexpected spikes.
 
While details are not publically available, the technical presentations provide some insights in mechanisms used by Uber for handling performance and scalability requirements, such as:
* **Extensive parallelization** of processing with the [competing consumers pattern](https://www.enterpriseintegrationpatterns.com/patterns/messaging/CompetingConsumers.html), by having multiple parallelly running (micro)service instances
* **Independent scaling** of processing components, to more flexibly manage needed capacity, and 
* Using **optimistic locking**, to avoid the need for complex distributed locking mechanisms.

In addition, Kafka supports well high performance and scalability requirements. Kafka is horizontally scalable, fault-tolerant, and optimized for speed, running as a cluster on one or more servers that can span multiple data centers (Uber uses use a combination of third-party cloud computing services and co-located data centers). 

  
  
### Reliability

Implementing a reliable streaming-based payment system comes with several challenges (see  [Reliable Processing in a Streaming Payment System](https://www.youtube.com/watch?v=5TD8m7w1xE0) by Emilee Urbanek and Manas Kelshikar for details):

* **System failures** (a failure may occur midway through processing)
* **Poison pill** (an inbound message cannot be consumed)
* **Functional bugs** (no technical errors, but results are invalid)

Key mechanisms to deal with reliability requirements, mentioned in Uber tech talks, include:

* **Redundancy** of all services, including the messaging infrastructure, enables resilience during internal system failures,
* Implementation of the [**guaranteed delivery pattern**](http://www.enterpriseintegrationpatterns.com/patterns/messaging/GuaranteedDelivery.html) pattern, by using Kafka capability to persist messages so that they are not lost even if the messaging system crashes,
* Implemention of **timeouts**, both in integration with external systems, as well as internal services to prevent long-term system overloading,
* **Retrying** operations, based on a defined error strategy (Figure 8), or move messages to a [dead letter queue](https://www.enterpriseintegrationpatterns.com/patterns/messaging/DeadLetterChannel.html), so that messages are never lost,
* Implementation of **idempotent message handling** for service operations. [An idempotent operation](https://stackoverflow.com/questions/1077412/what-is-an-idempotent-operation) is one that has no additional effect if it is called more than once with the same input parameters. Apache Kafka implements the "at least once" message delivery strategy, implying subscribers may receive the same message multiple times, so subscribers that manage state and cause side effects should implement idempotent message handling.  
* **Load-smoothing through queuing**, to avoid overloading of services, and
* **Validation** of processing results based on **side-effects recording** (Figure 9).


![Uber Payments Platform in Context](../assets/images/uber_payments/streaming_architecture_error_handling.png)
**Figure 8**: *Error handling requires an error strategy. An error can lead to retry of an operation, of its achiving the dead message queue (DMQ).*

![Uber Payments Platform in Context](../assets/images/uber_payments/streaming_architecture_validation.png)
**Figure 9**: *Each complex operation will lead to some side effects. A validator can them at some moment check if actual side effects match the expected once.*



## Implementation: Integration with External Systems

The Payments Platform interacts with payment service providers (PSPs) and banks to execute payment transactions. At the end of 2018, Uber claimed to interact with 28 PSPs and five banks directly.

The [presentation](https://www.youtube.com/watch?v=MJABqwzBkHs&feature=emb_title) by Uber engineer Paul Sorenson, provides some insights into how Uber integrates with external systems. While each integration with PSPs and banks is different, we can distinguish two integrations styles (Figure 10):
* API-based integrations with modern PSP integrations, with REST-based APIs, exchanging data in JSON, one transaction at a time, near-real time,
* legacy batch integration with banks, where integrations are done by exchanging files via SFTP,  with relatively low frequency (day or hours). 

![](../assets/images/uber_payments/external_integrations.png)
**Figure 10:** *Two integrations styles for integration with external systems: API-based, and file-based.*

Paul Sorenson also provides some concrete tips on how to properly implement idempotent message processing when working with external systems. Idempotency is an essential theme in integration with external payment systems. A good thing about PSP and banking systems is that they are normally implementing their services as idempotent message processors. Idempotency is essential for payment systems for two reasons:

* It helps to prevent double charging
* It improves reliability and simplifies system architecture. 

When a failure occurs (e.g., a network error), it may be challenging to determine if some operation succeeded or failed and in which state the system is. Without idempotency, for instance, retying operations may be risky, as you may execute the same operation twice (e.g. charging a customer twice for the same service). With idempotency, you can repeat the failed operation without such worries. Figure 10 illustrates how idempotency (in the context of integration with external systems) works in an ideal scenario.

![](../assets/images/uber_payments/external_communication_retry_simple.png)

**Figure 10:** *Idempotent message processing systems will not process the same message twice (figure is adapted from the [presentation](https://www.youtube.com/watch?v=MJABqwzBkHs&feature=emb_title) by Paul Sorenson).*

Idempotency works well if you repeat the request against the same system, with the same operation ID. The operations  ID needs to be provided by the application calling an idempotent service so that the service knows if it is getting the new request (not previously processed ID) or a repeated operation (already processed ID). 

One challenge of implementing idempotency when interacting with external systems relates to the IDs used for idempotent operations. Legacy payments systems accept a more limited range of values for IDs. Careful rotation and timing of such IDs are essential to avoid the external system rejecting the payment request. The [presentation](https://www.youtube.com/watch?v=MJABqwzBkHs&feature=emb_title) by Paul Sorenson provides some tricks on how to deal with this issue.

Paul Sorenson also talks about another challenge of implementing a proper idempotent behavior when integrating with the external systems, the one related to multiplexing PSPs. Payments operations use several PSPs in a complex arrangement, and another PSP may be used if a payment fails with the originally selected one. Such practice may improve collection rate, but naively retrying a failed operation on another PSP may lead to double charging, as illustrated in Figure 11.

![](../assets/images/uber_payments/external_communication_complex_wrong.png)
**Figure 11:** *The incorrect way to retry operations in the case of network failures when working with multiple PSPs (figure is adapted from the [presentation](https://www.youtube.com/watch?v=MJABqwzBkHs&feature=emb_title) by Paul Sorenson). Network error does not necessarily mean that the operation has failed, and retrying the operation on a different PSP may thus lead to double charging.*

The approach Uber uses to avoid this problem is by using dedicated request storage consulted when a retry needs to be performed, to ensure that retry goes back to an original service (Figure 12).

![](../assets/images/uber_payments/external_communication_complex_good.png)
**Figure 12:** *The correct way to retry operations in the case of network failures when working with multiple PSPs (figure is adapted from the [presentation](https://www.youtube.com/watch?v=MJABqwzBkHs&feature=emb_title) by Paul Sorenson). using dedicated request storage to ensure that retry goes back to an original service.*





## Development Process

In addition to standard testing, debugging, and rollout techniques, payment systems have few specifics.  

Developing and testing of payments systems is more challenging due to several reasons:
* the distributed nature of the payments platform (many loosely coupled moving parts), which requires complex 
  configurations for test environments,
* a considerable number of external integrations, which requires extensive integration testing,
* a worldwide scale and a huge amount of transactions, which makes it difficult to create realistic testing environments and loads.

In his presentation on [Payments Integration at Uber: A Case Study](https://www.youtube.com/watch?v=yooCE5B0SRA&feature=emb_title), Gergely Orosz provided some basic insights into the specifics of the development process at Uber Payments teams:

* **Sandbox testing.** Most payment service providers (PSPs), offer help in testing by providing support for sandbox testing. PSPs typically have a sandbox environment, an environment functionally equivalent to but otherwise isolated from the production environment. Such ready-to-be used settings simplify development and testing activities.

* **Testing with Real Cards.** Testing of payment systems always needs to, at some point, involve testing with real paying instruments (e.g., cards). 

* **Testing in production.** Some testing and development in production are unavoidable (e.g., develop against the production load, or by routing production traffic to development environments). Otherwise, it is practically impossible to simulate production architecture and load realistically in development and test settings. Among other technologies, Uber uses [Cerberus](https://cerberus-testing.com/) for tests that run against applications in production environments.

* **Rollouts.** Rollouts of the new version are data-driven, and as much as possible, treated as continuous experiments. Rollouts are planned well in advance, and require early agreement on which key metrics to track. Rollouts of new product versions require careful selection of first experimentation regions, to enable the gradual introduction of functionality with fewer risks.

* **Monitoring.** Monitoring requires building custom dashboards segmented by proper metrics, such as payment type, operation, or city/region. For monitoring, Uber uses [Grafana](https://grafana.com/), among other technologies.

* **Alerting.** Uber uses machine learning for anomaly detection and alerting. Alerting is configured at multiple levels, e.g., global as well as per country.

* **Mitigation and logs analysis.** Uber uses Elasticsearch and Kibana for analysis and exploration of production logs. The goal is to determine if there is a likely outage happening.



## Summary

This brief overview only scratches the surface of Uber Payments platforms. Many of the relevant topics, such as security and privacy, are not covered. Nevertheless, I believe that the presented material and referenced resources can provide some insights and ideas about the challenges of building modern payment systems.

Key points:

* Conceptually, the Uber payment platform can be described as a generalized **payment order processing system**, based on the ideas of double-entry bookkeeping.
   
* At a deeper level, Uber Payments platform is a collection of **microservices** organized in a **stream-processing architecture**. 
   
* The key technology used by Uber Payments is **Apache Kafka** - an open-source stream-processing software platform.
 
* Processing in distributed systems at scale comes with several challenges, including **error handling**, **validation**, and  **integration with external systems**. 

* Mentioned technologies: Apache Kafka, Go, Java, NodeJS, Python, Cerberus, Grafana, Elasticsearch, Kabana 

## Appendix 

### To Probe Further
> 1. [**Uber Payments Platform Engineering team Meeting in San Francisco**](https://eng.uber.com/payments-platform/), September 2018
>    1. [Engineering Uber’s Next-Gen Payment Platform](https://www.youtube.com/watch?v=rp7_7HcqmKA&feature=emb_title) by Mathieu Chauvin
>    1. [Evolution of Payments at Uber](https://www.youtube.com/watch?v=Dz6dAZs8Scg&feature=emb_title) by Nimish Sheth & Steven Karis 
>    1. [Payments Integration at Uber: A Case Study](https://www.youtube.com/watch?v=yooCE5B0SRA&feature=emb_title) by Gergely Orosz 
>    1. [To the Nines: Building Uber's Payments Processing System](https://www.youtube.com/watch?v=MJABqwzBkHs&feature=emb_title) by Paul Sorenson
> 1. [**MoneyCon ’19: Uber Hosts its First FinTech Engineering Conference**](https://eng.uber.com/moneycon/), July 2019
>    1. [Welcome & Keynote](https://www.youtube.com/watch?v=jItgWGO5qHE) by Uber Engineering Director Lee Crawford
>    1. [Reliable Processing in a Streaming Payment System](https://www.youtube.com/watch?v=5TD8m7w1xE0) by Uber engineers Emilee Urbanek and Manas Kelshikar
> 1. **News Articles**:
>    1. [Uber announces deeper push into financial services with Uber Money](https://www.cnbc.com/2019/10/28/uber-announces-deeper-push-into-financial-services-with-uber-money.html), CBNS, 2019
>    1. [Uber’s Fintech Strategy: A Conversation With Peter Hazlehurst, Head Of Uber Money](https://www.forbes.com/sites/ronshevlin/2019/11/04/a-peek-into-ubers-fintech-strategy-a-conversation-with-peter-hazlehurst-head-of-uber-money), Forbes, 2019
>    1. [Uber pushes into payments with Uber Money](https://www.ft.com/content/e8a3cf46-f969-11e9-a354-36acbbb0d9b6), Finacial Times, 2019
>    1. [Uber unveils Uber Money, its new financial services team, along with a digital wallet and new card offerings](https://www.businessinsider.com/uber-reveals-new-financial-services-team-uber-money-2019-10?international=true&r=US&IR=T), Business Insider, 2019
>    1. [Uber Money Wants To Be The Bank Account For Uber Drivers](https://www.pymnts.com/news/payments-innovation/2019/uber-money-wants-to-be-the-bank-account-for-uber-drivers/), pymnts.com, 2019
>    1. [Uber will pay drivers and couriers after every trip](https://www.engadget.com/2019/10/28/uber-money-bank-account-debit-credit-card/), engadet.com, 2019
>    1. [Official Uber Money Page](https://www.uber.com/newsroom/introducing-uber-money/), uber.com, 2019
>    1 [Uber Money is here: How big tech is transforming mobile payments!](https://siliconcanals.com/news/uber-money-is-here-how-big-tech-is-transforming-mobile-payments/), siliconcanals.com, 2019
>    1. [Uber Money to launch in India by 2020](https://www.livemint.com/companies/news/uber-money-to-launch-in-india-by-2020-11572441907978.html), livemint.com, 2019
> 1. [**Distributed architecture concepts I learned while building a large payments system**](https://blog.pragmaticengineer.com/distributed-architecture-concepts-i-have-learned-while-building-payments-systems/), by Gergely Orosz, 2018
> 1. [**Transforming Payments & Empowering Developers: Meet the Uber Amsterdam Tech Team**](https://eng.uber.com/uber-amsterdam-profile-2018/)
> 1. [**Scaling Cash Payments in Uber Eats**](https://eng.uber.com/driver-app-cash-payments/), Steven Austin, 2018
> 1. [**Re-Architecting Cash and Digital Wallet Payments for India with Uber Engineering**](https://eng.uber.com/india-payments/), Yijun Liu and Mrina Natarajan, 2018 
> 1. [**Braintree Case Study: Uber**](https://www.braintreepayments.com/nl/learn/braintree-merchants/uber), braintreepayments.com
> 1. [**How does Apple Pay work with Uber?**](https://discussions.apple.com/thread/7469114), discussions.apple.com, 2016
> 1. [**Adyen selected by Uber as a global 3D Secure solution provider**](https://www.adyen.com/press-and-media/2019/adyen-selected-by-uber-as-a-global-3d-secure-solution-provider), 2019


### Key Terminology
>
> * **Collection**: the acquiring of money (from a customer)
> * **Disbursement**: the payment of money (to a partner)
> * **PSP**: (Payment Service Provider: an entity offering an online service for accepting electronic payments)
> * **Bank**: an established authorized by a government to facilitate financial transactions (an other things)



