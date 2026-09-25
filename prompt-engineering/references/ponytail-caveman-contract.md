# Ponytail + Caveman + Unslop Contract

Use this reference when the user explicitly wants these literal directives, when the target runtime understands them, or when evals show they improve results.

By default, apply the behaviors while **authoring** the prompt instead of pasting a large control block into every prompt.

## Authoring semantics

- Ponytail -> smallest semantically complete safe solution, existing/native dependencies first, no speculative abstractions, no unrelated scope.
- Caveman -> concise wording, low filler, exact technical language.
- Unslop -> natural direct prose without canned AI phrasing.

These are style/scope lenses, not a substitute for the actual task contract.

## Optional literal block

Use only when justified:

```text
@ponytail / Use the simplest safe solution that fully fixes the requested problem. Prefer existing/native dependencies and project patterns. Avoid speculative abstractions, unrelated cleanup, and unnecessary dependencies. Expand scope only when required for correctness.
@caveman / Keep agent communication concise and technical. No filler. Preserve required constraints, evidence, validation, and safety details.
@unslop / Keep human-readable prose plain, specific, and natural. Remove canned AI phrasing and fake emphasis without weakening technical precision.
```

Do not put the literal block into exact JSON prompts, image/video prompts, legal/medical/customer-facing copy, or any prompt where it competes with the actual output contract.

## Self-check

- Did these directives earn their tokens?
- Could the same behavior be expressed more directly in the task's Boundaries or Output section?
- Do they duplicate a skill/system instruction already active in the runtime?
- Would removing them improve clarity without reducing success?

If yes, omit the literal block.
