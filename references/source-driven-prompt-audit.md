# Source Driven Prompt Audit

Use when user provides docs, articles, links, examples, or research requirements.

## Rule

Do not merely copy the user's summary. Inspect the sources when possible. Extract the real durable rules.

## Source priority

1. Primary product docs.
2. Official engineering blogs / GitHub repos.
3. Standards/specs/papers.
4. High-quality practitioner blogs.
5. Community guides.
6. News/secondary summaries.
7. User paraphrase.

Vendor docs are useful but biased. Treat marketing claims as claims, not laws.

## Extraction method

For each source, extract:

- concrete rule
- when it applies
- when not to apply it
- example pattern
- conflict with other sources
- where to implement in skill

## Conflict handling

Examples:

- OpenAI says instructions first for API prompts; Anthropic long-context says long documents near top and query later. Resolve by context: API task prompt -> instructions first; long-doc QA -> documents first, query later.
- Token-efficient style saves cost; too much compression can remove requirements. Resolve by keeping constraints/verification full, compressing wording/output.
- Vibe coding supports fast prototypes; production needs review and verification. Resolve by mode: prototype vs production.

## Implementation targets

- Triggering/description -> SKILL.md description.
- Core behavior -> SKILL.md body.
- Large detailed guidance -> references.
- Reusable checklists -> prompt-quality-checklist.md.
- Coding-specific guidance -> coding-agent-prompts.md.
- Repo rule files -> agent-instructions-files.md.
- Context/token rules -> context-management.md and token-efficient-caveman-style.md.
- Evals -> evals-and-iteration.md.

## Audit output

For skill maintenance final answers, report:

1. sources used
2. rules extracted
3. files changed
4. validation result
5. remaining uncertainty
