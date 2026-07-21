# Three-phase electromagnetic-pipe application record

## Purpose

`metapat.electromagnetic_pipe` preserves the current three-phase nested electromagnetic-pipe handoff as two linked surfaces:

1. an `EMPIRICAL-FRONTIER` `MetapatApplicationModule` bound to exact semantic-catalog identities;
2. a strict `ElectromagneticPipeDesign` record carrying the load-bearing engineering topology and unresolved experiment program.

Neither surface validates device performance.

## Control identity

```text
radial layers: 3
handednesses per layer: 2
phases per handedness: 3
phase circuits: 18
three-phase systems: 6
```

The natural control object is one three-phase vector per handedness per radial layer. The eighteen physical phase circuits remain separately measurable and isolatable, but they are not modeled as eighteen unrelated magnetic commands.

## Typed design surfaces

`WindingLayerSpec` preserves:

- radial order;
- wire gauge;
- turns per inch;
- three clockwise phases;
- three widdershins phases;
- two three-phase systems per radial layer.

`AlloyCandidate` preserves atomic-percent composition and rejects candidates that do not satisfy:

```text
Fe + Co + Ni = 75
Cr = 15
Mn = 10
total = 100
```

`ElectromagneticPipeDesign` preserves:

- three-meter assembly length;
- three-inch outer-pipe diameter;
- three iron pipes and three winding layers;
- current-command and voltage-compliance roles;
- drive modes and unresolved spatial phase geometry;
- ceramic-coated magnetic eddy-current attractors, explicitly not bearings;
- measurement requirements;
- normal-operation constraints;
- extreme-fault objectives;
- high-voltage and vacuum-insulation requirements;
- protection-distance status;
- twelve immediate next-work items;
- five alloy-search candidates;
- all unresolved `hmmm` boundaries.

## Evidence firewall

The following fields are required to remain false:

```text
electromagnetic_validity_claim
alloy_validity_claim
insulation_validity_claim
fault_containment_validity_claim
spacecraft_safety_validity_claim
```

The nested application record separately keeps METAPAT validity, domain validity, measurement validity, UCNS theorem transfer, and UCNS topology claims false.

Fault statements are objectives to test. Ceramic containment, molten-copper isolation, absence of conductive spray, and absence of spacecraft fire are not represented as demonstrated outcomes.

## Source and fixture

Human source:

```text
docs/applications/three-phase-electromagnetic-pipe.md
```

Packaged generated fixture:

```text
metapat/fixtures/three-phase-electromagnetic-pipe-v1.json
```

Generation and verification:

```bash
python tools/generate_application_fixtures.py
python tools/generate_application_fixtures.py --check
python -m pytest -q tests/test_electromagnetic_pipe.py
```

## hmmm

The strict record prevents unresolved engineering values from disappearing, but it cannot supply them. Frequency, phase current, voltage interpretation, target field, shielding attenuation, desired phase shift, attractor geometry, temperatures, protection distance, alloy microstructure, and heat treatment remain living experimental work.
