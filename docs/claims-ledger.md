# METAPAT claims ledger

Date: 2026-07-12

This ledger classifies public doctrine and executable assertions without changing Erin Spencer's canon text. Executable checks of definitions and encoded conditions are contract tests; they are not independent empirical evidence, formal proof, or validation of Meta Energy Theory as external truth.

## Status vocabulary

```text
ROOT-STIPULATION
DEFINITION
INTERNAL-DERIVATION
IMPLEMENTED-CONTRACT
CROSS-DOMAIN-HYPOTHESIS
EMPIRICAL-FRONTIER
RETRACTED_OR_SUPERSEDED
```

## Root canon

| Statement or surface | Status | Source | Boundary |
|---|---|---|---|
| “Legible difference is distinction.” | ROOT-STIPULATION | `AXIOMS.md`, `CHAPTER_ZERO.md`, `metapat.canon.ROOT_SPINE[0]` | Substrate-independent canon; not inferred from UCNS or EDCM. |
| “Distinction defines boundaries.” | ROOT-STIPULATION | same root sources | Canon statement. |
| “Boundaries define simplex.” | ROOT-STIPULATION | same root sources | Canon statement. |
| “Boundary is simplex of distinction.” | ROOT-STIPULATION | same root sources | Canon statement. |
| “Simplex holds or modifies energy in a state of being.” | ROOT-STIPULATION | same root sources | Canon statement. |
| Tensor as primitive simultaneous arrangement of energy-states | DEFINITION | `AXIOMS.md`, `metapat.canon.PRIMITIVE_EXTENSION` | Definition; deterministic tests only preserve encoding. |
| Time as sequential tensor alteration | DEFINITION | `AXIOMS.md`, `metapat.canon.TIME_DEFINITION` | Definition; no empirical theory of time is established by a boolean helper. |
| Registration | DEFINITION | `GLOSSARY.md`, `metapat.canon.definitions()` | Distinct from time and consciousness. |
| Observer role | DEFINITION | `GLOSSARY.md`, `metapat.canon.definitions()` | Observer does not necessarily mean mind. |
| Question as bounded unresolved energy-state | DEFINITION | root documents, `metapat.canon.definitions()` | Definition; unresolved questions remain unresolved. |

## Internal derivations and checks

| Surface | Status | What it checks | What it does not establish |
|---|---|---|---|
| `boundary_earns_its_keep` | INTERNAL-DERIVATION plus IMPLEMENTED-CONTRACT | With supplied source/target held present, changed boundary and changed outcome satisfy the encoded condition. | Causal truth, empirical validation, theorem proof. |
| `tensor_precedes_time` | INTERNAL-DERIVATION plus IMPLEMENTED-CONTRACT | A tensor value is present and an ordered alteration sequence has at least two states. | Metaphysical or physical proof of temporal priority. |
| `registration_is_not_time` | INTERNAL-DERIVATION plus IMPLEMENTED-CONTRACT | Sequence may exist without registration; supplied registration preserves the sequence exactly. | Empirical validation of time or registration. |
| `observer_role_by_registration` | INTERNAL-DERIVATION plus IMPLEMENTED-CONTRACT | Supplied simplex record preserves the supplied sequence. | Mind, consciousness, intent, or lived observer status. |
| `consciousness_is_optional` | INTERNAL-DERIVATION plus IMPLEMENTED-CONTRACT | Registration value is present while a separate conscious-story value is non-empty. | Detection or proof of consciousness. |

## Implemented architecture contracts

| Surface | Status | Contract |
|---|---|---|
| `metapat.canon.canon_digest()` | IMPLEMENTED-CONTRACT | Deterministically identifies the exact importable canon surface; digest rotation is observable. |
| `MetapatModuleEnvelope` | IMPLEMENTED-CONTRACT | Immutable, versioned semantic-authority and provenance envelope; exact references, statements, constraints, permitted interpretations, unresolved `hmmm`, canon identity, and provenance digest survive serialization. |
| `metapat.ucns.adapt_envelope_to_ucns` | IMPLEMENTED-CONTRACT | Constructs an actual `ucns.UCNSObject`; keeps METAPAT statements as external provenance; records stable hash and schema; transfers no theorem status. |
| Package and wheel gates | IMPLEMENTED-CONTRACT | Installed `metapat` public surface, metadata, typing marker, deterministic envelopes, and optional actual-UCNS integration work as declared. |

## Cross-domain and empirical status

| Claim family | Status | Boundary |
|---|---|---|
| Applying METAPAT terms to a particular scientific, organizational, psychological, or AI domain | CROSS-DOMAIN-HYPOTHESIS unless separately demonstrated | Domain tools may not redefine root canon. |
| Mapping METAPAT statements into UCNS payload semantics | EMPIRICAL-FRONTIER / hmmm | Current adapter uses external provenance only. No payload meaning is ratified. |
| EDCM measurements corresponding to METAPAT semantic labels | EMPIRICAL-FRONTIER | Labels constrain interpretation; they are not measured values. |
| Claims that contract tests validate the ontology externally | RETRACTED_OR_SUPERSEDED | Tests protect encoded contracts only. |
| Claims that UCNS theorem status proves METAPAT ontology | RETRACTED_OR_SUPERSEDED | Proof-status transfer is forbidden. |

## Superseded architecture statements

| Former surface | Status | Replacement |
|---|---|---|
| Single flow `UCNS -> METAPAT -> EDCM` | RETRACTED_OR_SUPERSEDED | Separate authority, runtime-data, and proof-status flows in `metapat.flow_plan`. |
| METAPAT-native `UCNSObject`, normalization, carrier calculation, and composition | RETRACTED_OR_SUPERSEDED | Optional adapter to the actual `ucns` package; no second algebra. |
| “theorem validation helpers” wording | RETRACTED_OR_SUPERSEDED | Deterministic canon contract checks with explicit non-validation boundaries. |

## Usage

When adding or changing a public claim:

1. cite the exact source statement or executable surface;
2. assign one status from this ledger;
3. state what evidence would change that status;
4. update affected code metadata, documentation, and tests together;
5. preserve unresolved constraints as `hmmm`.

## hmmm

The status of future domain-specific modules cannot be assigned in advance. Each module must declare whether it is definition, internal derivation, cross-domain hypothesis, or empirical frontier rather than inheriting root status merely by using METAPAT vocabulary.
