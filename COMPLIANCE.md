# METAPAT compliance surface

Date: 2026-07-21

## Authority

- Meta Energy Theory doctrine: `The-Interdependency/metapat`.
- Reusable build and evidence doctrine: `The-Interdependency/skill-lib`.
- Repo-local skill pin: `The-Interdependency/skill-lib@6f36340`, used by `tools/generate_msdmd.py` and declared by `.agents/skills/README.md`.
- `meta-module-build/SKILL.md` is byte-identical to the canonical file at the pinned lineage; its Git blob identity is `e9ca23f03a124a44d39b4ea79b60833677816711`.

If a repo-local skill conflicts with upstream `skill-lib`, upstream governs the skill contract. METAPAT governs only Meta Energy Theory doctrine.

## Standing gates

| Surface | Command | Required result |
|---|---|---|
| Source obligations / test evidence | `python tools/check_contract_graph.py` | graph closes with no orphan contract, phantom target, unresolved call, or undeclared top-level test |
| Generated metadata | `python tools/generate_msdmd.py --check` | committed `metapat_msdmd.ts` is byte-current across bounded `src/`, `tests/`, and `tools/` surfaces |
| Complete canon bytes | `python -c "from pathlib import Path; import metapat; metapat.assert_canon_files_match(Path('.'))"` | every declared canon file matches its exact Git blob identity |
| Semantic catalog tests | `python -m pytest -q tests/test_catalog.py tests/test_relations.py` | 39 modules, 52 declared relations, strict identity, bounded status, exact source resolution, and no inferred constitutive meaning pass |
| Catalog fixture | `python tools/generate_catalog.py --check` | packaged `semantic-module-catalog-v1.json` is byte-current with the live constructor |
| Catalog source integrity | `python -c "from pathlib import Path; import metapat; metapat.assert_catalog_complete(); metapat.assert_catalog_sources_match(Path('.'))"` | every module and relation resolves to an exact statement in its declared canon section |
| Application-module tests | `python -m pytest -q tests/test_application.py tests/test_quantum_magnetism.py` | strict catalog bindings, roundtrip, source integrity, scale separation, evidence firewall, and fixture identity pass |
| Application fixtures | `python tools/generate_application_fixtures.py --check` | packaged quantum-magnetism application fixture is byte-current with its constructor |
| Application binding integrity | construct the catalog and application, then run `validate_application_against_catalog()` and `assert_application_sources_match()` | exact catalog version, catalog digest, twelve module identities/digests/statuses, and 45 source statements match |
| Canon contracts | `python -m unittest discover -s tests` | pass |
| Full base suite | `python -m pytest -q` | pass; actual-UCNS tests may skip only when the optional dependency is absent |
| Explicit Phi policy | `python -m pytest -q tests/test_ucns_phi.py` | default external provenance, explicit-only constitutive authorization, exact order/canon binding, prohibited relation rejection, strict roundtrip, and no status transfer pass |
| Actual UCNS integration | `python -m pip install -e .[dev,ucns]` then targeted pytest | actual object, complete provenance, strict record roundtrip, and no theorem transfer pass |
| Distribution | `python -m build && python -m twine check dist/*` | source and wheel artifacts valid |
| Clean wheel | install `dist/*.whl` into a new virtual environment | version, typing marker, all three packaged fixtures, catalog and application identity, and dependency-free base import pass |

GitHub Actions is the standing execution evidence. A local run is supporting evidence only and does not supersede a later failing run of the same command.

## CONTRACTS / CHECKS status

Source modules contain obligations only. Test modules contain executable `CHECKS` entries using `proves:` and `self::function` resolution. Source `call:` fields are forbidden.

The audit performs no imports. It is negative-tested by planting:

- an orphan contract;
- a check claiming an unknown contract;
- an unresolvable call;
- an executable top-level test without a declaration.

The graph is `[test-backed]` only after the ordinary suite passes and the audit closes. Mutation-level verification remains a higher, currently unclaimed rung.

## Canon identity status

The canon text remains `metapat-canon-v1`. Identity schema `2.0.0` binds:

- importable canon constants and definitions;
- exact byte identities for `CHAPTER_ZERO.md`, `AXIOMS.md`, `POSTULATES.md`, `THEOREMS.md`, `THEORIES.md`, `GLOSSARY.md`, and `DOMAIN_RESTRAINT.md`.

The `CHAPTER_ZERO.md` Git blob identity is `ba5fcd47086b292ee7e0ddfd7951ca0c4385625f`. The aggregate canon identity is `116fffd7a02487537e43581152fca74099db43c1a0af8df2e737fa9b8afbd00e`.

## Semantic catalog status

Catalog schema `1.0.0`, version `metapat-semantic-catalog-v1`, materializes one root, twelve axioms, six postulates, eight theorems, twelve theories, and fifty-two exact `derived-from` edges. The catalog digest is:

```text
871d8a9c40ede0e47999e672bdbc18b8b72a70bb74e1f43a29af44e43882d08a
```

Every module and relation carries exact source provenance, bounded status, unresolved constraints, and deterministic identity. `WORKING-POSTULATE` preserves revisability. Theory 10 remains `CROSS-DOMAIN-HYPOTHESIS`. Ordinary catalog ancestry is not formal proof or constitutive payload containment.

## Application-module status

Application schema `1.0.0` binds domain applications to exact catalog identities without changing the catalog or canon. The first application is:

```text
application id: metapat.application.quantum_magnetism
version: quantum-magnetism-application-v1
claim status: CROSS-DOMAIN-HYPOTHESIS
root impact: none
catalog bindings: 12
application digest: 8579a9f88bce4ca2242a36731ce7fec76191ef57a6d2ccd7af9d72de1471b0ae
```

The packaged fixture is:

```text
metapat/fixtures/quantum-magnetism-application-v1.json
```

Each binding fixes catalog module ID, module digest, module claim status, application role, application statement, and binding digest. Theory 10 is deliberately absent. Nuclear, atomic, crystalline, and magnetic-domain scales remain separate. Physics remains the governing evidence domain.

The application record requires all of these fields to remain false:

```text
metapat_validity_claim
domain_validity_claim
measurement_validity_claim
ucns_theorem_status_transfer
ucns_topology_claim
```

Catalog binding therefore establishes application provenance, not physics validation, proof, measurement validity, or UCNS topology.

## Envelope, UCNS, and Phi status

`MetapatModuleEnvelope` schema `1.2.0` rejects unknown, missing, or incorrectly typed fields. The actual-UCNS adapter retains exact semantic provenance while keeping unit payloads and default `external-provenance` mapping.

`UCNSPhiPolicy` schema `1.0.0` permits only explicit `constitutive-simultaneous` authorization. Application bindings, catalog ancestry, temporal succession, adjacency, provenance, alternatives, fiq connectivity, external symmetry action, and arbitrary association remain prohibited as containment meanings.

## Explicit exclusion

This application change does not modify `The-Interdependency/ucns` or `The-Interdependency/edcm`. It performs no Hamiltonian derivation, simulation, measurement, or experimental comparison. The downstream topology-binding record, EDCM semantic consumer, and full shared-stack fixture remain separate changes.

No UCNS-A theorem/proof status is transferred to METAPAT, its catalog, the application, EDCM, edcmbone, or UCNS-G.

## hmmm

The quantum-magnetism mapping remains a cross-domain hypothesis until it defines each physical scale and boundary precisely, maps physical variables explicitly, produces distinguishing predictions, and compares them with experimental or computational evidence. “Field-space” remains unresolved among physical field, configuration space, and general potential-state landscape.
