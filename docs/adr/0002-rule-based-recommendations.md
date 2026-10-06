# ADR-0002: Rule-based, explainable recommendation core
* **Status:** Proposed - **Owner:** Sergey Nurtilek (rules) / Aidyn Zhubanyshev (engine) - **Date:** 2026-10-23
* **Context:** no labelled outcome data; literature shows ML data/validation limits [S3, S6] and the need for explanations [S7]; coaches must be able to review the logic.
* **Decision:** recommendations are produced by a configurable rule set; every recommendation stores rule id, input values, thresholds and plain-language rationale. ML is optional future work.
* **Consequences:** + transparent, testable, calibratable with coaches; - rules need expert effort and validation (see [KPI catalogue](../domain/kpi-catalogue.md)).
