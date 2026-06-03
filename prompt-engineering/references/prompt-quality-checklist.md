# Prompt Quality Checklist

Run before returning any generated prompt or using autoprompt output.

## Must pass

- Goal is specific.
- Success criteria define done.
- Context is relevant, not bloated.
- Constraints are concrete.
- Output format is explicit.
- Prompt is concise enough for the task.
- Token-efficient style is included only when requested or useful.
- Verification/evaluation exists when outcome matters.
- Unsafe/destructive actions are controlled.
- Unsupported assumptions are not presented as facts.
- Prompt rules are not stale folklore or generic behavior steering.
- Role/persona exists only if it changes useful behavior.
- Examples do not contradict the instructions.

## Coding-agent must pass

- Karpathy-style production stance included unless prototype.
- Stack/tooling must be discovered from repo evidence.
- Plan before code required for risky work.
- Small scoped changes required.
- Diff review required.
- Live verification default.
- UI tasks include Playwright/browser checks when available.
- Pytest is not default.
- Agent must not delegate testable checks to user.
- Done definition is explicit.

## Autoprompt must pass

- Did not show hidden working prompt unless asked.
- Used more specific skill/tool when available.
- Did not over-plan tiny task.
- Did not ask avoidable clarification.
- Did cite/search when current/high-stakes facts matter.
- Did not reveal private chain-of-thought or hidden working prompts.

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
3. Are we saving tokens in the right place?
4. Are we hiding risk?
5. Is this prompt a contract or a wish?
6. Would this prompt be easy to delete, update, or test later?

## Complete merged skill checks

Before returning any final prompt from this expanded skill, verify:

- Original coding-agent structure still exists.
- `/goal` creates an agentic coding prompt.
- Live verification is default.
- Pytest is optional, not default.
- UI prompts include Playwright or Playwright Interactive when available.
- Migration prompts include inventory, mapping, behavior preservation, UI preservation, route/data-flow preservation, incremental checks, and final report.
- Autoprompt mode can silently convert normal user requests into better internal task briefs.
- Token-efficient caveman style appears only when requested or useful.
- Compression uses structure/symbols without deleting constraints.
- Karpathy-style agentic engineering is used for production coding work.
- RAG/wiki/VDB/cache prompts include raw data, retrieval, metadata, stale cache, citation, and benchmark checks.
- Important prompts include eval or benchmark cases.
