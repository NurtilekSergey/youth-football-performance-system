# Contribution workflow

Rules follow the diploma-project repository requirements (GitHub/GitLab, YouTrack, review, tags).

## Accounts and authorship
* Every member commits with **their own account and real name/e-mail**. No shared accounts.
* Configure once: `git config user.name "<Full Name>"` and `git config user.email "<your e-mail>"`.

## Branches
* `main` is the reviewed baseline. Do **not** push to it directly once the first pre-defense is submitted.
* One branch per YouTrack task: `DIP-<id>-<short-slug>` (e.g. `DIP-10-database-schema`).

## Commits
* One coherent change per commit; message format: `DIP-<id>: <imperative summary>`.
* Documentation and design changes are committed the same way as code.
* No passwords, API keys, tokens or personal data. Use `config/.env.example` with placeholders.
* Player data concern minors: only synthetic or anonymised data may be committed.

## Pull requests
Each PR must: (1) explain the change, (2) reference the YouTrack task, (3) describe how it was checked.
**The other team member reviews and approves before merge.** Link the PR in the YouTrack task.

## Tags
Each submission is tagged and the tag is never moved: `pre-defense-1`, `pre-defense-2`, `final-pre-defense`.
Submission notes live in `docs/submissions/`.
