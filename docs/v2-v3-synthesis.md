# METAPAT v2 → v3 Synthesis

Status: **FROZEN COMPARATIVE RESULT / proposed synthesis, not canon**

This record compares the last v2 root at `510e0171f4ecc6d1889e66bb66a8734c49c3b1fa` with merged v3 at `72bb6acdc1e635a10f662b640d5058a222a84eb7` against the same three catalog-bound applications:

- `docs/applications/quantum-magnetism.md`
- `docs/applications/three-phase-electromagnetic-pipe.md`
- `docs/applications/affixiation-harmonics.md`

The comparison is not a popularity vote between versions. The question is which distinctions survive application and where they belong.

## Result

**SYNTHESIS.**

v3 is the stronger root. v2 contains operational distinctions that remain useful, but several were placed too high in the ontology. The synthesis keeps v3 structure/action as root and recovers useful v2 content only at the lowest layer that the applications actually require.

No evidence from the three frozen applications requires restoring `energy-state`, `relation`, `gradient`, `registration`, `question`, or `distinction` as root axioms.

## Frozen application coverage

The three applications contain 45 catalog-binding uses in each version:

| Application | v2 bindings | v3 bindings | Application claim/evidence coverage |
|---|---:|---:|---|
| Quantum magnetism | 12 | 12 | preserved |
| Three-phase electromagnetic pipe | 20 | 20 | preserved |
| Affixiation / harmonics | 13 | 13 | preserved |
| **Total** | **45** | **45** | **45/45 carried** |

The substantive domain statements, transfer limits, evidence boundaries, working questions, and `hmmm` remained materially intact. The principal change was which METAPAT structure carried each application statement.

This establishes **coverage compatibility**, not superiority by itself.

## What v3 improved

### 1. State is no longer energy

v2 used `energy-state` as root and then defined scalar and vector as modes of it.

v3 separates:

```text
state          = metricable property of a thing
scalar         = state metric
vector         = alters state
transformation = resulting state change
energy         = derived from vector + state + transformation + time
```

The applications survived this replacement without losing a required claim. Their former `energy-state` uses map cleanly to `state`.

**Standing: v3 SURVIVED; v2 `energy-state` as root is DEPRECATED.**

### 2. Action is separated from resulting structure

v2 made `relation` a root noun.

v3 makes `relate` the root action and tensor the structure produced when simplexes relate.

That preserves relation without treating the result of action as a primitive.

**Standing: v3 SURVIVED; root `relation` is DEPRECATED and replaced by root `relate` plus derived relation/configuration.**

### 3. Recursion is explicit

v3 states:

```text
simplexes relate -> tensor emerges
tensor -> thing
thing + boundary + state -> simplex
repeat
```

This carries v2 formed-object/integration behavior with fewer independent primitives.

**Standing: v3 SURVIVED.**

### 4. Registration and question moved to the right layer

The applications still need registration and bounded unresolved questions, but neither requires them to be primitive ontology.

v3 already carries them as postulate/theory:

- registration: preserve, express, or transmit transformation;
- question: bounded unresolved state or relation available to transformation.

**Standing: v3 placement SURVIVED.**

## What v2 carried that v3 still needs

### A. Distinction

The engineering application still requires components and states to remain separately legible. v2 named this directly as `legible difference is distinction`.

But v2 also made distinction constitutive of boundary. That conflicts with v3's cleaner claim that observation does not create structure: two things may have a boundary whether or not an observer has distinguished it.

Synthesis:

```text
Distinction is legible difference between things, states, or relations.
Distinction makes structure addressable; it does not create the structure distinguished.
```

**Placement: derived legibility operator, not root primitive.**

### B. Boundary mediation

v3 correctly defines boundary minimally:

```text
Boundary is the thing between things.
```

v2 correctly noticed an important consequence: some boundaries participate in transformation rather than merely marking adjacency.

Synthesis:

```text
When a boundary thing participates as a simplex at the selected scale,
its state may participate in relation or transformation.
A change in that boundary-state may alter the resulting relation or transformation.
Whether and how it does so belongs to the applicable domain evidence.
```

A boundary is therefore **not automatically a simplex**. It closes as simplex only when the required boundary-and-state structure exists at the scale being modeled.

**Placement: theorem/theory consequence of Boundary + State + Simplex + Transformation.**

This preserves `boundary earns its keep` without loading behavior into the definition of boundary.

### C. Tensor simultaneity

Affixiation still requires relations that exist without temporal succession. v2 expressed this strongly as `without sequence, there is tensor`.

v3 derives tensor rather than treating it as primitive, but derivation need not itself be temporal.

Synthesis:

```text
A tensor is structure produced when simplexes relate.
A relation may be structurally present without sequential transformation.
Time appears when transformation is sequential, not merely because a tensor exists.
```

**Placement: theorem/theory consequence of Tensor + Relate + Time.**

