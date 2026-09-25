#!/usr/bin/env python3
"""Heuristic linter for system, coding, general, and image/video prompts.

The linter finds likely prompt-engineering defects. It does not prove that a
prompt is good or bad. Review every finding against the actual model, runtime,
source evidence, and eval results.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Sequence

SEVERITY_RANK = {"low": 1, "medium": 2, "high": 3}


@dataclass(frozen=True)
class Finding:
    path: str
    severity: str
    code: str
    line: int | None
    message: str
    excerpt: str | None = None


def parse_args(argv: Sequence[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Lint prompts for duplication, unresolved placeholders, hidden-reasoning "
            "requests, prompt bloat, and unsupported specificity."
        )
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="Prompt file, directory, or '-' for stdin. Directories scan .md/.txt/.prompt files.",
    )
    parser.add_argument(
        "--mode",
        choices=("auto", "system", "coding", "image", "general"),
        default="auto",
        help="Prompt type. 'auto' infers from filename and content.",
    )
    parser.add_argument(
        "--context",
        choices=("none", "partial", "verified"),
        default="none",
        help="Evidence available to the prompt writer. Relevant mainly to coding prompts.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        dest="output_format",
        help="Output format.",
    )
    parser.add_argument(
        "--fail-on",
        choices=("high", "medium", "never"),
        default="high",
        help="Return exit code 1 when a finding at or above this severity exists.",
    )
    return parser.parse_args(argv)


def iter_inputs(paths: Sequence[str]) -> Iterable[tuple[str, str]]:
    for raw_path in paths:
        if raw_path == "-":
            yield "<stdin>", sys.stdin.read()
            continue

        path = Path(raw_path)
        if not path.exists():
            raise FileNotFoundError(f"Path does not exist: {path}")
        if path.is_file():
            yield str(path), path.read_text(encoding="utf-8")
            continue

        for child in sorted(path.rglob("*")):
            if child.is_file() and child.suffix.lower() in {".md", ".txt", ".prompt"}:
                yield str(child), child.read_text(encoding="utf-8")


def infer_mode(path: str, text: str) -> str:
    haystack = f"{Path(path).name}\n{text[:2500]}".lower()
    if any(term in haystack for term in ("system prompt", "developer prompt", "agent constitution")):
        return "system"
    if any(
        term in haystack
        for term in (
            "repository",
            "codebase",
            "coding agent",
            "implement",
            "bugfix",
            "pull request",
            "run tests",
        )
    ):
        return "coding"
    if any(
        term in haystack
        for term in (
            "image prompt",
            "video prompt",
            "generate an image",
            "generate a video",
            "visual composition",
        )
    ):
        return "image"
    return "general"


def strip_markdown_prefix(line: str) -> str:
    line = re.sub(r"^\s{0,3}(?:#{1,6}\s+|[-*+]\s+|\d+[.)]\s+)", "", line)
    line = re.sub(r"[`*_~]", "", line)
    return line.strip()


def normalized_instruction(line: str) -> str:
    line = strip_markdown_prefix(line).lower()
    line = re.sub(r"\[[^\]]+\]\([^)]*\)", "", line)
    line = re.sub(r"[^a-z0-9á-ž]+", " ", line, flags=re.IGNORECASE)
    return " ".join(line.split())


def visible_lines(text: str) -> list[tuple[int, str]]:
    result: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(text.splitlines(), start=1):
        if re.match(r"^\s*```", line):
            in_fence = not in_fence
            continue
        if not in_fence:
            result.append((number, line))
    return result


def add_line_matches(
    findings: list[Finding],
    *,
    path: str,
    lines: Sequence[tuple[int, str]],
    pattern: re.Pattern[str],
    severity: str,
    code: str,
    message: str,
    limit: int = 8,
) -> None:
    count = 0
    for line_number, line in lines:
        if pattern.search(line):
            findings.append(
                Finding(
                    path=path,
                    severity=severity,
                    code=code,
                    line=line_number,
                    message=message,
                    excerpt=line.strip()[:240] or None,
                )
            )
            count += 1
            if count >= limit:
                break


def lint_common(path: str, text: str, lines: Sequence[tuple[int, str]]) -> list[Finding]:
    findings: list[Finding] = []

    duplicates: dict[str, list[tuple[int, str]]] = {}
    for line_number, line in lines:
        normalized = normalized_instruction(line)
        if len(normalized) < 35:
            continue
        if normalized.startswith(("example ", "good ", "bad ")):
            continue
        duplicates.setdefault(normalized, []).append((line_number, line))

    for occurrences in duplicates.values():
        if len(occurrences) < 2:
            continue
        severity = "medium" if len(occurrences) >= 3 else "low"
        line_numbers = ", ".join(str(number) for number, _ in occurrences[:6])
        findings.append(
            Finding(
                path=path,
                severity=severity,
                code="DUPLICATE_RULE",
                line=occurrences[0][0],
                message=f"Likely duplicate instruction on lines {line_numbers}. State a rule once unless repetition is measured to help.",
                excerpt=occurrences[0][1].strip()[:240] or None,
            )
        )

    placeholder_pattern = re.compile(
        r"(?:\b(?:TODO|TBD|FIXME)\b|\{\{[^{}]+\}\}|\[(?:insert|fill|specific|describe|your|target|todo)[^\]]*\])",
        re.IGNORECASE,
    )
    add_line_matches(
        findings,
        path=path,
        lines=lines,
        pattern=placeholder_pattern,
        severity="medium",
        code="UNRESOLVED_PLACEHOLDER",
        message="Possible unresolved template placeholder. Replace it or confirm the output is intentionally a reusable template.",
    )

    cot_pattern = re.compile(
        r"(?:show|reveal|print|write|provide|expose).{0,35}(?:chain[- ]of[- ]thought|hidden reasoning|private reasoning|all reasoning)|think step by step",
        re.IGNORECASE,
    )
    add_line_matches(
        findings,
        path=path,
        lines=lines,
        pattern=cot_pattern,
        severity="high",
        code="HIDDEN_REASONING_REQUEST",
        message="Requests hidden chain-of-thought. Ask for a concise rationale, evidence, or verification instead.",
    )

    fluff_pattern = re.compile(
        r"\b(?:world[- ]class|best[- ]in[- ]class|elite|visionary|genius|award[- ]winning|unparalleled|legendary)\b",
        re.IGNORECASE,
    )
    model_control_pattern = re.compile(
        r"\b(?:use\s+the\s+highest\s+available\s+reasoning\s+effort|reasoning[_ -]?effort\s*[:=]\s*(?:low|medium|high|xhigh|max)|temperature\s*[:=]\s*[-+]?[0-9.]+)\b",
        re.IGNORECASE,
    )
    add_line_matches(
        findings,
        path=path,
        lines=lines,
        pattern=model_control_pattern,
        severity="low",
        code="RUNTIME_CONTROL_IN_PROMPT",
        message="Model/runtime control appears in prompt prose. Prefer the runtime/API setting unless the text itself is intentionally part of the task contract.",
    )
    add_line_matches(
        findings,
        path=path,
        lines=lines,
        pattern=fluff_pattern,
        severity="low",
        code="PERSONA_FLUFF",
        message="Decorative expertise language rarely improves decisions. Use a role only when it changes scope, judgment, or tone.",
    )

    emphasis_terms = re.findall(
        r"\b(?:MUST|NEVER|ALWAYS|CRITICAL|MANDATORY|ABSOLUTELY|NON[- ]NEGOTIABLE)\b",
        text,
    )
    if len(emphasis_terms) >= 24:
        findings.append(
            Finding(
                path=path,
                severity="high",
                code="AGGRESSIVE_EMPHASIS",
                line=None,
                message=f"Found {len(emphasis_terms)} aggressive emphasis terms. Repeated absolutes can create conflicts and overtriggering.",
            )
        )
    elif len(emphasis_terms) >= 10:
        findings.append(
            Finding(
                path=path,
                severity="medium",
                code="AGGRESSIVE_EMPHASIS",
                line=None,
                message=f"Found {len(emphasis_terms)} aggressive emphasis terms. Check whether each one encodes a real priority.",
            )
        )

    word_count = len(re.findall(r"\S+", text))
    if word_count > 3000:
        findings.append(
            Finding(
                path=path,
                severity="high",
                code="PROMPT_BLOAT",
                line=None,
                message=f"Prompt has about {word_count} words. Compare it against a minimal variant and ablate instruction groups.",
            )
        )
    elif word_count > 1600:
        findings.append(
            Finding(
                path=path,
                severity="medium",
                code="PROMPT_BLOAT",
                line=None,
                message=f"Prompt has about {word_count} words. Verify that the added context improves eval results.",
            )
        )

    return findings


FILE_PATTERN = re.compile(
    r"(?:^|[\s`'\"])(?:(?:\.{0,2}/)?(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+|\b[A-Za-z0-9_-]+\.(?:py|js|jsx|ts|tsx|java|cs|go|rs|rb|php|vue|svelte|json|ya?ml|toml|sql|html|css|scss))\b"
)
FUNCTION_PATTERN = re.compile(
    r"`?[A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)?\([^\n()]{0,80}\)`?"
)
FRAMEWORK_PATTERN = re.compile(
    r"\b(?:React|Next\.js|Vue|Nuxt|Svelte|Angular|Tailwind|shadcn|Framer Motion|Axios|Prisma|Django|FastAPI|Flask|Express|NestJS|Spring Boot|ASP\.NET|Entity Framework|Supabase|Firebase|Playwright|Cypress|Jest|Vitest|pytest|Ruff)\b",
    re.IGNORECASE,
)
COMMAND_PATTERN = re.compile(
    r"(?:"
    r"\b(?i:run|execute|invoke)\s+"
    r"(?:npm|npx|pnpm|yarn|bun|pip|pipx|poetry|uv|pytest|ruff|mypy|cargo|"
    r"go\s+test|dotnet|mvn|gradle|docker|kubectl|terraform|git|make|python(?:3)?\s+-m)"
    r"\b(?:\s+[A-Za-z0-9_./:@=+-]+)?"
    r"|[`$]\s*"
    r"(?:npm|npx|pnpm|yarn|bun|pip|pipx|poetry|uv|pytest|ruff|mypy|cargo|"
    r"go\s+test|dotnet|mvn|gradle|docker|kubectl|terraform|git|make|python(?:3)?\s+-m)"
    r"\b(?:\s+[A-Za-z0-9_./:@=+-]+)?"
    r"|^\s*(?:[-*+]\s+|\d+[.)]\s+)?"
    r"(?:"
    r"(?:npm|npx|pnpm|yarn|bun|pip|pipx|poetry|uv|pytest|ruff|mypy|cargo|dotnet|mvn|gradle|docker|kubectl|terraform)"
    r"\b(?:\s+[A-Za-z0-9_./:@=+-]+)?"
    r"|go\s+test\b(?:\s+[A-Za-z0-9_./:@=+-]+)?"
    r"|python(?:3)?\s+-m\b(?:\s+[A-Za-z0-9_./:@=+-]+)?"
    r"|git\s+(?:status|diff|show|log|test|checkout|switch|restore|add|commit|push|pull|fetch|merge|rebase|grep|ls-files)\b"
    r"|make\s+(?:-[fC]|test|build|lint|check|install|clean|all|deploy|package|release|verify|ci)\b"
    r")"
    r")"
)
DISCOVERY_PATTERN = re.compile(
    r"\b(?:inspect|locate|trace|search|read|find|examine|review|map|discover)\b"
    r".{0,140}?"
    r"\b(?:repo(?:sitory)?|codebase|source|implementation|files?|paths?|symbols?|"
    r"callers?|contracts?|tests?|conventions?|README|docs?|documentation|manifests?|"
    r"lock files?|configuration|config|data flow|entrypoints?|design system|existing patterns?)\b",
    re.IGNORECASE | re.DOTALL,
)
ENV_PATTERN = re.compile(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b")
UI_SPEC_PATTERN = re.compile(
    r"(?:#[0-9a-fA-F]{3,8}\b|\b\d+(?:\.\d+)?(?:px|rem|em|vh|vw)\b|\b(?:glassmorphism|neumorphism|gradient|rounded corners?|border radius|cards?|hero section|dark navy|purple|Inter|Roboto|Poppins|Framer Motion|three-column|two-column)\b)",
    re.IGNORECASE,
)


def lint_coding(
    path: str,
    text: str,
    lines: Sequence[tuple[int, str]],
    context: str,
) -> list[Finding]:
    findings: list[Finding] = []
    if context != "verified":
        severity = "medium" if context == "none" else "low"
        evidence_note = (
            "At C0, remove it unless the user supplied it; tell the target agent to inspect the repository."
            if context == "none"
            else "At C1, keep it only when directly supplied and label unverified details as hypotheses."
        )
        checks = (
            (FILE_PATTERN, "UNSUPPORTED_FILE_DETAIL", "Exact path or filename may exceed available project evidence."),
            (FUNCTION_PATTERN, "UNSUPPORTED_FUNCTION_DETAIL", "Function or call syntax may be an invented implementation detail."),
            (FRAMEWORK_PATTERN, "UNSUPPORTED_STACK_DETAIL", "Framework, package, or test tool may be unsupported by available project evidence."),
            (COMMAND_PATTERN, "UNSUPPORTED_COMMAND", "Exact command may be unsupported by available project evidence."),
            (ENV_PATTERN, "UNSUPPORTED_ENV_DETAIL", "Environment variable may be unsupported by available project evidence."),
            (UI_SPEC_PATTERN, "UNSUPPORTED_UI_DETAIL", "Exact visual choice may impose an unsupported design direction."),
        )
        for pattern, code, message in checks:
            add_line_matches(
                findings,
                path=path,
                lines=lines,
                pattern=pattern,
                severity=severity,
                code=code,
                message=f"{message} {evidence_note}",
                limit=6,
            )

    if context != "verified" and not DISCOVERY_PATTERN.search(text):
        findings.append(
            Finding(
                path=path,
                severity="high" if context == "none" else "medium",
                code="MISSING_DISCOVERY_GATE",
                line=None,
                message="Coding prompt lacks a repository-discovery step even though project context is not verified.",
            )
        )

    verification_terms = re.compile(
        r"\b(?:verify|verification|test|check|reproduce|acceptance criteria|done definition|evidence)\b",
        re.IGNORECASE,
    )
    if not verification_terms.search(text):
        findings.append(
            Finding(
                path=path,
                severity="medium",
                code="MISSING_VERIFICATION",
                line=None,
                message="Coding prompt has no observable verification or done criterion.",
            )
        )

    fixed_subagent_pattern = re.compile(
        r"\b(?:spawn|create|use|launch)\s+(?:exactly\s+)?\d+\s+(?:subagents|agents)\b",
        re.IGNORECASE,
    )
    add_line_matches(
        findings,
        path=path,
        lines=lines,
        pattern=fixed_subagent_pattern,
        severity="medium",
        code="FORCED_DELEGATION",
        message="Prompt forces a fixed agent count. Let the target choose delegation unless the split is a real requirement or measured failure fix.",
        limit=4,
    )

    choreography_hits = len(
        re.findall(r"\b(?:first|then|next|after that|finally)\b", text, re.IGNORECASE)
    )
    if choreography_hits >= 7:
        findings.append(
            Finding(
                path=path,
                severity="low",
                code="PROCESS_CHOREOGRAPHY",
                line=None,
                message=(
                    f"Prompt contains {choreography_hits} sequence markers. Check whether the exact process is truly required; "
                    "prefer outcome, boundaries, and done criteria when the agent can choose the path."
                ),
            )
        )

    return findings


def lint_system(path: str, text: str, lines: Sequence[tuple[int, str]]) -> list[Finding]:
    findings: list[Finding] = []

    ui_hits = [(number, line) for number, line in lines if UI_SPEC_PATTERN.search(line)]
    for line_number, line in ui_hits[:8]:
        findings.append(
            Finding(
                path=path,
                severity="high" if len(ui_hits) >= 4 else "medium",
                code="GLOBAL_UI_DOCTRINE",
                line=line_number,
                message="System prompt contains a fixed visual choice. Keep it only when backed by product requirements, brand evidence, or evals.",
                excerpt=line.strip()[:240] or None,
            )
        )

    for pattern, code, message in (
        (FILE_PATTERN, "TASK_DETAIL_IN_SYSTEM", "Project-specific path or filename may belong in task or repository context, not a durable system prompt."),
        (FUNCTION_PATTERN, "TASK_DETAIL_IN_SYSTEM", "Function-level implementation detail may belong in task or repository context, not a durable system prompt."),
        (COMMAND_PATTERN, "TASK_DETAIL_IN_SYSTEM", "Exact command may belong in verified repository instructions rather than a global system prompt."),
    ):
        add_line_matches(
            findings,
            path=path,
            lines=lines,
            pattern=pattern,
            severity="medium",
            code=code,
            message=message,
            limit=5,
        )

    stable_terms = re.compile(
        r"\b(?:scope|tool|permission|approval|evidence|uncertainty|privacy|safety|output|conflict|authority|verify)\b",
        re.IGNORECASE,
    )
    if not stable_terms.search(text):
        findings.append(
            Finding(
                path=path,
                severity="low",
                code="UNCLEAR_DURABLE_BEHAVIOR",
                line=None,
                message="System prompt does not clearly express durable scope, authority, evidence, tool, or output behavior. Confirm that a custom system prompt is needed at all.",
            )
        )

    return findings


def lint_image(path: str, text: str, lines: Sequence[tuple[int, str]]) -> list[Finding]:
    findings: list[Finding] = []

    for line_number, line in lines:
        comma_count = line.count(",")
        if comma_count >= 14:
            findings.append(
                Finding(
                    path=path,
                    severity="medium",
                    code="KEYWORD_SOUP",
                    line=line_number,
                    message=f"Line has {comma_count} commas and may be a keyword list. Prefer a coherent scene description with only material constraints.",
                    excerpt=line.strip()[:240] or None,
                )
            )
            break

    negative_count = len(re.findall(r"\b(?:no|without|avoid|exclude|never)\b", text, re.IGNORECASE))
    if negative_count >= 12:
        findings.append(
            Finding(
                path=path,
                severity="medium",
                code="NEGATIVE_PROMPT_BLOAT",
                line=None,
                message=f"Found {negative_count} negative constraints. Keep only failures that are likely or repeatedly observed.",
            )
        )

    tool_param_pattern = re.compile(
        r"\b(?:size|n|seed|quality|response_format|transparent_background)\s*[:=]",
        re.IGNORECASE,
    )
    add_line_matches(
        findings,
        path=path,
        lines=lines,
        pattern=tool_param_pattern,
        severity="low",
        code="TOOL_PARAMS_IN_VISUAL_PROMPT",
        message="Tool parameters appear inside visual intent. Keep API/tool arguments separate when the runtime supports structured parameters.",
    )

    return findings


def lint_general(path: str, text: str, lines: Sequence[tuple[int, str]]) -> list[Finding]:
    findings: list[Finding] = []
    objective_terms = re.compile(
        r"\b(?:goal|objective|task|create|write|rewrite|analy[sz]e|compare|extract|classify|summari[sz]e|design|build|produce|return|deliverable)\b",
        re.IGNORECASE,
    )
    if len(text.split()) > 80 and not objective_terms.search(text):
        findings.append(
            Finding(
                path=path,
                severity="low",
                code="UNCLEAR_OBJECTIVE",
                line=None,
                message="Long prompt has no obvious objective or deliverable. Put the requested outcome near the top.",
            )
        )
    return findings


def lint(path: str, text: str, mode: str, context: str) -> tuple[str, list[Finding]]:
    actual_mode = infer_mode(path, text) if mode == "auto" else mode
    lines = visible_lines(text)
    findings = lint_common(path, text, lines)

    if actual_mode == "coding":
        findings.extend(lint_coding(path, text, lines, context))
    elif actual_mode == "system":
        findings.extend(lint_system(path, text, lines))
    elif actual_mode == "image":
        findings.extend(lint_image(path, text, lines))
    else:
        findings.extend(lint_general(path, text, lines))

    findings.sort(
        key=lambda item: (
            -SEVERITY_RANK[item.severity],
            item.line if item.line is not None else 10**9,
            item.code,
        )
    )
    return actual_mode, findings


def render_text(results: Sequence[dict[str, object]]) -> str:
    chunks: list[str] = []
    for result in results:
        path = str(result["path"])
        mode = str(result["mode"])
        findings = result["findings"]
        assert isinstance(findings, list)
        chunks.append(f"{path} [{mode}]")
        if not findings:
            chunks.append("  OK: no heuristic findings")
            continue
        for raw_finding in findings:
            assert isinstance(raw_finding, dict)
            line = raw_finding.get("line")
            location = f":{line}" if line is not None else ""
            chunks.append(
                f"  {str(raw_finding['severity']).upper():6} "
                f"{raw_finding['code']}{location} -> {raw_finding['message']}"
            )
            excerpt = raw_finding.get("excerpt")
            if excerpt:
                chunks.append(f"         {excerpt}")
    return "\n".join(chunks)


def should_fail(findings: Sequence[Finding], threshold: str) -> bool:
    if threshold == "never":
        return False
    minimum = SEVERITY_RANK[threshold]
    return any(SEVERITY_RANK[finding.severity] >= minimum for finding in findings)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    results: list[dict[str, object]] = []
    all_findings: list[Finding] = []

    try:
        inputs = list(iter_inputs(args.paths))
    except (OSError, UnicodeError) as exc:
        print(f"prompt_lint: {exc}", file=sys.stderr)
        return 2

    if not inputs:
        print("prompt_lint: no supported prompt files found", file=sys.stderr)
        return 2

    for path, text in inputs:
        actual_mode, findings = lint(path, text, args.mode, args.context)
        all_findings.extend(findings)
        results.append(
            {
                "path": path,
                "mode": actual_mode,
                "context": args.context,
                "findings": [asdict(finding) for finding in findings],
            }
        )

    if args.output_format == "json":
        print(json.dumps({"results": results}, ensure_ascii=False, indent=2))
    else:
        print(render_text(results))

    return 1 if should_fail(all_findings, args.fail_on) else 0


if __name__ == "__main__":
    raise SystemExit(main())
