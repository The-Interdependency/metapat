# Independent adversary result — double-entry bookkeeping

Status: **FALSIFIED_IN_PART / SYNTHESIS REFINED / not canon**

Preregistration: `docs/adversaries/double-entry-prereg.md`

Target: the frozen v2→v3 synthesis on `main`.

## Domain facts used

The test uses two source classes without importing METAPAT assumptions into them:

1. IFRS Conceptual Framework for Financial Reporting:
   - a reporting entity may be one entity, part of one entity, or multiple entities;
   - the reporting entity has a determined boundary;
   - financial statements depict assets, liabilities, equity, income, expenses and changes in them;
   - recognition links beginning state, financial performance, owner contributions/distributions, and ending state;
   - recognised elements are quantified using declared measurement bases.
2. Double-entry bookkeeping mechanics:
   - each transaction is recorded in at least two general-ledger accounts;
   - at least one debit and one credit are recorded;
   - total debits equal total credits;
   - the accounting equation remains balanced.

These are domain constraints, not METAPAT claims.

## Frozen test results

| Test | Result | Reason |
|---|---|---|
| Native-language recoverability | SURVIVED except `energy` | Reporting entity, boundary, state, measurement, transaction, sequence and invariant map without redefining accounting; `energy` does not. |
| No metaphor substitution | FALSIFIED for universal `energy` | Calling a financial transaction or monetary value change `energy` adds a foreign claim solely because state changes. |
| No missing root primitive | SURVIVED | The accounting-specific balance law is a domain invariant over related state changes; it need not become a universal METAPAT primitive. |
| Root/action separation | SURVIVED | Accounts/items/reporting entities are distinguishable from transactions/postings that alter their recorded state. |
| Measurement separation | SURVIVED strongly | IFRS explicitly separates the item being measured, the measurement basis, and the resulting measure. |
| Sequence | SURVIVED | Ledger structure and a statement-of-position snapshot do not require sequence; transactions and reporting periods introduce ordered state transformation. |
| Boundary | SURVIVED | IFRS explicitly defines and reasons about the reporting entity boundary; it is conceptual rather than physical. |
| Energy | **FALSIFIED** | Accounting licenses economic resources, monetary measures, transactions and changes; it does not license the claim that these are energy. |
| Domain invariant | SURVIVED | Debit/credit equality and the accounting equation are representable as constraints on domain state/transformation without universal promotion. |
| Prediction/constraint | SURVIVED | A one-sided or debit/credit-unbalanced posting is invalid under double entry; a valid posting preserves the accounting balance relation. |

## Root mapping

### Thing — SURVIVED

Accounting supplies explicit addressable things: reporting entities, units of account, assets, liabilities, rights, obligations, accounts, and recognised items.

No appeal to `thing is that which is` is needed to rescue the mapping.

### Boundary — SURVIVED

The IFRS reporting entity has an explicit boundary determining which economic activities are included in the reporting entity.

This is useful evidence that METAPAT boundary need not be physical geometry.

### State — SURVIVED

Examples include an account balance, an asset or liability carrying amount, recognition status, and the reporting entity's financial position.

These are properties of domain things that may be measured.

### Simplex — SURVIVED

A reporting entity is bounded and has measurable state. A unit of account likewise has a declared scope and measurable/accountable state.

The domain does not require every accounting thing to be a simplex; it supplies valid simplex instances.

### Tensor — SURVIVED

A ledger or financial statement is structured from related addressable items/accounts. Its snapshot configuration exists as structure without requiring that the reader replay every transaction in sequence.

### Relate — SURVIVED strongly

Double entry makes relation unavoidable: one transaction affects at least two accounts. The balanced posting is a relation among account-state changes, not a property of one isolated account.

### Emerge — SURVIVED with restraint

Financial position and performance are constructed from recognised and related elements. `Emerge` is acceptable only as METAPAT's name for produced higher-order structure; it must not imply spontaneous physical emergence.

