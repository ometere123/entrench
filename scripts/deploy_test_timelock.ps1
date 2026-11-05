param()

$ErrorActionPreference = 'Stop'
Set-Location (Join-Path $PSScriptRoot '..')

$contract = 'contracts/test_only_900/entrench.py'
if (-not (Test-Path -LiteralPath $contract)) {
  throw 'MISSING_TEST_ONLY_CONTRACT'
}
if ($env:ENTRENCH_TEST_ONLY_ACK -ne '900') {
  throw 'Set ENTRENCH_TEST_ONLY_ACK=900 to authorize the isolated 900-second integration deploy.'
}

$source = Get-Content -LiteralPath $contract -Raw
if ($source -notmatch '(?m)^REMOVAL_DELAY = 900\r?$') {
  throw 'TEST_VARIANT_DELAY_MISMATCH'
}
if ($source -match '(?m)^REMOVAL_DELAY = 86400\r?$') {
  throw 'TEST_VARIANT_PRODUCTION_DELAY_PRESENT'
}

$python = Join-Path (Get-Location) '.venv312\Scripts\python.exe'
if (-not (Test-Path -LiteralPath $python)) { throw 'MISSING_PYTHON312_VENV' }
$env:GENVM_VERSION = 'v0.2.12'
$env:PYTHONIOENCODING = 'utf-8'
& $python scripts/preflight.py
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
$lint = Join-Path (Get-Location) '.venv312\Scripts\genvm-lint.exe'
if (-not (Test-Path -LiteralPath $lint)) { throw 'MISSING_PINNED_LINTER' }
& $lint lint $contract
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $lint check $contract --json
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
& $lint schema $contract --json *> $null
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
node scripts/network-guard.cjs
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }

$version = (& node scripts/local-cli.cjs --version).Trim()
if ($version -ne '0.39.1') { throw "WRONG_LOCAL_CLI_VERSION:$version" }
node scripts/local-cli.cjs network set studionet
node scripts/local-cli.cjs network info
$explicitAck = Read-Host 'Type 900 to continue the TEST-ONLY 900-second StudioNet deploy'
if ($explicitAck -ne '900') { exit 3 }
node scripts/local-cli.cjs deploy --contract $contract
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
Write-Host 'TEST-ONLY deploy submitted. Verify FINALIZED + execution success and record source parity.'
