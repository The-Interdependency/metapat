# METAPAT semantic module catalog v4

## Purpose

The catalog makes current METAPAT doctrine addressable without changing canon text.

It contains exactly:

```text
1 root module
12 axiom modules
7 postulate modules
8 theorem modules
12 theory modules
40 modules total
43 exact derived-from relations
```

Each entry carries a strict `MetapatModuleEnvelope`, doctrine class, claim status, contiguous ordinal, and deterministic module digest. The complete catalog carries the exact METAPAT canon identity and a deterministic catalog digest.

## Current canon relationship

Catalog v4 is bound to `metapat-canon-v4`.

The root begins:

```text
Thing
Boundary
State
Simplex
Tensor
```

The numbered extension adds:

```text
Relate
Emerge
Vector
Scalar
Transformation
Time
Domain Qualification
```

Tensor is constructed from related simplexes. Scalar is a state metric. Vector alters state and is inferred by scalar measurement. Domain-specific terms, including energy, require independent domain license.

## Identity layers

These identities remain separate:

```text
canon digest
catalog digest
module-envelope provenance digest
catalog-module digest
semantic-relation digest
UCNS geometry identity
Phi authorization digest
EDCM policy and epoch identity
```

A changed statement, source reference, claim status, constraint, unresolved `hmmm`, relation, or canon identity changes the appropriate digest. Identity evidence is not empirical validation or formal proof.

## Claim status

The catalog uses:

```text
ROOT-STIPULATION
DEFINITION
WORKING-POSTULATE
INTERNAL-DERIVATION
CROSS-DOMAIN-HYPOTHESIS
EMPIRICAL-FRONTIER
```

Current doctrine uses root stipulations/definitions for axioms, `WORKING-POSTULATE` for postulates, and `INTERNAL-DERIVATION` for current theorems and theories. Domain applications carry their own bounded claim status separately.

Using a module does not transfer its status into an application, measurement, UCNS object, or downstream theorem.

## Relations

The bounded relation vocabulary is:

```text
defines
derived-from
constrains
organizes
applies
constitutive-simultaneous
```

Catalog v4 materializes only exact `Derived from:` declarations present in `THEORIES.md`. It does not infer ancestry from similar wording, analogy, ordering, geometry, carrier size, or repeated terms.

`constitutive-simultaneous` is recognized by the shared vocabulary but is prohibited inside an ordinary catalog unless separately backed by explicit canon-bound `UCNSForkAuthorization`. Theory ancestry is not payload containment.

## Source integrity

Every module statement has a source reference of the form:

```text
FILE.md#heading-slug::statement-N
```

Every relation records its exact `Derived from:` statement and section reference. `assert_catalog_sources_match(Path("."))` fails if a source file, heading, exact statement, or declared relation drifts.

The catalog does not replace canon-bearing Markdown. It makes those statements addressable and verifies that the generated representation still resolves to them.

## Package surface

```python
from pathlib import Path
import metapat

catalog = metapat.canonical_semantic_catalog()
metapat.assert_catalog_complete(catalog)
metapat.assert_catalog_sources_match(Path("."), catalog)

module = metapat.semantic_module_by_id("metapat.axiom.5.tensor", catalog)
print(module.claim_status)
print(module.envelope.source_statements)
print(catalog.catalog_digest)
```

The installed package includes:

```text
metapat/fixtures/semantic-module-catalog-v4.json
```

It must remain byte-identical to `canonical_semantic_catalog().to_json()` plus one trailing newline.

## Regeneration

```bash
python tools/generate_catalog.py
python tools/generate_catalog.py --check
python tools/generate_msdmd.py --check
python tools/check_contract_graph.py
python -m pytest -q tests/test_catalog.py tests/test_relations.py
```

A canon/catalog rotation must update the packaged fixtures, generated evidence, application bindings, documentation, and consumer migration consequences together.

## Boundaries

The catalog establishes stable semantic addresses, exact doctrine text/provenance, bounded claim status, declared ancestry, deterministic identity, and strict serialization.

It does not establish empirical truth, formal proof, EDCM metric values, UCNS theorem-status transfer, application validity, or constitutive payload topology.

## hmmm

Completeness is never presumed. A later domain may require a new primitive, split a present one, refine one, or falsify part of the current construction.
