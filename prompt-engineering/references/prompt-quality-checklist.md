# Prompt Quality Checklist

Run before returning an important generated prompt or using an autoprompt brief.

## Core must pass

- Desired outcome is specific.
- Done state is observable/testable when the task has a meaningful completion condition.
- Context is relevant and separated from instructions.
- User suspicions or implementation preferences are labeled as hypotheses unless explicitly mandatory.
- Constraints and non-goals are concrete.
- Agent authority/approval boundary is clear when actions are possible.
- Output format is specified only as tightly as needed.
- Verification/evidence expectations exist when the outcome matters.
- Failure/uncertainty behavior exists for factual, risky, or incomplete tasks.
- Unsupported assumptions are not presented as facts.
- Prompt specificity does not exceed supplied or verified evidence.
- The prompt is no larger or more prescriptive than the task and eval evidence justify.

## Process-prescription check

Every explicit step, tool, file, subagent role, or command must answer: **why must this be prescribed?**

Keep it only if:

- order/procedure is part of the requirement,
- it is required for reproducibility/compliance/safety,
- it comes from verified project/runtime evidence,
- the user explicitly requested it,
- or evals show the general outcome prompt repeatedly fails without it.

Otherwise remove it and let the target choose the path.

## Agentic prompt must pass

- Action requests do not accidentally stop at a plan.
- Scope blocks unrelated features, cleanup, refactors, and redesigns.
- The agent may choose method/files/tools/delegation inside scope unless restricted for a reason.
- Destructive, irreversible, externally visible, costly, or materially out-of-scope actions have an approval boundary when the runtime does not already enforce one.
- Clarification is requested only when ambiguity could materially change correctness, safety, authorization, or the requested outcome.
- Verification asks for evidence, not fake certainty.

## Coding-agent must pass

- C0 prompts are discovery-first and do not invent repo details.
- C1 prompts preserve supplied facts and mark implementation theories as hypotheses.
- C2 prompts use only verified project specifics that help.
- Root-cause discovery is not replaced by a user guess.
- The prompt does not force exact files, commands, tests, or subagents without evidence/need.
- Small scoped work does not require ceremonial planning.
- Large/risky work may require a brief plan, sequencing, rollback, or independent review.
- Verification depth matches risk and uses existing project paths when possible.
- Tests are not weakened or invented to manufacture success.
- Diff/self-review is concise and bounded.
- Done definition prevents unrelated cleanup after the requested outcome is proven.

## System/developer prompt must pass

- Starts from platform-default/no-custom baseline for important use cases.
- Contains durable cross-task behavior, not current task data or guessed project facts.
- Separates advisory prompt rules from deterministic controls.
- Does not encode a fixed tool sequence or planning ritual without a durable reason.
- States each instruction once and resolves conflicts.
- Has representative eval cases and an ablation path when important.
- Accepts a shorter/blank custom prompt when it performs better.

## Examples check

Use examples only if they improve:

- format consistency,
- style/tone consistency,
- classification/extraction boundaries,
- or recurring edge cases.

Do not add examples because a provider/template says they are always good. Test them on the target runtime.

## Prompt debt check

Delete or rewrite a rule if:

- it is generic behavior steering with no measurable purpose,
- it was added for an old model/problem and no longer helps,
- it conflicts with another rule,
- it repeats tool/schema/runtime behavior,
- it narrows the solution path without a requirement,
- it forces planning/delegation for trivial work,
- nobody can explain how to test it,
- baseline/minimal behavior is equal or better without it,
- or it turns an unknown/hypothesis into a fake fact.

## Vague phrase conversion

Bad -> Better

- improve project -> define the user-visible or measurable result
- make better -> define audience + success criteria
- use best practices -> follow verified project/source constraints
- clean code -> define concrete maintainability issue in scope
- optimize -> state metric + baseline/target if known
- production ready -> define behavior, risk boundary, and verification
- fix everything -> define the requested outcome + directly related blockers

## Final self-check

1. Could another competent agent understand the job without guessing the outcome?
2. Does done mean something observable?
3. Did I turn context into an instruction accidentally?
4. Did I prescribe a process that is not actually required?
5. Is the agent free to make useful decisions inside scope?
6. Are real approval boundaries explicit?
7. Is unrelated scope expansion blocked?
8. Would the target likely do better with less instruction?
9. Which exact rule would I remove first in an ablation?
