# METAPAT Roadmap

## Current state

METAPAT is the canonical semantic authority for Meta Energy Theory. It exposes:

- exact root canon constants and byte-complete deterministic canon identity;
- immutable, strictly validated `MetapatModuleEnvelope` records;
- deterministic canon contract checks with explicit non-validation boundaries;
- an optional adapter that constructs actual `ucns.UCNSObject` geometry while retaining the complete semantic envelope in a serializable record;
- an explicit canon-bound Phi policy that may authorize ordered simultaneous constitutive children without inferring semantics from geometry;
- a source-CONTRACTS/test-CHECKS audit and generated msdmd collection;
- package, wheel, base, canon-integrity, Phi-policy, and actual-UCNS integration gates.

## Architecture

Authority:

```text
METAPAT canon
    |
    +-- constrains terms, interpretation, allowed derivations, and claim status
    v
UCNS adapters and EDCM consumers
```

Runtime:

```text
source evidence -> EDCM parsing -> actual UCNS representation -> EDCM readouts
                                     ^
                                     |
                          METAPAT-derived semantic constraints
```

Proof status does not transfer from UCNS into METAPAT ontology or EDCM measurement validity.

## Phase 0 — Canon stability

Status: implemented and continuously required.

- Preserve Chapter Zero and exact root strings.
- Keep root/tool/domain separation.
- Bind consumers to `CANON_VERSION`, `CANON_IDENTITY_SCHEMA_VERSION`, `canon_digest()`, and the complete canon-file manifest.
- Fail closed when any canon-bearing Markdown file changes without an explicit manifest update.
- Check repeated root-spine text against `AXIOMS.md` and `CHAPTER_ZERO.md` rather than protecting inconsistent copies independently.
- Keep unresolved details marked `hmmm`.
- Classify public claims in `docs/claims-ledger.md`.

## Phase 1 — Semantic module envelope

Status: implemented at schema `1.2.0`.

- `MetapatModuleEnvelope` is immutable and versioned.
- Exact source references and statements survive serialization.
- Root-spine references resolve to stable `AXIOMS.md` heading and statement identifiers.
- The root spine is a neutral `canon-module`; it is not classified as a simplex by constructor convenience.
- The module-kind vocabulary can name distinction, simplex, boundary-simplex, tensor, energy-state, scalar, vector, relation, gradient, transformation, registration, observer, time, question, postulate, theorem, and theory.
- Constraints, permitted interpretations, unresolved constraints, canon identity, and provenance digest remain distinct.
- Unknown, missing, or incorrectly typed schema fields fail closed.
- Canon or constraint rotation changes provenance identity.
- No measured EDCM values are present.
- The canonical root-spine fixture is packaged and checked against the live constructor.

## Phase 2 — Actual UCNS geometry adapter and Phi authority

Status: adapter implemented for ordered statement-count geometry; semantic authorization implemented at policy `1.0.0`.

- Base METAPAT remains importable without UCNS.
- Adapter calls without UCNS raise a clear dependency error.
- Adaptation constructs actual `ucns.UCNSObject` instances.
- Stable hash and UCNS serialization version are recorded.
- Exact statements, references, constraints, permitted interpretations, and unresolved `hmmm` survive in a strict serializable record.
- The adapter default remains `external-provenance`; METAPAT statements remain outside UCNS payloads and UCNS payloads remain unit.
- METAPAT contains no local normalization, product, factorization, star/disk-flip, or theorem-status algebra.
- `UCNSPhiPolicy` requires explicit authorization and permits only the `constitutive-simultaneous` relation.
- `UCNSForkAuthorization` binds parent identity, ordered child identities, source references, canon identity, policy version, unresolved constraints, and a deterministic authorization digest.
- Temporal succession, adjacency, provenance, alternatives, fiq connectivity, external symmetry action, and arbitrary association remain prohibited as payload-containment meanings.
- Phi policy and authorization records transfer no theorem status and make no METAPAT validity claim.

Remaining:

- hmmm: define the downstream topology-binding record for exact UCNS parent identity, payload path, ordered child hashes, authorization digest, and encoding-policy version.
- hmmm: add a fail-closed linter that rejects missing declarations, order drift, object-hash drift, canon drift, and external-edge-as-containment substitution.
- hmmm: consume an official versioned UCNS bridge record if UCNS standardizes one.
- hmmm: ratify any semantic mapping beyond default external provenance and explicitly authorized constitutive-simultaneous forks.

## Phase 3 — Evidence and metadata integrity

Status: repaired as a standing gate.

- Source modules own `CONTRACTS`; tests own `CHECKS`.
- `tools/check_contract_graph.py` audits without imports and is negative-tested.
- `metapat_msdmd.ts` is generated from bounded product surfaces through the pinned collector.
- The generated graph includes `src/metapat/flow_plan.py`; omission is a failing stale-collection condition.
- `COMPLIANCE.md` names the current pin, commands, evidence boundaries, and downstream exclusion.
- CI enforces graph closure, generated metadata freshness, complete canon-file integrity, explicit Phi-policy tests, packaged fixture identity, ordinary tests, builds, and wheel smoke checks.

## Phase 4 — EDCM semantic consumer

Status: separate downstream implementation required.

EDCM must:

- accept the exact versioned envelope or packaged fixture;
- retain canon digest, source refs, statements, constraints, permitted interpretations, unresolved `hmmm`, and provenance digest;
- keep semantic labels separate from metric values;
- preserve UCNS geometry identity, EDCM policy identity, METAPAT canon identity, and any Phi authorization identity as separate provenance components;
- create a new epoch when canon or policy identity changes;
- fail closed on malformed schema or provenance.

No EDCM implementation is included in this METAPAT repair.

## Phase 5 — Shared stack fixture

Status: hmmm / next cross-repository gate.

The deterministic fixture must prove:

1. METAPAT root canon remains byte-stable;
2. the envelope round-trips without loss;
3. an actual UCNS object is constructed;
4. stable hash and complete semantic provenance survive adaptation;
5. EDCM consumes constraints without making them metric values;
6. theorem status does not transfer;
7. `hmmm` fields survive the complete path;
8. canon or policy rotation produces a distinct epoch identity;
9. any constitutive fork is backed by a valid METAPAT authorization;
10. the authorization is bound to exact UCNS topology rather than inferred from payload presence.

## hmmm

The application-specific meaning of every future module remains separately declarative. Naming a module kind does not supply a measured state, an empirical result, or proof that an application object instantiates the named METAPAT term. The next METAPAT-native advancement is a complete addressable semantic module catalog; the first topology-bound Phi fixture remains a downstream UCNS/EDCM integration task.
