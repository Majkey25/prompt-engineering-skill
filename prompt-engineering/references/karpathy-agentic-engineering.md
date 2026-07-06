# Karpathy First Agentic Engineering

Use for coding-agent prompts, repo work, /goal prompts, migrations, refactors, bug fixes, UI work, and production-quality software prompts.

## Core doctrine

Karpathy's strongest useful signal is not "let AI write unchecked code". It is the boundary between playful prototype flow and serious engineering.

- Vibe coding -> fast prototype loop. Good for demos, throwaway scripts, learning, and creative exploration.
- Agentic engineering -> production loop. Requires specs, repo evidence, planning, diff review, verification, ownership, and maintenance.

Generated prompts must push real software work toward agentic engineering by default.

## Production default

For real repos, user-facing apps, migrations, auth, billing, data, security, deployment, refactors, UI preservation, backend APIs, performance, or anything the user may keep:

```text
Mode -> production.
No blind vibe coding.
Use highest available reasoning effort. Do not expose private chain-of-thought.
Specs -> repo evidence -> plan -> small change -> inspect diff -> verify live -> fix -> short report.
You own result. Do not say done because code was generated.
```

## Prototype exception

Only use this when user explicitly wants a quick prototype, throwaway demo, toy app, sketch, or experiment:

```text
Mode -> prototype.
Optimize for speed + visible result.
Still avoid secrets, destructive actions, fake APIs, unsafe commands, and broken install steps.
Report shortcuts + missing checks.
```

## The prompt is code

Treat prompts like source code:

- version important prompts
- make them scoped
- remove vague lines
- add success criteria
- add verification
- test against examples
- refactor when repeated
- move durable rules into repo instruction files or skills

## Human ownership

Generated coding prompts must say:

```text
AI can write code. Human still owns architecture, taste, security, data safety, and final judgment.
Review the diff. Do not accept generated changes blindly.
```

## Diff review gate

Include in every coding-agent prompt:

```text
After edits, review your own diff before final answer.
Look for bloat, repetition, accidental rewrites, style drift, weak abstractions, fake APIs, changed behavior, missed edge cases, security risk, and visual mismatch.
Fix safe issues before finishing.
```

## Missing context

For coding prompts with incomplete project information:

```text
Do not guess repo structure, files, functions, packages, APIs, commands, tests, env vars, or framework behavior.
Inspect repo and current official docs when needed.
Find the relevant code, callers, contracts, tests, and conventions before editing.
Then implement the smallest safe change.
```

## Ask/Plan before Code

For large/risky changes:

```text
First work in Ask/Plan mode. Do not edit yet.
Map repo -> affected files -> risks -> small plan.
Then implement the smallest safe slice.
```

Use for:

- migrations
- architecture changes
- broad refactors
- security hardening
- auth/session changes
- payment/billing
- database/data model
- deployment/infrastructure
- UI preservation/pixel matching
- performance work

## Subagent default

For generated coding prompts, include subagent guidance only when it helps. Useful subagents: repo mapper, docs verifier, QA/test agent, UI/browser agent, security/review agent, and diff reviewer. Keep one primary implementation owner. Subagents gather evidence or review; they do not replace ownership or invent unsupported implementation details.

## Live verification default

Generated prompts must require real checks where possible:

- run app/dev server/preview/backend/CLI
- run relevant build/lint/typecheck/test commands
- click UI with browser tools when UI is involved
- inspect console/network/server logs
- verify changed path and nearby old path
- report exact blocker if verification cannot run

## Anti-vibe replacements

Replace weak prompts:

- "vibe code this" -> "prototype quickly; list shortcuts + missing checks"
- "make production ready" -> "run build/lint/typecheck/live flow; fix scoped runtime errors; verify main path; report blockers"
- "just fix it" -> "reproduce issue -> root cause -> minimal fix -> verify broken path + nearby old path"
- "refactor everything" -> "scope refactor targets -> preserve behavior -> change minimal files -> verify"
- "make UI better" -> "define visual target -> preserve or change specified parts -> screenshot verify"

## Failure patterns to guard against

- accepting every diff
- not reading generated code
- shipping demo-quality code as production
- giant context dump
- broad rewrite without plan
- fake API/package names
- fixing tests instead of bug
- suppressing errors
- no rollback path
- no live verification
- no final risk report

## Final response target for coding agents

Require one short paragraph or at most 3 bullets, not a rigid report template. Include what changed, what was verified, and real blockers or risks only. Exact commands, screens, flows, endpoints, or URLs are useful when they prove verification. Skip empty sections and filler.
