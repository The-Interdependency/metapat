# Independent adversary result — double-entry bookkeeping

Status: **UNRESOLVED / tested synthesis; universal energy mapping FALSIFIED / not canon**

Preregistration: `docs/adversaries/double-entry-prereg.md`

Target: `docs/v2-v3-synthesis.md` at exact METAPAT commit `a1724645b3fc5d246cf8b7a3f8200c2ca3aa61f5`, Git blob `1a2db847197d40112fc29ca4ed11ffa4bc74bf0c`.

The preregistered decision rule is binding: the synthesis survives only if every frozen test passes, and its allowed `FALSIFIED` outcome requires a failed root claim. The universal Energy mapping fails, but the synthesis places Energy under measurement/result while material root mappings remain unresolved. The honest overall standing is therefore `UNRESOLVED`; the synthesis did not survive, and its universal Energy mapping is independently `FALSIFIED`. The refined candidate discussed below is post-result analysis and does not repair either result.

## Domain facts used

The source identities and bounded paragraphs are recorded in the preregistration. The test uses them without importing METAPAT assumptions into accounting:

1. IFRS Conceptual Framework for Financial Reporting:
   - a reporting entity has a determined reporting boundary;
   - financial statements depict economic resources, claims and changes in them;
   - recognition links depicted elements across statements and periods;
   - recognised elements are quantified using declared measurement bases.
2. Double-entry bookkeeping mechanics:
   - a transaction changes at least two accounts;
   - at least one debit and one credit are recorded;
   - total debits equal total credits.

These are domain constraints, not METAPAT claims.

## Frozen test results

| Test | Result | Reason |
|---|---|---|
| Native-language recoverability | **FALSIFIED for the tested synthesis** | Several structural mappings are supportable, but `energy` is not recoverable in native accounting language without adding a foreign claim. |
| No metaphor substitution | **FALSIFIED for universal `energy`** | Calling a financial transaction or monetary change `energy` merely because it changes state is the prohibited rescue move. |
| No missing root primitive | SURVIVED | The accounting balance law can remain a domain invariant over related changes; it need not become a universal METAPAT primitive. |
| Root/action separation | SURVIVED at the supported mappings | Accounting distinguishes entities/items and their properties from transactions/postings that alter recorded positions. Boundary-dependent structures remain unresolved below. |
| Measurement separation | SURVIVED | The underlying recognised right, obligation, account position or other measured property is distinct from a numerical balance/carrying amount produced under a measurement basis. |
| Sequence | **UNRESOLVED** | Ordered postings support sequential transformation, but the selected evidence does not establish the frozen claim that time is unnecessary for the mere existence of the ledger structure; a statement-of-position snapshot is not the ledger. |
| Boundary | **UNRESOLVED** | IFRS supplies a reporting boundary, but this test has not yet established the stronger METAPAT condition that the boundary itself is a thing between two identified things. |
| Energy | **FALSIFIED** | Accounting licenses resources, claims, measures, transactions and changes; it does not license calling their abstract change composite `energy`. |
| Domain invariant | **UNRESOLVED** | Debit/credit equality is supported, but the selected bounded evidence and evaluation omit the accounting-equation half of the frozen criterion. |
| Prediction/constraint | SURVIVED | A posting whose debits and credits do not balance violates double-entry bookkeeping. |

Because the Energy test fails, the tested synthesis does not survive and universal Energy naming is **FALSIFIED**. Because the allowed-outcome taxonomy reserves whole-synthesis `FALSIFIED` for a failed root claim while material root mappings remain unresolved, the whole-synthesis standing is **UNRESOLVED** rather than retroactively changing the frozen taxonomy.

## Mapping standing

### Thing — SURVIVED

Accounting supplies addressable things such as reporting entities, economic resources, claims, rights, obligations and accounts. No tautological rescue is needed for this bounded mapping.

### Boundary — UNRESOLVED

IFRS supplies a declared reporting-entity boundary that determines what is included in the reporting entity. That establishes a domain boundary concept, but not yet METAPAT's stronger root statement:

```text
Boundary is the thing between things.
```

This adversary has not independently established which accounting object is the boundary thing and which two things it lies between. Treating a scope delimiter as sufficient would weaken the tested root after seeing the evidence.

### State — SURVIVED

State is mapped to a metricable property or condition of the accounting thing: for example, recognition status, the existence/extent of a right or obligation, or the account's underlying recorded position before numerical measurement.

A numerical account balance or carrying amount is **not** used as state evidence in this mapping; it belongs on the scalar side below.

### Simplex — UNRESOLVED

Simplex requires a thing with boundary and state. State has support, but Boundary remains unresolved under the exact METAPAT definition, so this dependent mapping cannot be promoted to survived.

### Tensor — UNRESOLVED

