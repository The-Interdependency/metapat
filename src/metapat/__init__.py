"""METAPAT public package exports."""

# === MODULE_BUILD ===
# id: metapat_package_exports
#   module_name: metapat
#   module_kind: schema
#   summary: re-exports the public METAPAT canon, validation, and UCNS bridge surfaces
#   owner: The Interdependency
#   public_surface: metapat
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_ucns_bridge
#   rollout: importable_package
#   rollback: remove package exports
# === END MODULE_BUILD ===

# === DEPENDENCIES ===
# id: metapat_package_dependency_edges
#   summary: package exports depend on canon, validation, and UCNS bridge modules
#   imports: metapat.canon, metapat.validation, metapat.ucns
#   provides: metapat_package_exports
#   class: runtime
#   owner: The Interdependency
# === END DEPENDENCIES ===

from .canon import (
    ENERGY_THEORY_QUESTION,
    PRIMITIVE_EXTENSION,
    ROOT_SPINE,
    TIME_DEFINITION,
    definitions,
    primitive_extension,
    root_spine,
)
from .ucns import (
    ADDRESSABLE_GONOL_VERTICES,
    GONOL_VERTEX_COUNT,
    SPACE_ANCHOR_VERTEX,
    UNIT,
    AnchorPayload,
    UCNSObject,
    chapter_zero_ucns,
    compose,
    energy_question_ucns,
    lcm,
    make_ucns_object,
    minimal_gonal_order,
    minimal_gonol_order,
    primitive_extension_ucns,
    root_spine_ucns,
    ucns_from_statements,
)
from .validation import (
    boundary_earns_its_keep,
    consciousness_is_optional,
    observer_role_by_registration,
    registration_is_not_time,
    tensor_precedes_time,
)

__all__ = [
    "ADDRESSABLE_GONOL_VERTICES",
    "AnchorPayload",
    "ENERGY_THEORY_QUESTION",
    "GONOL_VERTEX_COUNT",
    "PRIMITIVE_EXTENSION",
    "ROOT_SPINE",
    "SPACE_ANCHOR_VERTEX",
    "TIME_DEFINITION",
    "UCNSObject",
    "UNIT",
    "boundary_earns_its_keep",
    "chapter_zero_ucns",
    "compose",
    "consciousness_is_optional",
    "definitions",
    "energy_question_ucns",
    "lcm",
    "make_ucns_object",
    "minimal_gonal_order",
    "minimal_gonol_order",
    "observer_role_by_registration",
    "primitive_extension",
    "primitive_extension_ucns",
    "registration_is_not_time",
    "root_spine",
    "root_spine_ucns",
    "tensor_precedes_time",
    "ucns_from_statements",
]
