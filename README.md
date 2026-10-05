# Youth Football Performance Monitoring and Training Recommendation System

Diploma project, Software Engineering, Astana IT University.
_Разработка системы мониторинга игровых показателей и формирования рекомендаций по тренировкам юных футболистов._

**Status:** pre-defense 1 stage - analysis, design and planning complete; implementation not started (see [status](#current-status)).

## Problem statement
Monitoring of training and performance in youth football is often informal (paper, spreadsheets, coach judgement), so individual data are scattered,
hard to compare over time and rarely converted into individual training decisions. International reviews describe youth monitoring as fragmented and
non-standardised ([literature review](docs/03-literature-review.md)). Existing tools are hardware-centred, scouting-oriented or administrative
([comparison](docs/04-existing-systems-comparison.md)).

## Target users
Youth coaches (primary), academy methodologists/analysts, academy administrators; optionally players/parents (read-only).

## Expected outcomes
A web-based **decision-support** system that records field tests, session load, wellness and match indicators; computes age/maturity-aware KPIs;
and generates **explainable, rule-based training recommendations**; plus an evaluation against current coach practice.
It does not replace a coach or medical specialist.

## Team and supervisor
| Member | Role | Responsibilities |
|---|---|---|
| Sergey Nurtilek (SE-2419) | Sports analyst / methodologist | Domain analysis, coach requirements, KPI and rule definitions, field testing and validation, analytical reports |
| Aidyn Zhubanyshev (SE-2417) | Full-stack developer / architect | Architecture, backend, database, API, recommendation algorithms, integration, technical documentation |
| Supervisor | Rakhym Akbota | |

## Scope
In: team/player management, test/session/wellness/match data entry and CSV import, KPI computation, explainable rule-based recommendations, reports.
Out: own hardware, real-time GPS, medical diagnosis, KFF Hub integration (import/export-friendly only), native mobile apps. Details: [proposal](docs/01-project-proposal.md).

## Selected technologies (proposed, pending supervisor confirmation)
FastAPI (Python) - PostgreSQL - REST/OpenAPI - rule engine - React + TypeScript - pytest - GitHub Actions. Rationale: [technology comparison](docs/05-technology-comparison.md), [ADRs](docs/adr/).

## Links
* YouTrack: **TODO - add URL** (backlog to import: [docs/youtrack-backlog.csv](docs/youtrack-backlog.csv))
* Documentation index below; submission notes: [docs/submissions/pre-defense-1.md](docs/submissions/pre-defense-1.md)

## Documentation
| # | Document |
|---|---|
| 1 | [Project proposal and scope](docs/01-project-proposal.md) |
| 2 | [Evidence of relevance](docs/02-evidence-of-relevance.md) |
| 3 | [Literature review](docs/03-literature-review.md) ([table](docs/literature/literature-table.csv)) |
| 4 | [Existing system comparison](docs/04-existing-systems-comparison.md) |
| 5 | [Technology comparison](docs/05-technology-comparison.md) |
| 6 | [Requirements specification](docs/06-requirements-specification.md) |
| 7 | [Architecture and diagrams](docs/07-architecture-and-diagrams.md) (sources in [diagrams/src](diagrams/src)) |
| 8 | [UX / prototype](docs/08-ux-prototype.md) - open [prototype/wireframes.html](prototype/wireframes.html) |
| 9 | [Verification and evaluation plan](docs/09-verification-and-evaluation-plan.md) |
| 10 | [Project management and risks](docs/10-project-management.md) |
| 11 | [Supervisor feedback log](docs/11-supervisor-feedback.md) |
| - | [KPI catalogue and rules](docs/domain/kpi-catalogue.md), [API contract](api/openapi.yaml) |

## Repository structure
```
src/backend, src/frontend   application code (placeholders until implementation starts)
docs/                       proposal, literature review, comparisons, requirements, ADRs, plans
diagrams/src, exports       editable diagram sources (Mermaid, Graphviz) and SVG/PNG exports
api/                        OpenAPI contract and examples
prototype/                  clickable low-fidelity wireframes
tests/                      automated checks (pytest)
config/                     configuration examples (.env.example) and draft recommendation rules
data/synthetic/             synthetic test data only (never real player data)
```

## Current status
| Area | Status |
|---|---|
| Analysis, literature, comparisons | Done (draft); interviews pending |
| Requirements, architecture, prototype, verification plan | Done (draft v0.1) |
| Backend / client implementation | Not started (DIP-21..26) |
| Evaluation / pilot | Planned (DIP-27) |

## Setup, execution and testing
No runnable application yet. Automated deliverable checks:
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-dev.txt
pytest
```
View the prototype: open `prototype/wireframes.html` in a browser. Regenerate diagrams: see [docs/07](docs/07-architecture-and-diagrams.md).

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md): task branches `DIP-<id>-...`, PRs reviewed by the other member, tags `pre-defense-1`, `pre-defense-2`, `final-pre-defense`.
Never commit credentials or real player data.
