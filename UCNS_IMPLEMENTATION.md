# UCNS Implementation

METAPAT now contains a narrow, internal UCNS-shaped bridge.

This bridge lives at:

```text
src/metapat/ucns.py
```

It is tested by:

```text
tests/test_ucns_bridge.py
```

## Scope

This is a METAPAT-native implementation layer.

It does not replace the external `The-Interdependency/ucns` algebra.

It exists to let METAPAT represent its own root, primitive extension, and Chapter Zero objects as UCNS-shaped carriers while the full external adapter remains unresolved.

## Implemented

The bridge implements:

1. `AnchorPayload` — one positive-side anchor plus optional recursive payload;
2. `UCNSObject` — a normalized carrier object with anchors, face bits, intrinsic carrier order, and label;
3. `minimal_gonal_order` / `minimal_gonol_order` — intrinsic carrier order from normalized fractional-turn anchors;
4. `make_ucns_object` — object factory with validation;
5. `ucns_from_statements` — ordered statement encoding as evenly spaced anchors;
6. `compose` — ordered UCNS-style product with XOR face-bit composition;
7. `root_spine_ucns` — current METAPAT root spine as a five-anchor carrier;
8. `primitive_extension_ucns` — primitive extension as a four-anchor carrier;
9. `energy_question_ucns` — the Energy Theory question as a one-anchor carrier;
10. `chapter_zero_ucns` — payload-bearing carrier with root, primitive extension, and question as recursive payloads.

## Gonol constants

```text
GONOL_VERTEX_COUNT = 157
SPACE_ANCHOR_VERTEX = 0
ADDRESSABLE_GONOL_VERTICES = 156
```

The space-anchor is reserved.

The 156 remaining vertices are addressable.

The bridge does not yet define the full symbolic vertex table.

## Carrier convention

METAPAT bridge positions are fractional turns in `[0, 1)`.

The first anchor is normalized to zero.

The intrinsic carrier order is the least common multiple of non-zero normalized denominators.

The external UCNS canonical constructor uses half-turn angles. The bridge exposes `to_canonical_args()` to map:

```text
position -> angle = 2 * position
```

## Face bits

Face bits are stored as `0` or `1` parallel to anchors.

Composition uses XOR.

No extra semantic claim is attached to face bits inside METAPAT until a specific mapping is declared.

## Recursive payloads

`None` is the unit payload.

A payload may itself be a `UCNSObject`.

`chapter_zero_ucns()` uses recursive payloads:

```text
root_spine
primitive_extension
energy_question
```

## External UCNS status

```text
external The-Interdependency/ucns adapter: hmmm
full UCNS algebra completeness inside METAPAT: not claimed
UCNS-gonol symbolic vertex table: hmmm
```

The current bridge is sufficient for METAPAT-local representation and tests.

It is not yet sufficient for full UCNS algebra, theorem transfer, or EDCM measurement construction.
