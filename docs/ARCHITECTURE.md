# Architecture and invariants

## Separation of judgment and authority

```text
immutable charter: principles + members + base policy
                         |
proposer supplies replacement POLICY and expected head (title is display-only)
                         |
           GenLayer Equivalence Principle
             leader vector [N/M/R/E/U]
                independent validator
             adversarial underestimate audit
                         |
            deterministic threshold map
               N -> 51%, M/E -> 75%
                 R -> 90% + 24h
                 U -> BLOCKED
                         |
         immutable member voting (one vote each)
                         |
                  queue, timelock
                         |
             head-pinned state transition
                         |
             independent consumer gate
```

## Genesis

The creator deploys a blank instance and provisions the complete constitutional
purpose, initial policy, protected-principle definitions and voter addresses.
The creator is automatically the first voter. Every voter must personally attest
the **final** roster revision. Editing any pre-seal item invalidates all earlier
attestations. The creator can seal only with at least three voters, at least one
principle, and all attestations current.

Thereafter the following are immutable: who votes, what is constitutionally
protected, threshold percentages, removal delay, founder identity, genesis hash.
The founder has **no override** after sealing.

## State and causality

The first head commits to the entire sealed charter and exact initial policy.
Each subsequent head commits to its parent, exact replacement hash, proposal ID,
semantic receipt and version. All proposals record the base head/version; only a
proposal matching the current head can be queued or executed. An independent
one-shot consumer accepts only an executed proposal whose execution head **is
still current**.

Voters are indexed into a bounded bitset (up to nine members). A member casts at
most one yes/no vote per open proposal; retraction clears its own bit. Nonmembers
cannot propose or vote. Each member has at most one active proposal per head,
preventing an unbounded single-actor set of concurrently live proposals.

## Semantic classification

Inputs are entirely on-chain: purpose, current canonical policy, full replacement
policy, immutable indexed principles. No live webpage changes the criteria. The
title is not included in the prompt. The leader returns one class per principle
plus a short reason and witness; the validator checks shape and independently
recomputes the full vector. A second audit tries to falsify N and detect cases
where M/E disguises R. Any audit uncertainty or missed classification rejects
the leader result. Malformed responses become U, never an ordinary vote.

The final stored witness is **leader-reported, not independently certified**.
It is useful for a human audit, not for any deterministic branch. Numerical
quorums and transitions come solely from the frozen policy table.

## Exact statuses

| Code | Meaning | Possible next transition |
| ---: | --- | --- |
| 1 | OPEN / awaiting approvals | QUEUED or CANCELLED |
| 2 | BLOCKED / uncertain classification | None |
| 3 | QUEUED / approval threshold met | EXECUTED after delay, or CANCELLED |
| 4 | EXECUTED / policy head updated | None |
| 5 | CANCELLED / proposer withdrew | None |

Proposals from a previous head remain as audit records but are never executable.

## Limits

At most nine voters, eight named protected principles, 4000 characters of
policy per version, 500 characters per principle. The bounded audit vector
helps keep validator tasks manageable. Excessively complicated constitutions
must be decomposed into separate protected domains, not silently truncated.
