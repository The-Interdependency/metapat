# EPAC typed multi-origin join terms

## Application identity

Status: **CROSS-DOMAIN-HYPOTHESIS / EPAC semantic license**

Root impact: **none**

METAPAT owns the spine vocabulary and this license. EPAC owns the typed join-term domain, implementation, and evidence. UCNS and EDCM retain their own law and measurement authority. No validity status transfers among them.

## Catalog bindings

| Catalog module | EPAC application role | Licensed statement |
|---|---|---|
| `metapat.root_spine` | customs-boundary | METAPAT supplies the semantic spine while EPAC retains its domain-qualified names, schemas, constructors, and evidence obligations. |
| `metapat.axiom.1.thing` | stored-join-term | EPAC uses Thing as the semantic role of one stored typed join term, not a formula bag, residue list, or count. |
| `metapat.axiom.2.boundary` | join-boundary | EPAC uses Boundary for named ordered slots, explicit holes and leftovers, and the stored window k. |
| `metapat.axiom.3.state` | origin-state | EPAC uses State for domain-qualified phase and capacity as metricable properties of a declared origin; stored property values are not scalar observations. |
| `metapat.axiom.4.simplex` | scale-origin | EPAC treats one complete scale origin O(S_n), with its boundary and state, as a Simplex-role object. |
| `metapat.axiom.5.tensor` | multi-origin-tensor | EPAC uses Tensor for the structure formed by all declared S0 through S6 origins and their authored relations; a flattened bag is not that object. |
| `metapat.axiom.6.relate` | authored-near-join | EPAC records only authored adjacent-scale joins and does not infer ancestry from analogy, shared counts, or shared geometry. |
| `metapat.axiom.7.emerge` | recursive-origin | EPAC may store join(O(S_n)) as a new identity O(S_{n+1}) while retaining its ordered constituent identities and provenance. |
| `metapat.axiom.9.scalar` | state-metric | EPAC uses Scalar for separately identified phase, capacity, slot-facing, and occupancy metrics or readouts of named state properties; a readout names its origin, measured property, and measurement rule and is not the state itself. |
| `metapat.axiom.10.transformation` | join-transformation | EPAC uses Transformation only for the resulting before/after change of a named state property of an identified thing caused by a declared join action; the action, a new origin identity, or different values at unrelated origins alone are not that result. |
| `metapat.axiom.11.time` | transformation-sequence | EPAC uses Time only when evidence establishes that at least two resulting state changes actually occurred sequentially; registration may preserve that sequence, but sorting records, sequence numbers, and structural scale order cannot create it or establish physical time. |
| `metapat.axiom.12.domain_qualification` | domain-customs | Every transferred spine role remains paired with an EPAC domain name; structural recurrence alone transfers no chemical, physical, energetic, or UCNS meaning. |

## EPAC scale map

| Scale | EPAC-qualified name |
|---|---|
| `S0` | subatomic slot |
| `S1` | atomic |
| `S2` | join/arity |
| `S3` | embed |
| `S4` | electronic state |
| `S5` | EPAC energy readout |
| `S6` | ensemble |

## EPAC domain statements

An EPAC join term stores named ordered slots, explicit holes and leftovers, a positive window k, exact origin state, and provenance; omission is not a representation of zero.

At each adjacent scale, join(O(S_n)) may be stored as a new identity O(S_{n+1}); recursive construction does not erase or contract the child identities that establish the join.

The EPAC tensor-role object contains every declared origin S0 through S6 and its authored adjacent-scale relations; a formula bag or subset fill cannot substitute for that structure.

EPAC join equality is join-isomorphism over typed ordered structure and state, not equality of counts, formulas, residue bags, or visible projections.

Visible and lifted phase records remain distinct EPAC objects when their declared identities or coordinates differ.

S5 energy readout is an EPAC-qualified functional of occupancy and is not a fourth circle, a universal energy primitive, or evidence of physical energy coupling.

## Recursive question form

typed origin O(S_n)

-> named ordered slots including holes and leftovers

-> authored adjacent-scale join

-> new identity O(S_{n+1})

-> preserved source identities and provenance

-> complete S0-through-S6 relational structure

