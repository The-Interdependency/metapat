"""Tests for the METAPAT-native UCNS bridge."""

from fractions import Fraction
import unittest

from src.metapat.canon import ENERGY_THEORY_QUESTION, PRIMITIVE_EXTENSION, ROOT_SPINE
from src.metapat.ucns import (
    ADDRESSABLE_GONOL_VERTICES,
    GONOL_VERTEX_COUNT,
    SPACE_ANCHOR_VERTEX,
    chapter_zero_ucns,
    compose,
    energy_question_ucns,
    make_ucns_object,
    minimal_gonal_order,
    minimal_gonol_order,
    primitive_extension_ucns,
    root_spine_ucns,
)


def test_gonol_space_anchor_constants() -> None:
    assert GONOL_VERTEX_COUNT == 157
    assert SPACE_ANCHOR_VERTEX == 0
    assert ADDRESSABLE_GONOL_VERTICES == 156


def test_minimal_gonal_order_normalizes_origin() -> None:
    positions = (Fraction(3, 7), Fraction(4, 7), Fraction(5, 7))
    assert minimal_gonal_order(positions) == 7
    assert minimal_gonol_order(positions) == 7


def test_root_spine_ucns_has_five_anchors() -> None:
    obj = root_spine_ucns()
    assert obj.label == "metapat.root_spine"
    assert obj.n_min == 5
    assert obj.n_dec == 5
    assert obj.length == 5
    assert obj.faces_pos == (0, 0, 0, 0, 0)
    assert obj.tags == ROOT_SPINE


def test_primitive_extension_ucns_has_four_anchors() -> None:
    obj = primitive_extension_ucns()
    assert obj.label == "metapat.primitive_extension"
    assert obj.n_min == 4
    assert obj.length == 4
    assert obj.tags == PRIMITIVE_EXTENSION


def test_energy_question_ucns_is_single_anchor() -> None:
    obj = energy_question_ucns()
    assert obj.label == "metapat.energy_question"
    assert obj.n_min == 1
    assert obj.length == 1
    assert obj.tags == (ENERGY_THEORY_QUESTION,)


def test_chapter_zero_ucns_carries_recursive_payloads() -> None:
    obj = chapter_zero_ucns()
    assert obj.label == "metapat.chapter_zero"
    assert obj.n_min == 3
    assert obj.length == 3
    assert obj.tags == ("root_spine", "primitive_extension", "energy_question")
    assert obj.has_recursive_payloads()
    assert obj.anchors_pos[0].payload.label == "metapat.root_spine"
    assert obj.anchors_pos[1].payload.label == "metapat.primitive_extension"
    assert obj.anchors_pos[2].payload.label == "metapat.energy_question"


def test_compose_multiplies_length_and_xors_faces() -> None:
    left = make_ucns_object(
        (Fraction(0), Fraction(1, 2)),
        face_bits=(0, 1),
        tags=("left_a", "left_b"),
        label="left",
    )
    right = make_ucns_object(
        (Fraction(0), Fraction(1, 2)),
        face_bits=(1, 0),
        tags=("right_a", "right_b"),
        label="right",
    )
    product = compose(left, right, label="product")
    assert product.label == "product"
    assert product.length == 4
    assert product.n_min == 2
    assert product.faces_pos == (1, 0, 0, 1)
    assert product.positions == (Fraction(0), Fraction(1, 2), Fraction(1, 2), Fraction(0))


def test_to_canonical_args_maps_turns_to_half_turn_angles() -> None:
    obj = make_ucns_object((Fraction(0), Fraction(1, 2)), label="bridge")
    args = obj.to_canonical_args()
    assert args["n_dec"] == 2
    assert args["n_min"] == 2
    assert args["A_plus"] == ((Fraction(0), None), (Fraction(1), None))
    assert args["F_plus"] == (0, 0)


class MetapatUCNSBridgeTests(unittest.TestCase):
    def test_00_gonol_space_anchor_constants(self) -> None:
        test_gonol_space_anchor_constants()

    def test_01_minimal_gonal_order_normalizes_origin(self) -> None:
        test_minimal_gonal_order_normalizes_origin()

    def test_02_root_spine_ucns_has_five_anchors(self) -> None:
        test_root_spine_ucns_has_five_anchors()

    def test_03_primitive_extension_ucns_has_four_anchors(self) -> None:
        test_primitive_extension_ucns_has_four_anchors()

    def test_04_energy_question_ucns_is_single_anchor(self) -> None:
        test_energy_question_ucns_is_single_anchor()

    def test_05_chapter_zero_ucns_carries_recursive_payloads(self) -> None:
        test_chapter_zero_ucns_carries_recursive_payloads()

    def test_06_compose_multiplies_length_and_xors_faces(self) -> None:
        test_compose_multiplies_length_and_xors_faces()

    def test_07_to_canonical_args_maps_turns_to_half_turn_angles(self) -> None:
        test_to_canonical_args_maps_turns_to_half_turn_angles()


if __name__ == "__main__":
    unittest.main()
