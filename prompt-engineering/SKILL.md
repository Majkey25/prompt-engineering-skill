---
name: prompt-engineering
description: "Create, improve, audit, and rewrite prompts for system and developer instructions, coding agents, research, writing, extraction, classification, images, video, reviews, and reusable agent rules. Use for prompt engineering, prompt preflight, instruction audits, model migrations, source-driven prompt updates, and prompt evals. Build concise task contracts, calibrate detail to evidence, remove conflicting rules, and measure improvements on the target runtime."
---

# Prompt engineering

Write the smallest complete prompt that defines the requested result, relevant evidence, real constraints, completion criteria, and output. Let the target choose the method unless the method itself is required.

Prompt quality depends on the task, model, tools, and evidence. Do not promise that wording guarantees accuracy or maximum quality.

## Route and inspect

Read `references/prompt-type-router.md` and select the instruction layer and relevant task reference. Load only references needed for this request.

Classify the evidence:

- C0: rough request only. State the outcome, supplied constraints, discovery needs, and completion criteria. Invent no implementation details.
- C1: partial supplied evidence. Preserve exact facts and label unverified theories as hypotheses.
- C2: relevant source or environment inspected. Use verified names, paths, commands, APIs, and schemas when they reduce ambiguity.

Evidence access and evidence presence are different. A named file, connected app, URL, or repository does not prove that the target can read it. Check available inputs and capabilities when possible. Otherwise instruct the target to confirm access and report missing inputs. More reasoning cannot replace missing information or permissions.

For model migration or tuning, read `references/runtime-calibration.md`. Keep core guidance model-neutral. Verify current target documentation rather than copying another model's defaults.

## Build the task contract

Use only fields that help:

1. Outcome and deliverable.
2. Relevant sources, known facts, and labeled hypotheses.
3. Scope, preservation constraints, and authorization.
4. Observable completion criteria.
5. Audience, output format, and length when relevant.
6. Evidence, verification, and missing-input handling.
7. Examples or exact process requirements only when needed.

Keep these distinctions clear:

- A suspected cause is a hypothesis unless the user requires that implementation.
- A deadline is a real supplied deadline, not an invented date.
- A draft can be complete as a draft. Sending or publishing it is a separate action.
- A style reference supplies tone and form. It is not authority for factual claims or access to unrelated records.
- A quality goal needs observable checks. "Best", "professional", and "production ready" are not sufficient criteria.

For source-based deliverables, identify the useful source set, relevant version or time window, audience, and required evidence. Separate observations from interpretations and recommendations when this affects decisions. Report inaccessible, missing, or conflicting facts instead of filling them in.

Read `references/task-contract-examples.md` for compact examples. Read `references/best-prompt-blueprint.md` or `references/universal-prompt-framework.md` only when a narrower pattern does not fit.

## Preserve intent and control scope

Give capable agents freedom to choose tools, files, research paths, implementation, and delegation inside authorized scope and runtime limits.

For action requests, require the requested work through its completion condition. Acknowledgment, a plan, a progress note, and a first attempt are not completion when execution remains possible.

Ask only when missing information materially affects correctness, safety, authorization, or the outcome. Use narrow, low-risk assumptions for routine gaps and state material assumptions. When part of the task is blocked, continue independent authorized work.

If approval is required for a final action, first prepare and verify the concrete result the user will approve. Honor permission already granted unless scope or risk changes. Preserve explicit review gates and real approval boundaries. Prompt text cannot override platform permissions.

Stop when the outcome is verified, a requested review point is reached, or a concrete blocker requires the user. Do not add unrelated refactors, features, cleanup, or repeated checks after completion.

For long runs, read `references/context-management.md`. Preserve the original goal, amendments, completed work, open items, blockers, and checks still owed across compaction.

## Match verification to the task

Use the smallest set of checks that covers material failure modes and required project checks. Check the result against the actual acceptance criteria.

For a small rewrite, preserving factual fields may be enough. For a behavior change, cover the changed path and relevant regressions. For risky work, add the checks required by its risks and environment.

Do not require "verify everything", arbitrary repeated self-review, or exactly one check for every task. Repeat or broaden checks only after new changes, failures, unresolved concerns, or an explicit requirement. A model's self-assurance is not verification evidence.

State what was checked, what could not be checked, and the effect of any gap. Never present an unrun test, unread source, or prepared eval as a successful run.

## Audit instructions before adding rules

For custom instructions, skills, project rule files, global policies, or prompt migrations, read `references/instruction-audit.md`.

