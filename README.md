# METAPAT

**Meta Energy Theory — Axioms, Postulates, Theorems, and Theories.**

METAPAT is the canonical semantic authority for Meta Energy Theory: a substrate-independent ontology of energy-state relation and transformation. UCNS may represent geometry and EDCM may measure source evidence; neither implementation owns or proves the root.

## Root spine

```text
Legible difference is distinction.
Distinction defines boundaries.
Boundaries define simplex.
Boundary is simplex of distinction.
Simplex holds or modifies energy in a state of being.
```

## Architecture

Authority flow:

```text
METAPAT canon
    |
    +-- constrains terms, interpretation, allowed derivations, and claim status
    v
UCNS adapters and EDCM consumers
```

Runtime data flow:

```text
source evidence -> EDCM parsing -> actual UCNS representation -> EDCM readouts
                                     ^
                                     |
                          METAPAT-derived semantic constraints
```

Proof-status boundary:

```text
UCNS theorem/domain status remains UCNS evidence.
It does not transfer into METAPAT ontology validity or EDCM measurement validity.
```

The former single diagram `UCNS -> METAPAT -> EDCM` is superseded because it collapsed authority, data, and proof status into one ambiguous arrow.

## Install, test, and build

Python 3.11 or newer is required.

```bash
python -m pip install -e .[dev]
python -m unittest discover -s tests
python -m pytest -q
python tools/check_contract_graph.py
python tools/generate_msdmd.py --check
python -m build
python -m twine check dist/*
```

The base package has no third-party runtime dependency. Install the actual UCNS adapter dependency explicitly:

```bash
python -m pip install -e .[dev,ucns]
```

## Byte-complete canon identity

`metapat.canon_digest()` binds two distinct surfaces without changing canon text:

1. the exact importable constants and definitions;
2. the exact Git blob identities of every canon-bearing Markdown file.

The manifest covers `CHAPTER_ZERO.md`, `AXIOMS.md`, `POSTULATES.md`, `THEOREMS.md`, `THEORIES.md`, `GLOSSARY.md`, and `DOMAIN_RESTRAINT.md`.

```python
from pathlib import Path
import metapat

print(metapat.CANON_VERSION)
print(metapat.CANON_IDENTITY_SCHEMA_VERSION)
print(metapat.canon_digest())
metapat.assert_canon_files_match(Path("."))
```

The canon remains `metapat-canon-v1`; identity schema `2.0.0` expands coverage to the complete canon file set. The corrected aggregate identity is `116fffd7a02487537e43581152fca74099db43c1a0af8df2e737fa9b8afbd00e`. A digest is identity evidence, not empirical validation or formal proof of the ontology.

## Immutable semantic module envelope

`MetapatModuleEnvelope` carries semantic authority and provenance only. Schema `1.2.0` carries:

- schema and module identity;
- canon version and byte-complete digest;
- exact source references and statement text;
- bounded constraints;
- permitted interpretations;
- unresolved `hmmm` fields;
- deterministic provenance digest.

The canonical root spine is represented as `module_kind="canon-module"`, not silently classified as a simplex. The allowed module vocabulary also includes distinction, simplex, boundary-simplex, tensor, energy-state, scalar, vector, relation, gradient, transformation, registration, observer, time, question, postulate, theorem, and theory. Naming a kind does not supply an empirical state or measured value.

Deserialization rejects unknown, missing, or incorrectly typed fields rather than coercing malformed input.

```python
import metapat

module = metapat.root_spine_module_envelope()
serialized = module.to_json()
roundtrip = metapat.MetapatModuleEnvelope.from_json(serialized)
assert roundtrip == module
```

The installed package includes `fixtures/root-spine-envelope-v1.json`, which must remain byte-identical to the live canonical constructor.

## Actual UCNS adapter

METAPAT defines no local `UCNSObject`, normalization, carrier calculation, or composition algebra. `metapat.ucns` lazily imports the actual `ucns` package only when adaptation is requested.

