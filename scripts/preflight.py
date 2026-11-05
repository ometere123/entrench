"""Local non-deploying build, source, toolchain and production-target checks."""
import ast
import hashlib
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
files = ["contracts/entrench.py", "contracts/test_only_900/entrench.py",
         "contracts/consumer_gate.py",
         "scripts/network-guard.cjs", "network.json", "package.json"]
network = json.loads((root / "network.json").read_text(encoding="utf-8"))
package = json.loads((root / "package.json").read_text(encoding="utf-8"))
requirements = (root / "requirements-direct.txt").read_text(encoding="utf-8")
expected = ("studionet", 61999, "https://studio.genlayer.com/api",
            "https://explorer-studio.genlayer.com")
assert (network["alias"], network["chainId"], network["rpc"], network["explorer"]) == expected
assert package["devDependencies"]["genlayer"] == "0.39.1"
assert "genlayer-test==0.29.0" in requirements
assert "genlayer-py==0.11.0" in requirements
assert "genvm-linter==0.11.0" in requirements
lock = json.loads((root / "package-lock.json").read_text(encoding="utf-8"))
assert lock["packages"]["node_modules/genlayer"]["version"] == "0.39.1"
for file in files[:3]:
    tree = ast.parse((root / file).read_text(encoding="utf-8"))
    classes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
    expected_class = "ConstitutionalActionGate" if file.endswith("consumer_gate.py") else "Entrench"
    assert expected_class in classes
for file in files:
    content = (root / file).read_bytes()
    print(hashlib.sha256(content).hexdigest(), file)
manifest_path = root / "SOURCE_SHA256_MANIFEST.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
for file in ("contracts/entrench.py", "contracts/test_only_900/entrench.py",
             "contracts/consumer_gate.py"):
    actual = hashlib.sha256((root / file).read_bytes()).hexdigest()
    assert manifest["files"][file]["sha256"] == actual, f"STALE_SOURCE_MANIFEST:{file}"
print("PREFLIGHT_OK | STABLE_STUDIONET_61999 | CLI_0.39.1")
