---
name: prompt-engineering
description: "create, improve, audit, and rewrite minimum-effective system and developer prompts, context-calibrated coding-agent prompts, general task prompts, image and video prompts, agent instructions, eval cases, reusable templates, and strict code review prompts. use when users ask for prompt engineering, system prompt design or audit, coding prompts, prompt preflight, prompt documentation, prompt audits, subagent plans, cr or code review prompts, image prompts, review rubrics, prompt evals or ablation, measurable prompt-quality improvements, or prompts that should embed ponytail minimalism and caveman brevity."
---

# Prompt Engineering

Create prompts and internal task briefs that produce useful, verified results. A good prompt is a lean work contract: clear goal, relevant context, enforceable constraints, explicit output format, and a way to check success.

## Mandatory routing and evidence gate

Before writing, load `references/prompt-type-router.md` and classify the target instruction layer. Do not use one mega-template for every prompt.

Classify available evidence:

- C0: rough request only; no relevant source, repository, product, or runtime inspected.
- C1: partial user-provided evidence; some facts are known, but the target environment is not verified.
- C2: relevant source, repository, product, or runtime directly inspected.

Specificity must not exceed evidence:

- C0 -> state outcome, supplied constraints, discovery path, and done criteria. Do not invent implementation facts.
- C1 -> use exact supplied facts, label hypotheses, and require verification.
- C2 -> use verified names, paths, commands, APIs, schemas, and patterns when they materially help.

A prompt template is a menu. Omit sections and placeholders that do not earn their place. Never fill an empty slot with plausible detail.

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
- Prompt request -> output the finished prompt; include Ponytail + Caveman when the target task is technical/agentic, except system/developer prompts use the minimum-effective workflow.

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
9. For coding task prompts: embed Ponytail + Caveman contract -> specs -> repo evidence -> plan -> small changes -> diff review -> live verification -> final report. Do not mechanically paste the full block into a durable system prompt.
10. For coding work, optimize for the smallest semantically complete change, not the smallest textual diff or fewest lines.
11. For CR/code review work: issue intent -> diff/context evidence -> risk review -> verification review -> verdict. No "LGTM" without proof.
12. Missing information is not permission to invent. Mark unknowns, tell the target agent where to inspect, and let repo/source evidence drive implementation.
13. For coding prompts, consider subagents when the task is large, parallelizable, risky, or review-heavy. Keep one primary owner and avoid fake parallelism for tiny changes.
14. Start important prompt work from the platform default or no-custom-prompt baseline.
15. Use the minimum effective prompt. Add a rule only for a real requirement, authorization boundary, material risk, or measured recurring failure.
16. Prompt specificity must never exceed source specificity. Unsupported detail is not helpful context.
17. System and developer prompts contain durable cross-task behavior. Current task facts belong in the user prompt or inspected project context.
18. A blank, shorter, or less prescriptive prompt is a valid result when it performs better in representative evals.

For coding, repo, migration, refactor, bugfix, feature, UI, security, production-quality, or /goal tasks, load `references/karpathy-agentic-engineering.md` and `references/coding-agent-prompts.md`.

For CR, code review, PR review, "is this fix good", "review this diff", "approve or reject", or hostile reviewer requests, load `references/review-rubric.md`.

## System and developer prompts

For system prompts, developer prompts, assistant policies, global agent instructions, or agent constitutions, load `references/system-prompt-architecture.md` and `references/system-prompt-evals.md`.

Required workflow:

1. Map model, runtime, tools, instruction hierarchy, and deterministic controls.
2. Separate durable behavior from current-task facts.
3. Run or design the same representative cases for baseline, minimal, and candidate variants.
4. Write the minimum effective prompt.
5. Remove or move rules that duplicate tools, schemas, permissions, hooks, validators, project files, or user-task context.
6. Ablate instruction groups and keep only rules that improve required behavior or enforce a real boundary.

Do not encode generic frontend taste into a global coding system prompt. No fixed cards, gradients, palette, font, animation library, spacing scale, or layout doctrine unless it comes from product requirements, brand evidence, repository patterns, supplied visual references, accessibility needs, or measured eval failures. Prefer outcome-level guidance and let the agent inspect the actual product.

