# 5. Technology comparison

Status: **v0.1 draft by the architect, to be confirmed with the supervisor.** Scores are the team's qualitative assessment
(1 = poor fit, 5 = strong fit) against project requirements; they are not benchmarks. Weights reflect the requirements in
[06-requirements-specification.md](06-requirements-specification.md). Team familiarity must be confirmed by each member
before the decision is final.

## 5.1 Decision criteria (from requirements)
| Code | Criterion | Linked requirements | Weight |
|---|---|---|---|
| K1 | Fit for data/ML-adjacent logic (KPI maths, rules, CSV import) | FR-05..FR-09 | 3 |
| K2 | Data integrity & relational queries (players, teams, history) | FR-01..FR-04, NFR-04 | 3 |
| K3 | Development speed / learning curve for a 2-person team | NFR-09 | 3 |
| K4 | Testability & tooling (automated tests, API docs) | NFR-07, NFR-08 | 2 |
| K5 | Security & access control support | NFR-02, NFR-03 | 2 |
| K6 | Operational simplicity (deploy locally / one small server) | NFR-10 | 2 |

## D1. Server platform
| Alternative | K1 | K2 | K3 | K4 | K5 | K6 | Weighted | Notes |
|---|---|---|---|---|---|---|---|---|
| **A. Python + FastAPI** | 5 | 4 | 4 | 5 | 4 | 4 | **66** | Pydantic validation, auto-generated OpenAPI, rich data libraries (pandas) for KPI maths |
| B. Java + Spring Boot | 3 | 5 | 3 | 4 | 5 | 3 | 56 | Mature, strong typing/security; heavier setup; slower iteration for data logic |
| C. Node.js (TypeScript) + NestJS | 3 | 4 | 4 | 4 | 4 | 4 | 58 | Same language as frontend; weaker data-processing ecosystem |

Weighted = sum(weight x score). **Proposed: A (FastAPI).** Risk: less enforced structure than Spring/Nest - mitigate with layered modules and tests.

## D2. Data storage
| Alternative | K1 | K2 | K3 | K4 | K5 | K6 | Weighted | Notes |
|---|---|---|---|---|---|---|---|---|
| **A. PostgreSQL** | 4 | 5 | 4 | 4 | 4 | 4 | **63** | Relational integrity, constraints, JSON columns for flexible metrics, window functions for trends |
| B. MongoDB | 3 | 3 | 4 | 3 | 3 | 3 | 49 | Flexible schema, but player/team/test relations and consistency matter more here |
| C. SQLite | 3 | 3 | 5 | 4 | 2 | 5 | 51 | Excellent for local prototypes/tests; weaker for multi-user concurrent access |

**Proposed: A (PostgreSQL)**; SQLite allowed for unit tests.

## D3. Method of component interaction (client <-> backend)
| Alternative | K1 | K2 | K3 | K4 | K5 | K6 | Weighted | Notes |
|---|---|---|---|---|---|---|---|---|
| **A. REST/JSON over HTTPS (OpenAPI)** | 4 | 4 | 5 | 5 | 4 | 5 | **70** | Simple, tool support, contract-first via [api/openapi.yaml](../api/openapi.yaml) |
| B. GraphQL | 4 | 4 | 3 | 4 | 3 | 3 | 54 | Flexible queries; extra complexity for a small, well-known set of resources |
| C. gRPC | 3 | 3 | 2 | 4 | 4 | 3 | 46 | Efficient binary RPC; poor fit for browser clients without a proxy |

**Proposed: A (REST/JSON).**

## D4. Recommendation method
| Alternative | Transparency | Works with little data | Coach acceptance | Effort | Verdict |
|---|---|---|---|---|---|
| **A. Knowledge-based rules (configurable) + explanation** | High | **Yes** | High (rules reviewable by coaches) | Medium | **Core** |
| B. Supervised ML (e.g. gradient boosting) | Low-medium | No - needs labelled outcomes we do not have | Uncertain | High | Stretch, only if data exist |
| C. Hybrid (rules + ML re-ranking) | Medium | Partly | Medium | High | Future work |

Rationale from literature: ML in sport often has small, biased data and rare external validation [S3, S6]; recommender research asks for explanations [S7].

## D5. Web client
| Alternative | Notes | Verdict |
|---|---|---|
| **A. React + TypeScript (SPA, responsive)** | Large ecosystem, component libraries, mobile-friendly | **Proposed** |
| B. Vue 3 | Gentle learning curve; smaller ecosystem for team | Alternative |
| C. Server-rendered templates (Jinja/HTMX) | Fewer moving parts; less interactive charts | Fallback if time is short |

## 5.2 Summary of proposed stack
FastAPI (Python 3.12) - PostgreSQL - REST/OpenAPI - rule engine in a separate, framework-independent module - React + TypeScript - pytest - GitHub Actions CI.
Decisions are recorded as ADRs in [adr/](adr/).
