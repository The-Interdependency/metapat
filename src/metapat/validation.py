"""Executable internal reductions for the current METAPAT canon."""

# === MODULE_BUILD ===
# id: metapat_validation_contracts
#   module_name: metapat.validation
#   module_kind: service
#   summary: executable internal reductions for current root, action, measurement, sequence, and domain-qualification contracts
#   owner: The Interdependency
#   public_surface: boundary_requires_multiplicity, simplex_closes, tensor_emerges, recursive_closure, vector_inferred_by_scalar, transformation_produces_time, domain_term_is_qualified
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts
#   rollout: importable_package
#   rollback: restore prior canon-bound validation helpers
#   requires: metapat_canon_core
#   since: 2026-09-14
#   unresolved: external empirical and formal validity remain outside these internal contract predicates
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: boundary_requires_multiple_things
#   given: candidate things participating in a boundary
#   then: at least two distinct thing instances are required
#   class: canon_contract
#
# id: simplex_closes_from_thing_boundary_state
#   given: thing, boundary, and state candidates
#   then: simplex closure requires all three to be present
#   class: canon_contract
#
# id: tensor_emerges_from_related_simplexes
#   given: multiple simplex candidates and a declared relation
#   then: encoded tensor emergence requires multiplicity and relation
#   class: canon_contract
#
# id: recursive_tensor_closure
#   given: a tensor candidate with boundary and state
#   then: the encoded simplex closure condition is reused
#   class: canon_contract
#
# id: vector_inference_from_scalar_change
#   given: two present scalar observations
#   then: encoded vector inference requires an observed scalar change and fails closed when either observation is missing
#   class: canon_contract
#
# id: sequential_transformation_produces_time
#   given: transformations are supplied in sequence
#   then: encoded time condition requires at least two ordered transformations
#   class: canon_contract
#
# id: domain_term_requires_domain_license
#   given: structural similarity and an explicit domain-license flag are supplied
#   then: the domain term is qualified only when the applicable domain independently licenses it; structural similarity alone is insufficient
#   class: canon_contract
# === END CONTRACTS ===


def boundary_requires_multiplicity(things: tuple[object, ...]) -> bool:
    return len({id(thing) for thing in things}) >= 2


def simplex_closes(thing: object, boundary: object, state: object) -> bool:
    return thing is not None and boundary is not None and state is not None


def tensor_emerges(simplexes: tuple[object, ...], related: bool) -> bool:
    return len(simplexes) >= 2 and related is True


def recursive_closure(tensor: object, boundary: object, state: object) -> bool:
    return simplex_closes(tensor, boundary, state)


def vector_inferred_by_scalar(scalar_before: object, scalar_after: object) -> bool:
    return (
        scalar_before is not None
        and scalar_after is not None
        and scalar_before != scalar_after
    )


def transformation_produces_time(transformations: tuple[object, ...]) -> bool:
    return len(transformations) >= 2


def domain_term_is_qualified(*, domain_licenses_term: bool, structurally_similar: bool = False) -> bool:
    """Return whether a source-domain term may be applied in the target domain.

    ``structurally_similar`` is accepted explicitly so callers cannot mistake
    similarity for authorization; it never substitutes for domain license.
    """

    _ = structurally_similar
    return domain_licenses_term is True


__all__ = [
    "boundary_requires_multiplicity",
    "domain_term_is_qualified",
    "recursive_closure",
    "simplex_closes",
    "tensor_emerges",
    "transformation_produces_time",
    "vector_inferred_by_scalar",
]
