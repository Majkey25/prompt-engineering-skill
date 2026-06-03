# Research Backed Principles

Last researched: 2026-06-03.

Use this file as decision support. For full reusable structure, load `best-prompt-blueprint.md`.

## Core rules

- Prompt quality is measured by output reliability, not by impressive wording.
- Define success criteria before heavy prompt engineering.
- Prefer the shortest prompt that fully specifies goal, context, constraints, output format, and verification.
- Separate instructions from user/source data with Markdown sections, XML tags, triple quotes, or schemas.
- Use zero-shot for simple tasks. Add few-shot examples only when consistency, labels, edge cases, or style need them.
- For factual work, require source grounding, citation/unsupported policy, and conflict handling.
- For agentic work, include tool-use rules, observation/action loop, done definition, and verification evidence.
- For important prompts, run representative cases, inspect failures, patch minimally, and retest.
- Treat prompts as technical debt: keep them short, reviewed, scoped, versioned when critical, and easy to delete.

## Model-specific reasoning

- OpenAI reasoning models: keep prompts simple/direct; avoid forcing visible chain-of-thought by default.
- Gemini and other providers may expose model-specific reasoning/planning controls; follow the current provider docs for the target model.
- Prefer "reason internally, validate, then return concise rationale" when the final output needs quality but not private reasoning.
- If visible reasoning is required for teaching/audit, ask for a concise explanation, not unrestricted chain-of-thought.

## Prompt shape

Strong prompts usually include:

1. Objective
2. Context/source data
3. Task/deliverable
4. Constraints/non-goals
5. Output format/schema
6. Examples if useful
7. Process/tool-use guidance
8. Verification/eval criteria
9. Failure/uncertainty policy
10. Style/length controls

Role/persona is optional. Use it only when it changes decisions.

## Source-specific takeaways

### OpenAI

- Put clear instructions near the start for ordinary API prompts.
- Delimit instruction and context.
- Be specific about outcome, length, format, style, and audience.
- Show desired output format with examples when needed.
- Start zero-shot, add few-shot when needed, then consider deeper optimization.
- Use prompt optimization with datasets, annotations, graders, and manual review for production prompts.

### Anthropic

- Establish success criteria and empirical tests before prompt engineering.
- Use clear/direct instructions, examples, XML structure, prompt chaining, and evals.
- Tune verbosity, effort, tool use, and update behavior explicitly when the target model needs it.

### Google Gemini

- Use structured sections for role, instructions, constraints, context, task, and output format.
- For current or grounded answers, make date/currentness and source-bound behavior explicit.
- Tune reasoning/planning instructions by model and cost/latency requirements.

### Microsoft/Azure OpenAI

- Use clear framing, separators, examples, grounding, and explicit output constraints.
- Validate generated answers even when prompt engineering is strong.

### The Prompt Report

- Prompting has many named techniques. Do not cargo-cult them.
- Select the smallest technique that matches the task and observed failure mode.

### Prompts as technical debt

- Avoid filling AGENTS.md, skill files, or system prompts with generic behavior steering.
- Do not keep old model folklore unless it still passes evals.
- Prefer concrete project facts, tool rules, and done criteria.
- Delete prompt rules whenever the base model/tool already handles the behavior.

## Sources

- OpenAI Help: https://help.openai.com/en/articles/6654000-best-practices-for-prompting
- OpenAI prompt engineering: https://platform.openai.com/docs/guides/prompt-engineering
- OpenAI reasoning best practices: https://platform.openai.com/docs/guides/reasoning-best-practices
- OpenAI prompt generation: https://platform.openai.com/docs/guides/prompt-generation
- OpenAI prompt optimizer: https://platform.openai.com/docs/guides/prompt-optimizer
- Anthropic prompt engineering overview: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- Anthropic prompting best practices: https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Google Gemini prompt strategies: https://ai.google.dev/gemini-api/docs/prompting-strategies
- Microsoft Azure OpenAI prompt engineering: https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/prompt-engineering
- The Prompt Report: https://arxiv.org/abs/2406.06608
- Prompts are technical debt too: https://www.seangoedecke.com/prompts-are-technical-debt-too/
