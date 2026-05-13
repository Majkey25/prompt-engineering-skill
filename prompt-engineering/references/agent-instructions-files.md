# Agent Instruction Files

Use when the user wants reusable repo-level or tool-level AI rules.

## Principle

Rules that repeat belong in files, not every chat prompt.

Keep them short, concrete, scoped, and version-controlled.

## AGENTS.md

For Codex and other agents that read AGENTS.md.

```markdown
# Project instructions

## Commands
- Install: [command]
- Run: [command]
- Test: [command]
- Lint: [command]
- Typecheck: [command]

## Architecture
- Main entry point: [path]
- Important folders: [paths]
- Do not touch: [paths / generated files]

## Coding style
- Follow existing patterns.
- Keep changes minimal.
- Use clear names.
- Comments: simple English only.

## Testing
- Add/update tests for behavior changes when project patterns exist.
- Do not weaken tests to pass.
- Fix root causes.

## Safety
- Do not hardcode secrets.
- Do not invent APIs.
- Do not run destructive commands without explicit approval.
- No broad rewrites without plan.

## Output
- Summarize changed files.
- Include verification results.
- Mention anything not verified.
```

## CLAUDE.md

For Claude Code project memory. Keep short. Delete lines that do not prevent real mistakes.

```markdown
# Claude project notes

## Start here
- Read: [README/path]
- Main app: [path]
- Key scripts: [commands]

## Rules
- Explore first -> plan -> code.
- Use existing patterns.
- Keep edits scoped.
- Verify with [commands/screenshots/expected output].
- Manage context. Start fresh after task completion.

## Do not
- Do not touch [paths].
- Do not add deps without reason.
- Do not suppress errors.
```

## Cursor rules

Use `.cursor/rules/*.mdc` for scoped reusable rules.

Good Cursor rules:

- focused
- actionable
- scoped by glob when possible
- under 500 lines
- split by domain
- include examples only when useful

Example:

```mdc
---
description: API validation rules
globs: ["src/api/**/*.ts"]
alwaysApply: false
---

- Validate request bodies with existing schema helper.
- Return typed error responses.
- Do not add new validation library.
- Follow examples in src/api/users.ts.
```

## GitHub Copilot instructions

Repo-wide:

```text
.github/copilot-instructions.md
```

Path-specific:

```text
.github/instructions/*.instructions.md
```

Rules:

- short standalone statements
- avoid conflicts
- put path-specific rules near matching files
- include commands and project conventions

## Windsurf

Prompt shape:

```text
Goal -> [specific]
Context -> @file @folder [relevant only]
Constraints -> [must/must not]
Verification -> [run/check]
Output -> [summary format]
```

## Aider

Use `CONVENTIONS.md` for repeated rules:

```markdown
# Conventions

- Follow existing style.
- Keep changes scoped.
- Do not add deps without asking.
- Run [test command] when relevant.
- Comments simple English only.
```

## Bad rules

- "use best practices"
- "write clean code"
- "make production ready"
- "optimize everything"
- giant architecture essay
- stale commands
- rules that contradict each other
