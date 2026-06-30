# METAPAT skill-lib / msdmd compliance ledger

## Status

METAPAT has a full structural compliance scaffold for skill-lib / msdmd:

- `AGENTS.md` exists and contains the source `LLMS` declaration.
- `llms.txt` exists as the generated-style repo instruction file.
- `.agents/skills/` exists with local skill entries for directly used skill-lib skills.
- `pyproject.toml` exists.
- `src/metapat/` exists as an importable Python package.
- `src/metapat/canon.py` has colocated msdmd metadata for module build, docs, capability, owner, boundary, and contracts.
- `src/metapat/validation.py` has colocated msdmd metadata for module build, docs, capability, owner, boundary, and contracts.
- `src/metapat/flow_plan.py` has colocated msdmd metadata for planned UCNS -> METAPAT -> EDCM flow.
- `tests/test_contracts.py` exists as executable theorem contract tests.
- `metapat_msdmd.ts` exists as the repo-level msdmd collection point.

## Five functional tests

The executable suite now protects:

1. Boundary Earns Its Keep.
2. Tensor Precedes Time.
3. Registration Is Not Time.
4. Observer Role by Registration.
5. Consciousness Is Optional.

The suite also retains root-spine and time/registration definition checks.

## Planned architecture edge

```text
UCNS -> METAPAT -> EDCM
```

Current state:

```text
UCNS side: hmmm, planned but not implemented.
EDCM side: hmmm, planned but not implemented.
Exact bridge APIs: hmmm.
```

## Local check command

```bash
python -m unittest discover -s tests
```

## hmmm

Full local execution of the compliance/test commands was not run from this chat environment.

A local clone should run:

```bash
python -m unittest discover -s tests
python -m llms.build --root . --out llms.txt --check
python -m msdmd.collect --root . --repo metapat --out metapat_msdmd.ts
```

Record exact output here after local execution.
