# METAPAT canon v4 — domain-qualified energy

Status: **ADOPTED CANON ROTATION / evidence-bound**

Adopted by the explicit canon-rotation decision in METAPAT PR #32, merged as `2a55cebc0ba1cd77661688a6590c34c71c3ff705`; current canon identity is `metapat-canon-v4`. Repository gates support implementation consistency but do not substitute for that assent.

Evidence considered: `docs/adversaries/double-entry-result.md`.

## Evidence standing

The independent double-entry adversary falsified the tested universal v3 use of `energy`:

```text
Energy is vectors altering state through transformation across time.
```

as a cross-domain name that would attach merely because an abstract state-change pattern recurs. The accounting domain did not independently license that term.

The same adversary did **not** directly falsify the weaker historical proposition:

```text
Every domain exposes some properties of Platonic energy.
```

Its standing in that adversary is `UNRESOLVED`. v4 withdraws the proposition from current canon rather than treating an unresolved result as falsification.

The adversary leaves Boundary, Simplex, Tensor, Emerge, and parts of its frozen sequence/invariant tests `UNRESOLVED`; it does not establish that the complete spine survived. PR #32's explicit canon decision, rather than this adversary, preserves the v3 structure/action spine through Time while removing universal energy naming.

## Adopted change

v4 preserves the v3 structure/action spine through Time and replaces universal energy naming with domain qualification:

```text
A structural recurrence does not transfer a domain term, mechanism, evidence standard, or conservation law.
A domain term applies only where that domain independently licenses it.
Energy is domain-qualified: a domain may identify energy in structures involving state, vector, transformation, and time, but METAPAT does not call all such structures energy.
```

The cross-domain rule is:

```text
Different domains may independently expose common structures and actions.
No domain owns common structure by name or mechanism.
Similarity permits comparison, not semantic transfer.
```

## Preserved root

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
```

## Replacement

v3 Axiom 12 `Energy` is deprecated and removed.

v4 Axiom 12 is `Domain Qualification`.

The former Theory 7 `Derived Energy` becomes `Domain Qualification` and constrains when a domain term may attach to the common structure.

## Identity and migration

- canon epoch: `metapat-canon-v4`
- identity schema: `4.0.0`
- module-envelope wire schema: `2.0.0` (incompatible with the prior `1.2.0` epoch)
- application-module wire schema: `2.0.0` (incompatible with the prior `1.0.0` epoch)
- UCNS adaptation-record wire: `2.0.0` (incompatible with the prior `1.0.0` epoch)
- catalog epoch: `metapat-semantic-catalog-v4`

v3 added `energy_definition` and required schema `3.0.0`; v4 removes that field and adds `domain_qualification_definition`, requiring schema `4.0.0`. The module-envelope wire schema also rotates from `1.2.0` to `2.0.0`, preventing a prior parser from accepting a v4 envelope merely because its field shape is familiar. The application-module and outer UCNS adaptation-record wires rotate from `1.0.0` to `2.0.0`; the latter also validates its embedded current envelope, provenance, and canon identities. These rotations prevent either cross-repository wrapper from bypassing the canon boundary. Consumers bound to v2, the historically mislabeled v3 wire shape, schema `3.0.0`, envelope schema `1.2.0`, application schema `1.0.0`, or adaptation-record wire `1.0.0` reject v4 until they explicitly bind identity schema `4.0.0`, each `2.0.0` wire, and the v4 canon, catalog, application, and provenance identities. No shared field names or successful digest computation constitute assent or migration.

## Nonclaims

- This does not claim accounting and physics are the same.
- This does not deny physical energy.
- This does not make debit/credit balance a universal conservation law.
- This does not rename every state change as energy.
- This does not claim the double-entry adversary falsified every weaker partial-property proposition about energy.
- This does not establish completeness of the remaining root.

## hmmm

The project name `Meta Energy Theory` remains unchanged by this rotation. Whether the historical name still best describes the surviving substrate is unresolved and must not be used to smuggle `energy` back into universal ontology.
