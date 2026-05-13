# Research Backed Principles

This file summarizes durable prompting rules from major official docs and practitioner sources. Use it as decision support, not as a citation database.

## OpenAI prompt guidance

- Put instructions clearly near the start for normal API prompts.
- Separate instruction and context with delimiters.
- Be specific about outcome, length, format, style, and audience.
- Show the desired output format with examples.
- Start zero-shot, add few-shot examples when needed, consider fine-tuning only when prompting is not enough.

## OpenAI Codex guidance

- Codex can inspect repo, edit files, run commands, and provide evidence from terminal/test output.
- Large changes benefit from Ask/Plan first, then Code/implementation.
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

## Claude Code guidance

- Give the agent a way to verify work: tests, screenshots, expected outputs.
- Explore first, plan, then code.
- Use CLAUDE.md for project memory, but keep it useful and short.
- Manage context aggressively because performance degrades as context fills.
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
