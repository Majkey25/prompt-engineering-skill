# Prompt Pattern Library

Choose patterns based on failure mode.

## Zero-shot

Use when task is simple and format is obvious.

```text
Summarize this text in 5 bullets for a busy manager.
Text: """
...
"""
```

## Few-shot / multishot

Use when style, classification, schema, or edge cases matter.

```text
Classify each ticket.
Labels -> bug / billing / feature / account / other

Example:
Input -> "I was charged twice"
Output -> billing

Now classify:
Input -> "..."
```

## Delimiters

Use to separate instruction/context/examples.

Good delimiters:

- triple quotes
- markdown sections
- XML tags
- JSON blocks

## XML-style tags

Use for long docs, multiple sources, and Claude-style prompts.

```xml
<documents>
  <document>
    <source>...</source>
    <content>...</content>
  </document>
</documents>
<task>Answer using only the documents.</task>
```

## Structured output

Use when output must be parsed.

```json
{
  "summary": "string",
  "risks": ["string"],
  "confidence": "low|medium|high",
  "missing_info": ["string"]
}
```

## Chain prompts

Use when task is too complex for one prompt.

1. Analyze sources.
2. Extract requirements.
3. Draft output.
4. Critique output.
5. Revise final.

## ReAct / tool loop

Use for agents that can act:

```text
Loop:
1. Observe current state.
2. Decide next action.
3. Use tool.
4. Read result.
5. Continue or stop by done definition.
```

## RAG/source grounding

Use when factuality matters:

```text
Use only provided sources.
Quote relevant evidence first.
Then answer.
If support is missing, say unsupported.
```

## Rubric prompt

Use when quality is subjective:

```text
Grade against rubric:
- accuracy
- completeness
- clarity
- constraints
- evidence
Return score + specific fixes.
```

## Prompt optimizer loop

Use when prompt quality matters:

```text
Prompt v1 -> run on cases -> grade -> identify failures -> edit prompt -> retest.
```

## Anti-patterns

- asking for "best practices" without specifics
- adding chain-of-thought request when a checklist is enough
- using examples that contradict constraints
- mixing multiple tasks without priority
- requesting JSON and prose at once without schema
- dumping irrelevant context
