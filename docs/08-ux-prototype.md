# 8. UX / prototype

**Prototype:** open [`prototype/wireframes.html`](../prototype/wireframes.html) in a browser (low-fidelity, clickable, synthetic data only).
**API-level prototype:** [`api/openapi.yaml`](../api/openapi.yaml) and [`api/examples/`](../api/examples/).

## 8.1 Key scenarios (owner: S. Nurtilek) and mapped screens
| Scenario | Actor | Steps | Screen | Requirement |
|---|---|---|---|---|
| SC-1 After training | Coach | Open team -> enter duration -> RPE and attendance per player -> save (target <= 3 min) | S2 | FR-06, NFR-05 |
| SC-2 Test day | Coach | Select player/test -> enter value and method -> save; implausible values flagged | S3 | FR-05, FR-17 |
| SC-3 Bulk data | Coach | Upload CSV -> read import report | S6 | FR-09 |
| SC-4 Weekly review | Coach/Analyst | Open team dashboard -> spot alerts -> open player | S1, S4 | FR-11, FR-12 |
| SC-5 Decide next focus | Coach | Read recommendations and explanations -> accept/modify/reject with comment | S5 | FR-13, FR-14, NFR-06 |

## 8.2 Design principles
Fast data entry on a phone at the pitch; explanations next to every recommendation; a visible decision-support disclaimer; maturity context shown with results.

## 8.3 Status and next step
Wireframes have **not yet been validated with coaches**; walkthrough questions are in the [interview guide](evidence/interview-guide.md) (Q7-Q10). Findings will be recorded and the prototype revised (DIP-20).
