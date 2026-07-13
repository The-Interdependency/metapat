name: METAPAT
description: |
  Canonical semantic authority for Meta Energy Theory. Preserve exact canon and its complete file identity, emit strict immutable provenance-bearing envelopes, use actual UCNS only through the optional adapter, and never convert semantic labels into EDCM measurements.

# === LLMS ===
# id: project_overview
#   content: METAPAT is the canonical semantic authority for Meta Energy Theory. Canon text and every canon-bearing file identity are protected together. Strict immutable envelopes carry exact semantic constraints and provenance without becoming UCNS algebra or EDCM measurement.
#
# id: key_definitions
#   METAPAT: Meta Energy Theory — Axioms, Postulates, Theorems, and Theories.
#   root_spine: Legible difference is distinction; distinction defines boundaries; boundaries define simplex; boundary is simplex of distinction; simplex holds or modifies energy in a state of being.
#   tensor: Primitive simultaneous arrangement of energy-states.
#   time: Sequential tensor alteration.
#   registration: Capacity of a simplex to preserve, express, or transmit sequential tensor alteration.
#   observer: A simplex performing registration; observer does not necessarily mean mind.
#   question: A bounded unresolved energy-state.
#
# id: architecture_summary
#   content: METAPAT owns semantic authority, actual UCNS owns geometry, and EDCM owns measurement. Their identities and proof statuses remain separate. No implementation owns the root.
#
# id: usage_rules
#   content: Preserve canon text exactly unless separately authorized. Run complete canon-file integrity, CONTRACTS/CHECKS audit, generated-msdmd, package, and actual-UCNS gates. Keep complete statements, references, constraints, permitted interpretations, unresolved hmmm, and provenance outside UCNS payload meaning. Do not modify EDCM in a METAPAT producer repair.
# === END LLMS ===

# METAPAT agent entrypoint

METAPAT is the canonical home of Meta Energy Theory. No implementation owns the root.

Human entry point: `README.md`. Evidence entry point: `COMPLIANCE.md`.

## Reading order

1. `CHAPTER_ZERO.md`
2. `AXIOMS.md`
3. `DOMAIN_RESTRAINT.md`
4. `POSTULATES.md`
5. `THEOREMS.md`
6. `THEORIES.md`
7. `GLOSSARY.md`
8. `docs/claims-ledger.md`
9. `COMPLIANCE.md`
10. `src/metapat/canon.py`
11. `src/metapat/envelope.py`
12. `src/metapat/ucns.py`
13. `src/metapat/flow_plan.py`
14. `tests/` and `tools/`
15. repo-local `.agents/skills/`

## Load-bearing boundaries

- METAPAT constrains terms, interpretations, allowed derivations, and claim status.
- UCNS supplies actual geometry through an optional adapter.
- EDCM measures source evidence under semantic constraints.
- UCNS theorem/domain status remains attached UCNS evidence only.
- Deterministic contract tests are not empirical or formal validation of the ontology.
- Source `CONTRACTS` own obligations; test `CHECKS` own executable evidence.

Do not restore the superseded single arrow `UCNS -> METAPAT -> EDCM`.

## Canon editing

- Preserve Erin Spencer's canon text exactly unless a canon change is separately authorized.
- `CANON_VERSION`, `CANON_IDENTITY_SCHEMA_VERSION`, `CANON_FILE_BLOBS`, and `canon_digest()` jointly identify the complete canon surface.
- Run `metapat.assert_canon_files_match(Path('.'))` from repository root.
- Any authorized canon rotation requires explicit versioning, manifest rotation, migration, documentation, and consumer epoch consequences.
- Unknown status is `hmmm`, not guessed closure.

## Semantic envelope

Use `MetapatModuleEnvelope` for cross-repository semantic authority. Preserve schema identity, module identity, canon identity, exact references and statements, constraints, permitted interpretations, unresolved constraints, and provenance digest. Deserialization must reject malformed types rather than coercing them. An envelope contains no calculated EDCM measurements.

The packaged `fixtures/root-spine-envelope-v1.json` must equal the live canonical constructor.

## UCNS adapter

`src/metapat/ucns.py` contains no local UCNS algebra.

- Base import works without UCNS installed.
- Adapter calls without UCNS raise `UCNSDependencyError`.
- Construct only actual `ucns.UCNSObject` values.
- Delegate composition only to actual `ucns.multiply`.
- Retain the complete semantic envelope in the strict serializable adaptation record.
- Current semantic mapping is `external-provenance`; payloads remain unit.
- Never transfer theorem or validity status.

## Evidence discipline

Run:

```bash
python -m pip install -e .[dev]
python -m unittest discover -s tests
python -m pytest -q
python tools/check_contract_graph.py
python tools/generate_msdmd.py --check
python -m build
python -m twine check dist/*
```

Actual UCNS integration:

```bash
python -m pip install -e .[dev,ucns]
python -m pytest -q tests/test_envelope.py tests/test_ucns_bridge.py tests/test_packaging.py
```

The no-import audit must close every contract/check edge and remain negative-tested. `metapat_msdmd.ts` is generated, never hand-maintained. Tests import `metapat`, not `src.metapat`. Skipped actual-UCNS tests are non-proof unless the optional dependency is genuinely absent and the integration job runs separately.

## skill-lib

The repo-local skill pin is declared in `.agents/skills/README.md`. Upstream `The-Interdependency/skill-lib` governs reusable skill doctrine. Do not edit vendored skills as part of runtime work unless the canonical skill-lib change is separately in scope.

## Guardrails

Do not collapse time into consciousness, registration into consciousness, observer into mind, gestalt into physical object-instantiation, tensor into a late relation map, boundary into a decorative edge, UCNS into METAPAT root, METAPAT into EDCM measurement output, or domain tools into root terms.

## hmmm

- Whether statements eventually map to UCNS payloads, tags, or remain external provenance.
- The downstream EDCM envelope consumer and complete shared-stack fixture.
- Formal governance for future authorized canon rotations.
- General mutation-level verification beyond the current negative audit tests.
