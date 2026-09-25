# Best Prompt Blueprint

Use when the user asks what a strong prompt should look like, wants prompt documentation, or needs a reusable template.

Updated: 2026-09-22

## Short answer

The best prompt is the shortest complete contract that tells the model:

- what outcome is wanted,
- what context/evidence matters,
- what boundaries cannot be crossed,
- what "done" means,
- what output to return,
- and how to handle uncertainty or verification when it matters.

It does **not** automatically tell the model how to think, which files to edit, which tools to call, or which intermediate steps to follow.

## Core principle

Prompt the result and the decision boundaries before prompting the procedure.

Concrete beats clever. Testable beats inspirational. Scoped beats exhaustive. Evidence beats guessed detail. A shorter prompt is better when it preserves the contract and lets a capable model choose a better path.

## Core versus optional modules

### Core

Most prompts need only:

1. Outcome
2. Relevant context/evidence
3. Boundaries or constraints
4. Done / acceptance criteria
5. Output shape

### Optional

Add only when useful:

- examples,
- source/citation policy,
- authority/approval boundary,
- uncertainty handling,
- style/length controls,
- exact process or tool instructions.

Exact process belongs in the prompt only when the path itself matters or measured failures justify it.

## Context is not instructions

Keep these distinct:

- **Given**: user-supplied facts and source material.
- **Verified**: facts checked against a source/runtime.
- **Hypothesis**: suspected cause or preferred implementation that still needs validation.
- **Unknown**: information the target should inspect, ask for only if material, or disclose.

Bad:

```text
The cache is leaking. Replace it with an LRU in services/conversation.py.
```

when neither claim has been verified.

Better:

```text
I suspect the conversation cache may be unbounded. Verify the actual root cause from the repository, then choose the smallest safe fix consistent with existing patterns.
```

## Outcome and done state

Weak:

```text
Fix the bug.
```

Better:

```text
Fix the bug end-to-end. Done means the root cause is understood, the broken workflow works again, nearby behavior is preserved, relevant checks pass, and the final diff contains no unrelated changes.
```

Done criteria are more useful than a long step list because they tell the model what success looks like without unnecessarily narrowing the solution path.

## Decision authority

For agents that can inspect, edit, and use tools, state the authority boundary rather than micromanaging implementation:

```text
Choose the implementation approach, files, tools, and any useful delegation yourself from the available evidence. Stay within scope. Ask before destructive, irreversible, externally visible, costly, or materially out-of-scope actions.
```

If the runtime already enforces these permissions, keep the prompt shorter.

## Clarification rule

Avoid both reckless guessing and unnecessary stalls:

```text
Ask only when missing information could materially change correctness, safety, authorization, or the requested outcome. Otherwise use the narrowest reasonable interpretation and proceed.
```

## Process guidance

Do **not** add a hand-written procedure by default.

Add ordered steps when:

- exact order is required,
- the workflow must be reproducible or auditable,
- a compliance/safety procedure is mandatory,
- intermediate outputs must be inspected,
- or evals show the model repeatedly chooses a bad process.

Otherwise, state the goal and constraints and let the model choose the route.

## Verification

Specify the evidence standard, not every command:

```text
Verify the result using the strongest relevant existing checks and the real workflow/runtime where practical. If verification cannot run, report the exact blocker.
```

Use exact test commands, URLs, browsers, or tools only when they are known requirements.

## Examples

Examples are useful when they define:

- ambiguous label boundaries,
- exact format,
- tone/style that words alone do not capture,
- tricky edge cases.

Start without examples when the task is already clear. Add 1 to 3 representative examples if evals show they help. Too many examples can add cost, bias, or overfitting.

## Structure and delimiters

Use Markdown headings, XML tags, or simple delimiters when they help distinguish instructions from data. Be consistent. For long context, keep source material clearly separated from the final task/query.

## Canonical minimal template

```text
# Outcome
[What should be true when the task is finished?]

# Context
[Relevant supplied or verified facts. Label hypotheses and unknowns.]

# Boundaries
[Must / must not / non-goals / authority limits.]

# Done
[Observable acceptance criteria.]

# Output
[Required format, audience, length, or schema.]
```

Optional additions:

```text
# Verification
[Evidence standard or required checks.]

# Examples
[Only when they improve consistency.]

# Required process
[Only when the exact path matters.]
```

## Prompt debt

Treat every extra rule as a liability until it earns its place.

Remove a rule when it:

- solves an old model problem that no longer appears,
- duplicates tool/schema/permission behavior,
- encodes guessed implementation,
- forces planning or delegation without need,
- repeats another instruction,
- or fails to improve representative eval cases.

## Evidence-calibrated specificity

- C0 -> desired outcome + discovery targets + boundaries + done.
- C1 -> exact supplied facts + labeled hypotheses + verification.
- C2 -> verified specifics where they reduce search or risk.

Never fill an empty template slot with plausible detail.

## Final check

Before shipping a prompt, ask:

1. Does it define the outcome?
2. Does "done" mean something observable?
3. Did I accidentally turn context or a hypothesis into an instruction?
4. Did I prescribe a process the model could choose better itself?
5. Is the authority boundary clear enough for an agentic task?
6. Is unrelated scope expansion blocked?
7. Could I delete a section without lowering success on evals?
