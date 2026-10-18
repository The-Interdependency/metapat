# METAPAT

**Meta Energy Theory — Axioms, Postulates, Theorems, and Theories.**

METAPAT is the canonical semantic authority for Meta Energy Theory. It compares structures and actions independently exposed across domains without allowing any one domain to own the root or transfer its vocabulary by resemblance alone.

Different domains may expose common structures and actions. Domain-specific names, mechanisms, evidence standards, and conservation laws remain domain-owned unless the target domain independently licenses them.

## Research abstract

Description dated 2026-10-14; published 2026-10-18. This is a research description, not a new verification, release, or promotion of claim status.

### METAPAT: Recursive Structure and Cross-Domain Reconstruction

**METAPAT—Meta Energy Theory: Axioms, Postulates, Theorems, and Theories—is an experimental semantic framework for identifying structures and actions independently recoverable across different domains.** It organizes root stipulations, definitions, revisable postulates, internal derivations, and application hypotheses into distinct evidentiary layers. Its central question is what survives comparison across domains without importing one domain’s vocabulary, mechanisms, or authority into another.

The framework begins with **thing, boundary, and state**. A simplex is a thing with boundary and state; related simplexes produce a tensor. That tensor may participate as a whole and, with boundary and state, become a simplex within a further construction. This recursive organization distinguishes a participant’s internal construction from its participation at another scale. State denotes a measurable property rather than its measurement; scalar denotes a state metric; vector denotes state-altering action inferred through scalar measurement; transformation denotes the resulting change; and time denotes sequential transformation. These are framework-specific definitions, not automatic inheritances from mathematical or physical terminology.

Its comparative method examines independently reconstructed candidates, removes domain-specific implementation, and tests the relations that remain. Recurrence supports a candidate shared structure without establishing identical meaning, mechanism, or universal applicability. An accounting adversary provides a consequential example: it falsified the universal application of the name *energy* to the abstract state-change composite while leaving several deeper correspondences unresolved. The current formulation consequently requires each domain to justify its own use of that term. New domains may add, split, refine, or falsify candidate structures rather than merely supply confirming examples.

The software implementation provides version-bound semantic catalogs, provenance-preserving application records, and a provisional recurrence classifier distinguishing structural equivalence, homology, analogy, divergence, and unresolved evidence. Decisions retain reconstruction origins, paths, declared invariants, replay status, and evidence identities. These mechanisms make semantic commitments and evidentiary boundaries inspectable; the classifier does not itself verify the mathematical proofs referenced by its inputs.

METAPAT’s proposed contribution is a **revisable account of recursive organization coupled to a disciplined method for cross-domain comparison**. In application, it identifies consequential distinctions and questions; UCNS supplies geometric representation, while EDCM operationalizes measurement. This division permits conceptual, mathematical, and empirical development to inform one another without substituting one kind of evidence for another.

**hmmm:** The adequacy of the primitive set, the breadth of independently demonstrated recurrence, and the framework’s explanatory value across real domains remain open to testing. Internal consistency and executable contracts establish narrower results than universal validity.

**Usage guidance:** Read this abstract for the research question and intended contribution. Use the scope, evidence, commands, and limitations in the rest of this README before relying on the work; retain the unresolved conditions above when quoting the description.

