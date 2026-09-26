# Changelog

## Unreleased

- Added model-scoped Claude Opus 5.5 prompting and harness guidance based on Anthropic primary sources and a full practitioner-video cross-check
- Added explicit long-run finish/continue/stop contracts, bounded durable task state, and steering semantics
- Separated runtime effort controls from prompt prose and added eval rules for premature stopping, repeated permission checks, and unverified work
- Added concrete visual-negative guidance, actual-reference preference, and stronger untrusted pasted-content boundaries
- Added explicit unverified-item reporting and evidence checks for delegated/subagent work
- Added evidence-calibrated coding prompts and prompt-type routing
- Added system/developer, general-task, image, and video prompt guidance
- Added a typed eval-manifest helper with overwrite protection
- Added Ruff and strict Pyright configuration for helper scripts
- Aligned review-only, verification, and untrusted-source safety contracts
- Added researched best prompt blueprint documentation
- Removed global mandatory caveman style from generated prompts
- Updated source-backed prompt principles for reasoning models, evals, and prompt technical debt
- Tightened skill metadata for ChatGPT/Codex skill discovery
- Improved public repository documentation
- Added installation instructions
- Added usage examples
- Added contribution guidelines
- Added `npx` installation guidance and agent self-install note
