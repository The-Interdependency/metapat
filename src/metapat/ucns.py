"""Optional adapter from METAPAT semantic envelopes to the actual UCNS package.

This module contains no UCNS algebra. It constructs actual UCNS objects only
when the optional dependency is present and keeps the complete METAPAT semantic
envelope boundary in a separately serializable adaptation record.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: metapat_ucns_adapter
#   module_name: metapat.ucns
#   module_kind: adapter
#   summary: adapts immutable METAPAT semantic envelopes into actual ucns.UCNSObject instances without duplicating UCNS algebra or losing semantic provenance
#   owner: The Interdependency
#   public_surface: GONOL_VERTEX_COUNT, SPACE_ANCHOR_VERTEX, ADDRESSABLE_GONOL_VERTICES, UCNSDependencyError, UCNSAdapterError, UCNSAdaptationRecord, UCNSAdaptation, require_ucns, adapt_envelope_to_ucns, root_spine_adaptation, root_spine_ucns, compose
#   internal_surface: _module_version, _angles_for_statement_count, _canonical_json, _require_record_string, _require_record_sequence
#   auth_boundary: none
#   storage_boundary: serialization-only
#   network_boundary: package import only; no network performed by runtime code
#   user_data_boundary: exact envelope statements and interpretation fields remain external provenance and are not placed into UCNS payloads
#   admin_only: false
#   tests: tests.test_ucns_bridge, tests.test_envelope, tests.test_packaging
#   rollout: optional_integration
#   rollback: remove adapter exports; base canon and envelope remain importable
#   requires: optional external ucns package, metapat_module_envelope
#   since: 2026-07-12
#   unresolved: whether statements should later map to UCNS tags, payloads, or remain external provenance
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_ucns_adapter_docs
#   summary: documents the actual-UCNS adapter and complete external-provenance boundary
#   audience: developer
#   source: UCNS_IMPLEMENTATION.md
#   covers: adapt_envelope_to_ucns, UCNSAdaptationRecord, strict record serialization, dependency and theorem-status boundaries
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_actual_ucns_adapter
#   summary: constructs actual UCNS geometry from statement count while retaining the complete METAPAT semantic envelope in a separate provenance record
#   exposes: metapat.ucns.adapt_envelope_to_ucns
#   inputs: MetapatModuleEnvelope, optional face bits
#   outputs: actual ucns.UCNSObject plus serializable UCNSAdaptationRecord
#   boundaries: auth:none, storage:serialization-only, network:none, user_data:semantic text remains provenance-only
# === END CAPABILITIES ===

# === BOUNDARIES ===
# id: metapat_ucns_adapter_boundary
#   summary: UCNS provides geometry only; METAPAT owns semantic authority; no theorem or empirical status transfer
#   auth_boundary: none
#   storage_boundary: serialization-only
#   network_boundary: none
#   user_data_boundary: all source and interpretation fields remain in the METAPAT envelope and adaptation record
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: metapat_ucns_constants_declarative
#   given: public gonol constants are imported
#   then: they retain the declared 157, 0, and 156 values without defining a local vertex algebra
#   class: canon_contract
#
# id: metapat_ucns_no_local_algebra
#   given: METAPAT public and adapter surfaces are inspected
#   then: no local UCNSObject, payload class, normalization, carrier, or object factory is exported
#   class: boundary_contract
#
# id: metapat_ucns_missing_dependency_clear
#   given: actual UCNS adaptation is requested while the ucns package is directly absent
#   then: a clear UCNSDependencyError is raised and no substitute algebra is created
#   class: safety
#
# id: metapat_ucns_transitive_failure_visible
#   given: importing ucns fails because one of its own dependencies is absent
#   then: the transitive ModuleNotFoundError remains visible rather than being mislabeled as direct UCNS absence
#   class: safety
#
# id: metapat_ucns_surface_validated
#   given: an importable ucns module lacks a required public surface
#   then: adapter validation fails before adaptation
#   class: integration_contract
#
# id: metapat_actual_ucns_object
#   given: UCNS is installed and a valid METAPAT envelope is adapted
#   then: the returned object is an actual ucns.UCNSObject and its stable hash is recorded
#   class: integration_contract
#
# id: metapat_ucns_provenance_survives
#   given: a semantic envelope is adapted
#   then: canon identity, exact statements and references, constraints, permitted interpretations, and unresolved hmmm survive outside UCNS payload meaning
#   class: provenance_contract
#
# id: metapat_ucns_no_theorem_transfer
#   given: any successful adaptation
#   then: theorem_status_transfer and metapat_validity_claim remain false
#   class: boundary_contract
#
# id: metapat_ucns_face_bits_fail_closed
#   given: face bits are the wrong length or contain non-binary values
#   then: adaptation rejects them before object construction
#   class: safety
#
# id: metapat_ucns_composition_delegated
#   given: two actual UCNS objects are composed
#   then: composition delegates exactly to ucns.multiply
#   class: integration_contract
#
# id: metapat_ucns_record_roundtrip
#   given: an adaptation record is serialized and reconstructed
#   then: every provenance and boundary field survives exactly and malformed records fail closed
#   class: schema_contract
# === END CONTRACTS ===

import importlib
import importlib.metadata
import json
from dataclasses import dataclass
from fractions import Fraction
from types import ModuleType
from typing import Any, Iterable, Mapping

from .envelope import MetapatModuleEnvelope, root_spine_module_envelope

GONOL_VERTEX_COUNT = 157
SPACE_ANCHOR_VERTEX = 0
ADDRESSABLE_GONOL_VERTICES = GONOL_VERTEX_COUNT - 1
UCNS_ADAPTER_SCHEMA = "metapat-actual-ucns-adapter-v1"
UCNS_ADAPTER_VERSION = "1.1.0"

UCNS_INSTALL_HINT = (
    "Install the optional UCNS integration with `python -m pip install -e .[ucns]` "
    "or install The-Interdependency/ucns directly."
)


class UCNSDependencyError(ModuleNotFoundError):
    """Raised when actual UCNS adaptation is requested without UCNS installed."""


class UCNSAdapterError(RuntimeError):
    """Raised when UCNS or an adaptation record violates the required contract."""


def _canonical_json(data: Mapping[str, Any]) -> str:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def _require_record_string(data: Mapping[str, Any], name: str) -> str:
    value = data[name]
    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string")
    return value


def _require_record_sequence(data: Mapping[str, Any], name: str) -> tuple[str, ...]:
    value = data[name]
    if not isinstance(value, (list, tuple)):
        raise ValueError(f"{name} must be an array of strings")
    result = tuple(value)
    if any(not isinstance(item, str) or not item.strip() for item in result):
        raise ValueError(f"{name} must contain only non-empty strings")
    return result


@dataclass(frozen=True, slots=True)
class UCNSAdaptationRecord:
    """Complete semantic provenance retained outside UCNS payload meaning."""

    adapter_schema: str
    adapter_version: str
    ucns_package_version: str | None
    ucns_serialization_version: str
    ucns_object_hash: str
    envelope_schema_id: str
    envelope_schema_version: str
    envelope_provenance_digest: str
    canon_version: str
    canon_digest: str
    module_id: str
    module_kind: str
    source_statement_refs: tuple[str, ...]
    source_statements: tuple[str, ...]
    constraints: tuple[str, ...]
    permitted_interpretations: tuple[str, ...]
    unresolved_constraints: tuple[str, ...]
    semantic_mapping: str = "external-provenance"
    theorem_status_transfer: bool = False
    metapat_validity_claim: bool = False

    def __post_init__(self) -> None:
        if self.adapter_schema != UCNS_ADAPTER_SCHEMA:
            raise ValueError(f"unsupported adapter_schema {self.adapter_schema!r}")
        if self.adapter_version != UCNS_ADAPTER_VERSION:
            raise ValueError(f"unsupported adapter_version {self.adapter_version!r}")
        if self.semantic_mapping != "external-provenance":
            raise ValueError("semantic_mapping must remain external-provenance")
        if self.theorem_status_transfer is not False:
            raise ValueError("theorem_status_transfer must be false")
        if self.metapat_validity_claim is not False:
            raise ValueError("metapat_validity_claim must be false")
        for name in (
            "ucns_serialization_version",
            "ucns_object_hash",
            "envelope_schema_id",
            "envelope_schema_version",
            "envelope_provenance_digest",
            "canon_version",
            "canon_digest",
            "module_id",
            "module_kind",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if self.ucns_package_version is not None and not isinstance(self.ucns_package_version, str):
            raise ValueError("ucns_package_version must be a string or null")
        for name in (
            "source_statement_refs",
            "source_statements",
            "constraints",
            "permitted_interpretations",
            "unresolved_constraints",
        ):
            value = getattr(self, name)
            if not isinstance(value, tuple) or any(not isinstance(item, str) or not item.strip() for item in value):
                raise ValueError(f"{name} must be a tuple of non-empty strings")
        if len(self.source_statement_refs) != len(self.source_statements):
            raise ValueError("source_statement_refs and source_statements must have equal length")

    def to_dict(self) -> dict[str, Any]:
        return {
            "adapter_schema": self.adapter_schema,
            "adapter_version": self.adapter_version,
            "ucns_package_version": self.ucns_package_version,
            "ucns_serialization_version": self.ucns_serialization_version,
            "ucns_object_hash": self.ucns_object_hash,
            "envelope_schema_id": self.envelope_schema_id,
            "envelope_schema_version": self.envelope_schema_version,
            "envelope_provenance_digest": self.envelope_provenance_digest,
            "canon_version": self.canon_version,
            "canon_digest": self.canon_digest,
            "module_id": self.module_id,
            "module_kind": self.module_kind,
            "source_statement_refs": list(self.source_statement_refs),
            "source_statements": list(self.source_statements),
            "constraints": list(self.constraints),
            "permitted_interpretations": list(self.permitted_interpretations),
            "unresolved_constraints": list(self.unresolved_constraints),
            "semantic_mapping": self.semantic_mapping,
            "theorem_status_transfer": self.theorem_status_transfer,
            "metapat_validity_claim": self.metapat_validity_claim,
        }

    def to_json(self) -> str:
        return _canonical_json(self.to_dict())

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "UCNSAdaptationRecord":
        if not isinstance(data, Mapping):
            raise ValueError("adaptation record must be a mapping")
        expected = {
            "adapter_schema",
            "adapter_version",
            "ucns_package_version",
            "ucns_serialization_version",
            "ucns_object_hash",
            "envelope_schema_id",
            "envelope_schema_version",
            "envelope_provenance_digest",
            "canon_version",
            "canon_digest",
            "module_id",
            "module_kind",
            "source_statement_refs",
            "source_statements",
            "constraints",
            "permitted_interpretations",
            "unresolved_constraints",
            "semantic_mapping",
            "theorem_status_transfer",
            "metapat_validity_claim",
        }
        unknown = set(data) - expected
        missing = expected - set(data)
        if unknown:
            raise ValueError(f"unknown adaptation record fields: {sorted(unknown)!r}")
        if missing:
            raise ValueError(f"missing adaptation record fields: {sorted(missing)!r}")
        package_version = data["ucns_package_version"]
        if package_version is not None and not isinstance(package_version, str):
            raise ValueError("ucns_package_version must be a string or null")
        if not isinstance(data["theorem_status_transfer"], bool):
            raise ValueError("theorem_status_transfer must be boolean")
        if not isinstance(data["metapat_validity_claim"], bool):
            raise ValueError("metapat_validity_claim must be boolean")
        return cls(
            adapter_schema=_require_record_string(data, "adapter_schema"),
            adapter_version=_require_record_string(data, "adapter_version"),
            ucns_package_version=package_version,
            ucns_serialization_version=_require_record_string(data, "ucns_serialization_version"),
            ucns_object_hash=_require_record_string(data, "ucns_object_hash"),
            envelope_schema_id=_require_record_string(data, "envelope_schema_id"),
            envelope_schema_version=_require_record_string(data, "envelope_schema_version"),
            envelope_provenance_digest=_require_record_string(data, "envelope_provenance_digest"),
            canon_version=_require_record_string(data, "canon_version"),
            canon_digest=_require_record_string(data, "canon_digest"),
            module_id=_require_record_string(data, "module_id"),
            module_kind=_require_record_string(data, "module_kind"),
            source_statement_refs=_require_record_sequence(data, "source_statement_refs"),
            source_statements=_require_record_sequence(data, "source_statements"),
            constraints=_require_record_sequence(data, "constraints"),
            permitted_interpretations=_require_record_sequence(data, "permitted_interpretations"),
            unresolved_constraints=_require_record_sequence(data, "unresolved_constraints"),
            semantic_mapping=_require_record_string(data, "semantic_mapping"),
            theorem_status_transfer=data["theorem_status_transfer"],
            metapat_validity_claim=data["metapat_validity_claim"],
        )

    @classmethod
    def from_json(cls, value: str) -> "UCNSAdaptationRecord":
        if not isinstance(value, str):
            raise ValueError("adaptation record JSON must be a string")
        decoded = json.loads(value)
        if not isinstance(decoded, dict):
            raise ValueError("adaptation record JSON must decode to an object")
        return cls.from_dict(decoded)


@dataclass(frozen=True, slots=True)
class UCNSAdaptation:
    """One actual UCNS object paired with its complete METAPAT provenance."""

    ucns_object: Any
    record: UCNSAdaptationRecord


def require_ucns() -> ModuleType:
    try:
        module = importlib.import_module("ucns")
    except ModuleNotFoundError as exc:
        if exc.name != "ucns":
            raise
        raise UCNSDependencyError(UCNS_INSTALL_HINT, name="ucns") from exc

    required = (
        "UCNSObject",
        "multiply",
        "stable_hash",
        "CANONICAL_SERIALIZATION_VERSION",
    )
    missing = tuple(name for name in required if not hasattr(module, name))
    if missing:
        raise UCNSAdapterError(
            "Importable ucns package is missing required public surfaces: "
            + ", ".join(missing)
        )
    return module


def _module_version(module: ModuleType) -> str | None:
    try:
        return importlib.metadata.version("ucns")
    except importlib.metadata.PackageNotFoundError:
        value = getattr(module, "__version__", None)
        return str(value) if value is not None else None


def _angles_for_statement_count(count: int) -> tuple[Fraction, ...]:
    if count < 1:
        raise ValueError("an envelope must contain at least one source statement")
    return tuple(Fraction(2 * index, count) for index in range(count))


def adapt_envelope_to_ucns(
    envelope: MetapatModuleEnvelope,
    *,
    face_bits: Iterable[int] | None = None,
) -> UCNSAdaptation:
    """Construct actual UCNS geometry while retaining complete provenance."""

    if not isinstance(envelope, MetapatModuleEnvelope):
        raise TypeError("envelope must be a MetapatModuleEnvelope")

    module = require_ucns()
    count = len(envelope.source_statements)
    angles = _angles_for_statement_count(count)
    faces = tuple(0 for _ in range(count)) if face_bits is None else tuple(face_bits)
    if len(faces) != count:
        raise ValueError("face_bits length must match source statement count")
    if any(not isinstance(face, int) or isinstance(face, bool) or face not in (0, 1) for face in faces):
        raise ValueError("face_bits must contain only integer face bits 0 or 1")

    actual_object = module.UCNSObject(
        count,
        count,
        [(angle, None) for angle in angles],
        list(faces),
    )
    record = UCNSAdaptationRecord(
        adapter_schema=UCNS_ADAPTER_SCHEMA,
        adapter_version=UCNS_ADAPTER_VERSION,
        ucns_package_version=_module_version(module),
        ucns_serialization_version=str(module.CANONICAL_SERIALIZATION_VERSION),
        ucns_object_hash=str(module.stable_hash(actual_object)),
        envelope_schema_id=envelope.schema_id,
        envelope_schema_version=envelope.schema_version,
        envelope_provenance_digest=envelope.provenance_digest,
        canon_version=envelope.canon_version,
        canon_digest=envelope.canon_digest,
        module_id=envelope.module_id,
        module_kind=envelope.module_kind,
        source_statement_refs=envelope.source_statement_refs,
        source_statements=envelope.source_statements,
        constraints=envelope.constraints,
        permitted_interpretations=envelope.permitted_interpretations,
        unresolved_constraints=envelope.unresolved_constraints,
    )
    return UCNSAdaptation(actual_object, record)


def root_spine_adaptation() -> UCNSAdaptation:
    return adapt_envelope_to_ucns(root_spine_module_envelope())


def root_spine_ucns() -> Any:
    return root_spine_adaptation().ucns_object


def compose(left: Any, right: Any) -> Any:
    module = require_ucns()
    if not isinstance(left, module.UCNSObject) or not isinstance(right, module.UCNSObject):
        raise TypeError("compose requires actual ucns.UCNSObject operands")
    return module.multiply(left, right)


__all__ = [
    "ADDRESSABLE_GONOL_VERTICES",
    "GONOL_VERTEX_COUNT",
    "SPACE_ANCHOR_VERTEX",
    "UCNS_ADAPTER_SCHEMA",
    "UCNS_ADAPTER_VERSION",
    "UCNSAdapterError",
    "UCNSAdaptation",
    "UCNSAdaptationRecord",
    "UCNSDependencyError",
    "UCNS_INSTALL_HINT",
    "adapt_envelope_to_ucns",
    "compose",
    "require_ucns",
    "root_spine_adaptation",
    "root_spine_ucns",
]
