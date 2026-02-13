# opencode Recipes & Best Practices

## Common Tasks

### 1. Feature Implementation
**Prompt**: "Implement a new feature [X] in [Project]. Ensure all related modules are updated and basic tests are added."
**Goal**: Project-wide synchronized changes.

### 2. Code Refactoring
**Prompt**: "Refactor the module [Y] to improve readability and reduce complexity. Use modern Python idioms where applicable."
**Goal**: Improving code quality without changing behavior.

### 3. Adding Tests
**Prompt**: "Scan the existing codebase and add missing pytest unit tests for the core logic in [Directory]."
**Goal**: Increasing test coverage.

## Configuration
- Always run `opencode run` from the **project root**.
- Default Model: `opencode/kimi-k2.5-free`.