Public repository context: [Domain restraint](https://github.com/The-Interdependency/metapat/blob/8abffcd7766069fc835872974de31b086c6af337/DOMAIN_RESTRAINT.md) · [Provisional structural recurrence](https://github.com/The-Interdependency/metapat/blob/8abffcd7766069fc835872974de31b086c6af337/docs/structural-recurrence.md).

## Root spine

```text
Thing is that which is.
Boundary is the thing between things.
State is a metricable property of a thing.
A simplex is a thing with boundary and state.
A tensor is structure produced when simplexes relate.
```

The current action, measurement, result, and domain-qualification extension is:

```text
Relate is this to that.
Tensors emerge from simplexes.
Vector alters state.
Vector is inferred by scalar measurement.
Scalar is a state metric.
Transformation is resulting state change.
Time is sequential transformation.
Structural recurrence does not transfer a domain term.
```

The final line is a semantic transfer constraint, not a measurement or transformation rule. Energy is domain-qualified: METAPAT does not call every state transformation energy merely because energetic systems can share the same abstract structure.

## Recursion

```text
Thing + Thing -> Boundary
Thing + Boundary + State -> Simplex
Simplexes Relate -> Tensor Emerges
Tensor -> Thing
Thing + Boundary + State -> Simplex
Repeat
```

A simplex may be constructed below the level at which it participates as a whole. Construction history does not prevent whole participation.

## Cross-domain reconstruction

METAPAT compares independently recovered structures and actions across domains.

The domain implementation does not transfer automatically. A capacitor remains electrical; a flywheel remains mechanical; language remains linguistic. What may transfer is the structure or action that survives removal of the domain-specific implementation.

A new domain may:

- reveal a new primitive;
- split a presently conflated primitive;
- refine an existing definition;
- or falsify part of the current architecture.

Completeness is never presumed.

## Architecture

Authority flow:

```text
METAPAT canon
    |
    +-- constrains terms, interpretation, allowed derivations, and claim status
    +-- catalog makes doctrine addressable
    +-- application modules bind domain uses to exact catalog identities and evidence limits
    v
UCNS adapters and EDCM consumers
```

Runtime data flow remains separate:

```text
source evidence -> EDCM parsing -> actual UCNS representation -> EDCM readouts
                                     ^
                                     |
                          METAPAT-derived semantic constraints
```

UCNS owns geometry and its theorem status. EDCM owns measurement. Neither implementation owns or proves the METAPAT root.

## Install, test, and build

Python 3.11 or newer is required.

```bash
python -m pip install -e .[dev]
python -m unittest discover -s tests
python -m pytest -q
python tools/check_contract_graph.py
python tools/generate_catalog.py --check
python tools/generate_application_fixtures.py --check
python -m pytest -q tests/test_epac_join_terms.py
python tools/generate_msdmd.py --check
python -m build
python -m twine check dist/*
```

The base package has no third-party runtime dependency. Install the actual UCNS adapter dependency explicitly when needed:

```bash
python -m pip install "git+https://github.com/The-Interdependency/ucns.git@19f1afddb993f7d933ac8727627e7d5e1c3b88fc"
python -m pip install -e .[dev]
```

## Byte-complete canon identity

`metapat.canon_digest()` binds the exact importable canon surface and the exact Git blob identities of every canon-bearing Markdown file.

The current canon epoch is `metapat-canon-v4`; identity schema `4.0.0` covers the exact v4 public identity shape and complete canon-file set:

- `CHAPTER_ZERO.md`
- `AXIOMS.md`
- `POSTULATES.md`
- `THEOREMS.md`
- `THEORIES.md`
- `GLOSSARY.md`
- `DOMAIN_RESTRAINT.md`

```python
from pathlib import Path
import metapat

print(metapat.CANON_VERSION)
print(metapat.canon_digest())
metapat.assert_canon_files_match(Path("."))
```

A digest is identity evidence, not empirical validation or formal proof.

Consumer migration is fail-closed. A consumer bound to any earlier canon, identity schema, or catalog—including v3 schema `3.0.0`—must reject v4 until it explicitly binds identity schema `4.0.0` and the v4 identities it uses. Unknown top-level identity fields are not an implicit migration path.

## Immutable semantic module envelope

`MetapatModuleEnvelope` carries semantic authority and provenance only. It preserves:

- schema and module identity;
- canon version and digest;
- exact source references and statements;
- constraints and permitted interpretations;
- unresolved `hmmm`;
- deterministic provenance identity.

The root spine is represented as `module_kind="canon-module"`. Current module vocabulary includes thing, boundary, state, simplex, tensor, relate, relation, emergence, scalar, vector, transformation, time, domain-qualification, registration, observer, question, postulate, theorem, and theory. `energy` is not a universal module kind in v4; a domain may use the term only under its own applicable evidence and licensing.

The v4 envelope wire schema is `2.0.0`. It is deliberately incompatible with the prior `1.2.0` epoch, so old and current parsers fail closed across the boundary until a consumer explicitly rebinds the v4 canon and provenance identities.

The packaged `fixtures/root-spine-envelope-v4.json` must remain byte-identical to the live constructor.

## Addressable semantic catalog

`metapat.canonical_semantic_catalog()` materializes the current doctrine as stable provenance-bearing modules:

```text
1 root module
12 axiom modules
7 postulate modules
8 theorem modules
12 theory modules
40 modules total
43 declared derived-from relations
```

The catalog does not infer ancestry from analogy, repeated terms, ordering, geometry, or similarity.

```python
from pathlib import Path
import metapat

catalog = metapat.canonical_semantic_catalog()
metapat.assert_catalog_complete(catalog)
metapat.assert_catalog_sources_match(Path("."), catalog)

tensor = metapat.semantic_module_by_id("metapat.axiom.5.tensor", catalog)
print(tensor.claim_status)
print(tensor.envelope.source_statements)
print(catalog.catalog_digest)
```

The current catalog epoch is `metapat-semantic-catalog-v4`. The packaged `fixtures/semantic-module-catalog-v4.json` must remain byte-identical to the live constructor plus one trailing newline.

## Catalog-bound applications

Application modules bind domain uses to exact catalog modules while preserving domain evidence boundaries. They do not promote application claims into root truth.

The v4 application-module wire schema is `2.0.0`; the prior `1.0.0` parser epoch must reject it until a consumer explicitly migrates to the v4 application and catalog identities.

The quantum-magnetism vertical slice is currently:

```text
application: metapat.application.quantum_magnetism
version: quantum-magnetism-application-v4
claim status: CROSS-DOMAIN-HYPOTHESIS
catalog bindings: 12
root impact: none
```

The application remains answerable to physics. Passing METAPAT contract checks does not validate quantum mechanics, a material model, or METAPAT itself.

## Actual UCNS adapter

METAPAT defines no local UCNS algebra. `metapat.ucns` lazily imports the actual `ucns` package only when adaptation is requested.

The default semantic mapping is `external-provenance`: METAPAT semantics remain in the adaptation record while UCNS owns its representation and geometry.

`UCNSAdaptationRecord` wire version `2.0.0` validates its embedded envelope schema `2.0.0` and exact v4 canon identity. The prior adaptation wire `1.0.0` and current wire reject one another; an outer record cannot be used to bypass explicit v4 migration.

One explicit semantic exception remains available through canon-bound `UCNSForkAuthorization` for `constitutive-simultaneous` children. Authorization supplies semantic permission only; downstream UCNS topology still has to be verified independently.

## Contract and evidence graph

The repository follows the pinned `skill-lib` split:

```text
CONTRACTS are source-owned obligations.
CHECKS are test-owned accountable witnesses.
audit reconciles the graph without importing code.
```

`tools/check_contract_graph.py` rejects orphan contracts, phantom evidence, unresolved self-calls, and other graph drift. Generated fixtures and `metapat_msdmd.ts` are regenerated from source; they are not hand-maintained.

## Current authority map

- `CHAPTER_ZERO.md` — canonical chapter and textbook Chapter Zero source.
- `AXIOMS.md` — numbered root structures/actions/results.
- `POSTULATES.md` — revisable working commitments.
- `THEOREMS.md` — internal derivations.
- `THEORIES.md` — organized derivation families.
- `DOMAIN_RESTRAINT.md` — prevents domain capture.
- `GLOSSARY.md` — current term definitions.
- `docs/claims-ledger.md` — public claim classification.
- `docs/semantic-module-catalog.md` — catalog contract and limits.
- `docs/structural-recurrence.md` — provisional recurrence API, exact producer replay, and no-transfer requirements.
- `docs/application-modules.md` — application schema and evidence firewall.
- `UCNS_IMPLEMENTATION.md` — actual adapter scope and limits.
- `docs/ucns-phi-policy.md` — explicit constitutive-fork authority and limits.
- `COMPLIANCE.md` — current evidence surfaces and commands.

## Repository rule

```text
No implementation owns the root.
```

## hmmm

METAPAT is intentionally open to falsification. A later domain may reveal a new primitive, split one, refine one, or falsify part of the current construction. Completeness is never presumed.
