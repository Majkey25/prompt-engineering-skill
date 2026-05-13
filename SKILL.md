---
name: prompt-engineering
description: "create, improve, audit, or rewrite prompts, agent goals, /goal prompts, system prompts, internal self-prompts, task briefs, reusable instructions, and repo rules. use for any task when the user wants requests routed through prompt engineering first, asks to use prompt-engineering as a preflight, or wants better answers by first turning their request into an internal working prompt. use for make/write/improve/audit prompt, prompt codex/claude/chatgpt agent, ai-agent task, agents.md/claude.md/cursor rules/copilot/windsurf/aider, migration/refactor/bugfix/feature/ui/playwright/live verification, research, writing, analysis, extraction, image/video, business, study, and coding prompts. follow source-backed prompt engineering, karpathy-style agentic engineering, lean context, caveman token efficiency, eval loops, live verification, and strict self-review."
---

# Prompt Engineering

Create prompts and internal task briefs that produce useful, verified results. Optimize behavior, not pretty wording.

## Autoprompt mode

When the user wants this skill used as a preflight for all tasks, treat every request as two layers:

1. Internal working prompt -> clarify task, constraints, success criteria, process, verification, output shape.
2. Actual answer or execution -> use that prompt silently unless the user asks to see it.

Do not dump the internal prompt by default. Use it to improve the answer.

If a more specific skill/tool fits the task, do not replace it. Use this skill to sharpen the task brief, then let the specific skill/tool do the work.

Use levels:

- Micro task -> make a compact internal prompt in your head, answer directly.
- Medium task -> use a visible short plan when useful, then execute.
- Large/risky task -> create a structured working prompt, plan first, then execute.
- Coding/repo task -> use agentic engineering contract.
- Prompt request -> output the finished prompt.

Safety and system rules still win.

## Top doctrine

Default doctrine for agentic and coding work:

1. Vibe coding is for prototypes and exploration.
2. Production work needs specs -> repo evidence -> plan -> small changes -> diff review -> live verification -> final report.
3. Prompt = work contract, not a wish.
4. Human owns architecture, taste, security, and final judgment.
5. AI output is untrusted until checked.
6. Brevity must never remove requirements, validation, evidence, safety, or done definition.

For coding, repo, migration, refactor, bugfix, feature, UI, security, production-quality, or /goal tasks, load `references/karpathy-agentic-engineering.md` and `references/coding-agent-prompts.md`.

## Caveman token style

Every generated prompt must include this near the top:

```text
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

Also write the prompt itself in that style. Use compact sections, arrows, checklists, and schemas. Do not write broken caveman grammar when precision matters.

Load `references/token-efficient-caveman-style.md` when cost, context, brevity, or token use matters.

## Source-backed mode

If the user provides articles, docs, links, or research targets:

1. Read or search the actual sources when possible.
2. Extract durable rules, not just user paraphrases.
3. Prefer primary docs over blogs.
4. Treat vendor docs as useful but biased.
5. Treat blog/community rules as field practice, not law.
6. Resolve conflicts.
7. Implement rules into the right reference file.

Load `references/source-driven-prompt-audit.md` and `references/research-backed-principles.md`.

## Choose prompt type first

Classify before writing or answering:

- Any normal user task in autoprompt mode -> internal task brief first.
- Coding agent / repo task -> coding-agent contract.
- `/goal` -> agentic coding prompt.
- Repo rules -> AGENTS.md / CLAUDE.md / Cursor Rules / Copilot / Windsurf / Aider.
- Research -> source plan, recency, citations, contradiction handling.
- Writing -> audience, tone, examples, constraints, revision criteria.
- Extraction/classification -> schema, labels, edge cases, null handling, examples.
- Image/video -> subject, composition, style, constraints, negative constraints, output specs.
- Analysis/decision -> criteria, options, tradeoffs, assumptions, evidence, recommendation.
- General prompt improvement -> universal framework + anti-vague rewrite.

## Universal skeleton

Use when no narrower template fits:

1. Role
2. Task
3. Context
4. Success criteria
5. Constraints
6. Process
7. Verification/evaluation
8. Output format
9. What not to do

Load `references/universal-prompt-framework.md`.

## Coding-agent structure

Use for Codex, Claude Code, Cursor, Copilot agent, Windsurf, Aider, ChatGPT agent, MCP/browser agents, and repo implementation:

1. Goal
2. Mode
3. Context
4. Non negotiable requirements
5. Repository analysis
6. Plan before code
7. Implementation rules
8. Live verification
9. UI verification, if relevant
10. Testing rules
11. Strict diff/self review
12. Done definition
13. Final response format

Hard defaults:

- Detect stack from repo evidence.
- Use existing tooling.
- Make small scoped changes.
- Preserve behavior unless changing it is explicit.
- Review diff before final.
- Do not hallucinate APIs, flags, packages, or framework behavior.
- Do not broad rewrite without reason.
- Live verify when possible.
- Do not ask user to test what agent can test.
- Pytest is not default. Use only if repo already uses it, user asks, or pytest infra clearly exists.
- Continue while a safe next step can increase confidence.

## Context management

Use lean context:

- Stable instructions first.
- Variable user input last.
- Long docs above the query when long-context behavior matters.
- Quote relevant source passages before answering long-doc questions.
- Keep rules scoped and actionable.
- Use skills/rules/files instead of giant chat prompts.
- Start fresh after logical task completion or repeated failure.

Load `references/context-management.md`.

## Pattern library

Choose patterns deliberately:

- Zero-shot -> simple tasks.
- Few-shot -> style/schema/edge-case consistency.
- Structured output -> extraction, classification, APIs.
- XML/Markdown delimiters -> separate instructions/context/examples.
- Chain prompts -> complex workflows.
- ReAct/tool loop -> agent tasks with observations/actions.
- RAG/source grounding -> factual answers from documents.
- Rubric/evals -> important prompts.

Load `references/prompt-pattern-library.md` and `references/domain-prompt-patterns.md`.

## Evals and iteration

For important prompts:

1. Define success criteria.
2. Create 3 to 5 representative cases.
3. Run prompt.
4. Compare output to criteria.
5. Find failure pattern.
6. Patch minimally.
7. Retest.

No perfect prompt. Iterate like engineering.

Load `references/evals-and-iteration.md`.

## Final answer behavior

- Normal prompt request -> output only finished prompt unless explanation requested.
- Prompt improvement -> improved prompt + short fix list.
- Autoprompt normal task -> answer the task; do not show internal prompt unless asked.
- Skill maintenance -> changed files + validation + packaged zip link + update instructions.

## Ultimate caveman and verification extensions

For high-value prompts, coding prompts, repo work, RAG/wiki prompts, benchmark prompts, cache prompts, or production prompts, also load `references/ultimate-caveman-extensions.md` and `references/rag-wiki-benchmark-prompts.md`.

Use these extra rules when relevant:

- Prefer compact but complete prompts: fewer words, more structure, no lost requirements.
- Use hostile review only for code, architecture, prompts, specs, migrations, security, performance, and other quality-sensitive work.
- For coding-agent prompts, require diff review and evidence. If two agents are involved, one agent implements and another reviews. Example: Codex implements -> Claude reviews, or Claude implements -> Codex reviews.
- For RAG/wiki/vector database/cache prompts, require source inventory, raw data checks, retrieval checks, chunking/metadata checks, stale cache checks, and benchmark questions.
- For benchmark prompts, define dataset, baseline, success metric, allowed tools, failure categories, and final evidence table.
- For live validation, prefer real workflow checks over symbolic quality words.
- For unclear tasks, convert vague wishes into scoped work contracts before answering.
