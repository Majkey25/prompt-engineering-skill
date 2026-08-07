# Ponytail + Caveman Contract

Use this reference when generated prompts should force both small-scope engineering and terse output.

## Required block

```text
@ponytail / Use Ponytail full: simplest safe solution that works. Make the smallest semantically complete change that fixes the root cause, preserves required behavior, avoids unrelated change, and is supported by verification proportionate to risk. Optimize semantic scope, not line count or textual diff size. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. Do not trade away correctness, clarity, validation, explicit errors, typing, or necessary tests to make the patch smaller. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

## Use

Include for coding-agent, repo, automation, workflow implementation, technical research, prompt-audit, and production-quality prompts.

For CR/code review, use `review-rubric.md` and keep the task review-only unless edits are explicitly requested.

Skip or isolate outside the output schema for exact JSON, customer-facing copy, legal/medical prose, image/video prompt text, and creative writing.

## Self-check

- Ponytail present when task can create implementation bloat.
- Caveman present when terse agent communication helps.
- No requirement lost to compression.
- No new dependency without clear evidence.
- Current APIs/functions verified when stale risk exists.
- Smallest semantically complete change, not smallest line count or textual diff.
- Scope expands only for a stated correctness or architecture reason.
- Verification depth matches risk; focused regression coverage is added when behavior changes and the repo has a suitable test layer.
- Editing stops once the requested outcome is proven and the diff is clean.
