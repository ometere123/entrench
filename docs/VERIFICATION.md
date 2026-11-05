# Verified build evidence — 2026-11-05

The following checks were executed locally against the working source:

| Check | Observed result |
| --- | --- |
| Python source/preflight/hash manifest | PASS |
| Offline `unittest` | **20/20 PASS** |
| GenVM Direct Mode `sdk_version=v0.2.12` | **26/26 PASS** |
| `genvm-lint lint` Entrench | PASS (3 static checks) |
| `genvm-lint lint` consumer | PASS (3 static checks) |
| `genvm-lint validate` Entrench | PASS (16 methods: 11 write/5 view) |
| `genvm-lint validate` consumer | PASS (2 methods: 1 write/1 view) |
| Local CLI package | `genlayer@0.39.1` installed |
| Stable RPC read-only `eth_chainId` | PASS: `61999` |
| Repository-local CLI executable | `node_modules/.bin/genlayer.cmd --version` = **0.39.1** |
| GenVM schema Entrench | PASS: 16 methods, 11 write / 5 view |
| GenVM schema consumer | PASS: 2 methods, 1 write / 1 view |
| Source SHA-256 manifest | PASS: matches both current deployable files |
| `git diff --cached --check` | PASS |
| GitHub Actions, first published source commit | **SUCCESS** — run `40893524450` at `710a85029ef37788b78cb0e16c3adfff0207e0d9` |
| Real StudioNet deploy + finalized lifecycle | NOT_EXECUTED |

GenVM semantic validation used the linter's cached compatible runtime after
its version lookup returned HTTP 403 and the fallback bundle was downloaded.
Direct Mode explicitly pinned the stable `v0.2.12` SDK artifact; it did
**not** use the linter fallback for those 26 contract execution tests.
Neither testing method is a substitute for live multi-validator finality.

GitHub CI proof:
`https://github.com/ometere123/entrench/actions/runs/40893524450`

At the earlier validation commit, the source hashes were:

```text
Entrench SHA-256:
c08135fc25cef9a634b5a9e6c4a7172466433d43ac14b782ead3fe282ebd2f55

Consumer SHA-256:
64912659e9488e06626f5ffc9f838c08ceba31c89ede3a1c2d5e8c9a0f013401
```

Current source hashes are maintained in
[`SOURCE_SHA256_MANIFEST.json`](../SOURCE_SHA256_MANIFEST.json) and verified by
`scripts/preflight.py`. They identify source bytes, not deployed-contract
parity. After any contract edit, rerun preflight and update the manifest before
deployment.

No StudioNet deployment or finalized lifecycle evidence is claimed by this
file yet; see `docs/LIVE_EVIDENCE.md`.
