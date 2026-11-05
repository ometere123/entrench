# Entrench

**A constitutional amendment guard for autonomous governance.**

> A protected right cannot be removed through an ordinary vote just because
> its removal was hidden inside a proposal named “Operational Improvement.”

Entrench is a **standalone, frontend-free GenLayer Intelligent Contract**.
Its reusable mechanism raises the voting threshold according to a proposed
policy's **substantive effect on immutable protected principles**, not its label.
An independent consumer demonstrates that an executed amendment has a
head-bound, machine-checkable effect.

## The invariant

| Independently assessed effect | Required approvals | Additional gate |
| --- | ---: | --- |
| No protected principle materially touched | 51% of immutable members | None |
| Protected principle materially modified or expanded | 75% | None |
| Protected principle removed or effectively disabled | 90% | 24-hour timelock |
| Any relevant impact unclear | Blocked | New, clearer proposal required |

Approvals are integer-ceiling rounded. With a five-member charter, the tiers
require **3, 4 and 5 distinct wallets**. Thresholds and protected definitions
cannot be altered by the charter owner's later actions.

Semantic classification is performed inside GenLayer's Equivalence Principle.
The proposer cannot supply an authoritative impact class. The leader returns a
bounded vector for every protected principle; validators independently classify
the same frozen old policy, proposed replacement and principles, then perform a
separate adversarial search for false negatives and covert removals. Policy text
is JSON-encoded as escaped untrusted data before prompt insertion. Code,
not the model, computes votes, delays, status and version transitions.

## Demo in one minute

1. A five-person charter protects members' withdrawal rights.
2. Proposal “Administrative Liquidity Improvement” silently deletes those
   rights from the replacement policy.
3. Semantic verdict is **R** even though the title sounds routine.
4. Three approvals (enough for an ordinary proposal) **cannot queue it**.
5. Even with all five approvals, it **cannot execute until 24 hours later**.
6. A genuine ordinary reporting-calendar edit passes with three approvals.
7. A consumer rejects a proposal/head pair once a newer policy head supersedes it.

The complete reproducible sequence is in [docs/REVIEWER_DEMO.md](docs/REVIEWER_DEMO.md).

## Package contents

- `contracts/entrench.py` — full constitutional registry, consensus gate,
  immutable membership, voting, queue, timelock, versioned policy head.
- `contracts/consumer_gate.py` — permissionless, non-value-bearing one-shot head-bound IC consumer.
- `tests/test_offline.py` — pure invariant and adversarial payload checks.
- `tests/test_direct.py` — genuine GenVM Direct Mode test scenarios.
- `scripts/network-guard.cjs` — exact production RPC chain ID and local CLI check.
- `scripts/receipt-summary.cjs` — compact finalized-receipt verifier for live evidence.
- `scripts/preflight.py` — non-deploying source and configuration verification.
- `scripts/deploy.sh` / `scripts/deploy.ps1` — deliberately explicit production deploy wrappers.
- `.github/workflows/ci.yml` — reproducible pinned Node/Python checks.
- `docs/SECURITY.md` — assumptions, failure modes and mitigations.

No frontend, backend, custodial wallet, Docker dependency or central decision API.

## Exact network and toolchain

| Setting | Required value |
| --- | --- |
| Network alias | **`studionet`** |
| Chain ID | **`61999`** |
| RPC | **`https://studio.genlayer.com/api`** |
| Explorer | **`https://explorer-studio.genlayer.com`** |
| GenLayer CLI | **local `genlayer@0.39.1`** |
| GenVM Direct Mode | **`v0.2.12`** |
| genlayer-test | **`0.29.2`** |
| genlayer-py | **`0.16.3`** |
| genvm-linter | **`0.11.0`** |

The global CLI is never installed, replaced or invoked by the project scripts.
`scripts/local-cli.cjs` resolves the checked-in local package directly and
fails if its version is not exactly `0.39.1`; `npm run cli -- ...` uses that
wrapper rather than allowing an npm/global fallback.

## Local verification

```bash
npm ci
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-direct.txt
.venv/bin/python scripts/preflight.py
.venv/bin/python -m unittest discover -s tests -p test_offline.py -v
.venv/bin/python -m pytest tests/test_direct.py -v
npm run network:check
```

The last command performs a **read-only** production RPC check. It must
return chain ID 61999; an unreachable RPC is a **failure**, not permission
to switch networks.

On Windows, use the corresponding `.venv\\Scripts\\python.exe` and see the
pinned test-runner compatibility note in the deployment guide. The checked-in
`tests/conftest.py` only repairs the Windows temporary-file cleanup defect in
`genlayer-test==0.29.2`; it does not alter contract execution.

## Production deployment

```bash
ENTRENCH_DEPLOY_ACK=61999 npm run deploy:core
ENTRENCH_DEPLOY_ACK=61999 npm run deploy:consumer
```

Before deployment, supply the correct funded and unlocked StudioNet account
through the local CLI's supported workflow. The wrapper asks for a second
interactive `61999` confirmation. Record only actual **FINALIZED,
successful** transaction receipts, deployed addresses, code/source parity and
subsequent lifecycle evidence. The consumer constructor needs the actual core
address, proposal ID and canonical execution head.

On Windows PowerShell, use `scripts/deploy.ps1 -Contract
contracts/entrench.py` (or `consumer_gate.py`) after setting
`$env:ENTRENCH_DEPLOY_ACK = '61999'`.

## Deliberate boundaries

- A consensus outcome is a protocol decision, not a mathematical proof that
  language has a uniquely correct interpretation.
- A malicious set of validators can still misclassify. Independent comparison
  plus adversarial review makes the failure detectable/testable, not impossible.
- Protected principles and voter roster are immutable after sealing; no
  membership churn or emergency admin override is included.
- The contract does not transfer money or claim legal enforceability.
- Untrusted policy text remains on-chain and public; do not put secrets into it.
The primary Entrench deployment is live at
[`0xE545b98d1c1Fce30421b64E55D71159984f7fd8d`](https://explorer-studio.genlayer.com/address/0xE545b98d1c1Fce30421b64E55D71159984f7fd8d)
and the typed consumer at
[`0xE1D0845B7A07e562C3f623Cb6668933AC14F363c`](https://explorer-studio.genlayer.com/address/0xE1D0845B7A07e562C3f623Cb6668933AC14F363c).
Both are source-byte matched and finalized on StudioNet 61999. The live
ordinary and consumer paths are proven, while the live M/R semantic attempts
reached `MAJORITY_DISAGREE`; therefore the 75%/90% and 24-hour live lifecycle
remains explicitly unresolved rather than claimed.

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and
[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for details. Recorded build results
(20 offline tests, 26 genuine Direct Mode tests, both semantic validations
passed) and live limitations are in [docs/VERIFICATION.md](docs/VERIFICATION.md)
and [docs/LIVE_EVIDENCE.md](docs/LIVE_EVIDENCE.md).
