## Summary
<!-- What does this PR change, and why? Keep the PR title in Conventional Commit form, e.g. "feat(events): add access-scope validation". -->

Closes #<!-- issue number -->

## Type of Change
- [ ] `feat` New feature / user story
- [ ] `fix` Bug fix
- [ ] `ci` / `build` Pipeline, Docker or infrastructure change
- [ ] `refactor` Code change with no behaviour change
- [ ] `test` Tests only
- [ ] `docs` Documentation only

## Track
- [ ] Backend (Django/API)
- [ ] Frontend (UI/UX)
- [ ] DevOps & Infra
- [ ] Mobile (Flutter)
- [ ] SPA (React/Angular)

## How Has This Been Tested?
<!-- Commands you ran, test cases added, manual steps. -->
```bash
docker compose run --rm web pytest --cov=apps
```

## Screenshots / Evidence
<!-- UI screenshots (mobile + desktop), workflow run links, Grafana panels, etc. -->

## DevOps & Quality Definition of Done
- [ ] Branch follows `<track>/<issue-number>-<short-description>`
- [ ] Commits follow Conventional Commits (`feat:`, `fix:`, `ci:`, `docs:`, `refactor:`, `test:`)
- [ ] Tests added/updated; coverage on new code >= 80%
- [ ] `ruff check` / `ruff format --check` pass locally
- [ ] No secrets, credentials or personal data committed
- [ ] New environment variables added to `.env.example`
- [ ] OpenAPI schema updated (if API changed)
- [ ] CI is green on this PR
- [ ] At least **1 peer review** requested

## Reviewer Notes
<!-- Anything reviewers should look at closely: migrations, race conditions, security-sensitive code (QR signing, auth), etc. -->
