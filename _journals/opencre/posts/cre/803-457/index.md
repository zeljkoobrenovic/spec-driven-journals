---
id: "CRE-803-457"
title: "Protection against AI-Specfic Threats"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-803-457
excerpt: "CRE 803-457 · in Cross-cutting concerns · 5 sub-requirements · 1 mapping to 1 standard and tool."
tags: PCI DSS
---
> **CRE**: [803-457](https://opencre.org/cre/803-457)
>
> **Part of**: [[cre-546-564]]
>
> **Maps to**: [[standard-pci-dss]]

## Where It Sits

---begin mermaid---
graph LR
  n546564["Cross-cutting concerns"] --> n803457["Protection against AI-Specfic Threats"]
  n803457 --> n061753["AI model behaviour integrity threats"]
  n803457 --> n230318["AI resource exhaustion attack"]
  n803457 --> n738144["Conventional threats to AI input, output and…"]
  n803457 --> n267786["Model confidentiality threats"]
  n803457 --> n220870["Training data confidentiality threats"]
  style n803457 stroke-width:3px
---end mermaid---

## Contains

- [[cre-061-753]] — 9 more below
- [[cre-230-318]]
- [[cre-738-144]] — 4 more below
- [[cre-267-786]] — 3 more below
- [[cre-220-870]] — 4 more below

## Mapped Standards and Tools

Each row is a section of an external standard or tool that OpenCRE links to this requirement. *Curated* links were set by the OpenCRE editors; *automatic* links were derived by OpenCRE (for example through CWE and CAPEC).

### PCI DSS

| ID | Section | Link |
| --- | --- | --- |
| 5.4 | Anti-phishing mechanisms protect users against phishing attacks. | automatic |

More: [[standard-pci-dss]]

## Source

Generated from the OpenCRE catalogue entry [803-457](https://opencre.org/cre/803-457). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
