# METAPAT Roadmap

## Current state

METAPAT is doctrine-first and msdmd-scaffolded.

It exposes:

- root canon constants in `src/metapat/canon.py`;
- theorem validation helpers in `src/metapat/validation.py`;
- planned flow status in `src/metapat/flow_plan.py`.

## Planned architecture flow

```text
UCNS -> METAPAT -> EDCM
```

## Phase 0: Canon stability

- Preserve Chapter Zero.
- Keep root/tool/domain separation.
- Keep tests small and theorem-focused.
- Keep unresolved bridge details marked `hmmm`.

## Phase 1: UCNS side

Purpose: receive UCNS-shaped representation without letting UCNS own METAPAT root.

Initial questions:

- Which UCNS object shape should represent simplex?
- Which UCNS object shape should represent tensor?
- How should boundary-simplex state be represented?
- What conversion preserves legible difference without importing UCNS as ontology?

Status: hmmm.

## Phase 2: METAPAT module derivation

Purpose: derive explicit METAPAT modules from UCNS-shaped input.

Initial module classes:

- simplex module;
- boundary-simplex module;
- tensor module;
- relation module;
- gradient-dynamics module;
- registration module;
- time module.

Status: hmmm.

## Phase 3: EDCM side

Purpose: emit METAPAT-derived modules to EDCM for measurement and application.

Initial questions:

- Which EDCM interface receives module outputs?
- Which outputs are measurement primitives and which are narrative labels?
- How does EDCM preserve METAPAT root distinction without flattening into EDCM terms?

Status: hmmm.
