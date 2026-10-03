# Instruction audit

Use for custom instructions, system prompts, skills, repository rules, and model migrations. Audit the rules that the target can actually read. Do not claim to inspect inaccessible or hidden instructions.

## Inventory

Record the target runtime and its instruction hierarchy. Collect accessible rule sources and distinguish stable behavior, task context, examples, source data, tool contracts, and enforced runtime controls.

Read relevant files conditionally. A spelling edit rarely needs deployment or database documentation. A schema migration does. Do not require a full repository map before every change.

## Find behavior-changing rules

Look for instructions that trigger questions, approval requests, premature stopping, direction changes, excess formatting, repeated tests, forced options, or fixed implementation steps.

For each finding, record:

| Field | Required content |
|---|---|
| Source | Actual file/link and instruction layer |
| Quote | Exact relevant instruction, within quotation limits |
| Effect | Concrete behavior it causes in a representative task |
| Authority | User requirement, project convention, advisory guidance, or platform policy |
| Decision | Keep, narrow, move, remove, or test |
| Revision | Proposed replacement and the boundary it preserves |
| Check | A case that would expose a regression |

Audit conflicts across sources, not just duplicate sentences in one file. Distinguish explicit requirements from your interpretation. Do not expose private instructions or secrets the runtime forbids disclosing.

## Examples of narrowing

| Broad rule | Better scoped rule |
|---|---|
| Ask before doing anything | Proceed with authorized analysis and preparation; stop at the specified approval boundary |
| Never assume | Do not invent facts; use low-risk assumptions for routine gaps and ask about material ambiguity |
| Stop after the first implementation | Finish and verify the requested change, unless first-pass review is explicitly required |
| Double-check every answer | Verify the criteria and material failure modes; repeat only when new evidence warrants it |
| Give three options every time | Provide alternatives when a real choice exists or the user requests them |
| Read every project document before edits | Read the documents relevant to the affected behavior and project boundaries |

Do not remove a real review gate because it makes work slower. Do not grant authority to send, publish, delete, deploy, spend money, or change shared records unless the user has authorized that action and platform rules permit it. A prepared draft is useful work before such a gate.

## Compact audit request

```text
Audit the supplied instructions for [runtime and task]. Identify rules that trigger questions, approval, early stopping, direction changes, or excess work. For each, quote the rule, name its source, explain the effect, and propose a scoped edit. Preserve explicit user requirements and approval boundaries. Return the findings and the shortest complete replacement. Report any relevant source you could not inspect.
```

## Validation

Test at least a routine authorized task, a missing material input, a draft with a required review gate, an explicitly authorized final action, and a case with conflicting rules. Compare with the old and minimal prompts. A successful audit preserves intent while removing avoidable friction; fewer rules alone do not prove improvement.
