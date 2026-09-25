# Evals And Iteration

Prompt quality is measured, not felt.

For important prompts, compare at least three variants on the same cases:

1. Baseline: platform default or no custom prompt
2. Minimal: smallest prompt containing true requirements
3. Candidate: proposed full prompt

A blank or shorter prompt is allowed to win.

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

1. Define cases and observable success criteria.
2. Run baseline, minimal, and candidate with stable model/runtime settings.
3. Label outputs and record exact failures, token use, latency, and cost.
4. Identify the failure pattern.
5. Update the smallest relevant instruction group. Prefer changing outcome/boundary/done wording before adding process choreography.
6. Re-test all variants.
7. Remove one instruction group at a time and rerun.
8. Keep only rules that improve real cases or enforce a non-negotiable boundary.

## Failure diagnosis

If output is vague -> add goal/context/examples.
If output drifts -> add constraints + output schema.
If output hallucinates -> add source rules + uncertainty policy.
If output overdoes work -> narrow scope + done definition.
If output ignores format -> add few-shot examples + strict schema.
If output is too long -> add caveman style + max length.
If coding agent breaks app -> add missing repo evidence, scope/authority boundaries, and verification first. Add exact process steps only if the failure is truly procedural and repeats.

## Production prompt rules

- Keep a test set of real prompts.
- Add edge cases from failures.
- Review optimized prompts manually before using.
- Do not chase one example if it hurts broader cases.
- Keep versioned prompts when business critical.
- Track false constraints, unsupported specificity, and unnecessary process prescription, not only task success.
- Blind reviewers to variant names when subjective quality matters.
- Use `scripts/make_prompt_eval.py` for a starter manifest, then replace placeholders with real cases.

## System-prompt and frontend evals

For system prompts, include normal, ambiguous, edge, adversarial, initiative, and approval cases.

For frontend-related global instructions, run a blind comparison:

- A: no custom visual doctrine
- B: outcome-only guidance such as coherent, usable, accessible, responsive, and project-consistent
- C: detailed visual doctrine with fixed palette, components, typography, layout, or animation

Score product fit, hierarchy, usability, accessibility, responsiveness, consistency with the actual project, implementation correctness, and false constraints. Reject C when A or B performs better.

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
- C0 prompts avoid unsupported files, functions, stacks, commands, tests, env vars, and UI choices
- C1 prompts label hypotheses and verify them
- C2 prompts use correct inspected project specifics

## Done definition template

```text
Done ->
- [outcome] complete
- [constraints] preserved
- [checks] run or blocker documented
- [risks] listed
- final output matches format
```
