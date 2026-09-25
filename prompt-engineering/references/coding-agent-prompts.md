# Coding Agent Prompt Template

Use for Codex, Claude Code, Cursor agents, Copilot agents, Windsurf, Aider, ChatGPT agents, MCP/browser agents, and repository implementation tasks.

The default is outcome-first agentic engineering. Give the agent the job, evidence, boundaries, and done state. Let it choose the implementation path unless the path itself is a requirement.

## Mandatory context gate

Load `coding-context-calibration.md` and classify prompt-writer evidence:

- C0: no repository or authoritative project source inspected. State desired behavior and discovery targets. Do not invent project details.
- C1: partial supplied evidence. Preserve exact supplied facts and label implementation theories as hypotheses.
- C2: relevant repository/source evidence directly inspected. Use verified specifics only where they help.

## Default copy-paste template

Use this compact form for most coding tasks:

```text
# Goal
[Describe the externally observable result. State what must remain unchanged when relevant.]

# Context
Known:
- [user-supplied or verified facts]

Hypotheses:
- [suspected root cause / implementation idea; omit if none]

Unknowns:
- Inspect the repository, docs, logs, tests, and runtime as needed. Do not invent project details.

# Boundaries
- Stay within the requested scope. No unrelated refactors, cleanup, features, or dependency churn.
- Treat implementation suggestions as hypotheses unless marked mandatory.
- Preserve existing behavior, interfaces, style, and architecture unless the task requires a change.
- Choose the files, implementation approach, tools, and delegation yourself based on repository evidence.
- Ask before destructive, hard-to-reverse, externally visible, costly, or materially out-of-scope actions.
- If ambiguity does not materially affect correctness, safety, authorization, or the requested outcome, choose the narrowest reasonable interpretation and proceed.

# Done
You are done when:
- the real root cause or required change is understood,
- the requested behavior works,
- behavior that should remain unchanged still works based on relevant checks,
- the strongest practical verification available has been performed,
- the diff contains no unrelated changes,
- and any remaining blocker or risk is stated concretely.

Do not stop at a plan or explanation when implementation was requested. Continue while a safe, in-scope next action can complete or materially verify the task.

# Verification
Use the project's existing verification path and real runtime/workflow where practical. Choose checks proportionate to the change. Do not weaken tests or fake success. If verification cannot run, report the exact blocker.

# Final response
Keep it concise. State what changed, what was verified, and only real remaining blockers or risks.
```

This is the default, not a mandatory schema. Delete sections that add no value.

## Exact-process exception

Add step-by-step process only when the process itself matters, for example:

- compliance or audit procedure,
- irreversible migration ordering,
- reproducible benchmark protocol,
- required release sequence,
- security approval boundary,
- user-mandated workflow,
- or a measured recurring failure that general outcome guidance does not fix.

Do not write a step list merely because the model is capable of following one.

## Repository discovery

At C0/C1, give discovery targets rather than fake implementation detail.

Good:

```text
Inspect the relevant implementation, callers, contracts, nearby patterns, tests, project instructions, and existing verification commands before choosing the fix.
```

Bad:

```text
Edit src/foo.ts, change bar(), run npm test, then create three subagents.
```

unless those exact details are supplied or verified requirements.

Never speculate about code that the target agent can inspect.

## Root-cause and hypothesis handling

If the user says "I think X is the bug," preserve it as evidence, not truth:

```text
I suspect [X], but verify the actual root cause before choosing the implementation. Do not optimize for proving my theory.
```

This prevents the prompt from turning a useful suspicion into a false constraint.

## Scope control

Use outcome-level scope rules:

```text
Fix the requested problem completely, but do not add unrelated features, cleanup, abstractions, or redesigns. Expand scope only when a narrower change would leave the root cause intact, break a contract, or create a temporary workaround.
```

Avoid giant negative lists unless evals show a specific recurring failure.

## Decision authority

For normal implementation requests, let the agent own technical choices inside scope:

