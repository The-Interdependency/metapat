"""Contracts for the optional adapter to the actual UCNS package."""

from __future__ import annotations

from types import ModuleType

import pytest

import metapat
import metapat.ucns as adapter_module
from metapat import (
    ADDRESSABLE_GONOL_VERTICES,
    GONOL_VERTEX_COUNT,
    SPACE_ANCHOR_VERTEX,
    UCNSAdapterError,
    UCNSDependencyError,
    adapt_envelope_to_ucns,
    compose,
    root_spine_module_envelope,
)


def test_gonol_space_anchor_constants() -> None:
    assert GONOL_VERTEX_COUNT == 157
    assert SPACE_ANCHOR_VERTEX == 0
    assert ADDRESSABLE_GONOL_VERTICES == 156


def test_metapat_exports_no_local_ucns_algebra() -> None:
    assert not hasattr(metapat, "UCNSObject")
    assert not hasattr(metapat, "AnchorPayload")
    assert not hasattr(adapter_module, "minimal_gonal_order")
    assert not hasattr(adapter_module, "make_ucns_object")


def test_direct_missing_ucns_raises_clear_dependency_error(monkeypatch) -> None:
    def missing(name: str):
        raise ModuleNotFoundError("No module named 'ucns'", name="ucns")

    monkeypatch.setattr(adapter_module.importlib, "import_module", missing)
    with pytest.raises(UCNSDependencyError, match="optional UCNS integration"):
        adapter_module.require_ucns()


def test_transitive_import_failure_is_not_hidden(monkeypatch) -> None:
    def broken(name: str):
        raise ModuleNotFoundError("No module named 'ucns_helper'", name="ucns_helper")

    monkeypatch.setattr(adapter_module.importlib, "import_module", broken)
    with pytest.raises(ModuleNotFoundError, match="ucns_helper"):
        adapter_module.require_ucns()


def test_importable_malformed_ucns_fails_adapter_validation(monkeypatch) -> None:
    malformed = ModuleType("ucns")
    malformed.UCNSObject = object
    monkeypatch.setattr(adapter_module.importlib, "import_module", lambda name: malformed)
    with pytest.raises(UCNSAdapterError, match="multiply"):
        adapter_module.require_ucns()


def test_root_spine_adapts_to_actual_ucns_object() -> None:
    ucns = pytest.importorskip("ucns")
    adaptation = adapt_envelope_to_ucns(root_spine_module_envelope())
    obj = adaptation.ucns_object

    assert isinstance(obj, ucns.UCNSObject)
    assert obj.n_min == 5
    assert len(obj.A_plus) == 5
    assert tuple(obj.F_plus) == (0, 0, 0, 0, 0)
    assert all(payload is None for _, payload in obj.A_plus)
    assert adaptation.record.ucns_object_hash == ucns.stable_hash(obj)
    assert adaptation.record.ucns_serialization_version == ucns.CANONICAL_SERIALIZATION_VERSION


def test_adaptation_preserves_semantic_provenance() -> None:
    pytest.importorskip("ucns")
    envelope = root_spine_module_envelope()
    record = adapt_envelope_to_ucns(envelope).record

    assert record.canon_version == envelope.canon_version
    assert record.canon_digest == envelope.canon_digest
    assert record.envelope_provenance_digest == envelope.provenance_digest
    assert record.source_statement_refs == envelope.source_statement_refs
    assert record.source_statements == envelope.source_statements
    assert record.unresolved_constraints == envelope.unresolved_constraints
    assert record.semantic_mapping == "external-provenance"


def test_adaptation_does_not_transfer_theorem_status() -> None:
    pytest.importorskip("ucns")
    record = adapt_envelope_to_ucns(root_spine_module_envelope()).record
    assert record.theorem_status_transfer is False
    assert record.metapat_validity_claim is False


def test_face_bits_fail_closed() -> None:
    pytest.importorskip("ucns")
    envelope = root_spine_module_envelope()
    with pytest.raises(ValueError, match="length"):
        adapt_envelope_to_ucns(envelope, face_bits=(0,))
    with pytest.raises(ValueError, match="integer face bits"):
        adapt_envelope_to_ucns(envelope, face_bits=(0, 0, 2, 0, 0))


def test_compose_delegates_to_actual_ucns() -> None:
    ucns = pytest.importorskip("ucns")
    left = adapt_envelope_to_ucns(root_spine_module_envelope()).ucns_object
    right = adapt_envelope_to_ucns(root_spine_module_envelope()).ucns_object
    result = compose(left, right)
    assert isinstance(result, ucns.UCNSObject)
    assert result == ucns.multiply(left, right)
