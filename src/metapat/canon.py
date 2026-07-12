"""Canonical METAPAT terms, exact statements, and deterministic identity.

Usage guidance
--------------
Import the constants or helper functions when a consumer needs METAPAT root
meaning. Use :func:`canon_digest` to bind a semantic module envelope to this
exact importable canon. The digest identifies the encoded canon surface; it is
not empirical validation or formal proof of the ontology.
"""

# === MODULE_BUILD ===
# id: metapat_canon_core
#   module_name: metapat.canon
#   module_kind: schema
#   summary: exposes exact Meta Energy Theory root constants and a deterministic canon identity without changing the canon text
#   owner: The Interdependency
#   public_surface: CANON_VERSION, ROOT_SPINE, PRIMITIVE_EXTENSION, TIME_DEFINITION, ENERGY_THEORY_QUESTION, root_spine, primitive_extension, definitions, canonical_canon_data, canon_digest
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_envelope
#   rollout: importable_package
#   rollback: remove digest helpers while preserving exact canon constants
#   requires: none
#   since: 2026-07-12
#   unresolved: formal version-governance process for future canon rotations
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_canon_docs
#   summary: documents METAPAT root spine and primitive extension
#   audience: agent
#   source: AXIOMS.md
#   covers: CANON_VERSION, ROOT_SPINE, PRIMITIVE_EXTENSION, TIME_DEFINITION, ENERGY_THEORY_QUESTION
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_canon_constants
#   summary: provides exact importable constants and deterministic identity for METAPAT root doctrine
#   exposes: metapat.canon.definitions, metapat.canon.canon_digest
#   inputs: none
#   outputs: dict, sha256 digest
#   boundaries: auth:none, storage:none, network:none, user_data:none
# === END CAPABILITIES ===

# === OWNERS ===
# id: metapat_canon_owner
#   owner: The Interdependency
#   steward: Erin Spencer
#   review_required_for: public_api, docs, canon
#   escalation: hmmm
# === END OWNERS ===

# === BOUNDARIES ===
# id: metapat_canon_boundaries
#   summary: static doctrine constants and deterministic serialization with no external effects
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: metapat_root_spine_exact
#   given: canon definitions are imported
#   then: root spine contains the current five load-bearing root lines in order
#   class: canon_contract
#   call: tests.test_contracts.test_root_spine_contains_current_axioms
#
# id: metapat_time_not_registration
#   given: canon definitions are inspected
#   then: time and registration remain separate definitions
#   class: canon_contract
#   call: tests.test_contracts.test_time_and_registration_are_separated
#
# id: metapat_canon_digest_deterministic
#   given: the same exact canon constants are serialized repeatedly
#   then: canonical data and the sha256 digest remain byte-for-byte stable
#   class: canon_contract
#   call: tests.test_envelope.test_canon_digest_is_deterministic
# === END CONTRACTS ===

from __future__ import annotations

import hashlib
import json
from typing import Any

CANON_VERSION = "metapat-canon-v1"

ROOT_SPINE: tuple[str, ...] = (
    "Legible difference is distinction.",
    "Distinction defines boundaries.",
    "Boundaries define simplex.",
    "Boundary is simplex of distinction.",
    "Simplex holds or modifies energy in a state of being.",
)

PRIMITIVE_EXTENSION: tuple[str, ...] = (
    "Tensor is primitive simultaneous arrangement of energy-states.",
    "Energy-state held is scalar.",
    "Energy-state motioned is vector.",
    "Energy-state vectors alter energy-state scalars.",
)

TIME_DEFINITION = "Time is sequential tensor alteration."
ENERGY_THEORY_QUESTION = "What questions do I ask?"


def root_spine() -> tuple[str, ...]:
    """Return the exact current root spine."""

    return tuple(ROOT_SPINE)


def primitive_extension() -> tuple[str, ...]:
    """Return the exact current primitive extension."""

    return tuple(PRIMITIVE_EXTENSION)


def definitions() -> dict[str, str]:
    """Return compact canonical definitions for contract checks and consumers."""

    return {
        "METAPAT": "Meta Energy Theory — Axioms, Postulates, and Theorems.",
        "tensor": "Primitive simultaneous arrangement of energy-states.",
        "time": TIME_DEFINITION,
        "registration": "Capacity of a simplex to preserve, express, or transmit sequential tensor alteration.",
        "observer": "A simplex performing registration; observer does not necessarily mean mind.",
        "question": "A bounded unresolved energy-state.",
    }


def canonical_canon_data() -> dict[str, Any]:
    """Return the deterministic public canon surface used for identity binding.

    The structure contains exact strings already declared by this module. It
    adds no interpretation and does not rewrite Chapter Zero or the root files.
    """

    return {
        "canon_version": CANON_VERSION,
        "root_spine": list(ROOT_SPINE),
        "primitive_extension": list(PRIMITIVE_EXTENSION),
        "time_definition": TIME_DEFINITION,
        "energy_theory_question": ENERGY_THEORY_QUESTION,
        "definitions": definitions(),
    }


def canon_digest() -> str:
    """Return a stable SHA-256 digest for :func:`canonical_canon_data`."""

    encoded = json.dumps(
        canonical_canon_data(),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


__all__ = [
    "CANON_VERSION",
    "ENERGY_THEORY_QUESTION",
    "PRIMITIVE_EXTENSION",
    "ROOT_SPINE",
    "TIME_DEFINITION",
    "canon_digest",
    "canonical_canon_data",
    "definitions",
    "primitive_extension",
    "root_spine",
]
