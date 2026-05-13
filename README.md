# Prompt Engineering Skill

A reusable AI agent skill for creating, improving, auditing, and rewriting prompts for ChatGPT, Codex, Claude Code, and similar agent workflows.  
It helps turn vague requests into clear, verifiable task briefs with constraints, validation steps, and output expectations.  
The skill also supports source-backed prompt engineering and Karpathy-style agentic engineering patterns documented in the references folder.

![License](https://img.shields.io/github/license/Majkey25/prompt-engineering-skill)
![Last Commit](https://img.shields.io/github/last-commit/Majkey25/prompt-engineering-skill)
![Issues](https://img.shields.io/github/issues/Majkey25/prompt-engineering-skill)
![Stars](https://img.shields.io/github/stars/Majkey25/prompt-engineering-skill?style=social)
![Forks](https://img.shields.io/github/forks/Majkey25/prompt-engineering-skill?style=social)
![Skill](https://img.shields.io/badge/skill-prompt%20engineering-blueviolet)
![ChatGPT](https://img.shields.io/badge/ChatGPT-compatible-10a37f)
![Codex](https://img.shields.io/badge/Codex-compatible-412991)
![Claude%20Code](https://img.shields.io/badge/Claude%20Code-compatible-cc785c)

## What this skill does

- Turns vague ideas into strong prompts
- Rewrites weak prompts into clear task briefs
- Creates prompts for coding agents
- Creates prompts for research agents
- Audits prompts for ambiguity, missing context, hidden assumptions, and weak success criteria
- Helps structure reusable agent instructions
- Supports prompt patterns inspired by documented guidelines in `prompt-engineering/references/`

## Who this is for

- Developers using Codex, Claude Code, or other coding agents
- People building reusable AI workflows
- Prompt engineers
- Students and builders who want stronger AI outputs
- Teams standardizing agent instructions

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

You can also install with an `npx` installer flow in environments that expose the skill installer through `npx`:

```bash
npx skill-installer install https://github.com/Majkey25/prompt-engineering-skill/tree/main/prompt-engineering
```

It is also possible to just tell the agent to install it by itself (for example: "Install the prompt-engineering skill from this repo URL").

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
- "Create a prompt for an agent that follows Karpathy-style prompt guidelines."

## Example output

**Before**

`Make my repo better.`

**After**

A structured prompt that defines context, goal, constraints, files to inspect, required changes, validation steps, and expected final output format.

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
        ├── universal-prompt-framework.md
        ├── coding-agent-prompts.md
        ├── karpathy-agentic-engineering.md
        └── ... (additional reference guides)
```

## Skill design

`prompt-engineering/SKILL.md` is the skill entrypoint. It defines invocation behavior, operating doctrine, and output expectations.  
The `prompt-engineering/references/` files contain focused guidelines loaded when relevant, such as coding-agent prompts, context management, evaluation loops, and prompt audit patterns.

## Contributing

Contributions are welcome. Open an issue for proposed changes, then submit a pull request with practical updates and examples.  
See [`CONTRIBUTING.md`](./CONTRIBUTING.md) for contribution rules.

## License

This project is licensed under the MIT License. See [`LICENSE`](./LICENSE).
