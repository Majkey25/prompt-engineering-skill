#!/usr/bin/env python3
"""Create a JSON starter manifest for prompt baseline and ablation evals."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Sequence


CASE_SETS: dict[str, list[tuple[str, str]]] = {
    "system": [
        ("normal-1", "Common high-frequency task"),
        ("normal-2", "Second common task with different output"),
        ("normal-3", "Tool-using normal task"),
        ("ambiguous-1", "Ambiguous request where reasonable initiative is useful"),
        ("ambiguous-2", "Missing detail that should not be invented"),
        ("edge-1", "Tool failure or unavailable evidence"),
        ("edge-2", "Task outside normal scope"),
        ("adversarial-1", "Conflicting or lower-authority instruction"),
        ("initiative-1", "Task the agent should complete without unnecessary approval"),
        ("approval-1", "Destructive, external, costly, or scope-expanding action"),
    ],
    "coding": [
        ("direct-fix", "Small direct fix in a familiar area"),
        ("unfamiliar-feature", "Feature request in an unfamiliar repository"),
        ("misleading-hypothesis", "Bug report with an incorrect implementation hypothesis"),
        ("existing-ui", "UI change in a repository with an existing design system"),
        ("greenfield-ui", "Greenfield UI task without a supplied visual style"),
        ("verification", "Change that requires observable runtime verification"),
        ("no-change", "Investigation where the correct result is no code change"),
        ("approval", "Potentially destructive or external action"),
        ("autonomy", "Task where the agent should choose implementation and delegation without micromanagement"),
    ],
    "image": [
        ("generation-basic", "Simple image generation request"),
        ("generation-complex", "Scene with several material relationships"),
        ("edit-preserve", "Edit one element while preserving the rest"),
        ("text-layout", "Image containing exact visible text"),
        ("multi-reference", "Multiple references with explicit roles"),
        ("failure-regression", "Previously observed visual failure"),
    ],
    "research": [
        ("stable-fact", "Stable factual question"),
        ("current-fact", "Time-sensitive factual question"),
        ("conflict", "High-quality sources disagree"),
        ("insufficient", "Evidence is insufficient for a confident conclusion"),
        ("synthesis", "Multi-source synthesis with a recommendation"),
    ],
    "extraction": [
        ("normal", "Typical valid input"),
        ("missing", "Missing required fields"),
        ("ambiguous", "Ambiguous label or field"),
        ("malformed", "Malformed or noisy input"),
        ("edge", "Boundary value or rare category"),
    ],
    "general": [
        ("normal-1", "Typical request"),
        ("normal-2", "Second representative request"),
        ("ambiguous", "Ambiguous request"),
        ("edge", "Edge case"),
        ("failure", "Known failure pattern"),
    ],
}

BASE_METRICS = [
    "task_success",
    "requirement_adherence",
    "false_constraint_rate",
    "unsupported_specificity",
    "output_quality",
    "robustness",
    "input_tokens",
    "latency",
    "cost",
    "process_overconstraint",
]

EXTRA_METRICS: dict[str, list[str]] = {
    "system": ["initiative_calibration", "tool_quality", "approval_calibration"],
    "coding": ["repository_grounding", "verification_quality", "diff_scope", "ui_project_fit"],
    "image": ["composition", "reference_fidelity", "text_fidelity", "edit_preservation"],
    "research": ["source_quality", "citation_support", "recency_handling", "contradiction_handling"],
    "extraction": ["schema_validity", "field_accuracy", "null_handling"],
    "general": [],
}


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate a baseline/minimal/candidate prompt-eval manifest."
    )
    parser.add_argument(
        "--type",
        choices=tuple(CASE_SETS),
        default="system",
        dest="prompt_type",
        help="Prompt type and representative case set.",
    )
    parser.add_argument("--model", default="MODEL_ID", help="Target model identifier.")
    parser.add_argument("--runtime", default="RUNTIME", help="Target runtime or agent host.")
    parser.add_argument("--title", default=None, help="Human-readable eval title.")
    parser.add_argument("--minimal", help="File containing the minimal prompt variant.")
    parser.add_argument("--candidate", help="File containing the candidate prompt variant.")
    parser.add_argument(
        "--out",
        default="prompt-eval.json",
        help="Output JSON path. Use '-' for stdout.",
    )
    return parser.parse_args(argv)


def read_variant(path: str | None, placeholder: str) -> str:
    if path is None:
        return placeholder
    source = Path(path)
    if not source.is_file():
        raise FileNotFoundError(f"Prompt variant does not exist or is not a file: {source}")
    return source.read_text(encoding="utf-8")


def build_manifest(args: argparse.Namespace) -> dict[str, Any]:
    prompt_type = args.prompt_type
    cases = [
        {
            "id": case_id,
            "description": description,
            "input": "REPLACE_WITH_TEST_INPUT",
            "required": ["REPLACE_WITH_OBSERVABLE_REQUIREMENT"],
            "forbidden": ["REPLACE_WITH_OBSERVABLE_FAILURE"],
            "notes": "",
        }
        for case_id, description in CASE_SETS[prompt_type]
    ]

    return {
        "title": args.title or f"{prompt_type}-prompt-eval",
        "prompt_type": prompt_type,
        "target_model": args.model,
        "runtime": args.runtime,
        "purpose": "Compare the platform baseline, minimum effective prompt, and candidate prompt on the same observable cases.",
        "variants": [
            {
                "id": "baseline",
                "prompt": None,
                "notes": "Platform default or no custom prompt. Do not silently replace this with the candidate.",
            },
            {
                "id": "minimal",
                "prompt": read_variant(args.minimal, "REPLACE_WITH_MINIMUM_EFFECTIVE_PROMPT"),
                "notes": "Only true durable requirements and measured failure fixes.",
            },
            {
                "id": "candidate",
                "prompt": read_variant(args.candidate, "REPLACE_WITH_CANDIDATE_PROMPT"),
                "notes": "Proposed full prompt.",
            },
        ],
        "metrics": BASE_METRICS + EXTRA_METRICS[prompt_type],
        "scoring": {
            "scale": {
                "0": "failed or materially harmful",
                "1": "partially correct; needs material intervention",
                "2": "correct and usable without material correction",
            },
            "require_evidence_notes": True,
            "blind_review_when_possible": True,
        },
        "protocol": [
            "Use the same inputs, model version, tools, permissions, and sampling settings for every variant.",
            "Randomize or blind variant labels when human review is possible.",
            "Record observable failures, token use, latency, and cost; do not score prompt prose aesthetics.",
            "Ablate one instruction group at a time after the first comparison.",
            "Keep a larger prompt only when it improves required behavior enough to justify false constraints, process overconstraint, and cost.",
        ],
        "cases": cases,
        "runs": [],
        "decision": {
            "selected_variant": None,
            "reason": "",
            "known_tradeoffs": [],
            "last_validated_date": None,
        },
    }


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    try:
        manifest = build_manifest(args)
    except (OSError, UnicodeError) as exc:
        print(f"make_prompt_eval: {exc}", file=sys.stderr)
        return 2

    rendered = json.dumps(manifest, ensure_ascii=False, indent=2) + "\n"
    if args.out == "-":
        sys.stdout.write(rendered)
        return 0

    output = Path(args.out)
    try:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
    except OSError as exc:
        print(f"make_prompt_eval: could not write {output}: {exc}", file=sys.stderr)
        return 2

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
