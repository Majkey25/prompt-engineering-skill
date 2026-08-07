#!/usr/bin/env python3
"""Regression tests for the prompt-engineering helper script."""

from __future__ import annotations

import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path

from make_prompt_eval import EvalArgs, build_manifest, main


class PromptEvalTests(unittest.TestCase):
    def args(
        self,
        *,
        minimal: str | None = None,
        candidate: str | None = None,
        out: str = "-",
    ) -> EvalArgs:
        return EvalArgs(
            prompt_type="coding",
            model="test-model",
            runtime="test-runtime",
            title=None,
            minimal=minimal,
            candidate=candidate,
            out=out,
        )

    def test_manifest_contains_three_comparable_variants(self) -> None:
        manifest = build_manifest(self.args())
        self.assertEqual(
            ["baseline", "minimal", "candidate"],
            [variant["id"] for variant in manifest["variants"]],
        )
        self.assertGreaterEqual(len(manifest["cases"]), 7)
        self.assertIn("unsupported_specificity", manifest["metrics"])

    def test_manifest_reads_prompt_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            minimal = root / "minimal.txt"
            candidate = root / "candidate.txt"
            minimal.write_text("minimal prompt", encoding="utf-8")
            candidate.write_text("candidate prompt", encoding="utf-8")
            manifest = build_manifest(self.args(minimal=str(minimal), candidate=str(candidate)))
            self.assertEqual("minimal prompt", manifest["variants"][1]["prompt"])
            self.assertEqual("candidate prompt", manifest["variants"][2]["prompt"])

    def test_main_writes_valid_json_to_new_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "eval.json"
            with redirect_stdout(StringIO()):
                result = main(["--type", "general", "--out", str(output)])
            self.assertEqual(0, result)
            self.assertIsInstance(json.loads(output.read_text(encoding="utf-8")), dict)

    def test_main_stdout_is_ascii_safe(self) -> None:
        stream = StringIO()
        with redirect_stdout(stream):
            result = main(["--title", "Příliš žluťoučký", "--out", "-"])
        self.assertEqual(0, result)
        self.assertTrue(stream.getvalue().isascii())
        self.assertEqual("Příliš žluťoučký", json.loads(stream.getvalue())["title"])

    def test_main_preserves_existing_source_file(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "minimal.txt"
            source.write_text("keep me", encoding="utf-8")
            with redirect_stderr(StringIO()):
                result = main(["--minimal", str(source), "--out", str(source)])
            self.assertEqual(2, result)
            self.assertEqual("keep me", source.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
