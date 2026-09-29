"""Catalog-bound EPAC multi-origin join-term application."""

# === MODULE_BUILD ===
# id: metapat_epac_join_terms_application
#   module_name: metapat.epac_join_terms
#   module_kind: schema
#   summary: licenses exact METAPAT spine roles for an EPAC-owned typed S0-through-S6 join-term representation without transferring domain validity
#   owner: The Interdependency
#   public_surface: EPAC_JOIN_TERMS_APPLICATION_VERSION, EPAC_JOIN_TERMS_BINDING_SPECS, epac_join_terms_application_module, epac_join_terms_application_digest
#   internal_surface: source declarations and application mapping constants
#   auth_boundary: none
#   storage_boundary: serialization-only and read-only source verification
#   network_boundary: none
#   user_data_boundary: public conceptual application text only
#   admin_only: false
#   tests: tests.test_epac_join_terms
#   rollout: importable catalog-bound application module and deterministic packaged fixture
#   rollback: remove the application module, fixture, and documentation while preserving canon and the generic application schema
#   requires: metapat_application_module_schema, metapat_semantic_catalog
#   since: 2026-09-29
#   unresolved: empirical adequacy, physical interpretation, UCNS correspondence, and promotion beyond application terminology remain unresolved
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_epac_join_terms_docs
#   summary: licenses the METAPAT-to-EPAC semantic map, recursive-origin vocabulary, and strict non-transfer boundary
#   audience: developer, agent, EPAC consumer, domain reviewer
#   source: docs/applications/epac-join-terms.md
#   covers: epac_join_terms_application_module, semantic role map, scale names, customs boundary, downstream evidence requirements
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_epac_join_terms_semantics
#   summary: emits one deterministic catalog-bound application record for EPAC typed join terms across S0 through S6
#   exposes: metapat.epac_join_terms.epac_join_terms_application_module
#   inputs: canonical semantic catalog v4
#   outputs: strict cross-domain application module and deterministic digest
#   boundaries: auth:none, storage:serialization-only, network:none, user_data:public conceptual text only
# === END CAPABILITIES ===

# === BOUNDARIES ===
# id: metapat_epac_join_terms_boundary
#   summary: semantic licensing only; no canon amendment, EPAC implementation validation, chemical or physical truth claim, energy coupling, UCNS law transfer, EDCM measurement, or inferred ancestry
#   auth_boundary: none
#   storage_boundary: serialization-only and read-only source verification
#   network_boundary: none
#   user_data_boundary: public conceptual text only
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: metapat_epac_join_terms_catalog_bound
#   given: the EPAC join-terms application module is constructed
#   then: every applied METAPAT concept is bound to an exact catalog module identity, digest, and claim status
#   class: integration_contract
#
# id: metapat_epac_join_terms_customs_boundary
#   given: the licensed role map and non-transfer declarations are inspected
#   then: METAPAT spine terms remain semantic roles while EPAC owns domain names and no UCNS, chemistry, physics, energy-coupling, or ancestry claim crosses the boundary
#   class: boundary_contract
#
# id: metapat_epac_join_terms_recursive_identity
#   given: recursive-origin semantics are inspected
#   then: a joined whole may become a new identity at the next declared scale without flattening or erasing its ordered constituents
#   class: boundary_contract
#
# id: metapat_epac_join_terms_complete_scale_map
#   given: selected application scales are inspected
#   then: S0 through S6 are each present exactly once and carry EPAC-qualified names
#   class: schema_contract
#
# id: metapat_epac_join_terms_candidate_status
#   given: application status and validity fields are inspected
#   then: the application remains a cross-domain hypothesis with no root impact and every validity-transfer flag false
#   class: canon_contract
#
# id: metapat_epac_join_terms_source_current
#   given: the application constructor and source document are checked together
#   then: exact role mappings, transfers, prohibitions, evidence requirements, and hmmm statements remain source-current
#   class: provenance_contract
#
# id: metapat_epac_join_terms_fixture_current
#   given: the packaged EPAC join-terms application fixture is inspected
#   then: its bytes equal the deterministic live constructor serialization plus one trailing newline
#   class: evidence
# === END CONTRACTS ===

