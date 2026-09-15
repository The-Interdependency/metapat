"""Static axiom, postulate, and theorem declarations for the semantic catalog."""

# === MODULE_BUILD ===
# id: metapat_semantic_doctrine_declarations
#   module_name: metapat.catalog_doctrine_data
#   module_kind: schema
#   summary: declares stable axiom, postulate, and theorem module identities, classes, source sections, and exact statements
#   owner: The Interdependency
#   public_surface: none
#   internal_surface: DOCTRINE_SPECS
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: exact canon statements only
#   admin_only: false
#   tests: tests.test_catalog
#   rollout: internal catalog constructor dependency
#   rollback: restore the prior canon-bound declaration set
#   requires: metapat_canon_core
#   since: 2026-07-21
#   unresolved: none
# === END MODULE_BUILD ===

DOCTRINE_SPECS = (
    ("metapat.axiom.1.thing", "thing", "axiom", "ROOT-STIPULATION", "AXIOMS.md", "1-thing", (
        "Thing is that which is.",
        "A solitary thing has no boundary.",
    ), ()),
    ("metapat.axiom.2.boundary", "boundary", "axiom", "ROOT-STIPULATION", "AXIOMS.md", "2-boundary", (
        "Boundary is the thing between things.",
        "Boundary requires more than one thing.",
    ), ()),
    ("metapat.axiom.3.state", "state", "axiom", "ROOT-STIPULATION", "AXIOMS.md", "3-state", (
        "State is a metricable property of a thing.",
        "State is not measurement.",
    ), ()),
    ("metapat.axiom.4.simplex", "simplex", "axiom", "ROOT-STIPULATION", "AXIOMS.md", "4-simplex", (
        "A simplex is a thing with boundary and state.",
        "A simplex is primitive where it participates as a whole.",
    ), ()),
    ("metapat.axiom.5.tensor", "tensor", "axiom", "DEFINITION", "AXIOMS.md", "5-tensor", (
        "A tensor is structure produced when simplexes relate.",
        "A tensor is a thing.",
    ), ()),
    ("metapat.axiom.6.relate", "relate", "axiom", "DEFINITION", "AXIOMS.md", "6-relate", (
        "Relate is this to that.",
        "Geometry is one possible relation, not the definition of relate.",
    ), ()),
    ("metapat.axiom.7.emerge", "emergence", "axiom", "DEFINITION", "AXIOMS.md", "7-emerge", (
        "Tensors emerge from simplexes.",
    ), ()),
    ("metapat.axiom.8.vector", "vector", "axiom", "DEFINITION", "AXIOMS.md", "8-vector", (
        "Vector alters state.",
        "Vector is inferred by scalar measurement.",
    ), ()),
    ("metapat.axiom.9.scalar", "scalar", "axiom", "DEFINITION", "AXIOMS.md", "9-scalar", (
        "Scalar is a state metric.",
    ), ()),
    ("metapat.axiom.10.transformation", "transformation", "axiom", "DEFINITION", "AXIOMS.md", "10-transformation", (
        "Transformation is resulting state change.",
    ), ()),
    ("metapat.axiom.11.time", "time", "axiom", "DEFINITION", "AXIOMS.md", "11-time", (
        "Time is sequential transformation.",
        "Registration may preserve time.",
        "Registration does not produce time.",
    ), ()),
    ("metapat.axiom.12.domain_qualification", "domain-qualification", "axiom", "DEFINITION", "AXIOMS.md", "12-domain-qualification", (
        "Structural recurrence does not transfer a domain term.",
        "A domain term applies only where that domain independently licenses it.",
        "Energy is domain-qualified. METAPAT does not call every state transformation energy merely because state, vector, transformation, and time are present.",
    ), ()),
    ("metapat.postulate.1.partial_domains", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "first-postulate-partial-domains", (
        "Different domains may independently expose common structures and actions.",
        "Cross-domain comparison may recover shared structure without making domains identical.",
        "Similarity does not transfer domain-specific names, mechanisms, evidence standards, or conservation laws.",
    ), ()),
    ("metapat.postulate.2.explicationary_use", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "second-postulate-explicationary-use", (
        "A domain term may clarify the root.",
        "A domain term may not redefine the root.",
    ), ()),
    ("metapat.postulate.3.recursive_closure", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "third-postulate-recursive-closure", (
        "A tensor may participate as a thing.",
        "A tensor with boundary and state is a simplex.",
    ), ()),
    ("metapat.postulate.4.registration_plurality", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "fourth-postulate-registration-plurality", (
        "Any simplex capable of preserving, expressing, or transmitting transformation may perform registration.",
        "Consciousness is one registration mode, not the parent ontology.",
    ), ()),
    ("metapat.postulate.5.observation_does_not_create_structure", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "fifth-postulate-observation-does-not-create-structure", (
        "Observation may register a boundary, state, relation, transformation, or tensor without creating the structure registered.",
    ), ()),
    ("metapat.postulate.6.cross_domain_falsification", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "sixth-postulate-cross-domain-falsification", (
        "When different domains independently expose the same candidate structure or action, remove the domain-specific implementation and test what remains.",
        "A new domain may add, split, refine, or falsify a candidate.",
        "Completeness is never presumed.",
    ), ()),
    ("metapat.postulate.7.discovery_before_recovery", "postulate", "postulate", "WORKING-POSTULATE", "POSTULATES.md", "seventh-postulate-discovery-before-recovery", (
        "Interest may select what to explore.",
        "Discovery may precede explanation.",
        "Freeze a result before independent recovery.",
        "Independent recovery tests the result, not the legitimacy of the discovery path.",
        "A simpler recovery method does not invalidate a more complex discovery method.",
    ), ()),
    ("metapat.theorem.1.boundary_requires_multiplicity", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "first-theorem-boundary-requires-multiplicity", (
        "If boundary is the thing between things, one thing alone has no boundary.",
        "Therefore boundary requires more than one thing.",
    ), ()),
    ("metapat.theorem.2.simplex_closure", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "second-theorem-simplex-closure", (
        "If a thing has boundary and state, it satisfies the simplex definition.",
        "Therefore thing + boundary + state closes as simplex.",
    ), ()),
    ("metapat.theorem.3.tensor_emergence", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "third-theorem-tensor-emergence", (
        "If simplexes relate and tensor is the structure produced when simplexes relate, a tensor emerges from related simplexes.",
    ), ()),
    ("metapat.theorem.4.recursive_closure", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "fourth-theorem-recursive-closure", (
        "If a tensor is a thing, then a tensor with boundary and state satisfies the simplex definition.",
        "Therefore tensor construction may recurse through simplex closure.",
    ), ()),
    ("metapat.theorem.5.scalar_vector_distinct", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "fifth-theorem-scalar-and-vector-are-distinct", (
        "If scalar is a state metric and vector alters state, scalar measures what vector alters.",
        "Therefore scalar and vector are not the same kind of thing.",
        "Vector is inferred through scalar measurement of state change.",
    ), ()),
    ("metapat.theorem.6.transformation_produces_time", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "sixth-theorem-transformation-produces-time-by-sequence", (
        "If vector alters state, the resulting state change is transformation.",
        "If transformations occur sequentially, there is time.",
    ), ()),
    ("metapat.theorem.7.domain_terms_do_not_transfer", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "seventh-theorem-domain-terms-do-not-transfer-by-structure-alone", (
        "If a structure or action can recur in domains with different native terms and mechanisms, structural recurrence alone cannot establish that one domain's term names the others.",
        "Therefore energy applies only where the applicable domain independently licenses energy; a common state-transformation pattern need not itself be energy.",
    ), ()),
    ("metapat.theorem.8.root_tool_separation", "theorem", "theorem", "INTERNAL-DERIVATION", "THEOREMS.md", "eighth-theorem-root-and-tool-separation", (
        "If different domains may expose common structures without transferring domain identity, no single domain may own the root.",
        "Therefore domain implementations may reveal METAPAT structure without becoming METAPAT structure by identity.",
    ), ()),
)
