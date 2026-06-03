# Prompt Engineering Skill

A reusable skill for creating, improving, auditing, and documenting prompts for ChatGPT, Codex, Claude Code, Cursor, Copilot agents, and similar AI workflows.

It turns vague requests into clear prompt contracts: objective, context, task, constraints, output format, verification, and failure handling. The skill is source-backed and treats prompts as maintainable artifacts, not magic wording.

![License](https://img.shields.io/github/license/Majkey25/prompt-engineering-skill)
![Last Commit](https://img.shields.io/github/last-commit/Majkey25/prompt-engineering-skill)
![Issues](https://img.shields.io/github/issues/Majkey25/prompt-engineering-skill)
![Stars](https://img.shields.io/github/stars/Majkey25/prompt-engineering-skill?style=social)
![Forks](https://img.shields.io/github/forks/Majkey25/prompt-engineering-skill?style=social)
![Skill](https://img.shields.io/badge/skill-prompt%20engineering-blueviolet)
![ChatGPT](https://img.shields.io/badge/ChatGPT-compatible-10a37f)
![Codex](https://img.shields.io/badge/Codex-compatible-412991)
![Claude%20Code](https://img.shields.io/badge/Claude%20Code-compatible-cc785c)

## What it does

- Creates strong prompts from rough ideas
- Rewrites weak prompts into clear task briefs
- Audits prompts for ambiguity, missing context, hidden assumptions, and weak success criteria
- Creates prompts for coding agents, research agents, RAG systems, extraction/classification, writing, and workflows
- Documents what a best-practice prompt should look like
- Builds reusable agent instruction files without bloated prompt folklore
- Adds eval/check criteria so prompt quality can be measured
- Supports token-efficient style only when useful or requested

## Core idea

The best prompt is the shortest complete contract that lets a model produce the desired output and lets a human or tool verify success.

A strong prompt usually includes:

1. Objective
2. Context and source data
3. Task and deliverable
4. Constraints and non-goals
5. Output format or schema
6. Examples, only when needed
7. Process or tool-use guidance
8. Verification or evaluation criteria
9. Failure and uncertainty policy
10. Style and length controls

The full researched blueprint lives in [`prompt-engineering/references/best-prompt-blueprint.md`](./prompt-engineering/references/best-prompt-blueprint.md).

## Why this skill is different

Most prompt libraries collect clever phrases. This skill removes that noise.

It follows current guidance from OpenAI, Anthropic, Google Gemini, Microsoft Azure OpenAI, prompt-engineering survey research, and the principle that prompts are technical debt. It avoids stale generic rules like always forcing visible chain-of-thought or stuffing every prompt with persona language.

For reasoning models, it prefers simple direct prompts, internal validation, concise rationale when useful, and explicit success criteria. For important prompts, it pushes eval cases and iteration instead of guessing.

## Installation

### ChatGPT

1. Download this repository as a ZIP.
2. Upload the `prompt-engineering/` folder through ChatGPT Skills.
3. Enable the skill in your workspace.

### Codex

Install directly from the skill directory URL:

```bash
$skill-installer install https://github.com/Majkey25/prompt-engineering-skill/tree/main/prompt-engineering
```

If your environment exposes a skill installer through `npx`, this can also work:

```bash
npx skill-installer install https://github.com/Majkey25/prompt-engineering-skill/tree/main/prompt-engineering
```

You can also tell the agent: "Install the prompt-engineering skill from this repo URL."

### Claude Code

Copy the skill folder to one of these locations:

- Project-level: `.claude/skills/prompt-engineering/`
- User-level: `~/.claude/skills/prompt-engineering/`

## Usage examples

- "Improve this prompt for a coding agent so it can implement the feature safely."
- "Turn these rough notes into a clean prompt for Codex."
- "Audit this prompt and tell me what context is missing."
- "Rewrite this prompt so Claude Code can modify the repo without breaking existing behavior."
- "Create a reusable prompt template for bug fixing."
- "Create a research prompt with citations, contradiction handling, and current-source rules."
- "Create a JSON extraction prompt with schema, null handling, and confidence rules."
- "Document how the best prompt should look and why."

## Example

Weak prompt:

```text
Make my repo better.
```

Better prompt contract:

```text
# Objective
Fix the highest-impact issue blocking the current app from running correctly.

# Context
Use the repository files, scripts, configs, and logs as evidence. Do not guess the stack.

# Task
Inspect the repo, identify the concrete blocker, fix the root cause, and verify the changed workflow live.

# Constraints
- Keep changes minimal.
- Preserve existing behavior outside the fix.
- Do not add dependencies unless required and justified.
- Do not claim done without exact verification evidence.

# Verification
Run the app or relevant command, test the changed path, test one nearby old path, and report exact commands/results.

# Output
Return summary, files changed, verification run, blockers, and remaining risks.
```

## Reference map

| Need | Reference |
|---|---|
| Best prompt structure | [`best-prompt-blueprint.md`](./prompt-engineering/references/best-prompt-blueprint.md) |
| Universal prompt template | [`universal-prompt-framework.md`](./prompt-engineering/references/universal-prompt-framework.md) |
| Coding-agent prompts | [`coding-agent-prompts.md`](./prompt-engineering/references/coding-agent-prompts.md) |
| Research-backed rules | [`research-backed-principles.md`](./prompt-engineering/references/research-backed-principles.md) |
| Prompt quality checklist | [`prompt-quality-checklist.md`](./prompt-engineering/references/prompt-quality-checklist.md) |
| Evals and iteration | [`evals-and-iteration.md`](./prompt-engineering/references/evals-and-iteration.md) |
| RAG/wiki/vector/cache prompts | [`rag-wiki-benchmark-prompts.md`](./prompt-engineering/references/rag-wiki-benchmark-prompts.md) |
| Source-driven prompt audits | [`source-driven-prompt-audit.md`](./prompt-engineering/references/source-driven-prompt-audit.md) |
| Token-efficient style | [`token-efficient-caveman-style.md`](./prompt-engineering/references/token-efficient-caveman-style.md) |

## Repository structure

```text
.
├── README.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
└── prompt-engineering/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        ├── best-prompt-blueprint.md
        ├── universal-prompt-framework.md
        ├── coding-agent-prompts.md
        ├── research-backed-principles.md
        └── ...
```

## Skill design

`prompt-engineering/SKILL.md` is the entrypoint. It controls when the skill triggers, how it routes tasks, and which reference file to load.

The reference files are deliberately split by use case so the agent loads only the relevant guidance. This keeps the skill useful without turning every prompt into a giant instruction dump.

## Contributing

Contributions should improve practical prompt behavior. Avoid generic "best practices" unless they become concrete rules, examples, templates, or checks.

See [`CONTRIBUTING.md`](./CONTRIBUTING.md).

## License

MIT. See [`LICENSE`](./LICENSE).
