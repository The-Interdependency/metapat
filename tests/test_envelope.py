from __future__ import annotations

import json

import pytest

from metapat import (
    ROOT_SPINE,
    MetapatModuleEnvelope,
    build_module_envelope,
    canon_digest,
    canonical_canon_data,
    root_spine_module_envelope,
)


def test_canon_digest_is_deterministic() -> None:
    first = canon_digest()
    second = canon_digest()
    assert first == second
    assert len(first) == 64
    assert canonical_canon_data()["root_spine"] == list(ROOT_SPINE)


def test_root_spine_envelope_preserves_exact_sources_and_constraints() -> None:
    envelope = root_spine_module_envelope()
    assert envelope.module_id == "metapat.root_spine"
    assert envelope.module_kind == "simplex"
    assert envelope.source_statements == ROOT_SPINE
    assert len(envelope.source_statement_refs) == len(ROOT_SPINE)
    assert envelope.canon_digest == canon_digest()
    assert envelope.provenance_digest
    assert any(value.startswith("hmmm:") for value in envelope.unresolved_constraints)


def test_envelope_roundtrip_preserves_hmmm() -> None:
    envelope = root_spine_module_envelope()
    reconstructed = MetapatModuleEnvelope.from_json(envelope.to_json())
    assert reconstructed == envelope
    assert reconstructed.to_json() == envelope.to_json()
    assert reconstructed.unresolved_constraints == envelope.unresolved_constraints


def test_canon_or_constraint_rotation_changes_provenance() -> None:
    original = root_spine_module_envelope()
    rotated_canon = build_module_envelope(
        module_id=original.module_id,
        module_kind=original.module_kind,
        source_statement_refs=original.source_statement_refs,
        source_statements=original.source_statements,
        constraints=original.constraints,
        permitted_interpretations=original.permitted_interpretations,
        unresolved_constraints=original.unresolved_constraints,
        canon_version="metapat-canon-v2-test",
        canon_identity="0" * 64,
    )
    changed_constraint = build_module_envelope(
        module_id=original.module_id,
        module_kind=original.module_kind,
        source_statement_refs=original.source_statement_refs,
        source_statements=original.source_statements,
        constraints=(*original.constraints, "Test-only changed constraint."),
        permitted_interpretations=original.permitted_interpretations,
        unresolved_constraints=original.unresolved_constraints,
    )
    assert rotated_canon.provenance_digest != original.provenance_digest
    assert changed_constraint.provenance_digest != original.provenance_digest


def test_envelope_contains_no_measurement_values() -> None:
    data = root_spine_module_envelope().to_dict()
    forbidden = {
        "measurements",
        "measured_values",
        "metric_values",
        "edcm_readouts",
        "measurement_validity",
        "theorem_status",
    }
    assert forbidden.isdisjoint(data)


def test_tampered_provenance_digest_fails_closed() -> None:
    data = root_spine_module_envelope().to_dict()
    data["constraints"] = [*data["constraints"], "tampered"]
    with pytest.raises(ValueError, match="provenance_digest"):
        MetapatModuleEnvelope.from_dict(data)


def test_unknown_schema_field_fails_closed() -> None:
    data = root_spine_module_envelope().to_dict()
    data["measured_value"] = 1
    with pytest.raises(ValueError, match="unknown envelope fields"):
        MetapatModuleEnvelope.from_dict(data)


def test_serialized_envelope_is_canonical_json() -> None:
    encoded = root_spine_module_envelope().to_json()
    assert json.dumps(json.loads(encoded), ensure_ascii=False, sort_keys=True, separators=(",", ":")) == encoded
