"""Public METAPAT canon, semantic-envelope, contract-check, and adapter exports.

Base import is dependency-free. Actual UCNS is imported only when an adapter
function is called.
"""

# === MODULE_BUILD ===
# id: metapat_package_exports
#   module_name: metapat
#   module_kind: schema
#   summary: re-exports exact canon identity, immutable semantic envelopes, deterministic canon contract checks, and the optional actual-UCNS adapter
#   owner: The Interdependency
#   public_surface: __version__, canon constants and digest, MetapatModuleEnvelope, build_module_envelope, root_spine_module_envelope, canon contract checks, adapt_envelope_to_ucns, root_spine_adaptation
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_envelope, tests.test_ucns_bridge, tests.test_packaging
#   rollout: importable_package
#   rollback: remove package exports while preserving source modules
#   requires: metapat_canon_core, metapat_module_envelope, metapat_canon_contract_checks, optional metapat_ucns_adapter
#   since: 2026-07-12
#   unresolved: EDCM consumer merge and full shared-stack fixture
# === END MODULE_BUILD ===

# === DEPENDENCIES ===
# id: metapat_package_dependency_edges
#   summary: base exports depend on canon, envelope, contract checks, and a lazy optional UCNS adapter module
#   imports: metapat.canon, metapat.envelope, metapat.validation, metapat.ucns
#   external_optional: ucns
#   provides: metapat_package_exports
#   class: runtime
#   owner: The Interdependency
# === END DEPENDENCIES ===

__version__ = "0.1.0"

from .canon import (
    CANON_VERSION,
    ENERGY_THEORY_QUESTION,
    PRIMITIVE_EXTENSION,
    ROOT_SPINE,
    TIME_DEFINITION,
    canon_digest,
    canonical_canon_data,
    definitions,
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
    "CANON_VERSION",
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
    "UCNSAdapterError",
    "UCNSAdaptation",
    "UCNSAdaptationRecord",
    "UCNSDependencyError",
    "UCNS_SIDE_STATUS",
    "adapt_envelope_to_ucns",
    "boundary_earns_its_keep",
    "build_module_envelope",
    "canon_digest",
    "canonical_canon_data",
    "compose",
    "consciousness_is_optional",
    "definitions",
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
