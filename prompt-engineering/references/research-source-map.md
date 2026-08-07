# Research Source Map

Last reviewed: 2026-08-03.

Use this selected source map for newer model-specific and research-backed rules. It is not a complete citation database. Recheck current model guidance before making strong claims because prompting behavior changes across model generations.

## Contents

- [Source priority](#source-priority)
- [OpenAI](#openai)
- [Anthropic](#anthropic)
- [Google](#google)
- [Courses and practitioner education](#courses-and-practitioner-education)
- [Primary research](#primary-research)
- [Skill interpretation](#interpretation-used-by-this-skill)

## Source priority

1. Current official model and product documentation
2. Current official examples, cookbooks, courses, and eval guidance
3. Primary research papers
4. High-quality practitioner reports with reproducible examples
5. Community pattern catalogs for ideas, not authority

Do not copy one vendor's model-specific rule into every model or runtime.

## OpenAI

### GPT-5.6 model guidance

Source: https://developers.openai.com/api/docs/guides/latest-model

Durable takeaways:

- Favor leaner prompts.
- State each instruction once.
- Remove repeated instructions and unnecessary examples.
- Keep examples and style rules only when they encode requirements or fix measured gaps.
- Newer models can infer intent better, so prompts often do not need to prescribe every step.
- Continue to provide hard constraints, approval boundaries, relevant context, success criteria, and required evidence.
- Validate prompt changes on representative tasks.

The guide reports directional internal coding-agent results where leaner system prompts improved eval scores while reducing tokens and cost. Treat the numbers as workload-specific, not a universal guarantee.

### OpenAI image prompting guidance

Source: https://openai.com/academy/image-generation/

Durable takeaways:

- A good image prompt often needs only 1 to 3 clear sentences.
- Describe purpose, subject, action, setting, and desired visual treatment.
- Add framing, lighting, or constraints only when they matter.
- Use direct preservation constraints for edits.
- Iterate from observed mismatch rather than adding random adjectives.

## Anthropic

### Prompt engineering overview

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview

Durable takeaways:

- Define success criteria and empirical tests before prompt optimization.
- Not every failure should be fixed with prompting; model, tooling, or architecture changes may be better.
- Prompting techniques are starting points that must be tested.

### Prompting best practices

Source: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices

Durable takeaways:

- Be clear and direct.
- Add relevant context and examples where they help.
- Separate complex prompt sections with consistent structure.
- A role can be a single sentence.
- Tell the model what to do rather than building long negative lists.
- Newer models can overreact to aggressive tool-triggering language, so old CRITICAL/MUST wording may need to be reduced.
- Model-specific behavior, including frontend defaults, changes over time.

### Claude Code best practices

Source: https://code.claude.com/docs/en/best-practices

Durable takeaways:

- Give the agent an executable verification signal.
- Explore first, then plan, then code when complexity earns planning.
- Let the agent fetch project context rather than asking the prompt writer to guess it.
- Keep CLAUDE.md concise and include only facts the model cannot reliably infer from the code.
- Bloated persistent instructions can hide the current task and degrade behavior.
- Use hooks or permissions for deterministic controls.

### Anthropic interactive prompt engineering tutorial and courses

Sources:

- https://github.com/anthropics/prompt-eng-interactive-tutorial
- https://github.com/anthropics/courses

Durable takeaways:

- Practice on examples and failure cases.
- Separate data from instructions.
- Build complex prompts incrementally.
- Treat evaluation as a core skill, not an optional final step.

## Google

### Gemini prompt design strategies

Source: https://ai.google.dev/gemini-api/docs/prompting-strategies

Durable takeaways:

- Prompt design is iterative.
- Use clear goals, relevant context, constraints, examples, and output format as needed.
- Break complex workflows into components rather than forcing one giant prompt.
- Use model-specific guidance and parameters.
- Prompt order and long-context structure can affect results.

### Gemini image generation prompting

Source: https://ai.google.dev/gemini-api/docs/image-generation

Durable takeaways:

- Describe a coherent scene rather than a disconnected keyword list.
- Use explicit preservation language for edits.
- Label the role of multiple references.
- Keep tool configuration separate from visual intent where possible.

## Courses and practitioner education

### DeepLearning.AI and OpenAI course

Source: https://learn.deeplearning.ai/courses/chatgpt-prompt-eng/information

Durable takeaways:

- Write clear and specific instructions.
- Develop prompts iteratively through examples and observed failures.
- Use prompts as part of an application workflow, not as isolated prose.

### DAIR.AI and Learn Prompting

Use these as broad technique catalogs and teaching resources. Verify model-specific recommendations against current vendor docs and evals before turning them into rules.

## Primary research

### The Prompt Report

Source: https://arxiv.org/abs/2406.06608

Durable takeaways:

- Prompt engineering contains many distinct techniques across text and other modalities.
- Terminology and evidence are fragmented.
- Technique selection should follow task and evaluation, not ritual.

### Automatic prompt optimization survey

Source: https://arxiv.org/abs/2502.16923

Durable takeaways:

- Prompt optimization is an empirical search problem.
- Automated optimization still requires a clear objective, cases, and metrics; add human review when stakes or evaluation design require it.

## Interpretation used by this skill

The sources do not support one universally ideal prompt template. They support:

- minimum effective prompting
- task and model-specific routing
- evidence-calibrated specificity
- clear separation of instruction layers
- empirical evals and ablation
- deterministic enforcement outside prompts when available
- direct visual prompting without unnecessary keyword or style bloat
