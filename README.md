# METAPAT

**Meta Energy Theory — Axioms, Postulates, Theorems, and Theories**

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
python -m build
python -m twine check dist/*
```

The base package has no third-party runtime dependency. Install the actual UCNS adapter dependency explicitly:

```bash
python -m pip install -e .[dev,ucns]
```

A built wheel can be checked independently:

```bash
python -m venv .wheel-venv
.wheel-venv/bin/python -m pip install dist/*.whl
.wheel-venv/bin/python -c "import metapat; print(metapat.__version__)"
```

## Deterministic canon identity

`metapat.canon_digest()` binds consumers to the exact importable canon surface without changing its text.

```python
import metapat

print(metapat.CANON_VERSION)
print(metapat.canon_digest())
```

A digest is identity evidence, not empirical validation or formal proof of the ontology.

## Immutable semantic module envelope

`MetapatModuleEnvelope` carries semantic authority and provenance only:

- schema id and version;
- module id and kind;
- canon version and digest;
- exact source statement references and exact statement text;
- bounded constraints;
- permitted interpretations;
- unresolved `hmmm` fields;
- deterministic provenance digest.

```python
import metapat

module = metapat.root_spine_module_envelope()
serialized = module.to_json()
roundtrip = metapat.MetapatModuleEnvelope.from_json(serialized)
assert roundtrip == module
```

The envelope contains no EDCM metric values. Changing canon identity or semantic constraints changes its provenance digest rather than silently rewriting historical output.

## Actual UCNS adapter

METAPAT no longer defines a local `UCNSObject`, normalization, carrier calculation, or composition algebra. `metapat.ucns` lazily imports the actual `ucns` package only when adaptation is requested.

```python
import metapat
import ucns

envelope = metapat.root_spine_module_envelope()
adaptation = metapat.adapt_envelope_to_ucns(envelope)

assert isinstance(adaptation.ucns_object, ucns.UCNSObject)
assert adaptation.record.ucns_object_hash == ucns.stable_hash(adaptation.ucns_object)
assert adaptation.record.canon_digest == envelope.canon_digest
assert adaptation.record.source_statement_refs == envelope.source_statement_refs
assert adaptation.record.theorem_status_transfer is False
```

Current semantic mapping is explicitly:

```text
external-provenance
```

METAPAT statement text is not inserted into UCNS payloads. Whether statements should eventually map to payloads, tags, or remain external provenance is preserved as `hmmm`.

## Canon contract checks

The compatibility module `metapat.validation` contains deterministic **canon contract checks**, not theorem validators.

```python
from metapat import registration_is_not_time

assert registration_is_not_time(({"t": 0}, {"t": 1}), None)
```

A `True` result means supplied Python values satisfy the encoded condition. It does not establish external truth, empirical validity, consciousness, intent, or formal proof. See [`docs/claims-ledger.md`](docs/claims-ledger.md).

## Current canon map

- [`CHAPTER_ZERO.md`](CHAPTER_ZERO.md) — canonical chapter.
- [`AXIOMS.md`](AXIOMS.md) — invariant root and primitive extension.
- [`POSTULATES.md`](POSTULATES.md) — allowed working claims.
- [`THEOREMS.md`](THEOREMS.md) — internal derivations and proof sketches, classified in the claims ledger.
- [`THEORIES.md`](THEORIES.md) — application families that do not redefine root.
- [`DOMAIN_RESTRAINT.md`](DOMAIN_RESTRAINT.md) — domain-import boundary.
- [`GLOSSARY.md`](GLOSSARY.md) — term meanings and status.
- [`docs/claims-ledger.md`](docs/claims-ledger.md) — public claim classification.
- [`UCNS_IMPLEMENTATION.md`](UCNS_IMPLEMENTATION.md) — actual adapter scope and limits.
- [`codex-handoff/2026-07-12-stack-repair/`](codex-handoff/2026-07-12-stack-repair/) — repair requirements and completion evidence.

## Repository rule

```text
No implementation owns the root.
```

`skill-lib`, `ucns`, `edcmbone`, `edcm`, `a0`, `a0p`, AIMMH, and other repositories may consume, apply, test, or represent METAPAT. They do not define it.

## hmmm

The EDCM consumer and full shared UCNS/METAPAT/EDCM contract fixture remain to be merged downstream. The semantic payload/tag/external-provenance choice remains unresolved and must not be silently selected by a constructor convenience.
