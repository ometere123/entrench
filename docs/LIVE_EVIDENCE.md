# StudioNet 61999 live evidence ledger

This ledger records only receipts and readbacks obtained from the required
StudioNet RPC. Explorer links are references for independent review; the
receipt status and execution result were checked through `genlayer-js` and the
chain RPC.

## Network and source

| Item | Verified value |
| --- | --- |
| Network | `studionet` |
| Chain ID | `61999` via `eth_chainId` |
| RPC | `https://studio.genlayer.com/api` |
| Local CLI | `genlayer@0.39.1` |
| Stable Direct Mode bundle | `v0.2.12` |
| Deployable source commit | `c806390a342b81f06dfa18ff71c2478fc9579df0` (later documentation-only commits do not change either contract) |

## Finalized corrected deployments and exact source parity

| Contract | Address | Deployment transaction | Receipt |
| --- | --- | --- | --- |
| Entrench | [`0x0fd3823b7f08F73275AABf60e88bEc9A1c507314`](https://explorer-studio.genlayer.com/address/0x0fd3823b7f08F73275AABf60e88bEc9A1c507314) | [`0x5f91ffd0e8ff6854b2d03c12ece6f426e08b45821c4e07dff5d4879d5bb458da`](https://explorer-studio.genlayer.com/tx/0x5f91ffd0e8ff6854b2d03c12ece6f426e08b45821c4e07dff5d4879d5bb458da) | FINALIZED, `MAJORITY_AGREE`, leader execution `SUCCESS` |
| ConstitutionalActionGate | [`0x4a51a85C33604B9B7F1C9347bF944853fE8F632f`](https://explorer-studio.genlayer.com/address/0x4a51a85C33604B9B7F1C9347bF944853fE8F632f) | [`0x84682211416ec86309796c82a1ec57b7eb6b0736a4627614113222d1af2b359d`](https://explorer-studio.genlayer.com/tx/0x84682211416ec86309796c82a1ec57b7eb6b0736a4627614113222d1af2b359d) | FINALIZED, `MAJORITY_AGREE`, leader execution `SUCCESS` |

The deployed code was fetched with `gen_getContractCode` and compared byte for
byte:

```text
Entrench: 4f504b32ff3246db0c72382dbeec2c93070caac6018cd7d861f93fa6235c8899
Consumer: 29024997d1331874cb44e5d3db7b3dc689fcbfcfb761a9543a8c76dd42c7396a
```

Both remote byte lengths and local byte lengths matched, and both comparisons
returned `match: true`.

## Recorded lifecycle

All hashes below are finalized StudioNet transactions unless explicitly marked
as a semantic disagreement. Each link is an explorer reference.

| Action | Transaction |
| --- | --- |
| Charter genesis | [`0xa2763de38dfc661d3d616a160734f103ae42c16fa3ea4d683301d5f9e7dddbd0`](https://explorer-studio.genlayer.com/tx/0xa2763de38dfc661d3d616a160734f103ae42c16fa3ea4d683301d5f9e7dddbd0) |
| Add five-member roster | [`0x05997eb6c46acdbdbd168ed35c207a9dba12ba1f6a214134d532a873c70e6af8`](https://explorer-studio.genlayer.com/tx/0x05997eb6c46acdbdbd168ed35c207a9dba12ba1f6a214134d532a873c70e6af8), [`0xa5c3b0e26c40f0f2bf453de15e483f314f52a0d9dc1a071ea394b50dc1608d37`](https://explorer-studio.genlayer.com/tx/0xa5c3b0e26c40f0f2bf453de15e483f314f52a0d9dc1a071ea394b50dc1608d37), [`0xd1c8be47624c5ede4b74e9fddfa1dfd79849ee1a909ef2558578eacf1e6a8015`](https://explorer-studio.genlayer.com/tx/0xd1c8be47624c5ede4b74e9fddfa1dfd79849ee1a909ef2558578eacf1e6a8015), [`0x062f844fbf30cef1b578f710f55a1ac8c8fb2f6d3be3a44054f86305d9121e9c`](https://explorer-studio.genlayer.com/tx/0x062f844fbf30cef1b578f710f55a1ac8c8fb2f6d3be3a44054f86305d9121e9c), [`0x56a4f74071f842d4a5a852576dd414f454343dcb6beba5d6325b649a97676691`](https://explorer-studio.genlayer.com/tx/0x56a4f74071f842d4a5a852576dd414f454343dcb6beba5d6325b649a97676691) |
| Final member attestations | [`0x57b346d396ba312d5840dd33aaf9a91abeb6a0435b470888c252657e712a39ae`](https://explorer-studio.genlayer.com/tx/0x57b346d396ba312d5840dd33aaf9a91abeb6a0435b470888c252657e712a39ae), [`0xb993079a9aef49d7290711234b7fa6ed2f294e1b28f8a064106ec8b71c8e16d2`](https://explorer-studio.genlayer.com/tx/0xb993079a9aef49d7290711234b7fa6ed2f294e1b28f8a064106ec8b71c8e16d2), [`0xc6d5e9fc9b681e2a27a0a71da9df1b3ebd49d225cc816bf1390753701cbf8a8f`](https://explorer-studio.genlayer.com/tx/0xc6d5e9fc9b681e2a27a0a71da9df1b3ebd49d225cc816bf1390753701cbf8a8f), [`0x4268380eeea7698a0ae275d8e82a69e68bed2ef3ce45fd0370222d86068afe87`](https://explorer-studio.genlayer.com/tx/0x4268380eeea7698a0ae275d8e82a69e68bed2ef3ce45fd0370222d86068afe87), [`0xc5b4cd85a6a28c1cd1e9156b1732130c1a4e59d07046669e06570f3e81c563ef`](https://explorer-studio.genlayer.com/tx/0xc5b4cd85a6a28c1cd1e9156b1732130c1a4e59d07046669e06570f3e81c563ef) |
| Charter seal | [`0xe30501b545277edc64b2ebe038abaa5a3bbee9160dede21c086267e5e57cfb9c`](https://explorer-studio.genlayer.com/tx/0xe30501b545277edc64b2ebe038abaa5a3bbee9160dede21c086267e5e57cfb9c) |
| Post-seal mutation rejected | [`0x96c646f096c269c35a9945c7db4a6a324ab9fd9ede4e6fec5cd74097ec348bfa`](https://explorer-studio.genlayer.com/tx/0x96c646f096c269c35a9945c7db4a6a324ab9fd9ede4e6fec5cd74097ec348bfa), finalized majority-agree receipt with leader rollback `IMMUTABLE_CHARTER` |
| Ordinary proposal | [`0x30035de1eb1956fce5f49f66bc79e9b0031066b9d12039a6a37db673ee48bab0`](https://explorer-studio.genlayer.com/tx/0x30035de1eb1956fce5f49f66bc79e9b0031066b9d12039a6a37db673ee48bab0) |
| Ordinary votes A/B/C | [`0x91e5ac56fb637907097b1dabdc3c7b028b6e8de0f3fc9f4e54a310fce87daeec`](https://explorer-studio.genlayer.com/tx/0x91e5ac56fb637907097b1dabdc3c7b028b6e8de0f3fc9f4e54a310fce87daeec), [`0x6be98be69f1321009c4a9bb113b59226f99f69ba85e6482ad81f4bf08b74d1b5`](https://explorer-studio.genlayer.com/tx/0x6be98be69f1321009c4a9bb113b59226f99f69ba85e6482ad81f4bf08b74d1b5), [`0xb053f92b91fd254168a08df10ab5d9c3a105ae0a8420028d00ba88c66db3cd5a`](https://explorer-studio.genlayer.com/tx/0xb053f92b91fd254168a08df10ab5d9c3a105ae0a8420028d00ba88c66db3cd5a) |
| Ordinary queue / execute | [`0xc932c074c0172a9dd4859bda4433188406cb7a9a6a045bca94c5f1637e3d946c`](https://explorer-studio.genlayer.com/tx/0xc932c074c0172a9dd4859bda4433188406cb7a9a6a045bca94c5f1637e3d946c), [`0xcfb5f519ba5b483013556d6a26def5252f2979190555293ac8c69624efbc2d45`](https://explorer-studio.genlayer.com/tx/0xcfb5f519ba5b483013556d6a26def5252f2979190555293ac8c69624efbc2d45) |
| Protected-tier expansion proposal | [`0xced78db6ba0fc9af035a82bc37b16447c93c993bd76e04b7df2bec21092e0131`](https://explorer-studio.genlayer.com/tx/0xced78db6ba0fc9af035a82bc37b16447c93c993bd76e04b7df2bec21092e0131), finalized `MAJORITY_AGREE`; readback vector `E`, `PROTECTED`, 75%, required 4 |
| Protected-tier votes A/B/C/D | [`0x5349355d202fdc1e7782415095a7684edf4332ea7c136a21a85887c5383ae3c9`](https://explorer-studio.genlayer.com/tx/0x5349355d202fdc1e7782415095a7684edf4332ea7c136a21a85887c5383ae3c9), [`0xbcb4464d32f1c50e87dd2c9292a75239dcac5bee01851b9b5926d5d156202a9f`](https://explorer-studio.genlayer.com/tx/0xbcb4464d32f1c50e87dd2c9292a75239dcac5bee01851b9b5926d5d156202a9f), [`0x566a4700a21eec23588cc15e68a9f676e0ddc68f332d1ce7ec74bfcfb0637514`](https://explorer-studio.genlayer.com/tx/0x566a4700a21eec23588cc15e68a9f676e0ddc68f332d1ce7ec74bfcfb0637514), [`0xbc0666c1047f9209c28601c3c29ec3a869879603e513eb921a6c7af6893757e2`](https://explorer-studio.genlayer.com/tx/0xbc0666c1047f9209c28601c3c29ec3a869879603e513eb921a6c7af6893757e2); all FINALIZED, `MAJORITY_AGREE` |
| Protected-tier queue / execute | [`0xe1f2df7c660d7266ffc7731e49c30ba59dd7e637e8f3332278efc9dbc8ac3c4f`](https://explorer-studio.genlayer.com/tx/0xe1f2df7c660d7266ffc7731e49c30ba59dd7e637e8f3332278efc9dbc8ac3c4f), [`0xaeab8de95bcec71aa30bed1874c2dbe15bbc20a6d88dc791d937b3633c4f0ac6`](https://explorer-studio.genlayer.com/tx/0xaeab8de95bcec71aa30bed1874c2dbe15bbc20a6d88dc791d937b3633c4f0ac6); all FINALIZED, `MAJORITY_AGREE`; new head `1e0ad8c9b76994f88a88b1299fb3ad05c41da6f88e909de0055961b1379ff8a8` |
| Consumer typed IC-to-IC success | [`0x4d3022ec356c8e7343a485eaf708fc29a2caaef723d30317697603bf30136ce0`](https://explorer-studio.genlayer.com/tx/0x4d3022ec356c8e7343a485eaf708fc29a2caaef723d30317697603bf30136ce0), finalized majority-agree, leader `SUCCESS`; `did_perform == true` |
| Consumer replay rejected | [`0x5bce7ff5f3e054dd3438f8745ac9dde9f7a304ad887eba675c85980649f36044`](https://explorer-studio.genlayer.com/tx/0x5bce7ff5f3e054dd3438f8745ac9dde9f7a304ad887eba675c85980649f36044), finalized majority-agree, leader rollback `ONE_SHOT`; `did_perform` remained `true` |
| Superseded-head readback | `is_executed(1, c06345ce8f3f9265346ec773cf870338b9bdb187c5ee1f27b4b8ed71143a7f6c) == false`; `is_executed(2, 1e0ad8c9b76994f88a88b1299fb3ad05c41da6f88e909de0055961b1379ff8a8) == true` |

## Live semantic-consensus limitation

The live material and removal proposals were submitted with exact frozen
heads and finalized without a state transition because the validator set
reached `MAJORITY_DISAGREE`. The observed transactions were:

- M-tier attempt: [`0xd31bad8f82dc1c80b691ed42b5b52ac355d7ab714fb8b1f70ffe4d29dd7ea727`](https://explorer-studio.genlayer.com/tx/0xd31bad8f82dc1c80b691ed42b5b52ac355d7ab714fb8b1f70ffe4d29dd7ea727)
- M-tier retry: [`0x76b4f990322a42922ad13e1c9d38961fa6a32242064ea3ef062caa5445ca12c0`](https://explorer-studio.genlayer.com/tx/0x76b4f990322a42922ad13e1c9d38961fa6a32242064ea3ef062caa5445ca12c0)
- R-tier disguised removal: [`0x0de1ba9e68b131ae3708bcbd4786e5a5d6a272cd5b368bb4a80a9e36029de4b7`](https://explorer-studio.genlayer.com/tx/0x0de1ba9e68b131ae3708bcbd4786e5a5d6a272cd5b368bb4a80a9e36029de4b7)
- Clear removal against the post-expansion head: [`0xee608ecf0e7229d2680eb82c8b043265c7d0b6e4c9b257ba6b8a2cae2bd5cee0`](https://explorer-studio.genlayer.com/tx/0xee608ecf0e7229d2680eb82c8b043265c7d0b6e4c9b257ba6b8a2cae2bd5cee0)
- Removal retry against the same post-expansion head: [`0x2f8feff1215f3d483709307e6fc38353087cf96578f566cefe0803eeb38f484e`](https://explorer-studio.genlayer.com/tx/0x2f8feff1215f3d483709307e6fc38353087cf96578f566cefe0803eeb38f484e)

This is a genuine fail-closed network result, not evidence that the removal
classification succeeded. Consequently, this ledger does **not** claim a live
75% or 90% proposal, a five-vote removal queue, or the 24-hour public-chain
timelock execution. The exact-tier and boundary behavior is covered by the
26 stable Direct Mode tests. A final submission should remain BLOCKED until a
stable 61999 semantic-consensus run produces a genuine R result and the
remaining live removal gate is independently captured. The 75% protected
path is now live-verified through the `E` expansion above; only the 90%
removal classification, five-vote queue and 24-hour execution remain
unverified because the network has not reached consensus on a removal.

## Historical removal-consensus root-cause investigation

The latest bounded removal retry was inspected as a full transaction object,
not only through the explorer summary:

- [`0x2f8feff1215f3d483709307e6fc38353087cf96578f566cefe0803eeb38f484e`](https://explorer-studio.genlayer.com/tx/0x2f8feff1215f3d483709307e6fc38353087cf96578f566cefe0803eeb38f484e)
  finalized as `MAJORITY_DISAGREE`.
- The leader executed with `SUCCESS` and no GenVM error.
- The aggregate vote map contained three `disagree` votes, one `agree` vote
  and one `idle` validator. The non-idle disagree entries exposed in the
  receipt and consensus history had `execution_result: SUCCESS`, no
  `genvm_result.error_code`, empty stdout and stderr, and
  `nondet_disagree: 0`. The idle validator reported only
  `CONSENSUS_VALIDATOR_QUORUM_REACHED`, which is cancellation after quorum,
  not the cause of the disagreement.
- The earlier M-tier, disguised-R and clear-R attempts show the same pattern:
  successful leader execution followed by successful validator disagreement;
  none produced a stored proposal or a state transition.

This establishes that the live failure is a validator-level rejection of the
leader's consensus predicate, not a leader VM crash, malformed transaction,
GenVM runtime error, or RPC finalization failure. It does **not** establish
whether a validator rejected because the normalized classification vector did
not exactly match, because the adversarial audit returned uncertainty or a
misclassification, or because an internal response was malformed. The stable
RPC exposes the validator vote and execution envelope but not the internal
`exec_prompt` responses or the boolean rejection branch. The documented
`gen_dbg_traceTransaction` method is also unavailable on this RPC
(`-32601 Method not found`), so no deeper receipt trace can substantiate one
of those sub-causes.

The stable Direct Mode suite reproduces each branch independently: a leader N
versus validator R result is rejected; a validator audit marking a hidden
removal is rejected; malformed leader responses become terminal U/blocked
proposals; and the multi-principle `NR` case maps deterministically to the
REMOVAL class. The historical suite was 26/26; the final pinned suite is 27/27, including the exact
`available_at - 1` and `available_at` removal-delay boundaries. These are
controlled test inputs, not live validator observations.

No production contract correction was applied from those receipts alone. Changing
vector equality, accepting audit uncertainty, or trusting the leader would
make removal liveness appear better by weakening the independent safety gate.
The production `REMOVAL_DELAY` therefore remains 86400 seconds. There is no
migration impact from that historical investigation because the later
correction was a fresh immutable deployment; the old deployed address was not
mutated.

## Corrected production deployment and removal gate

The source correction was included in source/test-variant commit `c806390a342b81f06dfa18ff71c2478fc9579df0`.
It changes only the semantic prompts: removal-first precedence is explicit in
both leader and independent-validator prompts, while exact vector agreement,
adversarial-audit rejection, thresholds and `REMOVAL_DELAY = 86400` are
unchanged. The prior deployed addresses remain historical; these are the
corrected production addresses.

| Contract | Address | Deployment transaction | Source parity |
| --- | --- | --- | --- |
| Corrected Entrench | [`0x0fd3823b7f08F73275AABf60e88bEc9A1c507314`](https://explorer-studio.genlayer.com/address/0x0fd3823b7f08F73275AABf60e88bEc9A1c507314) | [`0x5f91ffd0e8ff6854b2d03c12ece6f426e08b45821c4e07dff5d4879d5bb458da`](https://explorer-studio.genlayer.com/tx/0x5f91ffd0e8ff6854b2d03c12ece6f426e08b45821c4e07dff5d4879d5bb458da) | FINALIZED, `MAJORITY_AGREE`, leader `SUCCESS`; SHA-256 `4f504b32ff3246db0c72382dbeec2c93070caac6018cd7d861f93fa6235c8899`, exact remote-byte match |
| Corrected ConstitutionalActionGate | [`0x4a51a85C33604B9B7F1C9347bF944853fE8F632f`](https://explorer-studio.genlayer.com/address/0x4a51a85C33604B9B7F1C9347bF944853fE8F632f) | [`0x84682211416ec86309796c82a1ec57b7eb6b0736a4627614113222d1af2b359d`](https://explorer-studio.genlayer.com/tx/0x84682211416ec86309796c82a1ec57b7eb6b0736a4627614113222d1af2b359d) | FINALIZED, `MAJORITY_AGREE`, leader `SUCCESS`; SHA-256 `29024997d1331874cb44e5d3db7b3dc689fcbfcfb761a9543a8c76dd42c7396a`, exact remote-byte match |

The corrected five-wallet charter was finalized with genesis `0xb041b873be8b2b76e689ea65e83153b6ebe9beaed726e1fc9fefaf76d9365f94`, principle `0xddf2d511714873e86e7e42c5299689c2db2c9f6d7070ea2c3df9908b93aacc4d`, five member-add transactions, five finalized attestations, and seal `0x0c74b1559b00f984fa70f91166fd7475811f064eb132a0309245629daba834d4`. The sealed readback reported thresholds `[51,75,90]`, `removal_delay_seconds = 86400`, chain `61999`, and head `99e8d51c3b45e13b1c3d2f47a32816e71fdfc340b50360ad4b63f8a8dc21fd2a`.

The first corrected live removal proposal was transaction [`0x3faedadc74f86f9753aa891cc1fc8fda593c016b35f503c98f0f9bb35dbe9f5b`](https://explorer-studio.genlayer.com/tx/0x3faedadc74f86f9753aa891cc1fc8fda593c016b35f503c98f0f9bb35dbe9f5b), FINALIZED `MAJORITY_AGREE`, leader `SUCCESS`, with receipt votes 3 agree / 2 disagree. Readback: proposal `1`, vector `R`, `REMOVAL`, `90%`, `required_yes = 5`, exact frozen base head, status `OPEN`.

Four approvals were finalized. Queue attempt [`0x91612792f5ab7336dbd5754017e19a798dd270ef5b1c02b041f73a6207427e15`](https://explorer-studio.genlayer.com/tx/0x91612792f5ab7336dbd5754017e19a798dd270ef5b1c02b041f73a6207427e15) finalized consensus but leader rollback `INSUFFICIENT_APPROVALS`; no queue mutation occurred. The fifth approval and queue [`0x5e4bc1b5722eff30180550d3c6b48cfba24b8e0f96f6fd4f12e421ee2897236f`](https://explorer-studio.genlayer.com/tx/0x5e4bc1b5722eff30180550d3c6b48cfba24b8e0f96f6fd4f12e421ee2897236f) finalized with leader `SUCCESS`. Queue `created_at` was `2026-11-05T16:56:27.926688+00:00` / epoch `1793897787`; readback `available_at = 1793984187`, exactly `queue_time + 86400`.

Immediate execute [`0x23dd6e2698c624b0ff0c69961ca1df293a6cb7c36e611b5c87cb849b12fdb77d`](https://explorer-studio.genlayer.com/tx/0x23dd6e2698c624b0ff0c69961ca1df293a6cb7c36e611b5c87cb849b12fdb77d) finalized `MAJORITY_AGREE` with leader rollback `TIMELOCK_ACTIVE`; the proposal remained queued. Owner cancellation [`0x3013d244a1b6d45c7710318c53d2a73881e26f0c5cc0174c4d406b32a11e75a1`](https://explorer-studio.genlayer.com/tx/0x3013d244a1b6d45c7710318c53d2a73881e26f0c5cc0174c4d406b32a11e75a1) then finalized successfully with proposal status `CANCELLED`.

For reusable functionality, ordinary proposal `2` finalized as `N`/`ORDINARY`, then queue [`0x04a369f29b598cfd67df4c4561fb9abfb8a19af596e920ba3eadbd0103264801`](https://explorer-studio.genlayer.com/tx/0x04a369f29b598cfd67df4c4561fb9abfb8a19af596e920ba3eadbd0103264801) and execute [`0x23f9b3cd63546db67704b9ce905fde1704efe60900634ffa7f0f02647cef65d3`](https://explorer-studio.genlayer.com/tx/0x23f9b3cd63546db67704b9ce905fde1704efe60900634ffa7f0f02647cef65d3) finalized successfully, producing head `f3b7dfe3e72bbb567e37918a275c16a8dafe9cf99714dddf7cfbce131a87ede2`. The typed consumer was deployed against the exact address/proposal/head; `perform` [`0x6a7c3d6982fe6fc05a1bb4a83ab8ca1777297f45ab064ea8db21edc8466c4ffd`](https://explorer-studio.genlayer.com/tx/0x6a7c3d6982fe6fc05a1bb4a83ab8ca1777297f45ab064ea8db21edc8466c4ffd) finalized successfully and `did_perform == true`. Replay [`0xcef3d4bcb1cf14b8daf1dbaba97fe7864dee24a74e4c7bde3414e69469d8cf7a`](https://explorer-studio.genlayer.com/tx/0xcef3d4bcb1cf14b8daf1dbaba97fe7864dee24a74e4c7bde3414e69469d8cf7a) finalized with leader rollback `ONE_SHOT`; readback remained `true`.

## Test-only 900-second deployment and lifecycle

The isolated source `contracts/test_only_900/entrench.py` is byte-for-byte the
production source except for `REMOVAL_DELAY = 900`; its manifest hash is
`670326b4dd4e2d7577706b523e506e694aff1065d8fd9da970f079f90b46d4ce`. It passed
stable v0.2.12 lint, validation and schema checks. The first three guarded
deployment requests were finalized with leader `contract_error` and
`result.payload = invalid_contract`; those returned no usable contract code.
The subsequent three requests finalized with leader `SUCCESS`, and the latest
source-matched test-only address is
`0xF5D85F57b6095aAe3d06D64AE7f847866EB28e1C`. Its deployed bytes are exactly
22017 bytes and match SHA-256
`670326b4dd4e2d7577706b523e506e694aff1065d8fd9da970f079f90b46d4ce`.

The latest successful deployment has been read back with
`removal_delay_seconds = 900`, chain `61999`, and an initially unsealed
charter. The successful test-only deployment receipts are:

| Address | Deployment transaction | Created (UTC) | Receipt |
| --- | --- | --- | --- |
| `0xcA271Ae9970EA7d5477aF81f8137897B763530Bb` | [`0xfd98a2801b8d8b7e9b6b5c2f5c970822b6396fdaadfff29635e5dfabcacecd28`](https://explorer-studio.genlayer.com/tx/0xfd98a2801b8d8b7e9b6b5c2f5c970822b6396fdaadfff29635e5dfabcacecd28) | 2026-11-05T17:34:14Z | FINALIZED, `MAJORITY_AGREE`, leader `SUCCESS` |
| `0x075D03Aecc9fB329183e0a49b431b33EE34A610D` | [`0xd005b9eece5ffc2cae189a3252c5444b9ff930404ef18a5ac02bdd9449a8b8fc`](https://explorer-studio.genlayer.com/tx/0xd005b9eece5ffc2cae189a3252c5444b9ff930404ef18a5ac02bdd9449a8b8fc) | 2026-11-05T17:35:49Z | FINALIZED, `MAJORITY_AGREE`, leader `SUCCESS` |
| `0xF5D85F57b6095aAe3d06D64AE7f847866EB28e1C` | [`0xfbbe67b015c78b9439508d50e29787c0fb47dba6c60f31ba1f0bd5ecfe313c36`](https://explorer-studio.genlayer.com/tx/0xfbbe67b015c78b9439508d50e29787c0fb47dba6c60f31ba1f0bd5ecfe313c36) | 2026-11-05T17:40:07Z | FINALIZED, `MAJORITY_AGREE`, leader `SUCCESS` |

The complete test-only 900-second lifecycle was then finalized on the latest
address. It used five distinct signers (the original participant keystores did
not share the owner password, so four disposable replacement accounts were
created and funded from the owner; no production contract or source changed):

| Role | Signer address |
| --- | --- |
| Owner / A | `0x0d5540e0aD4B92Aa0ad4e5F1b8cD645ee1E363E7` |
| B | `0x0403F5D997Efe034581d917FBA48237fE13453F8` |
| C | `0x3013e3C5cC568d76DE2727514985Da2bf077663f` |
| D | `0x7107772C1bEE3530a35184fFBEB0E0e880e71Ca1` |
| E | `0xd942A3188218eDed2b5c16dd6c733A65BA5F487f` |

The owner initialized the charter with [`0x1fc6b84e0c24d37f4d7395f44b980f1914828605d9aa41d558a052ec5d75498c`](https://explorer-studio.genlayer.com/tx/0x1fc6b84e0c24d37f4d7395f44b980f1914828605d9aa41d558a052ec5d75498c) at `2026-11-05T19:59:12Z`, added the protected principle with [`0xa84b4fe544843f41f3855905673a6d79f0dd3b26ba4863593d1c2c0dcf775c7f`](https://explorer-studio.genlayer.com/tx/0xa84b4fe544843f41f3855905673a6d79f0dd3b26ba4863593d1c2c0dcf775c7f), and registered B–E with [`0x3a60d1d8928812b1cc8c4037768a35ab330b9fd85aaafcd73d068db876a584ef`](https://explorer-studio.genlayer.com/tx/0x3a60d1d8928812b1cc8c4037768a35ab330b9fd85aaafcd73d068db876a584ef), [`0xf0d7a982f7e391c9a29a8c57b8391852e5713d2e1fe005185025151b7736d032`](https://explorer-studio.genlayer.com/tx/0xf0d7a982f7e391c9a29a8c57b8391852e5713d2e1fe005185025151b7736d032), [`0x5c5703ad64134056bd0a54ce1e5ce018cbf78b26bd75e4dced85b65e5dc9cb9c`](https://explorer-studio.genlayer.com/tx/0x5c5703ad64134056bd0a54ce1e5ce018cbf78b26bd75e4dced85b65e5dc9cb9c) and [`0xc6875b897a2c2224960b049296721b59575f67557fd4d4a5ec352c267b77a223`](https://explorer-studio.genlayer.com/tx/0xc6875b897a2c2224960b049296721b59575f67557fd4d4a5ec352c267b77a223). Each transaction finalized with `MAJORITY_AGREE` and leader `SUCCESS`.

All five signers independently attested the final revision:

| Signer | Attestation transaction | Created (UTC) |
| --- | --- | --- |
| A | [`0x54b318f8ce126a0891f55250a7c18cd81338be503c3c81d962fc35e76d8b2a21`](https://explorer-studio.genlayer.com/tx/0x54b318f8ce126a0891f55250a7c18cd81338be503c3c81d962fc35e76d8b2a21) | 2026-11-05T20:12:49Z |
| B | [`0xa30f694ac5b181e3fa711ce57ec1496146fcdb3c7c4c28bb6269a8d3e8bf0f5d`](https://explorer-studio.genlayer.com/tx/0xa30f694ac5b181e3fa711ce57ec1496146fcdb3c7c4c28bb6269a8d3e8bf0f5d) | 2026-11-05T20:12:53Z |
| C | [`0xfca0a00b01c0e99b2925474f6b04962eb3df00e0bb1a5b7513ec3db285602588`](https://explorer-studio.genlayer.com/tx/0xfca0a00b01c0e99b2925474f6b04962eb3df00e0bb1a5b7513ec3db285602588) | 2026-11-05T20:12:57Z |
| D | [`0x5a2ccf36d960afbfb2298fb4644544aa42cad27a4ce1c8785bba652c8f82a823`](https://explorer-studio.genlayer.com/tx/0x5a2ccf36d960afbfb2298fb4644544aa42cad27a4ce1c8785bba652c8f82a823) | 2026-11-05T20:13:02Z |
| E | [`0x93977255b8c3e6db3314329615371f98213ef8d785d777e2b3dbefce992ad893`](https://explorer-studio.genlayer.com/tx/0x93977255b8c3e6db3314329615371f98213ef8d785d777e2b3dbefce992ad893) | 2026-11-05T20:13:07Z |

The charter was sealed by [`0xc0533734e983635d3ab8e44cae7ce3d522d8fc287ab37f1fdbe9054f9c47ba49`](https://explorer-studio.genlayer.com/tx/0xc0533734e983635d3ab8e44cae7ce3d522d8fc287ab37f1fdbe9054f9c47ba49) at `2026-11-05T20:15:10Z`. Readback: five members, thresholds `[51,75,90]`, `removal_delay_seconds = 900`, sealed `true`, and frozen head `131239bd2294e358d9079577ef57624846ab403ad4934ed65b47e5f92d819821`.

The genuine removal proposal was [`0xaa5b0a9a95ac9f3db4f69b328137e1db1c29aebf13096ac891bd50fef39135f0`](https://explorer-studio.genlayer.com/tx/0xaa5b0a9a95ac9f3db4f69b328137e1db1c29aebf13096ac891bd50fef39135f0), finalized at `2026-11-05T20:16:21Z` with `MAJORITY_AGREE`, leader `SUCCESS`, three agree / two disagree votes. Canonical readback classified it as vector `R`, `REMOVAL`, `90%`, `required_yes = 5`, exact base head, and witness text grounded in the withdrawal-right removal.

Four approvals finalized in [`0xe87092a046f0e538bc20a00d9462f403eac4f0642e296df3e1b6003d7de56c37`](https://explorer-studio.genlayer.com/tx/0xe87092a046f0e538bc20a00d9462f403eac4f0642e296df3e1b6003d7de56c37), [`0x754a610ef3fef53f825c17d1ad1fbb805cfcc4a5d4ddeaebfc1b7f508bd842a4`](https://explorer-studio.genlayer.com/tx/0x754a610ef3fef53f825c17d1ad1fbb805cfcc4a5d4ddeaebfc1b7f508bd842a4), [`0xb8a0d30566a41511eaf89a038fc0d909a03dd4d91355cabfd891df0eb20af599`](https://explorer-studio.genlayer.com/tx/0xb8a0d30566a41511eaf89a038fc0d909a03dd4d91355cabfd891df0eb20af599) and [`0xb1dbc867592de4c78accb4e5c20a3cacec8a5dc531bfefcae6cef729cd784925`](https://explorer-studio.genlayer.com/tx/0xb1dbc867592de4c78accb4e5c20a3cacec8a5dc531bfefcae6cef729cd784925). The four-approval queue attempt [`0x5827f09198fed260b6e3e57033fcc2b3e62b7c1e4ab11d0afd18d22c7a44c22a`](https://explorer-studio.genlayer.com/tx/0x5827f09198fed260b6e3e57033fcc2b3e62b7c1e4ab11d0afd18d22c7a44c22a) finalized consensus but rolled back with `INSUFFICIENT_APPROVALS`; readback showed `yes_count = 4`, `yes_mask = 15`, and no queue mutation.

The fifth approval [`0x00c2b6424204250546ddba6e26f447c666ac184a09f650603814b1475d30efc8`](https://explorer-studio.genlayer.com/tx/0x00c2b6424204250546ddba6e26f447c666ac184a09f650603814b1475d30efc8) finalized successfully. Queue [`0x4352cc7b2bee54d9ea33892a605aa5f60c8c83f1f0fe84c4717fa64431283ce5`](https://explorer-studio.genlayer.com/tx/0x4352cc7b2bee54d9ea33892a605aa5f60c8c83f1f0fe84c4717fa64431283ce5) finalized at `2026-11-05T20:22:00Z` / epoch `1793910120`; readback showed `yes_count = 5`, `yes_mask = 31`, `available_at = 1793911020`, exactly `queue_time + 900`.

Immediate execution [`0x976be31d39f4a71f671bd431a505d3852a061e53c6eb948f94c7ea6a650e6045`](https://explorer-studio.genlayer.com/tx/0x976be31d39f4a71f671bd431a505d3852a061e53c6eb948f94c7ea6a650e6045) finalized consensus at `2026-11-05T20:24:06Z` but rolled back with `TIMELOCK_ACTIVE`; the proposal remained queued. After repeated on-chain readbacks confirmed the deadline had passed (`now = 1793911408`, `available_at = 1793911020`), final execution [`0x4b908232661e5c176ae162a9e06da6dfa41ac291c6e3afd1c3fbd90a08434835`](https://explorer-studio.genlayer.com/tx/0x4b908232661e5c176ae162a9e06da6dfa41ac291c6e3afd1c3fbd90a08434835) finalized at `2026-11-05T20:43:48Z` with leader `SUCCESS`. Readback is `status = EXECUTED`, `execution_head = eb6008a6a5a04e4ef2382b235b93184b9535bab31e6635ede20c5f4f5489cfad`, charter `version = 2`, and the replacement policy no longer contains the withdrawal right.

The first four member broadcasts used plain strings and rolled back with the stable runtime error `str` has no `as_bytes`; they mutated no state. The successful retries above used `genlayer-js/types.CalldataAddress`, demonstrating that the live path uses the proper typed GenLayer address encoding required by the ABI.

This is a shortened-delay integration test only. It proves the 900-second test variant's state machine and finality, not the passage of the canonical production 86400-second timelock. Production remains unchanged and its removal was intentionally canceled after the early-rejection proof.
