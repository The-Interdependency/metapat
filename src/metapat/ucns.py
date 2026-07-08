"""METAPAT-native UCNS bridge.

This module is intentionally narrow. It does not replace the external
``The-Interdependency/ucns`` algebra. It gives METAPAT a deterministic,
importable UCNS-shaped representation for root, primitive extension, and
Chapter Zero objects while the full external bridge remains unresolved.
"""

from __future__ import annotations

# === MODULE_BUILD ===
# id: metapat_ucns_bridge
#   module_name: metapat.ucns
#   module_kind: adapter
#   summary: provides METAPAT-native UCNS-shaped carriers for root doctrine and Chapter Zero objects
#   owner: The Interdependency
#   public_surface: UCNSObject, AnchorPayload, make_ucns_object, root_spine_ucns, primitive_extension_ucns, energy_question_ucns, chapter_zero_ucns, compose
#   internal_surface: _normalize_positions, _as_fraction, _lcm_all
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_ucns_bridge
#   rollout: importable_package
#   rollback: remove module exports and restore UCNS_SIDE_STATUS to planned
#   unresolved: external The-Interdependency/ucns package adapter, full UCNS algebra completeness, UCNS-gonol symbolic vertex table
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_ucns_bridge_docs
#   summary: documents the METAPAT-native UCNS bridge and its limits
#   audience: developer
#   source: UCNS_IMPLEMENTATION.md
#   covers: UCNSObject, AnchorPayload, carrier normalization, Chapter Zero payload object
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_ucns_bridge_capabilities
#   summary: represents METAPAT doctrine as normalized UCNS-shaped objects with anchors, face bits, and recursive payloads
#   exposes: metapat.ucns.root_spine_ucns, metapat.ucns.chapter_zero_ucns, metapat.ucns.compose
#   inputs: positions, face_bits, payloads, tags, canon statements
#   outputs: UCNSObject
#   boundaries: auth:none, storage:none, network:none, user_data:none
# === END CAPABILITIES ===

# === OWNERS ===
# id: metapat_ucns_bridge_owner
#   owner: The Interdependency
#   steward: Erin Spencer
#   review_required_for: public_api, canon, external_ucns_adapter
#   escalation: hmmm
# === END OWNERS ===

# === BOUNDARIES ===
# id: metapat_ucns_bridge_boundaries
#   summary: pure local representation with no external calls and no mutation
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: ucns_bridge_space_anchor_reserved
#   given: gonol constants are imported
#   then: vertex 0 is reserved as space-anchor and 156 vertices remain addressable
#   class: bridge
#   call: tests.test_ucns_bridge.test_gonol_space_anchor_constants
#
# id: ucns_bridge_root_spine_carrier
#   given: the METAPAT root spine is encoded
#   then: five root lines become five normalized anchors on intrinsic carrier 5
#   class: bridge
#   call: tests.test_ucns_bridge.test_root_spine_ucns_has_five_anchors
#
# id: ucns_bridge_chapter_zero_payloads
#   given: Chapter Zero is encoded
#   then: top-level anchors carry recursive payloads for root, primitive extension, and question
#   class: bridge
#   call: tests.test_ucns_bridge.test_chapter_zero_ucns_carries_recursive_payloads
# === END CONTRACTS ===

# === DEPENDENCIES ===
# id: metapat_ucns_bridge_dependencies
#   summary: UCNS bridge depends only on METAPAT canon constants and Python standard library
#   imports: metapat.canon, dataclasses, fractions, functools, math, typing
#   external: The-Interdependency/ucns unresolved
#   provides: metapat_ucns_bridge
#   class: runtime
#   owner: The Interdependency
# === END DEPENDENCIES ===

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from math import gcd
from typing import Iterable, Sequence

from .canon import ENERGY_THEORY_QUESTION, PRIMITIVE_EXTENSION, ROOT_SPINE

UNIT = None

GONOL_VERTEX_COUNT = 157
SPACE_ANCHOR_VERTEX = 0
ADDRESSABLE_GONOL_VERTICES = GONOL_VERTEX_COUNT - 1


def lcm(a: int, b: int) -> int:
    """Return least common multiple for non-negative integer carrier sizes."""

    if a < 0 or b < 0:
        raise ValueError("carrier factors must be non-negative")
    return a * b // gcd(a, b) if a and b else 0


def _lcm_all(values: Iterable[int]) -> int:
    values = tuple(values)
    if not values:
        return 1
    return reduce(lcm, values, 1)


def _as_fraction(value: Fraction | int | str) -> Fraction:
    fraction = value if isinstance(value, Fraction) else Fraction(value)
    return fraction % 1


