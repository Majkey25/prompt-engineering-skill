# Video source audit

Source: [Nick Puru, An OpenAI engineer just published how they prompt GPT-6 Astra...](https://www.youtube.com/watch?v=xfHbePnyiks), published 2026-10-02, duration 19:23. Reviewed 2026-10-03.

Access: complete English automatic-caption transcript and visible title, description, and chapters. Automatic captions can misname models and products. The image stream was not available for reliable inspection, so no claim here depends on unread on-screen text. Examples below are original adaptations, not verbatim transcription.

## Coverage and integration

| Time | Video point | Existing coverage | Decision |
|---|---|---|---|
| 0:00-3:28 | Model introduction and changed behavior | Minimal prompts and scoped model tuning | Exclude prices, limits, promotion, and benchmark claims from core rules |
| 3:29-5:36 | Supply usable sources and context | Evidence levels already present | Add access checks, audience, source versions, and artifact requirements |
| 6:12-9:02 | Set writing form and use voice samples | Unslop already present | Add portable fallback and task-specific style contracts |
| 9:03-10:50 | Action requests need follow-through | Already covered | Clarify draft preparation, existing authorization, and final approval gates |
| 10:51-12:30 | Choose effort for the task | Runtime separation already present | Keep settings scoped; diagnose missing inputs before increasing effort |
| 12:31-14:27 | Define completion and verify it | Done criteria already present | Use risk-matched checks rather than a fixed count |
| 14:28-15:08 | Prompt words do not change the thinking picker | Already partly covered | Distinguish settings from possible behavioral effects of wording |
| 15:09-17:02 | Audit old instruction stacks | Prompt-debt checks already present | Add quote, source, effect, revision, and regression-case audit |
| 17:03-19:23 | Rewrite a rough request and reuse it | Templates already present | Add original artifact, status, follow-up, rewrite, and coding examples |

The advertising break at 5:37-6:09 adds no prompting rule. The complete transcript was assessed, including introduction, examples, settings discussion, and closing promotion.

## Limits and corrections

- Do not reduce every task to exactly one check. The useful lesson is to avoid redundant verification while preserving required checks.
- Do not delete all confirmation language. Keep explicit review gates and action boundaries, and honor authorization already granted.
- Do not treat an effort phrase as a settings change or claim it has zero effect in every model.
- Do not put passwords or login secrets in reusable project context. Use supported authentication mechanisms.
- Do not infer why a contact is silent from silence alone. Label hypotheses and preserve source evidence.
- Do not copy large style blocks into every prompt or depend on an unavailable external skill.

## Primary cross-check

- [OpenAI model guide](https://developers.openai.com/api/docs/guides/latest-model): instruction-file audits, completion, authorized preparation before approval, writing style, and calibrated verification.
- [Rethinking skills and prompts](https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra): task-dependent document loading and removal of stale procedures.
- [ChatGPT Work guidance](https://learn.chatgpt.com/docs/get-started-with-work): outcome, sources, constraints, quality criteria, and review stage.
- [Work and Codex usage guidance](https://help.openai.com/en/articles/20001516-managing-usage-with-gpt-6-astra-in-work-and-codex): missing access is not solved by higher effort.
- [ChatGPT thinking controls](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt): wording does not automatically change the selected level.

The cross-model contracts and examples are this skill's synthesis. They require target-runtime evaluation; the video does not establish a universal quality guarantee.
