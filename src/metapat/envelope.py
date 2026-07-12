"""Versioned immutable semantic-authority envelopes for METAPAT consumers.

Usage guidance
--------------
Create envelopes with :func:`build_module_envelope` or use
:func:`root_spine_module_envelope` as the cross-repository fixture. Consumers
may constrain interpretation using the envelope, but must not convert module
labels or statements directly into measured values.

Serialization is deterministic. ``provenance_digest`` binds every semantic and
provenance field except itself. Canon identity is carried separately through
``canon_version`` and ``canon_digest`` so a canon rotation is observable.
"""

# === MODULE_BUILD ===
# id: metapat_module_envelope
#   module_name: metapat.envelope
#   module_kind: schema
#   summary: versioned immutable semantic-authority and provenance envelope for UCNS adapters and EDCM consumers
#   owner: The Interdependency
#   public_surface: MODULE_ENVELOPE_SCHEMA_ID, MODULE_ENVELOPE_SCHEMA_VERSION, MODULE_KINDS, MetapatModuleEnvelope, build_module_envelope, root_spine_module_envelope
#   internal_surface: _canonical_payload, _digest_payload, _tuple_of_strings
#   auth_boundary: none
#   storage_boundary: serialized envelope only; no persistence performed
#   network_boundary: none
#   user_data_boundary: caller-supplied statements and constraints are preserved exactly
#   admin_only: false
#   tests: tests.test_envelope, tests.test_ucns_bridge
#   rollout: importable_package
#   rollback: remove envelope exports and cross-repository adapter fixtures
#   requires: metapat_canon_core
#   since: 2026-07-12
#   unresolved: whether METAPAT statements map to UCNS tags, payloads, or external provenance references
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_module_envelope_docs
#   summary: defines the METAPAT-to-consumer semantic authority boundary
#   audience: developer, agent
#   source: codex-handoff/2026-07-12-stack-repair/REQUIRED_CHANGES.md
#   covers: MetapatModuleEnvelope, provenance digest, canon identity, unresolved hmmm preservation
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_semantic_envelope
#   summary: emits deterministic immutable semantic constraints and provenance without calculated EDCM measurements
#   exposes: metapat.envelope.MetapatModuleEnvelope, metapat.envelope.root_spine_module_envelope
#   inputs: module identity, kind, exact source references and statements, constraints, permitted interpretations, unresolved constraints
#   outputs: immutable envelope, deterministic JSON, provenance digest
#   boundaries: auth:none, storage:serialization-only, network:none, user_data:caller-supplied exact text
# === END CAPABILITIES ===

# === BOUNDARIES ===
# id: metapat_module_envelope_boundary
#   summary: semantic authority and provenance only; no UCNS algebra, EDCM measurement, theorem transfer, or empirical validation
#   auth_boundary: none
#   storage_boundary: serialization-only
#   network_boundary: none
#   user_data_boundary: preserves caller-supplied text exactly
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: metapat_envelope_roundtrip
#   given: a valid immutable module envelope including unresolved hmmm fields
#   then: deterministic JSON roundtrip preserves every field and digest
#   class: schema_contract
#   call: tests.test_envelope.test_envelope_roundtrip_preserves_hmmm
#
# id: metapat_envelope_rotation_visible
#   given: otherwise identical envelopes with different canon digest or semantic constraints
#   then: provenance digests differ
#   class: provenance_contract
#   call: tests.test_envelope.test_canon_or_constraint_rotation_changes_provenance
#
# id: metapat_labels_not_measurements
#   given: a semantic envelope is constructed
#   then: no measured-values field or measurement-validity claim exists
#   class: boundary_contract
#   call: tests.test_envelope.test_envelope_contains_no_measurement_values
# === END CONTRACTS ===

from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from typing import Any, Iterable, Mapping

from .canon import CANON_VERSION, ROOT_SPINE, canon_digest

MODULE_ENVELOPE_SCHEMA_ID = "metapat.module-envelope"
MODULE_ENVELOPE_SCHEMA_VERSION = "1.0.0"
MODULE_KINDS = frozenset(
    {
        "simplex",
        "boundary-simplex",
        "tensor",
        "relation",
        "gradient",
        "registration",
        "time",
        "question",
    }
)


