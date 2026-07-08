"""Planned METAPAT flow direction."""

# === MODULE_BUILD ===
# id: metapat_flow_plan
#   module_name: metapat.flow_plan
#   module_kind: adapter
#   summary: records UCNS to METAPAT to EDCM flow status, including the METAPAT-native UCNS bridge
#   owner: The Interdependency
#   public_surface: FLOW_DIRECTION, UCNS_SIDE_STATUS, EDCM_SIDE_STATUS
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_ucns_bridge
#   rollout: documentation_only
#   rollback: restore UCNS_SIDE_STATUS to planned
#   unresolved: exact external UCNS package adapter, exact EDCM module surface
# === END MODULE_BUILD ===

# === CAPABILITIES ===
# id: metapat_flow_status
#   summary: exposes current UCNS to METAPAT to EDCM flow status
#   exposes: metapat.flow_plan.FLOW_DIRECTION
#   inputs: none
#   outputs: str
#   boundaries: auth:none, storage:none, network:none, user_data:none
# === END CAPABILITIES ===

# === DEPENDENCIES ===
# id: metapat_planned_flow_edges
#   summary: METAPAT now has a local UCNS-shaped bridge and still plans external UCNS/EDCM adapters
#   internal: metapat.ucns
#   external: The-Interdependency/ucns, The-Interdependency/edcm
#   provides: metapat_flow_plan
#   class: architecture
#   direction: UCNS -> METAPAT -> EDCM
#   owner: The Interdependency
# === END DEPENDENCIES ===

# === OWNERS ===
# id: metapat_flow_owner
#   owner: The Interdependency
#   steward: Erin Spencer
#   review_required_for: dependency, public_api, canon
#   escalation: hmmm
# === END OWNERS ===

# === BOUNDARIES ===
# id: metapat_flow_boundaries
#   summary: flow status constants with no active external calls
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
# === END BOUNDARIES ===

FLOW_DIRECTION = "UCNS -> METAPAT -> EDCM"
UCNS_SIDE_STATUS = "implemented: METAPAT-native UCNS bridge; hmmm: external The-Interdependency/ucns adapter unresolved"
EDCM_SIDE_STATUS = "hmmm: planned, not implemented"
