// Always execute the repository-local pinned GenLayer CLI package.
// This intentionally avoids npm exec's global fallback behavior when a local
// install is incomplete, and never resolves an unqualified `genlayer` command.
const { spawnSync } = require('node:child_process');
const { resolve } = require('node:path');

const root = resolve(__dirname, '..');
const packageJson = require(resolve(root, 'node_modules/genlayer/package.json'));
if (packageJson.version !== '0.39.1') {
  throw new Error(`WRONG_LOCAL_CLI_VERSION:${packageJson.version}`);
}

const entry = resolve(root, 'node_modules/genlayer/dist/index.js');
const result = spawnSync(process.execPath, [entry, ...process.argv.slice(2)], {
  cwd: root,
  stdio: 'inherit',
});
if (result.error) throw result.error;
process.exit(result.status ?? 1);
