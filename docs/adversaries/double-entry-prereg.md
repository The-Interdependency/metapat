# Independent adversary preregistration — double-entry bookkeeping

Status: **FROZEN TEST PLAN / not canon**

Target under test: `docs/v2-v3-synthesis.md` on `main`.

Independent domain: double-entry bookkeeping / financial reporting.

Selection reason: a formal non-physical domain with explicit entities, reporting boundaries, measurable account states, state-changing transactions, sequential records, and conserved balancing constraints. It was not used to construct METAPAT v2, v3, or the v2→v3 synthesis.

## Source boundary

Primary authority for domain concepts: IFRS Conceptual Framework for Financial Reporting. Supporting mechanics source: standard double-entry bookkeeping definitions for accounts, debit/credit entries, balances, and the accounting equation.

No accounting concept may be redefined to make METAPAT fit.

## Frozen pass/fail tests

The synthesis SURVIVES only if all of the following hold:

1. **Native-language recoverability** — each mapped METAPAT term corresponds to a domain fact without changing the accounting fact's meaning.
2. **No metaphor substitution** — a root term fails if it can be mapped only by saying two unlike things are 'basically the same'.
3. **No missing primitive forced by the domain** — accounting invariants may require derived/domain laws, but must not require a new METAPAT root primitive unless the existing root cannot represent the structure without information loss.
4. **Root/action separation survives** — domain entities/states and state-changing operations remain distinguishable.
5. **Measurement separation survives** — an account state and its measured balance remain distinguishable.
6. **Sequence test** — ordered postings may instantiate time as sequential transformation without requiring time for the mere existence of the ledger structure.
7. **Boundary test** — the domain must supply a defensible boundary concept; METAPAT may not invent one merely to satisfy the root.
8. **Energy test** — the accounting domain itself must license the METAPAT use of `energy`, or `energy` as a universal cross-domain term is FALSIFIED/REQUIRES-REPLACEMENT. Structural similarity alone is insufficient.
9. **Domain invariant test** — the synthesis must represent the double-entry invariant (balanced debit/credit effects and the accounting equation) without pretending the invariant is a universal METAPAT law.
10. **Prediction/constraint test** — the mapping must do more than relabel accounting vocabulary: it must expose at least one honest structural constraint, failure condition, or distinction already checkable in the domain.

## Allowed outcomes

- `SURVIVED` — synthesis carries the domain without new root primitives or semantic distortion.
- `SURVIVED_WITH_REFINEMENT` — root survives, but a derived term/placement must change.
- `FALSIFIED` — at least one root claim fails under the domain.
- `UNRESOLVED` — the domain evidence does not decide a material mapping.

## Prohibited rescue moves

- redefining an accounting term after seeing a mismatch;
- calling every transaction 'energy' merely because it changes state;
- promoting debit/credit conservation to a universal METAPAT law;
- treating the reporting entity boundary as physical geometry;
- using `thing is that which is` as a tautological escape from a failed distinction;
- converting a missing mapping into analogy and scoring it as a pass.

## hmmm

The adversary is deliberately chosen to make the name *Energy Theory* earn its keep. If structure survives while `energy` does not, that is a result, not an embarrassment.
