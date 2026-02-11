---
name: github
description: "End-to-end GitHub management: setup, auth, smart sync, CI checks, and deployment."
metadata:
  {
    "openclaw":
      {
        "emoji": "🐙",
        "requires": { "bins": ["gh", "git"] },
        "install":
          [
            {
              "id": "apt",
              "kind": "apt",
              "package": "gh git",
              "bins": ["gh", "git"],
              "label": "Install GitHub CLI and Git (apt)",
            },
          ],
      },
  }
---

# GitHub Advanced Skill

## 1. Setup & Auth (Environment Self-Healing)

Before any operation, check environment:
- **Check Git/GH**: `git --version && gh --version`
- **Interactive Auth**: If `gh auth status` fails, prompt user:
  ```bash
  gh auth login --hostname github.com -p https -w
  ```
- **Git Identity**: If `git config user.name` is empty, ask the user:
  "I need your Git identity to sign commits. Please provide your Name and Email."
  Then set them:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your@email.com"
  ```

## 2. Smart Repo Creation & Sync

To create and push a local project:
```bash
# In project directory
git init
gh repo create <repo-name> --public --source=. --remote=origin --push
```

To auto-sync with AI-generated messages:
1. **Analyze**: Run `git diff --cached` to see what changed.
2. **Summarize**: Describe the changes (e.g., "Fix: update main.py logic" or "Feat: add new test case").
3. **Commit**: `git commit -m "<AI-generated message>"`
4. **Push**: `git push origin $(git branch --show-current)`

## 3. Core Git Operations (Discovery & Maintenance)

Keep your local copy fresh and explore history:
- **Pull**: `git pull --rebase origin $(git branch --show-current)` (Fetch and rebase to keep history clean).
- **Log**: `git log --oneline --graph --decorate -n 10` (Visual history of last 10 commits).
- **Status**: `git status -sb` (Concise status showing branch info).
- **Diff**: `git diff` (Unstaged changes) or `git diff --cached` (Staged changes).
- **Show**: `git show <commit-hash>` (Details of a specific commit).

## 4. Pre-flight CI Checks

Run local checks before pushing to prevent broken builds:
- **Python**: `pytest` or `python -m py_compile *.py`
- **Node**: `npm test`
- **GitHub Actions**: `gh run list` to check remote status.

## 4. Deployment & Run

Run the project locally or trigger deployment:
- **Local Run**: `python main.py` or `npm start`
- **Remote Trigger**: `gh workflow run deploy.yml`

## 5. Standard Troubleshooting

- **Auth Error**: Run `gh auth login`.
- **Merge Conflict**: `git pull --rebase origin main` then resolve.
- **CI Failure**: `gh run view --log-failed`.
