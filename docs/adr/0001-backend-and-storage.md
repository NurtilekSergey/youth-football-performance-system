# ADR-0001: Backend platform, storage and API style
* **Status:** Proposed (to be accepted after supervisor review) - **Owner:** Aidyn Zhubanyshev - **Date:** 2026-10-23
* **Context:** two-person team; data-logic-heavy backend; relational player/team/test data; browser client.
* **Decision:** FastAPI + PostgreSQL + REST/OpenAPI. See [technology comparison](../05-technology-comparison.md).
* **Consequences:** + fast iteration, auto API docs, strong validation; - less enforced architecture (mitigated by module boundaries and tests).
* **Alternatives rejected:** Spring Boot (heavier for this scope), NestJS (weaker data ecosystem), MongoDB (weak relational integrity), GraphQL/gRPC (unneeded complexity).
