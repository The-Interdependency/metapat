"""Public METAPAT canon, semantic-envelope, contract-check, and adapter exports."""

# === MODULE_BUILD ===
# id: metapat_package_exports
#   module_name: metapat
#   module_kind: schema
#   summary: re-exports byte-complete canon identity, strict immutable semantic envelopes, deterministic canon contract checks, and the optional lossless actual-UCNS adapter
#   owner: The Interdependency
#   public_surface: __version__, canon constants and file manifest, MetapatModuleEnvelope, build_module_envelope, root_spine_module_envelope, canon contract checks, adapt_envelope_to_ucns, root_spine_adaptation
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: read-only canon verification and serialization only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_envelope, tests.test_canon_integrity, tests.test_ucns_bridge, tests.test_packaging
#   rollout: importable_package
#   rollback: remove new exports while preserving source modules and canon files
#   requires: metapat_canon_core, metapat_module_envelope, metapat_canon_contract_checks, optional metapat_ucns_adapter
#   since: 2026-07-12
#   unresolved: downstream EDCM consumer merge and full shared-stack fixture
# === END MODULE_BUILD ===

# === DEPENDENCIES ===
# id: metapat_package_dependency_edges
#   summary: base exports depend on canon, envelope, contract checks, flow declarations, and a lazy optional UCNS adapter module
#   imports: metapat.canon, metapat.envelope, metapat.flow_plan, metapat.validation, metapat.ucns
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
#   then: canon and envelope surfaces work without requiring UCNS
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

__version__ = "0.3.0"

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
    "CanonIntegrityError",
    "EDCM_SIDE_STATUS",
    "ENERGY_THEORY_QUESTION",
    "GONOL_VERTEX_COUNT",
    "MODULE_ENVELOPE_SCHEMA_ID",
    "MODULE_ENVELOPE_SCHEMA_VERSION",
    "MODULE_KINDS",
    "MetapatModuleEnvelope",
    "PRIMITIVE_EXTENSION",
    "PROOF_STATUS_FLOW",
    "ROOT_SPINE",
    "RUNTIME_DATA_FLOW",
    "SPACE_ANCHOR_VERTEX",
    "TIME_DEFINITION",
    "UCNS_ADAPTER_SCHEMA",
    "UCNS_ADAPTER_VERSION",
    "UCNSAdapterError",
    "UCNSAdaptation",
    "UCNSAdaptationRecord",
    "UCNSDependencyError",
    "UCNS_SIDE_STATUS",
    "adapt_envelope_to_ucns",
    "assert_canon_files_match",
    "boundary_earns_its_keep",
    "build_module_envelope",
    "canon_digest",
    "canon_file_mismatches",
    "canon_manifest_digest",
    "canonical_canon_data",
    "canonical_canon_manifest_data",
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
    "tensor_precedes_time",
]
