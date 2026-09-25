# Universal Prompt Framework

Use for a general prompt when no narrower task-specific template fits.

Treat this framework as a menu. Never fill placeholders with invented context. Classify evidence as C0/C1/C2 before adding factual specificity.

## Default template

```text
# Outcome
[One precise result.]

# Context
Given: [user-supplied facts/source data]
Verified: [checked facts, if any]
Hypotheses: [suspicions or interpretations that still need validation]
Unknowns: [what to inspect, ask only if material, or disclose]

# Boundaries
Must: [hard requirements]
Must not: [forbidden outcomes/actions]
Non-goals: [out of scope]
Authority: [what the agent may decide/do without asking, if relevant]

# Done
- [observable criterion]
- [preservation criterion]
- [verification criterion, if needed]

# Output
[format / audience / length / schema]
```

Optional modules:

```text
# Examples
[1-3 representative examples only when they improve consistency.]

# Verification
[Evidence/citation/test standard.]

# Required process
[Only when exact order/procedure is part of the requirement.]

# Failure / uncertainty
[What to do if evidence is missing or requirements conflict.]
```

## Agentic add-on

Use when the target can act with tools:

```text
Own the task through completion. Choose the method, tools, and delegation needed inside the requested scope. Do not stop at a plan when execution was requested. Ask before destructive, irreversible, externally visible, costly, or materially out-of-scope actions.
```

If the runtime already enforces these permissions, shorten or omit this block.

## Clarification add-on

```text
Ask only when missing information could materially change correctness, safety, authorization, or the requested outcome. Otherwise choose the narrowest reasonable interpretation and proceed.
```

## What not to add by default

- role/persona that changes nothing,
- "think step by step" or requests for hidden reasoning,
- a fixed tool-call sequence,
- a fixed number of subagents,
- guessed files/APIs/commands,
- redundant "be thorough" / "be smart" / "use best practices" wording,
- giant negative lists,
- repeated verification instructions.

## Internal autoprompt version

```text
Outcome -> [deliverable]
Context -> [known evidence + hypotheses + unknowns]
Boundaries -> [must / must not / scope / authorization]
Done -> [observable success]
Verify -> [only if outcome warrants it]
Output -> [shape]
```

## Prompt repair pattern

- "make better" -> define target reader/metric/outcome
- "optimize" -> define the axis and how improvement is measured
- "professional" -> define audience, tone, and format
- "production ready" -> define observable behavior, risk boundaries, and verification
- "clean code" -> define the concrete maintainability requirement in touched scope
- "fix everything" -> define the requested outcome and directly related blockers only

## Final prose pass

Apply `unslop` to human-readable prompt text. Preserve exact schemas, commands, quotations, and literal constraints.
