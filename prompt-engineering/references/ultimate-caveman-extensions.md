# Ultimate Ponytail + Caveman Extensions

Use when the user wants maximum prompt quality, low token cost, strict review, coding-agent prompts, production-grade prompts, multi-agent review, benchmark prompts, or hostile review behavior.

## Purpose

Make prompts shorter, sharper, and harder to misunderstand. Do not make them dumber.

Caveman style is not broken grammar. It is compressed engineering language:

- short sections
- exact verbs
- symbols where clear
- no motivational filler
- no fake quality words
- no long disclaimers
- no repeated constraints
- complete verification

## Required Ponytail + Caveman lines

Add near the top of generated technical/agent prompts:

```text
@ponytail / Use Ponytail full: simplest safe solution that works. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

## Compression rules

Prefer:

```text
Goal -> migrate React Router -> Next.js App Router.
Keep UI same.
Verify with Playwright Interactive.
```

Over:

```text
Your task is to carefully migrate the application from React Router to Next.js App Router while ensuring that the visual design remains unchanged and that verification is performed using Playwright Interactive.
```

Use symbols only when they reduce noise and keep meaning clear:

- `->` for transformation or sequence
- `=>` for result
- `+` for additive requirements
- `/` for alternatives or paired concepts
- `[]` for placeholders
- `OK/FAIL` for validation result
- `must / must not` for hard constraints

## Do not compress away risk controls

Never remove:

- scope
- constraints
- safety rules
- input assumptions
- success criteria
- verification
- edge cases
- final response format
- blocker reporting
- source/citation rules
- user-visible behavior preservation

Wrong:

```text
Fix app. Test. Done.
```

Right:

```text
Goal -> fix dashboard UI.
Keep visual design same.
Find real stack from repo.
Change minimal files.
Run app.
Use Playwright -> check dashboard, console, network.
Done only after verified or exact blocker reported.
```

## Hostile review mode

Use for coding, architecture, migrations, security, performance, data pipelines, prompts that control agents, and any production-risk task.

Insert this section:

```text
# Hostile review
Before final answer, review like a demanding senior reviewer having a bad day.
Find: fragile logic, hidden regressions, bad names, missing validation, broken edge cases, visual mismatch, broad rewrites, weak abstractions, fake APIs, ignored errors, fake success, and unverified assumptions.
Fix every safe issue.
Do not mark done while core workflow is unverified.
```

## Multi-agent review pattern

Use when the user mentions Codex, Claude Code, multiple agents, high quality, or brutal review.

```text
# Agent split
- Implementer: [Codex/Claude/agent A] changes code.
- Reviewer: [Claude/Codex/agent B] reviews diff + behavior.
- Reviewer must not rubber-stamp.
- Reviewer checks scope, regressions, style, tests, live verification, security, UI, performance.
- Implementer fixes valid review findings.
- Final answer includes review findings + fixes.
```

Do not always require two agents. Use this when available and worth the cost.

## Production-first contract

For serious tasks, add:

```text
Production rule:
No blind vibe coding.
No "looks done".
No unverified success.
Specs -> repo evidence -> plan -> small change -> run -> review diff -> verify -> report.
```

## Benchmark-first contract

For prompts where quality can be measured, add:

```text
Benchmark:
Define cases before optimizing.
Include easy + hard + negative cases.
Compare output to success criteria.
Do not claim improvement without evidence.
Report table: case / expected / actual / OK / notes.
```

## Prompt self-review loop

Before returning a prompt, check:

- Is the goal concrete?
- Is the target agent/tool named?
- Is context scoped?
- Are success criteria testable?
- Are constraints enforceable?
- Are vague words translated?
- Is output format explicit?
- Is verification present?
- Is `@ponytail / Use Ponytail full` present when the prompt is technical/agentic?
- Is `@caveman / Talk caveman` present?
- Did compression remove anything important?

If any answer is no -> fix the prompt before returning it.

## Weak words translation

Replace weak words:

- "better" -> exact metric/behavior to improve
- "clean" -> naming, duplication, errors, unused code, structure in touched scope
- "production ready" -> build/run/verify/error handling/security/config/doc checks in scope
- "optimize" -> measured hot path + baseline + change + post-check
- "fix everything" -> block goal + directly related issues only
- "best practices" -> repo conventions + official docs + measurable constraints

## Final compact prompt header

For high-value prompts, use this header:

```text
# Goal
[one precise outcome]

@ponytail / Use Ponytail full: simplest safe solution that works. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.

# Contract
No fake done.
No hidden assumptions.
No broad rewrite unless required.
Stdlib/native/existing deps first.
Verify current APIs/libs/functions before using them when stale risk exists.
Verify with real tools when possible.
Report blockers exactly.
```
