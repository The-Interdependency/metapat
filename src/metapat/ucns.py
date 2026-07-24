"""Fail-closed METAPAT consumer boundary for post-reset UCNS profiles.

UCNS is a stable identifier without a canonical expansion.  This module preserves
METAPAT semantic envelopes without constructing or imitating UCNS objects.
"""
from __future__ import annotations

import importlib.util
import json
from dataclasses import asdict, dataclass
from typing import Any, Mapping

from .envelope import MetapatModuleEnvelope, root_spine_module_envelope

GONOL_VERTEX_COUNT = 157
SPACE_ANCHOR_VERTEX = 0
ADDRESSABLE_GONOL_VERTICES = GONOL_VERTEX_COUNT - 1
UCNS_ADAPTER_SCHEMA = "metapat-ucns-profile-consumer-suspended-v2"
UCNS_ADAPTER_VERSION = "2.0.0"
RESET_BOUNDARY_REASON = (
    "awaiting post-reset producer profile, reviewed handoff, and exact UCNS source commit"
)
REJECTED_LEGACY_SCHEMAS = frozenset(
    {
        "metapat-actual-ucns-adapter-v1",
        "ucns-canonical-json-v1",
        "ucns.bridge-record@1.0.0",
        "ucns.factorization-evidence@1.0.0",
    }
)


class UCNSDependencyError(RuntimeError):
    """Raised when profile consumption is requested while activation is suspended."""


class UCNSAdapterError(RuntimeError):
    """Raised when a consumer request crosses the reset/profile boundary."""


@dataclass(frozen=True, slots=True)
class UCNSConsumerStatus:
    package_present: bool
    producer_recognized: bool = False
    profile_supported: bool = False
    adapter_active: bool = False
    supported_producer_epoch: str | None = None
    supported_profile: tuple[str, str] | None = None
    supported_bridge_schema: tuple[str, str] | None = None
    pinned_ucns_commit: str | None = None
    reason: str = RESET_BOUNDARY_REASON
    theorem_status_transfer: bool = False
    measurement_validity: bool = False
    metapat_validity: bool = False

    def as_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class UCNSAdaptationRecord:
    """Suspended deterministic record retaining METAPAT provenance only."""

    adapter_schema: str
    adapter_version: str
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
    activation_status: str = "suspended"
    semantic_mapping: str = "external-provenance"
    theorem_status_transfer: bool = False
    measurement_validity_claim: bool = False
    metapat_validity_claim: bool = False

    def __post_init__(self) -> None:
        if self.adapter_schema != UCNS_ADAPTER_SCHEMA or self.adapter_version != UCNS_ADAPTER_VERSION:
            raise ValueError("unsupported suspended adapter identity")
        if self.activation_status != "suspended":
            raise ValueError("adapter activation must remain suspended")
        if self.semantic_mapping != "external-provenance":
            raise ValueError("semantic text must remain external provenance")
        if self.theorem_status_transfer or self.measurement_validity_claim or self.metapat_validity_claim:
            raise ValueError("validity or theorem status cannot transfer")
        if len(self.source_statement_refs) != len(self.source_statements):
            raise ValueError("source refs and statements must preserve equal ordered occurrence counts")

    def to_dict(self) -> dict[str, Any]:
        data = asdict(self)
        for key in (
            "source_statement_refs",
            "source_statements",
            "constraints",
            "permitted_interpretations",
            "unresolved_constraints",
        ):
            data[key] = list(data[key])
        return data

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, sort_keys=True, separators=(",", ":"))

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "UCNSAdaptationRecord":
        values = dict(data)
        for key in (
            "source_statement_refs",
            "source_statements",
            "constraints",
            "permitted_interpretations",
            "unresolved_constraints",
        ):
            values[key] = tuple(values[key])
        return cls(**values)

    @classmethod
    def from_json(cls, text: str) -> "UCNSAdaptationRecord":
        value = json.loads(text)
        if not isinstance(value, Mapping):
            raise ValueError("adaptation record JSON must contain an object")
        return cls.from_dict(value)


@dataclass(frozen=True, slots=True)
class UCNSAdaptation:
    """Compatibility container; no UCNS object can exist while suspended."""

    ucns_object: None
    record: UCNSAdaptationRecord
    status: UCNSConsumerStatus


def _package_present() -> bool:
    try:
        return importlib.util.find_spec("ucns") is not None
    except (ImportError, AttributeError, ValueError):
        return False


def ucns_consumer_status() -> UCNSConsumerStatus:
    return UCNSConsumerStatus(package_present=_package_present())


def require_ucns() -> None:
    raise UCNSDependencyError(RESET_BOUNDARY_REASON)


def _suspended_record(envelope: MetapatModuleEnvelope) -> UCNSAdaptationRecord:
    return UCNSAdaptationRecord(
        adapter_schema=UCNS_ADAPTER_SCHEMA,
        adapter_version=UCNS_ADAPTER_VERSION,
        envelope_schema_id=envelope.schema_id,
        envelope_schema_version=envelope.schema_version,
        envelope_provenance_digest=envelope.provenance_digest,
        canon_version=envelope.canon_version,
        canon_digest=envelope.canon_digest,
        module_id=envelope.module_id,
        module_kind=envelope.module_kind,
        source_statement_refs=tuple(envelope.source_statement_refs),
        source_statements=tuple(envelope.source_statements),
        constraints=tuple(envelope.constraints),
        permitted_interpretations=tuple(envelope.permitted_interpretations),
        unresolved_constraints=tuple((*envelope.unresolved_constraints, RESET_BOUNDARY_REASON)),
    )


def suspended_envelope_record(envelope: MetapatModuleEnvelope) -> UCNSAdaptationRecord:
    """Retain semantic provenance deterministically without geometry construction."""
    return _suspended_record(envelope)


def adapt_envelope_to_ucns(envelope: MetapatModuleEnvelope, *args: Any, **kwargs: Any) -> UCNSAdaptation:
    del args, kwargs
    _suspended_record(envelope)
    raise UCNSAdapterError(RESET_BOUNDARY_REASON)


def root_spine_adaptation(*args: Any, **kwargs: Any) -> UCNSAdaptation:
    return adapt_envelope_to_ucns(root_spine_module_envelope(), *args, **kwargs)


def root_spine_ucns(*args: Any, **kwargs: Any) -> None:
    del args, kwargs
    raise UCNSAdapterError(RESET_BOUNDARY_REASON)


def compose(*objects: Any) -> None:
    del objects
    raise UCNSAdapterError(RESET_BOUNDARY_REASON)


__all__ = [
    "ADDRESSABLE_GONOL_VERTICES",
    "GONOL_VERTEX_COUNT",
    "REJECTED_LEGACY_SCHEMAS",
    "RESET_BOUNDARY_REASON",
    "SPACE_ANCHOR_VERTEX",
    "UCNS_ADAPTER_SCHEMA",
    "UCNS_ADAPTER_VERSION",
    "UCNSAdapterError",
    "UCNSAdaptation",
    "UCNSAdaptationRecord",
    "UCNSConsumerStatus",
    "UCNSDependencyError",
    "adapt_envelope_to_ucns",
    "compose",
    "require_ucns",
    "root_spine_adaptation",
    "root_spine_ucns",
    "suspended_envelope_record",
    "ucns_consumer_status",
]
