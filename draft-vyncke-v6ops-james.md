---
title: "Just Another Measurement of Extension header Survavibility"
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


--- abstract
In 2016, {{?RFC7872}} has measured the drop of packets with IPv6 extension headers. This document presents a slightly different methodology with more recent results.

--- middle

# Introduction

In 2016, {{?RFC7872}} has measured the drop of packets with IPv6 extension headers. This document presents a slightly different methodology with more recent results.


# Methodology

# Measurements

## Vantage Points

Several servers were used worldwide (albeit missing South America and Africa as authors were unable to have IPv6 servers in these regions). Table {{table_vantage}} lists all the vantage points together with their AS number and country.

{::include ./vantage_as.inc}
{: #table_vantage title="All vantage AS"}

### Tested Autonomous Systems


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
