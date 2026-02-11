# GitHub Manager & AI Sync

An AI-powered automation tool for managing GitHub repositories, integrated with OpenClaw.

## 🚀 Features

- **AI Commit Messages**: Automatically analyzes `git diff` using OpenAI models to generate professional, semantic commit messages.
- **Enhanced GitHub Skill**: A comprehensive OpenClaw skill definition for repository setup, authentication, and maintenance.
- **Smart Sync**: One-command workflow for `add`, `commit`, and `push`.
- **Core Git Integration**: Built-in support for `pull`, `log`, `diff`, and `status`.
- **Environment Self-Healing**: Automated checks for Git/GH installation and interactive auth guidance.

## 🛠️ Components

- `main.py`: The Python core that talks to OpenAI and handles the Git workflow.
- `SKILL.md`: The OpenClaw skill definition file.
- `.env`: Environment configuration for API keys and base URLs.

## 📦 Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your `.env`:
   ```env
   OPENAI_API_KEY=your_key
   OPENAI_BASE_URL=https://api.openai.com/v1
   OPENAI_MODEL=gpt-4o
   ```
3. Run the manager:
   ```bash
   python3 main.py
   ```

## 🐙 OpenClaw Integration

This project doubles as an OpenClaw Skill. Copy `SKILL.md` to your OpenClaw skills directory to enable advanced GitHub management capabilities.
