# 3. Literature review

**Scope.** Monitoring of youth football players, training-load and maturity, decision support / recommender
systems in sport, and machine learning in talent identification and injury forecasting.
**Sources:** 15 in total - 13 peer-reviewed publications (8 from 2022-2026, 5 foundational) and 2 grey
sources used only for context. Full analysis table: [literature/literature-table.csv](literature/literature-table.csv);
full citations: [literature/references.md](literature/references.md).
**Search method (honest note):** keyword searches (youth football / training load / GPS / maturation / sports
recommender systems / ML talent identification / injury forecasting) in web indexes and publisher pages; the
review is *not* a systematic review. Bibliographic details were checked against publisher or index pages.
Before the final defense the search should be repeated in Scopus/WoS/PubMed and documented (task DIP-17).

## 3.1 What is already known

### Monitoring concepts: internal vs external load
Training load is conventionally split into *external* load (what the player does: distance, sprints,
accelerations) and *internal* load (the psycho-physiological response: session-RPE, heart rate) [S10]. Our data model
keeps these separate. Rapid increases in load have been associated with non-contact injuries and the
acute:chronic workload ratio was proposed as a monitoring tool [S11]; we treat such ratios as *configurable
screening rules whose thresholds must be validated locally*, not as universal truths.

### Monitoring in youth football is fragmented and non-standard
A 2025 systematic review of 46 studies found that most studies measure physical external load with GPS and
internal load with sRPE or heart rate, only 22 tracked well-being, and only five applied multivariate models;
the authors call for standardised, multidimensional frameworks, especially for youth and sub-elite players [S1].
A 2026 narrative review of 34 GPS studies in male youth soccer reports widely differing speed thresholds,
acceleration definitions and processing methods, which prevents comparison between studies [S2].
**Implication:** the project must define KPIs explicitly (name, formula, unit, threshold, source) and keep them configurable.

### Age and biological maturity change the meaning of a result
In sub-elite academy players, chronological age, relative age and maturity band were linked to different
accumulated loads [S4]; in elite U14-U17 players, high-speed running per minute followed chronological age whereas
total distance and accelerations/decelerations depended on an age x maturity interaction, strongest in younger
players [S5]. **Implication:** KPI norms and recommendations should be age-group- and maturity-aware; anthropometrics
(height, weight, sitting height where available) are stored to estimate maturity status.

### Recommender / decision-support systems in sport
A 2024 overview analysing 140 publications describes knowledge-based, content-based, collaborative and hybrid
approaches in sport and lists open issues: explanations, evaluation metrics, psychological factors,
real-time recommendations and LLM support [S7]. A fuzzy decision system for training programmes was reported to beat
other decision methods, but on a 16-participant dataset and with a mostly qualitative comparison [S8].
**Implication:** with small data, a knowledge-based (rule) engine with explanations is realistic; evaluation must be
quantitative and compared to a baseline - a weakness visible in [S8].

### Machine learning: promising but data-hungry
Systematic review of ML in talent identification (27 studies) found modest-to-excellent discrimination, rare
calibration checks, rare external validation and 59% of studies at high risk of bias; the authors conclude ML should
*complement* traditional methods [S3]. One-class SVM on 951 14-year-olds gave a mean AUC-ROC of 0.763, with physical
tests being the most informative inputs [S9]. For injuries, ML on GPS data can give interpretable forecasts [S12],
but reviews note inconsistent load proxies, imbalance handling and scarce multi-season data [S6].
**Implication:** ML is a stretch goal; injury prediction is out of scope.

### Data quality of wearable tracking
Validation of a 10-Hz GPS unit showed good validity for linear movement but lower accuracy for short distances
with direction changes [S13]. **Implication:** imported tracking data need quality flags; our primary input
(field tests and session-RPE) does not require hardware.

## 3.2 Critical synthesis: gaps the project takes into account

| # | Gap in the literature | Evidence | How the project responds |
|---|---|---|---|
| G-1 | Youth monitoring is fragmented and not standardised | S1, S2 | Explicit, versioned KPI catalogue ([domain/kpi-catalogue.md](domain/kpi-catalogue.md)) |
| G-2 | Maturity/relative age are often ignored in interpretation | S4, S5 | Age- and maturity-aware norms |
| G-3 | Recommender evaluation is weak (small data, qualitative) | S7, S8 | Baseline + quantitative evaluation ([09](09-verification-and-evaluation-plan.md)) |
| G-4 | ML models lack calibration/external validation; data are scarce | S3, S6 | Transparent rules first; ML only as evaluated extension |
| G-5 | Most high-quality studies rely on GPS hardware / professional squads | S1, S2, S12 | Hardware-optional design: manual + CSV input |

## 3.3 Limitations of this review
* Not a systematic search; source selection may be biased towards open-access and recent items.
* Several 2026 items were located through index pages; their full texts should be read in full before citing specific numbers in the thesis.
* No peer-reviewed study specific to **Kazakhstan** youth academies was found in this search; the local picture rests on grey sources (G1, G2) and planned interviews.
* Sports-science claims here must be reviewed by the supervisor before the thesis text.

## References
See [literature/references.md](literature/references.md). Short key: S1 Afonso 2025 - S2 GPS narrative review 2026 - S3 Tang 2026 -
S4 Teixeira 2022 - S5 Ribeiro 2026 - S6 Majumdar 2022 - S7 Felfernig 2024 - S8 An 2024 - S9 Jauhiainen 2019 -
S10 Impellizzeri 2019 - S11 Gabbett 2016 - S12 Rossi 2018 - S13 Nikolaidis 2018 - G1 KFF 2025 - G2 FC Business.
