"""Checks for the catalog-bound EPAC typed join-terms application."""

# === CHECKS ===
# id: check_epac_join_terms_catalog_bound
#   proves: metapat_epac_join_terms_catalog_bound
#   call: self::test_application_bindings_match_catalog
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_customs_boundary
#   proves: metapat_epac_join_terms_customs_boundary
#   call: self::test_customs_boundary_blocks_unlicensed_transfer
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_recursive_identity
#   proves: metapat_epac_join_terms_recursive_identity
#   call: self::test_recursive_identity_is_preserved_without_flattening
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_complete_scale_map
#   proves: metapat_epac_join_terms_complete_scale_map
#   call: self::test_scale_map_is_exactly_s0_through_s6
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_candidate_status
#   proves: metapat_epac_join_terms_candidate_status
#   call: self::test_application_remains_unpromoted
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_source_current
#   proves: metapat_epac_join_terms_source_current
#   call: self::test_application_source_is_current
#   mutates: filesystem_read
#   cleanup: none
#
# id: check_epac_join_terms_fixture_current
#   proves: metapat_epac_join_terms_fixture_current
#   call: self::test_packaged_fixture_matches_constructor
#   mutates: filesystem_read
#   cleanup: none
#
# id: check_epac_join_terms_fixture_generated
#   proves: metapat_epac_join_terms_fixture_generated
#   call: self::test_fixture_renderer_is_deterministic
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_fixture_generator_current
#   proves: metapat_epac_join_terms_fixture_generator_current
#   call: self::test_fixture_generator_matches_packaged_bytes
#   mutates: filesystem_read
#   cleanup: none
#
# id: check_epac_join_terms_state_readout_distinction
#   proves: metapat_epac_join_terms_state_readout_distinction
#   call: self::test_state_readout_distinction
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_bearing_not_vector
#   proves: metapat_epac_join_terms_bearing_not_vector
#   call: self::test_bearing_not_vector
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_transformation_result
#   proves: metapat_epac_join_terms_transformation_result
#   call: self::test_transformation_result
#   mutates: none
#   cleanup: none
#
# id: check_epac_join_terms_time_occurrence
#   proves: metapat_epac_join_terms_time_occurrence
#   call: self::test_time_occurrence
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from importlib.resources import files
from pathlib import Path

import metapat
from metapat.epac_join_terms import (
    EPAC_JOIN_TERMS_APPLICATION_VERSION,
    EPAC_JOIN_TERMS_BINDING_SPECS,
    epac_join_terms_application_module,
)
from tools.generate_application_fixtures import render_epac_join_terms_fixture


def test_application_bindings_match_catalog() -> None:
    catalog = metapat.canonical_semantic_catalog()
    application = epac_join_terms_application_module(catalog)
    metapat.validate_application_against_catalog(application, catalog)
    assert len(application.catalog_bindings) == len(EPAC_JOIN_TERMS_BINDING_SPECS) == 12
    assert len({binding.module_id for binding in application.catalog_bindings}) == 12
    assert all(len(binding.module_digest) == 64 for binding in application.catalog_bindings)


def test_customs_boundary_blocks_unlicensed_transfer() -> None:
    application = epac_join_terms_application_module()
    non_transfers = " ".join(application.does_not_transfer)
    assert "does not transfer a UCNS coordinate" in non_transfers
    assert "EPAC phase is not chemistry phase" in non_transfers
    assert "does not establish energy coupling" in non_transfers
    assert "does not establish ancestry" in non_transfers
    assert application.ucns_topology_claim is False


def test_recursive_identity_is_preserved_without_flattening() -> None:
    application = epac_join_terms_application_module()
    statements = " ".join(application.domain_statements)
    assert "new identity O(S_{n+1})" in statements
    assert "does not erase or contract" in statements
    assert "flattened bag is not that object" in next(
        binding.application_statement
        for binding in application.catalog_bindings
        if binding.application_role == "multi-origin-tensor"
    )


def test_scale_map_is_exactly_s0_through_s6() -> None:
    application = epac_join_terms_application_module()
    assert application.selected_scales == (
        "S0 subatomic slot",
        "S1 atomic",
        "S2 join/arity",
        "S3 embed",
        "S4 electronic state",
        "S5 EPAC energy readout",
        "S6 ensemble",
    )


def test_application_remains_unpromoted() -> None:
    application = epac_join_terms_application_module()
    assert EPAC_JOIN_TERMS_APPLICATION_VERSION == "epac-join-terms-application-v4"
    assert application.claim_status == "CROSS-DOMAIN-HYPOTHESIS"
    assert application.root_impact == "none"
    assert all(
        value is False
        for value in (
            application.metapat_validity_claim,
            application.domain_validity_claim,
            application.measurement_validity_claim,
            application.ucns_theorem_status_transfer,
            application.ucns_topology_claim,
        )
    )
    assert application.to_json() == epac_join_terms_application_module().to_json()


def test_application_source_is_current() -> None:
    application = epac_join_terms_application_module()
    metapat.assert_application_sources_match(Path(__file__).resolve().parents[1], application)
    assert len(application.unresolved_constraints) == 3
    assert all(item.startswith("hmmm:") for item in application.unresolved_constraints)


def test_packaged_fixture_matches_constructor() -> None:
    fixture = files("metapat").joinpath("fixtures/epac-join-terms-application-v4.json")
    assert fixture.is_file()
    assert fixture.read_text(encoding="utf-8") == epac_join_terms_application_module().to_json() + "\n"


def test_fixture_renderer_is_deterministic() -> None:
    rendered = render_epac_join_terms_fixture()
    assert rendered.endswith("\n")
    assert rendered.count("\n") == 1
    assert rendered == render_epac_join_terms_fixture()


def test_fixture_generator_matches_packaged_bytes() -> None:
    fixture = files("metapat").joinpath("fixtures/epac-join-terms-application-v4.json")
    assert fixture.is_file()
    assert fixture.read_text(encoding="utf-8") == render_epac_join_terms_fixture()


def _statement(role: str) -> str:
    return next(
        binding.application_statement
        for binding in epac_join_terms_application_module().catalog_bindings
        if binding.application_role == role
    )


def test_state_readout_distinction() -> None:
    state = _statement("origin-state")
    scalar = _statement("state-metric")
    assert "metricable properties" in state
    assert "not scalar observations" in state
    assert "separately identified" in scalar
    assert "origin, measured property, and measurement rule" in scalar
    assert "not the state itself" in scalar
    assert "phase and capacity metrics" not in state


def test_bearing_not_vector() -> None:
    application = epac_join_terms_application_module()
    assert all(binding.module_id != "metapat.axiom.8.vector"
               and binding.application_role != "inferred-bearing"
               for binding in application.catalog_bindings)
    assert any("Static bearing" in item and "no Vector role is licensed" in item
               for item in application.does_not_transfer)
    assert "grants no Vector binding" in application.transfers[0]


def test_transformation_result() -> None:
    statement = _statement("join-transformation")
    assert "resulting before/after change" in statement
    assert "named state property of an identified thing" in statement
    assert "caused by a declared join action" in statement
    assert "different values at unrelated origins alone are not that result" in statement
    assert any("affected thing, named property, before and after states, resulting difference"
               in item for item in epac_join_terms_application_module().evidence_requirements)


def test_time_occurrence() -> None:
    statement = _statement("transformation-sequence")
    assert "at least two resulting state changes actually occurred sequentially" in statement
    assert "sorting records, sequence numbers, and structural scale order cannot create it" in statement
    assert any("simultaneous or unordered changes do not qualify" in item
               for item in epac_join_terms_application_module().evidence_requirements)