```python
import metapat
import ucns

envelope = metapat.root_spine_module_envelope()
adaptation = metapat.adapt_envelope_to_ucns(envelope)

assert isinstance(adaptation.ucns_object, ucns.UCNSObject)
assert adaptation.record.ucns_object_hash == ucns.stable_hash(adaptation.ucns_object)
assert adaptation.record.constraints == envelope.constraints
assert adaptation.record.permitted_interpretations == envelope.permitted_interpretations
assert adaptation.record.theorem_status_transfer is False
```

The adapter's default semantic mapping is explicitly:

```text
external-provenance
```

METAPAT statement text is not inserted into UCNS payloads by the adapter. The complete semantic envelope survives in the serializable adaptation record while UCNS payloads remain unit.

## Explicit UCNS Phi fork authority

The default external-provenance mapping has one ratified semantic exception: METAPAT may issue a canon-bound `UCNSForkAuthorization` when ordered children are simultaneous constitutive components of one parent.

```text
default adapter mapping: external-provenance
authorized relation: constitutive-simultaneous
authorization mode: explicit-only
```

Temporal succession, adjacency, provenance, alternatives, fiq connectivity, external symmetry actions, and arbitrary association are not payload containment. Authorization binds semantic meaning only; UCNS owns geometry, and a downstream integration must still bind the authorization to the exact parent object, payload path, ordered child hashes, and encoded topology. No theorem status, METAPAT validity, or EDCM measurement validity transfers.

See `docs/ucns-phi-policy.md`.

## Contract and evidence graph

The repository follows the pinned `skill-lib` split:

```text
CONTRACTS are source-owned obligations.
CHECKS are test-owned accountable witnesses.
audit reconciles the graph without importing code.
```

`tools/check_contract_graph.py` rejects source `call:` fields, orphan contracts, phantom `proves` targets, unresolvable `self::` calls, and top-level executable tests without CHECKS declarations. Its negative behavior is itself tested.

`metapat_msdmd.ts` is generated by `tools/generate_msdmd.py` through the pinned msdmd collector. It records declaration identity, metadata digests, and graph edges for all bounded `src/`, `tests/`, and `tools/` surfaces—including `src/metapat/flow_plan.py`—while excluding vendored `.agents` declarations from the product graph.

## Canon contract checks

`metapat.validation` contains deterministic **canon contract checks**, not theorem validators. A `True` result means supplied Python values satisfy an encoded condition. It does not establish external truth, empirical validity, consciousness, intent, or formal proof. See `docs/claims-ledger.md`.

## Current canon map

- `CHAPTER_ZERO.md` — canonical chapter.
- `AXIOMS.md` — invariant root and primitive extension.
- `POSTULATES.md` — allowed working claims.
- `THEOREMS.md` — internal derivations and proof sketches, classified in the claims ledger.
- `THEORIES.md` — application families that do not redefine root.
- `DOMAIN_RESTRAINT.md` — domain-import boundary.
- `GLOSSARY.md` — term meanings and status.
- `docs/claims-ledger.md` — public claim classification.
- `UCNS_IMPLEMENTATION.md` — actual adapter scope and limits.
- `docs/ucns-phi-policy.md` — explicit constitutive-fork semantic authority and downstream limits.
- `COMPLIANCE.md` — current evidence surfaces and commands.

## Repository rule

```text
No implementation owns the root.
```

`skill-lib`, `ucns`, `edcmbone`, `edcm`, `a0`, `a0p`, AIMMH, and other repositories may consume, apply, test, or represent METAPAT. They do not define it.

## hmmm

The downstream EDCM consumer and full shared UCNS/METAPAT/EDCM fixture remain separate repository changes. The first complete constitutive-fork fixture still requires a topology-binding schema and fail-closed linter over actual UCNS payload paths. Semantic uses outside explicitly authorized constitutive-simultaneous forks remain external provenance unless separately ratified.
