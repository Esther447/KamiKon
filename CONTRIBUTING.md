# Contributing to KamiKon

KamiKon runs as **Agile Scrum** with 2-week sprints (3-week sprints for the Flutter and SPA expansions). Work is tracked on the **KamiKon Delivery Board** (GitHub Projects), in **GitHub Issues**, and under **Milestones** (one per sprint).

> **Core principle:** a feature is not *Done* when it works on `localhost:8000`. It is *Done* when it passes linting, tests and security checks, builds into a container image in GitHub Actions, and deploys cleanly to Staging.

## 1. Workflow at a Glance

```text
Backlog → Ready for Sprint → In Progress → In Review (PR Open) → QA / Staging Verified → Done
```

1. **Pick an issue** in *Ready for Sprint* for the current Sprint, assign yourself, and move it to *In Progress*.
2. **Create a branch** from `main` (see naming below).
3. **Commit** using Conventional Commits.
4. **Open a PR** using the template, link the issue (`Closes #123`), and move the card to *In Review*.
5. Get at least **one peer review**, make sure CI is green, then merge.
6. Verify the change on Staging, then move the card to *QA / Staging Verified* and then *Done*.

## 2. Branch Naming

```text
<track>/<issue-number>-<short-description>
```

| Prefix | Use for | Example |
| :--- | :--- | :--- |
| `feat/` | User stories / features | `feat/14-campus-directory-models` |
| `fix/` | Bug fixes | `fix/52-rsvp-quota-race` |
| `devops/` | CI/CD, Docker, infra, observability | `devops/5-github-actions-pytest` |
| `docs/` | Documentation | `docs/31-api-auth-guide` |

Keep branches short-lived (ideally under 3 days). Rebase on or merge `main` often.

## 3. Conventional Commits

```text
<type>(<optional scope>): <imperative summary>
```

| Type | Meaning |
| :--- | :--- |
| `feat` | New feature |
| `fix` | Bug fix |
| `ci` | CI/CD workflow change |
| `build` | Docker, dependencies, build tooling |
| `docs` | Documentation |
| `refactor` | Code change without behaviour change |
| `test` | Adding or fixing tests |
| `chore` | Maintenance |

Examples: `feat(events): enforce OPEN_ALL_UNIVERSITIES access scope`, `ci: add pytest job with postgres service`.

## 4. Pull Request Rules (Team Agreement)

- No direct pushes to `main`. All changes go through a PR.
- At least **one peer review** (and/or instructor approval) before merging.
- Status checks must pass before merging (`ruff`, `pytest`, `bandit`, `docker build`) once the CI workflows land in Sprint 0 and Sprint 1.
- Prefer **squash merge** so `main` history reads as one Conventional Commit per PR.

## 5. Issues & Labels

Always open issues through a template: **User Story**, **DevOps Task**, or **Bug Report**.

| Group | Labels |
| :--- | :--- |
| Type | `type:feature`, `type:devops`, `type:bug`, `type:docs`, `type:security` |
| Component | `comp:auth`, `comp:institutions`, `comp:events`, `comp:discovery`, `comp:tickets-qr`, `comp:notifications`, `comp:design`, `comp:ci-cd`, `comp:docker`, `comp:infra`, `comp:observability`, `comp:mobile`, `comp:spa` |
| Learning | `good-first-issue`, `pair-programming-recommended` |

Issue titles keep an ID prefix: `[US-<sprint>.<n>]` for user stories, `[DO-<sprint>.<n>]` for DevOps tasks, and `[BUG]` for bugs.

## 6. Board Fields

| Field | Values |
| :--- | :--- |
| **Status** | Backlog · Ready for Sprint · In Progress · In Review (PR Open) · QA / Staging Verified · Done |
| **Track** | Backend (Django/API) · Frontend (UI/UX) · DevOps & Infra · Mobile (Flutter) · SPA (React/Angular) |
| **Priority** | P0 - Critical · P1 - High · P2 - Medium · P3 - Nice to Have |
| **Story Points** | Fibonacci: 1, 2, 3, 5, 8 (split anything bigger than 8) |
| **Sprint** | Sprint 0 … Sprint 7 (iteration) |

## 7. DevOps Champion Rotation

Each sprint, one team member is the **DevOps Champion**. They own the pipeline health for that sprint, review every `type:devops` PR, and demo the sprint's DevOps deliverable at the review. Rotate the role so every student practises both Web Development and DevOps.

## 8. Maintaining the Backlog

The initial backlog is generated from [`scripts/sprint_backlog.json`](scripts/sprint_backlog.json) by [`scripts/setup_github_project.py`](scripts/setup_github_project.py). To add planned work in bulk, edit the JSON and re-run the script. It is idempotent and only creates what is missing.
