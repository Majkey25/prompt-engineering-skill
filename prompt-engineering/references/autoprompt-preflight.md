# Autoprompt Preflight

Use when the user wants this skill to improve every task, not only explicit prompt-writing requests.

## Purpose

Turn any user request into a stronger internal task brief before answering or using tools.

Do not show the internal prompt unless the user asks.

Before adding factual detail, classify context: C0 rough request, C1 partial supplied evidence, or C2 inspected source/environment. Never make the internal brief look complete by inventing facts.

## Routing rule

Do not let this skill become a parasite that blocks better tools.

If a specific skill/tool fits, use this skill to sharpen the request, then invoke the specific skill/tool.

Examples:

- User asks for a spreadsheet -> internal prompt -> spreadsheet skill/tool.
- User asks for a PDF -> internal prompt -> PDF skill/tool.
- User asks for a system/developer prompt -> minimum-effective system-prompt workflow + eval plan.
- User asks for coding repo work -> classify C0/C1/C2 -> coding-agent contract / repo tools.
- User asks for image edit -> internal prompt -> image tool.
- User asks for factual current info -> internal prompt -> web/search.

## Micro internal prompt

Use for simple tasks:

```text
Task -> [user goal].
Need -> direct answer.
Constraints -> [user constraints].
Check -> obvious errors + missing assumptions.
Output -> concise, useful, no filler.
```

## Medium internal prompt

Use when task has multiple steps:

```text
Role -> senior operator.
Task -> [specific outcome]
Context -> [known facts]
Unknowns -> [what must be inferred or verified]
Constraints -> [must / must not]
Process -> plan briefly -> execute -> verify basics
Output -> [format user needs]
Risk -> state uncertainty, cite if researched
```

## Large/risky internal prompt

Use for coding, legal/finance/health, long docs, current facts, artifacts, or multi-tool work:

```text
Role -> strict task owner.
Goal -> [specific outcome]
Context -> [source material + constraints]
Success -> [done when]
Risk -> [what can go wrong]
Process -> inspect -> plan -> execute -> verify -> self-review
Tools -> [needed tools]
Output -> concise final + evidence/citations/artifact links
Stop -> no fake certainty; disclose blockers
```

## Autoprompt checklist

Before answering:

- What is the actual deliverable?
- What does done mean?
- What can be verified?
- What context is missing?
- Which tool/skill is more specific?
- What should not be changed/assumed?
- Is current web/internal search required?
- Should response be concise or detailed?

## What not to do

- Do not reveal private hidden reasoning.
- Do not spend more tokens planning than solving.
- Do not ask avoidable clarifying questions.
- Do not ignore specific tools because this skill triggered.
- Do not turn every tiny task into a giant prompt.
- Do not add files, functions, frameworks, commands, sources, dates, people, or other specifics that were not supplied or verified.
- Do not make a custom system prompt larger than the behavior gap it must fix.
