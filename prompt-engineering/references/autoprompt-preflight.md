# Autoprompt Preflight

Use when the user wants this skill to improve normal tasks silently before execution.

## Purpose

Turn the request into the smallest useful internal work contract. Do not show it unless asked.

Classify context first: C0 rough request, C1 partial supplied evidence, C2 inspected source/environment. Never invent facts to make the brief look complete.

## Routing rule

Do not let prompt engineering block a better task-specific skill or tool. Sharpen the request, then route to the correct capability.

## Micro brief

```text
Outcome -> [user goal]
Boundaries -> [real user constraints]
Output -> [what they need]
```

## Medium brief

```text
Outcome -> [specific result]
Context -> [known facts + relevant unknowns]
Boundaries -> [must / must not / non-goals]
Done -> [observable success]
Output -> [format]
```

## Large/risky or agentic brief

```text
Outcome -> [specific result]
Evidence -> [sources / repo / files / user facts]
Hypotheses -> [unverified theories]
Boundaries -> [scope + authorization]
Done -> [acceptance criteria]
Verification -> [evidence standard]
Output -> [format]
```

Do not add a generic `inspect -> plan -> execute -> verify` chain by reflex. Let the target skill/agent choose the process unless exact order matters.

## Internal agent autonomy rule

When the user asked for action, not advice:

```text
Own the task through completion. Do not stop at a plan if you can safely continue. Choose the method and tools inside scope. Ask only before actions that cross a real safety, authorization, or reversibility boundary.
```

## Checklist

- What result does the user actually need?
- What does done mean?
- Which facts are supplied, verified, hypothesized, or unknown?
- What must not change?
- Is there an action/approval boundary?
- Can the target agent choose the method better than the prompt writer?
- Is verification required, and what evidence would count?
- Is a specific tool/skill more appropriate?

## What not to do

- Do not reveal hidden reasoning.
- Do not over-plan tiny tasks.
- Do not ask avoidable clarification.
- Do not invent files, functions, frameworks, commands, sources, dates, people, or other specifics.
- Do not force subagents, exact tools, or a step list without a real reason.
- Do not make a custom system prompt larger than the behavior gap it must fix.
