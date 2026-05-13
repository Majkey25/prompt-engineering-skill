# Strict Review Rubric

Use for coding prompts, important prompts, and autoprompt self-checks.

## Standard strict review text

```text
Before finishing, run strict self-review. Act like a demanding reviewer having a bad day.
Find: fragile logic, hidden regressions, bad names, missing validation, broken edge cases, visual mismatches, unnecessary rewrites, weak abstractions, fake success, unverified assumptions, ignored errors, token bloat, and places where output only works accidentally.
Fix every safe issue before finalizing.
```

## Coding diff review

Check:

- scope creep
- behavior drift
- API/schema changes
- visual drift
- runtime errors
- type/lint errors
- console/network errors
- dead code
- repeated logic
- fake APIs/packages
- secret exposure
- unsafe commands
- missing rollback
- unverified claims

## Prompt review

Check:

- vague goal
- missing success criteria
- missing constraints
- bloated context
- no examples where examples matter
- no output format
- no eval/verification
- contradictions
- too much caveman compression
- hidden assumptions

## Repair rule

Do not merely report issues. Fix safe issues before final answer.
