// METAPAT msdmd collection point.
// Maintained by hand until the repo-local collector emits this TypeScript view.

export type MsdmdDeclaration = {
  file: string;
  block: string;
  id: string;
  fields: Record<string, string>;
};

export type MsdmdEdge = {
  from: string;
  to: string;
  kind: string;
  source_block: string;
  source_id: string;
};

export type MsdmdGap = {
  file: string;
  missing: string[];
  note?: string;
};

export type MsdmdCollection = {
  repo: string;
  declarations: MsdmdDeclaration[];
  gaps: MsdmdGap[];
  edges: MsdmdEdge[];
};

export const declarations: MsdmdDeclaration[] = [
  { file: "AGENTS.md", block: "LLMS", id: "project_overview", fields: { content: "METAPAT semantic authority, immutable envelopes, actual UCNS adapter, and EDCM consumer boundary." } },
  { file: "src/metapat/__init__.py", block: "MODULE_BUILD", id: "metapat_package_exports", fields: { module_name: "metapat" } },
  { file: "src/metapat/__init__.py", block: "DEPENDENCIES", id: "metapat_package_dependency_edges", fields: { imports: "metapat.canon, metapat.envelope, metapat.validation, metapat.ucns" } },
  { file: "src/metapat/canon.py", block: "MODULE_BUILD", id: "metapat_canon_core", fields: { module_name: "metapat.canon" } },
  { file: "src/metapat/canon.py", block: "DOCS", id: "metapat_canon_docs", fields: { source: "AXIOMS.md", status: "current" } },
  { file: "src/metapat/canon.py", block: "CAPABILITIES", id: "metapat_canon_constants", fields: { exposes: "metapat.canon.definitions, metapat.canon.canon_digest" } },
  { file: "src/metapat/canon.py", block: "OWNERS", id: "metapat_canon_owner", fields: { owner: "The Interdependency" } },
  { file: "src/metapat/canon.py", block: "BOUNDARIES", id: "metapat_canon_boundaries", fields: { network_boundary: "none" } },
  { file: "src/metapat/canon.py", block: "CONTRACTS", id: "metapat_root_spine_exact", fields: { call: "tests.test_contracts.test_root_spine_contains_current_axioms" } },
  { file: "src/metapat/canon.py", block: "CONTRACTS", id: "metapat_canon_digest_deterministic", fields: { call: "tests.test_envelope.test_canon_digest_is_deterministic" } },
  { file: "src/metapat/envelope.py", block: "MODULE_BUILD", id: "metapat_module_envelope", fields: { module_name: "metapat.envelope" } },
  { file: "src/metapat/envelope.py", block: "CAPABILITIES", id: "metapat_semantic_envelope", fields: { exposes: "MetapatModuleEnvelope, root_spine_module_envelope" } },
  { file: "src/metapat/envelope.py", block: "BOUNDARIES", id: "metapat_module_envelope_boundary", fields: { summary: "semantic authority and provenance only; no measurements" } },
  { file: "src/metapat/envelope.py", block: "CONTRACTS", id: "metapat_envelope_roundtrip", fields: { call: "tests.test_envelope.test_envelope_roundtrip_preserves_hmmm" } },
  { file: "src/metapat/ucns.py", block: "MODULE_BUILD", id: "metapat_ucns_adapter", fields: { module_name: "metapat.ucns" } },
  { file: "src/metapat/ucns.py", block: "CAPABILITIES", id: "metapat_actual_ucns_adapter", fields: { exposes: "metapat.ucns.adapt_envelope_to_ucns" } },
  { file: "src/metapat/ucns.py", block: "BOUNDARIES", id: "metapat_ucns_adapter_boundary", fields: { summary: "actual UCNS geometry; external METAPAT provenance; no theorem transfer" } },
  { file: "src/metapat/ucns.py", block: "CONTRACTS", id: "metapat_actual_ucns_object", fields: { call: "tests.test_ucns_bridge.test_root_spine_adapts_to_actual_ucns_object" } },
  { file: "src/metapat/validation.py", block: "MODULE_BUILD", id: "metapat_canon_contract_checks", fields: { module_name: "metapat.validation" } },
  { file: "src/metapat/validation.py", block: "CAPABILITIES", id: "metapat_canon_contract_checks", fields: { exposes: "five deterministic canon contract checks" } },
  { file: "src/metapat/validation.py", block: "CONTRACTS", id: "boundary_change_changes_outcome", fields: { call: "tests.test_contracts.test_boundary_change_changes_outcome" } },
  { file: "src/metapat/validation.py", block: "CONTRACTS", id: "tensor_before_time", fields: { call: "tests.test_contracts.test_tensor_precedes_time" } },
  { file: "src/metapat/validation.py", block: "CONTRACTS", id: "registration_not_time", fields: { call: "tests.test_contracts.test_registration_is_not_time" } },
  { file: "src/metapat/validation.py", block: "CONTRACTS", id: "observer_role_requires_registration", fields: { call: "tests.test_contracts.test_observer_role_by_registration" } },
  { file: "src/metapat/validation.py", block: "CONTRACTS", id: "consciousness_optional_observer_mode", fields: { call: "tests.test_contracts.test_consciousness_is_optional" } },
  { file: "src/metapat/flow_plan.py", block: "MODULE_BUILD", id: "metapat_flow_plan", fields: { module_name: "metapat.flow_plan" } },
  { file: "src/metapat/flow_plan.py", block: "DEPENDENCIES", id: "metapat_flow_edges", fields: { external: "The-Interdependency/ucns, The-Interdependency/edcm" } },
];

export const gaps: MsdmdGap[] = [
  { file: "The-Interdependency/edcm", missing: ["merged MetapatModuleEnvelope consumer", "full shared-stack fixture"], note: "downstream cross-repository work; hmmm until implemented and tested." },
  { file: "src/metapat/ucns.py", missing: ["ratified payload/tag/external-provenance semantic mapping"], note: "current mapping remains external-provenance and unresolved in the envelope." },
  { file: "COMPLIANCE.md", missing: ["current collector and skill-lib drift command output"], note: "must be regenerated from the active branch." },
];

export const edges: MsdmdEdge[] = [
  { from: "The-Interdependency/metapat", to: "The-Interdependency/ucns", kind: "semantic_envelope_to_optional_geometry_adapter", source_block: "DEPENDENCIES", source_id: "metapat_flow_edges" },
  { from: "The-Interdependency/metapat", to: "The-Interdependency/edcm", kind: "semantic_authority_constraints", source_block: "DEPENDENCIES", source_id: "metapat_flow_edges" },
  { from: "The-Interdependency/ucns", to: "The-Interdependency/edcm", kind: "runtime_geometry_evidence", source_block: "DEPENDENCIES", source_id: "metapat_flow_edges" },
];

const collection: MsdmdCollection = { repo: "The-Interdependency/metapat", declarations, gaps, edges };

export default collection;
