# Context Management

Context is budget, attention, and reliability. More context is not automatically better.

## Core rules

- Own the context window.
- Keep agents small and focused.
- Prefer durable files/skills/rules over huge repeated chat prompts.
- Add relevant files, not the whole repo.
- Compact tool errors before feeding them back.
- Start a new chat after a logical task or repeated failure.

## Ordering

For API prompts and reusable templates:

1. Stable instructions first.
2. Stable examples next.
3. Reference context next.
4. Variable user input last.

This improves cacheability when prefix caching exists and keeps repeated structure stable.

For long-document QA, especially Claude-style long context:

1. Put long documents near the top.
2. Put the query/instructions near the end.
3. Wrap documents in tags.
4. Ask for relevant quotes first, then answer from them.

## Compact error pattern

Bad:

```text
[paste 800 lines of build output]
```

Better:

```text
Command -> npm run build
Exit -> 1
Error -> TS2322 in src/api/user.ts:42
Cause hint -> UserDto missing email field
Relevant lines -> [short excerpt]
Need -> fix root cause, rerun build
```

## Small focused agents

Use smaller task briefs when possible:

- one bug
- one route
- one workflow
- one migration slice
- one UI screen
- one verification path

Avoid asking one agent to redesign, migrate, refactor, secure, document, and optimize everything in one pass.

## Fresh chat rule

Start a new agent chat when:

- a logical task is done
- agent repeated the same failed approach
- context is polluted by old assumptions
- tool outputs dominate useful context
- scope changes
- user switches topic

Carry forward only:

- goal
- repo facts
- decisions
- changed files
- commands run
- blockers
- next step

## Prompt caching hint

For systems with prompt caching, keep the static prefix identical:

```text
[stable instructions]
[stable examples]
[stable schemas]
--- variable request below ---
[user task]
```

Do not put timestamps, random IDs, or user-specific volatile data inside the static prefix.

## What to avoid

- giant monolithic prompt
- dumping full repo tree without reason
- repeated rules in every prompt when repo instruction file fits
- long unfiltered logs
- old assumptions from previous tasks
- context rot from endless chat
