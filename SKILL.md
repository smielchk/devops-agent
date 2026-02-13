---
name: devops
description: "End-to-end project management: environment setup, AI-powered smart sync, core git ops, and complex deployment (Docker/uv) with AI-IDE (opencode) integration."
---

# DevOps Agent Skill

## 1. Environment & Identity (Self-Healing)
- **Identity Check**: If `git config user.name` is missing, ask user: "I need your name and email for Git commits."
- **Auth**: If `gh auth status` fails, guide user to run `gh auth login`.
- **Tool Detection**: 
    - **Python**: Check for `python3-venv`, `pip`, and `uv`.
    - **Docker**: Check for `docker` AND `docker-compose`.
    - **AI-IDE**: Check for `opencode`. Install via `npm i -g opencode-ai` if missing.

## 2. Smart Sync & AI-IDE (opencode)
- **AI-Native IDE**: **CRITICAL** - For complex code maintenance, refactoring, or feature implementation, prefer using `opencode run`.
    - Usage: `opencode run --model opencode/kimi-k2.5-free "task description"`.
    - Refer to [reference/OPENCODE_RECIPES.md](reference/OPENCODE_RECIPES.md) for optimized prompts.
- **Security Scrub**: **CRITICAL** - Before any `git add` or `commit`, run `python3 scripts/safety_scrub.py .` to scan for hardcoded credentials. Force move them to `.env`.
- **Semantic Commits**: Analyze `git diff --cached` and generate messages based on [reference/GIT_CONVENTIONS.md](reference/GIT_CONVENTIONS.md).

## 3. Core Git Operations
- **Status**: `git status -sb`.
- **Sync**: `git pull --rebase origin $(git branch --show-current)`.
- **Auto-Push**: Automated `git add` -> `commit` -> `git push`.

## 4. Deployment Intelligence (README-First)
**CRITICAL**: Before running/deploying, ALWAYS read `README.md`.
- **Strategy Selection**: Identify if it's `uv run`, `npm start`, or `docker compose`.
- **Docker Strategy**: Prefer `docker compose` (V2).

## 5. Quality & Knowledge
- **Pre-flight**: Run `uv run pytest` before pushing.
- **Doc Maintenance**: After fixing environment issues or adding deployment methods, update the project's `README.md` to save the knowledge.

## Bundled Resources
- **Scripts**:
  - `scripts/safety_scrub.py`: Scans for leaked secrets.
- **References**:
  - `reference/GIT_CONVENTIONS.md`: Commit and branching standards.
  - `reference/OPENCODE_RECIPES.md`: AI-IDE best practices.
