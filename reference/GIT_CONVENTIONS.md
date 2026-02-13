# Git & Development Conventions

## Git Commit Message Format
We follow the Conventional Commits specification:
- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Changes that do not affect the meaning of the code (white-space, formatting, etc)
- `refactor`: A code change that neither fixes a bug nor adds a feature
- `perf`: A code change that improves performance
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to the build process or auxiliary tools and libraries

Example: `feat: integrate opencode as default IDE`

## Branching
- Main branch: `main` or `master`
- Feature branches: `feat/description`
- Bugfix branches: `fix/description`

## Code Style
- Python: PEP 8, using `uv` for dependency management.
- Formatting: Prefer `black` or `ruff`.
