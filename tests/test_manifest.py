"""Checks that every path referenced by .cursor-plugin/plugin.json exists relative to the repository root.

Run from the repository root:  python3 -m unittest discover -s tests -v
"""
import json
import os
import unittest

ROOT = os.path.join(os.path.dirname(__file__), "..")
MANIFEST = os.path.join(ROOT, ".cursor-plugin", "plugin.json")


class ManifestPaths(unittest.TestCase):
    def setUp(self):
        with open(MANIFEST) as f:
            self.manifest = json.load(f)

    def exists(self, rel):
        return os.path.exists(os.path.join(ROOT, rel))

    def test_logo_exists(self):
        self.assertTrue(self.exists(self.manifest["logo"]), self.manifest["logo"])

    def test_skills_mcp_and_commands_exist(self):
        self.assertTrue(self.exists(self.manifest["skills"]))
        self.assertTrue(self.exists(self.manifest["mcpServers"]))
        for command in self.manifest["commands"]:
            self.assertTrue(self.exists(command), command)

    def test_search_reference_matches_current_chunks_contract(self):
        path = os.path.join(ROOT, "skills", "tavily-best-practices", "references", "search.md")
        text = open(path).read()
        self.assertNotIn("chunks_per_source=5", text)
        self.assertNotIn("advanced/fast depth only", text)


if __name__ == "__main__":
    unittest.main()