## Coding context calibration

Before generating any coding-agent prompt, load `references/coding-context-calibration.md` and assign C0, C1, or C2. Then load `references/coding-agent-prompts.md` for the existing engineering guardrails.

- C0 -> do not name files, functions, frameworks, packages, commands, tests, environment variables, architecture, routes, or UI details unless the user explicitly supplied them. Tell the target agent what to inspect and what outcome to verify.
- C1 -> preserve exact supplied facts, mark unverified implementation theories as hypotheses, and direct the target agent to confirm them.
- C2 -> use verified project details with traceable evidence.

At every level, retain the root-cause, smallest-safe-change, existing-pattern, verification, testing, diff-review, and done-definition rules. The calibration gate changes unsupported task detail, not engineering rigor.

## General and visual prompts

- General non-coding task -> load `references/general-task-prompts.md`.
- Image, image edit, diagram, poster, or video -> load `references/image-video-prompts.md`.
- Use `references/universal-prompt-framework.md` only when no narrower pattern fits.

For visual prompts, start with a direct scene or edit request. Add composition, lighting, text, preservation, negative constraints, and tool parameters only when they materially control the result. Do not inject Ponytail + Caveman into image or video prompt text.

## Ponytail + Caveman prompt contract

For generated task prompts that target coding agents, repo work, technical research, automation design, workflow implementation, prompt audits, or production-quality execution, include this contract near the top of the generated prompt, directly after `# Goal`:

```text
@ponytail / Use Ponytail full: simplest safe solution that works. Make the smallest semantically complete change that fixes the root cause, preserves required behavior, avoids unrelated change, and is supported by verification proportionate to risk. Optimize semantic scope, not line count or textual diff size. Stdlib/native/existing deps first. No speculative abstractions. Delete before adding. No new dependency unless it clearly earns weight. Do not trade away correctness, clarity, validation, explicit errors, typing, or necessary tests to make the patch smaller. For current APIs, packages, functions, security, or version-specific behavior: inspect repo first, then verify official/current docs before coding. Stop researching once path is clear.
@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact technical names. Save tokens. Do not remove required reasoning, validation, evidence, or safety checks.
```

Do not add this block to prompts where it would corrupt the required output or audience: exact JSON-only prompts, legal/medical/customer-facing copy, image/video prompt text, or creative writing. Do not mechanically paste it into a system or developer prompt: use the minimum-effective system workflow and retain only durable, validated semantics in shorter wording. If the user explicitly asks to force it anyway, include it as an instruction section outside the final artifact/output schema.

For CR/code review prompts, use `references/review-rubric.md`. Keep them review-only unless the user explicitly requests edits.

Load `references/token-efficient-caveman-style.md` for the Caveman side. Use the Ponytail rules above as the compact source of truth unless the dedicated Ponytail skill is active.

For the reusable wording and self-check, load `references/ponytail-caveman-contract.md`.

## Evidence-first prompt creation

When creating any prompt, use maximum available reasoning internally before writing. Do not expose chain-of-thought. Output the finished prompt or concise rationale only.

For incomplete context:

- Separate known facts from unknowns.
- Do not invent project structure, file names, functions, framework choices, APIs, packages, commands, tests, env vars, or implementation details.
- If the target agent will have repo, terminal, browser, docs, or connector access, instruct that agent to inspect those sources first and then decide the implementation.
- For coding requests like "modify this function" without repo context, write a lean prompt that states the desired behavior and tells the agent to find the function, callers, tests, contracts, and existing patterns before editing.
- Prefer "inspect, verify, then implement the smallest semantically complete safe change" over guessed step-by-step implementation details.
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

For generated technical task or agent-execution prompts, use Ponytail + Caveman together by default. Ponytail controls scope and implementation weight. Caveman controls prompt brevity. Do not separate them unless the user asks, the prompt type would be damaged by terse style, or the target is a system/developer prompt being minimized and evaluated.

When relevant to a task-execution prompt, add the full Ponytail + Caveman contract near the top, not only the Caveman line.

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

