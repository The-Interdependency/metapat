# METAPAT compliance surface

Date: 2026-07-21

## Authority

- Meta Energy Theory doctrine: `The-Interdependency/metapat`.
- Reusable build and evidence doctrine: `The-Interdependency/skill-lib`.
- Repo-local skill source commit: `The-Interdependency/skill-lib@05ee7aa`, as declared by `.agents/skills/README.md`.
- `meta-module-build/SKILL.md` is byte-identical to the canonical file at both the declared source commit and later lineage `6f36340`; its Git blob identity is `e9ca23f03a124a44d39b4ea79b60833677816711`.

If a repo-local skill conflicts with upstream `skill-lib`, upstream governs the skill contract. METAPAT governs only Meta Energy Theory doctrine.

## Standing gates

| Surface | Command | Required result |
|---|---|---|
| Source obligations / test evidence | `python tools/check_contract_graph.py` | graph closes with no orphan contract, phantom target, unresolved call, or undeclared top-level test |
| Generated metadata | `python tools/generate_msdmd.py --check` | committed `metapat_msdmd.ts` is byte-current and includes `src/metapat/flow_plan.py` declarations |
| Complete canon bytes | `python -c "from pathlib import Path; import metapat; metapat.assert_canon_files_match(Path('.'))"` | every declared canon file matches its exact Git blob identity |
| Canon contracts | `python -m unittest discover -s tests` | pass |
| Full base suite | `python -m pytest -q` | pass; actual-UCNS tests may skip only when the optional dependency is absent |
| Explicit Phi policy | `python -m pytest -q tests/test_ucns_phi.py` | default external provenance, explicit-only constitutive authorization, exact order/canon binding, prohibited relation rejection, strict roundtrip, and no status transfer pass |
| Actual UCNS integration | `python -m pip install -e .[dev,ucns]` then targeted pytest | actual object, complete provenance, strict record roundtrip, and no theorem transfer pass |
| Distribution | `python -m build && python -m twine check dist/*` | source and wheel artifacts valid |
| Clean wheel | install `dist/*.whl` into a new virtual environment | version, typing marker, packaged fixture, envelope identity, and dependency-free base import pass |

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

The corrected `CHAPTER_ZERO.md` Git blob identity is `ba5fcd47086b292ee7e0ddfd7951ca0c4385625f`. The resulting aggregate canon identity is `116fffd7a02487537e43581152fca74099db43c1a0af8df2e737fa9b8afbd00e`.

The aggregate identity uses SHA-256. Git SHA-1 appears only as the repository's exact blob identity for each file and is not presented as a security proof or empirical validation.

## Envelope, UCNS, and Phi status

`MetapatModuleEnvelope` schema `1.2.0` rejects unknown, missing, or incorrectly typed fields. The root spine is represented as a neutral `canon-module`; canonical terms including distinction, energy-state, scalar, vector, transformation, observer, postulate, theorem, and theory can be named without classifying them as simplexes by constructor convenience.

The actual-UCNS adaptation record retains exact statements, resolvable references, constraints, permitted interpretations, unresolved `hmmm`, canon identity, and envelope provenance identity. It is independently strict and serializable. The adapter keeps unit UCNS payloads and uses `external-provenance` as its default semantic mapping.

`UCNSPhiPolicy` schema `1.0.0` ratifies one explicit semantic exception without changing adapter behavior: a canon-bound `UCNSForkAuthorization` may declare ordered children to be simultaneous constitutive components of one parent. Only `constitutive-simultaneous` is authorized. Temporal succession, adjacency, provenance, alternatives, fiq connectivity, external symmetry action, and arbitrary association remain prohibited as containment meanings.

The authorization record is producer-side semantic authority only. It does not construct UCNS geometry, infer meaning from payloads, validate downstream topology, transfer theorem status, establish METAPAT validity, or validate EDCM measurements.

The canonical root-spine fixture is packaged at:

```text
metapat/fixtures/root-spine-envelope-v1.json
```

The fixture must equal `root_spine_module_envelope().to_json()` byte-for-byte after trailing newline normalization.

## Explicit exclusion

This repair does not modify `The-Interdependency/ucns` or `The-Interdependency/edcm`. The downstream topology-binding record, EDCM semantic consumer, and full shared-stack fixture are separate downstream PRs after this producer authority is reconciled.

No UCNS-A theorem/proof status is transferred to METAPAT, EDCM, edcmbone, or UCNS-G by this change.

## hmmm

The first complete constitutive-fork fixture still requires exact binding among the METAPAT authorization digest, UCNS parent object, payload-bearing path, ordered child module identities, and ordered child UCNS stable hashes. Semantic mappings outside default external provenance and explicitly authorized constitutive-simultaneous forks remain unresolved.
