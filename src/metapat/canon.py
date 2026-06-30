"""Canonical METAPAT terms and definitions."""

# === MODULE_BUILD ===
# id: metapat_canon_core
#   module_name: metapat.canon
#   module_kind: schema
#   summary: exposes current Meta Energy Theory root and primitive extension as importable constants
#   owner: The Interdependency
#   public_surface: ROOT_SPINE, PRIMITIVE_EXTENSION, TIME_DEFINITION, ENERGY_THEORY_QUESTION, root_spine, primitive_extension, definitions
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts
#   rollout: importable_package
#   rollback: remove package exports
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_canon_docs
#   summary: documents METAPAT root spine and primitive extension
#   audience: agent
#   source: AXIOMS.md
#   covers: ROOT_SPINE, PRIMITIVE_EXTENSION, TIME_DEFINITION, ENERGY_THEORY_QUESTION
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_canon_constants
#   summary: provides exact importable constants for METAPAT root doctrine
#   exposes: metapat.canon.definitions
#   inputs: none
#   outputs: dict
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
#   summary: static doctrine constants with no external effects
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
#   class: canon
#   call: tests.test_contracts.test_root_spine_contains_current_axioms
#
# id: metapat_time_not_registration
#   given: canon definitions are inspected
#   then: time and registration remain separate definitions
#   class: canon
#   call: tests.test_contracts.test_time_and_registration_are_separated
# === END CONTRACTS ===

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
    """Return compact canonical definitions for agent checks."""

    return {
        "METAPAT": "Meta Energy Theory — Axioms, Postulates, and Theorems.",
        "tensor": "Primitive simultaneous arrangement of energy-states.",
        "time": TIME_DEFINITION,
        "registration": "Capacity of a simplex to preserve, express, or transmit sequential tensor alteration.",
        "observer": "A simplex performing registration; observer does not necessarily mean mind.",
        "question": "A bounded unresolved energy-state.",
    }
