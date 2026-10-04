# === CHECKS ===
# id: check_recurrence_homologous
#   proves: recurrence_homology_preserves_distinct_paths
#   call: self::test_distinct_complete_recurrence_is_homologous_without_proof
#   mutates: none
#   cleanup: none
#
# id: check_recurrence_same_structure_proof
#   proves: recurrence_same_structure_requires_proof
#   call: self::test_same_structure_requires_explicit_equivalence_proof
#   mutates: none
#   cleanup: none
#
# id: check_recurrence_shared_ancestry
#   proves: recurrence_homology_preserves_distinct_paths
#   call: self::test_shared_ancestry_reduces_independence_not_recurrence
#   mutates: none
#   cleanup: none
#
# id: check_recurrence_partial_analogy
#   proves: recurrence_no_semantic_transfer
#   call: self::test_partial_invariants_are_analogous
#   mutates: none
#   cleanup: none
#
# id: check_recurrence_unresolved
#   proves: recurrence_unresolved_fails_closed
#   call: self::test_unknown_mapping_or_replay_fails_closed
#   mutates: none
#   cleanup: none
#
# id: check_recurrence_failed_replay
#   proves: recurrence_no_semantic_transfer
#   call: self::test_failed_replay_is_divergent
#   mutates: none
#   cleanup: none
# id: check_recurrence_catalog_binding
#   proves: recurrence_catalog_bound
#   call: self::test_same_structure_requires_explicit_equivalence_proof
#   mutates: none
#   cleanup: none
# === END CHECKS ===

import pytest

from metapat.catalog import CATALOG_VERSION, canonical_semantic_catalog
from metapat.structural_recurrence import (
    RecurrenceDecision,
    RecurrenceEvidence,
    adjudicate_recurrence,
)


def evidence(**overrides):
    catalog = canonical_semantic_catalog()
    data = dict(
        source_domain="psychohistory",
        target_domain="ps-fauna",
        source_origin_id="asimov",
        target_origin_id="erin",
        source_path_id="population-statistics",
        target_path_id="distributed-attractor",
        declared_invariants=("many-to-system", "system-level-regularity"),
        preserved_invariants=("many-to-system", "system-level-regularity"),
        mapping_complete=True,
        replay_passed=True,
        catalog_version=CATALOG_VERSION,
        catalog_digest=catalog.catalog_digest,
        catalog_module_ids=(
            "metapat.axiom.12.domain_qualification",
            "metapat.postulate.1.partial_domains",
            "metapat.postulate.6.cross_domain_falsification",
            "metapat.theory.11.cross_domain_reconstruction",
        ),
        ancestry_resolved=True,
    )
    data.update(overrides)
    return RecurrenceEvidence(**data)


def test_distinct_complete_recurrence_is_homologous_without_proof():
    decision = adjudicate_recurrence(evidence())
    assert decision.outcome == "HOMOLOGOUS"
    assert decision.independent
    assert decision.semantic_transfer is False
    assert decision.source_domain == "psychohistory"
    assert decision.target_domain == "ps-fauna"
    assert decision.source_path_id == "population-statistics"
    with pytest.raises(ValueError, match="semantic_transfer"):
        RecurrenceDecision(
            outcome="HOMOLOGOUS", independent=True,
            source_domain="a", target_domain="b",
            source_origin_id="oa", target_origin_id="ob",
            source_path_id="pa", target_path_id="pb",
            catalog_version=decision.catalog_version,
            catalog_digest=decision.catalog_digest,
            catalog_module_ids=decision.catalog_module_ids,
            declared_invariants=("x",), preserved_invariants=("x",),
            shared_ancestry=(), equivalence_proof_id=None,
            semantic_transfer=True,
        )


def test_same_structure_requires_explicit_equivalence_proof():
    decision = adjudicate_recurrence(evidence(equivalence_proof_id="ucns-proof:abc"))
    assert decision.outcome == "SAME_STRUCTURE"
    with pytest.raises(ValueError, match="catalog version mismatch"):
        evidence(catalog_version="stale")
    with pytest.raises(ValueError, match="non-empty"):
        evidence(declared_invariants=("",), preserved_invariants=("",))


def test_shared_ancestry_reduces_independence_not_recurrence():
    decision = adjudicate_recurrence(evidence(shared_ancestry=("source:common-corpus",)))
    assert decision.outcome == "HOMOLOGOUS"
    assert decision.independent is False


def test_partial_invariants_are_analogous():
    decision = adjudicate_recurrence(
        evidence(preserved_invariants=("many-to-system",))
    )
    assert decision.outcome == "ANALOGOUS"


def test_unknown_mapping_or_replay_fails_closed():
    assert adjudicate_recurrence(evidence(mapping_complete=None)).outcome == "HMMM"
    assert adjudicate_recurrence(evidence(replay_passed=None)).outcome == "HMMM"
    decision = adjudicate_recurrence(evidence(ancestry_resolved=False))
    assert decision.outcome == "HMMM"
    assert decision.independent is None


def test_failed_replay_is_divergent():
    assert adjudicate_recurrence(evidence(replay_passed=False)).outcome == "DIVERGENT"
