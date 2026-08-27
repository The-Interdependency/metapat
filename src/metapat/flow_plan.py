"""Explicit METAPAT authority, question, runtime-data, and proof-status flows.

Usage guidance
--------------
Consumers may display these constants or use them in architecture checks. They
are declarations of responsibility, not runtime execution or empirical proof.
When METAPAT identifies questions whose answers require observation or
comparison, ``QUESTION_TO_MEASUREMENT_FLOW`` declares the handoff into EDCM.
"""

# === MODULE_BUILD ===
# id: metapat_flow_plan
#   module_name: metapat.flow_plan
#   module_kind: schema
#   summary: separates METAPAT semantic authority, question-to-measurement, EDCM/UCNS runtime data, and proof-status flows
#   owner: The Interdependency
#   public_surface: AUTHORITY_FLOW, QUESTION_TO_MEASUREMENT_FLOW, MEASUREMENT_SELECTION_BOUNDARY, RUNTIME_DATA_FLOW, PROOF_STATUS_FLOW, UCNS_SIDE_STATUS, EDCM_SIDE_STATUS
#   internal_surface: none
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_envelope, tests.test_ucns_bridge
#   rollout: documentation_and_contract
#   rollback: restore prior architecture declarations
#   requires: metapat_module_envelope, metapat_ucns_adapter
#   since: 2026-07-12
#   unresolved: executable EDCM consumer and shared-stack result envelope until merged cross-repository
# === END MODULE_BUILD ===

# === CAPABILITIES ===
# id: metapat_flow_status
#   summary: exposes distinct authority, question-to-measurement, runtime-data, and proof-status architecture declarations
#   exposes: metapat.flow_plan.AUTHORITY_FLOW, metapat.flow_plan.QUESTION_TO_MEASUREMENT_FLOW, metapat.flow_plan.MEASUREMENT_SELECTION_BOUNDARY, metapat.flow_plan.RUNTIME_DATA_FLOW, metapat.flow_plan.PROOF_STATUS_FLOW
#   inputs: none
#   outputs: str
#   boundaries: auth:none, storage:none, network:none, user_data:none
# === END CAPABILITIES ===

# === DEPENDENCIES ===
# id: metapat_flow_edges
#   summary: METAPAT determines which questions and distinctions matter while EDCM operationalizes measurable answers and actual UCNS carries geometry where used
#   internal: metapat.envelope, metapat.ucns
#   external: The-Interdependency/ucns, The-Interdependency/edcm
#   provides: metapat_flow_plan
#   class: architecture
#   direction: semantic authority, measurement design, runtime data, and proof status remain distinct
#   owner: The Interdependency
# === END DEPENDENCIES ===

# === CONTRACTS ===
# id: metapat_questions_seed_edcm
#   given: METAPAT identifies bounded questions whose answers require observation, comparison, or measurement
#   then: those questions seed an EDCM measurement design; METAPAT selects the distinctions worth asking about while EDCM owns operationalization into observables, metrics, ratios, baselines, comparisons, and falsifiers
#   class: architecture
#
# id: metapat_metrics_do_not_choose_questions
#   given: a domain exposes metrics or observations before the relevant distinctions are selected
#   then: metric availability may constrain observability but does not determine which distinctions matter; unresolved important distinctions remain hmmm rather than receiving invented proxies
#   class: measurement_boundary
# === END CONTRACTS ===

# === OWNERS ===
# id: metapat_flow_owner
#   owner: The Interdependency
#   steward: Erin Spencer
#   review_required_for: dependency, public_api, canon
#   escalation: hmmm
# === END OWNERS ===

# === BOUNDARIES ===
# id: metapat_flow_boundaries
#   summary: architecture status constants with no active external calls
#   auth_boundary: none
#   storage_boundary: none
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
# === END BOUNDARIES ===

AUTHORITY_FLOW = """METAPAT canon
    |
    +-- constrains terms, interpretation, allowed derivations, and claim status
    v
UCNS adapters and EDCM consumers"""

QUESTION_TO_MEASUREMENT_FLOW = """thing / domain object
    |
    v
METAPAT -> bounded questions and distinctions worth making legible
    |
    v
EDCM -> observables, metrics, ratios, baselines, comparisons, falsifiers
    |
    v
domain measurement instrument"""

MEASUREMENT_SELECTION_BOUNDARY = (
    "Available metrics constrain what can be observed; they do not determine which "
    "distinctions matter. An important distinction without an honest observable "
    "remains hmmm rather than receiving an invented proxy."
)

RUNTIME_DATA_FLOW = """source evidence -> EDCM parsing -> actual UCNS representation -> EDCM readouts
                                     ^
                                     |
                          METAPAT-derived semantic constraints"""

PROOF_STATUS_FLOW = (
    "UCNS theorem or domain status remains UCNS evidence and does not transfer "
    "into METAPAT ontology validity or EDCM measurement validity."
)

UCNS_SIDE_STATUS = (
    "implemented: optional adapter constructs actual ucns.UCNSObject geometry; "
    "METAPAT statements remain external provenance; no local UCNS algebra"
)
EDCM_SIDE_STATUS = (
    "hmmm: METAPAT question-to-measurement handoff is declared; executable EDCM "
    "consumer and shared-stack fixture must still be merged in The-Interdependency/edcm"
)

__all__ = [
    "AUTHORITY_FLOW",
    "QUESTION_TO_MEASUREMENT_FLOW",
    "MEASUREMENT_SELECTION_BOUNDARY",
    "RUNTIME_DATA_FLOW",
    "PROOF_STATUS_FLOW",
    "UCNS_SIDE_STATUS",
    "EDCM_SIDE_STATUS",
]
