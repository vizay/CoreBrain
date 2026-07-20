---
title: "ADR Templates"
source: "https://adr.github.io/adr-templates/"
author:
  - "[[adr.github.io]]"
published: 2024-10-25
created: 2026-07-19
description: "The following UML class diagram shows that many templates for ADR capturing exist, including (but not limited to) MADR, Nygardian ADRs, and Y-Statements:"
tags:
  - "clippings"
---
The following UML class diagram shows that many templates for ADR capturing exist, including (but not limited to) MADR, Nygardian ADRs, and Y-Statements:

```
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
  direction TB
  class ADR {
    <<abstract>>
  }
  ADR <|-- MADR
  ADR <|-- NygardADR
  ADR <|-- Y-Statement
  ADR <|-- OtherADRTemplate
```
```
#mermaid-1784485566925{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#ccc;}#mermaid-1784485566925 .error-icon{fill:#a44141;}#mermaid-1784485566925 .error-text{fill:#ddd;stroke:#ddd;}#mermaid-1784485566925 .edge-thickness-normal{stroke-width:1px;}#mermaid-1784485566925 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1784485566925 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1784485566925 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1784485566925 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1784485566925 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1784485566925 .marker{fill:lightgrey;stroke:lightgrey;}#mermaid-1784485566925 .marker.cross{stroke:lightgrey;}#mermaid-1784485566925 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1784485566925 p{margin:0;}#mermaid-1784485566925 g.classGroup text{fill:#ccc;stroke:none;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:10px;}#mermaid-1784485566925 g.classGroup text .title{font-weight:bolder;}#mermaid-1784485566925 .nodeLabel,#mermaid-1784485566925 .edgeLabel{color:#e0dfdf;}#mermaid-1784485566925 .edgeLabel .label rect{fill:#1f2020;}#mermaid-1784485566925 .label text{fill:#e0dfdf;}#mermaid-1784485566925 .edgeLabel .label span{background:#1f2020;}#mermaid-1784485566925 .classTitle{font-weight:bolder;}#mermaid-1784485566925 .node rect,#mermaid-1784485566925 .node circle,#mermaid-1784485566925 .node ellipse,#mermaid-1784485566925 .node polygon,#mermaid-1784485566925 .node path{fill:#1f2020;stroke:#ccc;stroke-width:1px;}#mermaid-1784485566925 .divider{stroke:#ccc;stroke-width:1;}#mermaid-1784485566925 g.clickable{cursor:pointer;}#mermaid-1784485566925 g.classGroup rect{fill:#1f2020;stroke:#ccc;}#mermaid-1784485566925 g.classGroup line{stroke:#ccc;stroke-width:1;}#mermaid-1784485566925 .classLabel .box{stroke:none;stroke-width:0;fill:#1f2020;opacity:0.5;}#mermaid-1784485566925 .classLabel .label{fill:#ccc;font-size:10px;}#mermaid-1784485566925 .relation{stroke:lightgrey;stroke-width:1;fill:none;}#mermaid-1784485566925 .dashed-line{stroke-dasharray:3;}#mermaid-1784485566925 .dotted-line{stroke-dasharray:1 2;}#mermaid-1784485566925 #compositionStart,#mermaid-1784485566925 .composition{fill:lightgrey!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #compositionEnd,#mermaid-1784485566925 .composition{fill:lightgrey!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #dependencyStart,#mermaid-1784485566925 .dependency{fill:lightgrey!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #dependencyStart,#mermaid-1784485566925 .dependency{fill:lightgrey!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #extensionStart,#mermaid-1784485566925 .extension{fill:transparent!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #extensionEnd,#mermaid-1784485566925 .extension{fill:transparent!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #aggregationStart,#mermaid-1784485566925 .aggregation{fill:transparent!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #aggregationEnd,#mermaid-1784485566925 .aggregation{fill:transparent!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #lollipopStart,#mermaid-1784485566925 .lollipop{fill:#1f2020!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 #lollipopEnd,#mermaid-1784485566925 .lollipop{fill:#1f2020!important;stroke:lightgrey!important;stroke-width:1;}#mermaid-1784485566925 .edgeTerminals{font-size:11px;line-height:initial;}#mermaid-1784485566925 .classTitleText{text-anchor:middle;font-size:18px;fill:#ccc;}#mermaid-1784485566925 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}«abstract»ADRMADRNygardADRY-StatementOtherADRTemplate
```

## Markdown Architectural Decision Records (MADR)

MADR is about architectural decisions that *matter* ([`[ˈmæɾɚ]`](https://en.wiktionary.org/wiki/matter#Pronunciation)). Olaf Zimmermann’s [MADR Template Primer](https://www.ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html) covers it in more depth. You can use MADR without installing software by populating the template in any text editor. Additionally, a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=StevenChen.vscode-adr-manager) is available, though it may be outdated and lack support for the latest features. [Other tools](https://adr.github.io/adr-tooling/#madr-template) are also available.

MADR provides a [full](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1) and a [minimal](https://github.com/adr/madr/blob/4.0.0/template/adr-template-minimal.md?plain=1) template, both of which now come in an annotated and a bare format. The rationale for this decision is documented in the [template decisions](https://github.com/adr/madr/tree/4.0.0/template#decisions).

We think that the *considered options* with their pros and cons are crucial to understand the reasons for choosing a particular design. Therefore, the [Markdown Architectural Decision Records (MADR)](https://adr.github.io/madr/) project in this organization includes such tradeoff analysis information. It also suggests metadata such as decision makers and confirmation in addition to decision status.

## Nygard ADR

An ADR consists of title, status, context, decision, and consequences according to “Documenting Architecture Decisions” by [@mtnygard](https://github.com/mtnygard).

The original [blog post from 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) suggests this structure, and a [Markdown rendering](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md) is also available.

## Y-Statement

In short, the Y-statement is as follows:

> In the context of `<use case/user story>`, facing `<concern>` we decided for `<option>` to achieve `<quality>`, accepting `<downside>`.

The long form of it is as follows (extra section “because”):

> In the context of `<use case/user story>`, facing `<concern>`, we decided for `<option>` and neglected `<other options>`, to achieve `<system qualities/desired consequences>`, accepting `<downside/undesired consequences>`, because `<additional rationale>`.

cards42 has adopted the Y-statement template in its German [ADR card](https://cards42.org/#adr); the English version is similar, but adds state information. Finally, you can find more explanations and examples on Medium: [Y-Statements - A Light Template for Architectural Decision Capturing](https://medium.com/@docsoc/y-statements-10eb07b5a177).

## Other ADR templates

Numerous other ADR formats exist, many of which are also featured in [@joelparkerhenderson’s GitHub repository](https://github.com/joelparkerhenderson/architecture_decision_record).

The [template](http://www.iso-architecture.org/42010/templates/) for [ISO/IEC/IEEE 42010:2011](https://en.wikipedia.org/wiki/ISO/IEC_42010), the international standard for architecture descriptions of systems and software engineering, suggests nine information items for ADRs its Appendix A. It also identifies areas to consider when identifying key decisions.