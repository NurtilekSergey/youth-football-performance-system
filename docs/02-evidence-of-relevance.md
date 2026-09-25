# 2. Evidence of relevance

Requirement: 3-5 discussions with user representatives or a substantive agreement with the client.
This document separates **verified findings** (with a source) from **assumptions** (to be tested).

## 2.1 Evidence collected so far (desk research + team knowledge)

| # | Evidence | Source | Type | What it tells us |
|---|---|---|---|---|
| E1 | Kazakhstan Football Federation (KFF) development strategy to 2030: single youth pathway (U-15 to senior), unified standards for youth competitions, "KFF Digital Football Hub" (player/coach digital IDs, registry of clubs and academies, automated youth registration, match statistics database and analytical tools), implementation 2025-2030 | [KFF news](https://kff.kz/en/news/27278) | Verified (official federation publication) | Digitalisation of youth football is a national priority; the Hub covers registry and match statistics - the page does **not** mention individual training-load monitoring or training recommendations |
| E2 | KFF partnership with EasyCoach (national teams, coach education, hub, competition management) | [FC Business](https://fcbusiness.co.uk/news/kazakhstan-football-federation-partners-with-easycoach/) | Verified, but promotional article, undated | A federation-level management platform already exists; our tool must not duplicate it and should stay import/export-friendly |
| E3 | International reviews: monitoring is fragmented, youth/sub-elite under-served, variable definitions are not standardised | Literature review S1, S2 | Verified (peer-reviewed) | Supports the need for a structured, standard-definition monitoring model for youth players |
| E4 | Team member Sergey Nurtilek has multi-year youth-football playing experience, including in the FC Aktobe structure | Team declaration (supervisor-justification document) | **Team-declared** | Source of first-hand familiarity with coach needs - not a substitute for interviews |

## 2.2 Planned discussions with user representatives (to be completed before the pre-defense)

> **Status: to schedule / not yet held.** No interview results are recorded here until they actually take place.
> Fill in the log below immediately after each discussion and attach notes in `docs/evidence/interviews/`.

| ID | Representative (role, organisation) | Date | Format | Consent for notes | Notes file | Status |
|---|---|---|---|---|---|---|
| I1 | Youth coach (academy TBD) | TBD | 30-45 min, semi-structured | TBD | `evidence/interviews/I1.md` | To schedule |
| I2 | Youth coach (different age group) | TBD | 30-45 min | TBD | `evidence/interviews/I2.md` | To schedule |
| I3 | Academy methodologist / head of youth | TBD | 30-45 min | TBD | `evidence/interviews/I3.md` | To schedule |
| I4 | Fitness / S&C coach | TBD | 30 min | TBD | `evidence/interviews/I4.md` | To schedule |
| I5 | Academy administrator (optional) | TBD | 20-30 min | TBD | `evidence/interviews/I5.md` | Optional |

Interview guide: [evidence/interview-guide.md](evidence/interview-guide.md).
Interview records must be anonymised (role + academy type, no player names).

## 2.3 Assumption register

| ID | Assumption | Why we believe it | How it will be verified | Status |
|---|---|---|---|---|
| A1 | Most youth coaches track data on paper / spreadsheets / messengers | Team experience | I1-I4 | Unverified |
| A2 | Coaches can collect simple field tests (sprint, agility, jump, endurance) every 4-8 weeks | Team experience; standard practice | I1-I4 | Unverified |
| A3 | Wearable GPS hardware is not available to most youth academies | Cost (see [comparison](04-existing-systems-comparison.md)) | I1-I4 | Unverified |
| A4 | Coaches want explainable recommendations, not a black-box score | Literature on recommender explanations (S7) | I1-I4, prototype walkthrough | Partly supported by literature |
| A5 | Biological maturity matters for fair interpretation of results of 12-16-year-olds | S4, S5 | Review with supervisor / methodologist | Supported by literature |
| A6 | Academies will share anonymised data for evaluation | - | Agreement with an academy | Unverified |

## 2.4 What would change the project
If interviews contradict A1-A3 (e.g. academies already have GPS and a data platform), the scope shifts towards
analytics/recommendation on top of imported GPS data rather than manual data entry.