def _tuple_of_strings(name: str, values: Iterable[str], *, allow_empty: bool = True) -> tuple[str, ...]:
    result = tuple(values)
    if not allow_empty and not result:
        raise ValueError(f"{name} must not be empty")
    for index, value in enumerate(result):
        if not isinstance(value, str) or not value.strip():
            raise ValueError(f"{name}[{index}] must be a non-empty string")
    return result


def _canonical_payload(data: Mapping[str, Any]) -> bytes:
    return json.dumps(
        data,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _digest_payload(data: Mapping[str, Any]) -> str:
    return hashlib.sha256(_canonical_payload(data)).hexdigest()


@dataclass(frozen=True, slots=True)
class MetapatModuleEnvelope:
    """Immutable semantic-authority record for external adapters and consumers.

    The envelope carries exact statements and bounded interpretation rules. It
    contains no EDCM metric values and makes no theorem, empirical, or external
    truth claim.
    """

    module_id: str
    module_kind: str
    source_statement_refs: tuple[str, ...]
    source_statements: tuple[str, ...]
    constraints: tuple[str, ...]
    permitted_interpretations: tuple[str, ...]
    unresolved_constraints: tuple[str, ...]
    canon_version: str = CANON_VERSION
    canon_digest: str = ""
    schema_id: str = MODULE_ENVELOPE_SCHEMA_ID
    schema_version: str = MODULE_ENVELOPE_SCHEMA_VERSION
    provenance_digest: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.module_id, str) or not self.module_id.strip():
            raise ValueError("module_id must be a non-empty string")
        if self.module_kind not in MODULE_KINDS:
            raise ValueError(
                f"unsupported module_kind {self.module_kind!r}; "
                f"expected one of {sorted(MODULE_KINDS)!r}"
            )
        if self.schema_id != MODULE_ENVELOPE_SCHEMA_ID:
            raise ValueError(f"unsupported schema_id {self.schema_id!r}")
        if self.schema_version != MODULE_ENVELOPE_SCHEMA_VERSION:
            raise ValueError(f"unsupported schema_version {self.schema_version!r}")
        if not isinstance(self.canon_version, str) or not self.canon_version.strip():
            raise ValueError("canon_version must be a non-empty string")

        refs = _tuple_of_strings("source_statement_refs", self.source_statement_refs, allow_empty=False)
        statements = _tuple_of_strings("source_statements", self.source_statements, allow_empty=False)
        if len(refs) != len(statements):
            raise ValueError("source_statement_refs and source_statements must have equal length")
        constraints = _tuple_of_strings("constraints", self.constraints)
        permitted = _tuple_of_strings("permitted_interpretations", self.permitted_interpretations)
        if not constraints and not permitted:
            raise ValueError("at least one constraint or permitted interpretation is required")
        unresolved = _tuple_of_strings("unresolved_constraints", self.unresolved_constraints)

        object.__setattr__(self, "source_statement_refs", refs)
        object.__setattr__(self, "source_statements", statements)
        object.__setattr__(self, "constraints", constraints)
        object.__setattr__(self, "permitted_interpretations", permitted)
        object.__setattr__(self, "unresolved_constraints", unresolved)

        digest = self.canon_digest or canon_digest()
        if len(digest) != 64 or any(character not in "0123456789abcdef" for character in digest.lower()):
            raise ValueError("canon_digest must be a lowercase hexadecimal SHA-256 digest")
        object.__setattr__(self, "canon_digest", digest.lower())

        expected = _digest_payload(self._provenance_fields())
        if self.provenance_digest and self.provenance_digest != expected:
            raise ValueError("provenance_digest does not match envelope contents")
        object.__setattr__(self, "provenance_digest", expected)

    def _provenance_fields(self) -> dict[str, Any]:
        return {
            "schema_id": self.schema_id,
            "schema_version": self.schema_version,
            "module_id": self.module_id,
            "module_kind": self.module_kind,
            "canon_version": self.canon_version,
            "canon_digest": self.canon_digest,
            "source_statement_refs": list(self.source_statement_refs),
            "source_statements": list(self.source_statements),
            "constraints": list(self.constraints),
            "permitted_interpretations": list(self.permitted_interpretations),
            "unresolved_constraints": list(self.unresolved_constraints),
        }

    def to_dict(self) -> dict[str, Any]:
        """Return a deterministic JSON-compatible representation."""

        data = self._provenance_fields()
        data["provenance_digest"] = self.provenance_digest
        return data

    def to_json(self) -> str:
        """Return canonical deterministic JSON."""

        return _canonical_payload(self.to_dict()).decode("utf-8")

    @classmethod
    def from_dict(cls, data: Mapping[str, Any]) -> "MetapatModuleEnvelope":
        """Validate and reconstruct an envelope from a mapping."""

        expected_fields = {
            "schema_id",
            "schema_version",
            "module_id",
            "module_kind",
            "canon_version",
            "canon_digest",
            "source_statement_refs",
            "source_statements",
            "constraints",
            "permitted_interpretations",
            "unresolved_constraints",
            "provenance_digest",
        }
        unknown = set(data) - expected_fields
        missing = expected_fields - set(data)
        if unknown:
            raise ValueError(f"unknown envelope fields: {sorted(unknown)!r}")
        if missing:
            raise ValueError(f"missing envelope fields: {sorted(missing)!r}")
        return cls(
            schema_id=str(data["schema_id"]),
            schema_version=str(data["schema_version"]),
            module_id=str(data["module_id"]),
            module_kind=str(data["module_kind"]),
            canon_version=str(data["canon_version"]),
            canon_digest=str(data["canon_digest"]),
            source_statement_refs=tuple(data["source_statement_refs"]),
            source_statements=tuple(data["source_statements"]),
            constraints=tuple(data["constraints"]),
            permitted_interpretations=tuple(data["permitted_interpretations"]),
            unresolved_constraints=tuple(data["unresolved_constraints"]),
            provenance_digest=str(data["provenance_digest"]),
        )

    @classmethod
    def from_json(cls, value: str) -> "MetapatModuleEnvelope":
        """Validate and reconstruct an envelope from canonical JSON text."""

        decoded = json.loads(value)
        if not isinstance(decoded, dict):
            raise ValueError("module envelope JSON must decode to an object")
        return cls.from_dict(decoded)


