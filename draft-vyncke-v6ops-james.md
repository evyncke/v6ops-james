---
title: "Just Another Measurement of Extension header Survivability (JAMES)"
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
 -
    ins: J. Iurman
    name: Justin Iurman
    organization: Université de Liège
    country: Belgium
    email: justin.iurman@uliege.be

normative:

informative:
  TIER1:
    title: Tier 1 network
    target: https://en.wikipedia.org/wiki/Tier_1_network
  ALEXA:
    title: The top 500 sites on the web
    target: https://www.alexa.com/topsites


--- abstract
In 2016, {{?RFC7872}} has measured the drop of packets with IPv6 extension headers. This document presents a slightly different methodology with more recent results. It is still work in progress.

--- middle

# Introduction

In 2016, {{?RFC7872}} has measured the drop of packets with IPv6 extension headers on their transit over the global Internet. This document presents a slightly different methodology with more recent results. Since then, {{?I-D.draft-ietf-opsec-ipv6-eh-filtering}} has provided some recommendations for filtering transit traffic, there may be some changes in providers policies.

It is still work in progress, but the authors wanted to present some results at IETF-113 (March 2022).

# Methodology

In a first phase, the measurement is done between collaborating IPv6 nodes spread over the Internet and multiple Autonomous Systems (ASs). As seen in {{analysed_as}}, the source/destination/transit ASs include some "tier-1" providers per {{TIER1}}, so, they are probably representative of the global Internet core.

Relying on collaborating nodes has some benefits:

- traffic timing can be measured accurately to answer whether extension headers are slower than plain IP6 packets;

- traffic can be captured into .pcap file at the source and at the destination for later analysis.

Future phases will send probes to non-collaborating nodes with a much reduced probing speed. The destination will include {{ALEXA}} top-n websites, popular CDN, as well as random prefix from the IPv6 global routing table. A revision of this IETF draft will describe those experiments.

# Measurements

## Vantage Points

Several servers were used worldwide (albeit missing Africa as authors were unable to find IPv6 servers in these regions). {{table_vantage}} lists all the vantage points together with their AS number and country.

{::include ./vantage_as.inc}
{: #table_vantage title="All vantage AS"}

### Tested Autonomous Systems {#analysed_as}

During first phase (traffic among fully meshed collaborative nodes), our probes have collected data on the following ASs:

{::include ./analysed_as.inc}
{: #table_analysed_as title="All AS (source/destination/transit)"}

### Tested Extension Headers

In the first phase among collaborating vantage points, packets always contained either a UDP payload or a TCP payload, the latter is sent with only the SYN flag set and with data as permitted by section 3.4 of {{!RFC793}} (2nd paragraph). A usual traceroute is done with only the UDP/TCP payload without any extension header with varying hop-limit in order to learn the traversed routers and ASs. Then, several UDP/TCP probes are sent by with a set of extension headers:

- destination options header containing either an unknown option with the "skip" bits or an unknown option with the "discard" bits of varying extension header length: 8, 256, and 512 octets;

- hop-by-hop options header containing either an unknown option with the "skip" bits or an unknown option with the "discard" bits of varying extension header length: 8, 256, and 512 octets;

- routing header with routing types from 0 to 6 inclusive ;

- atomic fragment header (i.e., more flag = 0 and offset = 0) or varying frame length 512, 1280, and 1492 octets;

- authentication header with dummy SPI followed by UDP/TCP header and a 38 octets payload.

In the above, length is the length of the extension header itself except for the fragmentation header where the length is the frame length (i.e., including the Ethernet, IPv6, and TCP/UDP headers + payload).

For hop-by-hop and destination options headers, when required multiple PadN options were used in order to bypass some Linux kernels that consider a PadN larger than 8 bytes is an attack, see section 5.3 of {{?BCP220}}, even if multiple PadN options violates section 2.1.9.5 of {{?RFC4942}}.

Next phases will also include packets without UDP/TCP but with Next-Header being:

- 59, "no next header" see section 4.7 of {{!RFC8200}};

- 143, "ethernet" see section 4.9 of {{!RFC8986}}.

### Drop attribution to AS
Comparing the traceroutes without extension headers and with extension headers allow the attribution of a packet drop to one AS. But, this is not an easy task as inter-AS links often use IPv6 address of only one AS (if not using link-local per {{?RFC7704}}). This document uses the following algorithm to attribute the drop to one AS for packet sourced in one AS and then having a path traversing AS#foo just before AS#bar:

- if the packet drop happens at the first router (i.e., hop limit == 1 does not trigger an ICMP hop-limit exceeded), then the drop is assumed to this AS as it is probably an ingress filter on the first router (i.e., the hosting provider in most of the cases - except if colocated with an IXP)

- if the packet drop happens in AS#foo after one or more hop(s) in AS#bar, then the drop is assumed to be in AS#foo ingress filter on a router with an interface address in AS#foo

- if the packet drop happens in AS#bar after one or more hop(s) in AS#bar before going to AS#foo, then the drop is assumed to be in AS#foo ingress filter on a router with an interface address in AS#bar

In several cases, the above algorithm was not possible (e.g., some intermediate routers do not generate an ICMP unreachable hop limit exceeded), then the drop is not attributed. Please also note that the goal of this document is to 'point fingers to operators' but more to evaluate the potential impact. I.e., a tier-1 provider dropping packets with extension headers has a much bigger impact on the Internet traffic than an access provider.

## Results

This section presents the current results out of phase 1 (collaborating vanytage points) testing.

Packets with some extension headers were never dropped over the Internet: packets with authentication, fragmentation (non-atomic fragments), and routing (type different from 0 and 4) headers can freely traverse the global Internet without being dropped.

The table below lists the few AS that drops packets with the routing header type 0.

{::include ./drop_rh0_as.inc}

It is possibly due to a strict implementation of {{?RFC5095}} but it is expected that no packet with routing header type 0 would be transmitted anymore. Other routing header types (mobile IPv6 {{?RFC6275}}, RPL {{?RFC6554}}, SRH {{?RFC8754}}, and even CRH-16 and CRH-32{{?I-D.draft-bonica-6man-comp-rtg-hdr}}) can be transmitted over the global Internet without being dropped.

Some ASs drop packets with hop-by-hop or destination options extension headers, see the following table:

{::include ./drop_hbh_dest_as.inc}

The above list seems to include only access providers and no major tier providers.

Finally, some ASs do not drop transit traffic (except for routing header type 0) and follow the recommendations of {{?I-D.draft-ietf-opsec-ipv6-eh-filtering}}. This list includes tier-1 transit providers (using the "regional" tag per {{TIER1}}):

{::include ./no_drop.inc}

# Security Considerations

While active probing of the Internet may be considered as an attack, this measurement was done among collaborating parties and using the probe attribution technique described in {{?I-D.draft-vyncke-opsec-probe-attribution}}.


# IANA Considerations

This document has no IANA actions.

--- back

# Acknowledgments
{:numbered="false"}

The authors want to thank Sander Steffann and Jan Zorz for allowing the use of their labs. Other to Fernando Gont who indicated a nice IPv6 hosting provider in South America.

Special thanks as well to professor Benoît Donnet for his support and advices. This document would not have existed without his support.
