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
#   content: Preserve canon text exactly unless separately authorized. Run complete canon-file integrity, CONTRACTS/CHECKS audit, generated-msdmd, explicit Phi-policy, package, and actual-UCNS gates. The adapter default is external provenance with unit payloads. Only an explicit canon-bound constitutive-simultaneous authorization may declare Phi fork meaning, and downstream topology must still be verified. Never turn semantic labels into EDCM metric values or transfer UCNS theorem status.
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
13. `src/metapat/ucns_phi.py`
14. `docs/ucns-phi-policy.md`
15. `src/metapat/flow_plan.py`
16. `tests/` and `tools/`
17. repo-local `.agents/skills/`

## Load-bearing boundaries

- METAPAT constrains terms, interpretations, allowed derivations, and claim status.
- UCNS supplies actual geometry through an optional adapter.
- EDCM measures source evidence under semantic constraints.
- UCNS theorem/domain status remains attached UCNS evidence only.
- Deterministic contract tests are not empirical or formal validation of the ontology.
- Source `CONTRACTS` own obligations; test `CHECKS` own executable evidence.
- Phi authorization supplies bounded semantic authority; it does not establish or inspect UCNS topology.

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
- The adapter default is `external-provenance`; payloads remain unit.
- Never transfer theorem or validity status.

The adapter does not infer semantic meaning from a UCNS payload, tag, cell, path, carrier, symmetry, or object shape.

## UCNS Phi policy

`src/metapat/ucns_phi.py` owns the semantic authorization policy; it does not own geometry.

- Default semantic mapping remains `external-provenance`.
- Fork mode is `explicit-authorization-only`.
- The only allowed relation is `constitutive-simultaneous`.
- Parent identity, ordered child identities, source references, canon digest, policy version, unresolved constraints, and authorization digest are identity-bearing.
- Temporal succession, adjacency, provenance, alternatives, fiq connectivity, external symmetry action, and arbitrary association may not be reinterpreted as containment.
- Child order is semantic identity.
- Authorization alone is necessary but not sufficient for accepting an encoded fixture.
- Downstream integration must bind exact UCNS parent identity, payload-bearing path, ordered child stable hashes, authorization digest, and policy version.
- Phi policy never transfers theorem status, establishes METAPAT validity, or validates EDCM readouts.

## Evidence discipline

Run:

```bash
python -m pip install -e .[dev]
python -m unittest discover -s tests
python -m pytest -q
python -m pytest -q tests/test_ucns_phi.py
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

The repo-local skill source commit is declared in `.agents/skills/README.md`. Upstream `The-Interdependency/skill-lib` governs reusable skill doctrine. Do not edit vendored skills as part of runtime work unless the canonical skill-lib change is separately in scope.

## Guardrails

Do not collapse time into consciousness, registration into consciousness, observer into mind, gestalt into physical object-instantiation, tensor into a late relation map, boundary into a decorative edge, UCNS into METAPAT root, METAPAT into EDCM measurement output, domain tools into root terms, or the mere presence of a UCNS payload fork into METAPAT-authorized constitutive meaning.

## hmmm

- The downstream EDCM envelope consumer and complete shared-stack fixture.
- The topology-binding schema and fail-closed linter for actual UCNS constitutive forks.
- Semantic mappings outside default external provenance and explicitly authorized constitutive-simultaneous forks.
- Formal governance for future authorized canon rotations.
- General mutation-level verification beyond the current negative audit tests.
