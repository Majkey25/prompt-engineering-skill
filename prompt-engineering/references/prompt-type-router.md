# Prompt Type Router

Classify the target before writing. Do not apply one universal mega-template to every request.

## Routing table

| Target | Primary reference | Secondary references |
|---|---|---|
| System or developer prompt | `system-prompt-architecture.md` | `system-prompt-evals.md`, `research-backed-principles.md` |
| Coding or repository agent prompt | `coding-context-calibration.md` | `coding-agent-prompts.md`, `karpathy-agentic-engineering.md`, `live-verification.md` |
| Repo instruction file | `agent-instructions-files.md` | `coding-context-calibration.md`, `context-management.md` |
| Code review prompt | `review-rubric.md` | `coding-context-calibration.md` |
| General task prompt | `general-task-prompts.md` | `universal-prompt-framework.md`, `domain-prompt-patterns.md` |
| Research prompt | `general-task-prompts.md` | `source-driven-prompt-audit.md`, `research-backed-principles.md` |
| Extraction or classification | `general-task-prompts.md` | `prompt-pattern-library.md`, `evals-and-iteration.md` |
| Image or video prompt | `image-video-prompts.md` | `domain-prompt-patterns.md` |
| Prompt audit or optimization | Domain-specific primary reference above + `prompt-quality-checklist.md` | `evals-and-iteration.md`; add `system-prompt-evals.md` only for system/developer prompts |
| Autoprompt preflight | `autoprompt-preflight.md` | the domain-specific reference selected above |

## Mandatory decisions

Before writing, answer internally:

1. What instruction layer is being authored?
2. What model or runtime will execute it?
3. What evidence is available now?
4. What evidence will the target agent be able to inspect later?
5. What behavior is a hard requirement versus a preference?
6. What can be enforced outside the prompt?
7. What is the smallest prompt that could succeed?
8. How will it be evaluated against a baseline?

## Context classification

Use the same evidence levels across prompt types:

- C0: only rough request, no source or target environment inspected
- C1: partial user-provided evidence
- C2: relevant source or environment directly inspected

Specificity ceiling:

- C0: outcome, supplied constraints, discovery path, done criteria
- C1: exact supplied facts plus labeled hypotheses and verification
- C2: verified details with traceable evidence

Never fill a template slot merely because it exists.

## Prompt length policy

Choose the shortest form that preserves requirements:

- Tiny one-off task: 1 to 5 lines
- Normal task: objective, context, constraints, output, check
- Complex or risky task: add process, tool policy, uncertainty, verification
- Durable system prompt: stable behavior only, then eval and ablate
- Repository agent: context-calibrated discovery and verification, not guessed implementation

A larger prompt is justified only by higher task complexity, stricter output requirements, real risk, or measured failures.
