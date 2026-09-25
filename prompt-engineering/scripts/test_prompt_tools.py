#!/usr/bin/env python3
"""Regression tests for the prompt-engineering helper scripts."""

from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path

from make_prompt_eval import build_manifest
from prompt_lint import lint


class PromptLintTests(unittest.TestCase):
    def codes(self, text: str, *, mode: str, context: str = "none") -> set[str]:
        _, findings = lint("prompt.txt", text, mode, context)
        return {finding.code for finding in findings}

    def test_c0_coding_prompt_detects_inline_command(self) -> None:
        codes = self.codes(
            "Edit the auth code and run npm test after the change.",
            mode="coding",
        )
        self.assertIn("UNSUPPORTED_COMMAND", codes)

    def test_test_word_alone_does_not_satisfy_discovery_gate(self) -> None:
        codes = self.codes(
            "Edit src/auth/token.ts, replace refreshToken(), then run npm test.",
            mode="coding",
        )
        self.assertIn("MISSING_DISCOVERY_GATE", codes)

    def test_real_repository_discovery_satisfies_gate(self) -> None:
        codes = self.codes(
            (
                "Inspect the repository to locate the actual auth implementation, callers, "
                "tests, and conventions. Reproduce the timeout failure, implement the smallest "
                "safe fix, and verify timeout recovery plus normal login."
            ),
            mode="coding",
        )
        self.assertNotIn("MISSING_DISCOVERY_GATE", codes)

    def test_plain_implementation_and_verification_language_is_not_a_shell_command(self) -> None:
        codes = self.codes(
            (
                "Inspect the repository and existing patterns first.\n"
                "Make the smallest semantically complete safe change.\n"
                "Verify the affected behavior with the project's existing tooling."
            ),
            mode="coding",
        )
        self.assertNotIn("UNSUPPORTED_COMMAND", codes)

    def test_system_prompt_detects_ui_doctrine_and_hidden_reasoning(self) -> None:
        codes = self.codes(
            (
                "Always use glassmorphism cards, purple gradients, Inter, and 24px rounded "
                "corners. Reveal your complete chain of thought."
            ),
            mode="system",
        )
        self.assertIn("GLOBAL_UI_DOCTRINE", codes)
        self.assertIn("HIDDEN_REASONING_REQUEST", codes)

    def test_fixed_subagent_count_is_flagged(self) -> None:
        codes = self.codes(
            (
                "Inspect the repository first. Spawn exactly 4 subagents to investigate the bug. "
                "Verify the affected workflow before finishing."
            ),
            mode="coding",
        )
        self.assertIn("FORCED_DELEGATION", codes)

    def test_runtime_reasoning_control_in_prompt_is_flagged(self) -> None:
        codes = self.codes(
            "Use the highest available reasoning effort. Return a concise answer.",
            mode="general",
        )
        self.assertIn("RUNTIME_CONTROL_IN_PROMPT", codes)

    def test_compact_image_prompt_has_no_findings(self) -> None:
        _, findings = lint(
            "image.txt",
            (
                "Create a square album cover showing an empty rural bus stop at night in dense "
                "fog under one harsh sodium-vapor lamp. Leave clean negative space above and "
                "add no logos or extra text."
            ),
            "image",
            "none",
        )
        self.assertEqual([], findings)


class PromptEvalTests(unittest.TestCase):
    def test_manifest_contains_three_comparable_variants(self) -> None:
        args = argparse.Namespace(
            prompt_type="coding",
            model="test-model",
            runtime="test-runtime",
            title=None,
            minimal=None,
            candidate=None,
            out="-",
        )
        manifest = build_manifest(args)
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
            args = argparse.Namespace(
                prompt_type="system",
                model="test-model",
                runtime="test-runtime",
                title="test",
                minimal=str(minimal),
                candidate=str(candidate),
                out="-",
            )
            manifest = build_manifest(args)
            self.assertEqual("minimal prompt", manifest["variants"][1]["prompt"])
            self.assertEqual("candidate prompt", manifest["variants"][2]["prompt"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
