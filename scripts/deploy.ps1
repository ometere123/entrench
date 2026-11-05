param(
  [ValidateSet('contracts/entrench.py', 'contracts/consumer_gate.py')]
  [string]$Contract
)

$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')

if (-not $Contract) {
  throw 'Specify contracts/entrench.py or contracts/consumer_gate.py'
}
if ($env:ENTRENCH_DEPLOY_ACK -ne '61999') {
  throw 'Set ENTRENCH_DEPLOY_ACK=61999 to authorize a live deployment.'
}

& py -3 scripts/preflight.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
node scripts/network-guard.cjs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$cli = Join-Path (Get-Location) 'node_modules\.bin\genlayer.cmd'
if (-not (Test-Path -LiteralPath $cli)) { throw 'MISSING_LOCAL_CLI_EXECUTABLE' }
$version = (& $cli --version).Trim()
if ($version -ne '0.39.1') { throw "WRONG_LOCAL_CLI_VERSION:$version" }
& $cli network set studionet
& $cli network info
$explicitAck = Read-Host 'Type 61999 to continue broadcasting a LIVE deploy'
if ($explicitAck -ne '61999') { exit 3 }
& $cli deploy --contract $Contract
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host 'Save actual tx hash and deployed address. Verify FINALIZED + execution success.'