def build_module_envelope(
    *,
    module_id: str,
    module_kind: str,
    source_statement_refs: Iterable[str],
    source_statements: Iterable[str],
    constraints: Iterable[str] = (),
    permitted_interpretations: Iterable[str] = (),
    unresolved_constraints: Iterable[str] = (),
    canon_version: str = CANON_VERSION,
    canon_identity: str | None = None,
) -> MetapatModuleEnvelope:
    """Construct a validated envelope using the current canon identity by default."""

    return MetapatModuleEnvelope(
        module_id=module_id,
        module_kind=module_kind,
        source_statement_refs=tuple(source_statement_refs),
        source_statements=tuple(source_statements),
        constraints=tuple(constraints),
        permitted_interpretations=tuple(permitted_interpretations),
        unresolved_constraints=tuple(unresolved_constraints),
        canon_version=canon_version,
        canon_digest=canon_identity or canon_digest(),
    )


def root_spine_module_envelope() -> MetapatModuleEnvelope:
    """Return the canonical cross-repository fixture for the five-line root spine."""

    refs = tuple(f"AXIOMS.md::ROOT_SPINE[{index}]" for index in range(1, len(ROOT_SPINE) + 1))
    return build_module_envelope(
        module_id="metapat.root_spine",
        module_kind="simplex",
        source_statement_refs=refs,
        source_statements=ROOT_SPINE,
        constraints=(
            "Preserve source statement order and exact text.",
            "Do not let a consuming domain redefine METAPAT root terms.",
            "Do not treat semantic labels as calculated EDCM measurements.",
            "Do not transfer UCNS theorem status into METAPAT ontology claims.",
        ),
        permitted_interpretations=(
            "Use the statements as semantic authority and external provenance constraints.",
            "Bind adaptations and consumer epochs to canon_digest and provenance_digest.",
        ),
        unresolved_constraints=(
            "hmmm: whether METAPAT statements should be represented as UCNS payloads, tags, or external provenance references.",
        ),
    )


__all__ = [
    "MODULE_ENVELOPE_SCHEMA_ID",
    "MODULE_ENVELOPE_SCHEMA_VERSION",
    "MODULE_KINDS",
    "MetapatModuleEnvelope",
    "build_module_envelope",
    "root_spine_module_envelope",
]
