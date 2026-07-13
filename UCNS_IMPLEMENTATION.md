# Actual UCNS adapter

METAPAT does not implement UCNS algebra.

The optional adapter lives at `src/metapat/ucns.py` and is tested by `tests/test_ucns_bridge.py`.

## Scope

The adapter converts a versioned immutable `MetapatModuleEnvelope` into actual geometry from the canonical `ucns` package.

Base METAPAT remains importable without UCNS installed. Adapter calls without the optional dependency raise a clear `UCNSDependencyError`; no local substitute is created.

## Implemented behavior

1. Validate the actual UCNS public surface.
2. Derive deterministic geometry from ordered source-statement count.
3. Construct a real `ucns.UCNSObject`.
4. Keep all UCNS payloads unit (`None`).
5. Record the actual UCNS stable hash and serialization version.
6. Preserve module id, kind, canon identity, envelope provenance digest, exact source references, exact statements, constraints, permitted interpretations, and unresolved `hmmm` fields in a separate strict adaptation record.
7. Serialize and reconstruct that record without coercing malformed fields.
8. Delegate composition only to actual `ucns.multiply`.
9. Mark theorem-status transfer and METAPAT-validity claims as false.

## Usage

```python
import metapat
import ucns

envelope = metapat.root_spine_module_envelope()
adaptation = metapat.adapt_envelope_to_ucns(envelope)

assert isinstance(adaptation.ucns_object, ucns.UCNSObject)
assert adaptation.record.ucns_object_hash == ucns.stable_hash(adaptation.ucns_object)
assert adaptation.record.canon_digest == envelope.canon_digest
assert adaptation.record.envelope_provenance_digest == envelope.provenance_digest
assert adaptation.record.constraints == envelope.constraints
assert adaptation.record.permitted_interpretations == envelope.permitted_interpretations
assert metapat.UCNSAdaptationRecord.from_json(adaptation.record.to_json()) == adaptation.record
```

Install the optional integration with:

```bash
python -m pip install -e .[ucns]
```

## Geometry convention

For an envelope containing `n` ordered source statements, the adapter constructs `n` evenly spaced anchors using UCNS half-turn angles:

```text
angle_i = 2i / n
```

It declares `n_dec = n_min = n`, supplies unit payloads, and defaults every face bit to `0` unless the caller explicitly supplies a same-length sequence of integer binary values. Boolean values are rejected rather than silently accepted as integers.

This is an adapter contract, not a METAPAT claim that statement order or count exhausts semantic geometry.

## Semantic boundary

Current mapping:

```text
semantic_mapping = external-provenance
```

The envelope and adaptation record retain:

- exact statement references;
- exact statement text;
- constraints;
- permitted interpretations;
- unresolved constraints;
- canon version and digest;
- envelope provenance digest.

None of these fields are silently placed into UCNS payloads or assigned UCNS mathematical meaning.

## Removed local algebra

The following former METAPAT-native surfaces are retired:

- local `UCNSObject`;
- local `AnchorPayload`;
- local normalization and carrier calculation;
- local object factory;
- local statement-to-payload encoding;
- local XOR product/composition;
- recursive Chapter Zero UCNS payload construction.

METAPAT may not reproduce these operations under new names. Geometry belongs to UCNS.

## Gonol constants

The existing project constants remain declarative:

```text
GONOL_VERTEX_COUNT = 157
SPACE_ANCHOR_VERTEX = 0
ADDRESSABLE_GONOL_VERTICES = 156
```

They do not define a local UCNS vertex algebra or symbolic table.

## Proof and validity firewall

Successful adaptation establishes only that:

- the envelope passed strict schema checks;
- actual UCNS constructed the object;
- the stable hash and complete provenance were recorded.

It does not establish:

- METAPAT ontology validity;
- EDCM measurement validity;
- empirical truth;
- a concrete UCNS negative certification;
- transfer of UCNS theorem status.

## hmmm

Whether any METAPAT statement should eventually map to UCNS payloads, tags, or remain external provenance is unresolved. The current adapter intentionally chooses no payload semantics while preserving that unresolved question in every canonical root-spine envelope.
