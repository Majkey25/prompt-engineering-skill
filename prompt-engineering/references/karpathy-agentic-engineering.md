# Karpathy First Agentic Engineering

Use for coding-agent prompts, repo work, `/goal`, migrations, refactors, bug fixes, UI work, and production-quality software prompts.

## Core doctrine

Fast AI coding is useful. Production work still needs ownership, scope discipline, evidence, verification, and review.

The prompt should define the engineering contract, not hand-write the agent's implementation path.

## Production default

For real repositories and user-facing work:

```text
Own the requested outcome through completion.
Inspect the real repository before choosing implementation details.
Use the smallest semantically complete safe change consistent with existing project patterns.
Stay within scope. Do not add unrelated cleanup or features.
Verify the changed behavior with the strongest relevant existing checks and real workflow where practical.
Do not claim done without evidence or an exact blocker.
```

Do not add "use highest reasoning effort", hidden chain-of-thought requests, or a mandatory plan unless the target runtime or task specifically requires them.

## Prototype exception

```text
Mode: prototype. Optimize for a working visible result with minimal machinery. Keep secrets and destructive actions safe. Report shortcuts and missing verification.
```

Use only when the user explicitly wants a prototype, demo, sketch, or throwaway experiment.

## The prompt is code

Treat important prompts like source code:

- keep them scoped,
- version when business-critical,
- remove vague and duplicate rules,
- add observable success criteria,
- test against representative cases,
- delete rules that no longer improve outcomes.

## Human ownership

Do not paste generic "human owns everything" boilerplate into every prompt. Preserve real approval boundaries and require review where risk warrants it.

## Diff review gate

For code-changing tasks, a compact self-review is useful:

```text
Before finishing, inspect the final diff for unrelated churn, regressions, unnecessary abstractions, missing validation, fake APIs, and unverified assumptions. Fix safe in-scope issues, then stop.
```

## Missing context

```text
Do not guess repo structure, files, functions, packages, APIs, commands, tests, env vars, or framework behavior. Inspect the relevant code, project instructions, callers/contracts, nearby patterns, and existing checks before choosing the implementation.
```

## Planning

Planning is conditional.

Require a brief plan before editing when architecture, migrations, auth, billing, security, data, deployment, or other broad/high-risk behavior makes sequencing and review valuable.

For small scoped tasks, do not force a plan. Let the agent inspect and execute.

## Subagents

Do not prescribe delegation by default. Let capable agents choose whether subagents help.

Constrain delegation only when:

- independent workstreams should be isolated,
- parallel work has real leverage,
- an independent review lane is required,
- or evals show over-delegation/under-delegation.

## Semantic minimality

- Optimize for smallest **semantically complete** change, not smallest line count.
- Fix root cause and preserve required behavior.
- Expand scope only for correctness/contract reasons.
- Stop when the requested outcome is proven and the diff is clean.

## Verification

Ask for the evidence standard, not a universal command list:

```text
Verify using the project's strongest relevant existing checks and the real affected workflow/runtime where practical. Match depth to risk. Report exact blockers when verification cannot run.
```

Name exact commands or tools only when supplied, verified, or required.

## Anti-vibe translations

- "vibe code this" -> define whether this is prototype or production and what done means
- "make production ready" -> define observable behavior, risk boundaries, and verification
- "just fix it" -> define broken vs expected behavior, scope, and done state
- "refactor everything" -> narrow the desired outcome and preservation contract
- "make UI better" -> define the visual/product outcome and reference truth

## Final response target

Ask for a concise recap of what changed and what was verified. Mention blockers/risks only when real. Do not force a rigid multi-heading report unless the user needs it.
