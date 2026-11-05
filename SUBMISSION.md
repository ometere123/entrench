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
ordinary and consumer paths are finalized on stable StudioNet 61999 with exact
source byte parity. The live validator set returned `MAJORITY_DISAGREE` for
the material/removal attempts, so this submission does not claim an unverified
75%/90% or 24-hour lifecycle.

## Repository

https://github.com/ometere123/entrench

## Verified deployments

- Entrench: [`0xE545b98d1c1Fce30421b64E55D71159984f7fd8d`](https://explorer-studio.genlayer.com/address/0xE545b98d1c1Fce30421b64E55D71159984f7fd8d)
- Consumer: [`0xE1D0845B7A07e562C3f623Cb6668933AC14F363c`](https://explorer-studio.genlayer.com/address/0xE1D0845B7A07e562C3f623Cb6668933AC14F363c)
- Network: `studionet`, chain `61999`, RPC `https://studio.genlayer.com/api`

## Reusability

Builders can deploy Entrench, freeze their own membership and principles, and
use `is_executed(proposal_id, expected_head)` from a typed intelligent-contract
consumer. The contract intentionally contains no frontend, backend, token,
custody or central decision service.

## Verification and limitations

- 20/20 offline tests and 26/26 stable GenVM Direct Mode tests pass.
- GenVM lint, validation and schema checks pass for both contracts.
- Deployed source bytes match the final contract hashes in
  `SOURCE_SHA256_MANIFEST.json`.
- The live ordinary amendment, immutable-charter rollback, typed consumer
  success and one-shot replay rollback are recorded in
  [`docs/LIVE_EVIDENCE.md`](docs/LIVE_EVIDENCE.md).
- Live M/R proposals finalized as `MAJORITY_DISAGREE`; the 75%/90% and
  public-chain 24-hour timelock lifecycle remains a blocker for a fully
  complete submission. This result is not relabeled as success.
