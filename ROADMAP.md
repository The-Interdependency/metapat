# METAPAT Roadmap

## Current state

METAPAT is the canonical semantic authority for Meta Energy Theory. It now exposes:

- exact root canon constants and deterministic canon identity;
- immutable versioned `MetapatModuleEnvelope` records;
- deterministic canon contract checks with explicit non-validation boundaries;
- an optional adapter that constructs actual `ucns.UCNSObject` geometry;
- package, wheel, base, and actual-UCNS integration gates.

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
- Bind consumer artifacts to `CANON_VERSION` and `canon_digest()`.
- Keep unresolved details marked `hmmm`.
- Classify public claims in `docs/claims-ledger.md`.

## Phase 1 — Semantic module envelope

Status: implemented.

- `MetapatModuleEnvelope` is immutable and versioned.
- Exact source references and statements survive serialization.
- Constraints, permitted interpretations, unresolved constraints, canon identity, and provenance digest remain distinct.
- Canon or constraint rotation changes provenance identity.
- No measured EDCM values are present.

## Phase 2 — Actual UCNS geometry adapter

Status: implemented for ordered statement-count geometry.

- Base METAPAT remains importable without UCNS.
- Adapter calls without UCNS raise a clear dependency error.
- Adaptation constructs actual `ucns.UCNSObject` instances.
- Stable hash and UCNS serialization version are recorded.
- METAPAT statements remain external provenance; UCNS payloads remain unit.
- METAPAT contains no local normalization, product, factorization, star/disk-flip, or theorem-status algebra.

Remaining:

- hmmm: ratify whether any semantic statement may map into UCNS payloads or tags.
- hmmm: consume an official versioned UCNS bridge record if UCNS standardizes one.

## Phase 3 — EDCM semantic consumer

Status: downstream implementation required.

EDCM must:

- accept the exact versioned envelope;
- retain canon digest, source refs, constraints, permitted interpretations, unresolved `hmmm`, and provenance digest;
- keep semantic labels separate from metric values;
- preserve UCNS geometry identity, EDCM policy identity, and METAPAT canon identity as separate provenance components;
- create a new epoch when canon or policy identity changes;
- fail closed on malformed schema or provenance.

## Phase 4 — Shared stack fixture

Status: hmmm / next cross-repository gate.

The deterministic fixture must prove:

1. METAPAT root canon remains stable;
2. the envelope round-trips without loss;
3. an actual UCNS object is constructed;
4. stable hash and source references survive adaptation;
5. EDCM consumes constraints without making them metric values;
6. theorem status does not transfer;
7. `hmmm` fields survive the complete path;
8. canon or policy rotation produces a distinct epoch identity.

## Phase 5 — Metadata and drift completion

Status: partial.

- Reconcile remaining repo-level msdmd declarations and generated `llms.txt`.
- Run repo-local skill-lib drift checks.
- Add canon-file byte integrity and generated metadata gates.
- Keep open PRs that modify `.agents/skills/` separate from canon/runtime changes.

## hmmm

The application-specific meaning of future simplex, boundary-simplex, tensor, relation, gradient, registration, time, and question modules must be declared per module. Naming a module kind does not supply a measured state or an empirical result.
