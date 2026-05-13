# Evals And Iteration

Prompt quality is measured, not felt.

## Start with success criteria

Before improving a prompt, define what good output looks like.

Bad:

```text
Make it high quality.
```

Better:

```text
Success -> output uses source facts, follows format, has no unsupported claims, handles edge cases, and can be used without edits.
```

## Use the smallest useful eval

For quick human eval:

```text
Grade 0-2:
- follows task
- follows format
- uses evidence
- handles edge cases
- no hallucinated claims
- concise enough
```

For automation:

- exact string checks
- schema validation
- required fields present
- forbidden phrases absent
- citation count
- diff size
- command exit code
- screenshot/visual check
- model grader for subjective quality

## Prompt iteration loop

1. Draft prompt.
2. Run on 3-5 representative cases.
3. Label outputs good/bad.
4. Write specific critique.
5. Identify failure pattern.
6. Update prompt minimally.
7. Re-test.
8. Keep what improves real cases.

## Failure diagnosis

If output is vague -> add goal/context/examples.
If output drifts -> add constraints + output schema.
If output hallucinates -> add source rules + uncertainty policy.
If output overdoes work -> narrow scope + done definition.
If output ignores format -> add few-shot examples + strict schema.
If output is too long -> add caveman style + max length.
If coding agent breaks app -> add repo analysis + live verification + self review.

## Production prompt rules

- Keep a test set of real prompts.
- Add edge cases from failures.
- Review optimized prompts manually before using.
- Do not chase one example if it hurts broader cases.
- Keep versioned prompts when business critical.

## Coding-agent evals

Use observable checks:

- app starts
- changed route works
- endpoint returns expected shape
- CLI command exits 0
- build/lint/typecheck pass where relevant
- tests pass if existing/relevant
- UI screenshots match when preservation required
- console/network logs clean enough
- final answer includes exact verification evidence

## Done definition template

```text
Done ->
- [outcome] complete
- [constraints] preserved
- [checks] run or blocker documented
- [risks] listed
- final output matches format
```
