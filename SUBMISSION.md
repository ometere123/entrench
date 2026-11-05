# Entrench — submission brief

## Title

Entrench: Constitutional Amendment Governance Guard

## Description

Entrench is a reusable, contract-only GenLayer primitive for constitutional
governance. It freezes a charter, member roster and protected principles, then
uses GenLayer semantic consensus to classify each proposed policy change as
ordinary, material, removal or unclear. Deterministic on-chain code applies
the corresponding quorum, timelock and head/version checks; a typed consumer
proves that an exact executed amendment can unlock a one-shot action. The
ordinary, protected-tier, removal-classification, timelock-gate and consumer
paths are finalized on stable StudioNet 61999 with exact source byte parity.
The production removal was queued with `available_at = queue_time + 86400` and
rejected early with `TIMELOCK_ACTIVE`; it was canceled rather than waiting 24
hours. A separate 900-second test source is documented but stable deployment
currently returns `invalid_contract`, so no shortened lifecycle is claimed.

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
- GitHub Actions was green on the corrected production source commit: [`run 42063888925`](https://github.com/ometere123/entrench/actions/runs/42063888925); the final documentation commit requires its own green run.
- Deployed source bytes match the final contract hashes in
  `SOURCE_SHA256_MANIFEST.json`.
- The live ordinary amendment, immutable-charter rollback, typed consumer
  success and one-shot replay rollback are recorded in
  [`docs/LIVE_EVIDENCE.md`](docs/LIVE_EVIDENCE.md).
- A live protected-tier `E` proposal reached 75%, four approvals and execution.
- The corrected live removal reached `R`/90%, rejected four approvals, queued
  with the exact 86400-second delay and rejected premature execution. The
  remaining blocker is stable runtime rejection of the isolated 900-second
  source as `invalid_contract`; no test-only address or lifecycle is claimed.
