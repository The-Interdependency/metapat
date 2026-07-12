"""Optional adapter from METAPAT semantic envelopes to the actual UCNS package.

This module contains no UCNS algebra. It imports the canonical ``ucns``
package only when adaptation is requested, constructs real
``ucns.UCNSObject`` instances, and keeps METAPAT statements outside the UCNS
payload channel as explicit provenance until the unresolved semantic mapping is
ratified.

Usage guidance
--------------
Install the optional UCNS integration, then call
:func:`adapt_envelope_to_ucns`. Base METAPAT canon and envelope imports remain
available without UCNS installed. Calling an adapter function without the
optional dependency raises :class:`UCNSDependencyError`; no local substitute is
created.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: metapat_ucns_adapter
#   module_name: metapat.ucns
#   module_kind: adapter
#   summary: adapts immutable METAPAT semantic envelopes into actual ucns.UCNSObject instances without duplicating UCNS algebra or transferring theorem status
#   owner: The Interdependency
#   public_surface: GONOL_VERTEX_COUNT, SPACE_ANCHOR_VERTEX, ADDRESSABLE_GONOL_VERTICES, UCNSDependencyError, UCNSAdapterError, UCNSAdaptationRecord, UCNSAdaptation, require_ucns, adapt_envelope_to_ucns, root_spine_adaptation, root_spine_ucns, compose
#   internal_surface: _module_version, _angles_for_statement_count
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: package import only; no network performed by runtime code
#   user_data_boundary: exact envelope statements remain external provenance and are not placed into UCNS payloads
#   admin_only: false
#   tests: tests.test_ucns_bridge, tests.test_envelope
#   rollout: optional_integration
#   rollback: remove adapter exports; base canon and envelope remain importable
#   requires: optional external ucns package, metapat_module_envelope
#   since: 2026-07-12
#   unresolved: whether statements should later map to UCNS tags, payloads, or remain external provenance
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_ucns_adapter_docs
#   summary: documents the actual-UCNS adapter and the external-provenance semantic boundary
#   audience: developer
#   source: UCNS_IMPLEMENTATION.md
#   covers: adapt_envelope_to_ucns, UCNSAdaptationRecord, dependency and theorem-status boundaries
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_actual_ucns_adapter
#   summary: constructs actual UCNS geometry from statement count while retaining METAPAT meaning in a separate provenance record
#   exposes: metapat.ucns.adapt_envelope_to_ucns
#   inputs: MetapatModuleEnvelope, optional face bits
#   outputs: actual ucns.UCNSObject plus UCNSAdaptationRecord
#   boundaries: auth:none, storage:none, network:none, user_data:semantic text remains provenance-only
# === END CAPABILITIES ===

# === BOUNDARIES ===
# id: metapat_ucns_adapter_boundary
#   summary: UCNS provides geometry only; METAPAT owns semantic authority; no theorem or empirical status transfer
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: source statements remain in the METAPAT envelope and adaptation record
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: metapat_actual_ucns_object
#   given: UCNS is installed and a valid METAPAT envelope is adapted
#   then: the returned object is an actual ucns.UCNSObject and its stable hash is recorded
#   class: integration_contract
#   call: tests.test_ucns_bridge.test_root_spine_adapts_to_actual_ucns_object
#
# id: metapat_ucns_provenance_survives
#   given: a semantic envelope is adapted
#   then: canon digest, envelope provenance digest, exact source references, and unresolved constraints survive outside UCNS payload meaning
#   class: provenance_contract
#   call: tests.test_ucns_bridge.test_adaptation_preserves_semantic_provenance
#
# id: metapat_ucns_no_theorem_transfer
#   given: any successful adaptation
#   then: theorem_status_transfer and metapat_validity_claim remain false
#   class: boundary_contract
#   call: tests.test_ucns_bridge.test_adaptation_does_not_transfer_theorem_status
# === END CONTRACTS ===

import importlib
import importlib.metadata
from dataclasses import asdict, dataclass
from fractions import Fraction
from types import ModuleType
from typing import Any, Iterable

from .envelope import MetapatModuleEnvelope, root_spine_module_envelope

GONOL_VERTEX_COUNT = 157
SPACE_ANCHOR_VERTEX = 0
ADDRESSABLE_GONOL_VERTICES = GONOL_VERTEX_COUNT - 1

UCNS_INSTALL_HINT = (
    "Install the optional UCNS integration with `python -m pip install -e .[ucns]` "
    "or install The-Interdependency/ucns directly."
)


class UCNSDependencyError(ModuleNotFoundError):
    """Raised when actual UCNS adaptation is requested without UCNS installed."""


class UCNSAdapterError(RuntimeError):
    """Raised when an importable UCNS package lacks the required public surface."""


@dataclass(frozen=True, slots=True)
class UCNSAdaptationRecord:
    """Provenance record kept separate from UCNS mathematical payload meaning."""

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
    unresolved_constraints: tuple[str, ...]
    semantic_mapping: str = "external-provenance"
    theorem_status_transfer: bool = False
    metapat_validity_claim: bool = False

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(frozen=True, slots=True)
class UCNSAdaptation:
    """One actual UCNS object paired with its METAPAT provenance boundary."""

    ucns_object: Any
    record: UCNSAdaptationRecord


def require_ucns() -> ModuleType:
    """Import and validate the actual UCNS package.

    Only direct absence of ``ucns`` is translated into
    :class:`UCNSDependencyError`. Transitive import failures remain visible.
    """

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
    """Construct an actual UCNS object for an immutable METAPAT envelope.

    Geometry is derived only from ordered statement count and caller-supplied
    face bits. Source statements, references, constraints, and unresolved
    ``hmmm`` fields remain external provenance. UCNS payloads are all unit
    (``None``) until a separate semantic mapping is ratified.
    """

    if not isinstance(envelope, MetapatModuleEnvelope):
        raise TypeError("envelope must be a MetapatModuleEnvelope")

    module = require_ucns()
    count = len(envelope.source_statements)
    angles = _angles_for_statement_count(count)
    faces = tuple(0 for _ in range(count)) if face_bits is None else tuple(face_bits)
    if len(faces) != count:
        raise ValueError("face_bits length must match source statement count")
    if any(not isinstance(face, int) or face not in (0, 1) for face in faces):
        raise ValueError("face_bits must contain only integer face bits 0 or 1")

    actual_object = module.UCNSObject(
        count,
        count,
        [(angle, None) for angle in angles],
        list(faces),
    )
    record = UCNSAdaptationRecord(
        adapter_schema="metapat-actual-ucns-adapter-v1",
        adapter_version="1.0.0",
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
        unresolved_constraints=envelope.unresolved_constraints,
    )
    return UCNSAdaptation(actual_object, record)


def root_spine_adaptation() -> UCNSAdaptation:
    """Adapt the canonical root-spine envelope into actual UCNS geometry."""

    return adapt_envelope_to_ucns(root_spine_module_envelope())


def root_spine_ucns() -> Any:
    """Compatibility helper returning the actual root-spine UCNS object only."""

    return root_spine_adaptation().ucns_object


def compose(left: Any, right: Any) -> Any:
    """Delegate composition to actual ``ucns.multiply``.

    METAPAT supplies no local normalization, product, star, disk-flip,
    factorization, or theorem vocabulary.
    """

    module = require_ucns()
    if not isinstance(left, module.UCNSObject) or not isinstance(right, module.UCNSObject):
        raise TypeError("compose requires actual ucns.UCNSObject operands")
    return module.multiply(left, right)


__all__ = [
    "ADDRESSABLE_GONOL_VERTICES",
    "GONOL_VERTEX_COUNT",
    "SPACE_ANCHOR_VERTEX",
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
