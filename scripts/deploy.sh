#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
contract="${1:-}"
if [[ "$contract" != "contracts/entrench.py" && "$contract" != "contracts/consumer_gate.py" ]]; then
  echo "Specify contracts/entrench.py or contracts/consumer_gate.py" >&2
  exit 2
fi
if [[ "${ENTRENCH_DEPLOY_ACK:-}" != "61999" ]]; then
  echo "Set ENTRENCH_DEPLOY_ACK=61999 to authorize a live deployment." >&2
  exit 2
fi
python3 scripts/preflight.py
npm run network:check
if [[ "$(node -p "require('./node_modules/genlayer/package.json').version")" != "0.39.1" ]]; then
  echo "Expected repository-local CLI 0.39.1" >&2
  exit 2
fi
# The CLI is invoked through node_modules; nothing touches the global CLI.
npm exec -- genlayer network set studionet
npm exec -- genlayer network info
echo "Check above info shows alias studionet, chain 61999, stable RPC."
read -r -p "Type 61999 to continue broadcasting a LIVE deploy: " explicit_ack
[[ "$explicit_ack" == "61999" ]] || exit 3
npm exec -- genlayer deploy --contract "$contract"
echo "Save actual tx hash and deployed address. Verify FINALIZED + execution success."
