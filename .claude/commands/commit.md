---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(git log:*), Bash(git commit:*), Bash(git rm:*)
description: Execute the git commit workflow - check status, review changes, and create a commit
---

# Git Commit Workflow

Execute the complete git commit workflow:

1. Run git status, diff, and log commands in parallel to understand current state
2. Analyze all changes (both staged and unstaged) 
3. Draft a commit message following project conventions
4. Add relevant files to staging (including git rm for deleted files)
5. Create commit with descriptive message (no references to Claude/Anthropic)
6. Verify commit succeeded with final git status

The commit message should:
- Be concise and descriptive
- Follow the project's existing commit style
- Focus on "why" not just "what"
- Never include references to Claude or Anthropic