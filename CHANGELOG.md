# Changelog

## 2026-10-03

- Replaced model-specific guidance with a portable prompt workflow and removed its profile and cross-links
- Analyzed the complete 19:23 user-provided video transcript and cross-checked technical recommendations with current OpenAI primary sources
- Added instruction audits with exact rule provenance, behavior effects, scoped revisions, and regression cases
- Added source-access checks, audience and artifact contracts, missing-field handling, and factual preservation
- Added risk-matched verification and separated draft preparation from final approval boundaries
- Added original examples for research artifacts, project updates, follow-up drafts, short rewrites, and repository fixes
- Removed contradictory automatic style directives and added a portable style fallback
- Reduced the main instruction file to 137 lines while keeping detailed references available on demand
- Passed skill validation, local reference checks, and 10 existing helper tests
- Assessed five prompt-generation scenarios in fresh agent threads; this is a qualitative check, not a measured cross-model performance gain

## Earlier changes

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
