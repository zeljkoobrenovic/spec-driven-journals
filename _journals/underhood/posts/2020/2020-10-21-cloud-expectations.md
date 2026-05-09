---
layout: post
title: "Public Cloud: Great Expectations"
date:   2020-01-21 21:12:01 +0100
categories: architecture
icon: cloud.png
author: by Željko Obrenović (obren.io)
permalink: cloud-expectations
timetoread: 15 min
excerpt: "This article enlists some of the key benefits we can expect from of cloud: development velocity, performance, scalability, functionality, uptime, costs, transparency, and security. The article also provides a reality check on these expectations. You need to earn the public cloud benefits; simply moving to the cloud rarely leads to immediate improvements."

---
![](assets/images/cloudstrategy/expectations.jpg)

> **KEY POINTS:**
> * This article enlists some of the key benefits you could expect from of cloud: velocity, performance, scalability, functionality, uptime, costs, transparency, and security. 
> * The article also provides a reality check on these expectations. Spoiler alert: you need to earn these benefits; simply moving to the cloud rarely leads to immediate improvements.

&nbsp; 
> *"We changed again, and yet again, and it was now too late and too far to go back, and I went on. And the mists had all solemnly risen now, and the world lay spread before me."*
>&nbsp;
>&nbsp;
<br>― Charles Dickens, Great Expectations

&nbsp; 
&nbsp;

When talking about architecture at any organization, Public Cloud is an unavoidable topic. Most organizations are on a journey that, in the long run, will lead towards a significant portion of our systems, if not all of them, running in a public cloud. And we all seem to have great expectations. 

Hype and buzzwords surround everything about the cloud. With this article, I wanted to, in plain English, discuss a critical aspect of the public cloud journey: the WHY question. In other words, why would we want to move there? What can and should you expect?