from __future__ import annotations

from .application import (
    MetapatApplicationModule,
    bind_catalog_module,
    validate_application_against_catalog,
)
from .catalog import MetapatSemanticCatalog, canonical_semantic_catalog, semantic_module_by_id

EPAC_JOIN_TERMS_APPLICATION_VERSION = "epac-join-terms-application-v4"
SOURCE_DOCUMENT = "docs/applications/epac-join-terms.md"

EPAC_JOIN_TERMS_BINDING_SPECS = (
    (
        "metapat.root_spine",
        "customs-boundary",
        "METAPAT supplies the semantic spine while EPAC retains its domain-qualified names, schemas, constructors, and evidence obligations.",
    ),
    (
        "metapat.axiom.1.thing",
        "stored-join-term",
        "EPAC uses Thing as the semantic role of one stored typed join term, not a formula bag, residue list, or count.",
    ),
    (
        "metapat.axiom.2.boundary",
        "join-boundary",
        "EPAC uses Boundary for named ordered slots, explicit holes and leftovers, and the stored window k.",
    ),
    (
        "metapat.axiom.3.state",
        "origin-state",
        "EPAC uses State for domain-qualified phase and capacity metrics at a declared origin.",
    ),
    (
        "metapat.axiom.4.simplex",
        "scale-origin",
        "EPAC treats one complete scale origin O(S_n), with its boundary and state, as a Simplex-role object.",
    ),
    (
        "metapat.axiom.5.tensor",
        "multi-origin-tensor",
        "EPAC uses Tensor for the structure formed by all declared S0 through S6 origins and their authored relations; a flattened bag is not that object.",
    ),
    (
        "metapat.axiom.6.relate",
        "authored-near-join",
        "EPAC records only authored adjacent-scale joins and does not infer ancestry from analogy, shared counts, or shared geometry.",
    ),
    (
        "metapat.axiom.7.emerge",
        "recursive-origin",
        "EPAC may store join(O(S_n)) as a new identity O(S_{n+1}) while retaining its ordered constituent identities and provenance.",
    ),
    (
        "metapat.axiom.8.vector",
        "inferred-bearing",
        "EPAC uses the Vector role only for bearing inferred from declared scalar measurements; it is not a stored free-arrow collection.",
    ),
    (
        "metapat.axiom.9.scalar",
        "state-metric",
        "EPAC phase, capacity, and any occupancy readout are exact domain-qualified scalar measurements rather than transferred physical quantities.",
    ),
    (
        "metapat.axiom.10.transformation",
        "join-transformation",
        "EPAC records a declared join as a transformation that produces a new origin state and preserves source and target identity.",
    ),
    (
        "metapat.axiom.11.time",
        "transformation-sequence",
        "EPAC may order transformation records sequentially without treating structural scale order as physical time.",
    ),
    (
        "metapat.axiom.12.domain_qualification",
        "domain-customs",
        "Every transferred spine role remains paired with an EPAC domain name; structural recurrence alone transfers no chemical, physical, energetic, or UCNS meaning.",
    ),
)

