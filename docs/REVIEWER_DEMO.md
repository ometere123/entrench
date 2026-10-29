# Reviewer demo: a disguised removal cannot pass as routine

## Five-wallet setup (real transaction calls)

1. Deploy `contracts/entrench.py` from Wallet A.
2. From A, call `set_genesis("Treasury constitutional governance",
   "Members may withdraw vested shares after 7 days. Reports are monthly.")`.
3. From A, call `add_principle("WITHDRAWAL",
   "Members' vested withdrawal rights must not be removed, disabled or
   effectively restricted by relabeling authority.")`.
4. From A, add B, C, D and E via `add_member(Address)`.
5. **Each of A–E** calls `attest_charter()` on the final revision.
6. A calls `seal_charter()`; save returned `head_hash`.

Never substitute a forged second account or assume a creator can attest for
others. For automated Direct Mode, the test fixtures provide independent
addresses; real StudioNet evidence requires real wallets and actual writes.

## A. Disguised constitutional removal

From A, submit:

- Title: `Administrative Liquidity Improvement`
- New policy: `Members are not entitled to withdrawals. Reports are monthly.`
- Expected head: exact current `head_hash`.

Inspect `get_proposal(id)`. With a genuine removal verdict `R`, the
deterministic fields must be `threshold_class=REMOVAL`,
`threshold_percent=90`, `required_yes=5`.

A/B/C cast three yes votes. Calling `queue(id)` MUST fail with
`INSUFFICIENT_APPROVALS`. D/E add yes votes. Now `queue(id)` succeeds
but `execute(id)` MUST fail with `TIMELOCK_ACTIVE` until the full
86400-second delay. The original withdrawal policy remains current until
execution. In demo environments, avoid waiting or manipulating production time;
the failure itself proves the gate.

## B. Ordinary and protected amendments

For an independent fresh charter, submit a purely administrative reporting
calendar change. When the semantic verdict is N, three of five yes votes
should queue and execute immediately. Record old/new head hashes.

For another fresh charter, change a protected withdrawal wait from 7 to
30 days. A genuine M verdict requires **four** of five yes votes.

## C. Consumer proof

Deploy `ConstitutionalActionGate(registry, proposal_id, expected_head)`.
Before the referenced amendment is executed, `perform()` fails. After a
genuine FINALIZED successful execution at the expected **current** head,
`perform()` succeeds once. A second `perform()` fails with `ONE_SHOT`.
If another amendment changes the current head first, the stale consumer fails.

## D. Adversarial validation

Direct Mode tests simulate:

- leader claims N while independent validator finds R — validator rejects;
- leader and verifier agree N, independent adversarial audit detects a hidden
  removal — validator rejects;
- U and malformed responses — fail closed;
- injections in the proposal text and misleading proposal titles — never
  parameterize the deterministic threshold.

Mocks provide controlled **test inputs**, not evidence that real network
validators reached those conclusions. Do not describe them as live votes.

## Proof checklist for a submitted deployment

- Repository `main` SHA and all green CI jobs.
- Local CLI `0.39.1`, alias `studionet`, `eth_chainId=61999`.
- Core and consumer deploy transaction hashes and addresses.
- Explicit `FINALIZED` status plus GenVM execution success.
- `gen_getContractCode` or CLI source read matches the exact committed source
  bytes (save SHA-256).
- Each A–E voter tx and resulting change in approval mask.
- Blocked 3-of-5 removal, queued 5-of-5 removal and timelock rejection.
- Ordinary and M-tier lifecycle + consumer one-shot/replay proof.

An evidence file should say `NOT_EXECUTED` until each event genuinely occurs.
