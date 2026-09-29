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
    assert len(application.catalog_bindings) == len(EPAC_JOIN_TERMS_BINDING_SPECS) == 13
    assert len({binding.module_id for binding in application.catalog_bindings}) == 13
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
