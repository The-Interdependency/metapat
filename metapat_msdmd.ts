import { defineMsdmdCollection } from "./.agents/skills/msdmd/collection";

export default defineMsdmdCollection({
  "declarations": [
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "packaging",
        "given": "the base package is imported without invoking the optional adapter",
        "then": "canon, catalog, application, engineering, relation, and Phi policy surfaces work without requiring UCNS"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_base_import_without_ucns"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the public package surface is inspected",
        "then": "no local UCNSObject class is exported"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_no_public_local_ucns"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "packaging",
        "given": "the installed package resources are inspected",
        "then": "the PEP 561 py.typed marker is present"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_package_typed_marker"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "packaging",
        "given": "the installed package and distribution metadata are inspected",
        "then": "both expose the same authoritative version"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_package_version_matches_metadata"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "packaging",
        "given": "the installed package resources are inspected",
        "then": "the electromagnetic-pipe design fixture is packaged and matches the live constructor exactly"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_pipe_fixture_packaged"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "packaging",
        "given": "the installed package resources are inspected",
        "then": "the canonical root-spine envelope fixture is packaged and matches the live constructor exactly"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_root_fixture_packaged"
    },
    {
      "block": "DEPENDENCIES",
      "fields": {
        "class": "runtime",
        "external_optional": "ucns",
        "imports": "metapat.canon, metapat.catalog, metapat.application, metapat.quantum_magnetism, metapat.electromagnetic_pipe, metapat.relations, metapat.envelope, metapat.flow_plan, metapat.validation, metapat.ucns_phi, metapat.ucns",
        "owner": "The Interdependency",
        "provides": "metapat_package_exports",
        "summary": "base exports depend on canon, catalog, application and engineering schemas, relations, envelopes, checks, flow declarations, Phi policy, and a lazy optional UCNS adapter"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_package_dependency_edges"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "schema",
        "module_name": "metapat",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "__version__, canon identity, semantic catalog and relations, application schemas, quantum-magnetism application, electromagnetic-pipe design, MetapatModuleEnvelope, UCNSPhiPolicy, UCNSForkAuthorization, actual-UCNS adapter",
        "requires": "metapat_canon_core, metapat_module_envelope, metapat_semantic_relations, metapat_semantic_catalog, metapat_application_module_schema, metapat_quantum_magnetism_application, metapat_electromagnetic_pipe_application, metapat_canon_contract_checks, metapat_ucns_phi_policy, optional metapat_ucns_adapter",
        "rollback": "remove electromagnetic-pipe exports and fixture while preserving canon, catalog, quantum application, envelope, Phi, and adapter surfaces",
        "rollout": "importable_package version 0.7.0",
        "since": "2026-07-21",
        "storage_boundary": "read-only canon and fixture verification plus serialization only",
        "summary": "re-exports byte-complete canon identity, the semantic catalog, strict catalog-bound applications and engineering records, immutable envelopes and relations, deterministic checks, explicit UCNS Phi authority, and the optional actual-UCNS adapter",
        "tests": "tests.test_contracts, tests.test_envelope, tests.test_catalog, tests.test_relations, tests.test_application, tests.test_quantum_magnetism, tests.test_electromagnetic_pipe, tests.test_canon_integrity, tests.test_ucns_phi, tests.test_ucns_bridge, tests.test_packaging",
        "unresolved": "downstream consumers must bind module and fork authorizations to exact application and UCNS topology identities",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/__init__.py",
      "id": "metapat_package_exports"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "semantic question-form only; no canon amendment, UCNS topology or notation selection, EDCM measurement validation, physical-frequency claim, theorem transfer, or external truth claim",
        "user_data_boundary": "public conceptual text only"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:public conceptual text only",
        "exposes": "metapat.affixiation_harmonics.affixiation_harmonics_application_module",
        "inputs": "canonical semantic catalog v2",
        "outputs": "strict cross-domain application module and deterministic digest",
        "summary": "emits one deterministic catalog-bound application record for affixiation and time-agnostic harmonic relation"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_semantics"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the application evidence and transfer boundaries are inspected",
        "then": "METAPAT owns semantic meaning, UCNS owns implementation, EDCM owns measurement, and no status transfers automatically"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_authority_firewall"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "application status and unresolved fields are inspected",
        "then": "the application remains a cross-domain hypothesis with no root impact and no promotion into postulate or theory"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_candidate_status"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "integration_contract",
        "given": "the affixiation-harmonics application module is constructed",
        "then": "every applied METAPAT concept is bound to an exact catalog module identity, digest, and claim status"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_catalog_bound"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "the application constructor and source document are checked together",
        "then": "exact definitions, catalog bindings, transfer limits, evidence boundaries, and hmmm statements remain source-current"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_source_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "affixiation semantics are inspected",
        "then": "participants remain individually addressable with identity and provenance preserved and no flattening or topology is implied"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_identity_preserved"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "recurrence, oscillation, and harmonic semantics are inspected",
        "then": "an ordered non-temporal relational parameter is permitted without redefining time or implying physical frequency"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_harmonics_time_agnostic"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, agent, UCNS consumer, EDCM consumer",
        "covers": "affixiation_harmonics_application_module, semantic definitions, authority boundaries, downstream evidence requirements",
        "source": "docs/applications/affixiation-harmonics.md",
        "status": "current",
        "summary": "defines affixiation, time-agnostic recurrence and oscillation, harmonic relation, resonance, and the METAPAT/UCNS/EDCM authority firewall"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "source declarations and application mapping constants",
        "module_kind": "schema",
        "module_name": "metapat.affixiation_harmonics",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "AFFIXIATION_HARMONICS_APPLICATION_VERSION, AFFIXIATION_HARMONICS_BINDING_SPECS, affixiation_harmonics_application_module, affixiation_harmonics_application_digest",
        "requires": "metapat_application_module_schema, metapat_semantic_catalog",
        "rollback": "remove application module and documentation while preserving canon and the generic application schema",
        "rollout": "importable catalog-bound application module",
        "since": "2026-08-20",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "defines catalog-bound conceptual semantics for identity-preserving affixiation and time-agnostic harmonic relation while leaving UCNS implementation and EDCM measurement authority downstream",
        "tests": "tests.test_affixiation_harmonics",
        "unresolved": "UCNS harmonic notation and EDCM measurement validity remain downstream; promotion into postulate or theory remains unresolved",
        "user_data_boundary": "public conceptual application text only"
      },
      "file": "src/metapat/affixiation_harmonics.py",
      "id": "metapat_affixiation_harmonics_application"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "application identity and semantic mapping only; no canon amendment, domain validation, EDCM measurement, formal proof, UCNS topology claim, or theorem-status transfer",
        "user_data_boundary": "exact application statements and provenance only"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_module_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:application text only",
        "exposes": "metapat.ApplicationCatalogBinding, metapat.MetapatApplicationModule, metapat.validate_application_against_catalog",
        "inputs": "catalog modules, application statements, domain scales, evidence requirements, source provenance, unresolved constraints",
        "outputs": "immutable application module, strict JSON, deterministic binding and application digests",
        "summary": "binds application statements to exact catalog modules and preserves domain evidence boundaries without claim-status transfer"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_catalog_bound_application_modules"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "an application binds a catalog module",
        "then": "module id, module digest, module claim status, application role, and application statement are digest-bound"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_binding_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "integration_contract",
        "given": "an application is checked against a canonical catalog",
        "then": "catalog version and digest plus every bound module identity, digest, and claim status match exactly"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_catalog_validation"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "a valid application module is serialized and reconstructed",
        "then": "every field and digest survive while unknown, missing, or incorrectly typed fields fail closed"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_roundtrip_strict"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "application source references are resolved against repository Markdown",
        "then": "every heading exists and each exact source statement occurs within its declared section"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_source_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "an application module or binding is constructed",
        "then": "root impact and all ontology, domain, measurement, theorem-transfer, and topology claims remain false"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_status_firewall"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "application content, binding content, catalog identity, or evidence boundary changes without digest rotation",
        "then": "reconstruction fails closed"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_tamper_rejected"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, agent, domain reviewer",
        "covers": "ApplicationCatalogBinding, MetapatApplicationModule, source checks, catalog validation",
        "source": "docs/application-modules.md",
        "status": "current",
        "summary": "documents catalog-bound application identity, source integrity, evidence firewalls, and downstream limits"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_module_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "canonical JSON, digest, strict scalar and sequence validators, Markdown source resolver",
        "module_kind": "schema",
        "module_name": "metapat.application",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "application schema constants, ApplicationCatalogBinding, MetapatApplicationModule, bind_catalog_module, validate_application_against_catalog, application_source_mismatches, assert_application_sources_match",
        "requires": "metapat_semantic_catalog, metapat_semantic_relations",
        "rollback": "remove application exports and fixtures while preserving canonical catalog",
        "rollout": "importable package schema and packaged application fixtures",
        "since": "2026-07-21",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "defines strict application modules and catalog bindings that preserve source, claim status, evidence boundaries, and unresolved hmmm without promoting applications into canon or proof",
        "tests": "tests.test_application",
        "unresolved": "application-specific empirical validation remains external to METAPAT",
        "user_data_boundary": "application doctrine, domain statements, and source provenance only"
      },
      "file": "src/metapat/application.py",
      "id": "metapat_application_module_schema"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "read",
        "summary": "static doctrine constants plus read-only verification of canon-bearing repository files",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_boundaries"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:read-only, network:none, user_data:none",
        "exposes": "metapat.canon.definitions, metapat.canon.canon_digest, metapat.canon.assert_canon_files_match",
        "inputs": "optional repository root for file-integrity checks",
        "outputs": "dict, sha256 digest, mismatch map",
        "summary": "provides exact importable constants and deterministic identity for METAPAT root doctrine"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_constants"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "the same exact canon constants and file manifest are serialized repeatedly",
        "then": "canonical data and the sha256 digest remain byte-for-byte stable"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_digest_deterministic"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "one canon-bearing file changes by one or more bytes",
        "then": "the mismatch is reported and strict verification fails closed"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_file_drift_visible"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the repository canon files are read without modification",
        "then": "every observed byte identity matches the committed manifest"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_files_match_repository"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the public canon file manifest is inspected",
        "then": "every canon-bearing Markdown file is named exactly once with an exact Git blob identity"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_manifest_complete"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "canon definitions are imported",
        "then": "root spine contains the current five load-bearing root lines in order"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_root_spine_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "canon definitions are inspected",
        "then": "time and registration remain separate definitions"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_time_not_registration"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "agent, developer",
        "covers": "exact constants, canon file manifest, identity schema, drift detection",
        "source": "AXIOMS.md, CHAPTER_ZERO.md, POSTULATES.md, THEOREMS.md, THEORIES.md, GLOSSARY.md, DOMAIN_RESTRAINT.md",
        "status": "current",
        "summary": "documents METAPAT root doctrine and byte-complete canon identity"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_json_bytes",
        "module_kind": "schema",
        "module_name": "metapat.canon",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "CANON_VERSION, CANON_IDENTITY_SCHEMA_VERSION, CANON_FILE_BLOBS, root_spine, primitive_extension, definitions, canonical_canon_data, canonical_canon_manifest_data, canon_digest, canon_manifest_digest, canon_file_mismatches, assert_canon_files_match",
        "requires": "none",
        "rollback": "restore the prior identity schema while preserving exact canon constants and Markdown files",
        "rollout": "importable_package",
        "since": "2026-07-12",
        "storage_boundary": "read",
        "summary": "exposes exact Meta Energy Theory root constants and a deterministic identity that includes every canon-bearing Markdown file",
        "tests": "tests.test_contracts, tests.test_envelope, tests.test_canon_integrity",
        "unresolved": "formal governance process for future authorized canon rotations",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_core"
    },
    {
      "block": "OWNERS",
      "fields": {
        "escalation": "hmmm",
        "owner": "The Interdependency",
        "review_required_for": "public_api, docs, canon, identity",
        "steward": "Erin Spencer"
      },
      "file": "src/metapat/canon.py",
      "id": "metapat_canon_owner"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "read-only canon verification and serialization only",
        "summary": "catalog identity and semantic addressability only; no empirical state, EDCM value, formal proof, inferred UCNS containment, or consumer application meaning",
        "user_data_boundary": "canon text and module identifiers only"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_semantic_catalog_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:canon text only",
        "exposes": "metapat.canonical_semantic_catalog, metapat.semantic_module_by_id, metapat.catalog_digest",
        "inputs": "byte-identified METAPAT canon and static catalog declarations",
        "outputs": "40 ordered semantic modules, declared derivation relations, strict JSON, catalog digest",
        "summary": "emits a deterministic complete catalog of current METAPAT doctrine and exact declared derivation edges"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_addressable_semantic_catalog"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "doctrine classes and claim statuses are inspected",
        "then": "postulates remain working postulates, internal derivations remain internal, and the symbolic transfer theory remains a cross-domain hypothesis"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_claim_status_bounded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "the canonical semantic catalog is constructed",
        "then": "it contains exactly one root, twelve axioms, seven postulates, eight theorems, and twelve theories in contiguous deterministic order"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_complete_ordered"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "identity_contract",
        "given": "catalog modules are inspected",
        "then": "every module id, ordinal, envelope digest, and module digest is unique and deterministic"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_module_identity_unique"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "a catalog is constructed without a UCNS fork authorization",
        "then": "constitutive-simultaneous relations are rejected rather than inferred from ancestry, order, or geometry"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_no_constitutive_inference"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "catalog relation records are inspected",
        "then": "every endpoint exists and every relation is an exact source-backed declared derivation rather than inferred analogy"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_relations_declared"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "a module statement, claim status, relation, constraint, canon identity, or unresolved field changes",
        "then": "a module, relation, or catalog digest changes"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_rotation_visible"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "the complete catalog is serialized and reconstructed",
        "then": "all modules, relations, unresolved hmmm, and digests survive while malformed or unknown fields fail closed"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_roundtrip_strict"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "catalog references are resolved against repository canon files",
        "then": "every heading exists and every exact source statement occurs within its declared section"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_catalog_sources_exact"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, agent, consumer",
        "covers": "canonical_semantic_catalog, SemanticCatalogModule, MetapatSemanticCatalog, source integrity, catalog fixture",
        "source": "docs/semantic-module-catalog.md",
        "status": "current",
        "summary": "documents catalog completeness, source resolution, claim classification, relation ancestry, and downstream limits"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_semantic_catalog_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_json, _digest, _text, _integer",
        "module_kind": "schema",
        "module_name": "metapat.catalog",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "catalog constants, SemanticCatalogModule, MetapatSemanticCatalog, canonical_semantic_catalog, semantic_module_by_id, catalog_digest, catalog_module_counts, assert_catalog_complete, catalog_source_mismatches, assert_catalog_sources_match",
        "requires": "metapat_canon_core, metapat_module_envelope, metapat_semantic_relations, metapat_semantic_catalog_builder",
        "rollback": "remove catalog exports and fixture while preserving envelope and canon surfaces",
        "rollout": "importable_package and packaged semantic-module-catalog-v2 fixture",
        "since": "2026-07-21",
        "storage_boundary": "read-only canon verification and serialization only",
        "summary": "materializes the complete current METAPAT root, axiom, postulate, theorem, and theory surfaces as addressable provenance-bearing modules",
        "tests": "tests.test_catalog",
        "unresolved": "downstream consumers must declare application meaning and any Phi topology binding separately",
        "user_data_boundary": "exact canon statements and references only"
      },
      "file": "src/metapat/catalog.py",
      "id": "metapat_semantic_catalog"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_refs, _envelope, _slug, _section, _ANCHORS, _STATUS",
        "module_kind": "schema",
        "module_name": "metapat.catalog_build",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "canonical_semantic_catalog, semantic_module_by_id, catalog_digest, catalog_module_counts, assert_catalog_complete, catalog_source_mismatches, assert_catalog_sources_match",
        "requires": "metapat_semantic_catalog, metapat_semantic_catalog_declarations, metapat_semantic_relations",
        "rollback": "remove only with semantic catalog schema and fixture",
        "rollout": "importable package constructor and compliance gate",
        "since": "2026-07-21",
        "storage_boundary": "read-only canon verification and serialization only",
        "summary": "constructs the canonical semantic catalog from static declarations and verifies completeness and exact Markdown source resolution",
        "tests": "tests.test_catalog",
        "unresolved": "downstream application meaning and Phi topology binding remain separate",
        "user_data_boundary": "exact canon statements and references only"
      },
      "file": "src/metapat/catalog_build.py",
      "id": "metapat_semantic_catalog_builder"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "CATALOG_SPECS, CATALOG_DERIVATIONS, CATALOG_DERIVED_TEXT",
        "module_kind": "schema",
        "module_name": "metapat.catalog_data",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "none",
        "requires": "metapat_semantic_doctrine_declarations, metapat_semantic_theory_declarations",
        "rollback": "remove only with semantic catalog",
        "rollout": "internal catalog constructor dependency",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "combines stable doctrine and theory declarations for canonical catalog construction",
        "tests": "tests.test_catalog",
        "unresolved": "future canon rotation requires explicit catalog version and migration",
        "user_data_boundary": "exact canon statements and references only"
      },
      "file": "src/metapat/catalog_data.py",
      "id": "metapat_semantic_catalog_declarations"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "DOCTRINE_SPECS",
        "module_kind": "schema",
        "module_name": "metapat.catalog_doctrine_data",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "none",
        "requires": "metapat_canon_core",
        "rollback": "remove only with semantic catalog",
        "rollout": "internal catalog constructor dependency",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "declares stable axiom, postulate, and theorem module identities, classes, source sections, and exact statements",
        "tests": "tests.test_catalog",
        "unresolved": "none",
        "user_data_boundary": "exact canon statements only"
      },
      "file": "src/metapat/catalog_doctrine_data.py",
      "id": "metapat_semantic_doctrine_declarations"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "THEORY_SPECS, CATALOG_DERIVATIONS, CATALOG_DERIVED_TEXT",
        "module_kind": "schema",
        "module_name": "metapat.catalog_theory_data",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "none",
        "requires": "metapat_canon_core",
        "rollback": "remove only with semantic catalog",
        "rollout": "internal catalog constructor dependency",
        "since": "2026-07-21",
        "storage_boundary": "none",
        "summary": "declares stable theory module identities, exact claim statements, and source-declared derivation ancestry",
        "tests": "tests.test_catalog",
        "unresolved": "theory 10 remains cross-domain hypothesis and theory 11 remains domain-restraint bounded",
        "user_data_boundary": "exact canon statements only"
      },
      "file": "src/metapat/catalog_theory_data.py",
      "id": "metapat_semantic_theory_declarations"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "engineering proposal and optimization structure only; no electromagnetic, materials, insulation, thermal, fault, spacecraft, measurement, UCNS topology, or theorem-status validity claim",
        "user_data_boundary": "public engineering handoff only"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_electromagnetic_pipe_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:public engineering handoff only",
        "exposes": "metapat.electromagnetic_pipe_design",
        "inputs": "canonical semantic catalog v2",
        "outputs": "strict engineering application, typed topology and material-search record, deterministic digest",
        "summary": "emits one deterministic catalog-bound engineering application and typed device-design record for the nested three-phase pipe system"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_electromagnetic_pipe_fixture"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "materials_boundary",
        "given": "the alloy candidates are inspected",
        "then": "every candidate is atomic percent, totals 100, preserves Fe plus Co plus Ni at 75, Cr at 15, Mn at 10, and remains a search candidate rather than an ideal-alloy claim"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_alloy_search_bounded"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "integration_contract",
        "given": "the pipe application is constructed",
        "then": "every METAPAT use is bound to an exact catalog module identity, digest, and claim status"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_application_catalog_bound"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the mobile-element fields are inspected",
        "then": "the objects remain ceramic-coated magnetic eddy-current attractors and are never typed as bearings"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_attractors_not_bearings"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "the electromagnetic-pipe design record is constructed",
        "then": "three radial layers, two handednesses, three phases per handedness, eighteen phase circuits, and six three-phase control systems remain exact and internally reconciled"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_control_topology_exact"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the design record and application are inspected",
        "then": "electromagnetic, materials, insulation, thermal, mechanical, spacecraft, measurement, topology, theorem-transfer, and METAPAT validity claims remain false"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_performance_firewall"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "a valid design record is serialized and reconstructed",
        "then": "every nested field and digest survive while unknown, missing, malformed, or tampered fields fail closed"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_roundtrip_strict"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "the constructor and handoff source are checked together",
        "then": "control topology, geometry, winding, attractor, alloy, instrumentation, fault, high-voltage, next-work, evidence, and hmmm statements remain source-current"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_source_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "the winding layers are inspected",
        "then": "outer 12 AWG at 6 turns per inch, middle 16 AWG at 12, and inner 20 AWG at 18 remain ordered and exact"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_pipe_winding_layers_exact"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, electrical engineer, materials engineer, safety reviewer, agent",
        "covers": "electromagnetic_pipe_application_module, electromagnetic_pipe_design, catalog bindings, source integrity, engineering evidence boundary",
        "source": "docs/applications/three-phase-electromagnetic-pipe.md",
        "status": "current",
        "summary": "preserves geometry, six-vector control topology, mobile-attractor distinction, alloy search, instrumentation, fault objectives, and empirical boundaries"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_electromagnetic_pipe_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "source declarations, binding specifications, canonical JSON and digest helpers",
        "module_kind": "schema",
        "module_name": "metapat.electromagnetic_pipe",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "pipe application and design schema constants, WindingLayerSpec, AlloyCandidate, ElectromagneticPipeDesign, electromagnetic_pipe_application_module, electromagnetic_pipe_design, electromagnetic_pipe_design_digest",
        "requires": "metapat_application_module_schema, metapat_semantic_catalog",
        "rollback": "remove electromagnetic-pipe exports and fixture while preserving the generic application schema and semantic catalog",
        "rollout": "public package exports and deterministic fixture in metapat 0.7.0",
        "since": "2026-07-21",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "preserves the three-phase nested electromagnetic-pipe handoff as a strict catalog-bound engineering application and design record without claiming device performance",
        "tests": "tests.test_electromagnetic_pipe",
        "unresolved": "frequency, current, target field, shielding, phase shift, attractor geometry, thermal limits, protection distance, and alloy performance remain empirical frontiers",
        "user_data_boundary": "public engineering handoff and provenance only"
      },
      "file": "src/metapat/electromagnetic_pipe.py",
      "id": "metapat_electromagnetic_pipe_application"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only",
        "summary": "semantic authority and provenance only; no UCNS algebra, EDCM measurement, theorem transfer, or empirical validation",
        "user_data_boundary": "preserves caller-supplied text exactly"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_module_envelope_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:caller-supplied exact text",
        "exposes": "metapat.envelope.MetapatModuleEnvelope, metapat.envelope.root_spine_module_envelope",
        "inputs": "module identity, kind, exact source references and statements, constraints, permitted interpretations, unresolved constraints",
        "outputs": "immutable envelope, deterministic JSON, provenance digest",
        "summary": "emits deterministic immutable semantic constraints and provenance without calculated EDCM measurements"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_semantic_envelope"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the same envelope is serialized repeatedly",
        "then": "JSON bytes remain canonical and deterministic"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_canonical_json"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "the canonical root-spine envelope is constructed",
        "then": "exact statements, references, constraints, permitted interpretations, canon identity, and unresolved hmmm are present"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_exact_provenance"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "otherwise identical envelopes with different canon digest or semantic constraints",
        "then": "provenance digests differ"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_rotation_visible"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "a valid immutable module envelope including unresolved hmmm fields",
        "then": "deterministic JSON roundtrip preserves every field and digest"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_roundtrip"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "serialized envelope content changes without a matching provenance digest",
        "then": "reconstruction fails closed"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_tamper_rejected"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "serialized envelope fields have incorrect scalar or sequence types",
        "then": "reconstruction rejects them rather than coercing them"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_type_strict"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "serialized envelope data contains an undeclared field",
        "then": "reconstruction fails closed"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_envelope_unknown_field_rejected"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "a semantic envelope is constructed",
        "then": "no measured-values field or measurement-validity claim exists"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_labels_not_measurements"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, agent",
        "covers": "MetapatModuleEnvelope, strict schema validation, provenance digest, canon identity, unresolved hmmm preservation",
        "source": "codex-handoff/2026-07-12-stack-repair/REQUIRED_CHANGES.md",
        "status": "current",
        "summary": "defines the METAPAT-to-consumer semantic authority boundary"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_module_envelope_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_payload, _digest_payload, _tuple_of_strings, _require_string, _require_string_sequence",
        "module_kind": "schema",
        "module_name": "metapat.envelope",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "MODULE_ENVELOPE_SCHEMA_ID, MODULE_ENVELOPE_SCHEMA_VERSION, MODULE_KINDS, MetapatModuleEnvelope, build_module_envelope, root_spine_module_envelope",
        "requires": "metapat_canon_core",
        "rollback": "remove envelope exports and cross-repository adapter fixtures",
        "rollout": "importable_package",
        "since": "2026-07-12",
        "storage_boundary": "serialized envelope only; no persistence performed",
        "summary": "versioned immutable semantic-authority and provenance envelope for UCNS adapters and EDCM consumers",
        "tests": "tests.test_envelope, tests.test_catalog, tests.test_ucns_bridge, tests.test_packaging",
        "unresolved": "semantic mappings beyond external provenance and explicitly authorized constitutive-simultaneous forks remain unresolved",
        "user_data_boundary": "caller-supplied statements and constraints are preserved exactly"
      },
      "file": "src/metapat/envelope.py",
      "id": "metapat_module_envelope"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "none",
        "summary": "architecture status constants with no active external calls",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/flow_plan.py",
      "id": "metapat_flow_boundaries"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:none, network:none, user_data:none",
        "exposes": "metapat.flow_plan.AUTHORITY_FLOW, metapat.flow_plan.RUNTIME_DATA_FLOW, metapat.flow_plan.PROOF_STATUS_FLOW",
        "inputs": "none",
        "outputs": "str",
        "summary": "exposes distinct authority, runtime-data, and proof-status architecture declarations"
      },
      "file": "src/metapat/flow_plan.py",
      "id": "metapat_flow_status"
    },
    {
      "block": "DEPENDENCIES",
      "fields": {
        "class": "architecture",
        "direction": "authority and runtime data are separate",
        "external": "The-Interdependency/ucns, The-Interdependency/edcm",
        "internal": "metapat.envelope, metapat.ucns",
        "owner": "The Interdependency",
        "provides": "metapat_flow_plan",
        "summary": "METAPAT constrains interpretation while actual UCNS carries geometry and EDCM measures source evidence"
      },
      "file": "src/metapat/flow_plan.py",
      "id": "metapat_flow_edges"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "schema",
        "module_name": "metapat.flow_plan",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "AUTHORITY_FLOW, RUNTIME_DATA_FLOW, PROOF_STATUS_FLOW, UCNS_SIDE_STATUS, EDCM_SIDE_STATUS",
        "requires": "metapat_module_envelope, metapat_ucns_adapter",
        "rollback": "restore prior architecture declarations",
        "rollout": "documentation_and_contract",
        "since": "2026-07-12",
        "storage_boundary": "none",
        "summary": "separates METAPAT semantic authority flow, EDCM/UCNS runtime data flow, and proof-status non-transfer",
        "tests": "tests.test_contracts, tests.test_envelope, tests.test_ucns_bridge",
        "unresolved": "question-to-measurement design constructor remains hmmm; EDCM semantic-envelope consumer exists",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/flow_plan.py",
      "id": "metapat_flow_plan"
    },
    {
      "block": "OWNERS",
      "fields": {
        "escalation": "hmmm",
        "owner": "The Interdependency",
        "review_required_for": "dependency, public_api, canon",
        "steward": "Erin Spencer"
      },
      "file": "src/metapat/flow_plan.py",
      "id": "metapat_flow_owner"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "worked semantic mapping only; physics remains answerable to physics and no root, proof, measurement, UCNS topology, or theorem-status claim is made",
        "user_data_boundary": "public application text only"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_magnetism_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:public application text only",
        "exposes": "metapat.quantum_magnetism_application_module",
        "inputs": "canonical semantic catalog v2",
        "outputs": "strict cross-domain application module and deterministic digest",
        "summary": "emits one deterministic catalog-bound application record for nuclear charge configuration and magnetic state formation"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_magnetism_fixture"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "integration_contract",
        "given": "the quantum-magnetism application module is constructed",
        "then": "every applied METAPAT term is bound to an exact catalog module digest and declared claim status"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_application_catalog_bound"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the application evidence fields are inspected",
        "then": "physics claims remain answerable to physics and all METAPAT, domain, measurement, theorem-transfer, and UCNS-topology validation claims remain false"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_application_physics_firewall"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "domain_boundary",
        "given": "selected physical scales and transfer limits are inspected",
        "then": "nuclear, atomic, crystalline, and magnetic-domain scales remain distinct and component identity is not inferred across scales"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_application_scales_distinct"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "the application constructor and source document are checked together",
        "then": "exact identity, catalog-binding, mapping, transfer, evidence, and hmmm statements remain source-current"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_application_source_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the application module and its catalog bindings are inspected",
        "then": "application status remains CROSS-DOMAIN-HYPOTHESIS, root impact remains none, and theory 10 is not imported"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_application_status_preserved"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, physicist, domain reviewer, agent",
        "covers": "quantum_magnetism_application_module, catalog bindings, source integrity, evidence boundary",
        "source": "docs/applications/quantum-magnetism.md",
        "status": "current",
        "summary": "binds the worked quantum-magnetism application to exact catalog modules while preserving scale, transfer, non-transfer, and physics evidence boundaries"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_magnetism_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "source declarations and application mapping constants",
        "module_kind": "schema",
        "module_name": "metapat.quantum_magnetism",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "QUANTUM_MAGNETISM_APPLICATION_VERSION, QUANTUM_MAGNETISM_BINDING_SPECS, quantum_magnetism_application_module, quantum_magnetism_application_digest",
        "requires": "metapat_application_module_schema, metapat_semantic_catalog",
        "rollback": "remove application exports and fixture while preserving generic application schema and canonical catalog",
        "rollout": "importable package constructor and packaged fixture",
        "since": "2026-07-21",
        "storage_boundary": "serialization-only and read-only source verification",
        "summary": "materializes the quantum-magnetism worked note as a strict cross-domain application module bound to exact catalog module identities and evidence limits",
        "tests": "tests.test_application, tests.test_quantum_magnetism",
        "unresolved": "field-space remains ambiguous among physical field, configuration space, and general potential-state landscape",
        "user_data_boundary": "public worked physics application text only"
      },
      "file": "src/metapat/quantum_magnetism.py",
      "id": "metapat_quantum_magnetism_application"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only",
        "summary": "relation records declare semantic ancestry only; they do not prove ontology, measurement validity, UCNS topology, or constitutive containment",
        "user_data_boundary": "canon text and module identifiers only"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_semantic_relation_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:canon text only",
        "exposes": "metapat.MetapatModuleRelation, metapat.build_relation",
        "inputs": "module endpoints, relation kind, evidence status, exact source references and statements, unresolved constraints",
        "outputs": "immutable relation record, deterministic JSON, relation digest",
        "summary": "emits deterministic semantic ancestry records with exact source provenance and no inherited proof or measurement status"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_semantic_relation_records"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "a semantic ancestry record is constructed",
        "then": "the record contains evidence classification but no theorem-transfer, measurement-value, ontology-validity, or topology-validity field"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_relation_no_status_transfer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "a valid semantic relation is serialized and reconstructed",
        "then": "every field and the deterministic digest survive while unknown, missing, or incorrectly typed fields fail closed"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_relation_roundtrip_strict"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "relation endpoints, source provenance, evidence status, or unresolved constraints change without digest rotation",
        "then": "reconstruction fails closed"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_relation_tamper_rejected"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "semantic relation and claim-status vocabularies are inspected",
        "then": "only declared relation kinds and evidence statuses are accepted"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_relation_vocabulary_bounded"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer, agent",
        "covers": "MetapatModuleRelation, RELATION_KINDS, CLAIM_STATUSES",
        "source": "docs/semantic-module-catalog.md",
        "status": "current",
        "summary": "documents relation vocabulary, evidence status, strict identity, and the prohibition on inferred constitutive containment"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_semantic_relations_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_json, _digest, _text, _strings",
        "module_kind": "schema",
        "module_name": "metapat.relations",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "CLAIM_STATUSES, RELATION_KINDS, RELATION_SCHEMA_ID, RELATION_SCHEMA_VERSION, MetapatModuleRelation, build_relation",
        "requires": "metapat_module_envelope",
        "rollback": "remove relation exports and catalog relation records",
        "rollout": "importable_package",
        "since": "2026-07-21",
        "storage_boundary": "serialization-only",
        "summary": "defines strict digest-bound semantic relation records and bounded claim-status vocabulary for the canonical module catalog",
        "tests": "tests.test_relations",
        "unresolved": "formal proof objects remain outside relation records",
        "user_data_boundary": "exact doctrine references and statements only"
      },
      "file": "src/metapat/relations.py",
      "id": "metapat_semantic_relations"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "archived face-bit or universal composition behavior is requested",
        "then": "the adapter fails closed"
      },
      "file": "src/metapat/ucns.py",
      "id": "metapat_ucns_archived_operations_rejected"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an installed package named ucns is inspected",
        "then": "only the exact producer epoch, profile, and bridge identities activate the adapter"
      },
      "file": "src/metapat/ucns.py",
      "id": "metapat_ucns_exact_identity_or_inactive"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary",
        "given": "an adaptation succeeds",
        "then": "theorem, measurement, and METAPAT validity transfer fields remain false"
      },
      "file": "src/metapat/ucns.py",
      "id": "metapat_ucns_no_authority_transfer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance",
        "given": "a METAPAT envelope is adapted through the exact profile",
        "then": "statement order and multiplicity survive while semantic text remains external provenance"
      },
      "file": "src/metapat/ucns.py",
      "id": "metapat_ucns_ordered_occurrence_provenance"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_package_present, _validate_module",
        "module_kind": "adapter",
        "module_name": "metapat.ucns",
        "network_boundary": "package import only",
        "owner": "The Interdependency",
        "public_surface": "UCNSConsumerStatus, UCNSAdaptationRecord, UCNSAdaptation, require_ucns, adapt_envelope_to_ucns, root_spine_adaptation, root_spine_ucns, compose",
        "requires": "metapat_module_envelope, exact UCNS post-reset profile",
        "rollback": "restore typed suspension without restoring archived adapter surfaces",
        "rollout": "exact_profile_only",
        "since": "2026-07-23",
        "storage_boundary": "deterministic serialized bridge and provenance records",
        "summary": "consumes only the exact post-reset UCNS ordered-occurrence profile while retaining METAPAT semantic authority externally",
        "tests": "tests/test_ucns_bridge.py",
        "unresolved": "no universal composition or factorization is authorized",
        "user_data_boundary": "semantic statements remain external provenance and are not placed in UCNS payloads"
      },
      "file": "src/metapat/ucns.py",
      "id": "metapat_exact_ucns_profile_consumer"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "serialization-only",
        "summary": "METAPAT authorizes meaning but does not construct UCNS algebra, validate topology, or transfer proof/measurement status",
        "user_data_boundary": "semantic module identities and canon references only"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_ucns_phi_boundary"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:serialization-only, network:none, user_data:semantic provenance only",
        "exposes": "metapat.authorize_constitutive_fork",
        "inputs": "MetapatModuleEnvelope, ordered child ids, source references, unresolved constraints",
        "outputs": "UCNSForkAuthorization",
        "summary": "authorizes ordered simultaneous constitutive children of one METAPAT parent"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_constitutive_fork_authority"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "integration_contract",
        "given": "authorization is checked against an envelope and child order",
        "then": "canon, parent, order, references, and policy match exactly"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_authorization_binds_canon_and_order"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "an authorization is constructed or decoded",
        "then": "relation_kind equals constitutive-simultaneous exactly"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_constitutive_relation_only"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "the default Phi policy is inspected",
        "then": "mapping remains external-provenance and forks require explicit authorization"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_default_external_provenance"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "provenance_contract",
        "given": "a fork is authorized from a canonical envelope",
        "then": "parent, ordered children, canon, policy, and source references are digest-bound"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_fork_requires_explicit_authorization"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "time, adjacency, provenance, alternatives, fiq connectivity, or external action is presented as containment",
        "then": "authorization fails closed"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_negative_relations_rejected"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "boundary_contract",
        "given": "any Phi policy or authorization",
        "then": "theorem_status_transfer and metapat_validity_claim remain false"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_no_status_transfer"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "schema_contract",
        "given": "authorization is serialized and reconstructed",
        "then": "fields and digest survive while malformed or tampered records fail closed"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_phi_record_roundtrip"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer",
        "covers": "UCNSPhiPolicy, UCNSForkAuthorization, authorize_constitutive_fork, validate_fork_authorization",
        "source": "docs/ucns-phi-policy.md",
        "status": "current",
        "summary": "documents constitutive-fork authorization and downstream fail-closed enforcement"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_ucns_phi_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_canonical_json, _strings, _payload, _digest",
        "module_kind": "schema",
        "module_name": "ucns_phi",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "UCNSPhiPolicy, UCNSForkAuthorization, ForkAuthorizationError, DEFAULT_UCNS_PHI_POLICY, authorize_constitutive_fork, validate_fork_authorization, PHI_POLICY_SCHEMA_ID, PHI_POLICY_VERSION, FORK_AUTHORIZATION_SCHEMA_ID, FORK_AUTHORIZATION_SCHEMA_VERSION, CONSTITUTIVE_RELATION_KIND, PROHIBITED_FORK_RELATION_KINDS",
        "requires": "metapat_module_envelope",
        "rollback": "remove exports and consumers; external-provenance UCNS adaptation remains unchanged",
        "rollout": "additive_semantic_authority_surface",
        "since": "2026-07-15",
        "storage_boundary": "serialization-only",
        "summary": "issues strict canon-bound constitutive-simultaneous authorization records before semantic UCNS payload forks",
        "tests": "tests.test_ucns_phi",
        "unresolved": "downstream EDCM must bind authorizations to actual UCNS payload topology",
        "user_data_boundary": "METAPAT module identities and source references remain semantic provenance; no transcript or measurement values"
      },
      "file": "src/metapat/ucns_phi.py",
      "id": "metapat_ucns_phi_policy"
    },
    {
      "block": "BOUNDARIES",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "network_boundary": "none",
        "storage_boundary": "none",
        "summary": "pure deterministic conditions; no external effects, theorem verification, or empirical validity claim",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/validation.py",
      "id": "metapat_contract_boundaries"
    },
    {
      "block": "CAPABILITIES",
      "fields": {
        "boundaries": "auth:none, storage:none, network:none, user_data:none",
        "exposes": "metapat.validation.boundary_earns_its_keep, metapat.validation.tensor_precedes_time, metapat.validation.registration_is_not_time, metapat.validation.observer_role_by_registration, metapat.validation.consciousness_is_optional",
        "inputs": "source_state, target_state, boundary_state, outcome, tensor_state, sequence, registration, story",
        "outputs": "bool",
        "summary": "checks deterministic Python conditions associated with METAPAT statements without claiming proof or empirical validation"
      },
      "file": "src/metapat/validation.py",
      "id": "metapat_canon_contract_checks"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "source and target are fixed while boundary state changes",
        "then": "encoded boundary condition passes only when outcome changes"
      },
      "file": "src/metapat/validation.py",
      "id": "boundary_change_changes_outcome"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "non-conscious registration with or without a separate conscious story",
        "then": "encoded condition requires registration but does not require conscious narrative"
      },
      "file": "src/metapat/validation.py",
      "id": "consciousness_optional_observer_mode"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "a simplex and a tensor alteration sequence",
        "then": "encoded observer-role condition passes only when the sequence is registered"
      },
      "file": "src/metapat/validation.py",
      "id": "observer_role_requires_registration"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "a tensor alteration sequence and an optional registration",
        "then": "encoded condition allows sequence without registration and checks exact preservation when present"
      },
      "file": "src/metapat/validation.py",
      "id": "registration_not_time"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "canon_contract",
        "given": "one tensor state and then an ordered pair of tensor states",
        "then": "encoded tensor-before-sequence condition passes"
      },
      "file": "src/metapat/validation.py",
      "id": "tensor_before_time"
    },
    {
      "block": "DOCS",
      "fields": {
        "audience": "developer",
        "covers": "boundary_earns_its_keep, tensor_precedes_time, registration_is_not_time, observer_role_by_registration, consciousness_is_optional",
        "source": "THEOREMS.md, docs/claims-ledger.md",
        "status": "current",
        "summary": "documents deterministic encoded conditions and their non-validation boundary"
      },
      "file": "src/metapat/validation.py",
      "id": "metapat_canon_contract_docs"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "none",
        "module_kind": "service",
        "module_name": "metapat.validation",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "boundary_earns_its_keep, tensor_precedes_time, registration_is_not_time, observer_role_by_registration, consciousness_is_optional",
        "requires": "none",
        "rollback": "restore prior metadata wording without changing function behavior",
        "rollout": "importable_package",
        "since": "2026-07-12",
        "storage_boundary": "none",
        "summary": "deterministic canon contract checks retained at the compatibility module path; not theorem verification or empirical validation",
        "tests": "tests.test_contracts",
        "unresolved": "whether a future major version moves these helpers to metapat.contracts",
        "user_data_boundary": "none"
      },
      "file": "src/metapat/validation.py",
      "id": "metapat_canon_contract_checks"
    },
    {
      "block": "OWNERS",
      "fields": {
        "escalation": "hmmm",
        "owner": "The Interdependency",
        "review_required_for": "public_api, tests, canon",
        "steward": "Erin Spencer"
      },
      "file": "src/metapat/validation.py",
      "id": "metapat_contract_owner"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_authority_firewall_is_explicit",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_affixiation_harmonics_authority_firewall"
      },
      "file": "tests/test_affixiation_harmonics.py",
      "id": "check_affixiation_harmonics_authority_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_remains_unpromoted",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_affixiation_harmonics_candidate_status"
      },
      "file": "tests/test_affixiation_harmonics.py",
      "id": "check_affixiation_harmonics_candidate_status"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_bindings_match_catalog",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_affixiation_harmonics_catalog_bound"
      },
      "file": "tests/test_affixiation_harmonics.py",
      "id": "check_affixiation_harmonics_catalog_bound"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_source_is_current",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_affixiation_harmonics_source_current"
      },
      "file": "tests/test_affixiation_harmonics.py",
      "id": "check_affixiation_harmonics_source_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_affixiation_preserves_identity_without_selecting_topology",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_affixiation_identity_preserved"
      },
      "file": "tests/test_affixiation_harmonics.py",
      "id": "check_affixiation_identity_preserved"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_harmonic_semantics_do_not_require_time",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_harmonics_time_agnostic"
      },
      "file": "tests/test_affixiation_harmonics.py",
      "id": "check_harmonics_time_agnostic"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_binding_is_exact_and_digest_bound",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_application_binding_exact"
      },
      "file": "tests/test_application.py",
      "id": "check_application_binding_exact"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_validates_against_exact_catalog",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_application_catalog_validation"
      },
      "file": "tests/test_application.py",
      "id": "check_application_catalog_validation"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_roundtrip_and_types_are_strict",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_application_roundtrip_strict"
      },
      "file": "tests/test_application.py",
      "id": "check_application_roundtrip_strict"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_source_statements_match",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_application_source_exact"
      },
      "file": "tests/test_application.py",
      "id": "check_application_source_exact"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_status_firewall_is_explicit",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_application_status_firewall"
      },
      "file": "tests/test_application.py",
      "id": "check_application_status_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_application_and_binding_tamper_are_rejected",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_application_tamper_rejected"
      },
      "file": "tests/test_application.py",
      "id": "check_application_tamper_rejected"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_canon_file_drift_is_reported",
        "cleanup": "tempdir_teardown",
        "mutates": "tempdir",
        "proves": "metapat_canon_file_drift_visible"
      },
      "file": "tests/test_canon_integrity.py",
      "id": "check_canon_file_drift_visible"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_manifest_names_all_canon_files",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_canon_manifest_complete"
      },
      "file": "tests/test_canon_integrity.py",
      "id": "check_canon_manifest_complete"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_repository_canon_files_match_manifest",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_canon_files_match_repository"
      },
      "file": "tests/test_canon_integrity.py",
      "id": "check_repository_canon_files_match"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_claim_statuses_remain_bounded",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_claim_status_bounded"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_claim_status_bounded"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_is_complete_and_ordered",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_complete_ordered"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_complete_ordered"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_packaged_catalog_fixture_is_current",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_fixture_current"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_fixture_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_fixture_render_is_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_fixture_generated"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_fixture_generated"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_module_identity_is_unique",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_module_identity_unique"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_identity_unique"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_rejects_unauthorized_constitutive_relation",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_no_constitutive_inference"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_no_constitutive_inference"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_relations_are_declared_and_resolvable",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_relations_declared"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_relations_declared"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_rotation_changes_identity",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_rotation_visible"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_rotation_visible"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_roundtrip_is_strict",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_roundtrip_strict"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_roundtrip_strict"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_catalog_sources_match_repository",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_catalog_sources_exact"
      },
      "file": "tests/test_catalog.py",
      "id": "check_catalog_sources_exact"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_packaged_root_spine_fixture_is_current",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_root_envelope_fixture_current"
      },
      "file": "tests/test_catalog.py",
      "id": "check_root_envelope_fixture_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_root_spine_fixture_render_is_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_root_envelope_fixture_generated"
      },
      "file": "tests/test_catalog.py",
      "id": "check_root_envelope_fixture_generated"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_audit_reports_required_negative_gaps",
        "cleanup": "tempdir_teardown",
        "mutates": "tempdir",
        "proves": "metapat_contract_audit_detects_gaps"
      },
      "file": "tests/test_contract_audit.py",
      "id": "check_contract_audit_negative_gaps"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_repository_contract_graph_closes",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_contract_graph_closes"
      },
      "file": "tests/test_contract_audit.py",
      "id": "check_repository_contract_graph_closes"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_boundary_change_changes_outcome",
        "cleanup": "none",
        "mutates": "none",
        "proves": "boundary_change_changes_outcome"
      },
      "file": "tests/test_contracts.py",
      "id": "check_boundary_change_changes_outcome"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_consciousness_is_optional",
        "cleanup": "none",
        "mutates": "none",
        "proves": "consciousness_optional_observer_mode"
      },
      "file": "tests/test_contracts.py",
      "id": "check_consciousness_optional"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_observer_role_by_registration",
        "cleanup": "none",
        "mutates": "none",
        "proves": "observer_role_requires_registration"
      },
      "file": "tests/test_contracts.py",
      "id": "check_observer_role_registration"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_registration_is_not_time",
        "cleanup": "none",
        "mutates": "none",
        "proves": "registration_not_time"
      },
      "file": "tests/test_contracts.py",
      "id": "check_registration_not_time"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_root_spine_contains_current_axioms",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_root_spine_exact"
      },
      "file": "tests/test_contracts.py",
      "id": "check_root_spine_exact"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_tensor_precedes_time",
        "cleanup": "none",
        "mutates": "none",
        "proves": "tensor_before_time"
      },
      "file": "tests/test_contracts.py",
      "id": "check_tensor_precedes_time"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_time_and_registration_are_separated",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_time_not_registration"
      },
      "file": "tests/test_contracts.py",
      "id": "check_time_registration_separated"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_alloy_search_bounded",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_alloy_search_bounded"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_alloy_search"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_attractors_not_bearings",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_attractors_not_bearings"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_attractors_not_bearings"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_application_catalog_bound",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_application_catalog_bound"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_catalog_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_control_topology_exact",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_control_topology_exact"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_control_topology"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_packaged_pipe_fixture_matches_live_constructor",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_pipe_fixture_current"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_fixture_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_fixture_renderer_is_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_fixture_generated"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_fixture_rendered"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_performance_firewall",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_performance_firewall"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_performance_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_roundtrip_strict",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_roundtrip_strict"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_roundtrip"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_source_current",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_pipe_source_current"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_source_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_pipe_winding_layers_exact",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_pipe_winding_layers_exact"
      },
      "file": "tests/test_electromagnetic_pipe.py",
      "id": "check_pipe_winding_layers"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_canon_digest_is_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_canon_digest_deterministic"
      },
      "file": "tests/test_envelope.py",
      "id": "check_canon_digest_deterministic"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_serialized_envelope_is_canonical_json",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_canonical_json"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_canonical_json"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_root_spine_envelope_preserves_exact_sources_and_constraints",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_exact_provenance"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_exact_provenance"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_canon_or_constraint_rotation_changes_provenance",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_rotation_visible"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_rotation_visible"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_envelope_roundtrip_preserves_hmmm",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_roundtrip"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_roundtrip"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_from_dict_rejects_scalar_field_coercion",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_type_strict"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_scalar_types_strict"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_from_dict_rejects_string_for_sequence_fields",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_type_strict"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_sequence_types_strict"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_tampered_provenance_digest_fails_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_tamper_rejected"
      },
      "file": "tests/test_envelope.py",
      "id": "check_envelope_tamper_rejected"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_envelope_contains_no_measurement_values",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_labels_not_measurements"
      },
      "file": "tests/test_envelope.py",
      "id": "check_labels_not_measurements"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_unknown_schema_field_fails_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_envelope_unknown_field_rejected"
      },
      "file": "tests/test_envelope.py",
      "id": "check_unknown_envelope_field_rejected"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_committed_msdmd_is_current",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_msdmd_generated"
      },
      "file": "tests/test_msdmd_generation.py",
      "id": "check_msdmd_generated_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_collection_excludes_vendored_skills",
        "cleanup": "tempdir_teardown",
        "mutates": "tempdir",
        "proves": "metapat_msdmd_scope_bounded"
      },
      "file": "tests/test_msdmd_generation.py",
      "id": "check_msdmd_scope_bounded"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_base_import_does_not_require_ucns",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_base_import_without_ucns"
      },
      "file": "tests/test_packaging.py",
      "id": "check_base_import_without_ucns"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_public_surface_contains_no_local_ucns_object_class",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_no_public_local_ucns"
      },
      "file": "tests/test_packaging.py",
      "id": "check_no_public_local_ucns"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_public_version_matches_distribution_metadata",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_package_version_matches_metadata"
      },
      "file": "tests/test_packaging.py",
      "id": "check_package_version_matches_metadata"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_electromagnetic_pipe_fixture_is_packaged_and_exact",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_pipe_fixture_packaged"
      },
      "file": "tests/test_packaging.py",
      "id": "check_pipe_fixture_packaged"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_root_spine_fixture_is_packaged_and_exact",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_root_fixture_packaged"
      },
      "file": "tests/test_packaging.py",
      "id": "check_root_fixture_packaged"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_typed_marker_is_packaged",
        "cleanup": "none",
        "mutates": "filesystem_read",
        "proves": "metapat_package_typed_marker"
      },
      "file": "tests/test_packaging.py",
      "id": "check_typed_marker_packaged"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quantum_application_bindings_match_catalog",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_application_catalog_bound"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_application_catalog_bound"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quantum_application_preserves_physics_firewall",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_application_physics_firewall"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_application_physics_firewall"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quantum_application_preserves_scale_distinctions",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_application_scales_distinct"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_application_scales_distinct"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quantum_application_source_is_current",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_application_source_current"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_application_source_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quantum_application_status_and_exclusions",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_application_status_preserved"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_application_status_preserved"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_packaged_quantum_fixture_is_current",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_fixture_current"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_fixture_current"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_quantum_fixture_render_is_deterministic",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_quantum_fixture_generated"
      },
      "file": "tests/test_quantum_magnetism.py",
      "id": "check_quantum_fixture_generated"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_relation_contains_no_status_transfer_surface",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_relation_no_status_transfer"
      },
      "file": "tests/test_relations.py",
      "id": "check_relation_no_status_transfer"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_relation_roundtrip_and_types_are_strict",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_relation_roundtrip_strict"
      },
      "file": "tests/test_relations.py",
      "id": "check_relation_roundtrip_strict"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_relation_tamper_is_rejected",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_relation_tamper_rejected"
      },
      "file": "tests/test_relations.py",
      "id": "check_relation_tamper_rejected"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_relation_vocabularies_are_bounded",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_relation_vocabulary_bounded"
      },
      "file": "tests/test_relations.py",
      "id": "check_relation_vocabulary_bounded"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_base_metapat_remains_available",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_ucns_ordered_occurrence_provenance"
      },
      "file": "tests/test_ucns_bridge.py",
      "id": "check_metapat_base_survives_ucns_profile"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_record_round_trip_and_legacy_boundaries",
        "cleanup": "monkeypatch_restore",
        "mutates": "process_import_state",
        "proves": "metapat_ucns_archived_operations_rejected"
      },
      "file": "tests/test_ucns_bridge.py",
      "id": "check_metapat_ucns_archived_operations"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_missing_or_legacy_package_stays_inactive",
        "cleanup": "monkeypatch_restore",
        "mutates": "process_import_state",
        "proves": "metapat_ucns_exact_identity_or_inactive"
      },
      "file": "tests/test_ucns_bridge.py",
      "id": "check_metapat_ucns_exact_identity"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_exact_profile_activates_and_preserves_order",
        "cleanup": "monkeypatch_restore",
        "mutates": "process_import_state",
        "proves": "metapat_ucns_ordered_occurrence_provenance, metapat_ucns_no_authority_transfer"
      },
      "file": "tests/test_ucns_bridge.py",
      "id": "check_metapat_ucns_order_and_no_transfer"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_validation_fails_on_child_order_and_rejects_parent_or_canon_tamper",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_authorization_binds_canon_and_order"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_canon_order_binding"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_default_policy_keeps_external_provenance_and_requires_authorization",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_default_external_provenance"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_default_external_provenance"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_authorization_binds_parent_children_canon_policy_and_sources",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_fork_requires_explicit_authorization"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_explicit_authorization"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_prohibited_relation_kinds_fail_closed",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_negative_relations_rejected"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_negative_relations"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_policy_and_authorization_never_transfer_status",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_no_status_transfer"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_no_status_transfer"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_only_constitutive_simultaneous_relation_is_accepted",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_constitutive_relation_only"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_relation_exact"
    },
    {
      "block": "CHECKS",
      "fields": {
        "call": "self::test_authorization_roundtrip_is_strict_and_tamper_evident",
        "cleanup": "none",
        "mutates": "none",
        "proves": "metapat_phi_record_roundtrip"
      },
      "file": "tests/test_ucns_phi.py",
      "id": "check_phi_roundtrip"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "orphan contracts, phantom proves targets, unresolvable calls, or undeclared executable tests are planted",
        "then": "the audit reports each gap and exits nonzero"
      },
      "file": "tools/check_contract_graph.py",
      "id": "metapat_contract_audit_detects_gaps"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "current METAPAT source promises and test evidence are audited without imports",
        "then": "every contract has a proving check, every check targets known contracts, every self call resolves, and every top-level test has a declaration"
      },
      "file": "tools/check_contract_graph.py",
      "id": "metapat_contract_graph_closes"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_load_parser, _top_level_test_functions, _split_csv, _audit",
        "module_kind": "instrument",
        "module_name": "tools.check_contract_graph",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "audit_repository, main",
        "requires": "repo-local skill-lib msdmd parser",
        "rollback": "remove the gate only with an explicit replacement audit",
        "rollout": "CI compliance gate",
        "since": "2026-07-12",
        "storage_boundary": "read",
        "summary": "reconciles source-owned CONTRACTS against test-owned CHECKS without importing product or test modules",
        "tests": "tests.test_contract_audit",
        "unresolved": "block type for harness-only checks remains hmmm in skill-lib doctrine",
        "user_data_boundary": "none"
      },
      "file": "tools/check_contract_graph.py",
      "id": "metapat_contract_graph_audit"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the generator runs in check mode against the packaged electromagnetic-pipe fixture",
        "then": "stale or missing fixture bytes fail visibly and current bytes pass"
      },
      "file": "tools/generate_application_fixtures.py",
      "id": "metapat_pipe_fixture_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the electromagnetic-pipe design constructor runs",
        "then": "the rendered fixture is deterministic JSON with one trailing newline"
      },
      "file": "tools/generate_application_fixtures.py",
      "id": "metapat_pipe_fixture_generated"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the generator runs in check mode against the packaged quantum-magnetism fixture",
        "then": "stale or missing fixture bytes fail visibly and current bytes pass"
      },
      "file": "tools/generate_application_fixtures.py",
      "id": "metapat_quantum_fixture_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the quantum-magnetism application constructor runs",
        "then": "the rendered fixture is deterministic JSON with one trailing newline"
      },
      "file": "tools/generate_application_fixtures.py",
      "id": "metapat_quantum_fixture_generated"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "FIXTURES",
        "module_kind": "instrument",
        "module_name": "tools.generate_application_fixtures",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "render_quantum_magnetism_fixture, render_electromagnetic_pipe_fixture, write_fixtures, main",
        "requires": "metapat_quantum_magnetism_application, metapat_electromagnetic_pipe_application",
        "rollback": "restore prior generated fixtures only with constructor and digest evidence attached",
        "rollout": "CI compliance gate and explicit regeneration command",
        "since": "2026-07-21",
        "storage_boundary": "read, optional generated-file write",
        "summary": "generates or verifies deterministic packaged application and engineering-design fixtures from canonical constructors",
        "tests": "tests.test_quantum_magnetism, tests.test_electromagnetic_pipe",
        "unresolved": "future application fixtures require separate constructors and evidence classification",
        "user_data_boundary": "none"
      },
      "file": "tools/generate_application_fixtures.py",
      "id": "metapat_application_fixture_generator"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the generator runs in check mode against the packaged fixture",
        "then": "stale or missing fixture bytes fail visibly and current bytes pass"
      },
      "file": "tools/generate_catalog.py",
      "id": "metapat_catalog_fixture_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the canonical semantic catalog constructor runs",
        "then": "the rendered fixture is deterministic JSON with one trailing newline"
      },
      "file": "tools/generate_catalog.py",
      "id": "metapat_catalog_fixture_generated"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the generator runs in check mode against the packaged root-spine envelope fixture",
        "then": "stale or missing fixture bytes fail visibly and current bytes pass"
      },
      "file": "tools/generate_catalog.py",
      "id": "metapat_root_envelope_fixture_current"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the canonical root-spine envelope constructor runs",
        "then": "the rendered fixture is deterministic JSON with one trailing newline"
      },
      "file": "tools/generate_catalog.py",
      "id": "metapat_root_envelope_fixture_generated"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "FIXTURES",
        "module_kind": "instrument",
        "module_name": "tools.generate_catalog",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "render_root_spine_envelope, render_catalog, write_semantic_fixtures, write_catalog, main",
        "requires": "metapat_semantic_catalog",
        "rollback": "restore prior generated fixture only with constructor and digest evidence attached",
        "rollout": "CI compliance gate and explicit regeneration command",
        "since": "2026-07-21",
        "storage_boundary": "read, optional generated-file write",
        "summary": "generates or verifies byte-current root-spine-envelope-v2 and semantic-module-catalog-v2 fixtures from their live constructors",
        "tests": "tests.test_catalog",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "tools/generate_catalog.py",
      "id": "metapat_catalog_generator"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "evidence",
        "given": "the pinned collector runs over the bounded METAPAT product surfaces",
        "then": "its rendered output is byte-for-byte identical to committed metapat_msdmd.ts"
      },
      "file": "tools/generate_msdmd.py",
      "id": "metapat_msdmd_generated"
    },
    {
      "block": "CONTRACTS",
      "fields": {
        "class": "safety",
        "given": "the collection is generated",
        "then": "product metadata from src, tests, and tools is included while vendored .agents skill metadata is excluded"
      },
      "file": "tools/generate_msdmd.py",
      "id": "metapat_msdmd_scope_bounded"
    },
    {
      "block": "MODULE_BUILD",
      "fields": {
        "admin_only": "false",
        "auth_boundary": "none",
        "internal_surface": "_load_collector, _stage_inputs",
        "module_kind": "instrument",
        "module_name": "tools.generate_msdmd",
        "network_boundary": "none",
        "owner": "The Interdependency",
        "public_surface": "render_collection, write_collection, main",
        "requires": "repo-local skill-lib msdmd collector",
        "rollback": "restore prior generated file only with the generator output attached",
        "rollout": "CI compliance gate and explicit regeneration command",
        "since": "2026-07-12",
        "storage_boundary": "read, optional generated-file write",
        "summary": "invokes the pinned skill-lib collector over METAPAT source, tests, and repository tools while excluding vendored skill declarations",
        "tests": "tests.test_msdmd_generation",
        "unresolved": "none",
        "user_data_boundary": "none"
      },
      "file": "tools/generate_msdmd.py",
      "id": "metapat_msdmd_generator"
    }
  ],
  "edges": [
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "metapat.canonical_semantic_catalog"
    },
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "metapat.catalog_digest"
    },
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "metapat.semantic_module_by_id"
    },
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "auth:none"
    },
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "network:none"
    },
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_addressable_semantic_catalog",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_addressable_semantic_catalog",
      "to": "user_data:canon text only"
    },
    {
      "from": "metapat_affixiation_harmonics_semantics",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_affixiation_harmonics_semantics",
      "to": "metapat.affixiation_harmonics.affixiation_harmonics_application_module"
    },
    {
      "from": "metapat_affixiation_harmonics_semantics",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_affixiation_harmonics_semantics",
      "to": "auth:none"
    },
    {
      "from": "metapat_affixiation_harmonics_semantics",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_affixiation_harmonics_semantics",
      "to": "network:none"
    },
    {
      "from": "metapat_affixiation_harmonics_semantics",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_affixiation_harmonics_semantics",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_affixiation_harmonics_semantics",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_affixiation_harmonics_semantics",
      "to": "user_data:public conceptual text only"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "metapat.canon.assert_canon_files_match"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "metapat.canon.canon_digest"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "metapat.canon.definitions"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "auth:none"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "network:none"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "storage:read-only"
    },
    {
      "from": "metapat_canon_constants",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_constants",
      "to": "user_data:none"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "metapat.validation.boundary_earns_its_keep"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "metapat.validation.consciousness_is_optional"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "metapat.validation.observer_role_by_registration"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "metapat.validation.registration_is_not_time"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "metapat.validation.tensor_precedes_time"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "auth:none"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "network:none"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "storage:none"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_canon_contract_checks",
      "to": "user_data:none"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "metapat.ApplicationCatalogBinding"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "metapat.MetapatApplicationModule"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "metapat.validate_application_against_catalog"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "auth:none"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "network:none"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_catalog_bound_application_modules",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_catalog_bound_application_modules",
      "to": "user_data:application text only"
    },
    {
      "from": "metapat_constitutive_fork_authority",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_constitutive_fork_authority",
      "to": "metapat.authorize_constitutive_fork"
    },
    {
      "from": "metapat_constitutive_fork_authority",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_constitutive_fork_authority",
      "to": "auth:none"
    },
    {
      "from": "metapat_constitutive_fork_authority",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_constitutive_fork_authority",
      "to": "network:none"
    },
    {
      "from": "metapat_constitutive_fork_authority",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_constitutive_fork_authority",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_constitutive_fork_authority",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_constitutive_fork_authority",
      "to": "user_data:semantic provenance only"
    },
    {
      "from": "metapat_electromagnetic_pipe_fixture",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_electromagnetic_pipe_fixture",
      "to": "metapat.electromagnetic_pipe_design"
    },
    {
      "from": "metapat_electromagnetic_pipe_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_electromagnetic_pipe_fixture",
      "to": "auth:none"
    },
    {
      "from": "metapat_electromagnetic_pipe_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_electromagnetic_pipe_fixture",
      "to": "network:none"
    },
    {
      "from": "metapat_electromagnetic_pipe_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_electromagnetic_pipe_fixture",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_electromagnetic_pipe_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_electromagnetic_pipe_fixture",
      "to": "user_data:public engineering handoff only"
    },
    {
      "from": "metapat_flow_status",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "metapat.flow_plan.AUTHORITY_FLOW"
    },
    {
      "from": "metapat_flow_status",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "metapat.flow_plan.PROOF_STATUS_FLOW"
    },
    {
      "from": "metapat_flow_status",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "metapat.flow_plan.RUNTIME_DATA_FLOW"
    },
    {
      "from": "metapat_flow_status",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "auth:none"
    },
    {
      "from": "metapat_flow_status",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "network:none"
    },
    {
      "from": "metapat_flow_status",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "storage:none"
    },
    {
      "from": "metapat_flow_status",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_flow_status",
      "to": "user_data:none"
    },
    {
      "from": "metapat_quantum_magnetism_fixture",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_quantum_magnetism_fixture",
      "to": "metapat.quantum_magnetism_application_module"
    },
    {
      "from": "metapat_quantum_magnetism_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_quantum_magnetism_fixture",
      "to": "auth:none"
    },
    {
      "from": "metapat_quantum_magnetism_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_quantum_magnetism_fixture",
      "to": "network:none"
    },
    {
      "from": "metapat_quantum_magnetism_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_quantum_magnetism_fixture",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_quantum_magnetism_fixture",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_quantum_magnetism_fixture",
      "to": "user_data:public application text only"
    },
    {
      "from": "metapat_semantic_envelope",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_envelope",
      "to": "metapat.envelope.MetapatModuleEnvelope"
    },
    {
      "from": "metapat_semantic_envelope",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_envelope",
      "to": "metapat.envelope.root_spine_module_envelope"
    },
    {
      "from": "metapat_semantic_envelope",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_envelope",
      "to": "auth:none"
    },
    {
      "from": "metapat_semantic_envelope",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_envelope",
      "to": "network:none"
    },
    {
      "from": "metapat_semantic_envelope",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_envelope",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_semantic_envelope",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_envelope",
      "to": "user_data:caller-supplied exact text"
    },
    {
      "from": "metapat_semantic_relation_records",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_relation_records",
      "to": "metapat.MetapatModuleRelation"
    },
    {
      "from": "metapat_semantic_relation_records",
      "kind": "exposes",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_relation_records",
      "to": "metapat.build_relation"
    },
    {
      "from": "metapat_semantic_relation_records",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_relation_records",
      "to": "auth:none"
    },
    {
      "from": "metapat_semantic_relation_records",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_relation_records",
      "to": "network:none"
    },
    {
      "from": "metapat_semantic_relation_records",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_relation_records",
      "to": "storage:serialization-only"
    },
    {
      "from": "metapat_semantic_relation_records",
      "kind": "risk",
      "source_block": "CAPABILITIES",
      "source_id": "metapat_semantic_relation_records",
      "to": "user_data:canon text only"
    },
    {
      "from": "check_affixiation_harmonics_authority_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_authority_firewall",
      "to": "self::test_authority_firewall_is_explicit"
    },
    {
      "from": "check_affixiation_harmonics_authority_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_authority_firewall",
      "to": "metapat_affixiation_harmonics_authority_firewall"
    },
    {
      "from": "check_affixiation_harmonics_candidate_status",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_candidate_status",
      "to": "self::test_application_remains_unpromoted"
    },
    {
      "from": "check_affixiation_harmonics_candidate_status",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_candidate_status",
      "to": "metapat_affixiation_harmonics_candidate_status"
    },
    {
      "from": "check_affixiation_harmonics_catalog_bound",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_catalog_bound",
      "to": "self::test_application_bindings_match_catalog"
    },
    {
      "from": "check_affixiation_harmonics_catalog_bound",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_catalog_bound",
      "to": "metapat_affixiation_harmonics_catalog_bound"
    },
    {
      "from": "check_affixiation_harmonics_source_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_source_current",
      "to": "self::test_application_source_is_current"
    },
    {
      "from": "check_affixiation_harmonics_source_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_harmonics_source_current",
      "to": "metapat_affixiation_harmonics_source_current"
    },
    {
      "from": "check_affixiation_identity_preserved",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_identity_preserved",
      "to": "self::test_affixiation_preserves_identity_without_selecting_topology"
    },
    {
      "from": "check_affixiation_identity_preserved",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_affixiation_identity_preserved",
      "to": "metapat_affixiation_identity_preserved"
    },
    {
      "from": "check_application_binding_exact",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_application_binding_exact",
      "to": "self::test_application_binding_is_exact_and_digest_bound"
    },
    {
      "from": "check_application_binding_exact",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_application_binding_exact",
      "to": "metapat_application_binding_exact"
    },
    {
      "from": "check_application_catalog_validation",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_application_catalog_validation",
      "to": "self::test_application_validates_against_exact_catalog"
    },
    {
      "from": "check_application_catalog_validation",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_application_catalog_validation",
      "to": "metapat_application_catalog_validation"
    },
    {
      "from": "check_application_roundtrip_strict",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_application_roundtrip_strict",
      "to": "self::test_application_roundtrip_and_types_are_strict"
    },
    {
      "from": "check_application_roundtrip_strict",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_application_roundtrip_strict",
      "to": "metapat_application_roundtrip_strict"
    },
    {
      "from": "check_application_source_exact",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_application_source_exact",
      "to": "self::test_application_source_statements_match"
    },
    {
      "from": "check_application_source_exact",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_application_source_exact",
      "to": "metapat_application_source_exact"
    },
    {
      "from": "check_application_status_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_application_status_firewall",
      "to": "self::test_application_status_firewall_is_explicit"
    },
    {
      "from": "check_application_status_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_application_status_firewall",
      "to": "metapat_application_status_firewall"
    },
    {
      "from": "check_application_tamper_rejected",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_application_tamper_rejected",
      "to": "self::test_application_and_binding_tamper_are_rejected"
    },
    {
      "from": "check_application_tamper_rejected",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_application_tamper_rejected",
      "to": "metapat_application_tamper_rejected"
    },
    {
      "from": "check_base_import_without_ucns",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_base_import_without_ucns",
      "to": "self::test_base_import_does_not_require_ucns"
    },
    {
      "from": "check_base_import_without_ucns",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_base_import_without_ucns",
      "to": "metapat_base_import_without_ucns"
    },
    {
      "from": "check_boundary_change_changes_outcome",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_boundary_change_changes_outcome",
      "to": "self::test_boundary_change_changes_outcome"
    },
    {
      "from": "check_boundary_change_changes_outcome",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_boundary_change_changes_outcome",
      "to": "boundary_change_changes_outcome"
    },
    {
      "from": "check_canon_digest_deterministic",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_canon_digest_deterministic",
      "to": "self::test_canon_digest_is_deterministic"
    },
    {
      "from": "check_canon_digest_deterministic",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_canon_digest_deterministic",
      "to": "metapat_canon_digest_deterministic"
    },
    {
      "from": "check_canon_file_drift_visible",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_canon_file_drift_visible",
      "to": "self::test_canon_file_drift_is_reported"
    },
    {
      "from": "check_canon_file_drift_visible",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_canon_file_drift_visible",
      "to": "metapat_canon_file_drift_visible"
    },
    {
      "from": "check_canon_manifest_complete",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_canon_manifest_complete",
      "to": "self::test_manifest_names_all_canon_files"
    },
    {
      "from": "check_canon_manifest_complete",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_canon_manifest_complete",
      "to": "metapat_canon_manifest_complete"
    },
    {
      "from": "check_catalog_claim_status_bounded",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_claim_status_bounded",
      "to": "self::test_catalog_claim_statuses_remain_bounded"
    },
    {
      "from": "check_catalog_claim_status_bounded",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_claim_status_bounded",
      "to": "metapat_catalog_claim_status_bounded"
    },
    {
      "from": "check_catalog_complete_ordered",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_complete_ordered",
      "to": "self::test_catalog_is_complete_and_ordered"
    },
    {
      "from": "check_catalog_complete_ordered",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_complete_ordered",
      "to": "metapat_catalog_complete_ordered"
    },
    {
      "from": "check_catalog_fixture_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_fixture_current",
      "to": "self::test_packaged_catalog_fixture_is_current"
    },
    {
      "from": "check_catalog_fixture_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_fixture_current",
      "to": "metapat_catalog_fixture_current"
    },
    {
      "from": "check_catalog_fixture_generated",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_fixture_generated",
      "to": "self::test_catalog_fixture_render_is_deterministic"
    },
    {
      "from": "check_catalog_fixture_generated",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_fixture_generated",
      "to": "metapat_catalog_fixture_generated"
    },
    {
      "from": "check_catalog_identity_unique",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_identity_unique",
      "to": "self::test_catalog_module_identity_is_unique"
    },
    {
      "from": "check_catalog_identity_unique",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_identity_unique",
      "to": "metapat_catalog_module_identity_unique"
    },
    {
      "from": "check_catalog_no_constitutive_inference",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_no_constitutive_inference",
      "to": "self::test_catalog_rejects_unauthorized_constitutive_relation"
    },
    {
      "from": "check_catalog_no_constitutive_inference",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_no_constitutive_inference",
      "to": "metapat_catalog_no_constitutive_inference"
    },
    {
      "from": "check_catalog_relations_declared",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_relations_declared",
      "to": "self::test_catalog_relations_are_declared_and_resolvable"
    },
    {
      "from": "check_catalog_relations_declared",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_relations_declared",
      "to": "metapat_catalog_relations_declared"
    },
    {
      "from": "check_catalog_rotation_visible",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_rotation_visible",
      "to": "self::test_catalog_rotation_changes_identity"
    },
    {
      "from": "check_catalog_rotation_visible",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_rotation_visible",
      "to": "metapat_catalog_rotation_visible"
    },
    {
      "from": "check_catalog_roundtrip_strict",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_roundtrip_strict",
      "to": "self::test_catalog_roundtrip_is_strict"
    },
    {
      "from": "check_catalog_roundtrip_strict",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_roundtrip_strict",
      "to": "metapat_catalog_roundtrip_strict"
    },
    {
      "from": "check_catalog_sources_exact",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_catalog_sources_exact",
      "to": "self::test_catalog_sources_match_repository"
    },
    {
      "from": "check_catalog_sources_exact",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_catalog_sources_exact",
      "to": "metapat_catalog_sources_exact"
    },
    {
      "from": "check_consciousness_optional",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_consciousness_optional",
      "to": "self::test_consciousness_is_optional"
    },
    {
      "from": "check_consciousness_optional",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_consciousness_optional",
      "to": "consciousness_optional_observer_mode"
    },
    {
      "from": "check_contract_audit_negative_gaps",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_negative_gaps",
      "to": "self::test_audit_reports_required_negative_gaps"
    },
    {
      "from": "check_contract_audit_negative_gaps",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_contract_audit_negative_gaps",
      "to": "metapat_contract_audit_detects_gaps"
    },
    {
      "from": "check_envelope_canonical_json",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_canonical_json",
      "to": "self::test_serialized_envelope_is_canonical_json"
    },
    {
      "from": "check_envelope_canonical_json",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_canonical_json",
      "to": "metapat_envelope_canonical_json"
    },
    {
      "from": "check_envelope_exact_provenance",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_exact_provenance",
      "to": "self::test_root_spine_envelope_preserves_exact_sources_and_constraints"
    },
    {
      "from": "check_envelope_exact_provenance",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_exact_provenance",
      "to": "metapat_envelope_exact_provenance"
    },
    {
      "from": "check_envelope_rotation_visible",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_rotation_visible",
      "to": "self::test_canon_or_constraint_rotation_changes_provenance"
    },
    {
      "from": "check_envelope_rotation_visible",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_rotation_visible",
      "to": "metapat_envelope_rotation_visible"
    },
    {
      "from": "check_envelope_roundtrip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_roundtrip",
      "to": "self::test_envelope_roundtrip_preserves_hmmm"
    },
    {
      "from": "check_envelope_roundtrip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_roundtrip",
      "to": "metapat_envelope_roundtrip"
    },
    {
      "from": "check_envelope_scalar_types_strict",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_scalar_types_strict",
      "to": "self::test_from_dict_rejects_scalar_field_coercion"
    },
    {
      "from": "check_envelope_scalar_types_strict",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_scalar_types_strict",
      "to": "metapat_envelope_type_strict"
    },
    {
      "from": "check_envelope_sequence_types_strict",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_sequence_types_strict",
      "to": "self::test_from_dict_rejects_string_for_sequence_fields"
    },
    {
      "from": "check_envelope_sequence_types_strict",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_sequence_types_strict",
      "to": "metapat_envelope_type_strict"
    },
    {
      "from": "check_envelope_tamper_rejected",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_envelope_tamper_rejected",
      "to": "self::test_tampered_provenance_digest_fails_closed"
    },
    {
      "from": "check_envelope_tamper_rejected",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_envelope_tamper_rejected",
      "to": "metapat_envelope_tamper_rejected"
    },
    {
      "from": "check_harmonics_time_agnostic",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_harmonics_time_agnostic",
      "to": "self::test_harmonic_semantics_do_not_require_time"
    },
    {
      "from": "check_harmonics_time_agnostic",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_harmonics_time_agnostic",
      "to": "metapat_harmonics_time_agnostic"
    },
    {
      "from": "check_labels_not_measurements",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_labels_not_measurements",
      "to": "self::test_envelope_contains_no_measurement_values"
    },
    {
      "from": "check_labels_not_measurements",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_labels_not_measurements",
      "to": "metapat_labels_not_measurements"
    },
    {
      "from": "check_metapat_base_survives_ucns_profile",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_metapat_base_survives_ucns_profile",
      "to": "self::test_base_metapat_remains_available"
    },
    {
      "from": "check_metapat_base_survives_ucns_profile",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_metapat_base_survives_ucns_profile",
      "to": "metapat_ucns_ordered_occurrence_provenance"
    },
    {
      "from": "check_metapat_ucns_archived_operations",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_archived_operations",
      "to": "self::test_record_round_trip_and_legacy_boundaries"
    },
    {
      "from": "check_metapat_ucns_archived_operations",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_archived_operations",
      "to": "metapat_ucns_archived_operations_rejected"
    },
    {
      "from": "check_metapat_ucns_exact_identity",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_exact_identity",
      "to": "self::test_missing_or_legacy_package_stays_inactive"
    },
    {
      "from": "check_metapat_ucns_exact_identity",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_exact_identity",
      "to": "metapat_ucns_exact_identity_or_inactive"
    },
    {
      "from": "check_metapat_ucns_order_and_no_transfer",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_order_and_no_transfer",
      "to": "self::test_exact_profile_activates_and_preserves_order"
    },
    {
      "from": "check_metapat_ucns_order_and_no_transfer",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_order_and_no_transfer",
      "to": "metapat_ucns_no_authority_transfer"
    },
    {
      "from": "check_metapat_ucns_order_and_no_transfer",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_metapat_ucns_order_and_no_transfer",
      "to": "metapat_ucns_ordered_occurrence_provenance"
    },
    {
      "from": "check_msdmd_generated_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_msdmd_generated_current",
      "to": "self::test_committed_msdmd_is_current"
    },
    {
      "from": "check_msdmd_generated_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_msdmd_generated_current",
      "to": "metapat_msdmd_generated"
    },
    {
      "from": "check_msdmd_scope_bounded",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_msdmd_scope_bounded",
      "to": "self::test_collection_excludes_vendored_skills"
    },
    {
      "from": "check_msdmd_scope_bounded",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_msdmd_scope_bounded",
      "to": "metapat_msdmd_scope_bounded"
    },
    {
      "from": "check_no_public_local_ucns",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_no_public_local_ucns",
      "to": "self::test_public_surface_contains_no_local_ucns_object_class"
    },
    {
      "from": "check_no_public_local_ucns",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_no_public_local_ucns",
      "to": "metapat_no_public_local_ucns"
    },
    {
      "from": "check_observer_role_registration",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_observer_role_registration",
      "to": "self::test_observer_role_by_registration"
    },
    {
      "from": "check_observer_role_registration",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_observer_role_registration",
      "to": "observer_role_requires_registration"
    },
    {
      "from": "check_package_version_matches_metadata",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_package_version_matches_metadata",
      "to": "self::test_public_version_matches_distribution_metadata"
    },
    {
      "from": "check_package_version_matches_metadata",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_package_version_matches_metadata",
      "to": "metapat_package_version_matches_metadata"
    },
    {
      "from": "check_phi_canon_order_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_canon_order_binding",
      "to": "self::test_validation_fails_on_child_order_and_rejects_parent_or_canon_tamper"
    },
    {
      "from": "check_phi_canon_order_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_canon_order_binding",
      "to": "metapat_phi_authorization_binds_canon_and_order"
    },
    {
      "from": "check_phi_default_external_provenance",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_default_external_provenance",
      "to": "self::test_default_policy_keeps_external_provenance_and_requires_authorization"
    },
    {
      "from": "check_phi_default_external_provenance",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_default_external_provenance",
      "to": "metapat_phi_default_external_provenance"
    },
    {
      "from": "check_phi_explicit_authorization",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_explicit_authorization",
      "to": "self::test_authorization_binds_parent_children_canon_policy_and_sources"
    },
    {
      "from": "check_phi_explicit_authorization",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_explicit_authorization",
      "to": "metapat_phi_fork_requires_explicit_authorization"
    },
    {
      "from": "check_phi_negative_relations",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_negative_relations",
      "to": "self::test_prohibited_relation_kinds_fail_closed"
    },
    {
      "from": "check_phi_negative_relations",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_negative_relations",
      "to": "metapat_phi_negative_relations_rejected"
    },
    {
      "from": "check_phi_no_status_transfer",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_no_status_transfer",
      "to": "self::test_policy_and_authorization_never_transfer_status"
    },
    {
      "from": "check_phi_no_status_transfer",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_no_status_transfer",
      "to": "metapat_phi_no_status_transfer"
    },
    {
      "from": "check_phi_relation_exact",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_relation_exact",
      "to": "self::test_only_constitutive_simultaneous_relation_is_accepted"
    },
    {
      "from": "check_phi_relation_exact",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_relation_exact",
      "to": "metapat_phi_constitutive_relation_only"
    },
    {
      "from": "check_phi_roundtrip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_phi_roundtrip",
      "to": "self::test_authorization_roundtrip_is_strict_and_tamper_evident"
    },
    {
      "from": "check_phi_roundtrip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_phi_roundtrip",
      "to": "metapat_phi_record_roundtrip"
    },
    {
      "from": "check_pipe_alloy_search",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_alloy_search",
      "to": "self::test_pipe_alloy_search_bounded"
    },
    {
      "from": "check_pipe_alloy_search",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_alloy_search",
      "to": "metapat_pipe_alloy_search_bounded"
    },
    {
      "from": "check_pipe_attractors_not_bearings",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_attractors_not_bearings",
      "to": "self::test_pipe_attractors_not_bearings"
    },
    {
      "from": "check_pipe_attractors_not_bearings",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_attractors_not_bearings",
      "to": "metapat_pipe_attractors_not_bearings"
    },
    {
      "from": "check_pipe_catalog_binding",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_catalog_binding",
      "to": "self::test_pipe_application_catalog_bound"
    },
    {
      "from": "check_pipe_catalog_binding",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_catalog_binding",
      "to": "metapat_pipe_application_catalog_bound"
    },
    {
      "from": "check_pipe_control_topology",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_control_topology",
      "to": "self::test_pipe_control_topology_exact"
    },
    {
      "from": "check_pipe_control_topology",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_control_topology",
      "to": "metapat_pipe_control_topology_exact"
    },
    {
      "from": "check_pipe_fixture_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_fixture_current",
      "to": "self::test_packaged_pipe_fixture_matches_live_constructor"
    },
    {
      "from": "check_pipe_fixture_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_fixture_current",
      "to": "metapat_pipe_fixture_current"
    },
    {
      "from": "check_pipe_fixture_packaged",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_fixture_packaged",
      "to": "self::test_electromagnetic_pipe_fixture_is_packaged_and_exact"
    },
    {
      "from": "check_pipe_fixture_packaged",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_fixture_packaged",
      "to": "metapat_pipe_fixture_packaged"
    },
    {
      "from": "check_pipe_fixture_rendered",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_fixture_rendered",
      "to": "self::test_pipe_fixture_renderer_is_deterministic"
    },
    {
      "from": "check_pipe_fixture_rendered",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_fixture_rendered",
      "to": "metapat_pipe_fixture_generated"
    },
    {
      "from": "check_pipe_performance_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_performance_firewall",
      "to": "self::test_pipe_performance_firewall"
    },
    {
      "from": "check_pipe_performance_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_performance_firewall",
      "to": "metapat_pipe_performance_firewall"
    },
    {
      "from": "check_pipe_roundtrip",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_roundtrip",
      "to": "self::test_pipe_roundtrip_strict"
    },
    {
      "from": "check_pipe_roundtrip",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_roundtrip",
      "to": "metapat_pipe_roundtrip_strict"
    },
    {
      "from": "check_pipe_source_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_source_current",
      "to": "self::test_pipe_source_current"
    },
    {
      "from": "check_pipe_source_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_source_current",
      "to": "metapat_pipe_source_current"
    },
    {
      "from": "check_pipe_winding_layers",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_pipe_winding_layers",
      "to": "self::test_pipe_winding_layers_exact"
    },
    {
      "from": "check_pipe_winding_layers",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_pipe_winding_layers",
      "to": "metapat_pipe_winding_layers_exact"
    },
    {
      "from": "check_quantum_application_catalog_bound",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_catalog_bound",
      "to": "self::test_quantum_application_bindings_match_catalog"
    },
    {
      "from": "check_quantum_application_catalog_bound",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_catalog_bound",
      "to": "metapat_quantum_application_catalog_bound"
    },
    {
      "from": "check_quantum_application_physics_firewall",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_physics_firewall",
      "to": "self::test_quantum_application_preserves_physics_firewall"
    },
    {
      "from": "check_quantum_application_physics_firewall",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_physics_firewall",
      "to": "metapat_quantum_application_physics_firewall"
    },
    {
      "from": "check_quantum_application_scales_distinct",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_scales_distinct",
      "to": "self::test_quantum_application_preserves_scale_distinctions"
    },
    {
      "from": "check_quantum_application_scales_distinct",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_scales_distinct",
      "to": "metapat_quantum_application_scales_distinct"
    },
    {
      "from": "check_quantum_application_source_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_source_current",
      "to": "self::test_quantum_application_source_is_current"
    },
    {
      "from": "check_quantum_application_source_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_source_current",
      "to": "metapat_quantum_application_source_current"
    },
    {
      "from": "check_quantum_application_status_preserved",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_status_preserved",
      "to": "self::test_quantum_application_status_and_exclusions"
    },
    {
      "from": "check_quantum_application_status_preserved",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_application_status_preserved",
      "to": "metapat_quantum_application_status_preserved"
    },
    {
      "from": "check_quantum_fixture_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_fixture_current",
      "to": "self::test_packaged_quantum_fixture_is_current"
    },
    {
      "from": "check_quantum_fixture_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_fixture_current",
      "to": "metapat_quantum_fixture_current"
    },
    {
      "from": "check_quantum_fixture_generated",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_quantum_fixture_generated",
      "to": "self::test_quantum_fixture_render_is_deterministic"
    },
    {
      "from": "check_quantum_fixture_generated",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_quantum_fixture_generated",
      "to": "metapat_quantum_fixture_generated"
    },
    {
      "from": "check_registration_not_time",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_registration_not_time",
      "to": "self::test_registration_is_not_time"
    },
    {
      "from": "check_registration_not_time",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_registration_not_time",
      "to": "registration_not_time"
    },
    {
      "from": "check_relation_no_status_transfer",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_relation_no_status_transfer",
      "to": "self::test_relation_contains_no_status_transfer_surface"
    },
    {
      "from": "check_relation_no_status_transfer",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_relation_no_status_transfer",
      "to": "metapat_relation_no_status_transfer"
    },
    {
      "from": "check_relation_roundtrip_strict",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_relation_roundtrip_strict",
      "to": "self::test_relation_roundtrip_and_types_are_strict"
    },
    {
      "from": "check_relation_roundtrip_strict",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_relation_roundtrip_strict",
      "to": "metapat_relation_roundtrip_strict"
    },
    {
      "from": "check_relation_tamper_rejected",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_relation_tamper_rejected",
      "to": "self::test_relation_tamper_is_rejected"
    },
    {
      "from": "check_relation_tamper_rejected",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_relation_tamper_rejected",
      "to": "metapat_relation_tamper_rejected"
    },
    {
      "from": "check_relation_vocabulary_bounded",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_relation_vocabulary_bounded",
      "to": "self::test_relation_vocabularies_are_bounded"
    },
    {
      "from": "check_relation_vocabulary_bounded",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_relation_vocabulary_bounded",
      "to": "metapat_relation_vocabulary_bounded"
    },
    {
      "from": "check_repository_canon_files_match",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_repository_canon_files_match",
      "to": "self::test_repository_canon_files_match_manifest"
    },
    {
      "from": "check_repository_canon_files_match",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_repository_canon_files_match",
      "to": "metapat_canon_files_match_repository"
    },
    {
      "from": "check_repository_contract_graph_closes",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_repository_contract_graph_closes",
      "to": "self::test_repository_contract_graph_closes"
    },
    {
      "from": "check_repository_contract_graph_closes",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_repository_contract_graph_closes",
      "to": "metapat_contract_graph_closes"
    },
    {
      "from": "check_root_envelope_fixture_current",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_envelope_fixture_current",
      "to": "self::test_packaged_root_spine_fixture_is_current"
    },
    {
      "from": "check_root_envelope_fixture_current",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_envelope_fixture_current",
      "to": "metapat_root_envelope_fixture_current"
    },
    {
      "from": "check_root_envelope_fixture_generated",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_envelope_fixture_generated",
      "to": "self::test_root_spine_fixture_render_is_deterministic"
    },
    {
      "from": "check_root_envelope_fixture_generated",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_envelope_fixture_generated",
      "to": "metapat_root_envelope_fixture_generated"
    },
    {
      "from": "check_root_fixture_packaged",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_fixture_packaged",
      "to": "self::test_root_spine_fixture_is_packaged_and_exact"
    },
    {
      "from": "check_root_fixture_packaged",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_fixture_packaged",
      "to": "metapat_root_fixture_packaged"
    },
    {
      "from": "check_root_spine_exact",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_root_spine_exact",
      "to": "self::test_root_spine_contains_current_axioms"
    },
    {
      "from": "check_root_spine_exact",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_root_spine_exact",
      "to": "metapat_root_spine_exact"
    },
    {
      "from": "check_tensor_precedes_time",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_tensor_precedes_time",
      "to": "self::test_tensor_precedes_time"
    },
    {
      "from": "check_tensor_precedes_time",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_tensor_precedes_time",
      "to": "tensor_before_time"
    },
    {
      "from": "check_time_registration_separated",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_time_registration_separated",
      "to": "self::test_time_and_registration_are_separated"
    },
    {
      "from": "check_time_registration_separated",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_time_registration_separated",
      "to": "metapat_time_not_registration"
    },
    {
      "from": "check_typed_marker_packaged",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_typed_marker_packaged",
      "to": "self::test_typed_marker_is_packaged"
    },
    {
      "from": "check_typed_marker_packaged",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_typed_marker_packaged",
      "to": "metapat_package_typed_marker"
    },
    {
      "from": "check_unknown_envelope_field_rejected",
      "kind": "calls",
      "source_block": "CHECKS",
      "source_id": "check_unknown_envelope_field_rejected",
      "to": "self::test_unknown_schema_field_fails_closed"
    },
    {
      "from": "check_unknown_envelope_field_rejected",
      "kind": "claims_proves",
      "source_block": "CHECKS",
      "source_id": "check_unknown_envelope_field_rejected",
      "to": "metapat_envelope_unknown_field_rejected"
    },
    {
      "from": "metapat_flow_edges",
      "kind": "owns",
      "source_block": "DEPENDENCIES",
      "source_id": "metapat_flow_edges",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_package_dependency_edges",
      "kind": "owns",
      "source_block": "DEPENDENCIES",
      "source_id": "metapat_package_dependency_edges",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_affixiation_harmonics_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_affixiation_harmonics_docs",
      "to": "affixiation_harmonics_application_module"
    },
    {
      "from": "metapat_affixiation_harmonics_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_affixiation_harmonics_docs",
      "to": "authority boundaries"
    },
    {
      "from": "metapat_affixiation_harmonics_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_affixiation_harmonics_docs",
      "to": "downstream evidence requirements"
    },
    {
      "from": "metapat_affixiation_harmonics_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_affixiation_harmonics_docs",
      "to": "semantic definitions"
    },
    {
      "from": "metapat_application_module_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_application_module_docs",
      "to": "ApplicationCatalogBinding"
    },
    {
      "from": "metapat_application_module_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_application_module_docs",
      "to": "MetapatApplicationModule"
    },
    {
      "from": "metapat_application_module_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_application_module_docs",
      "to": "catalog validation"
    },
    {
      "from": "metapat_application_module_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_application_module_docs",
      "to": "source checks"
    },
    {
      "from": "metapat_canon_contract_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_contract_docs",
      "to": "boundary_earns_its_keep"
    },
    {
      "from": "metapat_canon_contract_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_contract_docs",
      "to": "consciousness_is_optional"
    },
    {
      "from": "metapat_canon_contract_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_contract_docs",
      "to": "observer_role_by_registration"
    },
    {
      "from": "metapat_canon_contract_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_contract_docs",
      "to": "registration_is_not_time"
    },
    {
      "from": "metapat_canon_contract_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_contract_docs",
      "to": "tensor_precedes_time"
    },
    {
      "from": "metapat_canon_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_docs",
      "to": "canon file manifest"
    },
    {
      "from": "metapat_canon_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_docs",
      "to": "drift detection"
    },
    {
      "from": "metapat_canon_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_docs",
      "to": "exact constants"
    },
    {
      "from": "metapat_canon_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_canon_docs",
      "to": "identity schema"
    },
    {
      "from": "metapat_electromagnetic_pipe_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_electromagnetic_pipe_docs",
      "to": "catalog bindings"
    },
    {
      "from": "metapat_electromagnetic_pipe_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_electromagnetic_pipe_docs",
      "to": "electromagnetic_pipe_application_module"
    },
    {
      "from": "metapat_electromagnetic_pipe_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_electromagnetic_pipe_docs",
      "to": "electromagnetic_pipe_design"
    },
    {
      "from": "metapat_electromagnetic_pipe_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_electromagnetic_pipe_docs",
      "to": "engineering evidence boundary"
    },
    {
      "from": "metapat_electromagnetic_pipe_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_electromagnetic_pipe_docs",
      "to": "source integrity"
    },
    {
      "from": "metapat_module_envelope_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_module_envelope_docs",
      "to": "MetapatModuleEnvelope"
    },
    {
      "from": "metapat_module_envelope_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_module_envelope_docs",
      "to": "canon identity"
    },
    {
      "from": "metapat_module_envelope_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_module_envelope_docs",
      "to": "provenance digest"
    },
    {
      "from": "metapat_module_envelope_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_module_envelope_docs",
      "to": "strict schema validation"
    },
    {
      "from": "metapat_module_envelope_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_module_envelope_docs",
      "to": "unresolved hmmm preservation"
    },
    {
      "from": "metapat_quantum_magnetism_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_quantum_magnetism_docs",
      "to": "catalog bindings"
    },
    {
      "from": "metapat_quantum_magnetism_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_quantum_magnetism_docs",
      "to": "evidence boundary"
    },
    {
      "from": "metapat_quantum_magnetism_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_quantum_magnetism_docs",
      "to": "quantum_magnetism_application_module"
    },
    {
      "from": "metapat_quantum_magnetism_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_quantum_magnetism_docs",
      "to": "source integrity"
    },
    {
      "from": "metapat_semantic_catalog_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_catalog_docs",
      "to": "MetapatSemanticCatalog"
    },
    {
      "from": "metapat_semantic_catalog_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_catalog_docs",
      "to": "SemanticCatalogModule"
    },
    {
      "from": "metapat_semantic_catalog_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_catalog_docs",
      "to": "canonical_semantic_catalog"
    },
    {
      "from": "metapat_semantic_catalog_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_catalog_docs",
      "to": "catalog fixture"
    },
    {
      "from": "metapat_semantic_catalog_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_catalog_docs",
      "to": "source integrity"
    },
    {
      "from": "metapat_semantic_relations_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_relations_docs",
      "to": "CLAIM_STATUSES"
    },
    {
      "from": "metapat_semantic_relations_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_relations_docs",
      "to": "MetapatModuleRelation"
    },
    {
      "from": "metapat_semantic_relations_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_semantic_relations_docs",
      "to": "RELATION_KINDS"
    },
    {
      "from": "metapat_ucns_phi_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_ucns_phi_docs",
      "to": "UCNSForkAuthorization"
    },
    {
      "from": "metapat_ucns_phi_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_ucns_phi_docs",
      "to": "UCNSPhiPolicy"
    },
    {
      "from": "metapat_ucns_phi_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_ucns_phi_docs",
      "to": "authorize_constitutive_fork"
    },
    {
      "from": "metapat_ucns_phi_docs",
      "kind": "covers",
      "source_block": "DOCS",
      "source_id": "metapat_ucns_phi_docs",
      "to": "validate_fork_authorization"
    },
    {
      "from": "metapat_affixiation_harmonics_application",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_affixiation_harmonics_application",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_affixiation_harmonics_application",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_affixiation_harmonics_application",
      "to": "metapat_application_module_schema"
    },
    {
      "from": "metapat_affixiation_harmonics_application",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_affixiation_harmonics_application",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_application_fixture_generator",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_application_fixture_generator",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_application_fixture_generator",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_application_fixture_generator",
      "to": "metapat_electromagnetic_pipe_application"
    },
    {
      "from": "metapat_application_fixture_generator",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_application_fixture_generator",
      "to": "metapat_quantum_magnetism_application"
    },
    {
      "from": "metapat_application_module_schema",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_application_module_schema",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_application_module_schema",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_application_module_schema",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_application_module_schema",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_application_module_schema",
      "to": "metapat_semantic_relations"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_canon_contract_checks",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_canon_contract_checks",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_canon_contract_checks",
      "to": "none"
    },
    {
      "from": "metapat_canon_core",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_canon_core",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_canon_core",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_canon_core",
      "to": "none"
    },
    {
      "from": "metapat_catalog_generator",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_catalog_generator",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_catalog_generator",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_catalog_generator",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_contract_graph_audit",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_contract_graph_audit",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_contract_graph_audit",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_contract_graph_audit",
      "to": "repo-local skill-lib msdmd parser"
    },
    {
      "from": "metapat_electromagnetic_pipe_application",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_electromagnetic_pipe_application",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_electromagnetic_pipe_application",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_electromagnetic_pipe_application",
      "to": "metapat_application_module_schema"
    },
    {
      "from": "metapat_electromagnetic_pipe_application",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_electromagnetic_pipe_application",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_exact_ucns_profile_consumer",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_exact_ucns_profile_consumer",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_exact_ucns_profile_consumer",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_exact_ucns_profile_consumer",
      "to": "exact UCNS post-reset profile"
    },
    {
      "from": "metapat_exact_ucns_profile_consumer",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_exact_ucns_profile_consumer",
      "to": "metapat_module_envelope"
    },
    {
      "from": "metapat_flow_plan",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_flow_plan",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_flow_plan",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_flow_plan",
      "to": "metapat_module_envelope"
    },
    {
      "from": "metapat_flow_plan",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_flow_plan",
      "to": "metapat_ucns_adapter"
    },
    {
      "from": "metapat_module_envelope",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_module_envelope",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_module_envelope",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_module_envelope",
      "to": "metapat_canon_core"
    },
    {
      "from": "metapat_msdmd_generator",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_msdmd_generator",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_msdmd_generator",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_msdmd_generator",
      "to": "repo-local skill-lib msdmd collector"
    },
    {
      "from": "metapat_package_exports",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_application_module_schema"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_canon_contract_checks"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_canon_core"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_electromagnetic_pipe_application"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_module_envelope"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_quantum_magnetism_application"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_semantic_relations"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "metapat_ucns_phi_policy"
    },
    {
      "from": "metapat_package_exports",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_package_exports",
      "to": "optional metapat_ucns_adapter"
    },
    {
      "from": "metapat_quantum_magnetism_application",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_quantum_magnetism_application",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_quantum_magnetism_application",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_quantum_magnetism_application",
      "to": "metapat_application_module_schema"
    },
    {
      "from": "metapat_quantum_magnetism_application",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_quantum_magnetism_application",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_semantic_catalog",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_semantic_catalog",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog",
      "to": "metapat_canon_core"
    },
    {
      "from": "metapat_semantic_catalog",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog",
      "to": "metapat_module_envelope"
    },
    {
      "from": "metapat_semantic_catalog",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog",
      "to": "metapat_semantic_catalog_builder"
    },
    {
      "from": "metapat_semantic_catalog",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog",
      "to": "metapat_semantic_relations"
    },
    {
      "from": "metapat_semantic_catalog_builder",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_builder",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_semantic_catalog_builder",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_builder",
      "to": "metapat_semantic_catalog"
    },
    {
      "from": "metapat_semantic_catalog_builder",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_builder",
      "to": "metapat_semantic_catalog_declarations"
    },
    {
      "from": "metapat_semantic_catalog_builder",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_builder",
      "to": "metapat_semantic_relations"
    },
    {
      "from": "metapat_semantic_catalog_declarations",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_declarations",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_semantic_catalog_declarations",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_declarations",
      "to": "metapat_semantic_doctrine_declarations"
    },
    {
      "from": "metapat_semantic_catalog_declarations",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_catalog_declarations",
      "to": "metapat_semantic_theory_declarations"
    },
    {
      "from": "metapat_semantic_doctrine_declarations",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_doctrine_declarations",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_semantic_doctrine_declarations",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_doctrine_declarations",
      "to": "metapat_canon_core"
    },
    {
      "from": "metapat_semantic_relations",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_relations",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_semantic_relations",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_relations",
      "to": "metapat_module_envelope"
    },
    {
      "from": "metapat_semantic_theory_declarations",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_theory_declarations",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_semantic_theory_declarations",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_semantic_theory_declarations",
      "to": "metapat_canon_core"
    },
    {
      "from": "metapat_ucns_phi_policy",
      "kind": "owns",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_ucns_phi_policy",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_ucns_phi_policy",
      "kind": "requires",
      "source_block": "MODULE_BUILD",
      "source_id": "metapat_ucns_phi_policy",
      "to": "metapat_module_envelope"
    },
    {
      "from": "metapat_canon_owner",
      "kind": "owns",
      "source_block": "OWNERS",
      "source_id": "metapat_canon_owner",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_contract_owner",
      "kind": "owns",
      "source_block": "OWNERS",
      "source_id": "metapat_contract_owner",
      "to": "The Interdependency"
    },
    {
      "from": "metapat_flow_owner",
      "kind": "owns",
      "source_block": "OWNERS",
      "source_id": "metapat_flow_owner",
      "to": "The Interdependency"
    }
  ],
  "gaps": [],
  "repo": "metapat"
});
