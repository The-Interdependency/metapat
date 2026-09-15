# METAPAT compliance surface

Date: 2026-09-15

## Authority

- Meta Energy Theory doctrine: `The-Interdependency/metapat`.
- Reusable build/evidence doctrine: `The-Interdependency/skill-lib`.
- Canon source: `CHAPTER_ZERO.md`, `AXIOMS.md`, `POSTULATES.md`, `THEOREMS.md`, `THEORIES.md`, `GLOSSARY.md`, and `DOMAIN_RESTRAINT.md`.

If a repo-local skill conflicts with upstream `skill-lib`, upstream governs the skill contract. METAPAT governs Meta Energy Theory doctrine.

## Standing gates

| Surface | Command | Required result |
|---|---|---|
| Source obligations / test evidence | `python tools/check_contract_graph.py` | graph closes with no orphan contract, phantom target, unresolved call, or undeclared executable test |
| Generated metadata | `python tools/generate_msdmd.py --check` | committed `metapat_msdmd.ts` is byte-current |
| Complete canon bytes | `python -c "from pathlib import Path; import metapat; metapat.assert_canon_files_match(Path('.'))"` | every canon-bearing file matches its declared Git blob identity |
| Semantic catalog tests | `python -m pytest -q tests/test_catalog.py tests/test_relations.py` | 40 modules, 43 declared relations, strict identity, bounded status, exact sources, no inferred constitutive meaning |
| Canon semantic fixtures | `python tools/generate_catalog.py --check` | `root-spine-envelope-v4.json` and `semantic-module-catalog-v4.json` are current |
| Catalog source integrity | `python -c "from pathlib import Path; import metapat; metapat.assert_catalog_complete(); metapat.assert_catalog_sources_match(Path('.'))"` | every module and relation resolves to exact canon text |
| Application tests | `python -m pytest -q tests/test_application.py tests/test_quantum_magnetism.py tests/test_electromagnetic_pipe.py` | catalog bindings, source integrity, evidence firewalls, and fixture identity pass |
| Application fixtures | `python tools/generate_application_fixtures.py --check` | packaged v4 application fixtures are current |
| Canon contracts | `python -m unittest discover -s tests` | pass |
| Full base suite | `python -m pytest -q` | pass; actual-UCNS tests may skip only when optional dependency is absent |
| Explicit Phi policy | `python -m pytest -q tests/test_ucns_phi.py` | explicit-only constitutive authorization and no status transfer pass |
| Actual UCNS integration | CI pinned-producer job | actual UCNS object, exact provenance, strict roundtrip, no theorem/validity transfer |
| Distribution | `python -m build && python -m twine check dist/*` | source and wheel artifacts valid |
| Clean wheel | install `dist/*.whl` in a clean environment | version, typing marker, v4 fixtures, identity, and dependency-free base import pass |

GitHub Actions is the standing execution evidence. A local run is supporting evidence only and does not supersede a later failing run of the same command.

## Canon identity status

The current canon epoch is `metapat-canon-v4`. Identity schema `4.0.0` binds the exact v4 importable shape and exact bytes of every canon-bearing Markdown file. Earlier consumers, including v3 schema `3.0.0`, reject this identity until explicitly migrated.

The root is:

```text
Thing is that which is.
Boundary is the thing between things.
State is a metricable property of a thing.
A simplex is a thing with boundary and state.
A tensor is structure produced when simplexes relate.
```

The extension is:

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

Tensor is not primitive before simplex in v4. Scalar is not state. Energy-state is not a root primitive. Energy is domain-qualified rather than a universal name for state transformation.

## Semantic catalog status

Catalog schema `1.0.0`, version `metapat-semantic-catalog-v4`, materializes:

```text
1 root
12 axioms
7 postulates
8 theorems
12 theories
40 modules
43 exact derived-from relations
```

Every module and relation carries exact source provenance, bounded status, unresolved constraints where present, and deterministic identity. Catalog ancestry is not formal proof or constitutive payload containment.

## Application status

Application schema `1.0.0` binds domain applications to exact v4 catalog identities without changing canon.

Quantum magnetism remains `CROSS-DOMAIN-HYPOTHESIS`; the electromagnetic-pipe application remains `EMPIRICAL-FRONTIER`. Their evidence remains answerable to their physical domains.

Application records keep these validity/transfer fields false unless independently established:

```text
metapat_validity_claim
domain_validity_claim
measurement_validity_claim
ucns_theorem_status_transfer
ucns_topology_claim
```

Catalog binding establishes provenance, not domain validation, proof, measurement validity, or UCNS topology.

## Envelope, UCNS, and Phi status

`MetapatModuleEnvelope` schema `1.2.0` rejects unknown, missing, or incorrectly typed fields. The actual-UCNS adapter retains exact semantic provenance while keeping representation authority in UCNS and default `external-provenance` mapping.

`UCNSPhiPolicy` permits only explicit `constitutive-simultaneous` authorization. Application bindings, catalog ancestry, temporal succession, adjacency, provenance, alternatives, external symmetry action, and arbitrary association remain insufficient to establish containment.

## Cross-domain falsification

Different domains may independently expose common structures and actions. A candidate survives only while independent domain comparisons fail to add, split, refine, or falsify it. Similarity alone is insufficient; domain-specific implementation and vocabulary must be removed before structural transfer is claimed, and domain terms require independent target-domain license.

## Explicit exclusions

METAPAT does not replace UCNS geometry, EDCM measurement, physics evidence, formal proof, or application-domain validation.

No UCNS theorem/proof status transfers to METAPAT, its catalog, an application, EDCM, or another consumer merely through binding or adaptation.

## hmmm

Completeness is never presumed. Physical validation of current applications and downstream consumer-epoch migration remain outside the canon rotation and require their owning evidence/repositories.
