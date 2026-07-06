---
name: prompt-engineering
description: "create, improve, audit, and rewrite source-backed prompts, agent instructions, task briefs, eval cases, reusable templates, and strict code review prompts. use when users ask for stronger prompts, prompt preflight, prompt documentation, prompt audits, coding-agent prompts, subagent plans, cr/code review prompts, review rubrics, measurable prompt-quality improvements, or prompts that should embed ponytail minimalism and caveman brevity."
---

# Prompt Engineering

Create prompts and internal task briefs that produce useful, verified results. A good prompt is a lean work contract: clear goal, relevant context, enforceable constraints, explicit output format, and a way to check success.

## Autoprompt mode

When the user wants this skill used as a preflight for all tasks, treat every request as two layers:

1. Internal working prompt -> clarify task, constraints, success criteria, process, verification, output shape.
2. Actual answer or execution -> use that prompt silently unless the user asks to see it.

Do not dump the internal prompt by default. Use it to improve the answer.

If a more specific skill/tool fits the task, do not replace it. Use this skill to sharpen the task brief, then let the specific skill/tool do the work.

Use levels:

- Micro task -> make a compact internal prompt in your head, answer directly.
- Medium task -> use a visible short plan when useful, then execute.
- Large/risky task -> create a scoped working prompt, plan first, then execute.
- Coding/repo task -> use agentic engineering contract with Ponytail + Caveman embedded in the generated prompt.
- Prompt request -> output the finished prompt; include Ponytail + Caveman when the target task is technical/agentic.

Safety and system rules still win.

## Top doctrine

Default doctrine:

1. Prompt = work contract, not a wish.
2. Prompt = technical debt. Every rule must earn its place. Delete stale, vague, or model-folklore rules.
3. Start from success criteria and representative cases before optimizing important prompts.
4. Prefer clear structure, concrete constraints, examples where useful, and explicit output format.
5. Keep context relevant and separated from instructions with Markdown, XML tags, or other delimiters.
6. Model-specific guidance matters. Do not blindly apply old rules like "think step by step" to reasoning models.
7. AI output is untrusted until checked against sources, schema, eval cases, or live behavior.
8. Brevity must never remove requirements, validation, evidence, safety, or done definition.
9. For coding work: embed Ponytail + Caveman contract -> specs -> repo evidence -> plan -> small changes -> diff review -> live verification -> final report.
10. For CR/code review work: issue intent -> diff/context evidence -> risk review -> verification review -> verdict. No "LGTM" without proof.
11. Missing information is not permission to invent. Mark unknowns, tell the target agent where to inspect, and let repo/source evidence drive implementation.
12. For coding prompts, consider subagents when the task is large, parallelizable, risky, or review-heavy. Keep one primary owner and avoid fake parallelism for tiny changes.

For coding, repo, migration, refactor, bugfix, feature, UI, security, production-quality, or /goal tasks, load `references/karpathy-agentic-engineering.md` and `references/coding-agent-prompts.md`.

For CR, code review, PR review, "is this fix good", "review this diff", "approve or reject", or hostile reviewer requests, load `references/review-rubric.md`.

## Ponytail + Caveman prompt contract

For generated prompts that target coding agents, repo work, CR/code review, technical research, automation design, workflow implementation, prompt audits, or production-quality execution, include this contract near the top of the generated prompt, directly after `# Goal`:

```text
@ponytail / Use Ponytail full: simplest safe solution that works. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

Do not add this block to prompts where it would corrupt the required output or audience: exact JSON-only prompts, legal/medical/customer-facing copy, image/video prompt text, or creative writing. If the user explicitly asks to force it anyway, include it as an instruction section outside the final artifact/output schema.

Load `references/token-efficient-caveman-style.md` for the Caveman side. Use the Ponytail rules above as the compact source of truth unless the dedicated Ponytail skill is active.

For the reusable wording and self-check, load `references/ponytail-caveman-contract.md`.

## Evidence-first prompt creation

When creating any prompt, use maximum available reasoning internally before writing. Do not expose chain-of-thought. Output the finished prompt or concise rationale only.

For incomplete context:

- Separate known facts from unknowns.
- Do not invent project structure, file names, functions, framework choices, APIs, packages, commands, tests, env vars, or implementation details.
- If the target agent will have repo, terminal, browser, docs, or connector access, instruct that agent to inspect those sources first and then decide the implementation.
- For coding requests like "modify this function" without repo context, write a lean prompt that states the desired behavior and tells the agent to find the function, callers, tests, contracts, and existing patterns before editing.
- Prefer "inspect, verify, then implement the smallest safe change" over guessed step-by-step implementation details.
- For current libraries, APIs, models, CLIs, or security-sensitive behavior, require official/current docs after repo inspection.
- Keep prompts plain and compact. Add only rules that materially reduce guessing, risk, or rework.

## Subagent guidance for coding prompts

For Codex, Claude Code, Cursor, Fable-style agents, MCP agents, or other agentic coding systems, decide whether subagents help before adding them.

Use subagents when they create real leverage:

- Repo mapper -> find relevant files, data flow, entrypoints, tests, and conventions.
- Docs verifier -> check current official docs for APIs, packages, models, CLIs, or framework behavior.
- QA/test agent -> run existing checks, reproduce bugs, inspect logs, and verify workflows.
- UI/browser agent -> use screenshots, browser checks, console/network inspection, and responsive checks.
- Security/review agent -> inspect auth, secrets, data safety, permissions, and risky diffs.
- Diff reviewer -> independently review the final patch for bloat, regressions, fake APIs, and missed edge cases.

Rules:

- Do not add subagents for tiny tasks where one agent can safely inspect, edit, and verify.
- Keep one primary implementation owner.
- Give each subagent a narrow evidence-gathering or review job.
- Tell the primary agent to synthesize subagent findings, reject unsupported claims, and implement only after evidence is clear.
- Do not let subagents create contradictory plans without a final owner deciding.


## Token-efficient style

For generated technical or agent prompts, use Ponytail + Caveman together by default. Ponytail controls scope and implementation weight. Caveman controls prompt brevity. Do not separate them unless the user asks or the prompt type would be damaged by terse style.

When relevant, add the full Ponytail + Caveman contract near the top, not only the Caveman line.

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
- CR / code review / is this fix good -> strict code review mode. Load `references/review-rubric.md`.
- Repo rules -> AGENTS.md / CLAUDE.md / Cursor Rules / Copilot / Windsurf / Aider.
- Research -> source plan, recency, citations, contradiction handling.
- Writing -> audience, tone, examples, constraints, revision criteria.
- Extraction/classification -> schema, labels, edge cases, null handling, examples.
- Image/video -> subject, composition, style, constraints, negative constraints, output specs.
- Analysis/decision -> criteria, options, tradeoffs, assumptions, evidence, recommendation.
- General prompt improvement -> universal framework + anti-vague rewrite.

## Universal skeleton

Use when no narrower template fits:

1. Objective
2. Target user / audience
3. Relevant context and source data
4. Task and exact deliverable
5. Constraints and non-goals
6. Output format or schema
7. Examples, only if they improve consistency
8. Process / tool-use guidance
9. Verification / eval criteria
10. Failure and uncertainty policy
11. Optional style and length controls

Load `references/best-prompt-blueprint.md` and `references/universal-prompt-framework.md`.

## Coding-agent structure

Use for Codex, Claude Code, Cursor, Copilot agent, Windsurf, Aider, ChatGPT agent, MCP/browser agents, and repo implementation. Treat this as a menu, not mandatory ceremony. For small coding prompts, keep only the sections that reduce guessing or risk. Expand only for broad, risky, production, migration, security, data, deployment, or UI verification work:

1. Goal
2. Ponytail + Caveman contract
3. Mode
4. Context
5. Non negotiable requirements
6. Repository analysis
7. Plan before code
8. Implementation rules
9. Live verification
10. UI verification, if relevant
11. Testing rules
12. Strict diff/self review
13. Done definition
14. Concise final response

Hard defaults:

- Include the Ponytail + Caveman contract directly after `# Goal` in coding-agent prompts.
- Ask the target agent to use the highest available reasoning effort for planning, repo evidence, implementation choices, and verification, but do it in one compact instruction.
- Detect stack from repo evidence.
- Use existing tooling.
- Make small scoped changes.
- Preserve behavior unless changing it is explicit.
- Review diff before final.
- Do not hallucinate APIs, flags, packages, commands, files, tests, or framework behavior.
- When project context is missing, prompt the target agent to inspect the repo and sources instead of guessing.
- Add scoped subagent instructions when they help repo mapping, docs verification, QA, UI checks, security review, or diff review.
- Do not add broad generic guardrails just because the task is technical.
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
- Prompt optimization -> only after test cases or real failures exist.

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

- Normal prompt request -> output only the finished prompt unless explanation is requested; include the Ponytail + Caveman block when the prompt is for technical/agentic execution.
- Prompt improvement -> improved prompt + short fix list.
- Autoprompt normal task -> answer the task; do not show internal prompt unless asked.
- Skill maintenance -> concise plain text: what changed, validation status, and real blockers or risks only. No rigid multi-section report unless the user asks for one.

## Strict review and verification extensions

For high-value prompts, coding prompts, repo work, CR/code review prompts, RAG/wiki prompts, benchmark prompts, cache prompts, or production prompts, load the relevant verification references:

- Token-efficient or hostile-review prompts -> `references/ultimate-caveman-extensions.md`
- CR/code review prompts -> `references/review-rubric.md`
- RAG/wiki/vector/cache/benchmark prompts -> `references/rag-wiki-benchmark-prompts.md`

Use these extra rules when relevant:

- Prefer compact but complete prompts: fewer words, enough structure, no lost requirements.
- Use hostile review only for code, architecture, prompts, specs, migrations, security, performance, code review, and other quality-sensitive work.
- In CR mode, be blunt, evidence-bound, and fair. Review like a senior maintainer who owns production risk. Separate blockers from nits. Prefer REQUEST CHANGES when root cause, tests, runtime proof, or scope control is weak.
- For coding-agent prompts, require diff review and evidence. If two agents are involved, one agent implements and another reviews. Example: Codex implements -> Claude reviews, or Claude implements -> Codex reviews.
- For RAG/wiki/vector database/cache prompts, require source inventory, raw data checks, retrieval checks, chunking/metadata checks, stale cache checks, and benchmark questions.
- For benchmark prompts, define dataset, baseline, success metric, allowed tools, failure categories, and final evidence table.
- For live validation, prefer real workflow checks over symbolic quality words.
- For unclear tasks, convert vague wishes into scoped work contracts before answering.