This retains the useful content of `tensor precedes time` without making tensor ontologically primitive.

### D. State-metric difference; domain-qualified gradient

The quantum-magnetism and electromagnetic-pipe applications still use gradients in their domain prose and feedback structures. v3 correctly moved their METAPAT bindings from root `gradient` to scalar state metrics.

The synthesis should not re-import the physics/mathematics term `gradient` as a universal METAPAT operator.

Generic METAPAT relation:

```text
state-metric difference = difference among scalar measurements of related states
```

Domain specialization:

```text
When a domain supplies the ordered, geometric, differentiable, or other structure
required to define a gradient, that domain gradient may instantiate a
state-metric difference within the METAPAT mapping.
```

No universal gradient-to-vector law follows.

**Placement: `state-metric difference` may be derived generically; `gradient` remains domain-qualified.**

This preserves the useful application language while rejecting v2's overreach of `gradient dynamics are how vectors select direction` as a universal root law.

### E. Integration

Affixiation uses the idea that a relation can become a higher-scale object-whole while participants retain identity and provenance.

v3 already covers the generic structural part through `emerge` + recursive closure. Identity/provenance retention is an affixiation requirement, not a universal property of every emergent tensor.

Synthesis:

```text
Generic METAPAT: emergence + recursive closure may produce a higher-scale whole.
Affixiation: the higher-scale whole additionally preserves participant identity and provenance.
```

**Placement: generic structure is already covered by v3; `integration` remains application/theory vocabulary where needed.**

## Synthesized architecture

### Root structure

```text
Thing
Boundary
State
Simplex
Tensor
```

### Root action

```text
Relate
Emerge
Vector
```

### Measurement / result

```text
Scalar
Transformation
Time
Energy
```

### Derived operational layer

```text
Distinction            = legible difference; makes structure addressable
Relation               = configuration/result of things or simplexes relating
State-metric difference = difference among scalar measurements of related states
Boundary mediation     = stateful boundary-simplex participation may alter relation/transformation
Tensor simultaneity    = relation need not be sequential to exist as structure
Registration           = preservation/expression/transmission of transformation
Question               = bounded unresolved state or relation
Observer               = simplex performing registration
```

Domain/application vocabulary may specialize this layer:

```text
gradient    = domain-qualified state-metric structure where the domain defines one
integration = application/theory name for emergence into a higher-scale whole
```

The derived layer may grow or shrink without changing the root if later applications falsify, split, or refine an operator.

## Result against the three frozen cases

### Quantum magnetism

The synthesis retains v3 `state` and `scalar` separation. Physical potential gradients remain physics-defined gradients and map into METAPAT as measured state differences across declared relations.

No return to primitive `energy-state` or root `gradient` is required.

**SURVIVED.**

### Three-phase electromagnetic pipe

The synthesis preserves separately legible components (`distinction`), stateful boundary participation (`boundary mediation`), measured field/phase/thermal differences, domain-defined magnetic gradients, sequential transformation (`time`), sensor/log preservation (`registration`), and unresolved design bounds (`question`) without promoting them unnecessarily into root.

**SURVIVED.**

### Affixiation and time-agnostic harmonics

The synthesis preserves participant identity, pre-temporal relation, tensor emergence, recursive closure, and higher-scale affixiation. Tensor need not be primitive for a relation to exist without temporal succession.

**SURVIVED.**

## Comparative standing

```text
v2 root:        SURVIVED historically; overpacked
v3 root:        SURVIVED current frozen applications
v2 operational distinctions: PARTLY RETAINED, REPLACED IN PLACEMENT
synthesis:      SURVIVED the same three frozen application mappings
superiority:    PROVISIONAL — stronger by reduced primitive load and preserved coverage,
                not yet established against new independent domains
```

The synthesis is preferable to either version alone **for these frozen cases** because it preserves v3's smaller root while recovering the useful v2 distinctions without re-promoting domain vocabulary into universal ontology.

## Falsification conditions

The synthesis fails if a new application demonstrates any of the following:

1. `energy-state` is required as a root primitive and cannot be represented as state plus derived energy;
2. relation must exist as a primitive independently of `relate` and produced structure;
3. distinction is constitutive of boundary rather than merely required for legibility;
4. generic state-metric difference is insufficient and some stronger non-domain-specific operator is required;
5. tensor structure intrinsically requires sequence;
6. emergence plus recursive closure cannot carry the required higher-scale object structure;
7. a derived operator must become root to prevent contradiction or information loss.

Until such evidence appears, do not enlarge the root merely because v2 once placed a useful concept there.

## hmmm

The synthesis establishes placement against three existing applications, not completeness across all domains. A new independent application is the correct next adversary.

The two existing uses of `gradient` are both physics/engineering uses. They support retaining gradient as domain vocabulary, not promoting it back into METAPAT's general ontology.
