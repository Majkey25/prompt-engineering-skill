# Token Efficient Ponytail + Caveman Style

Use to reduce cost, latency, implementation bloat, and context bloat without weakening the task.

Use Ponytail + Caveman together for generated coding, repo, technical-agent, automation, workflow, and prompt-audit prompts. Use only Caveman for non-coding prompts where implementation minimalism is irrelevant.

Do not force it into:

- creative writing
- customer-facing prose
- legal or medical wording
- exact JSON output
- user-visible copy where tone matters more than tokens

## Required technical-agent block

For coding, repo, automation, workflow, technical research, and prompt-audit prompts, add:

```text
@ponytail / Use Ponytail full: simplest safe solution that works. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

For non-coding prompts where only terse style is needed, add only:

```text
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

## What to compress

Compress:

- greetings
- filler
- motivational language
- repeated explanations
- long prose transitions
- obvious statements
- verbose headings

Do not compress away:

- constraints
- success criteria
- verification
- safety rules
- edge cases
- schemas
- exact commands
- exact file paths
- exact API names
- Ponytail requirements: stdlib/native/existing deps first, no speculative abstractions, no unverified current APIs

## Symbols

Use symbols when readable:

- `->` sequence
- `=>` consequence/result
- `+` include/and
- `/` alternatives or paired concepts
- `[]` placeholders
- `<=` limits
- `!=` not equal / forbidden

Example:

```text
Goal -> fix dashboard route.
Ponytail -> minimal diff; existing deps first; verify current APIs before use.
Keep -> UI/layout/colors unchanged.
Verify -> run app + Playwright + console/network check.
Done => changed flow works + old flow still works.
```

## Bad compression

Bad:

```text
fix app fast. test maybe. done.
```

Good:

```text
Goal -> fix login bug.
Scope -> minimal files.
Verify -> reproduce bug, fix root cause, run existing checks, test login live.
Stop -> no fake done; report blocker if cannot run.
```

## Agent final replies

When prompting an agent and terse output is desired, require:

```text
Final reply: concise.
Include only: summary, files, verification, risks.
No filler. No fake certainty.
```