```text
Choose the implementation approach, files, tools, and any useful delegation yourself from repository evidence. Prefer the simplest safe solution consistent with existing project patterns.
```

Do not prescribe a fixed number of subagents, exact file list, or tool sequence unless required.

## Clarification policy

Prevent unnecessary stalls without authorizing risky guessing:

```text
Ask only when missing information could materially change correctness, safety, authorization, or the requested outcome. Otherwise choose the narrowest reasonable interpretation, state any important assumption briefly, and proceed.
```

## Planning

Visible planning is optional, not ritual.

Use a short plan before editing only when the task is broad, risky, migration-heavy, security-sensitive, or benefits from user review before changes. For small scoped fixes, let the agent inspect and act directly.

When a plan is required, ask for decisions and risk, not ceremony:

```text
Before editing, briefly state the affected area, main risk, and chosen approach. Then continue with implementation unless approval is explicitly required.
```

## Subagents

Modern agents may orchestrate delegation themselves. Default to giving them freedom to choose.

Add explicit subagent instructions only when:

- independent workstreams can run in parallel,
- isolated context reduces risk,
- an independent reviewer is required,
- or evals show the agent delegates poorly.

If over-delegation is a problem:

```text
Use subagents only for independent or parallel work that benefits from isolated context. For simple, sequential, single-file, or tightly coupled work, act directly.
```

## Verification

Prompt for evidence, not a ceremonial command checklist.

Default:

```text
Verify the changed behavior using the project's strongest relevant existing checks and the real workflow/runtime where practical. Match verification depth to risk. If a check is unavailable, report the exact blocker rather than claiming success.
```

Name exact commands, browsers, endpoints, screenshots, or test suites when:

- the user requires them,
- repository evidence confirms they are the correct path,
- or they are part of the acceptance criteria.

For UI work, browser verification and screenshots are useful when the runtime/tooling supports them. For APIs, use the real endpoint or integration path when practical. For migrations, compare before/after behavior when risk warrants it.

## Tests

Do not force a fixed test count or framework.

- Use existing tests when relevant.
- Add the smallest focused regression coverage when externally observable behavior changes and the repo has a suitable test layer.
- Do not weaken or rewrite tests just to make the patch pass.
- Do not invent a test runner.

## Diff review

A compact self-review instruction is usually enough:

```text
Before finishing, inspect the final diff for unrelated churn, incomplete root-cause fixes, regressions, unnecessary abstractions, fake APIs, missing validation, and unverified assumptions. Fix safe in-scope issues, then stop.
```

Do not ask for endless opportunistic cleanup.

## Large/risky task add-on

Use when architecture, auth, billing, data, deployment, migration, security, or broad behavior is involved:

```text
Before editing, map the affected contracts and risks from repository evidence. Choose the smallest safe sequence of changes. Preserve rollback/recovery where relevant. Verify incrementally and compare before/after behavior for high-risk paths.
```

## Prototype add-on

Only when the user explicitly wants a prototype:

```text
Mode: prototype. Optimize for a working visible result with minimal machinery. Keep secrets and destructive actions safe. Report shortcuts and missing verification.
```

## Literal Ponytail/Caveman/Unslop directives

Do not paste them automatically. Use the behaviors while authoring the prompt. Include literal `@ponytail`, `@caveman`, or `@unslop` lines only when the user requests them, the runtime consumes them, or evals show they help.

## Tool-specific notes

### Codex

- Keep prompts outcome-first when the prompt writer has not inspected the repo.
- Use AGENTS.md only for durable verified project rules.
- Let the agent discover implementation details and existing checks.

### Claude Code

- Keep CLAUDE.md short and durable.
- Let Claude inspect project state instead of pre-writing its implementation plan.
- Give it verification access and clear completion criteria.

### Cursor / Copilot / Windsurf / Aider

- Put persistent rules in the platform's scoped instruction files only when they are stable.
- Keep task prompts focused on the current outcome and evidence.
- Do not duplicate repository facts or generic process rules across every request.
