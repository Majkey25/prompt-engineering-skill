# Goal Patterns

`/goal` is a strong signal for an agentic coding prompt. Do not merely rewrite the sentence. Expand it into the full prompt structure.

## Default `/goal` conversion

Input:

```text
/goal Migrate this project from [legacy] to [target]. Make sure all screens stay exactly the same visually, using playwright interactive to verify the output.
```

Output intent:

- Treat as a coding-agent implementation prompt.
- Add stack discovery.
- Add migration inventory.
- Add visual preservation rules.
- Add Playwright Interactive verification.
- Add live verification default.
- Add strict self review.
- Add final report format.

## Task classes

### Migration
Add migration inventory, route mapping, behavior mapping, data-flow mapping, incremental implementation, UI preservation, old/new comparison, smoke tests, and migration report.

### Refactor
Require behavior preservation, public API preservation, small steps, no formatting churn, targeted typing cleanup, and live verification of unchanged behavior.

### Bugfix
Require reproduction first when possible, root cause, minimal fix, regression check, and live verification of the broken workflow.

### Feature
Require existing pattern discovery, minimal design, integration with current architecture, validation, and live verification of the new user flow or endpoint.

### UI preservation or pixel matching
Require baseline screenshot when possible, post-change screenshot, visual comparison, responsive checks, console and network inspection, and no taste-driven redesign.

### UI redesign
Require explicit design goal, preserve functional flows, verify responsiveness, check console and network, and avoid unrelated backend changes.

### Backend/API change
Require route and schema inventory, compatibility notes, request/response validation, live endpoint checks, and old client flow verification.

### Type cleanup or lint cleanup
Require existing tooling discovery, minimal semantic changes, no behavior changes, command reruns, and no blanket ignores unless justified.

### Performance improvement
Require baseline observation, scoped optimization, no behavior regressions, and practical verification of the hot path when possible.

### Security hardening
Require threat-aware review, least privilege, input validation, safe error handling, no secret leaks, and live checks of relevant deny/allow paths where possible.

### Full project cleanup
Convert vague cleanup into scoped buckets: build/runtime errors, dead code, typing, lint, structure, docs, and verification. Do not allow unlimited rewrites.

### Repo onboarding before implementation
Require repository map, commands, entrypoints, risks, and then implementation. Do not spend forever documenting instead of shipping the requested change.
