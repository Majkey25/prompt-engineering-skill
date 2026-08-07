# System Prompt Architecture

Use this file when creating, rewriting, or auditing a system prompt, developer prompt, assistant policy, agent constitution, global behavior prompt, or reusable product-level instruction set.

## Contents

- [Core rule](#core-rule)
- [Instruction layers](#do-not-confuse-instruction-layers)
- [Stable versus dynamic content](#stable-versus-dynamic-content)
- [Minimum-effective workflow](#minimum-effective-system-prompt-workflow)
- [Recommended contents](#recommended-system-prompt-contents)
- [Frontend restraint](#frontend-and-visual-design-restraint)
- [Compact templates](#compact-templates)
- [Audit and output](#system-prompt-audit)

## Core rule

Use the minimum effective system prompt.

A system prompt should define durable behavior that must apply across many requests. It should not pre-solve future tasks, guess project details, or impose taste that the model already handles well.

Start from the model's unprompted or minimally prompted baseline. Add a rule only when at least one condition is true:

- It encodes a real product requirement.
- It defines an authorization or approval boundary.
- It prevents a measured recurring failure.
- It establishes a tool-use contract the runtime does not enforce.
- It defines a stable output contract shared by most requests.
- It handles a material safety, privacy, compliance, or data-loss risk.

If none applies, leave the behavior to the model.

## Do not confuse instruction layers

Map the runtime before writing. Different layers serve different purposes.

| Layer | Put here | Do not put here |
|---|---|---|
| System / developer | Durable role, scope, global priorities, authority boundaries, stable tool policy | One task's data, guessed project structure, temporary UI request |
| User prompt | Current objective, supplied context, task-specific constraints, deliverable | Global product policy that must survive every request |
| Project instruction file | Verified project commands, conventions, architecture decisions, recurring gotchas | Generic language rules, guessed file map, stale docs |
| Tool description | Exact tool capability, inputs, outputs, side effects, errors | General assistant personality, duplicate global rules |
| Deterministic runtime control | Permissions, schemas, hooks, validators, sandboxing, hard limits | Advisory prose that must never fail |
| Eval suite | Representative tasks, edge cases, regressions, scoring | Production instructions shown to the model |

When a requirement can be enforced deterministically, prefer code, permissions, schemas, hooks, validators, or tool restrictions over repeated prompt prose.

## Stable versus dynamic content

Keep stable behavior in the system or developer layer:

- product role and supported scope
- action versus advice boundaries
- confirmation requirements
- source and uncertainty policy
- global privacy and security constraints
- tool selection principles
- durable response requirements

Keep dynamic content in the user/task layer:

- current goal
- repository facts
- file names and function names
- screenshots and design references
- target audience for one artifact
- one-off output format
- current errors, logs, or acceptance criteria

Do not cache temporary facts as global behavior.

## Minimum effective system prompt workflow

1. Identify the target model, runtime, tools, and authority hierarchy.
2. Define 3 to 8 representative tasks and at least 2 failure cases.
3. Run a baseline with no custom system prompt or the platform default.
4. Write the smallest prompt that adds only missing durable behavior.
5. Compare baseline, minimal, and candidate prompts on the same cases.
6. Remove one instruction group at a time and rerun the evals.
7. Keep only rules whose removal causes a measurable regression or violates a real requirement.
8. Move deterministic requirements out of prose when possible.

Never treat prompt length or strict tone as evidence of quality.

## Recommended system prompt contents

Use only the sections that earn their place.

### Identity and purpose

One sentence is often enough.

Good:

```text
You are an engineering assistant that inspects repositories, implements requested changes, and reports verification evidence.
```

Weak:

```text
You are a world-class, elite, visionary, award-winning software genius.
```

A role is useful only when it changes decisions, scope, expertise, tone, or risk posture.

### Scope

State what the assistant handles and what it does not handle when the boundary is not obvious.

```text
Handle repository analysis, implementation, debugging, and code review. Do not make external writes unless the user explicitly requests them.
```

### Autonomy and approval boundaries

Define what action the user authorizes by default.

```text
For requests to explain, review, diagnose, or plan, inspect relevant materials and report findings without editing.
For requests to build, change, or fix, make in-scope local changes and run non-destructive validation.
Require confirmation for destructive actions, external writes, purchases, credential changes, or material scope expansion.
```

State this policy once. Repeating permission warnings can make capable agents unnecessarily passive.

### Tool policy

Describe selection rules and side effects, not every obvious operation.

```text
Use tools when they provide evidence or complete requested work. Read before writing. Inspect tool results before choosing the next action. Do not invent tool outputs or unsupported parameters.
```

Tool schemas should carry exact arguments and return fields.

### Evidence and uncertainty

```text
Treat supplied data and tool results as evidence. Distinguish verified facts, user claims, inferences, and unknowns. Do not fill missing facts with plausible specifics.
```

### Output policy

Keep global output rules narrow. Task-specific formats belong in the user prompt.

```text
Return the requested deliverable. Include concise verification evidence and real blockers when work involved tools or edits.
```

### Conflict policy

```text
Follow higher-authority instructions over lower-authority ones. When same-level requirements conflict, preserve safety and user intent, state the conflict briefly, and choose the least destructive interpretation.
```

## Frontend and visual design restraint

Do not encode a house style into a global coding system prompt unless the product genuinely requires that style.

Bad global rules:

- Always use cards, gradients, rounded corners, and large hero sections.
- Use a specific palette, font, framework, component library, or animation style for every frontend.
- Avoid or require a visual motif based only on personal taste.
- Prescribe exact layouts for projects the prompt writer has not inspected.

These rules can override the model's stronger native design judgment and conflict with the repository's design system.

Use outcome-level rules instead:

```text
For frontend work, inspect the existing product, design system, components, assets, and nearby screens before choosing a visual direction. Preserve established visual language unless redesign is requested. For greenfield UI without a supplied style, use sound design judgment to produce a coherent, usable, accessible, and responsive result. Do not impose a fixed palette, component pattern, or layout doctrine without evidence.
```

Add detailed visual constraints only when they come from:

- a user request
- a brand guide
- a reference screenshot or design file
- existing repository patterns
- an accessibility requirement
- a measured recurring failure in evals

For visual work, verification should use screenshots, interaction checks, responsive views, and comparison against actual references. It should not compare against invented taste rules.

## Avoid overprescription

Do not add instructions that:

- tell a capable model every intermediate step without a measured need
- duplicate platform behavior, tool descriptions, or schemas
- encode implementation details for unknown future projects
- require planning for trivial tasks
- require subagents for every task
- demand a fixed response structure for unrelated outputs
- use repeated CRITICAL, MUST, NEVER, or similar emphasis to compensate for prompt bloat
- ask for hidden chain-of-thought
- force a frontend aesthetic unrelated to the user or project
- solve one historic failure at the expense of normal cases

Prefer outcome, boundaries, evidence, and done criteria over choreography.

## Compact templates

### Minimal assistant

```text
You are [purpose].

Help with [scope]. Use available sources and tools when they materially improve accuracy or complete the requested work. Do not invent missing facts. Follow the user's requested output and state real uncertainty or blockers briefly.
```

### Tool-using agent

```text
You are an agent for [purpose].

For analysis requests, inspect relevant evidence and report findings. For action requests, make the requested in-scope changes and verify them. Read before writing. Require confirmation for destructive actions, external writes, costly actions, or material scope expansion. Treat tool results as evidence and never invent results. Stop when the requested outcome is verified or an exact blocker remains.
```

### Coding agent without project-specific facts

```text
You are a repository coding agent. Understand the actual codebase before choosing an implementation. For requested changes, locate the relevant code, conventions, dependencies, callers, tests, and verification commands; then implement the smallest semantically complete safe change. Do not invent files, functions, frameworks, APIs, commands, or design requirements. Preserve existing behavior and visual language unless the request changes them. Verify the affected workflow and report concise evidence.
```

### Prompt-engineering assistant

```text
You design and audit prompts for the target model and runtime. Start from the minimum effective prompt, separate durable system behavior from task-specific context, and never add unsupported project or product details. Compare important prompts against a baseline and representative eval cases. Add constraints only for real requirements or measured failures, and remove instructions that do not improve outcomes.
```

## System prompt audit

Check every rule:

1. What exact failure or requirement does it address?
2. Is it stable across most requests?
3. Is this the correct instruction layer?
4. Can the runtime enforce it instead?
5. Does it duplicate another rule?
6. Could it suppress a model capability or conflict with user intent?
7. Is its effect covered by an eval?
8. What happens if the rule is removed?

Classify each rule:

- Keep: required and validated.
- Move: useful, but belongs in user context, a skill, project file, tool schema, or code.
- Narrow: valid only for a subset of tasks.
- Test: plausible but not yet supported by evals.
- Remove: generic, duplicate, stale, harmful, or untestable.

## Required output when designing a system prompt

When the user asks simply for a finished system prompt, perform the architecture and eval analysis internally and output only the prompt.

When the user requests an audit, design rationale, implementation package, or prompt documentation, return:

1. Target runtime and assumptions
2. Instruction-layer map
3. Final minimal system prompt
4. Requirements that should be enforced outside the prompt
5. Eval cases and comparison plan
6. Known risks or unresolved conflicts
