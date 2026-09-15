# METAPAT claims ledger

Date: 2026-09-13

This ledger classifies public doctrine and executable assertions without changing canon text. Contract checks protect encoded conditions; they are not independent empirical evidence, formal proof, or validation of Meta Energy Theory as external truth.

## Status vocabulary

```text
ROOT-STIPULATION
DEFINITION
WORKING-POSTULATE
INTERNAL-DERIVATION
IMPLEMENTED-CONTRACT
CROSS-DOMAIN-HYPOTHESIS
EMPIRICAL-FRONTIER
RETRACTED_OR_SUPERSEDED
```

## Current canon

| Statement/surface | Status | Boundary |
|---|---|---|
| Thing is that which is. | ROOT-STIPULATION | Root structure; no domain ownership implied. |
| Boundary is the thing between things. | ROOT-STIPULATION | Boundary requires multiplicity; observation does not create it. |
| State is a metricable property of a thing. | ROOT-STIPULATION | State is not measurement. |
| A simplex is a thing with boundary and state. | ROOT-STIPULATION | A constructed thing may participate as a whole. |
| A tensor is structure produced when simplexes relate. | DEFINITION | Tensor is constructed, not primitive before simplex. |
| Relate is this to that. | DEFINITION | Geometry is one possible relation, not the definition. |
| Tensors emerge from simplexes. | DEFINITION | Emergence is tied to related-simplex structure. |
| Vector alters state; vector is inferred by scalar measurement. | DEFINITION | Vector is distinct from state metric. |
| Scalar is a state metric. | DEFINITION | Scalar measures state; it is not state. |
| Transformation is resulting state change. | DEFINITION | Result of vector alteration. |
| Time is sequential transformation. | DEFINITION | Registration may preserve time but does not produce it. |
| Energy is vectors altering state through transformation across time. | DEFINITION / derived root term | Energy is composite at this level rather than primitive. |
| Seven postulates | WORKING-POSTULATE | Revisable commitments; may not silently rewrite axioms. |
| Eight theorems | INTERNAL-DERIVATION | Internal reductions, not external proof. |
| Twelve theories | INTERNAL-DERIVATION | Organized derivation families; remain falsifiable. |

## Cross-domain reconstruction

| Claim | Status | Boundary |
|---|---|---|
| Every domain exposes some properties of Platonic energy. | WORKING-POSTULATE | Does not imply every domain exposes the same properties. |
| No domain exposes all properties of Platonic energy. | WORKING-POSTULATE | Keeps the search open; completeness is never presumed. |
| A shared candidate may be compared after domain implementation is removed. | WORKING-POSTULATE | Similarity alone is insufficient. |
| A later domain may add, split, refine, or falsify a candidate. | WORKING-POSTULATE | No current primitive/operator set is certified complete. |
| An electrical/mechanical/linguistic implementation is identical to a METAPAT primitive. | RETRACTED_OR_SUPERSEDED | Domain implementations remain domain-specific. |

## Internal derivations and contract checks

| Surface | Status | What it checks | What it does not establish |
|---|---|---|---|
| `boundary_requires_multiplicity` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | Encoded boundary eligibility requires at least two things. | External metaphysical proof. |
| `simplex_closes` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | Thing, boundary, and state are all present. | Empirical objecthood. |
| `tensor_emerges` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | Multiple simplexes plus relation satisfy the encoded tensor condition. | Universal emergence law. |
| `recursive_closure` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | A tensor with boundary and state satisfies simplex closure. | That any specific real system closes this way. |
| `vector_inferred_by_scalar` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | Changed scalar measurements permit the encoded inference condition. | Complete physical vector reconstruction. |
| `transformation_produces_time` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | Multiple ordered transformations satisfy the encoded sequence condition. | External theory of physical time. |
| `energy_is_derived` | INTERNAL-DERIVATION + IMPLEMENTED-CONTRACT | Vector, state, transformation, and time are present. | Empirical conservation law or physical-energy theory. |

## Implemented architecture contracts