def _normalize_positions(positions: Sequence[Fraction | int | str]) -> tuple[Fraction, ...]:
    if not positions:
        raise ValueError("UCNS object requires at least one anchor")
    raw = tuple(_as_fraction(position) for position in positions)
    theta0 = raw[0]
    return tuple((position - theta0) % 1 for position in raw)


def minimal_gonal_order(positions: Sequence[Fraction | int | str]) -> int:
    """
    Return the intrinsic carrier order induced by anchor positions.

    Positions are fractional turns on the normalized carrier circle. The first
    anchor is shifted to zero before denominators are read, matching UCNS
    carrier normalization.
    """

    normalized = _normalize_positions(positions)
    denominators = [position.denominator for position in normalized if position != 0]
    return _lcm_all(denominators)


# Alias preserves current METAPAT spelling in notes.
minimal_gonol_order = minimal_gonal_order


@dataclass(frozen=True)
class AnchorPayload:
    """One positive-side UCNS anchor plus optional recursive payload."""

    position: Fraction
    payload: "UCNSObject | None" = UNIT
    tag: str = ""

    def normalized_against(self, origin: Fraction) -> "AnchorPayload":
        return AnchorPayload((self.position - origin) % 1, self.payload, self.tag)


@dataclass(frozen=True)
class UCNSObject:
    """
    METAPAT-native UCNS-shaped carrier.

    This bridge preserves the load-bearing METAPAT invariants needed now:
    anchors, face bits, intrinsic carrier order, unit payloads, and recursive
    payloads. It does not claim to be the complete external UCNS algebra.
    """

    n_dec: int
    n_min: int
    anchors_pos: tuple[AnchorPayload, ...]
    faces_pos: tuple[int, ...]
    label: str = ""

    def __post_init__(self) -> None:
        if not self.anchors_pos:
            raise ValueError("UCNS object requires at least one anchor")
        if len(self.anchors_pos) != len(self.faces_pos):
            raise ValueError("anchors_pos and faces_pos must have the same length")
        if any(face not in (0, 1) for face in self.faces_pos):
            raise ValueError("faces_pos must contain only 0 or 1")

        raw_positions = tuple(anchor.position for anchor in self.anchors_pos)
        normalized_positions = _normalize_positions(raw_positions)
        computed_n_min = minimal_gonal_order(normalized_positions)

        if self.n_min != computed_n_min:
            raise ValueError(
                f"n_min={self.n_min} does not match intrinsic carrier {computed_n_min}"
            )
        if self.n_dec < self.n_min:
            raise ValueError("n_dec must be at least n_min")
        if self.n_dec % self.n_min != 0:
            raise ValueError(f"n_dec={self.n_dec} must be a multiple of n_min={self.n_min}")

        normalized_anchors = tuple(
            AnchorPayload(position, anchor.payload, anchor.tag)
            for position, anchor in zip(normalized_positions, self.anchors_pos)
        )
        object.__setattr__(self, "anchors_pos", normalized_anchors)

    @property
    def length(self) -> int:
        return len(self.anchors_pos)

    @property
    def positions(self) -> tuple[Fraction, ...]:
        return tuple(anchor.position for anchor in self.anchors_pos)

    @property
    def tags(self) -> tuple[str, ...]:
        return tuple(anchor.tag for anchor in self.anchors_pos)

    def has_recursive_payloads(self) -> bool:
        return any(anchor.payload is not UNIT for anchor in self.anchors_pos)

    def to_canonical_args(self) -> dict[str, object]:
        """
        Return arguments shaped for the external UCNS canonical constructor.

        External UCNS currently uses angles in [0, 4) and computes carrier
        denominators from half-turn angles. METAPAT positions are fractional
        turns, so the bridge maps position -> angle = 2 * position.
        """

        return {
            "n_dec": self.n_dec,
            "n_min": self.n_min,
            "A_plus": tuple(
                (position * 2, anchor.payload)
                for position, anchor in zip(self.positions, self.anchors_pos)
            ),
            "F_plus": self.faces_pos,
        }


