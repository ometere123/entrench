# Security model and hostile review

## Threat inventory

| Threat | Mechanism / status |
| --- | --- |
| Harmless-sounding title hides rights removal | Title excluded from semantic prompt; full old/new policy compared |
| Proposer submits “ordinary” verdict | No class parameter accepted; contract runs its own validator assessment |
| Malicious leader marks removal N | Validator independently classifies; audit searches for covert removal |
| Validator agreement is still wrong | **Residual** semantic risk; cannot promise mathematical certainty |
| Prompt injection embedded in new policy | Explicit untrusted delimiters; validator independently checks impact |
| Response misses a protected principle | Fixed-length vector; malformed/missing entries become U |
| LLM invents voting threshold | Thresholds hardcoded in deterministic contract code |
| Founder changes protected principle after votes | No write interface after seal; roster revision attestations |
| Founder enrolls wallets without their consent | Each must attest the final charter before sealing |
| One voter impersonates multiple votes | Sender-indexed yes/no masks; no signed payload delegation |
| Outside wallet casts votes | Sender membership check |
| Duplicate or opposing votes | Disjoint bit masks; changing vote requires retraction |
| Execution immediately after removal vote | 86400-second deterministic transaction-time delay |
| Proposal replays against new constitution | Base-head and base-version checks on queue/execute |
| Consumer uses superseded policy receipt | `is_executed(pid, expected_head)` also checks current head |
| Double consumer use | Permanent one-shot flag |
| Malicious or broken RPC points to wrong Studio | Pre-deployment exact `eth_chainId` guard, fail closed |
| Global rc CLI uses different protocol | Node dependency is locked to local CLI 0.39.1 |
| Consumer assumes ACCEPTED is final | Deployment runbook requires FINALIZED and execution success |
| Large prompt or on-chain history abuse | Bounded policy/rules; one live proposal per member per head |

## Honest guarantees

The governance quorum is deterministic **assuming** a correctly accepted
semantic classification. Entrench makes misclassification harder and permits
adversarial tests/appeals, but semantic agreement is not an oracle of legal truth.
The public network may be reset; recorded Git evidence must refer to actual
receipts and independently matched deployed source.

Attestations verify each voter participated in the seal workflow, not that an
underlying identity is a human. A single actor controlling multiple registered
wallets remains a governance/Sybil design risk; register only trusted distinct
governors. The charter is intentionally immutable: wallet loss can make a 90%
threshold impossible. This is a constitutional tradeoff, not a hidden override.

The initial policy can itself contain contradictory language. Users should
review and sign the exact genesis hash before sealing. Smart-contract validity
does not substitute for external legal advice.
