# Deployment and verification (stable StudioNet ONLY)

The project has a single network configuration: `studionet`, chain 61999,
RPC `https://studio.genlayer.com/api`, explorer
`https://explorer-studio.genlayer.com`. Do not change network aliases to
make a deployment script work.

## Local preflight

```bash
npm ci
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-direct.txt
.venv/bin/python scripts/preflight.py
.venv/bin/python -m unittest discover -s tests -p test_offline.py -v
.venv/bin/python -m pytest tests/test_direct.py -v
npm run network:check
npm run cli -- --version
npm run cli -- network set studionet
npm run cli -- network info
```

The project uses the repository-local `node_modules/.bin/genlayer` executable
(or `scripts/local-cli.cjs`, which resolves the same package directly); never
install or invoke a global CLI. The network guard reads the actual chain ID
from the stable RPC before any broadcast. A local install is invalid if
`node_modules/.bin/genlayer.cmd --version` is not exactly `0.39.1`.

The pinned Direct Mode tests use `genlayer-test==0.29.0`, `genlayer-py==0.11.0`
and `sdk_version="v0.2.12"` to avoid
accidentally using a later GenVM artifact. On native Windows, an older
the pinned runner's file-descriptor unlink issue may require a
compatibility shim; running tests in Linux CI avoids that platform-specific
loader behavior. The checked-in shim is test infrastructure only and is not
imported by deployed contracts. Do not bypass tests because of a missing GenVM
artifact.

## Deployment

Choose a funded StudioNet account using the CLI's supported account workflow.
Keep passwords/private keys entirely outside Git and the review report.

```bash
ENTRENCH_DEPLOY_ACK=61999 npm run deploy:core
```

On Windows PowerShell, use the native guarded wrapper:

```powershell
$env:ENTRENCH_DEPLOY_ACK = '61999'
.\scripts\deploy.ps1 -Contract contracts/entrench.py
```

Record actual address, hash, validator votes, execution success and finality.
Complete the real five-wallet lifecycle described in
`docs/REVIEWER_DEMO.md`.

Only then deploy the consumer, supplying the actual registry address,
proposal ID, and **current execution head** via its constructor:

```bash
ENTRENCH_DEPLOY_ACK=61999 npm run deploy:consumer
```

CLI may ask interactively for constructor args and account password. Confirm
it is asking for the intended values; never invent successful confirmation.

The independent consumer is intentionally permissionless and non-value-bearing:
any caller may trigger its one-shot action once the exact amendment/head pair is
canonical. It is not a requester-owned entitlement. Applications that need
requester authorization must add that authorization in their own wrapper.

## Source parity

1. Produce SHA-256 locally for `contracts/entrench.py` and
   `contracts/consumer_gate.py`.
2. Fetch deployed contract code from the correct chain 61999.
3. Compare **exact source bytes**, not just filenames or class names.
4. Query `get_charter()`, `get_proposal(id)`, and `is_executed(id, head)`.
5. Record the transaction terminal status and execution result separately.
6. Never describe a merely ACCEPTED operation as FINALIZED.

The current verified deployment ledger is in
[`docs/LIVE_EVIDENCE.md`](LIVE_EVIDENCE.md). It records the corrected production
addresses, transaction receipts, exact source-byte parity, genuine `R` queue,
86400-second early rejection, ordinary lifecycle, typed consumer execution and
replay rollback. Historical M/R disagreements remain labeled as historical.

## Test-only 900-second integration variant

`contracts/test_only_900/entrench.py` is an isolated copy whose only contract
logic difference is `REMOVAL_DELAY = 900`. It is never the canonical production
source and must not be described as evidence that the production 24-hour delay
has elapsed. The guarded Windows command is:

```powershell
$env:ENTRENCH_TEST_ONLY_ACK = '900'
.\scripts\deploy_test_timelock.ps1
```

The guard rechecks the exact source, manifest, stable RPC chain ID and local
CLI. At the time of this handoff, stable StudioNet finalized test-variant
deployment requests as `contract_error / invalid_contract` and created no
contract. Do not record a returned address unless a future runtime correction
produces FINALIZED + leader execution `SUCCESS` and exact source parity.
