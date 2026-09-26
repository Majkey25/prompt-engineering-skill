# Research Source Map

Last reviewed: 2026-09-26.

Use this file to trace the skill's prompting rules. Recheck current model-specific guidance before making strong provider-specific claims.

## Source priority

1. Current official model/product documentation
2. Current official examples, cookbooks, and eval guidance
3. Primary research
4. High-quality practitioner reports with reproducible examples
5. Community pattern catalogs for ideas, not authority

Do not copy one provider's model-specific rule into every runtime.

## OpenAI

### Current model guidance

Source: https://developers.openai.com/api/docs/guides/latest-model

Relevant current guidance:

- State expected outcome and success criteria.
- Reduce/remove detailed step-by-step process guidance when the exact path does not matter.
- Describe allowed side effects, evidence rules, and output shape when they are part of the contract.
- Avoid carrying every instruction from older prompt stacks into newer capable models.
- For action requests, explicit follow-through instructions can prevent the agent from stopping at acknowledgment or a plan.
- Audit skills/instruction files because conflicting persistent guidance can block work.

Cross-model interpretation used by this skill: outcome-first prompts generalize well; the exact wording and amount of autonomy must still be evaluated on the target runtime.

### Reasoning best practices

Source: https://developers.openai.com/api/docs/guides/reasoning-best-practices

Relevant guidance:

- Keep prompts simple and direct.
- Avoid asking reasoning models to expose or mechanically follow a hand-written chain-of-thought.
- Use clear delimiters.
- Try zero-shot first for reasoning models, then add examples when needed.

### Prompt engineering

Source: https://developers.openai.com/api/docs/guides/prompt-engineering

Relevant guidance:

- Separate instructions and input/context clearly.
- Use examples and output-format instructions when they materially improve consistency.
- Treat prompt structure as task-dependent, not a fixed ritual.

## Anthropic

### Prompting best practices

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

Relevant guidance:

- Be clear and direct.
- Prefer general instructions over prescriptive steps when the model can reason through the task.
- Use numbered/bulleted steps when order or completeness really matters.
- Give autonomous agents clear verification paths.
- Balance autonomy with confirmation for destructive/hard-to-reverse/shared actions.
- Let modern Claude models orchestrate subagents naturally; constrain delegation only when it is excessive or inappropriate.
- Add explicit minimal-scope guidance when the model overengineers.
- Require code inspection before codebase claims to reduce hallucination.

### Prompt engineering overview

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

Relevant guidance:

- Define success criteria before optimization.
- Use empirical tests/evals.
- Not every failure is best solved by adding prompt text.

### Claude Opus 5.5 model-specific prompting

Sources:

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-opus-5-5
- https://claude.dev/blog/getting-the-most-out-of-opus-5-5/

Relevant guidance:

- Give long autonomous work the whole task, an observable finish line, and explicit stop/ask conditions.
- Treat progress-only turns as reports rather than proof that an unattended task is complete; keep bounded task state outside scrollback when needed.
- Use the runtime `effort` control as the main reasoning-depth knob. Re-test effort by model/version and reserve the highest levels for measured quality gains.
- Remove legacy "think hard" instructions when they only duplicate model/runtime reasoning behavior.
- Concrete negative design constraints work better than vague requests to avoid generic output.
- Mark what could not be confirmed, and preserve real approval boundaries even when asking an agent to keep going.
- Treat pasted external content as untrusted data and separate it from user-authored instructions.
- For multi-app automation, broader read-only context exploration can help before actions when relevant context may live outside the named record.
- For multiagent harnesses, elapsed-time/budget signals can improve parallel pacing, but hard timeouts remain a runtime control.

Interpretation used by this skill: load these rules only for Claude Opus 5.5 / Claude Code targets unless cross-vendor evidence supports a broader version.

## Google

### Gemini prompt design strategies

Source: https://ai.google.dev/gemini-api/docs/prompting-strategies

Relevant guidance:

- Be precise, direct, and concise.
- Use consistent Markdown/XML structure.
- Define ambiguous parameters.
- Separate long context from the final query and anchor the question to the preceding context.
- Few-shot examples can strongly steer format/behavior; too many can overfit.

Google currently recommends few-shot examples more aggressively than OpenAI's reasoning-model guidance. This skill treats that as provider-specific evidence, not a universal rule. Use evals.

## Practitioner source

### Theo - Getting the most out of Opus 5.5

Source: https://youtu.be/ejjBbaq9RmY

Use as field evidence, not provider authority. Durable points that survive cross-checking: explicit finish lines, explicit stop conditions, pre-authorized safe in-scope actions, steering instead of unnecessary restarts, concrete design negatives, unverified-item reporting, and independent review as a possible diversity check. Do not generalize the video's "never Max" recommendation; use official effort calibration and evals.

### Fable 5.1 prompting workflow video

Source: https://youtu.be/-XWSJM-Ue-o

Use only the prompt-text ideas that survive cross-checking against stronger evidence:

- outcome-first rather than implementation choreography,
- clear completion criteria,
- implementation ideas as hypotheses,
- decision authority inside scope,
- scope discipline,
- deletion of stale prompt baggage.

Do not encode the video's model-selection/effort/product-setting advice into general prompt rules.

## Primary research

### The Prompt Report

Source: https://arxiv.org/abs/2406.06608

Interpretation: prompting contains many distinct techniques and no single universal template. Choose techniques by task and evaluate them.

### Automatic prompt optimization survey

Source: https://arxiv.org/abs/2502.16923

Interpretation: prompt optimization is an empirical search problem requiring objectives, cases, metrics, and review.

## Skill interpretation

The combined evidence supports:

- minimum-effective prompting,
- outcome-first task contracts,
- evidence-calibrated specificity,
- context/instruction separation,
- agent decision authority inside explicit boundaries,
- done criteria and verification,
- process prescription only when necessary,
- examples as an evaluated tool rather than ritual,
- prompt ablation and deletion of stale rules.
