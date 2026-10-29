# Verified build evidence — 2026-10-29

The following checks were executed locally against the working source:

| Check | Observed result |
| --- | --- |
| Python source/preflight/hash manifest | PASS |
| Offline `unittest` | **19/19 PASS** |
| GenVM Direct Mode `sdk_version=v0.2.12` | **20/20 PASS** |
| `genvm-lint lint` Entrench | PASS (3 static checks) |
| `genvm-lint lint` consumer | PASS (3 static checks) |
| `genvm-lint validate` Entrench | PASS (16 methods: 11 write/5 view) |
| `genvm-lint validate` consumer | PASS (2 methods: 1 write/1 view) |
| Local CLI package | `genlayer@0.39.1` installed |
| Stable RPC read-only `eth_chainId` | PASS: `61999` |
| `git diff --cached --check` | PASS |
| GitHub Actions on current commit | PENDING_FIRST_PUSH |
| Real StudioNet deploy + finalized lifecycle | NOT_EXECUTED |

GenVM semantic validation used the linter's cached compatible runtime after
its version lookup returned HTTP 403 and the fallback bundle was downloaded.
Direct Mode explicitly pinned the stable `v0.2.12` SDK artifact; it did
**not** use the linter fallback for those 20 contract execution tests.
Neither testing method is a substitute for live multi-validator finality.

At validation time:

```text
Entrench SHA-256:
c08135fc25cef9a634b5a9e6c4a7172466433d43ac14b782ead3fe282ebd2f55

Consumer SHA-256:
64912659e9488e06626f5ffc9f838c08ceba31c89ede3a1c2d5e8c9a0f013401
```

Those hashes identify the source bytes, not deployed-contract parity.
After any source edit, rerun `python3 scripts/preflight.py` and update the
manifest rather than carrying stale digests forward.
