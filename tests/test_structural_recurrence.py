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
# === END CHECKS ===

from metapat.structural_recurrence import RecurrenceEvidence, adjudicate_recurrence


def evidence(**overrides):
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
    )
    data.update(overrides)
    return RecurrenceEvidence(**data)


def test_distinct_complete_recurrence_is_homologous_without_proof():
    decision = adjudicate_recurrence(evidence())
    assert decision.outcome == "HOMOLOGOUS"
    assert decision.independent
    assert decision.semantic_transfer is False


def test_same_structure_requires_explicit_equivalence_proof():
    decision = adjudicate_recurrence(evidence(equivalence_proof_id="ucns-proof:abc"))
    assert decision.outcome == "SAME_STRUCTURE"


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


def test_failed_replay_is_divergent():
    assert adjudicate_recurrence(evidence(replay_passed=False)).outcome == "DIVERGENT"
