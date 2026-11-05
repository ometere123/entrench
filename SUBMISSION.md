# Entrench — submission brief

## Title

Entrench: Constitutional Amendment Governance Guard

## Description

Entrench is a standalone GenLayer constitutional governance guard. It freezes a charter, voting roster and protected principles, then uses independent semantic consensus to classify policy changes by their real effect—not their titles. Deterministic enforcement requires 51% approval for ordinary changes, 75% for protected modifications or expansions, and 90% plus a 24-hour timelock for removal. Ambiguous classifications fail closed. On stable StudioNet 61999, live transactions prove removal classification, five-wallet approval, queueing, early timelock rejection, ordinary and protected amendment execution, and a typed one-shot consumer with replay protection. A separate 900-second test-only deployment proves post-deadline removal execution; the production 24-hour wait was not completed. Source integrity, Direct Mode and CI are verified.

## Repository

https://github.com/ometere123/entrench

## Verified deployments

- Entrench: [`0x0fd3823b7f08F73275AABf60e88bEc9A1c507314`](https://explorer-studio.genlayer.com/address/0x0fd3823b7f08F73275AABf60e88bEc9A1c507314)
- Consumer: [`0x4a51a85C33604B9B7F1C9347bF944853fE8F632f`](https://explorer-studio.genlayer.com/address/0x4a51a85C33604B9B7F1C9347bF944853fE8F632f)
- Network: `studionet`, chain `61999`, RPC `https://studio.genlayer.com/api`

## Reusability

Builders can deploy Entrench, freeze their own membership and principles, and
use `is_executed(proposal_id, expected_head)` from a typed intelligent-contract
consumer. The contract intentionally contains no frontend, backend, token,
custody or central decision service.

## Verification and limitations

- 22/22 offline tests and 27/27 stable GenVM Direct Mode tests pass.
- GenVM lint, validation and schema checks pass for production, consumer and
  the isolated 900-second source.
- GitHub Actions is green for source/test-variant commit `c806390a342b81f06dfa18ff71c2478fc9579df0`: [`run 42080046282`](https://github.com/ometere123/entrench/actions/runs/42080046282), and for final commit `73888ad3f9e75bf1faaffa5868c67b4db7b5aee0`: [`run 42111182791`](https://github.com/ometere123/entrench/actions/runs/42111182791).
- Deployed source bytes match the final contract hashes in
  `SOURCE_SHA256_MANIFEST.json`.
- The live ordinary amendment, immutable-charter rollback, typed consumer
  success and one-shot replay rollback are recorded in
  [`docs/LIVE_EVIDENCE.md`](docs/LIVE_EVIDENCE.md).
- A live protected-tier `E` proposal reached 75%, four approvals and execution.
- The corrected live removal reached `R`/90%, rejected four approvals, queued
  with the exact 86400-second delay and rejected premature execution. The
  latest test-only deployment is source-matched at
  `0xF5D85F57b6095aAe3d06D64AE7f847866EB28e1C`; its five-wallet 900-second
  lifecycle finalized successfully and is explicitly separated from production
  evidence.
