# Goal Patterns

`/goal` is a strong signal for an agentic coding prompt. Convert it into a complete work contract, but do not expand it into boilerplate for its own sake.

## Default `/goal` conversion

Input:

```text
/goal Migrate this project from [legacy] to [target]. Make sure all screens stay exactly the same visually, using playwright interactive to verify the output.
```

Output intent:

- State the migration outcome and what must remain unchanged.
- Tell the agent to inspect the real stack and existing patterns before choosing implementation details.
- Add only the migration-specific constraints that matter.
- Treat Playwright Interactive as a required verification method because the user explicitly named it.
- Define a done state that includes preserved behavior/visuals and verified output.
- Let the agent choose the exact files, change sequence, and delegation unless the task supplies a required sequence.

## Task classes

### Migration

Define target state, behavior/data/route/UI preservation requirements, rollback or compatibility constraints when relevant, and before/after verification. Do not pre-write a migration sequence unless ordering is required.

### Refactor

Define behavior/API preservation, scope boundaries, and acceptance checks. Let the agent choose the internal refactor path from repository evidence.

### Bugfix

Describe the broken behavior and expected behavior. Preserve the user's suspected cause as a hypothesis. Require root-cause validation, the smallest safe fix, and verification of the broken path plus nearby behavior when useful.

### Feature

Define the user-visible capability, integration boundaries, non-goals, and acceptance criteria. Let the agent discover the existing pattern and choose implementation details.

### UI preservation or pixel matching

State exactly what must remain visually unchanged and which reference/baseline controls truth. Require browser/screenshot verification when available. Do not inject taste-driven design instructions.

### UI redesign

Define the design outcome, supplied references/brand constraints, preserved functional flows, and acceptance criteria. Avoid hard-coding a generic design system without evidence.

### Backend/API change

Define required externally observable contract changes and compatibility requirements. Let the agent inspect routes, schemas, clients, and tests before deciding implementation.

### Type or lint cleanup

Define the concrete target and forbid unrelated behavior changes. Let the agent discover the repo's existing tooling.

### Performance improvement

Define the metric/hot path and success threshold when known. Require baseline and post-change evidence. Do not prescribe an optimization technique before measurement.

### Security hardening

Define the threat/abuse path or security property to improve, authorization boundaries, and verification. Do not turn a guessed mitigation into a mandatory implementation unless required.

### Full project cleanup

Reject unlimited cleanup. Convert it into scoped outcomes and directly related blockers. Do not authorize broad rewrites by default.

### Repo onboarding before implementation

Ask the agent to discover only the project facts needed to execute the requested work. Do not spend more time producing a repo tour than solving the task.
