# 1. Project proposal and scope

| Item | Value |
|---|---|
| **Title** | Development of a Youth Football Performance Monitoring and Training Recommendation System |
| **Title (RU)** | Разработка системы мониторинга игровых показателей и формирования рекомендаций по тренировкам юных футболистов |
| **Programme** | Software Engineering, Astana IT University |
| **Team** | Sergey Nurtilek (SE-2419) - sports analyst / methodologist; Aidyn Zhubanyshev (SE-2417) - full-stack developer / software architect |
| **Supervisor** | Rakhym Akbota |
| **Status** | Pre-defense 1 (24 October 2026) - analysis, design and planning stage |

## 1.1 Problem statement
Training in youth football in Kazakhstan is, to a large extent, still tracked informally (paper notes,
messengers, spreadsheets) and judged by a coach's experience. As a result, individual player data are
scattered, hard to compare over time, and rarely turned into concrete, individualised training decisions.

The scientific literature points to the same gap on the international level: monitoring of football players is
*fragmented*, only a few studies use multivariate approaches, and youth and sub-elite players are the least
covered group ([Afonso et al., 2025](03-literature-review.md#references) - S1). GPS-based monitoring of youth players lacks
standard variable definitions and thresholds (S2), and biological maturity changes what a given workload
means for a young player (S4, S5). Commercial tools (see [existing-system comparison](04-existing-systems-comparison.md))
are either hardware-centred and aimed at professional teams, scouting-oriented, or club-administration tools.

> **Note on evidence.** Statements about the situation in Kazakhstan academies are the team's working
> hypotheses until confirmed by the interviews planned in [02-evidence-of-relevance.md](02-evidence-of-relevance.md).

## 1.2 Target users
| User | Need |
|---|---|
| **Youth coach** (primary) | Record sessions/tests quickly, see player trends, receive explainable recommendations |
| **Academy methodologist / analyst** | Define KPIs and norms per age group, review cohort-level reports |
| **Academy administrator** | Manage teams, players, coaches and access |
| _Player / parent_ (secondary, read-only, optional) | Understand progress |

## 1.3 Aim
Design and build a web-based decision-support system that collects training and match indicators of youth
football players, evaluates them against configurable age-group KPIs, and produces transparent training
recommendations for the coach.

## 1.4 Objectives
1. Analyse the domain and existing solutions; collect and verify requirements with coaches (3-5 discussions).
2. Formalise football norms into measurable KPIs and rule-based recommendation logic (age- and maturity-aware).
3. Specify requirements with priorities and acceptance criteria.
4. Design architecture, data model and API; prototype key coach scenarios.
5. Implement backend (API, database, KPI and recommendation engine) and a web client.
6. Evaluate in field conditions against a baseline (current coach practice) and report limitations.

## 1.5 Expected outcomes
* Validated KPI catalogue and recommendation rules (individual result: Sergey).
* Working backend, database, API, web client and technical documentation (individual result: Aidyn).
* Evaluation report: agreement with coach judgement, usability, efficiency vs. baseline.

## 1.6 Scope
**In scope**
* Player/team/coach management with role-based access.
* Entry and CSV import of: field tests (sprint, agility, jump, endurance), session load (session-RPE),
  attendance, wellness questionnaire, match indicators, anthropometrics for maturity estimation.
* KPI calculation per age group and player history; trends and cohort comparison.
* Rule-based recommendation engine with an explanation for every recommendation.
* Reports (screen, CSV/PDF export).

**Out of scope (for the diploma project)**
* Own hardware or computer-vision tracking; real-time GPS streaming.
* Medical diagnosis, injury treatment, or anything replacing a coach/medical specialist - the system is a
  **decision-support** tool only.
* Integration with the KFF Digital Football Hub (planned by the federation for 2025-2030; see
  [evidence](02-evidence-of-relevance.md)) - only an import/export-friendly design.
* Mobile native apps (responsive web only).

**Stretch (only if time allows):** ML-based ranking of recommendations (see [technology comparison](05-technology-comparison.md)).

## 1.7 Engineering complexity (why this is a diploma-level task)
* Domain-to-software mapping: sports norms -> formal, configurable, testable rules.
* Data model for heterogeneous, time-series player metrics with age/maturity context and data-quality control.
* Explainable recommendation engine with a traceable rule -> evidence -> recommendation chain.
* Privacy-aware handling of minors' data (anonymisation, roles, consent).
* Evaluation design with baseline and field testing.

## 1.8 Assumptions and constraints
* Primary input is manual/CSV entry; wearable hardware is optional and not required.
* Access to an academy/coaches for interviews and pilot data is needed (risk R1 in [project management](10-project-management.md)).
* Real player data are never committed to this repository.
