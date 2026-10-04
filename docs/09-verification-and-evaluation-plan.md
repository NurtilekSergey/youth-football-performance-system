# 9. Verification and evaluation plan (draft v0.1)

Owner: S. Nurtilek (evaluation design), A. Zhubanyshev (automated tests). Targets marked *proposed* are to be agreed with the supervisor.

## 9.1 Aim to be demonstrated
The system helps coaches record youth-player data faster and produces explainable recommendations that coaches judge useful, compared with current practice.

## 9.2 Baselines
| ID | Baseline | Used for |
|---|---|---|
| B0 | Current coach practice (paper/spreadsheet + own judgement), documented in interviews I1-I4 | Data-entry time, usefulness |
| B1 | Naive rule: same generic training suggestion for every player of an age group (no individual data) | Recommendation relevance |

## 9.3 Outcome metrics and measurement conditions
| ID | Metric | How measured | Conditions | Target (proposed) | Req. |
|---|---|---|---|---|---|
| M1 | Acceptance-criteria pass rate | Automated + manual test run of all Must requirements | CI + staging | 100% of Must | all M |
| M2 | Coach agreement with recommendations | >= 3 coaches independently rate >= 30 player cases (anonymised, from pilot or synthetic-realistic data): relevant / not relevant; compare system vs B1; report % agreement and inter-rater agreement (Fleiss' kappa) | Blind to which source made the recommendation | System relevance > B1; report kappa | FR-13 |
| M3 | Decision distribution | Share of accepted / modified / rejected recommendations in pilot (FR-14) | Pilot period >= 4 weeks | Report; investigate rejected rules | FR-14 |
| M4 | Data-entry time | Median time to enter a 20-player session: system vs B0 (stopwatch) | >= 5 coaches or role-played sessions | <= 3 min and not slower than B0 | NFR-05 |
| M5 | Usability | SUS questionnaire | >= 5 coaches after task scenarios SC-1..SC-5 | mean SUS >= 68 | NFR-05 |
| M6 | API performance | Load test (e.g. Locust/k6), synthetic 500 players / 100k records | 50 concurrent users, reference laptop/VM | p95 <= 500 ms | NFR-01 |
| M7 | Explainability completeness | Automated check over all generated recommendations | Test suite | 100% contain rule ID, inputs, threshold, cohort, rationale | NFR-06 |
| M8 | KPI computation correctness | Unit tests vs hand-calculated reference dataset | CI | z-score error <= 0.01; coverage >= 80% on KPI/rule modules | FR-10, NFR-07 |
| M9 | Access control | Automated endpoint tests per role | CI | 100% endpoints covered | NFR-02 |

## 9.4 Test levels
Unit (KPI maths, rules, validators) - API/contract (OpenAPI conformance, RBAC) - integration (import -> KPI -> recommendation) - usability sessions - field pilot.
Test data: synthetic generator in `data/synthetic/` (committed); real data only with consent, anonymised, stored outside the repository.

## 9.5 Field pilot protocol (draft)
1. Agree with an academy/coach, obtain parental/academy consent for anonymised data.
2. Collect >= 4 weeks of sessions + one test battery per team (U13-U15).
3. Coaches review recommendations weekly and record decisions (FR-14).
4. Compute M2-M5; report limitations (sample size, single academy, thresholds still placeholders).

## 9.6 Threats to validity
Small sample; thresholds unvalidated; coaches not blind to the tool; norms from other populations; self-reported RPE/wellness by minors.

## 9.7 What is already automated
`pytest` checks repository deliverables (structure, OpenAPI validity, rule file schema, literature-review minimums). Run: `pip install -r requirements-dev.txt && pytest`.