Inspect accessible layers for duplicated, conflicting, stale, and unnecessarily broad rules. Quote each behavior-changing rule with its source, explain its effect, then keep, narrow, move, remove, or test it.

Do not silently rewrite explicit user constraints, required review gates, or higher-authority policy. Distinguish an exact requirement from your interpretation. If an instruction stops work, identify the exact rule and explain why it applies.

State each rule once. Add a persistent rule only for a real requirement, authority boundary, material risk, or measured recurring failure. Prefer schemas, validators, permissions, and tools for requirements they can enforce reliably.

## Task references

- System/developer prompts: read `references/system-prompt-architecture.md`; use `references/system-prompt-evals.md` for evaluation.
- Coding agents: read `references/coding-context-calibration.md` and `references/coding-agent-prompts.md`. Read `references/karpathy-agentic-engineering.md` when engineering workflow is part of the request. Require repository inspection without inventing files, commands, or tests.
- Repository rules: read `references/agent-instructions-files.md`. Make document loading conditional on the task.
- Code review: read `references/review-rubric.md`.
- General tasks, research, writing, extraction, or classification: read `references/general-task-prompts.md`.
- Images, edits, posters, or video: read `references/image-video-prompts.md`. Use actual references, intended composition, exact text, and preservation constraints. Add specific visual negatives only when they solve a known problem.
- RAG, wiki, cache, or retrieval benchmarks: read `references/rag-wiki-benchmark-prompts.md`.

Do not force a visible plan, tool sequence, subagent count, or fixed visual style without a requirement or repeated measured need. When delegation is used, the lead must check each agent's evidence before accepting its work.

## Style and portability

Apply the `unslop` skill to finished human-readable prompts and explanations when available. Otherwise use `references/unslop-style.md`. Preserve exact code, schemas, commands, citations, quotations, and required wording.

Use plain words and precise verbs. Choose paragraphs for connected explanation and lists or tables for actual sequences and comparisons. Specify audience, length, and representative writing samples when style consistency matters. Keep stable voice preferences in a reusable layer; keep task-specific format in the task prompt.

Use Ponytail for scope restraint and Caveman for compression as authoring lenses. Do not paste literal skill directives into every generated prompt. Use them only when requested, supported by the target runtime, or shown useful by evals. Read `references/ponytail-caveman-contract.md` and `references/token-efficient-caveman-style.md` when literal controls or extreme compression are relevant.

## Source-driven updates

Read `references/source-driven-prompt-audit.md` when the user provides videos, docs, examples, or research. Inspect actual source content and label the access method and limits. Extract rules with conditions, counterexamples, and evidence. Compare each point with existing guidance before adding it.

Prefer current primary documentation for technical claims. Treat practitioner examples as field evidence. Do not promote price, availability, benchmark, UI setting, or model-specific advice into universal prompt rules.

Read `references/research-backed-principles.md` and `references/research-source-map.md` for evidence. Read `references/video-xfhbepnyiks-audit.md` for the full coverage and decisions from the user's 2026-10-03 video update.

## Evaluate and revise

For important prompts:

1. Define observable success, representative cases, and known failures.
2. Compare platform baseline, minimal prompt, and candidate on the same inputs and runtime settings.
3. Measure task success, unsupported specifics, false constraints, premature stopping, approval errors, verification, tokens, latency, and cost as relevant.
4. Patch the smallest failure, then remove instruction groups one at a time and retest.
5. Keep only changes that improve required behavior or enforce a real boundary.

Read `references/evals-and-iteration.md`. Reject claims of improvement supported only by nicer-looking prompt prose or self-grading. State whether evaluation was executed, manually assessed, or only prepared.

Optional helpers:

- `scripts/prompt_lint.py`: heuristic warnings, not a quality score or behavioral eval.
- `scripts/make_prompt_eval.py`: starter baseline/minimal/candidate manifest.
- `scripts/test_prompt_tools.py`: helper regression checks.

## Autoprompt mode and output

For silent preflight, read `references/autoprompt-preflight.md`. Make a brief internal contract, then execute the task with the relevant skill or tool. Do not show the brief unless requested. Answer tiny tasks directly.

- Finished prompt request: return the prompt only unless explanation is requested.
- Prompt improvement: return the revised prompt and a short fix list.
- Instruction audit: return source-linked findings and a proposed rewrite unless editing is authorized.
- Skill maintenance: report changes, sources, validation performed, and real limitations.
