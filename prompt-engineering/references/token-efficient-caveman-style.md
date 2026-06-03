# Token Efficient Caveman Style

Use to reduce cost, latency, and context bloat without weakening the task.

## Header line

After token-efficient style is selected, add:

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

## Compact output for agents

When prompting an agent, require:

```text
Final reply: caveman concise.
Include only: summary, files, verification, risks.
No filler. No "great question". No fake certainty.
```
