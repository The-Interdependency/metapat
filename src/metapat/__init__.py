"""Public METAPAT canon, catalog, application, semantic-envelope, contract-check, and adapter exports."""

# === MODULE_BUILD ===
# id: metapat_package_exports
#   module_name: metapat
#   module_kind: schema
#   summary: re-exports byte-complete canon identity, addressable semantic catalog, strict catalog-bound application modules, immutable envelopes and relations, deterministic checks, explicit UCNS Phi authority, and the optional actual-UCNS adapter
#   owner: The Interdependency
#   public_surface: __version__, canon identity, semantic catalog and relations, MetapatModuleEnvelope, canon contract checks, UCNSPhiPolicy, UCNSForkAuthorization, actual-UCNS adapter
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: read-only canon verification and serialization only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_envelope, tests.test_catalog, tests.test_relations, tests.test_application, tests.test_quantum_magnetism, tests.test_canon_integrity, tests.test_ucns_phi, tests.test_ucns_bridge, tests.test_packaging
#   rollout: importable_package
#   rollback: remove catalog exports and fixture while preserving prior canon, envelope, Phi, and adapter surfaces
#   requires: metapat_canon_core, metapat_module_envelope, metapat_semantic_relations, metapat_semantic_catalog, metapat_application_module_schema, metapat_quantum_magnetism_application, metapat_canon_contract_checks, metapat_ucns_phi_policy, optional metapat_ucns_adapter
#   since: 2026-07-12
#   unresolved: downstream consumers must bind module and fork authorizations to exact application and UCNS topology identities
# === END MODULE_BUILD ===

# === DEPENDENCIES ===
# id: metapat_package_dependency_edges
#   summary: base exports depend on canon, semantic catalog, relation and envelope schemas, contract checks, flow declarations, Phi policy, and a lazy optional UCNS adapter
#   imports: metapat.canon, metapat.catalog, metapat.application, metapat.quantum_magnetism, metapat.relations, metapat.envelope, metapat.flow_plan, metapat.validation, metapat.ucns_phi, metapat.ucns
#   external_optional: ucns
#   provides: metapat_package_exports
#   class: runtime
#   owner: The Interdependency
# === END DEPENDENCIES ===

# === CONTRACTS ===
# id: metapat_package_version_matches_metadata
#   given: the installed package and distribution metadata are inspected
#   then: both expose the same authoritative version
#   class: packaging
#
# id: metapat_package_typed_marker
#   given: the installed package resources are inspected
#   then: the PEP 561 py.typed marker is present
#   class: packaging
#
# id: metapat_base_import_without_ucns
#   given: the base package is imported without invoking the optional adapter
#   then: canon, catalog, envelope, relation, and Phi policy surfaces work without requiring UCNS
#   class: packaging
#
# id: metapat_no_public_local_ucns
#   given: the public package surface is inspected
#   then: no local UCNSObject class is exported
#   class: boundary_contract
#
# id: metapat_root_fixture_packaged
#   given: the installed package resources are inspected
#   then: the canonical root-spine envelope fixture is packaged and matches the live constructor exactly
#   class: packaging
# === END CONTRACTS ===

__version__ = "0.5.0"

from .application import (
    APPLICATION_BINDING_SCHEMA_ID,
    APPLICATION_BINDING_SCHEMA_VERSION,
    APPLICATION_CLAIM_STATUSES,
    APPLICATION_SCHEMA_ID,
    APPLICATION_SCHEMA_VERSION,
    ApplicationCatalogBinding,
    MetapatApplicationModule,
    application_source_mismatches,
    assert_application_sources_match,
    bind_catalog_module,
    validate_application_against_catalog,
)
from .canon import (
    CANON_FILE_BLOBS,
    CANON_IDENTITY_SCHEMA_VERSION,
    CANON_VERSION,
    CanonIntegrityError,
    ENERGY_THEORY_QUESTION,
    PRIMITIVE_EXTENSION,
    ROOT_SPINE,
    TIME_DEFINITION,
    assert_canon_files_match,
    canon_digest,
    canon_file_mismatches,
    canon_manifest_digest,
    canonical_canon_data,
    canonical_canon_manifest_data,
    definitions,
    git_blob_sha1,
    observed_canon_file_blobs,
    primitive_extension,
    root_spine,
)
from .catalog import (
    CATALOG_SCHEMA_ID,
    CATALOG_SCHEMA_VERSION,
    CATALOG_VERSION,
    DOCTRINE_CLASSES,
    EXPECTED_MODULE_COUNT,
    EXPECTED_MODULE_COUNTS,
    MetapatSemanticCatalog,
    SemanticCatalogModule,
    assert_catalog_complete,
    assert_catalog_sources_match,
    canonical_semantic_catalog,
    catalog_digest,
    catalog_module_counts,
    catalog_source_mismatches,
    semantic_module_by_id,
)
from .envelope import (
    MODULE_ENVELOPE_SCHEMA_ID,
    MODULE_ENVELOPE_SCHEMA_VERSION,
    MODULE_KINDS,
    MetapatModuleEnvelope,
    build_module_envelope,
    root_spine_module_envelope,
)
from .flow_plan import (
    AUTHORITY_FLOW,
    EDCM_SIDE_STATUS,
    PROOF_STATUS_FLOW,
    RUNTIME_DATA_FLOW,
    UCNS_SIDE_STATUS,
)
from .quantum_magnetism import (
    QUANTUM_MAGNETISM_APPLICATION_VERSION,
    QUANTUM_MAGNETISM_BINDING_SPECS,
    quantum_magnetism_application_digest,
    quantum_magnetism_application_module,
)
from .relations import (
    CLAIM_STATUSES,
    RELATION_KINDS,
    RELATION_SCHEMA_ID,
    RELATION_SCHEMA_VERSION,
    MetapatModuleRelation,
    build_relation,
)
from .ucns_phi import (
    CONSTITUTIVE_RELATION_KIND,
    DEFAULT_UCNS_PHI_POLICY,
    FORK_AUTHORIZATION_SCHEMA_ID,
    FORK_AUTHORIZATION_SCHEMA_VERSION,
    PHI_POLICY_SCHEMA_ID,
    PHI_POLICY_VERSION,
    PROHIBITED_FORK_RELATION_KINDS,
    ForkAuthorizationError,
    UCNSForkAuthorization,
    UCNSPhiPolicy,
    authorize_constitutive_fork,
    validate_fork_authorization,
)
from .ucns import (
    ADDRESSABLE_GONOL_VERTICES,
    GONOL_VERTEX_COUNT,
    SPACE_ANCHOR_VERTEX,
    UCNS_ADAPTER_SCHEMA,
    UCNS_ADAPTER_VERSION,
    UCNSAdapterError,
    UCNSAdaptation,
    UCNSAdaptationRecord,
    UCNSDependencyError,
    adapt_envelope_to_ucns,
    compose,
    require_ucns,
    root_spine_adaptation,
    root_spine_ucns,
)
from .validation import (
    boundary_earns_its_keep,
    consciousness_is_optional,
    observer_role_by_registration,
    registration_is_not_time,
    tensor_precedes_time,
)

