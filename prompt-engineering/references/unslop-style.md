# Unslop style

Use the dedicated `unslop` skill as the final prose pass whenever it is available. This reference is the compact fallback and embedding contract for generated prompts.

## Embedded directive

```text
@unslop / Use the Unslop skill as the final prose pass. Remove obvious AI phrasing, filler, puffery, sycophancy, fake emphasis, canned transitions, vague claims, and robotic structure. Prefer plain, specific, human wording. Preserve exact technical names, code, schemas, quotations, and required output constraints. Do not make terse technical output chattier just to add personality.
```

## Rules

- Apply to finished user-facing prose by default.
- Keep exact machine-readable output, code, commands, schemas, citations, and verbatim quotations unchanged.
- Do not add personality where the requested output is intentionally terse or formal.
- Remove generic AI filler, decorative headings, forced rule-of-three structures, vague claims, fake enthusiasm, and canned conclusions.
- Prefer plain words, active voice, concrete facts, and sentence-case headings.
- Do not use Unslop to relax technical requirements or delete necessary caveats.
- In technical agent prompts, place `@unslop` beside `@ponytail` and `@caveman` unless the prompt must be exact JSON/code-only or another strict schema.
