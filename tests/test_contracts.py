"""Executable contract tests for METAPAT.

These tests are deliberately small. They protect the current Chapter Zero spine
without pretending to formalize the full ontology.
"""

import unittest

from src.metapat.canon import TIME_DEFINITION, definitions, root_spine
from src.metapat.validation import (
    boundary_earns_its_keep,
    consciousness_is_optional,
    observer_role_by_registration,
    registration_is_not_time,
    tensor_precedes_time,
)


def test_root_spine_contains_current_axioms() -> None:
    assert root_spine() == (
        "Legible difference is distinction.",
        "Distinction defines boundaries.",
        "Boundaries define simplex.",
        "Boundary is simplex of distinction.",
        "Simplex holds or modifies energy in a state of being.",
    )


def test_time_and_registration_are_separated() -> None:
    defs = definitions()
    assert defs["time"] == "Time is sequential tensor alteration."
    assert "preserve, express, or transmit" in defs["registration"]
    assert defs["time"] != defs["registration"]
    assert TIME_DEFINITION == defs["time"]


def test_boundary_change_changes_outcome() -> None:
    assert boundary_earns_its_keep(
        source_state="fixed_source",
        target_state="fixed_target",
        boundary_state_a="open",
        boundary_state_b="filtered",
        outcome_a="passes",
        outcome_b="delayed",
    )
    assert not boundary_earns_its_keep(
        source_state="fixed_source",
        target_state="fixed_target",
        boundary_state_a="same",
        boundary_state_b="same",
        outcome_a="passes",
        outcome_b="delayed",
    )


def test_tensor_precedes_time() -> None:
    tensor_state = {"a": "held", "b": "held"}
    sequenced = (tensor_state, {"a": "altered", "b": "held"})
    assert tensor_precedes_time(tensor_state, sequenced)
    assert not tensor_precedes_time(None, sequenced)
    assert not tensor_precedes_time(tensor_state, (tensor_state,))


def test_registration_is_not_time() -> None:
    sequence = ({"t": 0}, {"t": 1})
    assert registration_is_not_time(sequence, None)
    assert registration_is_not_time(sequence, sequence)
    assert not registration_is_not_time(({"t": 0},), None)


def test_observer_role_by_registration() -> None:
    sequence = ({"t": 0}, {"t": 1})
    observer_simplex = {"registered": sequence}
    merely_present_simplex = {"state": "present"}
    assert observer_role_by_registration(observer_simplex, sequence)
    assert not observer_role_by_registration(merely_present_simplex, sequence)


def test_consciousness_is_optional() -> None:
    nonconscious_registration = ({"layer": 1}, {"layer": 2})
    conscious_story = "I remember the alteration."
    assert consciousness_is_optional(nonconscious_registration, conscious_story)
    assert not consciousness_is_optional(None, conscious_story)
    assert not consciousness_is_optional(nonconscious_registration, "")


class MetapatContractTests(unittest.TestCase):
    def test_root_spine_contains_current_axioms(self) -> None:
        test_root_spine_contains_current_axioms()

    def test_time_and_registration_are_separated(self) -> None:
        test_time_and_registration_are_separated()

    def test_01_boundary_earns_its_keep(self) -> None:
        test_boundary_change_changes_outcome()

    def test_02_tensor_precedes_time(self) -> None:
        test_tensor_precedes_time()

    def test_03_registration_is_not_time(self) -> None:
        test_registration_is_not_time()

    def test_04_observer_role_by_registration(self) -> None:
        test_observer_role_by_registration()

    def test_05_consciousness_is_optional(self) -> None:
        test_consciousness_is_optional()
