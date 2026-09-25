# Domain Prompt Patterns

Apply the `unslop` skill as the final prose pass for every human-readable prompt produced from these patterns. Skip literal `@unslop` injection only when the target format is exact JSON, code-only, image/video prompt text, or another strict machine-readable schema.

## Writing / editing

Include:

- audience
- purpose
- source facts
- voice
- length
- banned phrases
- structure
- edit pass

```text
Goal -> write [artifact] for [audience].
Talk caveman -> concise, natural, no filler.
Context -> [why it matters]
Input facts -> [facts only]
Voice -> [direct / warm / formal / human / terse]
Constraints -> [length / must include / must avoid]
Output -> final only.
Self-check -> remove filler, vague claims, fake polish, repetition.
```

## Research / synthesis

Include:

- research question
- source priority
- date sensitivity
- citation rules
- contradiction handling
- uncertainty
- output shape

```text
Goal -> answer [question] with current evidence.
Talk caveman -> concise, cite claims, no filler.
Sources -> prefer primary docs / official data / recent sources.
Method -> search, compare, triangulate, note conflicts.
Rules -> cite key claims; mark inference; say unknown if unsupported.
Output -> verdict / evidence / conflicts / risks / next step.
```

## Extraction / classification

Include:

- schema
- labels
- examples
- null handling
- confidence
- validation

```text
Goal -> extract fields from input.
Talk caveman -> output exact JSON only.
Schema -> {...}
Rules:
- preserve original wording where possible
- missing -> null
- uncertain -> add confidence < 0.7
- no invented fields
Examples -> [2-3 if label mapping matters]
Output -> valid JSON only.
```

## Analysis / decision

Include:

- options
- criteria
- assumptions
- risks
- tradeoffs
- recommendation format

```text
Goal -> choose best option for [situation].
Talk caveman -> direct, no fence-sitting.
Options -> [A/B/C]
Criteria -> [ranked]
Constraints -> [budget/time/risk]
Method -> compare evidence, stress test, pick.
Output -> recommendation / why / tradeoffs / risks / next action.
```

## Image prompt

Load `image-video-prompts.md` for generation, editing, reference composition, diagrams, text-heavy layouts, and model-specific visual restraint. Start with a direct 1 to 3 sentence scene or edit request when that is enough.

Include only when material:

- subject
- composition
- style
- medium
- camera/lens if relevant
- lighting
- color
- mood
- constraints
- negatives
- iteration target

```text
Goal -> generate image.
Use compact natural visual language. Do not inject the technical Ponytail or Caveman contract.
Subject -> [main subject]
Composition -> [framing / layout / focal point]
Style -> [medium / era / rendering]
Lighting -> [setup]
Palette -> [colors]
Details -> [must include]
Negative -> [avoid]
Output -> one image prompt, no commentary.
```

## Video prompt

Load `image-video-prompts.md`. Use timing beats only when timing matters.

Include only when material:

- scene
- duration
- camera motion
- subject motion
- timing beats
- style
- audio if relevant
- negatives

```text
Goal -> generate [duration] video.
Scene -> [where / who / mood]
Camera -> [movement / lens / framing]
Action beats -> 0-2s [...], 2-5s [...]
Style -> [look]
Negative -> [avoid]
Output -> video prompt only.
```

## Study / tutoring

Include:

- learner level
- topic
- goal
- diagnosis
- practice
- feedback loop

```text
Goal -> teach [topic] to [level].
Talk caveman -> simple, exact, no fluff.
Method -> explain -> example -> question -> feedback.
Rules -> do not dump wall of text; check understanding.
Output -> lesson + 3 practice tasks + answer key.
```

## Business workflow / SOP / automation

Include:

- trigger
- inputs
- tools/systems
- steps
- exception paths
- owner/handoff
- audit trail
- done state

```text
Goal -> design workflow for [process].
Talk caveman -> concise, operational.
Trigger -> [event]
Inputs -> [data]
Steps -> [ordered]
Tools -> [systems]
Exceptions -> [failures + handling]
Output -> SOP / automation spec / checklist.
Done -> owner can run without guessing.
```

## System prompt / assistant behavior

Load `system-prompt-architecture.md` and `system-prompt-evals.md`. Start from baseline behavior and write only durable cross-task rules. Do not use this compact pattern as permission to add task data, guessed project details, or a generic frontend aesthetic.

Include only when required:

- role
- scope
- behavior rules
- refusal/limits
- tool use
- output style
- memory/context rules
- eval checklist

```text
Role -> [assistant purpose]
Scope -> [what it handles]
Rules -> [do / don't]
Tools -> [when to use]
Output -> [style]
Quality -> [self-check]
Limits -> [when to ask / refuse / escalate]
```
