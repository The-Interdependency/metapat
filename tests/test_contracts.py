"""Executable canon contract tests for the installed METAPAT v4 surface."""

# === CHECKS ===
# id: check_root_spine_exact
#   proves: metapat_root_spine_exact
#   call: self::test_root_spine_contains_current_axioms
#   mutates: none
#   cleanup: none
#
# id: check_time_registration_separated
#   proves: metapat_time_not_registration
#   call: self::test_time_and_registration_are_separated
#   mutates: none
#   cleanup: none
#
# id: check_boundary_multiplicity
#   proves: boundary_requires_multiple_things
#   call: self::test_boundary_requires_multiplicity
#   mutates: none
#   cleanup: none
#
# id: check_simplex_closure
#   proves: simplex_closes_from_thing_boundary_state
#   call: self::test_simplex_closes
#   mutates: none
#   cleanup: none
#
# id: check_tensor_emergence
#   proves: tensor_emerges_from_related_simplexes
#   call: self::test_tensor_emerges
#   mutates: none
#   cleanup: none
#
# id: check_recursive_closure
#   proves: recursive_tensor_closure
#   call: self::test_recursive_closure
#   mutates: none
#   cleanup: none
#
# id: check_vector_inference
#   proves: vector_inference_from_scalar_change
#   call: self::test_vector_inferred_by_scalar
#   mutates: none
#   cleanup: none
#
# id: check_transformation_time
#   proves: sequential_transformation_produces_time
#   call: self::test_transformation_produces_time
#   mutates: none
#   cleanup: none
#
# id: check_domain_term_qualification
#   proves: domain_term_requires_domain_license
#   call: self::test_domain_term_is_qualified
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import unittest

from metapat import TIME_DEFINITION, definitions, root_spine
from metapat.validation import (
    boundary_requires_multiplicity,
    domain_term_is_qualified,
    recursive_closure,
    simplex_closes,
    tensor_emerges,
    transformation_produces_time,
    vector_inferred_by_scalar,
)


def test_root_spine_contains_current_axioms() -> None:
    assert root_spine() == (
        "Thing is that which is.",
        "Boundary is the thing between things.",
        "State is a metricable property of a thing.",
        "A simplex is a thing with boundary and state.",
        "A tensor is structure produced when simplexes relate.",
    )


def test_time_and_registration_are_separated() -> None:
    defs = definitions()
    assert defs["METAPAT"] == "Meta Energy Theory — Axioms, Postulates, Theorems, and Theories."
    assert defs["time"] == "Time is sequential transformation."
    assert "preserve, express, or transmit" in defs["registration"]
    assert defs["time"] != defs["registration"]
    assert TIME_DEFINITION == defs["time"]


def test_boundary_requires_multiplicity() -> None:
    assert boundary_requires_multiplicity(("a", "b"))
    assert not boundary_requires_multiplicity(("a",))


def test_simplex_closes() -> None:
    assert simplex_closes("thing", "boundary", "state")
    assert not simplex_closes("thing", None, "state")


def test_tensor_emerges() -> None:
    assert tensor_emerges(("simplex-a", "simplex-b"), True)
    assert not tensor_emerges(("simplex-a",), True)
    assert not tensor_emerges(("simplex-a", "simplex-b"), False)


def test_recursive_closure() -> None:
    assert recursive_closure("tensor", "boundary", "state")
    assert not recursive_closure("tensor", "boundary", None)


def test_vector_inferred_by_scalar() -> None:
    assert vector_inferred_by_scalar(1, 2)
    assert not vector_inferred_by_scalar(1, 1)


def test_transformation_produces_time() -> None:
    assert transformation_produces_time(("t1", "t2"))
    assert not transformation_produces_time(("t1",))


def test_domain_term_is_qualified() -> None:
    assert domain_term_is_qualified(domain_licenses_term=True)
    assert not domain_term_is_qualified(domain_licenses_term=False)
    assert not domain_term_is_qualified(
        domain_licenses_term=False,
        structurally_similar=True,
    )


class MetapatContractTests(unittest.TestCase):
    def test_root_spine_contains_current_axioms(self) -> None:
        test_root_spine_contains_current_axioms()

    def test_time_and_registration_are_separated(self) -> None:
        test_time_and_registration_are_separated()

    def test_01_boundary_requires_multiplicity(self) -> None:
        test_boundary_requires_multiplicity()

    def test_02_simplex_closes(self) -> None:
        test_simplex_closes()

    def test_03_tensor_emerges(self) -> None:
        test_tensor_emerges()

    def test_04_recursive_closure(self) -> None:
        test_recursive_closure()

    def test_05_vector_inferred_by_scalar(self) -> None:
        test_vector_inferred_by_scalar()

    def test_06_transformation_produces_time(self) -> None:
        test_transformation_produces_time()

    def test_07_domain_term_is_qualified(self) -> None:
        test_domain_term_is_qualified()
