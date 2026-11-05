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
| Deployable source commit | `3282664aa9ed3504563773b96d743affb83bb163` (later documentation-only commits do not change either contract) |

## Finalized deployments and exact source parity

| Contract | Address | Deployment transaction | Receipt |
| --- | --- | --- | --- |
| Entrench | [`0xE545b98d1c1Fce30421b64E55D71159984f7fd8d`](https://explorer-studio.genlayer.com/address/0xE545b98d1c1Fce30421b64E55D71159984f7fd8d) | [`0x1d3d1692d227b8cad3bc35e9e7cefc25d0f332f5392ea72e55c4e04d72c06703`](https://explorer-studio.genlayer.com/tx/0x1d3d1692d227b8cad3bc35e9e7cefc25d0f332f5392ea72e55c4e04d72c06703) | FINALIZED, `MAJORITY_AGREE`, leader execution `SUCCESS` |
| ConstitutionalActionGate | [`0xE1D0845B7A07e562C3f623Cb6668933AC14F363c`](https://explorer-studio.genlayer.com/address/0xE1D0845B7A07e562C3f623Cb6668933AC14F363c) | [`0x2060e239f115bd023200edf69705e7349a55b699460b184bda8de11ffe3dd86a`](https://explorer-studio.genlayer.com/tx/0x2060e239f115bd023200edf69705e7349a55b699460b184bda8de11ffe3dd86a) | FINALIZED, `MAJORITY_AGREE`, leader execution `SUCCESS` |

The deployed code was fetched with `gen_getContractCode` and compared byte for
byte:

```text
Entrench: a22ce1480c9dbc4c0263c48e4c835448a25dd303208eb5aa6bb0f2ea2b9db256
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
| Consumer typed IC-to-IC success | [`0x4d3022ec356c8e7343a485eaf708fc29a2caaef723d30317697603bf30136ce0`](https://explorer-studio.genlayer.com/tx/0x4d3022ec356c8e7343a485eaf708fc29a2caaef723d30317697603bf30136ce0), finalized majority-agree, leader `SUCCESS`; `did_perform == true` |
| Consumer replay rejected | [`0x5bce7ff5f3e054dd3438f8745ac9dde9f7a304ad887eba675c85980649f36044`](https://explorer-studio.genlayer.com/tx/0x5bce7ff5f3e054dd3438f8745ac9dde9f7a304ad887eba675c85980649f36044), finalized majority-agree, leader rollback `ONE_SHOT`; `did_perform` remained `true` |

## Live semantic-consensus limitation

The live material and removal proposals were submitted with exact frozen
heads and finalized without a state transition because the validator set
reached `MAJORITY_DISAGREE`. The observed transactions were:

- M-tier attempt: [`0xd31bad8f82dc1c80b691ed42b5b52ac355d7ab714fb8b1f70ffe4d29dd7ea727`](https://explorer-studio.genlayer.com/tx/0xd31bad8f82dc1c80b691ed42b5b52ac355d7ab714fb8b1f70ffe4d29dd7ea727)
- M-tier retry: [`0x76b4f990322a42922ad13e1c9d38961fa6a32242064ea3ef062caa5445ca12c0`](https://explorer-studio.genlayer.com/tx/0x76b4f990322a42922ad13e1c9d38961fa6a32242064ea3ef062caa5445ca12c0)
- R-tier disguised removal: [`0x0de1ba9e68b131ae3708bcbd4786e5a5d6a272cd5b368bb4a80a9e36029de4b7`](https://explorer-studio.genlayer.com/tx/0x0de1ba9e68b131ae3708bcbd4786e5a5d6a272cd5b368bb4a80a9e36029de4b7)

This is a genuine fail-closed network result, not evidence that the M/R
classification succeeded. Consequently, this ledger does **not** claim a live
75% or 90% proposal, a five-vote removal queue, or the 24-hour public-chain
timelock execution. The exact-tier and boundary behavior is covered by the
26 stable Direct Mode tests. A final submission should remain BLOCKED until a
stable 61999 semantic-consensus run produces a genuine M/R result and the
remaining live gates are independently captured.
