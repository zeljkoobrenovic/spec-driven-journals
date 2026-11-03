---
id: "CRE-621-287"
title: "File upload"
date: 2026-10-22
author: OpenCRE (opencre.org)
permalink: cre-621-287
excerpt: "CRE 621-287 · in Technical application security controls › Input and output protection › File handling · 5 sub-requirements."
tags: 
---
> **CRE**: [621-287](https://opencre.org/cre/621-287)
>
> **Part of**: [[cre-636-660]] › [[cre-503-455]] › [[cre-130-550]]

## Where It Sits

---begin mermaid---
graph LR
  n130550["File handling"] --> n621287["File upload"]
  n621287 --> n163518["Check uploaded archives for decompression att…"]
  n621287 --> n463820["Limit size and number of uploaded files"]
  n621287 --> n112273["Scan untrusted files for malware"]
  n621287 --> n384344["Store and serve user-uploaded files such that…"]
  n621287 --> n660052["Validate max input/file sizes"]
  style n621287 stroke-width:3px
---end mermaid---

## Contains

- [[cre-163-518]]
- [[cre-463-820]]
- [[cre-112-273]]
- [[cre-384-344]]
- [[cre-660-052]]

## Mapped Standards and Tools

OpenCRE has no direct standard links on this requirement; see the requirements it contains.

## Source

Generated from the OpenCRE catalogue entry [621-287](https://opencre.org/cre/621-287). OpenCRE is maintained by the OpenCRE project; see [opencre.org](https://opencre.org) for the live data.
