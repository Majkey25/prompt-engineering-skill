# Prompt Quality Checklist

Run before returning any generated prompt or using autoprompt output.

## Must pass

- Goal is specific.
- Done state is testable.
- Context is relevant, not bloated.
- Source/user data is separated from instructions.
- Constraints are concrete and enforceable.
- Output format is explicit.
- Examples are used only when they improve consistency.
- Verification/evaluation exists when outcome matters.
- Failure and uncertainty behavior is defined for factual, risky, or incomplete tasks.
- Unsafe/destructive actions are controlled.
- Unsupported assumptions are not presented as facts.
- Missing project/source facts are marked as unknown and assigned to repo/source inspection, not invented.
- Token-efficient style is used only when useful, not blindly.

## Coding-agent must pass

- Karpathy-style production stance included unless prototype.
- Stack/tooling must be discovered from repo evidence.
- If code context is missing, prompt tells the agent what to inspect instead of guessing implementation details.
- Subagents are considered for large/risky/parallelizable work and omitted for tiny scoped changes.
- Plan before code required for risky work.
- Small scoped changes required.
- Diff review required.
- Live verification default.
- UI tasks include Playwright/browser checks when available.
- Pytest is not default.
- Agent must not delegate testable checks to user.
- Done definition is explicit.
- Final response request is concise plain text unless a rigid structure is actually needed.

## Autoprompt must pass

- Did not show hidden working prompt unless asked.
- Used more specific skill/tool when available.
- Did not over-plan tiny task.
- Did not ask avoidable clarification.
- Did cite/search when current/high-stakes facts matter.

## Prompt debt check

Delete or rewrite a rule if:

- It is generic behavior steering with no measurable purpose.
- It was added for an old model and no longer helps.
- It conflicts with another rule.
- It repeats system/tool behavior.
- It makes every task longer without improving outputs.
- Nobody can explain how to test it.
- It solves one edge case but harms normal cases.

## Vague phrase conversion

Bad -> Better

- improve project -> identify scoped issue, fix it, verify exact workflow
- make better -> define target audience + success criteria
- use best practices -> follow repo/source-specific rules
- clean code -> clear names, no duplication in scope, explicit errors, no behavior drift
- optimize -> state metric: speed/cost/tokens/readability/reliability
- production ready -> run relevant checks, verify live path, handle errors, report blockers
- fix everything -> fix only in-scope blockers; report unrelated issues

## Final self-check

Ask:

1. Could another agent execute this without guessing?
2. Does done mean something testable?
3. Is context sufficient but not bloated?
4. Are source and uncertainty rules present when needed?
5. Are we hiding risk?
6. Is this prompt a contract or a wish?

## Complete merged skill checks

Before returning any final prompt from this expanded skill, verify:

- Original coding-agent structure still exists.
- `/goal` creates an agentic coding prompt.
- Live verification is default.
- Pytest is optional, not default.
- UI prompts include Playwright or Playwright Interactive when available.
- Migration prompts include inventory, mapping, behavior preservation, UI preservation, route/data-flow preservation, incremental checks, and final report.
- Autoprompt mode can silently convert normal user requests into better internal task briefs.
- Token-efficient style does not delete constraints.
- Karpathy-style agentic engineering is used for production coding work.
- RAG/wiki/VDB/cache prompts include raw data, retrieval, metadata, stale cache, citation, and benchmark checks.
- Important prompts include eval or benchmark cases.