I base my discussion on the [**Cloud Strategy**](https://architectelevator.com/book/cloudstrategy/) book, adapting the cloud's benefits listed there to my experiences. I group potential benefits of the cloud in eight categories:
* Development velocity (time-to-market)
* Performance (geo-proximity)
* Scalability
* Managed value-adding services (e.g., ML, AI analyses)
* Uptime
* Elastic pricing model
* Transparency
* Security

In the following sections, I discuss each of these drivers for public cloud migrations. Each section has two parts, one discussing benefits and the other providing a reality check. These benefits have to be earned and will not automatically follow the mere move to the public cloud.


## Development Velocity (Time-to-Market)

For most organizations, increasing development velocity is probably the most significant long-term benefit of the public cloud. 

Modern public cloud tools can assist in accelerating software delivery in multiple ways. Figure 1 illustrates my view on the drivers of increased velocity in the cloud.


![](assets/images/cloudstrategy/velocity.png)
***Figure 1:** The drivers of increased developer velocity in the public cloud.*

Fully managed build toolchains and automated deployment tools, for instance, allow teams to be more productive by focusing on feature development. At the same time, the cloud takes care of compiling, testing, and deploying software. Another source of accelerating software delivery comes from managed and self-service tools. These tools encapsulate low-level details and complexity and empower developers to do tasks that would otherwise require additional SiteOps or DevOps teams. 

The hiring of developers can be easier for the public cloud. On the one hand, modern cloud tools are more attractive to talented developers. On the other hand, public cloud expertise is more standardized, and it is easier to find public cloud experts worldwide and outsource your development.

Reality check:
* If you do not have high-velocity in your current setting, then it is unlikely that you will immediately get it from the cloud. Moreover, you may lose some velocity due to the need to learn new technologies, at least temporarily. Cloud gives you more options to increase development velocity, but to benefit from these options, you need to live DevOps culture and have a high level of automation at all levels.
* The best way to prepare for high-velocity is to focus on improving [4 key metrics](https://www.thoughtworks.com/radar/techniques/four-key-metrics): lead time, deployment frequency, mean time to restore (MTTR), and change failure percentage. The researchers have determined that these four key metrics differentiate between low, medium, and high IT organization performers. If you are a high performer, then the cloud can make you even better. If you are not, then moving to the public cloud is only the first step.


## Performance

Hosting applications with a cloud provider can provide shorter paths and a better user experience than applications hosted on-premises. Figure 2, for instance, illustrates the current investment in data centers and networks for the Google Cloud Provider. With our customers on different continents, we can benefit from the public cloud's geo-proximity to provide shorter paths to our customers. Even a minute increase in performance can have a significant impact on users' behavior.

![](assets/images/cloudstrategy/gcpinfra.png)
***Figure 2:** Google Cloud Provider infrastructure overview.*


Reality check:
* Geo-proximity is just one aspect of overall system performance. Other elements include database query processing, waiting for a response from external services, chattiness between services. So you may be disappointed by the impact of cloud migration on the performance of your application.
* Best way to prepare for performance optimizations in the public cloud is to know your performance profile well. Transparency is the key. In particular, having clear insights on all drivers behind latency.
* By moving a part of your applications to the cloud, your performance can worsen if your application depends on service outside the public cloud, e.g., in the data center. 


## Scalability

A vital premise of the public cloud is the instant availability of computing and storage resources, allowing applications to scale out to remain performant under increased load. Conveniently, the cloud model makes capacity management the cloud provider's responsibility, freeing our IT from maintaining unused hardware inventory. We can provision new servers when we need them and only when we need them.

 While we can scale our data centers by adding more hardware, planning is the main difference with the public cloud. In a public cloud, you can decide to scale up at any moment; capacity is practically unlimited. There is no long-term commitment. You can scale down your operations any time you want.


Reality check:
* Main business value of scalability is having an option to instantly scale up (or down) operations with predictable costs and without long-term commitments. Examples include increased load due to new COVID-like crisis, adding new marketplaces within months. If your load is stable or predictably growing, then you do not directly benefit from cloud scalability.
* While public cloud providers allow you to scale down at any moment, it is our responsibility to stop resource usage, not the cloud providers. That means that we need to architect applications so that they can be scaled up and down. And we also need to have a "scaling down" discipline. It has little cost benefits if you can kill servers an hour after you provision them if you keep forgetting to do so. From my previous experiences, I know examples of people running large clusters of servers the whole weekend while they needed them for only 30 minutes.



## Managed Value-Adding Services

The cloud is not all about computing resources. Cloud providers offer services that are impractical or impossible to implement at the scale of corporate data centers (Figure 3). For example, large-scale machine learning systems or pre-trained models inherently live in the cloud. Examples include open-source machine learning frameworks such as TensorFlow, pre-trained models such as Amazon Rekognition or Google Vision AI, or data warehouse tools like Google BigQuery or AWS Redshift. Another example includes services that on-premise would require significant operational capacity, such as managing big Kubernetes clusters. 

<div style="text-align: center">
<img src="assets/images/cloudstrategy/gcp-services.png" style="width: 480px"><br>
</div>
***Figure 3:** Google Cloud Platform catalog contains 100+ products, covering a wide array of use cases.*

Reality check:
* You do not get any value from services you do not use. Moving to the cloud to be around speculatively valuable services may be difficult to justify.
* Added value functionality is the most valuable when a cloud offering closely matches your market needs (e.g., registration plate recognition). If that is not the case, you may end up with complicated hacks to manage "managed" services.
* Using managed services creates some level of lock-in. While this is not necessarily bad, you need to be aware of the potential consequences.



## Uptime

A global footprint allows applications to run across a network of global data centers, each of which features multiple availability zones (AZs). Cloud providers also maintain massive network connections to the internet backbone, improving their resilience against distributed denial-of-service (DDoS) attacks. Public cloud run-time platforms have built-in resilience as part of their container orchestration or serverless platforms.


Reality check:
* Cloud computing isn't a magic button that makes brittle applications suddenly available 24/7 with zero downtime. Even if the server keeps running, your application might be failing. You may need to adjust the application architecture and the deployment model to achieve high levels of availability.



## Elastic Pricing Model 

Savings in the public cloud come from using managed services and the cloud's elastic "pay as you grow" pricing model that allows suspending compute resources that you are not utilizing (Figure 4). The significant savings potential lies in this elastic pricing model.

<div style="text-align: center">
<img src="assets/images/cloudstrategy/elasticity.png"><br>
</div>
***Figure 4:** Without elasticity, you need to provide and pay for enough resources to handle the highest demand. With elasticity, you provision only the resources necessary to address current demand.*


Reality check:
* Cloud providers have favorable Economies of Scale but invest heavily in global network infrastructure, security, data-center facilities, and modern technologies such as machine learning. Cloud providers do not use cheap technology, and hence one should be cautious about expecting drastic cost reduction by merely lifting and shifting an existing workload to the cloud.
* Realizing any savings requires transparency into resource utilization and high levels of deployment automation—cloud savings have to be earned.
* Elasticity is bi-directional (Figure 5) and can lead to a drastic cost increase if an unexpected usage increase occurs, e.g., denial of wallet.

<div style="text-align: center">
<img src="assets/images/cloudstrategy/elasticitycosts.png" style="height: 360px"><br>
</div>
<i><b>Figure 5:</b>Elasticity can both increase and reduce costs.</i>



## Transparency

Migrating to the cloud can dramatically increase transparency thanks to uniform automation and monitoring. Classic IT often has limited transparency in its operational environments. Simple questions like how many servers are provisioned, which applications run on them, or what is their patch status are often tricky and time-consuming to answer.

Figure 6 shows the anonymous screenshot of the Cloud usage explorer, a tool I built to visualize automatically collected data about the Google Cloud Platform (GCP) usage. Google Cloud Providers gives detailed data about which platform uses which services, resource family, budget. You can also understand which people and teams have access to each service. It is possible to get real-time information about our cloud usages and understand the trends in a fully automated fashion.

<div style="text-align: center">
<img src="assets/images/cloudstrategy/cloud-usage-explorer.png" style="height: 360px"><br>
</div>
<i><b>Figure 6:</b>An example of an cloud usage explorer.</i>

Reality check:
* Transparency is good, but its value lies in using the obtained data to improve your systems. Hence, we need transparency and the process to turn transparency into action.
* To get full transparency of your system requires additional measures and logging. Cloud can tell you how much storage or network you use, but it will not tell you anything about your system's internals.
* You can solve the problem of the limited transparency of classical IT with better tools and processes. Our private cloud provides quite a significant amount of detailed information.


## Security

Public cloud providers invest heavily in security at multiple levels, including hardware, operating models, and products.

Public cloud hardware investments are essential as attack vectors have shifted to exploit hardware-level vulnerabilities based on microprocessor design (Spectre and Meltdown) or compromised supply chains. Such attacks render traditional data-center "perimeter" defenses ineffective and position large-scale cloud providers as the few civilian organizations with the necessary resources to provide adequate protection. Several cloud providers further increase security with custom-developed hardware, such as AWS' Nitro System or Google's Titan Chip. Such custom-developed hardware employs the notion of an "in-house hardware root of trust" that detects hardware or firmware manipulation. 

Cloud providers use a sophisticated operating model with frequent and automated updates, additionally strengthening their security posture. Public cloud providers invest in ensuring compliance with many security and related privacy regulations, such as [ISO/IEC 27001](https://en.wikipedia.org/wiki/ISO/IEC_27001), [ISO/IEC 27017](https://en.wikipedia.org/wiki/ISO/IEC_27017), [ISO/IEC 27018](https://en.wikipedia.org/wiki/ISO/IEC_27018), [ISO/IEC 27701](https://en.wikipedia.org/wiki/ISO/IEC_27701), [SOC 2/3](https://en.wikipedia.org/wiki/System_and_Organization_Controls), and [GDPR](https://en.wikipedia.org/wiki/General_Data_Protection_Regulation).

Lastly, cloud providers provide numerous security products such as Software-Defined Networks (SDNs), identity-aware gateways, firewalls, Web Application Firewalls (WAFs), and many more, which you can use to protect applications deployed to the cloud.

Reality check:
* There is no set of products that automatically increase security when migrating to the cloud. Cloud gives you options to increase your security, but it is up to you to apply them properly. Security follows the weakest link principle. Perfect cloud security will not help you if, for instance, you make your access keys publicly available. According to a [2017 Gartner report](https://www.gartner.com/smarterwithgartner/is-the-cloud-secure/), at least 95% of cloud security failures are the customer's fault.
* Cloud providers generally follow the shared responsibility model, where they are responsible for the security **of** the cloud, we are accountable for security **in** the cloud. The cloud vendor manages and controls the host Operating System (OS), the virtualization layer, and their facilities' physical security. We are responsible for configuration and managing the security controls. We are also responsible for encrypting data in transit and at rest. 


## Setting Clear Expectations and Measuring Progress

While there are many reasons for moving to the public cloud, and different teams will get different values, one thing is the same. You need to set your expectations explicitly and communicate them with key stakeholders.  If you move to the cloud to increase development velocity, but other stakeholders expect cost reduction, we have set the stage for an unproductive conflict. 

Another important thing is to measure your progress. Setting expectations to be measured is not easy but is crucial to justify investments. 

Lastly, moving to the cloud is not only a technical issue. Improving development velocity, for instance, does not have value in itself. The value of development velocity lies in shorter [time-to-market (TTM)](https://en.wikipedia.org/wiki/Time_to_market). But estimating the value of shorter TTM requires input from product and business stakeholders. Consequently, we need to work closely with business stakeholders to create realistic and pragmatic cases of public cloud usage.




## Acknowledgments

I would like to thank Peter Maas, Jilles Oldenbeuving and David Campbell for their feedback and numerous discussions on the public cloud. Photo by Juan Mendez from Pexels.


## To Probe Further

1. [**Cloud Strategy**](https://architectelevator.com/book/cloudstrategy/), Gregor Hohpe, LeanPub 2020.
