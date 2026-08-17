# METAPAT 0.7.0 — canon v2 rotation

## Identity

This release rotates the canon-bearing tensor clarification through every dependent identity:

```text
package: 0.7.0
canon: metapat-canon-v2
canon digest: 3bcfe224fc5bf7bac4d1035303b628447f81cfe81c31caf95ac18a74082bd9cc
catalog: metapat-semantic-catalog-v2
catalog digest: 5dbbe75a6ab488a8f745f24137a705de7c739925715518cba391f16cd7f22621
quantum-magnetism application: quantum-magnetism-application-v2
quantum-magnetism digest: a504c15b80371abf57cbdbcc32030bca11227f3231b377e3a6f537d9bc130195
electromagnetic-pipe application: three-phase-electromagnetic-pipe-application-v2
electromagnetic-pipe application digest: 9189aad20573e0c7e8e29cc795bb081bed89ebc5932c692b7d228899cc409940
electromagnetic-pipe design digest: 42f3985b72491583f08aaa00b5f90bf585c38f07cc42915fdfc2ff451e1d4134
```

The Fourth Axiom root statement remains exactly:

```text
Tensor is primitive.
```

The new prose explains simultaneity, nesting, recursion, and possible domain representations. It remains subordinate to the root. Mathematical, physical, computational, linguistic, chess, and other tools may explicate or represent the tensor; they do not redefine the METAPAT root.

## Consumer migration

Consumers must:

1. reject records pinned to `metapat-canon-v1` when v2 is required;
2. bind the exact v2 canon digest, envelope provenance digest, catalog version and digest, application version and digest, and any consumer-local policy identity;
3. mint a new consumer-local epoch rather than silently rebinding an old epoch;
4. preserve separate METAPAT semantic, UCNS geometry/proof, and EDCM measurement authority.

METAPAT declares the rotation and required bindings. UCNS, EDCM, and other consumers own their local epoch names and migrations.

## Current generated fixtures

```text
metapat/fixtures/root-spine-envelope-v2.json
metapat/fixtures/semantic-module-catalog-v2.json
metapat/fixtures/quantum-magnetism-application-v2.json
metapat/fixtures/three-phase-electromagnetic-pipe-v2.json
```

Regenerate and verify them with:

```bash
python tools/generate_catalog.py
python tools/generate_application_fixtures.py
python tools/generate_catalog.py --check
python tools/generate_application_fixtures.py --check
```

The v1 generated fixtures are removed from the current package surface; their identities remain recoverable from the `0.6.0` source epoch.

## hmmm

The exact names and rollout timing of downstream UCNS and EDCM consumer-local epochs remain owned by those repositories. Silence is not migration.
