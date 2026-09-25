# Token Efficient Prompt Style

Use to reduce prompt and response bloat without weakening the work contract.

Apply Ponytail, Caveman, and Unslop as authoring behavior. Do not automatically paste literal skill directives into generated prompts.

## What to compress

Compress:

- greetings and filler,
- repeated rules,
- motivational language,
- verbose transitions,
- obvious procedural narration,
- duplicated context,
- headings that do not improve parsing.

Do not compress away:

- outcome,
- scope and authorization boundaries,
- relevant evidence/context,
- done criteria,
- verification requirements,
- safety constraints,
- schemas or exact literals,
- uncertainty/failure behavior when material.

## Compact agent pattern

```text
Goal -> fix login bug end-to-end.
Context -> [facts]; suspicion: [hypothesis].
Scope -> only directly related changes; preserve existing auth behavior.
Authority -> choose implementation/tools; ask before destructive/external actions.
Done -> root cause fixed + login works + relevant checks pass + no unrelated diff.
Verify -> strongest existing checks + real login flow where practical.
Final -> concise summary + verification + real blockers only.
```

This is better than compressing the prompt into vague fragments such as `fix app fast. test maybe.`

## Symbols

Use `->`, `=>`, `+`, `/`, and `[]` only when they make the prompt easier to scan. Do not turn normal prose into notation if readability gets worse.

## Literal directives

If the user explicitly asks to embed Ponytail/Caveman/Unslop, load `ponytail-caveman-contract.md` and use the compact optional block there.
