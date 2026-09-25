# High-Constraint Prompt Extensions

Use when the task needs maximum scope discipline, hostile review, benchmark structure, or multi-agent separation. Do not add these modules automatically.

## Scope discipline

```text
Stay within the requested outcome. No unrelated features, cleanup, abstractions, or redesigns. Expand scope only when a narrower change would leave the root cause intact, violate a contract, or create a temporary workaround.
```

## Hostile review

Use for code, architecture, migrations, security, performance, data pipelines, prompts that control agents, and other quality-sensitive work:

```text
Before finishing, review the final result like a demanding maintainer. Look for incomplete root-cause fixes, hidden regressions, unnecessary scope, fragile logic, missing validation, unsupported assumptions, and fake success. Fix safe in-scope issues, then stop.
```

## Independent reviewer

Use only when independent review is worth the extra cost/context:

```text
Use a separate reviewer for the final diff/result. The reviewer should inspect evidence independently, identify blockers vs nits, and must not rubber-stamp. The primary owner decides and fixes valid findings.
```

Do not force two agents for small tasks.

## Benchmark contract

```text
Define representative cases and observable success criteria before changing the prompt/system. Compare baseline, minimal, and candidate variants on the same cases. Do not claim improvement without measured evidence. Record failures and patch only the smallest recurring pattern.
```

## Optional literal Ponytail/Caveman/Unslop

Do not require it. Load `ponytail-caveman-contract.md` only when the user explicitly wants those directives or evals prove they help.

## Self-check

- Is this extension solving a real risk or measured failure?
- Does it add an authority/safety boundary that is otherwise missing?
- Does it force process that the target could choose better itself?
- Can it be removed after the failure pattern disappears?