DOMAINS = (
    "EPAC relational representation",
    "typed recursive join terms",
    "multi-origin provenance",
)
SELECTED_SCALES = (
    "S0 subatomic slot",
    "S1 atomic",
    "S2 join/arity",
    "S3 embed",
    "S4 electronic state",
    "S5 EPAC energy readout",
    "S6 ensemble",
)
DOMAIN_STATEMENTS = (
    "An EPAC join term stores named ordered slots, explicit holes and leftovers, a positive window k, exact origin state, and provenance; omission is not a representation of zero.",
    "At each adjacent scale, join(O(S_n)) may be stored as a new identity O(S_{n+1}); recursive construction does not erase or contract the child identities that establish the join.",
    "The EPAC tensor-role object contains every declared origin S0 through S6 and its authored adjacent-scale relations; a formula bag or subset fill cannot substitute for that structure.",
    "EPAC join equality is join-isomorphism over typed ordered structure and state, not equality of counts, formulas, residue bags, or visible projections.",
    "Visible and lifted phase records remain distinct EPAC objects when their declared identities or coordinates differ.",
    "S5 energy readout is an EPAC-qualified functional of occupancy and is not a fourth circle, a universal energy primitive, or evidence of physical energy coupling.",
)
SHARED_QUESTION_FORM = (
    "typed origin O(S_n)",
    "-> named ordered slots including holes and leftovers",
    "-> authored adjacent-scale join",
    "-> new identity O(S_{n+1})",
    "-> preserved source identities and provenance",
    "-> complete S0-through-S6 relational structure",
)
TRANSFERS = (
    "The spine roles Thing, Boundary, State, Simplex, Tensor, Scalar, Vector, Transformation, and Time may label their declared EPAC semantic counterparts.",
    "A bounded lower-scale whole may participate in an authored adjacent-scale relation and the joined whole may receive a new identity.",
    "Ordered constituent identity, explicit holes and leftovers, state metrics, and provenance may remain addressable across recursive construction.",
    "Exact deterministic serialization and replay may test whether an EPAC implementation preserves the licensed distinctions.",
)
DOES_NOT_TRANSFER = (
    "This license does not transfer a UCNS coordinate, phase law, topology, theorem status, gonol identity, or implementation into EPAC.",
    "EPAC phase is not chemistry phase, and visible or lifted coordinates acquire no physical meaning merely because they are stored.",
    "S5 naming does not establish energy coupling, conservation, entropy, force, field, or empirical physical validity.",
    "Shared shape, count, phase, vocabulary, or geometry does not establish ancestry or authorize an inferred join.",
    "A formula bag, residue collection, contracted cardinality, subset fill, or gravity-point registry is not licensed as the multi-origin tensor-role object.",
    "METAPAT licensing does not validate EPAC implementation correctness, molecular geometry, production suitability, or external-domain truth.",
)
WORKING_QUESTION = "Can an EPAC-owned constructor preserve a typed, ordered, provenance-bearing S0-through-S6 join tree such that every stored field has both a METAPAT spine role and an EPAC domain name, while bags remain explicitly non-structural sidecars?"
EVIDENCE_BOUNDARY = "METAPAT owns this exact semantic license and its catalog bindings. EPAC owns the schema, constructor, equality, serialization, replay, and domain evidence. UCNS retains any UCNS law and EDCM retains measurement authority. Passing deterministic tests establishes contract conformance only, not chemical, physical, empirical, or production validity."
EVIDENCE_REQUIREMENTS = (
    "The EPAC schema must represent every scale S0 through S6, a new identity at each recursive join, named ordered slots, positive k, explicit holes and leftovers, exact state metrics, and provenance.",
    "Closed-schema parsing must reject a bag presented as a tree, missing scales, inferred skip-scale joins, omitted holes, duplicate identities, unlicensed fields, and malformed provenance.",
    "Join-isomorphism tests must distinguish two trees with the same counts but different typed ordered structure and must keep visible and lifted records distinct.",
    "A deterministic public fixture and replay receipt must bind the exact METAPAT application identity and permit independent recovery without private construction state.",
    "Existing EPAC molecular-shape falsification must remain unchanged; subsequent comparisons may compare S3 tree to S3 tree only.",
)
UNRESOLVED = (
    "hmmm: Whether the typed multi-origin representation supports a useful native private operation that its public projection cannot efficiently reproduce remains unestablished.",
    "hmmm: No chemical or physical interpretation of EPAC phase, bearing, capacity, or S5 occupancy is licensed by this application.",
    "hmmm: Whether any later UCNS correspondence is useful must be licensed and tested separately without rewriting UCNS law.",
)


def _catalog_binding_rows() -> tuple[str, ...]:
    return tuple(
        f"| `{module_id}` | {role} | {statement} |"
        for module_id, role, statement in EPAC_JOIN_TERMS_BINDING_SPECS
    )


