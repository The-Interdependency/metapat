# Repo-local skill installation

METAPAT follows the organization convention for repo-local agent skills.

Canonical upstream:

```text
The-Interdependency/skill-lib
```

Local path:

```text
.agents/skills/<skill-name>/SKILL.md
```

This repo installs lightweight repo-local skill entries for the skills METAPAT uses directly. If a local skill entry conflicts with `The-Interdependency/skill-lib`, treat `skill-lib` as canonical for the skill contract. Treat `The-Interdependency/METAPAT` as canonical only for Meta Energy Theory doctrine.

Installed local skill entries:

- `msdmd/`
- `llms-build/`
- `meta-module-build/`
- `doc-build/`
- `cap-build/`
- `deps-build/`
- `owner-build/`
- `test-build/`
- `risk-boundary-build/`
- `meta/`
- `the-interdependency/`
- `skill-build/`

Source commit: `The-Interdependency/skill-lib` @ `d0f6209` (verbatim sync).