__all__ = [
    "__version__",
    "ADDRESSABLE_GONOL_VERTICES",
    "AUTHORITY_FLOW",
    "CANON_FILE_BLOBS",
    "CANON_IDENTITY_SCHEMA_VERSION",
    "CANON_VERSION",
    "CATALOG_SCHEMA_ID",
    "CATALOG_SCHEMA_VERSION",
    "CATALOG_VERSION",
    "CLAIM_STATUSES",
    "CONSTITUTIVE_RELATION_KIND",
    "CanonIntegrityError",
    "DEFAULT_UCNS_PHI_POLICY",
    "DOCTRINE_CLASSES",
    "EDCM_SIDE_STATUS",
    "ENERGY_THEORY_QUESTION",
    "EXPECTED_MODULE_COUNT",
    "EXPECTED_MODULE_COUNTS",
    "FORK_AUTHORIZATION_SCHEMA_ID",
    "FORK_AUTHORIZATION_SCHEMA_VERSION",
    "ForkAuthorizationError",
    "GONOL_VERTEX_COUNT",
    "MODULE_ENVELOPE_SCHEMA_ID",
    "MODULE_ENVELOPE_SCHEMA_VERSION",
    "MODULE_KINDS",
    "MetapatModuleEnvelope",
    "MetapatModuleRelation",
    "MetapatSemanticCatalog",
    "PHI_POLICY_SCHEMA_ID",
    "PHI_POLICY_VERSION",
    "PRIMITIVE_EXTENSION",
    "PROHIBITED_FORK_RELATION_KINDS",
    "PROOF_STATUS_FLOW",
    "RELATION_KINDS",
    "RELATION_SCHEMA_ID",
    "RELATION_SCHEMA_VERSION",
    "ROOT_SPINE",
    "RUNTIME_DATA_FLOW",
    "SPACE_ANCHOR_VERTEX",
    "SemanticCatalogModule",
    "TIME_DEFINITION",
    "UCNS_ADAPTER_SCHEMA",
    "UCNS_ADAPTER_VERSION",
    "UCNSAdapterError",
    "UCNSAdaptation",
    "UCNSAdaptationRecord",
    "UCNSDependencyError",
    "UCNSForkAuthorization",
    "UCNSPhiPolicy",
    "UCNS_SIDE_STATUS",
    "adapt_envelope_to_ucns",
    "assert_canon_files_match",
    "assert_catalog_complete",
    "assert_catalog_sources_match",
    "authorize_constitutive_fork",
    "boundary_earns_its_keep",
    "build_module_envelope",
    "build_relation",
    "canon_digest",
    "canon_file_mismatches",
    "canon_manifest_digest",
    "canonical_canon_data",
    "canonical_canon_manifest_data",
    "canonical_semantic_catalog",
    "catalog_digest",
    "catalog_module_counts",
    "catalog_source_mismatches",
    "compose",
    "consciousness_is_optional",
    "definitions",
    "git_blob_sha1",
    "observed_canon_file_blobs",
    "observer_role_by_registration",
    "primitive_extension",
    "registration_is_not_time",
    "require_ucns",
    "root_spine",
    "root_spine_adaptation",
    "root_spine_module_envelope",
    "root_spine_ucns",
    "semantic_module_by_id",
    "tensor_precedes_time",
    "validate_fork_authorization",
    "APPLICATION_BINDING_SCHEMA_ID",
    "APPLICATION_BINDING_SCHEMA_VERSION",
    "APPLICATION_CLAIM_STATUSES",
    "APPLICATION_SCHEMA_ID",
    "APPLICATION_SCHEMA_VERSION",
    "ApplicationCatalogBinding",
    "MetapatApplicationModule",
    "QUANTUM_MAGNETISM_APPLICATION_VERSION",
    "QUANTUM_MAGNETISM_BINDING_SPECS",
    "application_source_mismatches",
    "assert_application_sources_match",
    "bind_catalog_module",
    "quantum_magnetism_application_digest",
    "quantum_magnetism_application_module",
    "validate_application_against_catalog",
]