| Surface | Status | Contract |
|---|---|---|
| `metapat.canon.canon_digest()` | IMPLEMENTED-CONTRACT | Deterministically identifies the exact importable v3 canon and complete canon-file manifest. |
| `CANON_FILE_BLOBS` / `assert_canon_files_match()` | IMPLEMENTED-CONTRACT | Bind all canon Markdown byte-for-byte and fail closed on drift. |
| `MetapatModuleEnvelope` | IMPLEMENTED-CONTRACT | Strict semantic/provenance envelope preserving exact source, constraints, `hmmm`, canon identity, and digest. |
| `MetapatModuleRelation` | IMPLEMENTED-CONTRACT | Strict relation record with exact endpoints/source and no theorem/measurement transfer. |
| `MetapatSemanticCatalog` | IMPLEMENTED-CONTRACT | Catalog v3 contains exactly 40 ordered modules and 43 exact declared derivation edges. |
| `assert_catalog_complete()` | IMPLEMENTED-CONTRACT | Enforces 1 root, 12 axioms, 7 postulates, 8 theorems, 12 theories. |
| `assert_catalog_sources_match()` | IMPLEMENTED-CONTRACT | Every module/relation resolves to exact canon text. |
| `tools/generate_catalog.py` | IMPLEMENTED-CONTRACT | Generates/checks `root-spine-envelope-v3.json` and `semantic-module-catalog-v3.json`. |
| `MetapatApplicationModule` / `ApplicationCatalogBinding` | IMPLEMENTED-CONTRACT | Bind domain applications to exact catalog identities and evidence boundaries without status laundering. |
| `validate_application_against_catalog()` | IMPLEMENTED-CONTRACT | Fails on catalog/module identity, digest, or status drift. |
| `assert_application_sources_match()` | IMPLEMENTED-CONTRACT | Fails when application source headings/statements drift. |
| `tools/generate_application_fixtures.py` | IMPLEMENTED-CONTRACT | Generates/checks current packaged v3 application fixtures. |
| `metapat.ucns.adapt_envelope_to_ucns` | IMPLEMENTED-CONTRACT | Uses actual UCNS, preserves external semantic provenance, transfers no theorem status. |
| `UCNSForkAuthorization` | IMPLEMENTED-CONTRACT | Records explicit `constitutive-simultaneous` semantic authorization; does not prove encoded topology. |
| `tools/check_contract_graph.py` | IMPLEMENTED-CONTRACT | Reconciles source CONTRACTS with test CHECKS and reports graph defects. |
| `tools/generate_msdmd.py` | IMPLEMENTED-CONTRACT | Generates the repository metadata graph from bounded source/test/tool surfaces. |

## Application and empirical status

| Claim family | Status | Boundary |
|---|---|---|
| Applying METAPAT to a scientific/technical/social/cognitive domain | CROSS-DOMAIN-HYPOTHESIS unless separately demonstrated | Addressability does not make an application root/theorem/measurement. |
| Quantum-magnetism catalog binding/source fixture | IMPLEMENTED-CONTRACT | Establishes provenance/evidence limits only. |
| Quantum-magnetism physical adequacy | CROSS-DOMAIN-HYPOTHESIS / EMPIRICAL-FRONTIER | Remains answerable to physics. |
| Electromagnetic-pipe binding/design identity | IMPLEMENTED-CONTRACT | Establishes exact proposal identity, not performance. |
| Electromagnetic-pipe performance | EMPIRICAL-FRONTIER | Requires simulation, characterization, thermal/insulation/fault tests, and prototypes. |
| Explicit constitutive semantic authorization | IMPLEMENTED-CONTRACT | Does not establish downstream UCNS topology. |
| EDCM values corresponding to METAPAT labels | EMPIRICAL-FRONTIER | Semantic labels constrain interpretation; they are not measured values. |

## Superseded v2 doctrine

| Former surface | Status | Replacement |
|---|---|---|
| “Legible difference is distinction.” as first root axiom | RETRACTED_OR_SUPERSEDED | Thing / Boundary / State root construction. |
| “Distinction defines boundaries.” | RETRACTED_OR_SUPERSEDED | Boundary is prior to registered distinction in v3. |
| “Boundary is simplex of distinction.” | RETRACTED_OR_SUPERSEDED | Boundary is the thing between things. |
| “Tensor is primitive.” | RETRACTED_OR_SUPERSEDED | Tensor is structure produced when simplexes relate. |
| “Energy-state held is scalar.” | RETRACTED_OR_SUPERSEDED | State is metricable; scalar is a state metric. |
| “Energy-state motioned is vector.” | RETRACTED_OR_SUPERSEDED | Vector alters state and is inferred by scalar measurement. |
| “Time is sequential tensor alteration.” | RETRACTED_OR_SUPERSEDED | Time is sequential transformation. |
| Energy as primitive substrate vocabulary | RETRACTED_OR_SUPERSEDED | Energy is derived from vector/state/transformation/time. |
| Catalog v2 / 52 declared edges | RETRACTED_OR_SUPERSEDED | Catalog v3 / 43 declared edges. |
| v2 root/catalog/application fixtures | RETRACTED_OR_SUPERSEDED | v3 fixtures; consumers fail closed until migrated. |
| Single flow `UCNS -> METAPAT -> EDCM` | RETRACTED_OR_SUPERSEDED | Separate semantic authority, representation/geometry, measurement, and proof-status flows. |
| Local METAPAT UCNS algebra | RETRACTED_OR_SUPERSEDED | Optional adapter to actual UCNS. |
| Application binding as domain validation | RETRACTED_OR_SUPERSEDED | Binding establishes provenance and evidence boundaries only. |

## Usage

When adding or changing a public claim:

1. cite the exact source or executable surface;
2. assign one status from this ledger;
3. state what evidence would change that status;
4. update affected catalog/application declarations, fixtures, code metadata, docs, tests, generated msdmd, and canon manifest;
5. preserve unresolved constraints as `hmmm`.

## hmmm

The current v3 construction is deliberately incomplete in the epistemic sense: no finite domain set can certify that no later domain will add, split, refine, or falsify a candidate. That open boundary is part of the method, not a claim of completed universality.
