# General Task Prompts

Use for non-coding, non-system, and non-image tasks. Choose the smallest task-specific contract instead of dumping the universal template.

## Contents

- [Context rule](#general-context-rule)
- [Minimal prompt](#minimal-general-prompt)
- [Writing and research](#writing-and-editing)
- [Extraction and classification](#extraction)
- [Analysis and planning](#analysis-and-decision-support)
- [Teaching, summarization, and translation](#teaching-and-study)
- [High-stakes domains](#high-stakes-domains)
- [Creative ideation](#creative-ideation)

## General context rule

Do not add factual context that the user did not provide and you did not verify.

Separate:

- Given: user-supplied facts and source material
- Verified: facts checked with tools or authoritative sources
- Inferred: interpretations that must be labeled
- Unknown: missing information that should be searched, requested only when necessary, or disclosed

## Minimal general prompt

```text
Outcome: [what should be true when finished]
Context: [relevant supplied/verified facts; label hypotheses]
Boundaries: [must / must not / non-goals]
Done: [observable success criteria]
Output: [format, audience, length]
```

Use this unless the task needs a narrower pattern below. Do not add a step-by-step process unless the order or method is part of the requirement. If the user wants a finished document, spreadsheet, file, or other artifact, ask the target for the finished deliverable rather than an outline or plan unless planning is the actual task.

## Writing and editing

Specify audience and purpose before decorative style labels.

```text
Write [artifact] for [audience] to achieve [purpose].
Use only these facts: [facts/source].
Tone: [concrete description or example].
Must include: [requirements].
Avoid: [specific unwanted behavior].
Length/format: [constraint].
Return the final artifact only.
```

For rewriting, preserve meaning unless the user explicitly authorizes changes. Do not invent facts to make prose sound stronger.

## Research and factual synthesis

```text
Answer [research question].
Use [source scope], prioritizing primary and current sources.
Distinguish sourced fact, inference, disagreement, and unknown.
Cite load-bearing claims.
Return: verdict, evidence, conflicts, uncertainty, and practical implication.
```

Add date boundaries, geography, population, product version, or jurisdiction only when they matter.

## Extraction

```text
Extract [fields] from the supplied input.
Return valid [JSON/CSV/table] matching [schema].
Use null for missing values.
Preserve source wording for [fields].
Do not infer values unless the schema explicitly permits inference.
Validate types and required fields before returning.
```

Use deterministic structured-output features when available instead of relying only on prose.

## Classification

```text
Classify each input into exactly one of: [labels].
Definitions: [decision boundaries].
If no label is supported, use [other/unknown].
Return [schema] with label, confidence, and short evidence.
```

Use examples only when label boundaries are genuinely ambiguous. Include hard edge cases, not only obvious examples.

## Analysis and decision support

```text
Evaluate [decision] for [decision maker].
Options: [known options].
Criteria: [ranked criteria].
Constraints: [budget, time, risk, dependencies].
Challenge assumptions and identify missing evidence.
Return recommendation, rationale, tradeoffs, failure conditions, and next action.
```

Do not force a recommendation when evidence is insufficient. State what evidence would change the decision.

## Planning and operations

```text
Create an executable plan for [outcome].
Known constraints: [facts].
Identify dependencies, owners, milestones, risks, and completion checks.
Do not invent organizational facts, dates, or resources.
Return the smallest sequence that reaches the outcome.
```

For workflows, include exception paths and handoffs only when operationally relevant. If the target can execute the work, give it the outcome and decision boundaries first; let it choose the method unless the procedure must be fixed.

## Teaching and study

```text
Teach [topic] to a learner at [level] for [goal].
Start from what they already know: [context].
Explain with [preferred depth], then use one worked example and targeted practice.
Check understanding before increasing difficulty.
Return [lesson/practice/answer key format].
```

Do not overload the learner with every related concept.

## Summarization

```text
Summarize [input] for [audience and use].
Preserve [decisions, numbers, deadlines, risks, quotes, or other critical details].
Exclude [noise].
Do not add information absent from the source.
Return [format and length].
```

## Translation

```text
Translate from [source language] to [target language] for [audience/use].
Preserve meaning, names, numbers, formatting, and terminology.
Use [formal/informal/domain] register.
Flag ambiguous source phrases instead of silently inventing meaning.
Return translation only unless notes are requested.
```

## High-stakes domains

For medical, legal, financial, security, or safety-critical tasks:

- verify current primary sources
- define jurisdiction/version/population where relevant
- separate information from professional advice or authorized action
- include uncertainty and material limitations
- do not turn generic prompts into autonomous authority
- require human approval or deterministic controls for consequential actions

Use domain-specific skills when available.

## Creative ideation

```text
Generate [number] distinct concepts for [goal/audience].
Constraints: [real constraints].
Vary each option by [meaningful dimensions].
Avoid near-duplicates and generic filler.
For each, give [name, core idea, why it fits, risk/tradeoff].
```

Do not overconstrain early exploration. Separate divergent ideation from later selection and refinement.

## Prompt output policy

When the user asks for a prompt, return the final prompt only unless they request explanation, variants, or an audit.

When improving a prompt, preserve valid requirements. Do not add invented context merely to make the prompt look more complete. Treat user implementation ideas as hypotheses unless they are explicitly mandatory, and do not turn them into a forced process without evidence.


## Final prose pass

Apply the `unslop` skill to finished human-readable prompt text. Preserve exact schemas, code, quotations, commands, and other literal output constraints.
