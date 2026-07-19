---
title: "Architectural decision"
source: "https://en.wikipedia.org/wiki/Architectural_decision"
author:
  - "[[Wikipedia]]"
published: 2016-08-23
created: 2026-07-19
description:
tags:
  - "clippings"
processed: true
---
In [software engineering](https://en.wikipedia.org/wiki/Software_engineering "Software engineering") and [software architecture](https://en.wikipedia.org/wiki/Software_architecture "Software architecture") design, **architectural decisions** are design decisions that address [architecturally significant requirements](https://en.wikipedia.org/wiki/Architecturally_significant_requirements "Architecturally significant requirements"); they are perceived as hard to make [^1] and/or costly to change.[^2]

## Characteristics

Architectural decisions influence and impact the [non-functional characteristics](https://en.wikipedia.org/wiki/Non-functional_requirement "Non-functional requirement") of a system. Each architectural decision describes a concrete, architecturally significant design issue (a.k.a. design problem, decision required) for which several potential solutions (a.k.a. options, alternatives) exist. An architectural decision captures the result of a conscious, often collaborative option selection process and provides [design rationale](https://en.wikipedia.org/wiki/Design_rationale "Design rationale") for the decision making outcome, e.g., by referencing one or more of the quality attributes addressed by the architectural decision and answering "why" questions about the design and option selection. Architectural decisions concern a [software system](https://en.wikipedia.org/wiki/Software_system "Software system") as a whole, or one or more of the core components of such a system. Types of architectural decisions are the selection of architectural tactics and patterns, of integration technologies, and of [middleware](https://en.wikipedia.org/wiki/Middleware "Middleware"), as well as related implementation strategies and assets (both commercial products and open source projects).[^3]

Software architecture design is a [wicked problem](https://en.wikipedia.org/wiki/Wicked_problem "Wicked problem"),[^4] therefore architectural decisions are difficult to get right. Often, no single optimal solution for any given set of architecture design problems exists. Architectural decision making is a core responsibility of software architects;[^5] additional motivation for/of the importance of architectural decisions as a first-class concept in software architecture can be found online.[^6]

## History

Rationale was mentioned in an early definition of [software architecture](https://en.wikipedia.org/wiki/Software_architecture "Software architecture") by Perry/Woolf,[^7] but not researched much until 2004, when a workshop on architectural decisions and Architectural [Knowledge Management](https://en.wikipedia.org/wiki/Knowledge_management "Knowledge management") was held in Groningen, NL. Early publications can be traced back to this workshop.[^8] [^9] From 2006 on, the architectural knowledge management and architectural decision research communities gained momentum and a number of papers was published at major software architecture conferences such as European Conference on Software Architecture (ECSA), Quality of Software Architecture (QoSA) and (Working) International Conference on Software Architecture (ICSA). A Springer book summarized the state of the art as of 2009,[^10] and a systematic mapping study from 2013 [^11] compiles and analyzes more and more recent research results.

In practice, the importance of making the correct decisions has always been recognized, for instance in software development processes such as OpenUP; many templates and practices for decision documentation exist. Seven of these templates are compared in.[^12] The most recent standard for architecture descriptions, [ISO/IEC/IEEE 42010:2011](https://en.wikipedia.org/wiki/ISO/IEC_42010 "ISO/IEC 42010") has a dedicated rationale entity, and gives detailed recommendations which architectural decisions to capture and which properties of an architectural decision to record in the decision log.[^13]

## Decision management steps

### Decision identification

Before a decision can be made, the need for a decision must be articulated: how urgent and how important is the AD? Does it have to be made now or can it wait until more is known about requirements and system under construction? Both personal and collective experience, as well as recognized design methods and practices, can assist with decision identification; it has been proposed that [Agile software development](https://en.wikipedia.org/wiki/Agile_software_development "Agile software development") team should maintain a *decision backlog* complementing the product backlog of the project.[^14]

### Decision making

Identified decisions can only be made if certain criteria are met, which form a definition of ready for AD making: (1) Stakeholders have been identified, (2) Time is right, (3) Alternatives (aka options) listed, (4) Requirements and other criteria defined, (5) ADR Template chosen.[^15]

A number of decision making techniques exists, both general ones and software and software architecture specific ones, for instance, [dialogue mapping](https://en.wikipedia.org/wiki/Dialogue_mapping "Dialogue mapping").[^16] *Group decision making* is an active research topic.

### Decision documentation

Many templates and tools for decision capturing exist, both in agile communities (e.g., M. Nygard's architecture decision records [^17]) and in software engineering and architecture design methods (e.g., see table layouts suggested by IBM UMF [^18] and by Tyree and Akerman from CapitalOne [^19]). G. Fairbanks included decision rationale in his one-page Architecture Haikus;[^20] his notation was later evolved into Y-statements. See [^21] for motivation, examples, comparisons.

### Decision enactment (enforcement)

Architectural decisions are used in [software design](https://en.wikipedia.org/wiki/Software_design "Software design"); hence they have to be communicated to, and accepted by, the stakeholders of the system that fund, develop, and operate it. *Architecturally evident coding styles* [^22] and [code reviews](https://en.wikipedia.org/wiki/Code_reviews "Code reviews") that focus on architectural concerns and decisions are two related practices.

Architectural decisions also have to be considered when modernizing a software system in [software evolution](https://en.wikipedia.org/wiki/Software_evolution "Software evolution").

### Decision sharing (optional step)

Architectural decisions often recur across projects, so experience from past decisions can be reused within a structured knowledge management approach.[^23]

It is important to know when a single architectural decision can be considered done. Five elements of a definition of done have been proposed: evidence, criteria, agreement, documentation, realization/review.[^24]

## Examples

On large scale projects, the number of architectural decisions to be made can exceed 100, including:

- Selection of architectural layering scheme and individual layer responsibilities (when adopting the Layers pattern from [^25])
- Choice of implementation technology per layer, component, and connector (e.g., programming language, interface contract format, [XML](https://en.wikipedia.org/wiki/XML "XML") vs. [JSON](https://en.wikipedia.org/wiki/JSON "JSON") when designing integration interfaces and message exchanges)
- Choice of presentation layer frameworks on client side (e.g., JavaScript frameworks) and on the server side (e.g., Java and PHP frameworks)

Refer to the design concept catalogs in Attribute-Driven Design 3.0 [^26] and domain-specific decision guidance models [^27] for more examples.

This is an example of a decision made, which is formatted according to the Y-statement template proposed in:[^28]

*“In the context of the Web shop service, facing the need to keep user session data consistent and current across shop instances, we decided for the Database Session State Pattern (and against Client Session State or Server Session State) [^29] to achieve cloud elasticity, accepting that a session database needs to be designed, implemented, and replicated.”*

## Templates

Many templates have been suggested by practicing architects and by software architecture researchers. [GitHub](https://en.wikipedia.org/wiki/GitHub "GitHub") repositories such as "Architecture decision record (ADR)" [^30] and "Markdown Architectural Decision Records" [^31] collect many of them, as well as links to tools and writing hints.

## Software architecture group decision making

Both practitioners and researchers recognize that software architecture decision-making is a group process that involves several stakeholders discussing, evaluating and shortlisting architectural decisions. Studies [^32] [^33] of practitioners found that though groups are ideally sized, a structured approach to decision-making is largely lacking. Specifically:

- There is a predominance of unstructured approach to decision-making. This limits the participation of group members.
- There is a lack of collaborative tool support to assist architects in the decision-making process.
- Architects often experience delays and omissions in the decision-making process due to lack a of a structured approach
- Architecting teams experience challenges including [groupthink](https://en.wikipedia.org/wiki/Groupthink "Groupthink") and [group polarization](https://en.wikipedia.org/wiki/Group_polarization "Group polarization")

These challenges provide good scope for experimentation and research for the software architecture community.

[^1]: Fowler, M. (2003). "Design – Who needs an architect?". IEEE Software. 20 (5): 11–44. doi:10.1109/MS.2003.1231144

[^2]: Booch, G., [abstracting-the-unknown](https://saturn2016.sched.org/event/63lK/keynote-abstracting-the-unknown), SATURN 2016 keynote

[^3]: Page 64 in O. Zimmermann, Architectural Decisions as Reusable Design Assets. IEEE Software, Volume 28, Issue 1, Pages 64-69, Jan./Feb. 2011.

[^4]: Conklin, Jeffrey (2006). Dialogue mapping: building shared understanding of wicked problems. Chichester, England: Wiley Publishing. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0470017686](https://en.wikipedia.org/wiki/Special:BookSources/0470017686 "Special:BookSources/0470017686").

[^5]: Kruchten, P., [What do software architects really do?](https://pkruchten.files.wordpress.com/2010/05/kruchten_2008_journal-of-systems-and-software.pdf), The Journal of Systems and Software 81 (2008) 2413–2416

[^6]: Hohpe, G., [Is This Architecture? Look for Decisions!](https://www.enterpriseintegrationpatterns.com/ramblings/86_isthisarchitecture.html)

[^7]: Perry, D. E.; Wolf, A. L. (1992). "Foundations for the study of software architecture" (PDF). ACM SIGSOFT Software Engineering Notes. 17 (4): 40. doi:10.1145/141874.141884

[^8]: Jansen, A.; Bosch, J. (2005). "Software Architecture as a Set of Architectural Design Decisions". 5th Working IEEE/IFIP Conference on Software Architecture (WICSA'05)

[^9]: Kruchten, Philippe, Patricia Lago, and [Hans Van Vliet](https://en.wikipedia.org/wiki/Hans_Van_Vliet "Hans Van Vliet"). " [Building up and reasoning about architectural knowledge](http://www.dimap.ufrn.br/~thais/MES20072/SoftwareArchitecturalGeneralModel.pdf)." *Quality of Software Architectures.* Springer Berlin Heidelberg, 2006. 43-58.

[^10]: Babar, M.A.; Dingsøyr, T.; Lago, P.; Vliet, H. van (2009). Software Architecture Knowledge Management: Theory and Practice (eds.), First Edition. Springer.

[^11]: Li, Z., Liang, P., Avgeriou, P., Application of Knowledge-based Approaches in Software Architecture: A Systematic Mapping Study, Information and Software Technology, Volume 55, Issue 5, May 2013, Pages 777-794, Elsevier.

[^12]: Zimmermann, O., Wegmann, L., Koziolek, H., Goldschmidt, T., [Architectural Decision Guidance across Projects](http://www.ifs.hsr.ch/fileadmin/user_upload/customers/ifs.hsr.ch/Home/projekte/ADMentor-WICSA2015ubmissionv11nc.pdf), Proc. of. IEEE/IFIP WICSA 2015

[^13]: [ISO/IEC/IEEE 42010:Templates for using the Standard](http://www.iso-architecture.org/42010/templates/).

[^14]: Hofmeister, C., Kruchten, P., Nord, R., Obbink, H.; Ran, A., America, P. (2007), A general model of software architecture design derived from five industrial approaches.

[^15]: O. Zimmermann (2023). A Definition of Ready for Architectural Decisions, [https://medium.com/olzzio/a-definition-of-ready-for-architectural-decisions-ads-2814e399b09b](https://medium.com/olzzio/a-definition-of-ready-for-architectural-decisions-ads-2814e399b09b)

[^16]: Conklin, Jeffrey (2006). Dialogue mapping: building shared understanding of wicked problems. Chichester, England: Wiley Publishing. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0470017686](https://en.wikipedia.org/wiki/Special:BookSources/0470017686 "Special:BookSources/0470017686").

[^17]: M. Nygard, [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html)

[^18]: Zimmermann, O., [An Architectural Decision Modeling Framework for SOA and Cloud Design](https://resources.sei.cmu.edu/library/asset-view.cfm?assetid=22124), SEI SATURN 2010 presentation.

[^19]: Tyree, J., Akerman, A., [Architecture decisions: demystifying architecture](https://ieeexplore.ieee.org/xpl/articleDetails.jsp?arnumber=1407822)

[^20]: G. Fairbanks, Architecture Haiku, [http://www.slideshare.net/matthewmccullough/architecture-haiku](https://www.slideshare.net/matthewmccullough/architecture-haiku)

[^21]: T. van Lessen, A Brief Introduction to ADRs, [https://speakerdeck.com/vanto/a-brief-introduction-to-architectural-decision-records](https://speakerdeck.com/vanto/a-brief-introduction-to-architectural-decision-records)

[^22]: Fairbanks, G., [An architecturally-evident coding style: making your design visible in your code](http://dl.acm.org/citation.cfm?id=1869542.1869627&coll=DL&dl=GUIDE), Proc. of OOPSLA 2010

[^23]: Babar, M.A.; Dingsøyr, T.; Lago, P.; Vliet, H. van (2009). Software Architecture Knowledge Management:Theory and Practice (eds.), First Edition. Springer.

[^24]: O. Zimmermann (2020). A Definition of Done for Architectural Decisions, [https://medium.com/olzzio/a-definition-of-done-for-architectural-decisions-426cf5a952b9](https://medium.com/olzzio/a-definition-of-done-for-architectural-decisions-426cf5a952b9)

[^25]: Buschmann, Frank; Meunier, Regine; Rohnert, Hans; Sommerlad, Peter (1996). Pattern-Oriented Software Architecture, Volume 1: A System of Patterns. John Wiley & Sons. [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [0-471-95869-7](https://en.wikipedia.org/wiki/Special:BookSources/0-471-95869-7 "Special:BookSources/0-471-95869-7").

[^26]: H. Cervantes, R. Kazman, Designing Software Architectures: A Practical Approach, Addison-Wesley, 2016.

[^27]: Page 21 in Zimmermann, O., Guidance Models and Decision-Making Tooling for SOA, Cloud, and Outsourcing Solution Design, [https://resources.sei.cmu.edu/asset\_files/Presentation/2011\_017\_001\_24654.pdf](https://resources.sei.cmu.edu/asset_files/Presentation/2011_017_001_24654.pdf)

[^28]: Uwe Zdun et al., Sustainable Architectural Design Decisions, IEEE Software, Volume 30, Number 6 (2013), available at [http://www.infoq.com/articles/sustainable-architectural-design-decisions](http://www.infoq.com/articles/sustainable-architectural-design-decisions)

[^29]: M. Fowler,[Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/)

[^30]: J. Parker-Hernderson, Architecture decision record (ADR), [https://github.com/joelparkerhenderson/architecture\_decision\_record](https://github.com/joelparkerhenderson/architecture_decision_record)

[^31]: ADR organization,[Markdown Architectural Decision Records](https://github.com/adr/madr)

[^32]: Rekhav, V. Smrithi; Muccini, Henry (April 2014). "A Study on Group Decision-Making in Software Architecture". *2014 IEEE/IFIP Conference on Software Architecture*. pp. 185–194. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1109/WICSA.2014.15](https://doi.org/10.1109%2FWICSA.2014.15). [ISBN](https://en.wikipedia.org/wiki/ISBN_\(identifier\) "ISBN (identifier)") [978-1-4799-3412-6](https://en.wikipedia.org/wiki/Special:BookSources/978-1-4799-3412-6 "Special:BookSources/978-1-4799-3412-6"). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [17362075](https://api.semanticscholar.org/CorpusID:17362075).

[^33]: V, Smrithi Rekha; Muccini, Henry (1 September 2018). ["Group decision-making in software architecture: A study on industrial practices"](https://www.sciencedirect.com/science/article/abs/pii/S0950584918300740). *Information and Software Technology*. **101**: 51–63. [doi](https://en.wikipedia.org/wiki/Doi_\(identifier\) "Doi (identifier)"):[10.1016/j.infsof.2018.04.009](https://doi.org/10.1016%2Fj.infsof.2018.04.009). [ISSN](https://en.wikipedia.org/wiki/ISSN_\(identifier\) "ISSN (identifier)") [0950-5849](https://search.worldcat.org/issn/0950-5849). [S2CID](https://en.wikipedia.org/wiki/S2CID_\(identifier\) "S2CID (identifier)") [49384683](https://api.semanticscholar.org/CorpusID:49384683).