## Transfers

- The spine roles Thing, Boundary, State, Simplex, Tensor, and Scalar may label their declared EPAC counterparts; Transformation and Time require their stated result and occurrence evidence, and this application grants no Vector binding.
- A bounded lower-scale whole may participate in an authored adjacent-scale relation and the joined whole may receive a new identity.
- Ordered constituent identity, explicit holes and leftovers, state properties, separately identified readouts, and provenance may remain addressable across recursive construction.
- Exact deterministic serialization and replay may test whether an EPAC implementation preserves the licensed distinctions.

## Does not transfer

- Static bearing inferred from slot-facing signs remains an EPAC readout; no Vector role is licensed without a separately established state-altering operation and measured resulting change.

- This license does not transfer a UCNS coordinate, phase law, topology, theorem status, gonol identity, or implementation into EPAC.
- EPAC phase is not chemistry phase, and visible or lifted coordinates acquire no physical meaning merely because they are stored.
- S5 naming does not establish energy coupling, conservation, entropy, force, field, or empirical physical validity.
- Shared shape, count, phase, vocabulary, or geometry does not establish ancestry or authorize an inferred join.
- A formula bag, residue collection, contracted cardinality, subset fill, or gravity-point registry is not licensed as the multi-origin tensor-role object.
- METAPAT licensing does not validate EPAC implementation correctness, molecular geometry, production suitability, or external-domain truth.

## Working question

Can an EPAC-owned constructor preserve a typed, ordered, provenance-bearing S0-through-S6 join tree such that every stored field has both a METAPAT spine role and an EPAC domain name, while bags remain explicitly non-structural sidecars?

## Evidence boundary

METAPAT owns this exact semantic license and its catalog bindings. EPAC owns the schema, constructor, equality, serialization, replay, and domain evidence. UCNS retains any UCNS law and EDCM retains measurement authority. Passing deterministic tests establishes contract conformance only, not chemical, physical, empirical, or production validity.

1. The EPAC schema must represent every scale S0 through S6, a new identity at each recursive join, named ordered slots, positive k, explicit holes and leftovers, exact state properties, separately identified readouts, and provenance.
2. Closed-schema parsing must reject a bag presented as a tree, missing scales, inferred skip-scale joins, omitted holes, duplicate identities, unlicensed fields, and malformed provenance.
3. Join-isomorphism tests must distinguish two trees with the same counts but different typed ordered structure and must keep visible and lifted records distinct.
4. A deterministic public fixture and replay receipt must bind the exact METAPAT application identity and permit independent recovery without private construction state.
5. Existing EPAC molecular-shape falsification must remain unchanged; subsequent comparisons may compare S3 tree to S3 tree only.
6. State and scalar evidence must identify the origin and metricable property separately from each readout and its measurement rule; storing a phase or capacity value does not establish observation.
7. Transformation evidence must identify the affected thing, named property, before and after states, resulting difference, and the join action responsible; an action record or new identity alone is insufficient.
8. Time evidence must establish occurrence order for at least two evidenced transformations independently of record sorting, serialization, scale labels, or assigned sequence numbers; simultaneous or unordered changes do not qualify.

## Usage guidance

```python
from pathlib import Path
import metapat

application = metapat.epac_join_terms_application_module()
metapat.validate_application_against_catalog(application, metapat.canonical_semantic_catalog())
metapat.assert_application_sources_match(Path("."), application)
print(application.application_digest)
```

Consumers must pin this exact application digest and revalidate each binding.
The application has twelve catalog bindings and omits Vector: preserve static
bearing as an EPAC readout. A join action can remain an authored relation while
its resulting property change is unestablished. A stored list can preserve a
sequence only after occurrence evidence establishes that sequence. Missing
result or occurrence evidence leaves those roles `hmmm`; the application
constructor checks declarations and provenance, not downstream execution.

## hmmm

Whether the typed multi-origin representation supports a useful native private operation that its public projection cannot efficiently reproduce remains unestablished.

No chemical or physical interpretation of EPAC phase, bearing, capacity, or S5 occupancy is licensed by this application.

Whether any later UCNS correspondence is useful must be licensed and tested separately without rewriting UCNS law.
