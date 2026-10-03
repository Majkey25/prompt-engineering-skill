# Runtime calibration

Keep the core prompt portable. Add model-specific instructions only for the named target and verified need. Do not assume behavior, effort labels, UI names, or defaults carry across model generations or products.

## Diagnose before tuning

| Failure | First check |
|---|---|
| Missing or invented facts | Relevant input, source coverage, access, and grounding |
| Unnecessary questions or early stopping | Completion criteria, authorization, and conflicting instruction files |
| Poor artifact | Audience, template, format, material constraints, and inspectable output |
| Excess tests or long responses | Scope, output contract, duplicated rules, and risk-matched checks |
| Reasoning failure with adequate inputs | Target capability and supported runtime controls |

More effort cannot provide a missing file, permission, or connected app. Naming a source is not equivalent to making it accessible.

## Separate settings from words

Check current official documentation for supported controls. Select or benchmark the actual reasoning setting separately from prompt text. Do not claim that writing "think harder" changes a model picker or API parameter. Such wording can still affect behavior in some runtimes; test that effect rather than claiming it always does nothing.

Keep the model version, tools, permissions, and settings fixed when comparing prompt variants. Sweep supported effort levels separately. Record success, latency, and cost. Choose the least costly configuration that meets the required quality, rather than maximizing an effort label by default.

Do not embed one model's recommended starting level, benchmark result, price, message quota, or UI navigation in universal prompt templates. Recheck these details when the user actually requests configuration advice.

## Capability and verification

Give a tool-using target a way to inspect the result when available. A statement that a model checks its own work does not replace executed tests, source checks, artifact inspection, or required independent review.

Use enough checks to cover the task's material risks. Neither "always one check" nor "always double-check everything" is a sound universal policy.

## Current evidence

Reviewed for this update on 2026-10-03:

- [OpenAI model guide](https://developers.openai.com/api/docs/guides/latest-model): task-specific autonomy, instruction audits, style, and bounded verification.
- [Reasoning guidance](https://developers.openai.com/api/docs/guides/reasoning-best-practices): clear direct prompts and target-appropriate reasoning instructions.
- [Work and Codex usage guidance](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex): reasoning settings do not supply missing evidence or access.
- [ChatGPT thinking controls](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt): prompt wording does not automatically switch thinking level.

These sources support the distinctions above. The diagnostic table and evaluation procedure are this skill's operational synthesis, not guaranteed model behavior.
