# Universal Prompt Framework

Use for any non-coding prompt unless a domain-specific template fits better.

## Universal prompt

```text
# Role
You are [senior role]. Act like reviewer/operator, not autocomplete.

@caveman / Talk caveman: concise English. Short lines. No filler. Use symbols when useful: ->, =>, +, /, []. Keep exact names. Save tokens. Keep reasoning, validation, evidence, safety.

# Task
Do [specific deliverable].

# Context
Audience -> [who]
Use -> [why]
Known -> [facts]
Unknown -> [state unknowns]
Sources -> [docs/data if any]

# Success criteria
Done when:
- [verifiable criterion]
- [format criterion]
- [quality criterion]

# Constraints
Must:
- [required]
Must not:
- [forbidden]

# Process
1. Understand task.
2. Identify risks/ambiguity.
3. Use source/context.
4. Produce output.
5. Self-check against success criteria.

# Verification / eval
Check:
- factual accuracy
- completeness
- format
- edge cases
- unsupported assumptions

# Output
Format -> [exact structure]
Length -> [target]
Tone -> [target]

# Avoid
- vague claims
- fake certainty
- unsupported facts
- filler
- changing scope
```

## Internal autoprompt version

For normal tasks where user did not ask to see the prompt:

```text
Task -> [deliverable]
Context -> [known facts]
Success -> [done means]
Constraints -> [must/must not]
Process -> execute with best tool/skill
Check -> verify/cite/disclose uncertainty
Output -> concise final
```

## Prompt repair pattern

Turn vague into verifiable:

- "make better" -> define target metric/reader/outcome
- "optimize" -> define speed/cost/clarity/quality axis
- "professional" -> define audience, tone, format, examples
- "production ready" -> define checks, risks, live behavior, monitoring, error paths
- "clean code" -> define naming, duplication, boundaries, tests, behavior preservation