Load `references/prompt-type-router.md`, then classify before writing or answering:

- System/developer/global behavior prompt -> minimum-effective system architecture + baseline/minimal/candidate eval.
- Any normal user task in autoprompt mode -> internal task brief first.
- Coding agent / repo task -> coding-agent contract.
- `/goal` -> agentic coding prompt.
- CR / code review / is this fix good -> strict code review mode. Load `references/review-rubric.md`.
- Repo rules -> AGENTS.md / CLAUDE.md / Cursor Rules / Copilot / Windsurf / Aider.
- Research -> source plan, recency, citations, contradiction handling.
- Writing -> audience, tone, examples, constraints, revision criteria.
- Extraction/classification -> schema, labels, edge cases, null handling, examples.
- Image/video -> direct visual intent, supplied references, material composition/preservation constraints, and tool parameters kept separate where supported.
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

Use for Codex, Claude Code, Cursor, Copilot agent, Windsurf, Aider, ChatGPT agent, MCP/browser agents, and repo implementation. First apply the C0/C1/C2 gate from `references/coding-context-calibration.md`. Treat this structure as a menu, not mandatory ceremony. For small coding prompts, keep only the sections that reduce guessing or risk. Expand only for broad, risky, production, migration, security, data, deployment, or UI verification work:

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

- Classify prompt-writer evidence as C0, C1, or C2 before adding project-specific detail.
- Do not populate optional template fields with guesses. At C0, state desired behavior and discovery targets instead of implementation instructions.
- Include the Ponytail + Caveman contract directly after `# Goal` in coding-agent prompts.
- Ask the target agent to use the highest available reasoning effort for planning, repo evidence, implementation choices, and verification, but do it in one compact instruction.
- Detect stack from repo evidence.
- Use existing tooling.
- Make small scoped changes.
- Start with the narrowest viable scope. Expand only when a narrower fix would preserve the root cause, violate an invariant or contract, duplicate logic, or create a temporary workaround; state the reason before expanding.
- Preserve behavior unless changing it is explicit.
- Use verification proportionate to change risk. When externally observable behavior changes and a suitable test layer exists, add or update the smallest focused regression test. Do not force persistent tests for generated, configuration-only, documentation-only, or mechanically verified changes.
- Review diff before final.
- Stop editing when the requested behavior works, relevant checks pass, the diff contains no unrelated changes, and no known correctness issue remains within scope.
- Do not hallucinate APIs, flags, packages, commands, files, tests, or framework behavior.
- When project context is missing, prompt the target agent to inspect the repo and sources instead of guessing.
- Add scoped subagent instructions when they help repo mapping, docs verification, QA, UI checks, security review, or diff review.
- For broad, risky, security-sensitive, migration, data, RAG/vector/cache, or cross-project porting tasks, mention an independent verification lane when feasible: separate terminal/context, baseline end-to-end or integration evals before changes, same evals after changes, compare before/after, and do not rely only on the implementer's self-review. Do not hardcode this for every small coding task.
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

1. Define success criteria and representative cases.
2. Run the platform default or no-custom-prompt baseline.
3. Run a minimum-effective variant.
4. Run the proposed candidate on the same cases.
5. Compare task success, false constraints, unsupported specificity, token cost, and domain-specific quality.
6. Find the failure pattern and patch minimally.
7. Ablate instruction groups and retest.

No perfect prompt. A shorter prompt may win. Iterate like engineering.

Load `references/evals-and-iteration.md`; for system prompts also load `references/system-prompt-evals.md`.

## Optional deterministic helpers

Use scripts when they improve repeatability:

- `scripts/make_prompt_eval.py` -> create a JSON starter manifest for baseline, minimal, candidate, representative cases, metrics, and ablation.
- `scripts/test_prompt_tools.py` -> run regression tests for the eval helper after maintenance.

Run the helper on representative prompt variants before relying on its manifest.

## Final answer behavior

- Normal prompt request -> output only the finished prompt unless explanation is requested; include the Ponytail + Caveman block for technical/agentic task execution, but not automatically for system/developer prompts.
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
