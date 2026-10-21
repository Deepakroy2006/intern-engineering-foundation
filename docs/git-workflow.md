# One-page Git Workflow Explanation

## Core concepts

- **Repository:** A project folder tracked by Git, including its history.
- **Clone:** Copies a remote repository to your computer (`git clone URL`).
- **Branch:** An independent line of work. `main` is the stable branch; `feature/day2-profile` holds this task.
- **Switch / checkout:** Changes the branch you are working on (`git switch BRANCH`). `git checkout` is an older, still-supported alternative.
- **Add:** Stages selected changes for the next commit (`git add FILE`).
- **Commit:** Saves a snapshot to local history (`git commit -m "feat: ..."`).
- **Push:** Sends local commits to a remote repository (`git push -u origin BRANCH`).
- **Fetch:** Downloads remote updates without changing your current branch (`git fetch origin`).
- **Pull:** Fetches and integrates remote changes into the current branch (`git pull`).
- **Merge:** Integrates one branch into another. Switch to the destination branch before merging.
- **Pull Request (PR):** A request on GitHub/GitLab to review and merge a branch into another branch.
- **Code review:** Teammates inspect a PR for correctness, clarity, tests, and maintainability before approving it.
- **Merge conflict:** Occurs when Git cannot automatically reconcile overlapping changes. Edit the conflicted files, remove conflict markers, test, stage the resolution, and commit.
- **`.gitignore`:** Lists generated, local, or sensitive files Git should not track.
- **`README.md`:** The project's front page: purpose, structure, setup, and usage.

## Standard feature workflow

1. Clone the repository from GitHub/GitLab.
2. Create and switch to a feature branch: `git switch -c feature/day2-profile`.
3. Make one focused change at a time.
4. Inspect and stage changes: `git status` and `git add FILE`.
5. Commit with a meaningful message, such as `feat: add intern profile data model`.
6. Push the branch: `git push -u origin feature/day2-profile`.
7. Fetch or pull updates when teammates have changed the remote repository.
8. Open a PR from `feature/day2-profile` into `main`; describe the change and test results.
9. Review feedback, make updates, and push follow-up commits. Merge only after approval and checks.
10. Update local `main` after the PR is merged: `git switch main`, `git pull origin main`.

## Useful commands

```bash
git status
git branch
git switch main
git fetch origin
git pull origin main
git switch feature/day2-profile
git push -u origin feature/day2-profile
```

## If a merge conflict occurs

Run `git status`, open each conflicted file, resolve the `<<<<<<<`, `=======`, and `>>>>>>>` sections, run tests, then use `git add FILE` and commit the resolution. Do not blindly accept one side without checking the intended result.

## Commit message examples

- `docs: add project setup instructions`
- `feat: add intern profile data model`
- `feat: print formatted intern profile`
- `test: cover profile output`
- `chore: ignore Python cache files`
