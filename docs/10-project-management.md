# 10. Project management and risks

## 10.1 Links
* **Repository:** TODO - add GitHub/GitLab URL (private repo: grant access to supervisor and committee before each pre-defense).
* **YouTrack project:** TODO - add URL. Project short name proposed: `DIP`. Backlog to import: [youtrack-backlog.csv](youtrack-backlog.csv)
  (IDs, assignee, priority, deadline, acceptance criteria). Branches/commits use these IDs (see [CONTRIBUTING](../CONTRIBUTING.md)).
* **Supervisor:** Rakhym Akbota.

## 10.2 Responsibilities
| Member | Role | Responsibilities | Individual result |
|---|---|---|---|
| **Sergey Nurtilek** (SE-2419) | Sports analyst / methodologist | Domain analysis, coach requirements, football norms -> business rules, KPI and recommendation criteria, field tests and data validation, analytical reports, defence materials | Scientific-methodological base, validated KPI system, analytical reporting |
| **Aidyn Zhubanyshev** (SE-2417) | Full-stack developer / software architect | System architecture, backend and data processing, database and API, recommendation algorithms, integration, debugging, technical documentation | Working software, stable backend, structured DB, technical docs |
| Both | - | Cross-review of every pull request; weekly supervisor meeting; shared ownership of requirements and evaluation | - |

Which deliverable each member owns in this repository is visible in the git history (author of each commit) and the `Owner` lines of documents.

## 10.3 Milestones (proposed; align with the academic calendar and supervisor)
| Milestone | Target | Content |
|---|---|---|
| M0 Pre-defense 1 | 2026-10-24 | Analysis, design, planning deliverables (this repo, tag `pre-defense-1`) |
| M1 Evidence and requirements baseline | 2026-11 | Interviews done, requirements/prototype revised (DIP-16, 19, 20) |
| M2 Backend core | 2026-12 | DB, API, KPI engine, recommendation engine (DIP-21..25) |
| M3 Pre-defense 2 | date TBD | Working backend + prototype client, first evaluation results |
| M4 Client MVP and pilot | 2027-01..03 | DIP-26, DIP-27 |
| M5 Final pre-defense | date TBD | Evaluation report, thesis (DIP-28) |

## 10.4 Risks
| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|---|
| R1 | No academy/coaches available for interviews and pilot | Medium | High | Start outreach now; use Nurtilek's football network; fallback: expert panel + synthetic-realistic data (reported as limitation) | Nurtilek |
| R2 | Consent/privacy obstacles for minors' data | Medium | High | Pseudonymised IDs, academy-level consent, no real data in repo | Both |
| R3 | Thresholds/norms lack validated source | High | Medium | Mark placeholders, review with supervisor and coaches, calibrate with pilot | Nurtilek |
| R4 | Scope creep (ML, wearables, mobile apps) | Medium | Medium | Strict scope (proposal 1.6); stretch items only after Must done | Aidyn |
| R5 | Two-person bus factor / schedule slip | Medium | High | Weekly checkpoints, cross-review, backlog with deadlines | Both |
| R6 | Recommendations misread as medical/training prescriptions | Low | High | Disclaimer in UI/reports; wording "consider"; supervisor review of rule text | Nurtilek |
| R7 | Federation platforms (KFF Hub, EasyCoach) overlap or change | Low | Medium | Import/export-friendly design; follow KFF announcements | Aidyn |

## 10.5 Dependencies
Interviews -> requirements freeze -> backend design; KPI norms (DIP-23) -> KPI engine tests (DIP-22); rules (DIP-8) -> recommendation engine (DIP-24); access to academy -> pilot (DIP-27).

## 10.6 Next steps
Create YouTrack project and import backlog; push repo and give access; supervisor review (DIP-15); schedule interviews (DIP-16).
