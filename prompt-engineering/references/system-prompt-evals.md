# System Prompt Evals and Ablation

Use for important system prompts, developer prompts, agent constitutions, coding-agent policies, reusable instruction files, and any prompt that affects many tasks.

## Contents

- [Core rule](#core-rule)
- [Required variants](#required-variants)
- [Representative cases](#representative-case-set)
- [Metrics and scoring](#metrics)
- [Frontend comparison](#frontend-prompt-evaluation)
- [Coding specificity](#coding-prompt-specificity-evaluation)
- [Ablation and regression record](#ablation-workflow)
- [Decision thresholds](#decision-thresholds)
- [Eval manifest](#eval-manifest-shape)

## Core rule

Never evaluate a system prompt only by reading it.

Compare behavior on representative tasks. A strict-looking prompt can degrade performance, suppress useful model judgment, increase token cost, create conflicts, or cause overtriggering.

## Required variants

Test at least:

1. Baseline: platform default or no custom system prompt
2. Minimal: smallest prompt containing true product requirements
3. Candidate: proposed full prompt

For mature prompts, also test ablations that remove one instruction group at a time.

## Representative case set

Include:

- 3 to 5 normal high-frequency tasks
- 2 ambiguous tasks
- 2 edge or failure cases
- 1 adversarial or conflicting-instruction case
- 1 task where the model should use initiative
- 1 task where the model should stop or request approval

For coding agents, include:

- small direct fix
- unfamiliar repository feature
- bug with misleading initial hypothesis
- UI task with existing design system
- greenfield UI task without style reference
- task requiring verification
- task where no code change is needed

## Metrics

Score observable behavior, not prompt aesthetics.

| Metric | Question |
|---|---|
| Task success | Did it produce the requested outcome? |
| Requirement adherence | Did it obey real hard constraints? |
| False constraint rate | Did prompt rules block or distort valid work? |
| Unsupported specificity | Did it invent facts, files, functions, tools, or requirements? |
| Initiative calibration | Did it act when authorized and stop when approval was required? |
| Tool quality | Did it choose, call, and interpret tools correctly? |
| Verification | Did it obtain evidence rather than claim success? |
| Output quality | Is the result useful, clear, and fit for the audience? |
| UI quality | Is the interface coherent, usable, accessible, responsive, and project-consistent? |
| Context cost | How many input tokens and repeated instructions were consumed? |
| Latency/cost | Did added prompt weight provide enough benefit? |
| Robustness | Does quality hold across varied cases and reruns? |

## Simple 0 to 2 rubric

- 0: failed or materially harmful
- 1: partially correct, needs intervention
- 2: correct and usable without material correction

Score each metric per case. Keep written failure notes, not only totals.

## Frontend prompt evaluation

Do a blind comparison when system prompts contain frontend or visual design rules.

Run the same tasks with:

- A: no custom visual doctrine
- B: outcome-only guidance, such as coherent, usable, accessible, responsive, and consistent with the project
- C: detailed visual doctrine, such as fixed palettes, cards, gradients, typography, layout, or animation rules

Have reviewers score:

- visual hierarchy
- product fit
- consistency with existing design
- usability
- accessibility
- responsiveness
- originality without gratuitous decoration
- implementation correctness

Reject detailed global rules when B or A performs better. Personal taste is not an eval metric unless it is the product requirement.

## Coding prompt specificity evaluation

Use prompts written from C0 context and check whether they:

- avoid invented file names and functions
- avoid guessed frameworks and commands
- tell the target agent to inspect the repository
- preserve user requirements without adding fake facts
- let repository evidence determine implementation

Then provide C2 evidence and confirm the prompt becomes appropriately specific.

## Ablation workflow

1. Group rules by purpose, such as permissions, tools, verification, style, UI, safety, output.
2. Remove one group.
3. Run the same cases with stable model settings.
4. Compare quality, token use, latency, and false constraints.
5. Keep the group only if it improves real outcomes or enforces a non-negotiable requirement.
6. Repeat for duplicates and high-token sections.

Do not remove safety or compliance controls merely because a tiny eval set did not trigger them. Test the relevant risk cases.

## Regression record

For each retained rule, record:

```text
Rule group:
Requirement or failure addressed:
Cases that exercise it:
Observed improvement:
Known downside:
Owner/source:
Last validated date:
```

This turns prompt maintenance into engineering instead of folklore.

## Decision thresholds

Accept a larger candidate only when:

- it materially improves task success or required safety behavior
- it does not increase false constraints beyond an agreed tolerance
- it does not degrade common tasks
- its token and latency cost is justified
- the behavior cannot be enforced more reliably elsewhere

When baseline or minimal wins, use it. A blank or short prompt is a valid result.

## Eval manifest shape

```json
{
  "prompt_type": "system",
  "target_model": "model-id",
  "variants": ["baseline", "minimal", "candidate"],
  "metrics": [
    "task_success",
    "requirement_adherence",
    "false_constraint_rate",
    "unsupported_specificity",
    "verification",
    "token_cost"
  ],
  "cases": [
    {
      "id": "normal-1",
      "input": "...",
      "required": ["..."],
      "forbidden": ["..."],
      "notes": "..."
    }
  ]
}
```

Use `scripts/make_prompt_eval.py` to create a starter manifest.