### Vector — SURVIVED as exact representation

A transaction can be represented as a sparse directed change over an ordered set of account states. Its debit/credit entries specify signed/typed changes to those states.

Accounting need not use the word `vector`; the mapping is valid because it is an exact mathematical representation of multiple coordinated state changes, not a metaphor.

### Scalar — SURVIVED strongly

Balances, carrying amounts, and other monetary measures are scalar state metrics under a declared measurement basis.

### Transformation — SURVIVED

Transactions and other recognised events change account balances, assets, liabilities, equity, income or expenses.

### Time — SURVIVED

A statement of financial position can be a state at one date; ordered transactions and comparison between beginning/end reporting states instantiate sequential transformation.

### Energy — FALSIFIED as universal ontology

The domain supplies no accounting fact that licenses:

```text
financial transaction = energy
monetary value = energy
state change = energy
```

The v3 definition

```text
Energy is vectors altering state through transformation across time.
```

would classify ordinary bookkeeping activity as energy solely because it matches an abstract change pattern. That violates the preregistered no-metaphor rule.

The structural composite survives. The universal name `energy` does not.

## Domain invariant

Double-entry adds a strong constraint without adding a METAPAT primitive:

```text
transaction
-> postings to at least two accounts
-> total debits = total credits
-> accounting equation remains balanced
```

This is a domain law over related transformations.

METAPAT can represent the accounts, states, relation, measures and transformations while accounting owns the balancing law.

The law must not be promoted into a universal conservation theorem merely because it resembles conservation laws elsewhere.

## Refined synthesis

The independent domain supports this universal layer:

```text
STRUCTURE
Thing
Boundary
State
Simplex
Tensor

ACTION
Relate
Emerge
Vector

MEASUREMENT / RESULT
Scalar
Transformation
Time
```

Useful derived operators remain:

```text
Distinction
Relation/configuration
State-metric difference
Boundary mediation
Tensor simultaneity
Registration
Question
Observer
```

Domain-qualified terms remain outside universal ontology unless independently recovered:

```text
Gradient
Integration criteria
Energy
Domain invariants such as debit/credit balance
```

## Consequence for Meta Energy Theory

The accounting adversary does **not** show that the structures used to study energy are wrong.

It falsifies the stronger claim that every domain-instantiated state transformation should itself be called energy.

A defensible synthesis is therefore:

```text
Common structures/actions may recur across domains.
Energy is one domain-qualified realization of those structures where the domain itself licenses energy.
Structural recurrence does not transfer the name, mechanism, evidence, or conservation law of energy into another domain.
```

This preserves METAPAT as a project that began from energy and compares recurrent structure across domains, while preventing `energy` from swallowing every form of change.

The current v3 statements

```text
Every domain exposes some properties of Platonic energy.
No domain exposes all properties of Platonic energy.
```

are therefore **FALSIFIED AS UNIVERSAL CLAIMS** by this adversary unless `Platonic energy` is explicitly redefined as a non-energy structural abstraction. Such a redefinition would be semantic rescue and is rejected by this test.

A candidate replacement is:

```text
Different domains may independently expose common structures and actions.
No domain owns those common structures by name or mechanism.
A domain term transfers only when the target domain independently licenses it.
```

## Standing

```text
v3 structural root through Time: SURVIVED
v2-derived operational layer: SURVIVED with prior placement refinements
Energy as universal axiom: FALSIFIED
"every domain exposes Platonic energy": FALSIFIED
accounting balance as universal law: REJECTED / domain-owned
refined synthesis: SURVIVED this independent adversary
```

## hmmm

Whether the project name **Meta Energy Theory** should remain historical/scope-setting or be changed to reflect the more general structure/action substrate is unresolved. Naming does not get to repair ontology.

One independent adversary is enough to falsify a universal claim; it is not enough to establish that the refined synthesis is complete.