def _scale_rows() -> tuple[str, ...]:
    return tuple(
        f"| `{scale.split(maxsplit=1)[0]}` | {scale.split(maxsplit=1)[1]} |"
        for scale in SELECTED_SCALES
    )


def _source_pairs() -> tuple[tuple[str, str], ...]:
    pairs: list[tuple[str, str]] = [
        ("application-identity", "Status: **CROSS-DOMAIN-HYPOTHESIS / EPAC semantic license**"),
        ("application-identity", "Root impact: **none**"),
        (
            "application-identity",
            "METAPAT owns the spine vocabulary and this license. EPAC owns the typed join-term domain, implementation, and evidence. UCNS and EDCM retain their own law and measurement authority. No validity status transfers among them.",
        ),
    ]
    pairs.extend(("catalog-bindings", row) for row in _catalog_binding_rows())
    pairs.extend(("epac-scale-map", row) for row in _scale_rows())
    pairs.extend(("epac-domain-statements", statement) for statement in DOMAIN_STATEMENTS)
    pairs.extend(("recursive-question-form", line) for line in SHARED_QUESTION_FORM)
    pairs.extend(("transfers", f"- {statement}") for statement in TRANSFERS)
    pairs.extend(("does-not-transfer", f"- {statement}") for statement in DOES_NOT_TRANSFER)
    pairs.append(("working-question", WORKING_QUESTION))
    pairs.append(("evidence-boundary", EVIDENCE_BOUNDARY))
    pairs.extend(
        ("evidence-boundary", f"{index}. {statement}")
        for index, statement in enumerate(EVIDENCE_REQUIREMENTS, start=1)
    )
    pairs.extend(("hmmm", item.removeprefix("hmmm: ")) for item in UNRESOLVED)
    return tuple(pairs)


def epac_join_terms_application_module(
    catalog: MetapatSemanticCatalog | None = None,
) -> MetapatApplicationModule:
    selected = catalog or canonical_semantic_catalog()
    bindings = tuple(
        bind_catalog_module(
            semantic_module_by_id(module_id, selected),
            application_role=role,
            application_statement=statement,
        )
        for module_id, role, statement in EPAC_JOIN_TERMS_BINDING_SPECS
    )
    source_pairs = _source_pairs()
    refs = tuple(
        f"{SOURCE_DOCUMENT}#{anchor}::statement-{index}"
        for index, (anchor, _statement) in enumerate(source_pairs, start=1)
    )
    application = MetapatApplicationModule(
        application_id="metapat.application.epac_join_terms",
        application_version=EPAC_JOIN_TERMS_APPLICATION_VERSION,
        title="EPAC Typed Multi-Origin Join Terms",
        claim_status="CROSS-DOMAIN-HYPOTHESIS",
        domains=DOMAINS,
        selected_scales=SELECTED_SCALES,
        source_document=SOURCE_DOCUMENT,
        source_statement_refs=refs,
        source_statements=tuple(statement for _anchor, statement in source_pairs),
        catalog_version=selected.catalog_version,
        catalog_digest=selected.catalog_digest,
        catalog_bindings=bindings,
        domain_statements=DOMAIN_STATEMENTS,
        shared_question_form=SHARED_QUESTION_FORM,
        transfers=TRANSFERS,
        does_not_transfer=DOES_NOT_TRANSFER,
        working_question=WORKING_QUESTION,
        evidence_boundary=EVIDENCE_BOUNDARY,
        evidence_requirements=EVIDENCE_REQUIREMENTS,
        unresolved_constraints=UNRESOLVED,
    )
    validate_application_against_catalog(application, selected)
    return application


def epac_join_terms_application_digest() -> str:
    return epac_join_terms_application_module().application_digest


__all__ = [
    "EPAC_JOIN_TERMS_APPLICATION_VERSION",
    "EPAC_JOIN_TERMS_BINDING_SPECS",
    "epac_join_terms_application_digest",
    "epac_join_terms_application_module",
]
