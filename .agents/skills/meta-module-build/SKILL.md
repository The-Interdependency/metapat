---
name: meta-module-build
description: Metadata-first module build skill built on msdmd. Canonical upstream is The-Interdependency/skill-lib/meta-module-build. Load this when adding or changing METAPAT modules, bridge stubs, public surfaces, tests, docs, rollout, or rollback notes.
---

# meta-module-build — local METAPAT skill entry

Canonical upstream: `The-Interdependency/skill-lib/meta-module-build/SKILL.md`.

METAPAT modules start with `MODULE_BUILD` blocks before implementation expands.

Required local fields follow upstream:

```text
id, module_name, module_kind, summary, owner, public_surface, internal_surface, tests, rollout, rollback, auth_boundary, storage_boundary, network_boundary, user_data_boundary, admin_only
```

Unknowns are `hmmm`, not guessed.
