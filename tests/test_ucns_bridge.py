from __future__ import annotations

import pytest

import metapat
import metapat.ucns as adapter_module
from metapat import (
    ADDRESSABLE_GONOL_VERTICES,
    GONOL_VERTEX_COUNT,
    SPACE_ANCHOR_VERTEX,
    UCNSAdapterError,
    UCNSAdaptationRecord,
    UCNSDependencyError,
    adapt_envelope_to_ucns,
    root_spine_module_envelope,
)


def test_base_metapat_and_declared_constants_remain_available() -> None:
    assert metapat.root_spine()
    assert metapat.canonical_semantic_catalog()
    assert GONOL_VERTEX_COUNT == 157
    assert SPACE_ANCHOR_VERTEX == 0
    assert ADDRESSABLE_GONOL_VERTICES == 156


def test_no_local_ucns_object_or_algebra_is_exported() -> None:
    assert not hasattr(metapat, "UCNSObject")
    assert not hasattr(adapter_module, "UCNSObject")
    assert not hasattr(adapter_module, "AnchorPayload")
    assert not hasattr(adapter_module, "multiply")
    assert not hasattr(adapter_module, "stable_hash")


def test_installed_package_name_cannot_activate(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(adapter_module, "_package_present", lambda: True)
    status = adapter_module.ucns_consumer_status()
    assert status.package_present is True
    assert status.producer_recognized is False
    assert status.profile_supported is False
    assert status.adapter_active is False


def test_require_ucns_fails_at_post_reset_profile_boundary() -> None:
    with pytest.raises(UCNSDependencyError, match="awaiting post-reset producer profile"):
        adapter_module.require_ucns()


def test_adaptation_request_fails_closed_without_constructing_geometry() -> None:
    envelope = root_spine_module_envelope()
    with pytest.raises(UCNSAdapterError, match="awaiting post-reset producer profile"):
        adapt_envelope_to_ucns(envelope)


def test_semantic_envelope_record_remains_usable_without_geometry() -> None:
    envelope = root_spine_module_envelope()
    record = adapter_module.suspended_envelope_record(envelope)
    assert record.source_statement_refs == envelope.source_statement_refs
    assert record.source_statements == envelope.source_statements
    assert record.canon_digest == envelope.canon_digest
    assert record.constraints == envelope.constraints
    assert record.permitted_interpretations == envelope.permitted_interpretations
    assert record.semantic_mapping == "external-provenance"
    assert record.activation_status == "suspended"
    assert record.theorem_status_transfer is False
    assert record.measurement_validity_claim is False
    assert record.metapat_validity_claim is False
    assert record.unresolved_constraints[-1].startswith("awaiting post-reset")


def test_statement_order_and_repetition_survive_suspended_record() -> None:
    envelope = root_spine_module_envelope()
    record = adapter_module.suspended_envelope_record(envelope)
    assert list(zip(record.source_statement_refs, record.source_statements)) == list(
        zip(envelope.source_statement_refs, envelope.source_statements)
    )


def test_suspended_record_round_trip_is_deterministic() -> None:
    record = adapter_module.suspended_envelope_record(root_spine_module_envelope())
    reconstructed = UCNSAdaptationRecord.from_json(record.to_json())
    assert reconstructed == record
    assert reconstructed.to_json() == record.to_json()


def test_legacy_schema_ids_are_pre_reset() -> None:
    assert "metapat-actual-ucns-adapter-v1" in adapter_module.REJECTED_LEGACY_SCHEMAS
    assert "ucns-canonical-json-v1" in adapter_module.REJECTED_LEGACY_SCHEMAS
