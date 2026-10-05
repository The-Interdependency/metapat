# Provisional structural recurrence

Stack owns the current English semantic trajectories. UCHC remains the
extraction target until its graduation gates close. UCNS owns geometric
comparison and proof evidence; METAPAT classifies supplied recurrence evidence;
EDCM owns measurements. These roles transfer no semantic, proof, or measurement
status. The exact participants are recorded in
[`work-graphs/system-set-recurrence-v0.json`](work-graphs/system-set-recurrence-v0.json).

## Usage guidance

Install with `python -m pip install -e '.[dev]'`. Construct evidence with the
current catalog explicitly; never silently relabel an older catalog epoch.

```python
from metapat.catalog import CATALOG_VERSION, canonical_semantic_catalog
from metapat.structural_recurrence import RecurrenceEvidence, adjudicate_recurrence

catalog = canonical_semantic_catalog()
evidence = RecurrenceEvidence(
    source_domain="fixture:domain-a", target_domain="fixture:domain-b",
    source_origin_id="origin:a", target_origin_id="origin:b",
    source_path_id="path:a", target_path_id="path:b",
    declared_invariants=("fixture:ordered-relation",),
    preserved_invariants=(),
    mapping_complete=None, replay_passed=None,
    catalog_version=CATALOG_VERSION, catalog_digest=catalog.catalog_digest,
    catalog_module_ids=(
        "metapat.axiom.12.domain_qualification",
        "metapat.postulate.1.partial_domains",
        "metapat.postulate.6.cross_domain_falsification",
        "metapat.theory.11.cross_domain_reconstruction",
    ),
    ancestry_resolved=False,
    unresolved=("UCNS comparison evidence has not been supplied",),
)
decision = adjudicate_recurrence(evidence)
assert decision.outcome == "HMMM"
assert decision.independent is None
```

The example is synthetic. It establishes no relation between real domains.

## Decision requirements

| Outcome | Required supplied evidence |
| --- | --- |
| `SAME_STRUCTURE` | Complete mapping, successful replay, every named invariant preserved, resolved ancestry, no unresolved inputs, and a nonblank equivalence-proof identity. |
| `HOMOLOGOUS` | The same completed evidence without a proof identity, plus distinct origins or paths. Shared ancestry reduces independence without erasing recurrence. |
| `ANALOGOUS` | Completed mapping/replay/ancestry, no unresolved inputs, and a nonempty proper subset of declared invariants preserved. |
| `DIVERGENT` | Resolved inputs with failed mapping/replay, or no declared invariant preserved. |
| `HMMM` | Unresolved evidence, or complete preservation without a proof identity or distinct reconstruction paths. |

All records require distinct source/target domains, nonempty identifiers, and
current catalog version/digest with unique, existing module bindings including
all four required modules. Empty declared invariants, scalar sequence values,
blank invariant IDs, and undeclared preserved invariants are rejected.

`RecurrenceDecision` retains domains, origins, paths, catalog bindings, invariant
sets, proof identity, ancestry, mapping/replay status, and unresolved inputs.
Direct construction carries these same fields and must reproduce both outcome
and independence. Its three transfer flags must be exactly `False`.
Use `adjudicate_recurrence` to construct a decision from validated evidence.

## Verification and limits

Run `python -m pytest -q tests/test_structural_recurrence.py`, then the complete
gates in `COMPLIANCE.md`. Regenerate metadata with
`python tools/generate_msdmd.py` when source obligations or test declarations
change; check it with `python tools/generate_msdmd.py --check`.

The base suite checks the sealed synthetic Stack handoff fixture. To replay it
through the real producer, check out the exact Stack commit recorded in the work
graph, then run:

```bash
STACK_SOURCE_ROOT=/absolute/path/to/exact-stack-checkout \
  python -m pytest -q tests/test_stack_recurrence_handoff.py
```

The required CI integration job performs that checkout and replay. It rejects a
different commit, changed producer module bytes, changed emitted records, or a
receipt that cannot be independently recomputed. This is compatibility and
boundary evidence, not a geometric comparison or empirical recurrence result.

The tests check these encoded contracts. A supplied proof ID is retained and
required for `SAME_STRUCTURE`; this module does not verify the proof itself.
A catalog binding supplies provenance, not domain truth or a UCNS theorem.

## hmmm

The UCNS comparison law, equivalence theorem, and geometry binding English
semantic trajectories remain unresolved. A valid Stack receipt and matching
relation signatures cannot supply those missing conclusions. UCHC graduation
also remains incomplete.
