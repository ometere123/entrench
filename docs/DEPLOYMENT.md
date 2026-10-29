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
npm exec -- genlayer --version
npm exec -- genlayer network set studionet
npm exec -- genlayer network info
```

The project uses `node_modules/.bin/genlayer` via npm; never install a
global CLI over your existing release candidate. The network guard reads
the actual chain ID from the stable RPC before any broadcast.

The pinned Direct Mode tests use `sdk_version="v0.2.12"` to avoid
accidentally using a later GenVM artifact. On native Windows, an older
`genlayer-test==0.29.2` file-descriptor unlink issue may require a
compatibility shim; running tests in Linux CI avoids that platform-specific
loader behavior. Do not bypass tests because of a missing GenVM artifact.

## Deployment

Choose a funded StudioNet account using the CLI's supported account workflow.
Keep passwords/private keys entirely outside Git and the review report.

```bash
ENTRENCH_DEPLOY_ACK=61999 npm run deploy:core
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

## Source parity

1. Produce SHA-256 locally for `contracts/entrench.py` and
   `contracts/consumer_gate.py`.
2. Fetch deployed contract code from the correct chain 61999.
3. Compare **exact source bytes**, not just filenames or class names.
4. Query `get_charter()`, `get_proposal(id)`, and `is_executed(id, head)`.
5. Record the transaction terminal status and execution result separately.
6. Never describe a merely ACCEPTED operation as FINALIZED.

Deployment evidence is intentionally not fabricated in this repository.