def make_ucns_object(
    positions: Sequence[Fraction | int | str],
    *,
    face_bits: Sequence[int] | None = None,
    payloads: Sequence[UCNSObject | None] | None = None,
    tags: Sequence[str] | None = None,
    label: str = "",
    n_dec: int | None = None,
) -> UCNSObject:
    """Build a normalized METAPAT UCNS object from anchor positions."""

    normalized = _normalize_positions(positions)
    n_min = minimal_gonal_order(normalized)
    declared_n = n_min if n_dec is None else n_dec

    length = len(normalized)
    faces = tuple(0 for _ in range(length)) if face_bits is None else tuple(face_bits)
    payload_tuple = tuple(UNIT for _ in range(length)) if payloads is None else tuple(payloads)
    tag_tuple = tuple("" for _ in range(length)) if tags is None else tuple(tags)

    if len(faces) != length:
        raise ValueError("face_bits length must match positions length")
    if len(payload_tuple) != length:
        raise ValueError("payloads length must match positions length")
    if len(tag_tuple) != length:
        raise ValueError("tags length must match positions length")

    anchors = tuple(
        AnchorPayload(position=position, payload=payload, tag=tag)
        for position, payload, tag in zip(normalized, payload_tuple, tag_tuple)
    )
    return UCNSObject(
        n_dec=declared_n,
        n_min=n_min,
        anchors_pos=anchors,
        faces_pos=faces,
        label=label,
    )


def ucns_from_statements(statements: Sequence[str], *, label: str, face_bit: int = 0) -> UCNSObject:
    """Represent ordered statements as evenly spaced UCNS anchors."""

    if face_bit not in (0, 1):
        raise ValueError("face_bit must be 0 or 1")
    if not statements:
        raise ValueError("statements must not be empty")

    order = len(statements)
    positions = tuple(Fraction(index, order) for index in range(order))
    return make_ucns_object(
        positions,
        face_bits=tuple(face_bit for _ in range(order)),
        tags=tuple(statements),
        label=label,
    )


def compose(left: UCNSObject | None, right: UCNSObject | None, *, label: str = "") -> UCNSObject | None:
    """
    Ordered UCNS-style product over METAPAT bridge objects.

    Face bits compose by XOR. Recursive payloads compose if both are present;
    otherwise the present payload is carried forward.
    """

    if left is UNIT:
        return right
    if right is UNIT:
        return left

    positions: list[Fraction] = []
    faces: list[int] = []
    payloads: list[UCNSObject | None] = []
    tags: list[str] = []

    beta0 = right.positions[0]
    for left_index, left_anchor in enumerate(left.anchors_pos):
        for right_index, right_anchor in enumerate(right.anchors_pos):
            positions.append((left_anchor.position + (right_anchor.position - beta0)) % 1)
            faces.append(left.faces_pos[left_index] ^ right.faces_pos[right_index])
            if left_anchor.payload is not UNIT and right_anchor.payload is not UNIT:
                payload = compose(left_anchor.payload, right_anchor.payload)
            elif left_anchor.payload is not UNIT:
                payload = left_anchor.payload
            else:
                payload = right_anchor.payload
            payloads.append(payload)
            if left_anchor.tag and right_anchor.tag:
                tags.append(f"{left_anchor.tag} ⊠ {right_anchor.tag}")
            else:
                tags.append(left_anchor.tag or right_anchor.tag)

    n_dec = _lcm_all((left.n_dec, right.n_dec))
    return make_ucns_object(
        positions,
        face_bits=faces,
        payloads=payloads,
        tags=tags,
        label=label,
        n_dec=n_dec,
    )


def root_spine_ucns() -> UCNSObject:
    """Return the current METAPAT root spine as a UCNS object."""

    return ucns_from_statements(ROOT_SPINE, label="metapat.root_spine")


def primitive_extension_ucns() -> UCNSObject:
    """Return the current primitive extension as a UCNS object."""

    return ucns_from_statements(PRIMITIVE_EXTENSION, label="metapat.primitive_extension")


def energy_question_ucns() -> UCNSObject:
    """Return the Energy Theory question as a one-anchor UCNS object."""

    return ucns_from_statements((ENERGY_THEORY_QUESTION,), label="metapat.energy_question")


def chapter_zero_ucns() -> UCNSObject:
    """
    Return a payload-bearing UCNS object for Chapter Zero.

    The three top-level anchors are root spine, primitive extension, and
    question. Each anchor carries its own recursive UCNS payload.
    """

    payloads = (root_spine_ucns(), primitive_extension_ucns(), energy_question_ucns())
    return make_ucns_object(
        (Fraction(0, 1), Fraction(1, 3), Fraction(2, 3)),
        payloads=payloads,
        tags=("root_spine", "primitive_extension", "energy_question"),
        label="metapat.chapter_zero",
    )


__all__ = [
    "ADDRESSABLE_GONOL_VERTICES",
    "AnchorPayload",
    "GONOL_VERTEX_COUNT",
    "SPACE_ANCHOR_VERTEX",
    "UCNSObject",
    "UNIT",
    "chapter_zero_ucns",
    "compose",
    "energy_question_ucns",
    "lcm",
    "make_ucns_object",
    "minimal_gonal_order",
    "minimal_gonol_order",
    "primitive_extension_ucns",
    "root_spine_ucns",
    "ucns_from_statements",
]
