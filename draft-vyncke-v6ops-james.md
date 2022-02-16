---
title: "Just Another Measurement of Extension header Survavibility (JAMES)"
abbrev: "JAMES"
category: info
submissiontype: IETF
docname: draft-vyncke-v6ops-james-latest
ipr: trust200902
area: "Operations and Management"
workgroup: "IPv6 Operations"
keyword: Internet-Draft
venue:
  group: "IPv6 Operations"
  type: "Working Group"
  mail: "v6ops@ietf.org"
  arch: "https://mailarchive.ietf.org/arch/browse/v6ops/"
  github: "evyncke/v6ops-james"
  latest: "https://evyncke.github.io/v6ops-james/draft-vyncke-v6ops-james.html"

stand_alone: yes
smart_quotes: no
pi: [toc, sortrefs, symrefs]

author:
 -
    ins: E. Vyncke
    name: Éric Vyncke
    organization: Cisco
    street: De Kleetlaan 64
    code: 1831
    city: Diegem
    country: Belgium
    email: evyncke@cisco.com
 -
    ins: R. Léas
    name: Raphaël Léas
    organization: Université de Liège
    city: Liège
    country: Belgium
    email: raphael.leas@student.uliege.be

normative:

informative:
  TIER1:
    title: Tier 1 network
    target: https://en.wikipedia.org/wiki/Tier_1_network
  ALEXA:
    title: The top 500 sites on the web
    target: https://www.alexa.com/topsites


--- abstract
In 2016, {{?RFC7872}} has measured the drop of packets with IPv6 extension headers. This document presents a slightly different methodology with more recent results.

--- middle

# Introduction

In 2016, {{?RFC7872}} has measured the drop of packets with IPv6 extension headers on their transit over the global Internet. This document presents a slightly different methodology with more recent results.


# Methodology

In a first phase, the measurement is done between collaborating IPv6 nodes spread over the Internet and multiple Autonomous Systems (ASs). As seen in {{analysed_as}}, the source/destination/transit ASs include some "tier-1" providers per {{TIER1}}, so, they are probably representative of the global Internet core.

Relying on collaborating nodes has some benefits:

- traffic timing can be measured accurately to answer whether extension headers are slower than plain IP6 packets;

- traffic can be capture into .pcap file at the source and at the destination for later analysis.

Future phases will send probes to non-collaborating nodes with a much reduce probing speed. The destination will include {{ALEXA}} top-n web sites, popular CDN, as well as random prefix from the IPv6 global routing table. A revision of this IETF draft will describe those experiments.

# Measurements

## Vantage Points

Several servers were used worldwide (albeit missing South America and Africa as authors were unable to have IPv6 servers in these regions). {{table_vantage}} lists all the vantage points together with their AS number and country.

{::include ./vantage_as.inc}
{: #table_vantage title="All vantage AS"}

### Tested Autonomous Systems {#analysed_as}

During first phase (traffic among fully meshed collaborative nodes), our probes have collected data on the following ASs:

{::include ./analysed_as.inc}
{: #table_analysed_as title="All AS (source/destination/transit)"}

### Tested Extension Headers

## Results

### AS dropping transit traffic

### Most dropped extension headers

# Security Considerations

While active probing of the Internet may be considered as an attack, this measurement was done among collaborating parties and using the probe attribution technique described in I-D.draft-vyncke-opsec-probe-attribution.


# IANA Considerations

This document has no IANA actions.

--- back

# Acknowledgments
{:numbered="false"}

The authors want to thank Sander Steffann and Jan Zorz for allowing the use of their labs.

Special thanks as well to professor Benoît Donnet and research assistant Justin Iurman for their support and advices. This document would not have existed without their support.
