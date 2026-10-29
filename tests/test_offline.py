"""Pure/structural invariants, runnable without GenVM or network access."""
import ast
import pathlib
import unittest

SOURCE = pathlib.Path(__file__).resolve().parents[1] / "contracts" / "entrench.py"
TEXT = SOURCE.read_text(encoding="utf-8")
MODULE = ast.parse(TEXT)
FUNCTIONS = {"_threshold", "_count", "_requirements", "_normalize", "_valid", "_json",
             "_prompt", "_audit_prompt"}
scope = {"CLASSES": "NMREU", "NORMAL_PCT": 51, "PROTECTED_PCT": 75,
         "REMOVAL_PCT": 90, "REMOVAL_DELAY": 86400, "_json": None}
import json
scope["json"] = json
nodes = [n for n in MODULE.body if isinstance(n, ast.FunctionDef) and n.name in FUNCTIONS]
exec(compile(ast.Module(body=nodes, type_ignores=[]), str(SOURCE), "exec"), scope)


class ThresholdTests(unittest.TestCase):
    def test_all_roster_sizes_ceil_rounding(self):
        for n in range(3, 10):
            for pct in (51, 75, 90):
                expected = (n * pct + 99) // 100
                self.assertEqual(scope["_threshold"](n, pct), expected)

    def test_exact_five_member_tiers(self):
        for vector, kind, votes in [("NN", "ORDINARY", 3),
                                    ("MN", "PROTECTED", 4),
                                    ("EN", "PROTECTED", 4),
                                    ("RN", "REMOVAL", 5),
                                    ("NMRE", "REMOVAL", 5)]:
            d = scope["_requirements"](vector, 5)
            self.assertEqual((d["class"], d["yes"]), (kind, votes))

    def test_removed_right_requires_delay(self):
        self.assertEqual(scope["_requirements"]("R", 5)["delay"], 86400)
        self.assertEqual(scope["_requirements"]("N", 5)["delay"], 0)
        self.assertEqual(scope["_requirements"]("M", 5)["delay"], 0)

    def test_ambiguous_fails_closed(self):
        for vector in ("U", "NMU", "", "X", "NNX"):
            self.assertTrue(scope["_requirements"](vector, 5)["blocked"])

    def test_approval_masks_do_not_double_count(self):
        count = scope["_count"]
        self.assertEqual(count(0b10101, 5), 3)
        self.assertEqual(count(0b100001, 5), 1)
        self.assertEqual(count(0b11111, 5), 5)


class ConsensusPayloadTests(unittest.TestCase):
    def norm(self, response, n=2):
        return scope["_normalize"](response, n)

    def test_valid_ordinary(self):
        self.assertEqual(self.norm({"impacts": ["N", "N"],
            "reason_code": "UNCHANGED", "witness": ""})["vector"], "NN")

    def test_valid_protected(self):
        self.assertEqual(self.norm({"impacts": ["M", "R"],
            "reason_code": "ADVERSE", "witness": "Withdrawals deleted"})["vector"], "MR")

    def test_missing_rule_is_unknown(self):
        self.assertEqual(self.norm({"impacts": ["N"],
            "reason_code": "OK", "witness": ""})["vector"], "UU")

    def test_no_witness_for_material_effect_fails(self):
        self.assertEqual(self.norm({"impacts": ["R", "N"],
            "reason_code": "OK", "witness": ""})["vector"], "UU")

    def test_extra_key_fails(self):
        self.assertEqual(self.norm({"impacts": ["N", "N"],
            "reason_code": "OK", "witness": "", "override": True})["vector"], "UU")

    def test_boolean_or_number_code_fails(self):
        for code in (None, True, 99):
            self.assertEqual(self.norm({"impacts": ["N", code],
                "reason_code": "OK", "witness": ""})["vector"], "UU")

    def test_non_ascii_reason_fails(self):
        self.assertEqual(self.norm({"impacts": ["N", "N"],
            "reason_code": "é", "witness": ""})["vector"], "UU")

    def test_oversized_witness_fails(self):
        self.assertEqual(self.norm({"impacts": ["R", "N"],
            "reason_code": "OK", "witness": "x" * 301})["vector"], "UU")

    def test_valid_result_rejects_bad_shape(self):
        check = scope["_valid"]
        self.assertFalse(check({"vector": "N", "reason": "OK", "witness": ""}, 2))
        self.assertFalse(check({"vector": "NX", "reason": "OK", "witness": ""}, 2))
        self.assertTrue(check({"vector": "NN", "reason": "OK", "witness": ""}, 2))

    def test_prompt_does_not_include_proposal_title(self):
        prompt = scope["_prompt"]("charter", "old", "new", [[0, "RIGHT", "x"]], "LEADER")
        self.assertIn("COMPLETE canonical old policy", prompt)
        self.assertIn("immutable", prompt)
        self.assertIn("UNTRUSTED", prompt)
        self.assertNotIn("Operational Liquidity Improvement", prompt)


class ContractArchitectureTests(unittest.TestCase):
    def test_no_privileged_seal_rewrite(self):
        contract = next(n for n in MODULE.body if isinstance(n, ast.ClassDef) and n.name == "Entrench")
        methods = {n.name for n in contract.body if isinstance(n, ast.FunctionDef)}
        self.assertFalse({"force_execute", "change_threshold", "replace_principle",
                          "set_head", "admin_override"} & methods)

    def test_proposal_title_not_in_semantic_assessment(self):
        assessment = next(n for n in MODULE.body if isinstance(n, ast.ClassDef)
                          and n.name == "Entrench")
        method = next(n for n in assessment.body if isinstance(n, ast.FunctionDef)
                      and n.name == "_semantic_assessment")
        self.assertNotIn("title", ast.unparse(method))

    def test_consumer_checks_execution_and_current_head(self):
        consumer = (SOURCE.parent / "consumer_gate.py").read_text(encoding="utf-8")
        self.assertIn("is_executed(self.proposal_id, self.expected_head)", consumer)
        self.assertIn("ONE_SHOT", consumer)
        self.assertIn("AMENDMENT_NOT_CANONICAL", consumer)

    def test_production_network_is_single_target(self):
        import json
        config = json.loads((SOURCE.parents[1] / "network.json").read_text(encoding="utf-8"))
        self.assertEqual(config["alias"], "studionet")
        self.assertEqual(config["chainId"], 61999)
        self.assertEqual(config["rpc"], "https://studio.genlayer.com/api")
        self.assertEqual(config["explorer"], "https://explorer-studio.genlayer.com")


if __name__ == "__main__":
    unittest.main()
