---
name: devops
description: "End-to-end project management: environment setup, AI-powered smart sync, core git ops, and complex deployment (Docker/uv) with README-first intelligence."
metadata:
  {
    "openclaw":
      {
        "emoji": "🛠️",
        "requires": { "bins": ["gh", "git"] },
        "install":
          [
            {
              "id": "apt",
              "kind": "apt",
              "package": "gh git docker.io docker-compose",
              "bins": ["gh", "git", "docker", "docker-compose"],
              "label": "Install DevOps Toolchain (apt)",
            },
          ],
      },
  }
---

# DevOps Agent Skill

## 1. Environment & Identity (Self-Healing)
- **Identity Check**: If `git config user.name` is missing, ask user: "I need your name and email for Git commits."
- **Auth**: If `gh auth status` fails, guide user to run `gh auth login`.
- **Tool Detection**: 
    - **Python**: Check for `python3-venv`, `pip`, and `uv`.
    - **Docker**: Check for `docker` AND `docker-compose`.
    - **Node**: Check for `npm` or `bun`.

## 2. Smart Sync & AI Semantics
- **Creation**: `git init` and `gh repo create <name> --public --source=. --push`.
- **AI Commits**: Analyze `git diff --cached` and generate semantic messages (e.g., `feat:`, `fix:`, `docs:`).
- **Security Scrub**: **CRITICAL** - Before any `git add` or `commit`, scan for hardcoded credentials (e.g., `sk-...`). Force move them to `.env` or mask them in examples.
- **Auto-Push**: Automated `git add` -> `commit` -> `git push`.

## 3. Core Git Operations (Discovery & Maintenance)
- **Status**: `git status -sb` (Concise status).
- **History**: `git log --oneline --graph --decorate -n 10` (Visual history).
- **Diff**: `git diff` (Unstaged) and `git diff --cached` (Staged).
- **Sync**: `git pull --rebase origin $(git branch --show-current)`.

## 4. Deployment Intelligence (README-First)
**CRITICAL**: Before running/deploying, ALWAYS read `README.md`:
- **Env Strategy**: Is it `uv run`, `npm start`, or `python main.py`?
- **Config Audit**: Are `.env` or `config.yaml` required? If missing (even if `.example` exists), alert user and offer to create them.
- **Docker Strategy**: 
    - Prefer `docker compose` (V2).
    - Fallback to `docker-compose` (V1) if V2 is unavailable.
    - Check for `Dockerfile` or `docker-compose.yml`.

## 5. Quality & Operations (CI/Run)
- **AI-Native IDE (opencode)**: **CRITICAL** - For complex code maintenance, refactoring, or feature implementation, prefer using `opencode run`.
    - Usage: `opencode run --model opencode/kimi-k2.5-free "task description"`.
    - Context: Always run within the project root to ensure `opencode` can see the codebase.
- **Pre-flight**: Run `pytest` or `python -m py_compile` before pushing.
- **Remote CI**: `gh run list` and `gh run view --log-failed` to check GitHub Actions.
- **One-Click Run**: Execute identified start scripts from README.
- **Doc Maintenance**: After fixing environment issues or adding deployment methods, update the project's `README.md` (e.g., `Troubleshooting` or `Deployment` section) to save the knowledge for others.

## 6. Troubleshooting
- **Permission**: For repo deletion, user must run `gh auth refresh -s delete_repo`.
- **Python Venv**: On Debian/Ubuntu, suggest `sudo apt install python3-venv` if creation fails.
- **Conflicts**: Use `git pull --rebase` and resolve manually if needed.
