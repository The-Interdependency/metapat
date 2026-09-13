"""Static theory and declared-derivation data for the semantic catalog."""

# === MODULE_BUILD ===
# id: metapat_semantic_theory_declarations
#   module_name: metapat.catalog_theory_data
#   module_kind: schema
#   summary: declares stable theory module identities, exact claim statements, and source-declared derivation ancestry
#   owner: The Interdependency
#   public_surface: none
#   internal_surface: THEORY_SPECS, CATALOG_DERIVATIONS, CATALOG_DERIVED_TEXT
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact canon statements only
#   admin_only: false
#   tests: tests.test_catalog
#   rollout: internal catalog constructor dependency
#   rollback: restore the prior canon-bound theory declarations
#   requires: metapat_canon_core
#   since: 2026-07-21
#   unresolved: none
# === END MODULE_BUILD ===

THEORY_SPECS = (
    ("metapat.theory.0.root_prior_restraint", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-0-root-prior-restraint", (
        "Every domain may reveal part of Platonic energy without owning the root.",
    ), ()),
    ("metapat.theory.1.thing_boundary_state", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-1-thing-boundary-state-construction", (
        "Thing, boundary, and state are sufficient to close simplex.",
    ), ()),
    ("metapat.theory.2.relational_tensor_formation", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-2-relational-tensor-formation", (
        "Simplexes relate; tensor is the structure that emerges from their relation.",
    ), ()),
    ("metapat.theory.3.recursive_closure", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-3-recursive-closure", (
        "A tensor is a thing and may close as simplex when it has boundary and state.",
    ), ()),
    ("metapat.theory.4.state_measurement", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-4-state-measurement", (
        "State exists independently of its metric; scalar measures state, while vector is inferred from measured state change.",
    ), ()),
    ("metapat.theory.5.transformation", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-5-transformation", (
        "Vector alters state; the resulting state change is transformation.",
    ), ()),
    ("metapat.theory.6.time", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-6-time", (
        "Time is sequential transformation.",
    ), ()),
    ("metapat.theory.7.derived_energy", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-7-derived-energy", (
        "Energy is composite: vectors altering state through transformation across time.",
    ), ()),
    ("metapat.theory.8.emergence", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-8-emergence", (
        "Tensors emerge from simplexes and may become simplexes in recursive construction.",
    ), ()),
    ("metapat.theory.9.registration_observer", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-9-registration-and-observer-roles", (
        "Registration preserves, expresses, or transmits transformation; observation does not create the structure registered.",
    ), ()),
    ("metapat.theory.10.questions_unresolved_structure", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-10-questions-as-unresolved-structure", (
        "A question is a bounded unresolved state or relation available to transformation.",
        "Energy Theory is a question-finder before it is an answer-machine.",
    ), ()),
    ("metapat.theory.11.cross_domain_reconstruction", "theory", "theory", "INTERNAL-DERIVATION", "THEORIES.md", "theory-11-cross-domain-reconstruction", (
        "Independent domain implementations may expose the same candidate structure or action without making the domains identical.",
        "The candidate survives only while later domains fail to falsify, split, or refine it.",
    ), ("hmmm: completeness is never presumed.",)),
)

CATALOG_DERIVATIONS = {
    "metapat.theory.0.root_prior_restraint": ("metapat.root_spine", "metapat.postulate.1.partial_domains", "metapat.postulate.2.explicationary_use", "metapat.postulate.6.cross_domain_falsification", "metapat.theorem.8.root_tool_separation"),
    "metapat.theory.1.thing_boundary_state": ("metapat.axiom.1.thing", "metapat.axiom.2.boundary", "metapat.axiom.3.state", "metapat.axiom.4.simplex", "metapat.theorem.1.boundary_requires_multiplicity", "metapat.theorem.2.simplex_closure"),
    "metapat.theory.2.relational_tensor_formation": ("metapat.axiom.5.tensor", "metapat.axiom.6.relate", "metapat.axiom.7.emerge", "metapat.theorem.3.tensor_emergence"),
    "metapat.theory.3.recursive_closure": ("metapat.axiom.5.tensor", "metapat.postulate.3.recursive_closure", "metapat.theorem.4.recursive_closure"),
    "metapat.theory.4.state_measurement": ("metapat.axiom.3.state", "metapat.axiom.8.vector", "metapat.axiom.9.scalar", "metapat.theorem.5.scalar_vector_distinct"),
    "metapat.theory.5.transformation": ("metapat.axiom.8.vector", "metapat.axiom.10.transformation", "metapat.theorem.6.transformation_produces_time"),
    "metapat.theory.6.time": ("metapat.axiom.11.time", "metapat.theorem.6.transformation_produces_time"),
    "metapat.theory.7.derived_energy": ("metapat.axiom.12.energy", "metapat.theorem.7.energy_is_derived"),
    "metapat.theory.8.emergence": ("metapat.axiom.5.tensor", "metapat.axiom.6.relate", "metapat.axiom.7.emerge", "metapat.theorem.3.tensor_emergence", "metapat.theorem.4.recursive_closure"),
    "metapat.theory.9.registration_observer": ("metapat.postulate.4.registration_plurality", "metapat.postulate.5.observation_does_not_create_structure"),
    "metapat.theory.10.questions_unresolved_structure": ("metapat.postulate.5.observation_does_not_create_structure", "metapat.postulate.6.cross_domain_falsification", "metapat.postulate.7.discovery_before_recovery"),
    "metapat.theory.11.cross_domain_reconstruction": ("metapat.postulate.1.partial_domains", "metapat.postulate.2.explicationary_use", "metapat.postulate.6.cross_domain_falsification", "metapat.theorem.8.root_tool_separation"),
}

CATALOG_DERIVED_TEXT = {
    "metapat.theory.0.root_prior_restraint": "Derived from: root restraint; Postulates 1, 2, and 6; Theorem 8.",
    "metapat.theory.1.thing_boundary_state": "Derived from: Axioms 1-4; Theorems 1-2.",
    "metapat.theory.2.relational_tensor_formation": "Derived from: Axioms 5-7; Theorem 3.",
    "metapat.theory.3.recursive_closure": "Derived from: Axiom 5; Postulate 3; Theorem 4.",
    "metapat.theory.4.state_measurement": "Derived from: Axioms 3, 8, and 9; Theorem 5.",
    "metapat.theory.5.transformation": "Derived from: Axioms 8 and 10; Theorem 6.",
    "metapat.theory.6.time": "Derived from: Axiom 11; Theorem 6.",
    "metapat.theory.7.derived_energy": "Derived from: Axiom 12; Theorem 7.",
    "metapat.theory.8.emergence": "Derived from: Axioms 5-7; Theorems 3-4.",
    "metapat.theory.9.registration_observer": "Derived from: Postulates 4-5.",
    "metapat.theory.10.questions_unresolved_structure": "Derived from: Postulates 5-7.",
    "metapat.theory.11.cross_domain_reconstruction": "Derived from: Postulates 1, 2, and 6; Theorem 8.",
}
