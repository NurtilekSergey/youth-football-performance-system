# 6. Requirements specification (initial, v0.1)

Priority = MoSCoW (**M**ust / **S**hould / **C**ould). Each requirement has a testable acceptance criterion (AC).
"Source" links to evidence/assumptions in [02](02-evidence-of-relevance.md) and literature ([03](03-literature-review.md)). Requirements derived from
assumptions (A-ids) must be re-confirmed after the interviews.

## 6.1 Actors
Coach (primary), Analyst/methodologist, Academy administrator, Player/parent (optional read-only). See [system context](07-architecture-and-diagrams.md).

## 6.2 Functional requirements (owner of domain content: S. Nurtilek)

| ID | Requirement | Pri | Acceptance criterion | Source |
|---|---|---|---|---|
| FR-01 | Users sign in with role-based access (Admin, Analyst, Coach) | M | Given a coach of team X, when requesting team Y data, then access is denied (HTTP 403) | NFR-02 |
| FR-02 | Admin manages teams and age groups; coach is assigned to teams | M | A team with age group, season and >=1 coach can be created, edited and archived | Proposal 1.6 |
| FR-03 | Create/edit player profiles (pseudonymised ID, birth date, position, dominant foot, team) | M | A player can be created with required fields; invalid birth date is rejected with a message | S4, S5 |
| FR-04 | Record anthropometrics (height, weight, optional sitting height, optional parental height) and derive maturity band | S | Given valid anthropometrics, when saving, then a maturity band or "not estimable" with reason is stored | S4, S5, A5 |
| FR-05 | Record field-test results from the KPI battery (K-SPR10, K-SPR30, K-AGI, K-CMJ, K-END) with date and method | M | A result outside the plausible range (defined per KPI) is rejected or flagged; saved result appears in the player history | KPI catalogue |
| FR-06 | Record session data: date, duration, per-player RPE (CR-10) and attendance | M | Session load (RPE x duration) is computed and stored; entering 20 players is possible in one form | S1, S10, A2 |
| FR-07 | Record wellness items (sleep, fatigue, mood, soreness, 1-5) | S | Composite K-WELL is computed; values outside 1-5 are rejected | S1 |
| FR-08 | Record match indicators (minutes, coach technical-tactical rating 1-5) | S | Match record is linked to player and date | KPI catalogue |
| FR-09 | Import test/session/external-load data from CSV with validation report | S | Given a file with 100 rows including 5 invalid, then 95 are imported and a report lists the 5 rejected rows with reasons | S2, S13, A3 |
| FR-10 | Compute KPIs: raw value, z-score/percentile vs cohort norm of same age group (and maturity band if available), change over time | M | For a seeded dataset, computed z-scores equal reference values within 0.01 | S5, KPI catalogue |
| FR-11 | Show a player's KPI trends and history | M | Player view shows time series for each KPI with cohort band | S1 |
| FR-12 | Show team/cohort report (distribution, outliers, attendance, weekly load) | S | Coach sees team report for chosen period | A1 |
| FR-13 | Generate recommendations from configured rules, each with rule ID, inputs, threshold and rationale | M | For a seeded player whose K-SPR30 z = -1.3, R-01 is produced with its rationale; with <3 observations R-09 is produced instead | S7, ADR-0002 |
| FR-14 | Coach records a decision on each recommendation (accepted / modified / rejected + comment) | M | Decision is stored with timestamp and user; used in evaluation | S7 (evaluation gap) |
| FR-15 | Analyst edits KPI norms and rule thresholds with versioning | S | Changed threshold creates a new rules version; earlier recommendations keep their version reference | S2 |
| FR-16 | Export player/team report as CSV and PDF | C | Export contains the same values as the screen | A1 |
| FR-17 | Data-quality flags (missing, outlier, device-method change) | S | Outlier >3 SD from cohort is flagged, not silently dropped | S13 |
| FR-18 | Audit log of changes to player data | C | Each edit records user, time, old and new value | NFR-03 |
| FR-19 | User interface languages: Russian and English (Kazakh later) | C | Language switch changes all UI labels | Evidence E1 |

## 6.3 Non-functional requirements (owner: A. Zhubanyshev)

| ID | Requirement | Pri | Acceptance criterion (measurable) |
|---|---|---|---|
| NFR-01 | Performance | S | p95 API response <= 500 ms at 50 concurrent users with 500 players and 100,000 metric records (load test, synthetic data) |
| NFR-02 | Security | M | Passwords stored hashed (bcrypt/argon2); HTTPS in deployment; role checks on every endpoint (automated tests cover 100% of endpoints) |
| NFR-03 | Privacy of minors' data | M | No real names required (pseudonymised player ID); consent flag stored; delete-player removes personal data; no real data in the repository (checked by CI secret/data scan) |
| NFR-04 | Data integrity | M | Relational constraints and unit/range validation; invalid input never stored (tests for each KPI) |
| NFR-05 | Usability | S | Mean SUS >= 68 with >= 5 coaches; entering a 20-player session takes <= 3 min (median) |
| NFR-06 | Explainability | M | 100% of generated recommendations contain rule ID, inputs, threshold, cohort and rationale |
| NFR-07 | Testability | M | Unit tests for KPI and rule modules; line coverage of these modules >= 80% |
| NFR-08 | API documentation | S | OpenAPI contract in repo is valid and every implemented endpoint is described (contract test) |
| NFR-09 | Maintainability | S | Modular structure (api, domain, rules, persistence); linter and CI pass on every PR |
| NFR-10 | Deployability | S | `docker compose up` starts the full system on a laptop; setup documented in README |
| NFR-11 | Compatibility | C | Works on current Chrome, Firefox and mobile Safari; usable at 360 px width |

## 6.4 Constraints
* Decision support only - UI and reports must display a disclaimer that recommendations do not replace a coach or medical specialist.
* Hardware-optional: no requirement depends on a wearable device.
* Only synthetic or anonymised data in the repository.

## 6.5 Change control
Requirements change only via PR referencing a YouTrack task; version history is in git. Priorities to be reviewed with the supervisor and after interviews (I1-I4).
