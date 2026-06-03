# Domain Prompt Patterns

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
Style -> concise, natural, no filler.
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
Style -> concise, cite claims, no filler.
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
Style -> direct, no fence-sitting.
Options -> [A/B/C]
Criteria -> [ranked]
Constraints -> [budget/time/risk]
Method -> compare evidence, stress test, pick.
Output -> recommendation / why / tradeoffs / risks / next action.
```

## Image prompt

Include:

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
Style -> compact, visual terms only.
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

Include:

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
Style -> simple, exact, no fluff.
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
Style -> concise, operational.
Trigger -> [event]
Inputs -> [data]
Steps -> [ordered]
Tools -> [systems]
Exceptions -> [failures + handling]
Output -> SOP / automation spec / checklist.
Done -> owner can run without guessing.
```

## System prompt / assistant behavior

Include:

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
