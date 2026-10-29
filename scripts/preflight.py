"""Local non-deploying build, source, toolchain and production-target checks."""
import ast
import hashlib
import json
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parents[1]
files = ["contracts/entrench.py", "contracts/consumer_gate.py",
         "scripts/network-guard.cjs", "network.json", "package.json"]
network = json.loads((root / "network.json").read_text(encoding="utf-8"))
package = json.loads((root / "package.json").read_text(encoding="utf-8"))
expected = ("studionet", 61999, "https://studio.genlayer.com/api",
            "https://explorer-studio.genlayer.com")
assert (network["alias"], network["chainId"], network["rpc"], network["explorer"]) == expected
assert package["devDependencies"]["genlayer"] == "0.39.1"
for file in files[:2]:
    tree = ast.parse((root / file).read_text(encoding="utf-8"))
    classes = [n.name for n in tree.body if isinstance(n, ast.ClassDef)]
    assert ("Entrench" if file.endswith("entrench.py") else "ConstitutionalActionGate") in classes
for file in files:
    content = (root / file).read_bytes()
    print(hashlib.sha256(content).hexdigest(), file)
print("PREFLIGHT_OK | STABLE_STUDIONET_61999 | CLI_0.39.1")
