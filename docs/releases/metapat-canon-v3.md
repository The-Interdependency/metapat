# METAPAT canon v3

Status: proposed canon rotation on `research/platonic-energy-operators` until all repository gates pass.

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
- identity schema remains `2.0.0`; its shape did not change.

## Migration rule

v2 consumers must fail closed until they explicitly bind v3 module identities and digests. No v2 application binding is silently rebound.

## hmmm

Application migrations, regenerated fixtures, generated msdmd, and downstream consumer epochs remain incomplete until repository gates demonstrate them explicitly.
