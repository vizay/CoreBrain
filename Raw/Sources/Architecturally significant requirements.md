---
title: "Architecturally significant requirements"
source: "https://en.wikipedia.org/wiki/Architecturally_significant_requirements"
author:
  - "[[Wikipedia]]"
published: 2016-04-02
created: 2026-07-19
description:
tags:
  - "clippings"
---
**Architecturally significant requirements** are those requirements that have a measurable effect on a computer system’s [architecture](https://en.wikipedia.org/wiki/Software_architecture "Software architecture").[^1] This can comprise both software and hardware requirements. They are a subset of [requirements](https://en.wikipedia.org/wiki/Software_requirement "Software requirement") that affect a system architecture in measurably identifiable ways.

## Relation to non-functional requirements and quality attributes

Architecturally significant requirements were only recently, as of 2016, recognized as an important notion. When discussing architecture, the terms [non-functional requirements](https://en.wikipedia.org/wiki/Non-functional_requirement "Non-functional requirement") or [quality attributes](https://en.wikipedia.org/wiki/List_of_system_quality_attributes "List of system quality attributes") are often used.[^2] However, recent empirical studies show that, for a [software system](https://en.wikipedia.org/wiki/Software_system "Software system"), not all non-functional requirements affect its [architecture](https://en.wikipedia.org/wiki/Software_architecture "Software architecture"), and functional [requirements](https://en.wikipedia.org/wiki/Software_requirement "Software requirement") can also affect its architecture.[^1] [^3] This research suggests distinguishing which software requirements are architecturally significant and whether they are functional when discussing software architecture is worth it.[^3]

## Characteristics

Architecturally significant requirements can be characterized by the following aspects.[^1]

### Descriptive characteristics

Architecturally significant requirements are often hard to define and articulate, tend to be expressed vaguely, tend to be initially neglected, tend to be hidden within other requirements, and are subjective, variable, and situational. Other requirements could also demonstrate these descriptive characteristics. However, architecturally significant requirements’ significance made these manifestations unique and challenging.

### Indicators

A requirement with a broad effect targets trade-off points, is strict (constraining, limiting, non-negotiable), assumption-breaking, or difficult to achieve, and is likely to be architecturally significant.

Indicators of architectural significance that have been reported in the literature include:

- The requirement is associated with high business value and/or technical risk.
- The requirement is a concern of a particularly influential stakeholder.
- The requirement has a first-of-a-kind character, e.g. none of the responsibilities of existing components in the architecture address it.
- The requirement has QoS/SLA characteristics that deviate from those already satisfied by the evolving architecture.
- The requirement has caused budget overruns or client dissatisfaction in a previous project with a similar context.

The OpenUP [^4] and Peter Eeles [^5] discuss additional criteria for architectural significance in several articles and presentations. Seven criteria for architectural significance were addressed at the European Conference on Software Architecture in 2020: business value/risk, stakeholder concern, quality level, external dependencies, cross-cutting, first-of-a-kind, and source of problems on past projects.

### Heuristics

When a requirement specifies a [software system](https://en.wikipedia.org/wiki/Software_system "Software system") ’s [quality attributes](https://en.wikipedia.org/wiki/Quality_attributes "Quality attributes"), refers to its core features, imposes constraints on it, or defines the environment in which it will run, it is likely to be architecturally significant.

See discussion of design vs. architecture under [software architecture](https://en.wikipedia.org/wiki/Software_architecture "Software architecture") for additional criteria of architectural significance.

## Elicitation

Like all non-functional requirements and quality attributes,[^6] architecturally significant requirements should be specified [SMART](https://en.wikipedia.org/wiki/SMART_criteria "SMART criteria"). Quality attribute scenarios [^2] are one way to achieve the S (specific) and the M (measured) criteria in SMART. The [Software Engineering Institute](https://en.wikipedia.org/wiki/Software_Engineering_Institute "Software Engineering Institute") recommends Quality Attribute Workshops for this effort.[^7] It has been suggested that architecture analysis and design be kept lightweight and flexible; quality attribute trees for specific application genres and technology domains can support such approaches.[^8]

Communicating the elicited architecturally significant requirements and any other architectural artifacts in a comprehensible notation and language for the [target audience](https://en.wikipedia.org/wiki/Target_audience "Target audience") (particularly business [stakeholders](https://en.wikipedia.org/wiki/Stakeholder_theory "Stakeholder theory")) is essential.[^9]

## Impact

Architecturally significant requirements are used in [software design](https://en.wikipedia.org/wiki/Software_design "Software design") to drive and justify [architectural decisions](https://en.wikipedia.org/wiki/Architectural_decision "Architectural decision"); if not satisfied properly, they contribute to the accumulation of [technical debt](https://en.wikipedia.org/wiki/Technical_debt "Technical debt"). For instance, failure to meet security and compliance requirements complicates the system and process assurance audits and increases the risk of audit findings.[^10] Exemplary advice on addressing system quality attributes (including architecturally significant requirements) is available in the literature.[^11] [^12]

[^1]: Chen, Lianping; Ali Babar, Muhammad; Nuseibeh, Bashar (2013). "Characterizing Architecturally Significant Requirements". *IEEE Software*. **30** (2): 38–45. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2013ISoft..30b..38C](https://ui.adsabs.harvard.edu/abs/2013ISoft..30b..38C). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/MS.2012.174](https://doi.org/10.1109%2FMS.2012.174). [hdl](https://en.wikipedia.org/wiki/Hdl_\(identifier\) "Hdl (identifier)"):[10344/3061](https://hdl.handle.net/10344%2F3061). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [17399565](https://api.semanticscholar.org/CorpusID:17399565).

[^2]: Bass, Len; Clements, Paul (2003). *Software Architecture in Practice*. Addison Wesley. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-0321154958](https://en.wikipedia.org/wiki/Special:BookSources/978-0321154958 "Special:BookSources/978-0321154958").

[^3]: Eckhardt, Jonas; Vogelsang, Andreas; Fernández, Daniel (2016). [*Are "Non-functional" Requirements really Non-functional? - An Investigation of Non-functional Requirements in Practice*](https://www4.in.tum.de/~vogelsan/publications/ICSE16.pdf) (PDF). [The 38th International Conference on Software Engineering](http://2016.icse.cs.txstate.edu/). Association for Computing Machinery.

[^4]: ["Concept: Architecturally Significant Requirements"](https://web.archive.org/web/20161017101618/http://epf.eclipse.org/wikis/openup/core.tech.common.extend_supp/guidances/concepts/arch_significant_requirements_1EE5D757.html). Archived from [the original](https://epf.eclipse.org/wikis/openup/core.tech.common.extend_supp/guidances/concepts/arch_significant_requirements_1EE5D757.html) on October 17, 2016. Retrieved August 19, 2016.

[^5]: ["Peter Eeles on ResearchGate"](https://www.researchgate.net/profile/Peter-Eeles-2).

[^6]: ["Quality Attributes"](https://web.archive.org/web/20121016131907/http://www.sei.cmu.edu/reports/95tr021.pdf) (PDF). *sei.cmu.edu*. Archived from [the original](http://www.sei.cmu.edu/reports/95tr021.pdf) (PDF) on October 16, 2012.

[^7]: ["The SEI Quality Attribute Workshop"](http://www.sei.cmu.edu/architecture/tools/establish/qaw.cfm). February 8, 2018.

[^8]: Keeling, Michael (2015). ["Lightweight and Flexible: Emerging Trends in Software Architecture from the SATURN Conferences"](https://doi.org/10.1109%2FMS.2015.65). *IEEE Software*. **32** (3): 7–11. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2015ISoft..32c...7K](https://ui.adsabs.harvard.edu/abs/2015ISoft..32c...7K). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/MS.2015.65](https://doi.org/10.1109%2FMS.2015.65).

[^9]: Schulenklopper, Jochem (2016). "Why They Just Don't Get It: Communicating about Architecture with Business Stakeholders". *IEEE Software*. **33** (3): 13–19. [Bibcode](https://en.wikipedia.org/wiki/Bibcode_\(identifier\) "Bibcode (identifier)"):[2016ISoft..33c..13S](https://ui.adsabs.harvard.edu/abs/2016ISoft..33c..13S). [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/MS.2016.67](https://doi.org/10.1109%2FMS.2016.67). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [1309474](https://api.semanticscholar.org/CorpusID:1309474).

[^10]: K. Julisch et al., [Compliance by design - Bridging the chasm between auditors and IT architects](http://soadecisions.org/download/ComplianceByDesign-AAM.pdf) [Archived](https://web.archive.org/web/20170921213138/http://soadecisions.org/download/ComplianceByDesign-AAM.pdf) 2017-09-21 at the [Wayback Machine](https://en.wikipedia.org/wiki/Wayback_Machine "Wayback Machine") Computers & Security 30(6-7): 410-426 (2011)

[^11]: ["Implementing System-Quality Attributes"](https://msdn.microsoft.com/en-us/library/bb402962.aspx).

[^12]: A. Rotem-Gal-Oz, SOA Patterns, Manning, 2012.