A ledger is structured from related accounts/items, but METAPAT defines tensor as structure produced when **simplexes** relate. The selected accounting components have not yet been independently shown to satisfy Simplex at the tested scale. Generic structured relation is insufficient.

### Relate — SURVIVED

Double entry makes relation explicit: one transaction changes at least two accounts, and the balanced posting constrains the combined changes rather than one isolated account.

### Emerge — UNRESOLVED at this scale

Higher-order financial structures are produced from related elements, but the tested METAPAT emergence path depends on the unresolved Simplex/Tensor mapping. No independent pass is claimed here.

### Vector — SURVIVED at a bounded operational mapping

The evidence is the **state-altering transaction/posting effect**, not vector notation. A transaction changes the recorded position of affected accounts. Comparing scalar measurements before and after the posting exposes the signed/typed state changes from which that state-altering operation is inferred.

A sparse mathematical vector is a convenient representation of those coordinated changes; the notation itself supplies no semantic authority.

### Scalar — SURVIVED

Account balances, carrying amounts and other quantified amounts are scalar measurements of accounting properties under declared measurement bases. They remain measurements, not the underlying state itself.

### Transformation — SURVIVED

Transactions and recognised events change recorded rights, obligations, account positions, assets, liabilities, equity, income or expenses.

### Time — SURVIVED at the evaluated mapping; frozen sequence test UNRESOLVED

A statement of financial position can represent a state at one date. Ordered transactions and comparison of beginning/end reporting states instantiate sequential transformation. This does not settle whether time is unnecessary for the mere existence of the ledger structure, so the complete frozen sequence test remains unresolved.

### Energy — FALSIFIED as universal cross-domain ontology/name

The domain supplies no accounting fact that licenses:

```text
financial transaction = energy
monetary value = energy
state change = energy
```

The tested v3 definition

```text
Energy is vectors altering state through transformation across time.
```

would classify ordinary bookkeeping activity as energy solely because it matches an abstract change pattern. That violates the preregistered no-metaphor rule. The supported structural relations do not transfer the domain term `energy` into accounting.

## Domain invariant

Double entry supplies a bounded domain constraint without adding a METAPAT primitive:

```text
transaction
-> changes at least two accounts
-> at least one debit and one credit
-> total debits = total credits
```

This remains an accounting law over related changes. Similarity to conservation laws elsewhere does not authorize universal promotion.

The frozen invariant test also requires evaluation of the accounting equation. The selected evidence/evaluation does not establish that half, so the complete invariant test remains `UNRESOLVED`.

## Post-result refined candidate

The adversary supports retaining these mappings at their stated scopes:

```text
SURVIVED
Thing
State
Relate
Vector        # state-altering transaction effect inferred from scalar changes
Scalar
Transformation
Time
```

It leaves these mappings unresolved at the selected accounting scale:

```text
UNRESOLVED
Boundary
Simplex
Tensor
Emerge
```

It falsifies this tested universal mapping:

```text
FALSIFIED
Energy as the cross-domain name for the abstract state-change composite
```

This is a **candidate refinement after falsification**, not a preregistered outcome and not canon.

A domain-respecting replacement direction remains:

```text
Different domains may independently expose common structures and actions.
No domain owns those common structures by name or mechanism.
A domain term transfers only when the target domain independently licenses it.
```

## Separate standing of the partial-property postulate

The current v3 postulate says:

```text
Every domain exposes some properties of Platonic energy.
No domain exposes all properties of Platonic energy.
```

This adversary does **not** directly falsify that weaker existential claim. The report itself finds accounting analogues for several properties used in the v3 composite. Failure of the name/identity `energy` does not prove absence of every partial property.

Standing here: **UNRESOLVED**. A future falsifier must target the partial-property proposition itself rather than reuse the failure of the `energy` name.

## Standing

```text
tested v2->v3 synthesis: UNRESOLVED; it did not survive
Thing / State / Relate / Scalar / Transformation / Time: SURVIVED at stated scopes
Vector: SURVIVED only as state-altering transaction effect inferred from scalar changes
Boundary / Simplex / Tensor / Emerge: UNRESOLVED at selected accounting scale
Energy as universal cross-domain ontology/name: FALSIFIED
"every domain exposes some properties of Platonic energy": UNRESOLVED
accounting balance as universal law: REJECTED / domain-owned
post-result refined candidate: PROPOSED, not the preregistered outcome
```

## hmmm

Whether the project name **Meta Energy Theory** remains historical/scope-setting or changes with a future canon rotation is unresolved. Naming does not repair ontology.

One independent adversary can falsify the tested universal `energy` mapping. It does not establish that the unresolved structure survived, does not complete the frozen sequence or invariant tests, and does not settle the weaker partial-property postulate.
