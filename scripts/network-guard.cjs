// Hard-stop before any signing, deploying, or funding operation.
const fs = require('node:fs');
const { resolve } = require('node:path');
const root = resolve(__dirname, '..');
const config = JSON.parse(fs.readFileSync(resolve(root, 'network.json'), 'utf8'));
if (config.alias !== 'studionet' || config.chainId !== 61999
    || config.rpc !== 'https://studio.genlayer.com/api'
    || config.explorer !== 'https://explorer-studio.genlayer.com') {
  throw new Error('INVALID_PRODUCTION_PROFILE');
}
const installed = JSON.parse(fs.readFileSync(resolve(root, 'node_modules/genlayer/package.json'), 'utf8'));
if (installed.version !== '0.39.1') throw new Error('WRONG_LOCAL_CLI_VERSION');
const controller = new AbortController();
const t = setTimeout(() => controller.abort(), 12000);
(async () => {
  try {
    const response = await fetch(config.rpc, {
      method: 'POST',
      headers: { 'content-type': 'application/json' },
      body: JSON.stringify({ jsonrpc: '2.0', id: 1, method: 'eth_chainId', params: [] }),
      signal: controller.signal
    });
    if (!response.ok) throw new Error('RPC_HTTP_' + response.status);
    const rpc = await response.json();
    if (rpc.error || Number.parseInt(rpc.result, 16) !== 61999) {
      throw new Error('CHAIN_ID_MISMATCH_' + JSON.stringify(rpc));
    }
    console.log('Verified stable studionet: chain 61999; RPC ' + config.rpc
      + '; local genlayer CLI 0.39.1');
  } catch (error) {
    console.error('FAIL CLOSED: network not verified: ' + error.message);
    process.exitCode = 1;
  } finally { clearTimeout(t); }
})();
