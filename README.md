# METAPAT

**Meta Energy Theory — Axioms, Postulates, Theorems, and Theories**

METAPAT is the canonical source for Meta Energy Theory as a substrate-independent ontology of energy-state relation and transformation.

Energy Theory answers:

```text
What questions do I ask?
```

It does so by finding shared question-forms among domains while refusing to let any domain redefine the root.

## Root spine

```text
Legible difference is distinction.
Distinction defines boundaries.
Boundaries define simplex.
Boundary is simplex of distinction.
Simplex holds or modifies energy in a state of being.
```

## Primitive extension

```text
Tensor is primitive simultaneous arrangement of energy-states.
Without sequence, there is tensor.
Time is sequential tensor alteration.
```

## Current canon map

- [`CHAPTER_ZERO.md`](CHAPTER_ZERO.md) — Meta Energy Theory axioms, postulates, and theorems.
- [`AXIOMS.md`](AXIOMS.md) — invariant root and primitive extension.
- [`POSTULATES.md`](POSTULATES.md) — allowed working claims that organize application without changing root.
- [`THEOREMS.md`](THEOREMS.md) — derived statements and proof sketches.
- [`THEORIES.md`](THEORIES.md) — organized derivation families for applying the root without changing it.
- [`GLOSSARY.md`](GLOSSARY.md) — current term meanings and status.
- [`DOMAIN_RESTRAINT.md`](DOMAIN_RESTRAINT.md) — rule for importing tools from domains without domain capture.
- [`examples/`](examples/) — canonical examples used to test whether the ontology stays stable.
- [`tests/`](tests/) — executable theorem contract tests plus Markdown validation specs.
- [`codex/skill-lib-handoff.md`](codex/skill-lib-handoff.md) — handoff for altering `The-Interdependency/skill-lib` so it consumes METAPAT rather than owning Energy Theory.

## msdmd compliance

METAPAT now carries a skill-lib / msdmd compliance scaffold:

- [`AGENTS.md`](AGENTS.md) — agent entry point and source `LLMS` block.
- [`llms.txt`](llms.txt) — generated-style root instructions from the `LLMS` declaration.
- [`metapat_msdmd.ts`](metapat_msdmd.ts) — repo-level msdmd collection point.
- [`src/metapat/`](src/metapat/) — importable package modules with colocated `MODULE_BUILD`, `DOCS`, `CAPABILITIES`, `OWNERS`, `BOUNDARIES`, `CONTRACTS`, and `DEPENDENCIES` declarations where applicable.
- [`.agents/skills/`](.agents/skills/) — repo-local skill entries pointing back to canonical `The-Interdependency/skill-lib`.

## Planned architecture flow

```text
UCNS -> METAPAT -> EDCM
```

Current status:

```text
UCNS side: hmmm, planned but not implemented.
EDCM side: hmmm, planned but not implemented.
Exact bridge APIs: hmmm.
```

The flow plan is declared in [`src/metapat/flow_plan.py`](src/metapat/flow_plan.py). It records the intended architectural edge without pretending implementation exists.

## Repository rule

```text
No implementation owns the root.
```

`skill-lib`, `ucns`, `edcmbone`, `edcm`, `a0`, `a0p`, AIMMH, and other repositories may consume, apply, test, or represent METAPAT. They do not define it.

## Development check

After cloning:

```bash
python -m unittest discover -s tests
```

hmmm: full local execution of skill-lib drift/compliance checks has not yet been run in this repository after the initial scaffold commit.
