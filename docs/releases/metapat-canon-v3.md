# METAPAT canon v3

Status: **SUPERSEDED HISTORICAL ROTATION**. v3 was merged in PR #29 and later replaced by v4 in PR #32. Repository gates were implementation evidence, not canon assent.

## Root change

v3 replaces the v2 energy-first primitive extension with a structure/action construction:

```text
Thing
Boundary
State
Simplex
Tensor

Relate
Emerge
Vector

Scalar
Transformation
Time
Energy
```

Exact root definitions remain owned by `AXIOMS.md` and `CHAPTER_ZERO.md`.

## Principal consequences

- tensor is constructed from related simplexes rather than primitive before simplex;
- state is distinct from scalar measurement;
- vector alters state and is inferred through scalar measurement;
- time is sequential transformation;
- energy is derived rather than primitive;
- every domain exposes some properties of Platonic energy and no domain exposes all;
- cross-domain recurrence is tested by removing implementation-specific properties rather than importing a domain as root;
- completeness is never presumed.

## Identity

- canon epoch: `metapat-canon-v3`
- catalog epoch: `metapat-semantic-catalog-v3`
- identity schema: `3.0.0`; v3 added the top-level `energy_definition` field and therefore could not truthfully reuse v2 schema `2.0.0`.

The merged v3 implementation incorrectly continued to emit `2.0.0`. This historical defect is recorded rather than treating the mislabeled wire identity as a supported schema. Current v4 consumers must not accept either label as v4.

## Migration rule

At the v3 boundary, v2 consumers had to fail closed until they explicitly bound v3 schema `3.0.0`, module identities, and digests. No v2 application binding was eligible for silent rebinding. Current consumers must use the v4 migration rule instead.

## hmmm

The exact downstream effect of the short-lived mislabeled v3 schema remains `hmmm`; repository history preserves the defect, and no consumer may infer migration from the reused `2.0.0` label.
