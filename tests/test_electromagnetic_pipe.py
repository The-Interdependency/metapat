from __future__ import annotations

import json
import unittest
from pathlib import Path

from metapat import canonical_semantic_catalog, validate_application_against_catalog
from metapat.application import assert_application_sources_match
from metapat.electromagnetic_pipe import (
    AlloyCandidate,
    ElectromagneticPipeDesign,
    electromagnetic_pipe_application_module,
    electromagnetic_pipe_design,
)


class TestElectromagneticPipeApplication(unittest.TestCase):
    def test_control_topology_and_windings(self) -> None:
        design = electromagnetic_pipe_design()
        self.assertEqual(design.assembly_length_m, 3.0)
        self.assertEqual(design.outer_pipe_diameter_in, 3.0)
        self.assertEqual(design.radial_layer_count, 3)
        self.assertEqual(design.handednesses, ("clockwise", "widdershins"))
        self.assertEqual(design.phases_per_handedness, 3)
        self.assertEqual(design.phase_circuit_count, 18)
        self.assertEqual(design.three_phase_system_count, 6)
        self.assertEqual(
            tuple((layer.layer_name, layer.wire_awg, layer.turns_per_inch) for layer in design.winding_layers),
            (("outer", 12, 6), ("middle", 16, 12), ("inner", 20, 18)),
        )
        self.assertEqual(design.control_object, "one three-phase vector per handedness per radial layer")
        self.assertEqual(design.current_command_variable, "phase current")
        self.assertEqual(design.voltage_role, "compliance")

    def test_attractors_and_alloy_search_remain_bounded(self) -> None:
        design = electromagnetic_pipe_design()
        self.assertEqual(
            design.mobile_element_designation,
            "ceramic-coated magnetic eddy-current attractors",
        )
        self.assertEqual(design.prohibited_mobile_element_designation, "bearings")
        self.assertNotIn("bearing", design.mobile_element_designation.lower())
        self.assertIn("field-history response", design.mobile_element_effects)
        self.assertIn("cluster", design.mobile_element_behaviors)
        self.assertEqual(len(design.alloy_candidates), 5)
        for candidate in design.alloy_candidates:
            self.assertEqual(candidate.basis, "atomic percent")
            self.assertEqual(candidate.iron + candidate.cobalt + candidate.nickel, 75.0)
            self.assertEqual(candidate.chromium, 15.0)
            self.assertEqual(candidate.manganese, 10.0)
        with self.assertRaisesRegex(ValueError, r"Fe \+ Co \+ Ni"):
            AlloyCandidate("invalid", 40, 20, 10, 20, 10)

    def test_application_is_catalog_bound_and_source_current(self) -> None:
        catalog = canonical_semantic_catalog()
        application = electromagnetic_pipe_application_module(catalog)
        validate_application_against_catalog(application, catalog)
        self.assertEqual(application.claim_status, "EMPIRICAL-FRONTIER")
        self.assertEqual(application.root_impact, "none")
        self.assertEqual(len(application.catalog_bindings), 20)
        self.assertNotIn(
            "metapat.theory.10.symbolic_and_memetic_transfer",
            {binding.module_id for binding in application.catalog_bindings},
        )
        repo_root = Path(__file__).resolve().parents[1]
        assert_application_sources_match(repo_root, application)
        self.assertTrue(any("six three-phase systems" in text for text in application.source_statements))
        self.assertTrue(any("not bearings" in text for text in application.source_statements))

    def test_roundtrip_and_evidence_firewall(self) -> None:
        design = electromagnetic_pipe_design()
        reconstructed = ElectromagneticPipeDesign.from_json(design.to_json())
        self.assertEqual(reconstructed, design)
        self.assertEqual(json.loads(reconstructed.to_json()), json.loads(design.to_json()))

        application = design.application
        self.assertFalse(application.metapat_validity_claim)
        self.assertFalse(application.domain_validity_claim)
        self.assertFalse(application.measurement_validity_claim)
        self.assertFalse(application.ucns_theorem_status_transfer)
        self.assertFalse(application.ucns_topology_claim)
        self.assertFalse(design.electromagnetic_validity_claim)
        self.assertFalse(design.alloy_validity_claim)
        self.assertFalse(design.insulation_validity_claim)
        self.assertFalse(design.fault_containment_validity_claim)
        self.assertFalse(design.spacecraft_safety_validity_claim)
        self.assertTrue(design.protection_distance_status.startswith("No fixed protection distance"))

        unknown = design.to_dict()
        unknown["ideal_alloy"] = "claimed"
        with self.assertRaisesRegex(ValueError, "unknown pipe-design fields"):
            ElectromagneticPipeDesign.from_dict(unknown)

        tampered = design.to_dict()
        tampered["phase_circuit_count"] = 17
        with self.assertRaisesRegex(ValueError, "phase_circuit_count"):
            ElectromagneticPipeDesign.from_dict(tampered)

        changed = design.to_dict()
        changed["protection_distance_status"] = "known"
        with self.assertRaisesRegex(ValueError, "design_digest"):
            ElectromagneticPipeDesign.from_dict(changed)


if __name__ == "__main__":
    unittest.main()
