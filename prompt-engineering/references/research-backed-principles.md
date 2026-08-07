# Research Backed Principles

This file summarizes durable prompting rules from major official docs and practitioner sources. Use it as decision support, not as a citation database.

For selected current source URLs, review dates, and model-specific caveats, load `research-source-map.md`. Recheck time-sensitive model guidance before turning it into a durable rule.

## OpenAI prompt guidance

- Put instructions clearly near the start for normal API prompts.
- Separate instruction and context with delimiters.
- Be specific about outcome, length, format, style, and audience.
- Show the desired output format with examples.
- Start zero-shot, add few-shot examples when needed, consider fine-tuning only when prompting is not enough.
- For newer capable models, start lean and state each instruction once. Do not prescribe every intermediate step when the model can infer intent and use tools.
- Compare important prompts against a platform-default or no-custom-prompt baseline. OpenAI reports workload-specific internal coding-agent gains from removing repeated instructions, unnecessary examples, and bloated tool descriptions; treat those numbers as directional, not universal.
- Keep hard requirements, relevant context, approval boundaries, and success criteria even when shortening.

## OpenAI image prompting guidance

- A useful image prompt can often be 1 to 3 clear sentences.
- State purpose, subject, action, setting, and the visual treatment that materially matters.
- Add framing, lighting, exact text, or preservation rules only when they control the result.
- For edits, state what changes and what must remain unchanged.
- Iterate from observed mismatch instead of adding random adjectives or giant negative lists.

## OpenAI Codex guidance

- Codex can inspect repo, edit files, run commands, and provide evidence from terminal/test output.
- Large changes benefit from planning before implementation.
- AGENTS.md is the durable repo instruction layer.
- The agent loop is model + tools + observations + user feedback, not just one prompt.

## OpenAI Skills guidance

- Skill description controls discovery.
- Full SKILL.md loads only after trigger.
- References/resources should be read only when needed.
- Keep SKILL.md as control plane; move deep detail to references.

## Anthropic prompt guidance

- Define success criteria before prompt engineering.
- Build empirical tests/evals where possible.
- Use clear/direct instructions.
- Use examples for consistency.
- Use XML tags/delimiters to separate content.
- Chain complex prompts instead of one giant prompt.
- For long context, put long docs high and query/instructions late; ask for quotes first.
- A role can be one sentence. Decorative expertise language is not a substitute for clear scope.
- Newer models can overtrigger on repeated CRITICAL, MUST, NEVER, and aggressive tool-use language. Use priority words only where they encode real hierarchy or risk.
- Not every failure is best solved with more prompt text. Consider model choice, tool design, schemas, permissions, hooks, retrieval, or application logic.

## Claude Code guidance

- Give the agent a way to verify work: tests, screenshots, expected outputs.
- Explore first, plan, then code.
- Use CLAUDE.md for project memory, but keep it useful and short.
- Manage context aggressively because performance degrades as context fills.
- Let the coding agent fetch repository facts it can inspect more reliably than the upstream prompt writer.
- Keep CLAUDE.md limited to durable facts and commands that the model cannot reliably infer from the project. Bloated persistent instructions can hide the current task.
- Use hooks, permissions, schemas, and other deterministic controls for requirements that must not be advisory.
- Course-correct early.

## Google Vertex guidance

- Prompt design is iterative.
- Prompts can include instructions, context, examples, and partial input.
- Rigorous testing/evaluation matters.
- Try order changes when quality is inconsistent.

## Microsoft/Azure style guidance

- Use clear task framing.
- Use separators, markdown, XML-like tags, schemas, and examples when structure matters.
- Specify output format and constraints.

## DAIR / Learn Prompting / pattern catalog guidance

- Patterns are tools, not magic.
- Use zero-shot for simple tasks.
- Use few-shot for format/style consistency.
- Use ReAct/tool loops for agentic tasks.
- Use RAG/source grounding for factual tasks.
- Use rubrics/evals for quality-sensitive tasks.

## Cursor guidance

- Plan first for larger work.
- Use relevant files/context, not everything.
- Rules are persistent context and should be focused, actionable, scoped, and split when large.
- Use project rules when repeating prompts.

## GitHub Copilot guidance

- Custom instructions add reusable repo/team context.
- Repository-wide, path-specific, and agent instructions have precedence rules.
- Keep instructions short and self-contained.
- Avoid conflicts between instruction layers.

## HumanLayer 12-factor guidance

- Own your prompts.
- Own your context window.
- Treat tools as structured outputs.
- Compact errors into context.
- Prefer small focused agents over giant agents.
- Trigger agents from anywhere, but keep control flow explicit.

## Karpathy/vibe coding guidance

- Natural language is now a programming interface.
- Vibe coding is useful for flow/prototypes.
- Production needs human ownership, architecture taste, security review, diff review, tests/checks, and verification.
- AI code may be bloaty, repetitive, or poorly abstracted. Prompt must force review.

## Interpretation rule

The sources do not establish one universally best prompt structure. Use them to choose the minimum effective prompt for the target model, runtime, evidence level, and task. Preserve model capability unless a true requirement or measured failure justifies narrowing it.
