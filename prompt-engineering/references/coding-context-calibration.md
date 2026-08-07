# Coding Context Calibration

Use this file whenever a prompt is being written for Codex, Claude Code, Cursor, Copilot, Windsurf, Aider, ChatGPT coding agents, or any agent that will inspect a repository after receiving the prompt.

## Contents

- [Core rule](#core-rule)
- [C0, C1, and C2 context levels](#context-levels)
- [Specificity ledger](#specificity-ledger)
- [C0 discovery-first template](#c0-discovery-first-prompt-template)
- [C1 partial template](#c1-partially-grounded-template)
- [C2 grounded template](#c2-project-grounded-template)
- [Frontend and UI prompts](#frontend-and-ui-prompts)
- [Bad versus good rewrites](#bad-versus-good-rewrites)
- [Self-check](#prompt-writer-self-check)

## Core rule

Prompt specificity must not exceed evidence specificity.

A prompt writer who has not inspected the project must not design the implementation. State the outcome and constraints, then tell the repository-aware agent what evidence to inspect before deciding how to implement it.

## Context levels

Classify the available context before writing the prompt.

### C0: No project evidence

You have only the user's request or a rough issue description. You have not inspected the repository, files, screenshots, logs, package manifests, docs, or runtime.

Allowed:

- desired user-visible behavior
- business objective
- exact constraints stated by the user
- non-goals stated by the user
- discovery instructions for the target agent
- verification outcomes
- general safety and scope rules

Forbidden as facts:

- file paths or file names not supplied by the user
- function, class, route, component, table, or variable names not supplied by the user
- framework, language, package manager, database, test runner, or deployment platform guesses
- commands, flags, environment variables, schemas, APIs, or dependencies not supplied by the user
- exact UI architecture, component choices, palette, spacing system, or layout
- implementation steps that depend on unknown architecture

Default output: a lean discovery-first coding prompt.

### C1: Partial evidence

You have some exact user-provided material, such as a snippet, error, screenshot, issue, file name, stack name, or log, but not enough to understand the full project.

Allowed:

- exact supplied facts
- clearly labeled hypotheses
- instructions to verify the supplied clue against the repository
- narrower search guidance based on the supplied evidence

Do not convert:

- a likely location into a confirmed location
- a sample name into an existing symbol
- an error message into a proven root cause
- a screenshot into a complete design system
- a framework mentioned by the user into proof of the current repository version or structure

Default output: a partially grounded prompt that labels known facts and unknowns.

### C2: Verified project evidence

The relevant repository state, files, configuration, tests, docs, design references, and runtime evidence were directly inspected, and that evidence is available to the prompt writer.

Allowed:

- exact paths, symbols, commands, versions, data flow, and project conventions that were actually observed
- an implementation direction supported by repository evidence
- precise acceptance criteria tied to existing tests or workflows

Still forbidden:

- unsupported claims outside inspected scope
- stale details copied from unrelated branches or docs
- invented APIs or commands
- turning one local pattern into a global architecture rule without evidence

Default output: a project-specific coding prompt with cited or clearly traceable evidence.

## Specificity ledger

Before producing a coding prompt, sort material into four buckets:

```text
Provided by user:
- exact facts and requirements

Observed directly:
- facts verified from repository, tools, docs, logs, or screenshots

Inferred:
- plausible interpretation that the target agent must verify

Unknown:
- facts the target agent must discover before implementation
```

Only the first two buckets may appear as facts. Inferences must be labeled. Unknowns must become discovery tasks, not fabricated details.

## C0 discovery-first prompt template

Use this as the default when the prompt writer cannot inspect the project.

```text
# Goal
[State the requested user-visible or system-visible outcome. Do not add a guessed stack or implementation.]

@ponytail / Use Ponytail full: simplest safe solution that works. Make the smallest semantically complete change that fixes the root cause, preserves required behavior, avoids unrelated change, and is supported by verification proportionate to risk. Optimize semantic scope, not line count or textual diff size. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. Do not trade away correctness, clarity, validation, explicit errors, typing, or necessary tests to make the patch smaller. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.

# Known requirements
- [Only requirements explicitly supplied by the user.]

# Unknown project facts
- The prompt writer has not inspected this repository.
- Do not assume the stack, architecture, file layout, symbols, dependencies, commands, tests, or design system.

# Discover before implementation
- Inspect repository instructions, README/docs, manifests, lock files, configuration, and existing scripts.
- Locate the current implementation, callers, data flow, contracts, tests, and nearby patterns relevant to the requested outcome.
- Identify the actual verification path from repository evidence.
- For current external APIs or packages, inspect the repository version first, then consult official documentation when needed.
- Summarize the evidence and choose the smallest semantically complete implementation that fits the project.

# Constraints
- Preserve unrelated behavior and existing conventions.
- Do not invent files, functions, APIs, packages, commands, schemas, or UI requirements.
- Do not redesign or broaden scope unless the requested outcome requires it and repository evidence supports the expansion.
- Do not ask the user to perform checks the agent can run.

# Verification
- Run the relevant existing checks discovered in the project.
- Verify the affected workflow directly when the environment permits.
- Review the final diff for unsupported assumptions, unrelated churn, and incomplete behavior.
- Report exact evidence or the exact blocker.

# Done
The requested outcome works, relevant existing behavior is preserved, verification is complete, and the diff contains no unrelated changes. If verification is blocked, report the task as incomplete with the exact blocker; do not call it done.
```

Remove unused sections. Do not fill them with guesses to make the prompt look complete.

## C1 partially grounded template

Insert the shared Ponytail + Caveman contract immediately after `# Goal`; it is omitted below to avoid duplicating the source of truth in `SKILL.md`.

```text
# Goal
[Requested outcome]

# Supplied evidence
- [Exact user-provided file, error, screenshot, snippet, stack detail, or constraint]

# Treat as hypotheses until verified
- [Likely interpretation, clearly labeled]

# Repository work
- Verify the supplied evidence in the current checkout.
- Find the relevant implementation, callers, tests, contracts, and project conventions.
- Let repository evidence determine the implementation.

# Requirements
- [Only supplied requirements]

# Constraints and verification
[Use the existing coding-agent guardrails proportionate to risk.]
```

## C2 project-grounded template

For risky production work, use the full coding-agent template after relevant evidence is available. Include:

- verified target paths and symbols
- observed current behavior
- exact required behavior
- affected contracts and callers
- existing project commands
- existing design references
- concrete verification path

Label evidence source when ambiguity matters, for example:

```text
Observed in `package.json`: project uses [tool/version].
Observed in `[path]`: current flow does [behavior].
User requires: [new behavior].
```

## Frontend and UI prompts

### Existing product

Tell the agent to inspect:

- current pages and nearby flows
- design tokens and theme configuration
- shared components
- typography and spacing patterns
- responsive behavior
- accessibility patterns
- screenshots, Figma, Canva, or other actual references

Use this default:

```text
Preserve the product's established visual language unless redesign is explicitly requested. Reuse existing components and tokens when they fit. Do not impose a generic card, gradient, palette, font, animation, or layout doctrine. Verify the affected flow visually and functionally.
```

### Greenfield UI with no visual reference

Do not compensate for missing design context by inventing a rigid style system in the prompt. Define the outcome:

```text
Create a coherent, usable, accessible, and responsive interface appropriate to the product's purpose. Use strong visual hierarchy and interaction design. Choose implementation and visual details after inspecting the available stack and assets. Avoid generic filler UI, but do not force a predetermined aesthetic without a real requirement.
```

### Supplied visual reference

Be specific about fidelity:

```text
Use the supplied reference as the source of truth for composition, hierarchy, spacing, typography, imagery, and states. Preserve unrelated behavior. Compare screenshots after implementation and correct material differences.
```

Do not infer invisible states, breakpoints, or components from one screenshot without checking the project or asking only when the target agent cannot discover them.

## Bad versus good rewrites

### Unknown repository

Bad:

```text
Edit src/components/Dashboard.tsx, add a Zustand store, create useDashboardData(), and use Tailwind grid cards.
```

Why bad: every implementation detail may be fabricated.

Good:

```text
Add the requested dashboard behavior. First inspect the repository to find the actual dashboard implementation, state/data pattern, shared components, styling system, and existing tests. Use those patterns and implement the smallest complete change. Do not introduce a state library or visual redesign unless repository evidence and the requirement justify it. Verify the dashboard flow and review the diff.
```

### Partial error report

Bad:

```text
The refresh token function in src/auth/token.ts is broken. Replace it with Axios interceptors.
```

Good:

```text
Users report login failure after session timeout. Treat the refresh-token explanation as a hypothesis. Reproduce the failure, trace the actual auth/session flow, inspect existing HTTP client patterns and tests, identify the root cause, implement the smallest safe fix, and verify both timeout recovery and normal login. Do not add a new client or interceptor pattern without repository evidence.
```

### No UI reference

Bad:

```text
Use a dark navy background, glassmorphism cards, purple gradients, 24px rounded corners, Inter, and Framer Motion.
```

Good:

```text
Build the requested screen after inspecting the app's existing design system and nearby screens. Preserve its visual language. If the project is truly greenfield and has no style reference, choose a coherent accessible direction appropriate to the product instead of following a fixed generic aesthetic.
```

## Prompt writer self-check

Before returning a coding prompt, ask:

1. Did I inspect the project myself?
2. Which details came directly from the user?
3. Which details are observations, and where were they observed?
4. Did I turn any hypothesis into a fact?
5. Did I name a file, function, framework, command, API, package, test, or UI pattern without evidence?
6. Can the target agent discover this detail more reliably from the repository?
7. Am I constraining implementation because of a real requirement, or because the template had an empty slot?
8. Would a shorter outcome-focused prompt leave useful model capability intact?

If evidence is C0, the answer must be discovery-first.
