import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1] / "skills"


def load(skill, script):
    spec = importlib.util.spec_from_file_location(script, ROOT / skill / "scripts" / (script + ".py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class DataSkillsTests(unittest.TestCase):
    def test_sections_preserve_source_and_fences(self):
        run = load("genpark-markdown-sections", "sections").sections
        source = "intro\r\n# A\r\n```md\r\n# not heading\r\n```\r\n### C\r\ntext\r\n## B\r\n"
        out = run(source)
        self.assertEqual("".join(s["text"] for s in out), source)
        self.assertEqual([s["heading_path"] for s in out], [[], ["A"], ["A", "C"], ["A", "B"]])
        self.assertEqual([(s["start_line"], s["end_line"]) for s in out], [(1, 1), (2, 5), (6, 7), (8, 8)])
        self.assertEqual(run(""), [])
        self.assertEqual(len(run("# A\n~~~\n## code\n~~~~\n# B\n")), 2)
        self.assertEqual(run("# A\n# A\n")[1]["start_line"], 2)

    def test_exact_identity_and_provenance(self):
        run = load("genpark-json-record-dedup", "dedup").deduplicate
        out = run({"keys": ["id"], "records": [{"id": {"a": 1, "b": 2}}, {"id": {"b": 2, "a": 1}}, {"id": True}, {"id": 1}, {"id": None}]})
        self.assertEqual(out["kept_indexes"], [0, 2, 3, 4])
        self.assertEqual(out["duplicates"], [{"index": 1, "kept_index": 0}])
        with self.assertRaises(ValueError):
            run({"keys": ["id"], "records": [{}]})
        with self.assertRaises(ValueError):
            run({"keys": ["id"], "records": [{"id": float("nan")}]})


if __name__ == "__main__":
    unittest.main()
