# Verified build and deployment evidence — 2026-11-05

## Local quality gates

| Check | Observed result |
| --- | --- |
| Python source/preflight/hash manifest | PASS |
| Offline `unittest` | **22/22 PASS** |
| GenVM Direct Mode `sdk_version=v0.2.12` | **27/27 PASS** |
| `genvm-lint lint` Entrench | PASS (3 static checks; UTF-8 output mode on Windows) |
| `genvm-lint lint` consumer | PASS (3 static checks; UTF-8 output mode on Windows) |
| `genvm-lint validate` Entrench | PASS (16 methods: 11 write/5 view) |
| `genvm-lint validate` consumer | PASS (2 methods: 1 write/1 view) |
| Local CLI package | `genlayer@0.39.1` installed |
| Stable RPC read-only `eth_chainId` | PASS: `61999` |
| Repository-local CLI executable | `node_modules/.bin/genlayer.cmd --version` = **0.39.1** |
| GenVM schema Entrench | PASS: 16 methods, 11 write / 5 view |
| GenVM test-only 900-second variant lint/validation/schema | PASS: 16 methods, 11 write / 5 view |
| GenVM schema consumer | PASS: 2 methods, 1 write / 1 view |
| Source SHA-256 manifest | PASS: matches both current deployable files |
| `npm ci` | PASS |
| `git diff --check` | PASS |

CI sets `GENVM_VERSION=v0.2.12` for lint, validation and schema extraction so
artifact discovery cannot silently select a newer preview bundle.

The Direct Mode suite includes exact queue/removal-time boundaries, malformed
semantic verdicts, prompt-delimiter escaping, validator disagreement, hidden
removal, prompt injection, cross-head rejection, replay, and consumer behavior.
Mocked adversarial observations are test inputs, not live validator evidence.

## Live stable StudioNet evidence

The actual RPC returned chain ID `61999`; no preview network was used. Both
deployments finalized with `MAJORITY_AGREE` and leader execution `SUCCESS`, and
both deployed source byte arrays matched the local source hashes. The full
receipt ledger and lifecycle links are in [`LIVE_EVIDENCE.md`](LIVE_EVIDENCE.md).

The corrected production ordinary amendment, removal classification, five-wallet
queue gate, protected-tier expansion, and typed consumer path
succeeded. A post-seal
mutation rolled back as `IMMUTABLE_CHARTER`, and consumer replay rolled back as
`ONE_SHOT` without changing the one-shot state.

The corrected live removal finalized as `R`/90%, required five approvals, rejected
four-approval queueing, queued with `available_at = queue_time + 86400`, and
rejected immediate execution with `TIMELOCK_ACTIVE`. It was canceled afterward,
so the full production 24-hour wait was not claimed. The shortened test-only
source passed local lint/validation/schema and the latest stable deployment
finalized successfully at `0xF5D85F57b6095aAe3d06D64AE7f847866EB28e1C` with
exact source parity. Its five-wallet 900-second lifecycle then finalized with
an exact `queue_time + 900` deadline, early `TIMELOCK_ACTIVE` rejection and
post-deadline execution; it remains explicitly test-only.

## CI

The source/test-variant commit `c806390a342b81f06dfa18ff71c2478fc9579df0`
passed [`run 42080046282`](https://github.com/ometere123/entrench/actions/runs/42080046282).
The final evidence commit `d0af34d169b686d2ddd16f9e49212d3065e4349b`
passed [`run 42109276609`](https://github.com/ometere123/entrench/actions/runs/42109276609).
The previous run failed at the preflight hash check because Windows CRLF bytes
were not preserved in the Git blob; `.gitattributes` and the committed source
blob now make the parity check deterministic across Windows and Linux.

GenVM semantic validation used the linter's compatible cached runtime after
its version lookup returned HTTP 403 and a fallback bundle was downloaded.
Direct Mode explicitly pinned `v0.2.12`; it did not use the linter fallback for
those contract execution tests. Neither local test layer substitutes for live
multi-validator finality.
