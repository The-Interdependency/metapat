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

This repo currently installs lightweight repo-local skill entries for the skills METAPAT uses directly. If a local skill entry conflicts with `The-Interdependency/skill-lib`, treat `skill-lib` as canonical for the skill contract. Treat `The-Interdependency/METAPAT` as canonical only for Meta Energy Theory doctrine.

Installed local skill entries:

- `msdmd/`
- `meta-module-build/`
- `doc-build/`
- `cap-build/`
- `deps-build/`
- `owner-build/`
- `risk-boundary-build/`
- `meta/`
- `skill-build/`

Pending local skill entries:

- `llms-build/`
- `test-build/`
- `the-interdependency/`

The pending entries remain available from upstream `skill-lib`. METAPAT still has source `LLMS`, committed `llms.txt`, `CONTRACTS` blocks, and executable tests.

hmmm: exact propagation source commit SHA for a future full verbatim skill-lib sync.
