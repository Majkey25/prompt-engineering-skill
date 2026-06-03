# Coding Agent Prompt Template

Use for Codex, Claude Code, Cursor agent, Copilot agent, Windsurf, Aider, ChatGPT agent, MCP agents, browser agents, and repo tasks.

Default stance: Karpathy-first agentic engineering. Fast AI is useful. Blind vibe coding is not acceptable for production work.

## Copy-paste template

```text
# Goal
[Specific outcome. Include target stack, scope, and what must stay unchanged.]

# Mode
Production unless I explicitly say prototype.
No blind vibe coding.
Use AI speed + engineering discipline.
Specs -> repo evidence -> plan -> small changes -> diff review -> live verification -> final report.

# Communication
Be concise. Use exact technical names. No filler. Keep requirements, validation, evidence, and safety checks intact.

# Context
Known:
- [project facts]
- [user constraints]
- [relevant files/routes/screenshots/errors]
Unknown:
- Mark unknowns. Find answers in repo before assuming.

# Non negotiable requirements
- Detect real stack from repository files. No framework/tool/test-runner guesses.
- Preserve existing behavior unless explicitly changed.
- Preserve existing style, naming, architecture, and formatting conventions.
- Change only files needed for this task.
- No fake APIs, packages, commands, flags, routes, env vars, or framework features.
- No broad rewrite without written reason + small plan.
- No hardcoded secrets. No unsafe destructive commands.
- Do not ask me to test what you can test.
- Do not say done unless verified or exact blocker is documented.

# Repository analysis
1. Read README/docs.
2. Inspect package files + lock files.
3. Inspect config: build, lint, typecheck, test, framework, env examples, CI.
4. Find entrypoints, routes, components, API clients, backend setup, data flow.
5. Identify existing scripts and verification path.
6. Summarize stack + affected files + risks before editing.

# Plan before code
Before editing:
1. Restate task in <= 3 bullets.
2. List affected files.
3. List risks.
4. Give small implementation plan.
Then implement.

# Implementation rules
- Prefer existing tools/patterns.
- Keep changes minimal.
- Validate data at boundaries.
- Keep error handling explicit.
- Avoid formatting churn.
- Do not add dependencies unless needed + justified.
- Verify after each major slice when practical.

# Live verification
- Run existing install/setup only if needed.
- Run existing build/lint/typecheck/test commands when relevant.
- Start app/dev server/preview/backend/CLI if environment allows.
- Verify changed workflow live.
- Verify one nearby old workflow still works.
- Investigate failures. Fix root cause, not symptom.
- If verification cannot run, state exact command tried + exact blocker.

# UI verification
[Include for UI tasks]
- Use Playwright / Playwright Interactive if available.
- Capture baseline screenshot if original state can run.
- Capture post-change screenshot.
- Compare main screens visually.
- Check console errors.
- Check network failures.
- Click through affected user flow.
- Check responsive layout if relevant.
- Do not redesign by taste if goal is preservation.

# Testing rules
- Use existing tests when relevant.
- Add/update tests only when they reduce real risk and match repo patterns.
- Pytest is not default. Use pytest only if repo already uses it, I ask for it, or pytest infra clearly exists.
- Do not weaken tests to pass.

# Strict diff/self review
Before final answer, review your own diff like a demanding reviewer having a bad day.
Find: bloat, repetition, fragile logic, hidden regressions, bad names, missing validation, broken edge cases, visual mismatch, unnecessary rewrites, weak abstractions, fake success, unverified assumptions, ignored errors.
Fix every safe issue before finalizing.

# Done definition
Done only when:
- Requested change is implemented.
- Behavior that should remain unchanged still works based on checks.
- Changed workflow was live verified, or blocker is exact.
- Relevant build/lint/typecheck/test/browser/backend/CLI checks were run when available.
- Diff was self-reviewed.
- Risks are explicit.

# Final response
Return:
1. Summary
2. Files changed
3. Diff review findings
4. Verification run: exact commands / URLs / screens / endpoints / flows
5. Failures or blockers
6. Remaining risks
```

## Large change prepend

Use for migrations, architecture changes, security, auth, payment, data model, performance, or UI preservation:

```text
First work in Ask/Plan mode. Do not edit yet.
Map repo -> identify risks -> propose plan.
Then implement the smallest safe slice.
Continue while a clear safe next step improves confidence.
```

## Prototype prepend

Only if user asks for quick prototype:

```text
Mode -> prototype.
Optimize for speed + visible result.
Still avoid secrets, destructive actions, fake APIs, and broken install steps.
Report shortcuts + missing checks.
```

## Tool-specific notes

### Codex
- For large work, start with Ask mode plan, then Code mode implementation.
- Use AGENTS.md when repo rules should persist.
- Require terminal/log/test evidence when available.

### Claude Code
- Use CLAUDE.md for durable project memory.
- Keep CLAUDE.md short, specific, and useful.
- Give screenshots/tests/expected outputs so Claude can verify.
- Manage context aggressively.

### Cursor
- Use .cursor/rules for scoped reusable rules.
- Rules should be focused, actionable, scoped, and split when large.
- Add relevant files, not the whole repo.
- Start a new chat after a logical task.

### Copilot
- Use .github/copilot-instructions.md for repo-wide context.
- Use .github/instructions/*.instructions.md for path-specific rules.
- Keep instructions short and self-contained.

### Windsurf
- Include objective, relevant context, constraints, and @ mentions.
- Do not rely on vague intent.

### Aider
- Put repeated style/project rules in CONVENTIONS.md.
- Keep coding prompt scoped and file-aware.

## Optional token-efficient header

Add only when the user requests caveman/token compression or the prompt must be extremely compact:

```text
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```
