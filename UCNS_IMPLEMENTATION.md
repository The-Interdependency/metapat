# Actual UCNS adapter

METAPAT does not implement UCNS algebra.

The optional adapter lives at `src/metapat/ucns.py` and is tested by `tests/test_ucns_bridge.py`. Semantic fork authorization lives separately at `src/metapat/ucns_phi.py` and is tested by `tests/test_ucns_phi.py`.

## Scope

The adapter converts a versioned immutable `MetapatModuleEnvelope` into actual geometry from the canonical `ucns` package.

Base METAPAT remains importable without UCNS installed. Adapter calls without the optional dependency raise a clear `UCNSDependencyError`; no local substitute is created.

## Implemented adapter behavior

1. Validate the actual UCNS public surface.
2. Create one unit-payload UCNS cell per ordered source-statement occurrence and retain each source reference as cell provenance.
3. Construct a real `ucns.UCNSObject`.
4. Keep all UCNS payloads unit (`None`).
5. Record the exact producer epoch, profile, bridge schema, source commit, bridge JSON, and bridge stable identity.
6. Preserve module id, kind, canon identity, envelope provenance digest, exact source references, exact statements, constraints, permitted interpretations, and unresolved `hmmm` fields in a separate strict adaptation record.
7. Serialize and reconstruct that record without coercing malformed fields.
8. Reject archived face-bit inputs and universal composition requests under this ordered-occurrence profile.
9. Mark theorem-status transfer and METAPAT-validity claims as false.

## Usage

```python
import metapat
import ucns

envelope = metapat.root_spine_module_envelope()
adaptation = metapat.adapt_envelope_to_ucns(envelope)
bridge = ucns.EdcmMetapatBridgeRecord.from_json_bytes(
    adaptation.record.ucns_bridge_json.encode("utf-8")
)

assert isinstance(adaptation.ucns_object, ucns.UCNSObject)
assert adaptation.record.ucns_stable_identity == bridge.stable_identity
assert adaptation.record.adapter_version == "2.0.0"
assert adaptation.record.envelope_schema_version == "2.0.0"
assert adaptation.record.canon_digest == envelope.canon_digest
assert adaptation.record.envelope_provenance_digest == envelope.provenance_digest
assert adaptation.record.constraints == envelope.constraints
assert adaptation.record.permitted_interpretations == envelope.permitted_interpretations
assert metapat.UCNSAdaptationRecord.from_json(adaptation.record.to_json()) == adaptation.record
```

Install the optional integration with:

```bash
python -m pip install "git+https://github.com/The-Interdependency/ucns.git@19f1afddb993f7d933ac8727627e7d5e1c3b88fc"
python -m pip install -e .[dev]
```

## Ordered-occurrence convention

For an envelope containing `n` ordered source statements, the adapter constructs `n` `ucns.Cell` values in the same order:

```text
payload = None
provenance = {"source_ref": matching_source_statement_ref}
```

Those cells are passed to the pinned producer's `make_carrier` and ordered-occurrence profile. Face bits and universal composition belong to archived adapters and are rejected.

This is an adapter contract, not a METAPAT claim that statement order or count exhausts semantic geometry.

## Default semantic boundary

The adapter mapping remains:

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

Adaptation-record wire `2.0.0` validates all of those embedded envelope identities against the current v4 parser epoch. It rejects outer wire `1.0.0`, envelope schema `1.2.0`, non-current canon identity, provenance tampering, unknown fields, and malformed sequence fields rather than treating any of them as implicit migration.

None of these fields are silently placed into UCNS payloads or assigned UCNS mathematical meaning. The adapter does not infer semantic meaning from a payload, tag, cell, path, carrier, symmetry, or object shape.

## Explicit Phi semantic authority

METAPAT has ratified one semantic exception without altering the adapter: an explicit, canon-bound `UCNSForkAuthorization` may declare ordered children to be simultaneous constitutive components of one parent.

```text
default semantic mapping: external-provenance
fork mode: explicit-authorization-only
allowed relation: constitutive-simultaneous
```

The authorization binds:

- parent semantic module identity;
- ordered child semantic module identities;
- exact source statement references;
- METAPAT canon digest;
- Phi policy version;
- unresolved constraints;
- deterministic authorization digest.

It refuses to treat temporal succession, adjacency, provenance, alternatives, fiq connectivity, external symmetry action, or arbitrary association as payload containment.

This producer authorization is necessary but not sufficient for an encoded UCNS fixture. A downstream integration must separately bind the exact UCNS parent object, payload-bearing cell or path, ordered child stable hashes, authorization digest, and encoding-policy version. See `docs/ucns-phi-policy.md`.

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

- the envelope and adaptation record passed strict current-epoch schema, canon, and provenance checks;
- actual UCNS constructed the object;
- the bridge stable identity and complete provenance were recorded.

A valid Phi authorization establishes only that METAPAT explicitly declared one ordered constitutive-simultaneous semantic relation under the named canon and policy.

Neither establishes:

- METAPAT ontology validity;
- EDCM measurement validity;
- empirical truth;
- a concrete UCNS negative certification;
- correct downstream payload topology;
- transfer of UCNS theorem status.

## hmmm

The topology-binding schema and fail-closed linter for the first actual constitutive-fork fixture remain downstream work. Any payload or tag semantics beyond explicit constitutive-simultaneous authorization remain unresolved; the adapter intentionally continues to use unit payloads and external provenance.
