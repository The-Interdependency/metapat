# METAPAT application modules

## Purpose

Application modules bind domain-specific uses of METAPAT to exact catalog modules without amending canon or transferring claim status.

A `MetapatApplicationModule` carries:

- application identity and version;
- application claim status;
- named domains and selected scales;
- exact source document references and statements;
- exact catalog version and digest;
- ordered catalog bindings;
- domain statements and shared question-form;
- what transfers and what does not;
- working question;
- evidence boundary and requirements;
- unresolved `hmmm`;
- explicit false status-transfer and validation fields;
- deterministic application digest.

The current v4 application-module wire schema is `2.0.0`. It is incompatible with the pre-v4 `1.0.0` parser epoch so parsing alone cannot become implicit migration.

## Catalog bindings

Each `ApplicationCatalogBinding` binds:

```text
catalog module id
catalog module digest
catalog module claim status
application role
application statement
binding digest
```

A binding states how an application uses a module. It does not change the module, inherit its status, prove the application, or establish UCNS topology.

Catalog validation requires exact agreement on catalog version/digest and every bound module ID, digest, and claim status.

A catalog rotation therefore invalidates stale application fixtures rather than silently relabeling them.

## Evidence firewall

Application modules currently permit:

```text
CROSS-DOMAIN-HYPOTHESIS
EMPIRICAL-FRONTIER
```

Every application module requires:

```text
root_impact = none
metapat_validity_claim = false
domain_validity_claim = false
measurement_validity_claim = false
ucns_theorem_status_transfer = false
ucns_topology_claim = false
```

The schema records a bounded application hypothesis and provenance. It does not supply external evidence.

## Source integrity

Application source references use:

```text
path/to/document.md#heading-slug::statement-N
```

`assert_application_sources_match()` fails if a source document, heading, exact statement, or source identity drifts.

The source Markdown remains the human-readable application surface. The fixture is its strict machine-readable identity-bearing representation.

## Quantum-magnetism vertical slice

```text
application: metapat.application.quantum_magnetism
version: quantum-magnetism-application-v4
status: CROSS-DOMAIN-HYPOTHESIS
catalog bindings: 12
root impact: none
```

It preserves nuclear, atomic, crystalline, and magnetic-domain scale distinctions and keeps physics as the governing evidence domain. The current v4 bindings include root restraint, partial domains, tensor, relate, scalar/state measurement, boundary, state, transformation, and cross-domain reconstruction.

Unresolved “field-space” meaning remains `hmmm`.

Package usage:

```python
from pathlib import Path
import metapat

catalog = metapat.canonical_semantic_catalog()
application = metapat.quantum_magnetism_application_module(catalog)

metapat.validate_application_against_catalog(application, catalog)
metapat.assert_application_sources_match(Path("."), application)
print(application.application_digest)
```

Packaged fixture:

```text
metapat/fixtures/quantum-magnetism-application-v4.json
```

## Electromagnetic-pipe vertical slice

The engineering application is separately bound as `EMPIRICAL-FRONTIER`. Its exact design identity and source bindings do not establish claimed electromagnetic, materials, thermal, insulation, mechanical, or fault performance; those remain answerable to engineering evidence.

Packaged fixture:

```text
metapat/fixtures/three-phase-electromagnetic-pipe-v4.json
```

## Regeneration

```bash
python tools/generate_application_fixtures.py
python tools/generate_application_fixtures.py --check
python tools/generate_msdmd.py --check
python tools/check_contract_graph.py
python -m pytest -q tests/test_application.py tests/test_quantum_magnetism.py tests/test_electromagnetic_pipe.py
```

Generated application fixtures must not be edited by hand.

## hmmm

Application schemas preserve declared evidence requirements but do not execute simulations, derive physical laws, collect measurements, or promote domain claims. Those remain evidence required from the owning domain.
