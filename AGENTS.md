name: METAPAT
description: |
  Canonical semantic authority for Meta Energy Theory. Preserve exact canon, emit immutable provenance-bearing module envelopes, use actual UCNS only through the optional adapter, and never convert semantic labels into EDCM measurements.

# === LLMS ===
# id: project_overview
#   content: METAPAT is the canonical semantic authority for Meta Energy Theory: a substrate-independent ontology of energy-state relation and transformation. It preserves exact root canon and exports immutable semantic constraint envelopes without becoming UCNS algebra or EDCM measurement.
#
# id: key_definitions
#   METAPAT: Meta Energy Theory — Axioms, Postulates, and Theorems.
#   root_spine: Legible difference is distinction; distinction defines boundaries; boundaries define simplex; boundary is simplex of distinction; simplex holds or modifies energy in a state of being.
#   tensor: Primitive simultaneous arrangement of energy-states.
#   time: Sequential tensor alteration.
#   registration: Capacity of a simplex to preserve, express, or transmit sequential tensor alteration.
#   observer: A simplex performing registration; observer does not necessarily mean mind.
#   question: A bounded unresolved energy-state.
#
# id: architecture_summary
#   content: Authority flows from METAPAT canon into UCNS adapters and EDCM consumers. Runtime evidence flows through EDCM parsing and actual UCNS geometry into EDCM readouts under METAPAT-derived constraints. UCNS theorem status transfers into neither METAPAT validity nor EDCM measurement validity.
#
# id: usage_rules
#   content: Preserve METAPAT as root canon. Use MetapatModuleEnvelope for semantic authority and provenance. Do not recreate UCNS algebra. Do not put statements into UCNS payloads unless ratified; current mapping is external-provenance. Treat validation.py helpers as deterministic canon contract checks only. Use hmmm for unresolved details. Update msdmd blocks with code and docs.
# === END LLMS ===

# METAPAT agent entrypoint

METAPAT is the canonical home of Meta Energy Theory. No implementation owns the root.

Human entry point: `README.md`.

## Reading order

1. `CHAPTER_ZERO.md`
2. `AXIOMS.md`
3. `DOMAIN_RESTRAINT.md`
4. `THEOREMS.md`
5. `THEORIES.md`
6. `GLOSSARY.md`
7. `docs/claims-ledger.md`
8. `codex-handoff/2026-07-12-stack-repair/REQUIRED_CHANGES.md`
9. `src/metapat/canon.py`
10. `src/metapat/envelope.py`
11. `src/metapat/ucns.py`
12. `src/metapat/flow_plan.py`
13. `tests/`
14. repo-local `.agents/skills/`

## Load-bearing boundaries

```text
No implementation owns the root.
```

- METAPAT constrains terms, interpretations, allowed derivations, and claim status.
- UCNS supplies actual geometry through an optional adapter.
- EDCM measures source evidence under semantic constraints.
- UCNS theorem/domain status remains attached UCNS evidence only.
- Deterministic contract tests are not empirical or formal validation of the ontology.

## Architecture

Authority:

```text
METAPAT canon
    |
    +-- constrains terms, interpretation, allowed derivations, and claim status
    v
UCNS adapters and EDCM consumers
```

Runtime:

```text
source evidence -> EDCM parsing -> actual UCNS representation -> EDCM readouts
                                     ^
                                     |
                          METAPAT-derived semantic constraints
```

Do not restore the superseded single arrow `UCNS -> METAPAT -> EDCM`.

## Canon editing

- Preserve Erin Spencer's canon text exactly unless a canon change is separately authorized.
- `CANON_VERSION` and `canon_digest()` identify the importable canon surface.
- Any canon rotation requires explicit versioning, migration, documentation, and consumer epoch consequences.
- Unknown status is `hmmm`, not a guessed closure.

## Semantic envelope

Use `MetapatModuleEnvelope` for cross-repository semantic authority. Required distinctions:

- schema identity;
- module identity and kind;
- canon version and digest;
- exact source references and statements;
- constraints;
- permitted interpretations;
- unresolved constraints;
- provenance digest.

An envelope contains no calculated EDCM measurements. Module labels do not become measured values.

## UCNS adapter

`src/metapat/ucns.py` contains no local UCNS algebra.

- Base import must work without UCNS installed.
- Adapter calls without UCNS raise `UCNSDependencyError`.
- Transitive import failures and malformed public surfaces remain visible.
- Construct only actual `ucns.UCNSObject` values.
- Delegate composition only to actual `ucns.multiply`.
- Keep source text and references in the envelope/adaptation record.
- Current semantic mapping is `external-provenance`; payloads remain unit.
- Do not copy normalization, carrier derivation, multiplication, factorization, star/disk-flip, domain status, or theorem vocabulary into METAPAT.

## Contract checks

`src/metapat/validation.py` is a compatibility module containing deterministic canon contract checks.

- Do not call them theorem validators.
- Each helper must state what encoded condition it checks and what it cannot establish.
- Results do not detect consciousness, intent, causality, or external truth.
- Claim classifications live in `docs/claims-ledger.md`.

## Package and verification

```bash
python -m pip install -e .[dev]
python -m unittest discover -s tests
python -m pytest -q
python -m build
python -m twine check dist/*
```

Actual UCNS integration:

```bash
python -m pip install -e .[dev,ucns]
python -m pytest -q tests/test_envelope.py tests/test_ucns_bridge.py
```

Tests import `metapat`, not `src.metapat`. Base tests may explicitly skip actual-UCNS contracts when the optional dependency is absent; they may not substitute a fake algebra and report integration success.

## msdmd and skill-lib

- New modules begin with accurate `MODULE_BUILD` metadata.
- Update DOCS, CAPABILITIES, BOUNDARIES, CONTRACTS, DEPENDENCIES, and OWNERS with the same change.
- Tests contain no MODULE_BUILD blocks.
- Do not edit repo-local skills as part of runtime work unless the canonical skill-lib change is separately in scope.
- Run drift and collection tooling when available; report missing or failing checks honestly.
- Include runnable usage guidance and limitations in code and docs.

## Guardrails

Do not collapse time into consciousness, registration into consciousness, observer into mind, gestalt into physical object-instantiation, tensor into a late relation map, boundary into a decorative edge, UCNS into METAPAT root, METAPAT into EDCM measurement output, or domain tools into root terms.

## hmmm

- Whether statements eventually map to UCNS payloads, tags, or remain external provenance.
- The downstream EDCM envelope consumer and complete shared-stack fixture.
- Formal governance for future canon rotations.
- Remaining generated `llms.txt`, repo-level msdmd, and skill-lib drift reconciliation.
