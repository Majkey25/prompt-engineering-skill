#!/usr/bin/env python3
"""Regression tests for the prompt-engineering helper scripts."""

from __future__ import annotations

import argparse
import json
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from make_prompt_eval import build_manifest
from make_prompt_eval import main as make_eval
from prompt_lint import iter_inputs, lint, render_text
from prompt_lint import main as lint_main


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


class PromptLintBoundaryTests(unittest.TestCase):
    def link(self, path: Path, target: Path, *, directory: bool = False) -> None:
        try:
            path.symlink_to(target, target_is_directory=directory)
        except OSError as exc:
            self.skipTest(f"Symlink creation is unavailable: {exc}")

    def test_directory_scan_skips_links_and_keeps_regular_nested_prompts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            selected = root / "selected"
            selected.mkdir()
            nested = selected / "nested"
            nested.mkdir()
            prompt = nested / "normal.PROMPT"
            prompt.write_text("regular prompt", encoding="utf-8")
            outside = root / "outside"
            outside.mkdir()
            sentinel = outside / "private.txt"
            sentinel.write_text("TODO outside sentinel", encoding="utf-8")
            self.link(selected / "absolute.md", sentinel)
            self.link(selected / "relative.txt", Path("../outside/private.txt"))
            self.link(selected / "internal.md", prompt)
            self.link(selected / "linked-directory", outside, directory=True)
            self.assertEqual([(str(prompt), "regular prompt")], list(iter_inputs([str(selected)])))
            # An explicitly selected file still grants access, regardless of suffix or link.
            self.assertEqual(
                [(str(selected / "absolute.md"), "TODO outside sentinel")],
                list(iter_inputs([str(selected / "absolute.md")])),
            )

    def test_text_output_quotes_paths_and_neutralizes_controls(self) -> None:
        path = "prompt\nforged\x1b[2J\u202e.md"
        output = render_text([{"path": path, "mode": "general", "findings": []}])
        self.assertEqual(f"{path!r} [general]", output.splitlines()[0])
        self.assertEqual(2, len(output.splitlines()))

    def test_cli_escapes_terminal_sequences_but_json_preserves_prompt_data(self) -> None:
        prompt = (
            "TODO \x1b[2J \x1b]8;;https://example.invalid/\x07 link \x1b]8;;\x07 "
            "\x1b]52;c;dGVzdA==\x07 \x7f \x9d \u202e \u2066 český text"
        )
        output = StringIO()
        with patch("sys.stdin", StringIO(prompt)), redirect_stdout(output):
            self.assertEqual(0, lint_main(["-", "--mode", "general", "--fail-on", "never"]))
        rendered = output.getvalue()
        for character in ["\x1b", "\x07", "\x7f", "\x9d", "\u202e", "\u2066"]:
            self.assertNotIn(character, rendered)
            self.assertIn(repr(character)[1:-1], rendered)
        self.assertIn("český text", rendered)
        output = StringIO()
        with patch("sys.stdin", StringIO(prompt)), redirect_stdout(output):
            self.assertEqual(
                0, lint_main(["-", "--mode", "general", "--format", "json", "--fail-on", "never"])
            )
        document = json.loads(output.getvalue())
        self.assertEqual(prompt, document["results"][0]["findings"][0]["excerpt"])

    def test_cli_errors_escape_untrusted_path_controls(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing\u202e.md"
            errors = StringIO()
            with redirect_stderr(errors):
                self.assertEqual(2, lint_main([str(missing)]))
            self.assertNotIn("\u202e", errors.getvalue())
            self.assertIn("\\u202e", errors.getvalue())


class PromptEvalTests(unittest.TestCase):
    def test_existing_manifest_is_preserved(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "eval.json"
            with redirect_stdout(StringIO()):
                self.assertEqual(0, make_eval(["--out", str(output)]))
            output.write_text("existing evaluation results", encoding="utf-8")
            with redirect_stderr(StringIO()):
                self.assertEqual(2, make_eval(["--out", str(output)]))
            self.assertEqual("existing evaluation results", output.read_text(encoding="utf-8"))

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
