# Contributing to Lacus

The main purpose of this project is to develop a moderation and general purpose Discord bot.

## Summary

* [Code of Conduct](#code-of-conduct)
* [Issues](#issues)
* [Pull Requests](#pull-requests)
* [Git workflow](#git-workflow)
* [Useful Git Commands](#useful-git-commands)

## Code of Conduct

By participating and contributing to this project, you agree to uphold these rules:

- Give credit where credit is due
- Be respectful to all project participants
- Follow the *Code of Conduct* from [contributor-covenant.org](https://www.contributor-covenant.org/version/1/4/code-of-conduct/)

## Issues
- Documenting critical issues, bugs, and other concerns
- Tracking topics/ questions that need to be researched
- For proposing new features, suggestions, or enhancements

## Pull Requests
- PRs must be associated with an issue
- PRs should only address ONE project related concern
- If PR is rejected, code reviewer must provide reason for rejection
- PRs must be reviewed and tested* (*unless the code is small enough to not require testing*)
  - To test the code, code reviewer must pull the PR, run/test the application, and run unit tests (if any)
- Code reviewer should not do any fixes to the PR before letting the PR author do it themselves

## Git Workflow
- Assign yourself a git issue
- Create branch for issue
  - Branch naming convention: `<issue-number>-<short issue descriptor>`
    - Ex: For git issue `#4 Create contributing.md document`, branch name can look like: `4-add-contributing-doc`
- Work on code, stage your changes (`git add <changed-files>`), and commit (`git commit -m "<msg>"`)
  - Follow this commit message guidelines [link](https://chris.beams.io/posts/git-commit/)
  - Each commit should be associated with only one change; for multiple changes, make multiple commits
- When ready, push branch to github (`git push -u origin <branch-name>`)
- When ready, create pull request; make sure to link the issue in your PR (Ex: include message like `Closes #<issue-number>` in your PR body)
- Once PR is merged, branch will be deleted

## Useful git commands
```bash
## Create and switch to new branch
git checkout -b <branchname>

## After creating new feature, bugfix, etc:
git add <add-your-files> # or add all: git add .

## commit your code with a message
git commit -m "<enter your message here>"

## Pushing your branch for the first time
## after doing this once, you can just do git push 
git push -u origin <branchname> 

-------------------------------------------------------
# Comparing local and remote branches

## Pull changes from github
git fetch origin

## List all branches
git branch -a

## See changes between local branch and remote branch
git diff <localbranch> <remotebranch>

-------------------------------------------------------
# Syncing local main branch with gihub; WARNING: Hard reset, will erase unsaved work
git fetch origin
git reset --hard origin/main
git clean -f -d
```

 

