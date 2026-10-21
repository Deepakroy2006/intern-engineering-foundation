# Intern Engineering Foundation

A beginner-friendly Day 2 exercise for learning Git and version control through a simple Python intern profile.

## Repository structure

```text
intern-engineering-foundation/
├── docs/
│   └── git-workflow.md
├── src/
│   └── intern_profile.py
├── tests/
│   └── test_intern_profile.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer
- Git

## Run the profile

```bash
python src/intern_profile.py
```

Replace the sample intern name, role, department, and skills in `src/intern_profile.py` with your own details.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Git workflow

The assignment uses `main` as the stable branch and `feature/day2-profile` for the profile implementation. See [`docs/git-workflow.md`](docs/git-workflow.md) for the workflow, including push, pull, fetch, merge, pull requests, reviews, and merge-conflict handling.

## Example output

```text
Intern Profile
--------------
Name: Your Name
Role: Engineering Intern
Department: Engineering
Skills: Python, Git, Problem Solving
```

The profile is intentionally populated with sample values. Update the constants at the top of `src/intern_profile.py` before submitting your work.
