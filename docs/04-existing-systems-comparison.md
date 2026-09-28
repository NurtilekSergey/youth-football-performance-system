# 4. Existing system comparison

**Method.** Five systems relevant to youth football in Kazakhstan were compared against eight criteria.
Cells contain only what the cited vendor/third-party page states. **"n/s" = not stated on the page checked - it does
not mean the feature is absent.** Vendor statements are marketing claims, not independent evidence.
Verification by demo/trial for each "n/s" is task DIP-18. Checked: 23 October 2026.

## 4.1 Systems and sources
| ID | System | Type | Sources |
|---|---|---|---|
| X1 | Catapult Vector (athlete monitoring) | GPS/inertial wearable + software | [Catapult - Vector 8 launch](https://www.catapult.com/blog/catapult-launches-vector8-the-future-of-athlete-monitoring) |
| X2 | Playermaker | Foot-mounted sensors + app | [Playermaker FAQ](https://www.playermaker.com/pages/faq) |
| X3 | Hudl Wyscout | Video + event-data scouting platform | [Wyscout FAQ](https://www.hudl.com/en_gb/products/wyscout/faq) |
| X4 | Sportlyzer | Youth/amateur club management | [Capterra listing](https://capterra.com/p/144279/Sportlyzer/) |
| X5 | EasyCoach | Federation/club management (KFF partner) | [FC Business](https://fcbusiness.co.uk/news/kazakhstan-football-federation-partners-with-easycoach/) |

## 4.2 Comparison matrix
Legend: **Y** stated; **P** partly stated; **n/s** not stated; **N** stated as not offered.

| Criterion | X1 Catapult Vector | X2 Playermaker | X3 Hudl Wyscout | X4 Sportlyzer | X5 EasyCoach | **This project (target)** |
|---|---|---|---|---|---|---|
| **C1** Aimed at youth academies | P - page targets professional teams | **Y** - players from age 8 | P - "Youth Pack" (190+ youth competitions) but B2B scouting | **Y** - youth/amateur clubs | P - national/youth teams, federation level | Y |
| **C2** Physical load monitoring | **Y** - GPS + inertial wearable | **Y** - distance, sprints, acc/dec | n/s (match data, not training load) | n/s | P - "player monitoring" (details n/s) | Y (manual + CSV) |
| **C3** Technical / match performance metrics | n/s | **Y** - touches, kicking power, first touch, etc. | **Y** - tagged events, ~2,500 data points per match | n/s | n/s | P (coach-entered match indicators) |
| **C4** Coach-defined KPIs & field-test battery (sprint, agility, jump, endurance) | n/s | n/s | n/s | n/s | n/s | **Y** |
| **C5** Automated training recommendations | P - "AI-driven readiness insights" (content n/s) | **Y** - "AI training suggestions" (logic n/s) | n/s | n/s | n/s | **Y - rule-based, explained** |
| **C6** Age/maturity-aware interpretation | n/s | P - scores ranked by age, gender, position; maturity n/s | n/s | n/s | n/s | **Y** |
| **C7** Hardware dependency / cost | Wearable + dock + receivers; price n/s | Foot sensors; membership $149/year (page) | No hardware; price n/s (separate page) | None; EUR 7.50/user/month basic plan (Capterra) | None; price n/s | None (optional CSV from wearables) |
| **C8** Localisation (RU/KZ) / local federation fit | n/s | EN/ES/PT/DE only (page) | n/s | n/s | **Y** - already partnered with KFF | RU/KZ/EN planned |

## 4.3 Findings (claims that are supported by the evidence above)
1. **Hardware-based tools** (X1, X2) offer rich physical/technical metrics, but depend on devices and subscriptions; X1 is positioned for professional teams.
2. **Scouting / management tools** (X3, X4, X5) cover recruitment, administration and federation processes; none of the pages checked describes
   a coach-defined KPI model for youth field tests or individual training recommendations.
3. **Recommendations:** only X2 states an automated training-suggestion feature, and how it works is not described, so explainability could not be assessed.
4. **Maturity-awareness** (C6) is not stated by any of the five pages checked - consistent with literature gap G-2.
5. **EasyCoach** is already the KFF's federation-level platform; the project should complement it (import/export), not replace it.

## 4.4 Why a new solution is still justified - and its limits
**Hypothesis:** no single evaluated product documents, in the sources checked, the combination *hardware-optional input +
coach-configurable age/maturity-aware KPIs + explainable training recommendations*. This is a hypothesis until each "n/s" cell is verified
(demo, trial, or vendor contact) - planned task DIP-18. If a product turns out to cover this, the project's contribution shifts to localisation,
open configuration and evaluation.

Only five systems were compared (the required range is 3-5); further candidates (e.g. other athlete-monitoring or academy-management tools) are listed in the backlog.
