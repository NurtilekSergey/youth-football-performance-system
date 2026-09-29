# KPI catalogue and recommendation rules (draft v0.1)

Owner: **Sergey Nurtilek** (sports analyst / methodologist). Status: **draft for supervisor and coach review.**
Purpose: turn football norms into formal, measurable, configurable definitions (literature gap G-1: definitions differ between studies [S1, S2]).

> The system is a **decision-support tool**. Rules below are hypotheses to be calibrated with coaches and the supervisor; they are not
> medical advice or training prescriptions. Numeric thresholds marked *placeholder* have no validated source yet.

## 1. Context variables (needed to interpret every KPI)
| Variable | Definition | Why |
|---|---|---|
| Age group | Season age category (e.g. U13-U17), configurable | Norms differ by age [S4, S5] |
| Chronological age | Years at test date | [S5] |
| Relative age | Birth quartile within the age group | [S4] |
| Maturity status | e.g. % predicted adult height (as in [S5]) -> pre/circa/post-PHV band. *Method to be fixed with supervisor; may need parental height or a maturity-offset alternative.* | [S4, S5] |
| Position | GK/DF/MF/FW | Demands differ by position [S2] |

## 2. KPIs
| ID | KPI | Type | Definition / formula | Unit | Better = | Frequency | Source of data |
|---|---|---|---|---|---|---|---|
| K-SPR10 | 10 m sprint | Field test | Time over 10 m from standing start | s | lower | every 6-8 weeks | Timing gates or stopwatch (record method) |
| K-SPR30 | 30 m sprint | Field test | Time over 30 m | s | lower | every 6-8 weeks | as above |
| K-AGI | Agility | Field test | Time of agreed agility test (T-test or Illinois - to be chosen with coaches) | s | lower | every 6-8 weeks | Coach |
| K-CMJ | Jump height | Field test | Countermovement jump height | cm | higher | every 6-8 weeks | Jump mat / app |
| K-END | Endurance | Field test | Agreed intermittent test (e.g. Yo-Yo IR1 or 30-15 IFT - to be chosen) | m / level | higher | every 8-12 weeks | Coach |
| K-SRPE | Session load (internal) | Load | RPE (CR-10, 0-10) x session duration (min) | AU | n/a | every session | Player, collected by coach [S1, S10] |
| K-WLOAD | Weekly load & load change | Load | Sum of K-SRPE per week; ratio = this week / mean of previous 4 weeks [S11] | AU, ratio | monitor | weekly | derived |
| K-ATT | Attendance | Load | Attended / planned sessions over 4 weeks | % | higher | weekly | Coach |
| K-WELL | Wellness | Internal | Mean of 4 items (sleep, fatigue, mood, soreness) on a 1-5 scale, 5 = best | 1-5 | higher | before sessions or daily | Player self-report |
| K-MIN | Match minutes | Match | Minutes played per match | min | n/a | per match | Coach |
| K-TECH | Technical-tactical rating | Match | Coach rating 1-5 on agreed criteria (rubric defined in methodology) | 1-5 | higher | per match | Coach |
| K-EXT | External load (optional import) | Load | Total distance, high-speed distance, sprint count, acc/dec - as exported by a GPS/wearable; **definitions and thresholds stored with the import** (S2) | m, count | monitor | per session | CSV import |

## 3. Normalisation
For test KPIs the system reports (a) the raw value, (b) a z-score and percentile versus the **cohort norm for the same age group (and, when available, maturity band)**,
and (c) the player's own change over time. Sign convention: *positive z = better than cohort*.
**Norm sources (in order):** (1) published reference values - candidate to review: a 2021 systematic review of reference values for young male soccer players (PMC8622615, *found in search, not yet read*);
(2) the academy's own cohort once enough observations exist. **Minimum cohort size for z-scores: 15 (placeholder).**

## 4. Draft recommendation rules
Machine-readable copy: [`config/recommendation-rules.yaml`](../../config/recommendation-rules.yaml) (validated by tests).

| ID | Trigger (draft) | Recommendation to the coach (draft) | Evidence / status |
|---|---|---|---|
| R-01 | K-SPR30 z <= -1 (cohort, same age group) | Consider an acceleration/speed development block for this player | Placeholder threshold; [S9] suggests physical tests carry information |
| R-02 | K-AGI z <= -1 | Consider agility / change-of-direction work | Placeholder |
| R-03 | K-CMJ z <= -1 | Consider lower-limb power work | Placeholder |
| R-04 | K-END z <= -1 | Consider an aerobic / intermittent endurance block | Placeholder |
| R-05 | K-WLOAD ratio > 1.5 (placeholder) | Review planned load; consider reducing volume/intensity for the coming week | Concept from [S11]; threshold must be validated locally |
| R-06 | K-WELL below player's own 4-week mean by > 1 SD on 2 consecutive entries | Consider a recovery-focused session and a conversation with the player | Placeholder; not a medical assessment |
| R-07 | K-ATT < 70% over 4 weeks (placeholder) | Check reasons for absence (injury, school, motivation) | Placeholder |
| R-08 | Maturity band = circa-PHV | Interpret test changes cautiously; emphasise technique and coordination in feedback | Rationale: [S4, S5]; wording to be reviewed by supervisor |
| R-09 | Fewer than 3 observations for a KPI | Show "insufficient data" instead of a recommendation | Guards against over-interpretation |

Every recommendation shown to the coach must contain: rule ID, input values and dates, threshold, cohort used, and a plain-language rationale (NFR-06).

## 5. Open methodological questions (for supervisor)
1. Which agility and endurance tests are practical in Kazakhstan academies (equipment, time)?
2. Which maturity-estimation method is feasible without parental height data?
3. Where do we take initial norms for U13-U17 boys (and girls, if in scope)?
4. How to validate thresholds R-05..R-07 (coach panel review, then pilot)?
