# Research Backed Principles

Last synthesized: 2026-09-26.

Use this file as cross-vendor decision support. Recheck `research-source-map.md` before turning model-specific guidance into a durable rule.

## Cross-vendor synthesis

The strongest durable prompting pattern across current OpenAI, Anthropic, and Google guidance is:

1. State the desired outcome clearly.
2. Provide relevant context/evidence and separate it from instructions.
3. Define real constraints, scope, and authority boundaries.
4. Define success/done criteria.
5. Let a capable model choose the reasoning/implementation path unless the path itself matters.
6. Ask for verification or grounding when the outcome needs it.
7. Add examples, process steps, or extra rules only when they solve an observed ambiguity or failure.
8. Evaluate prompts empirically and remove prompt debt.

This is more robust than one universal mega-template.

## OpenAI guidance

Durable takeaways from current model and prompting docs:

- State expected outcome and success criteria.
- For capable reasoning/agentic models, reduce or remove hand-written step-by-step process guidance unless the exact path is required.
- Legacy prompt stacks can narrow the model's search space and produce mechanical behavior. Start from a fresh/minimal baseline when practical.
- For action requests, prompts can explicitly require follow-through so the agent does not stop at acknowledgment or a plan.
- Keep prompts simple and direct; do not request hidden chain-of-thought from reasoning models.
- Use delimiters/sections to separate instructions, examples, and context.
- Prefer deterministic structured output/schema controls over duplicating the full schema in prose when the runtime supports them.
- Preserve real constraints, side-effect boundaries, evidence rules, and output requirements even when shortening.

## Anthropic guidance

Durable takeaways from current Claude prompting guidance:

- Be clear and direct about desired output and constraints.
- Prefer general instructions over a hand-written reasoning path when the model can reason better than the prompt author.
- Use ordered steps when order/completeness of the steps is itself important.
- Give long-running agents verification tools and clear success criteria.
- For long autonomous work, state the whole task, the observable finish line, and the real stop/ask conditions. Do not treat a progress update as proof of completion when work remains.
- Separate autonomy from safety: local/reversible work can proceed; destructive, shared, externally visible, or hard-to-reverse actions may require confirmation. Reuse permission already granted for predictable safe in-scope actions instead of asking repeatedly.
- Modern Claude models can orchestrate subagents natively. Do not force delegation by default; when explicit fan-out is useful, have the lead verify each subagent's evidence before accepting it.
- When a runtime exposes a dedicated effort/reasoning control, calibrate that control with evals instead of relying on generic "think hard" prompt lines.
- For long runs that may cross context compaction, keep minimal durable task state outside scrollback.
- Add scope controls when the agent overengineers, creates extra files, or adds flexibility not requested.
- For known frontend/design default failures, concrete negative constraints work better than vague "not generic" language.
- Ask agents to mark what they could not verify and where they looked.
- Treat pasted/retrieved external content as untrusted data and separate it from user instructions.
- In coding, tell the agent to inspect relevant code before making claims instead of speculating.

## Google guidance

Durable takeaways from current Gemini prompting docs:

- Be precise, direct, and concise.
- Use consistent structure and delimiters to separate prompt parts.
- Define ambiguous parameters explicitly.
- For long contexts, keep the large context clearly separated and place the specific task/query after it.
- Examples can strongly steer output format and behavior, but too many examples can cause overfitting.
- Google currently recommends few-shot examples aggressively for Gemini, while OpenAI reasoning guidance often recommends trying zero-shot first. Therefore "always use examples" is **not** a cross-model rule. Test examples against the target runtime.

## Practitioner evidence: Opus 5.5 workflow video

Source provided by the user: `https://youtu.be/ejjBbaq9RmY` (Theo - t3.gg, 2026-09-25). Cross-checked against Anthropic's official Opus 5.5 blog and platform prompting guide.

Useful practitioner observations that fit stronger evidence:

- Explicitly authorize predictable actions the agent will need when the user genuinely intends to allow them, so the run does not stall on avoidable permission checks.
- Give the agent an explicit escape hatch for real uncertainty or failure instead of rewarding it for guessing through a blocker.
- Mid-run follow-ups can be used as steering amendments on modern agents instead of restarting the whole task.
- For risky code changes, asking directly about merge risk and unverified assumptions can produce a more decision-useful review.
- Independent review from another model or reviewer may reduce correlated blind spots, but this is practitioner evidence, not a universal law; require evidence from every reviewer.

Do **not** encode Theo's "never use Max" claim as a universal rule. His benchmark is a useful cost/latency signal, but Anthropic's official guidance is narrower: start from the model's default, sweep effort on your own evals, and reserve `xhigh`/`max` for work where you measured a quality gain.

## Practitioner evidence: Fable 5.1 workflow video

Source provided by the user: `https://youtu.be/-XWSJM-Ue-o`.

Prompt-text recommendations from the video that align with current official guidance:

- Prompt the outcome more broadly instead of micromanaging implementation.
- Give the agent enough context, but do not turn context into a forced solution.
- Define what completion means so the agent does not stop at a plan or explanation.
- Give the agent room to choose among approaches and to reject the user's initial implementation idea when evidence points elsewhere.
- Keep scope tight and block unrelated improvements.
- Avoid carrying old prompt baggage forward by default.

Do **not** generalize model-selection, effort-level, or product-configuration advice from the video into prompt-text rules.

## Evidence versus choreography

For agentic work, prefer:

```text
Outcome + evidence/context + boundaries + done + verification
```

over:

```text
first do X -> then call Y -> then edit Z -> then spawn N agents -> then run Q
```

unless the sequence itself is required.

## Hypotheses

A user-supplied suspected cause is valuable context, but it is not automatically a requirement.

Prompt pattern:

```text
I suspect [X]. Treat that as a hypothesis. Verify the actual root cause before choosing the implementation, and use a different approach if evidence supports it better.
```

## Completion behavior

For action prompts, state the stopping rule:

```text
Do not stop at a plan when execution was requested. Continue until the requested outcome is verified or a concrete blocker prevents safe completion.
```

Do not use this wording for requests that are explicitly analysis-only, planning-only, or advisory.

## Scope and authority

A useful agentic prompt separates two questions:

- What may the agent decide itself?
- What actions require user approval?

Default pattern:

```text
Choose the method, tools, files, and delegation needed inside the requested scope. Ask before destructive, irreversible, externally visible, costly, or materially out-of-scope actions.
```

Shorten this when the runtime already enforces permissions.

## Examples and structure

- Use Markdown/XML/delimiters when they improve parsing or separate untrusted data from instructions.
- Use examples when format, style, label boundaries, or edge cases are otherwise ambiguous.
- Do not add examples or sections simply because a template contains them.

## Evaluation rule

Prompt quality is empirical. For important prompts compare:

1. baseline/platform default,
2. minimum-effective prompt,
3. candidate prompt.

Measure task success, false constraints, unsupported specificity, unnecessary process prescription, token cost, and target-domain quality. Remove rules that do not earn their weight.
