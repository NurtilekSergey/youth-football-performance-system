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
