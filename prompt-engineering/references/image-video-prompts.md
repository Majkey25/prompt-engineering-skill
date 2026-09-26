# Image and Video Prompts

Use this file when creating or improving prompts for image generation, image editing, image composition, diagrams, posters, product imagery, infographics, storyboards, or video generation.

## Contents

- [Core rule](#core-rule)
- [Task classification](#first-classify-the-task)
- [Evidence and references](#evidence-and-reference-rule)
- [Generation and editing](#minimal-image-prompt)
- [Text, products, and diagrams](#text-in-images)
- [Video prompts](#video-prompt)
- [Negative constraints](#negative-constraints)
- [Tool parameters](#tool-parameters-versus-prompt-text)
- [Specificity and iteration](#specificity-calibration)

## Core rule

Describe the intended visual result clearly. Do not turn every visual request into keyword soup or a page-long cinematic specification.

For modern multimodal generators, 1 to 3 clear sentences are often enough. Add detail only when it controls something the user actually cares about or corrects a measured failure.

## First classify the task

- Generate from text
- Edit an existing image
- Preserve subject or identity
- Combine references
- Transfer style
- Create text-heavy layout or infographic
- Create a diagram or instructional visual
- Generate a video or animation
- Create multiple consistent variants

The prompt structure changes by task. Do not use a generic photography template for every image.

## Evidence and reference rule

Use supplied images, brand assets, sketches, layouts, and text as source material. Do not invent visual facts that are not visible or provided. When the target runtime can inspect images, prefer the actual screenshot, chart, diagram, or reference over retyping its content into prose; spatial relationships and visual defects can be lost in transcription.

For editing, distinguish:

- Change: what must be altered
- Preserve: what must remain unchanged
- Match: lighting, perspective, texture, proportions, identity, or style
- Output: crop, aspect ratio, background, resolution, or transparency when supported

## Minimal image prompt

```text
Create [purpose/output]: [main subject and action] in [setting], with [desired visual style or mood]. [Framing, lighting, text, or preservation constraint only if important].
```

Example:

```text
Create a square album cover showing an empty rural bus stop at night in heavy fog, photographed with harsh sodium-vapor lighting. Leave clean negative space in the upper third for the title and include no extra text or logos.
```

## Image editing prompt

```text
Using the provided image, change only [target change]. Preserve [identity/composition/background/lighting/other fixed details]. Match the original [perspective, shadows, texture, focus, and color treatment].
```

Example:

```text
Using the provided room photo, replace only the blue sofa with a worn brown leather chesterfield. Keep the room layout, pillows, windows, camera angle, and lighting unchanged, and match the original shadows and perspective.
```

Do not redescribe the whole image unless fidelity requires it. Excess restatement can accidentally change preserved regions.

## Reference composition

```text
Create [final output] using [element] from reference 1 and [element] from reference 2. Preserve [critical identity/details]. Place them in [scene] with consistent scale, perspective, lighting, and shadows.
```

When several references serve different roles, label them explicitly:

- Reference A: subject identity
- Reference B: clothing/product
- Reference C: pose or composition
- Reference D: visual style

## Text in images

Provide exact text separately and define hierarchy.

```text
Create a vertical event poster.
Headline: "NIGHT SIGNAL"
Secondary text: "12 SEPTEMBER 2026"
Footer: "DOORS 19:00"
Use a bold condensed sans-serif headline, strong contrast, and enough spacing for every line to remain readable. Do not add any other words, logos, or pseudo-text.
```

For dense infographics, first finalize the copy and information hierarchy. Then generate the visual. Do not ask the image model to invent factual labels or statistics.

## Product and commercial imagery

Specify:

- product and material
- intended use or audience
- scene or surface
- camera angle when it matters
- lighting when it matters
- brand/reference fidelity
- required empty space or crop
- forbidden extra labels or logos

Do not add lens numbers, studio terminology, or rendering jargon unless it serves the desired result.

## Diagrams and instructional visuals

Define information structure before style.

```text
Create a clean 16:9 architecture diagram showing [nodes] and [directed relationships]. Use exact labels from the supplied list. Group [items] inside [boundary]. Make the primary flow visually dominant. Do not add components or connections not present in the source.
```

For technical accuracy, generate or validate labels and relationships outside the image model when possible.

## Video prompt

Use a compact scene description plus temporal behavior.

```text
Create a [duration] [aspect ratio] video of [subject/action] in [setting]. Camera: [framing and movement]. Motion beats: [ordered actions]. Visual treatment: [style, light, mood]. Preserve [reference identity/details]. Avoid [specific failure only].
```

Example:

```text
Create an 8-second 16:9 video of a battered red guitar amplifier powering on in a dark rehearsal room. Start with a static close-up, then slowly push in as the pilot light flickers and dust moves in the warm beam. Realistic handheld texture, shallow depth of field, no text, no logos, no camera cuts.
```

Use timestamped beats only when timing matters. Do not micromanage every second for a simple motion.

## Negative constraints

Use negatives for concrete failure prevention. If a model repeatedly falls back to an unwanted design default, name the exact pattern to avoid; a vague instruction such as "avoid a generic AI look" is weaker than concrete exclusions.

- no extra text or logos
- preserve the face and expression
- do not change the background
- no additional objects
- no camera cuts
- no duplicated limbs

Avoid giant generic negative lists. They consume attention and can fight the positive description.

Prefer positive direction when possible:

Bad:

```text
No clutter, no ugly layout, no bad lighting, no weird colors.
```

Better:

```text
Use a restrained composition with one clear focal point, soft natural light from the left, and a muted neutral palette.
```

## Tool parameters versus prompt text

When the image or video tool exposes explicit parameters, use them instead of duplicating them in prose:

- aspect ratio or dimensions
- output count
- quality
- transparent background
- duration
- frame rate
- seed, when supported
- edit mask or reference images

Keep the prompt about visual intent. Keep machine settings in tool arguments.

## Specificity calibration

Add detail for:

- exact text
- identity preservation
- composition and object relationships
- brand fidelity
- camera framing that changes meaning
- lighting central to the mood
- layout constraints
- elements that must remain fixed

Leave room for model judgment for:

- incidental background details
- ordinary material rendering
- subtle color variation
- natural pose details
- noncritical decoration

A long prompt is not automatically more controllable. Test and iterate on the actual failure.

## Iteration pattern

1. Generate a minimal version.
2. Identify the largest mismatch.
3. Change one or two prompt dimensions.
4. Preserve successful parts explicitly when editing.
5. Repeat until the intended result is reached.

Do not rewrite the entire prompt after every attempt unless the concept changed.

## Output behavior

When the user asks for a prompt, return the final prompt only unless they ask for explanation or variants.

When the user asks for prompt options, vary one meaningful dimension per option, such as composition, mood, medium, or camera treatment. Do not return near-duplicates with random adjectives.
