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
#   call: self::test_catalog_binding_rejects_stale_unknown_and_duplicate_modules
#   mutates: none
#   cleanup: none
# id: check_recurrence_same_path
#   proves: recurrence_homology_preserves_distinct_paths, recurrence_unresolved_fails_closed
#   call: self::test_identical_origin_and_path_do_not_establish_homology
#   mutates: none
#   cleanup: none
# id: check_recurrence_domain_boundary
#   proves: recurrence_domains_distinct
#   call: self::test_same_domain_evidence_and_decisions_are_rejected
#   mutates: none
#   cleanup: none
# id: check_recurrence_direct_decision
#   proves: recurrence_decision_evidence_coherent, recurrence_same_structure_requires_proof, recurrence_no_semantic_transfer, recurrence_catalog_bound
#   call: self::test_direct_decisions_cannot_bypass_evidence_guards
#   mutates: none
#   cleanup: none
# id: check_recurrence_identity_preserved
#   proves: recurrence_decision_evidence_coherent, recurrence_no_semantic_transfer
#   call: self::test_decisions_preserve_domain_path_and_unresolved_identity
#   mutates: none
#   cleanup: none
# id: check_recurrence_identifier_containers
#   proves: recurrence_decision_evidence_coherent, recurrence_same_structure_requires_proof
#   call: self::test_identifier_sequences_reject_malformed_values_and_freeze_lists
#   mutates: none
#   cleanup: none
# === END CHECKS ===

from dataclasses import asdict, replace

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


def test_catalog_binding_rejects_stale_unknown_and_duplicate_modules():
    current = evidence()
    assert adjudicate_recurrence(current).catalog_digest == canonical_semantic_catalog().catalog_digest
    for overrides in (
        {"catalog_version": "metapat-semantic-catalog-v3"},
        {"catalog_digest": "0" * 64},
        {"catalog_module_ids": current.catalog_module_ids[:-1]},
        {"catalog_module_ids": current.catalog_module_ids + ("metapat.fake.nonexistent",)},
        {"catalog_module_ids": current.catalog_module_ids + current.catalog_module_ids[:1]},
    ):
        with pytest.raises(ValueError):
            evidence(**overrides)


def test_identical_origin_and_path_do_not_establish_homology():
    same = evidence(target_origin_id="asimov", target_path_id="population-statistics")
    assert same.paths_distinct is False
    decision = adjudicate_recurrence(same)
    assert decision.outcome == "HMMM"
    assert decision.independent is False
    with pytest.raises(ValueError, match="outcome"):
        replace(decision, outcome="HOMOLOGOUS")
    for distinct in (
        replace(same, target_origin_id="other-origin"),
        replace(same, target_path_id="other-path"),
    ):
        assert adjudicate_recurrence(distinct).outcome == "HOMOLOGOUS"


def test_same_domain_evidence_and_decisions_are_rejected():
    for proof in (None, "fixture-proof:id"):
        with pytest.raises(ValueError, match="distinct domains"):
            evidence(target_domain="psychohistory", equivalence_proof_id=proof)
        decision = adjudicate_recurrence(evidence(equivalence_proof_id=proof))
        with pytest.raises(ValueError, match="distinct domains"):
            replace(decision, target_domain=decision.source_domain)


def test_direct_decisions_cannot_bypass_evidence_guards():
    homologous = adjudicate_recurrence(evidence())
    same = adjudicate_recurrence(evidence(equivalence_proof_id="fixture-proof:id"))
    for decision in (homologous, same):
        assert RecurrenceDecision(**asdict(decision)) == decision
        for field in ("semantic_transfer", "proof_status_transfer", "measurement_status_transfer"):
            for bad in (True, 1, 0, None, "false"):
                with pytest.raises(ValueError, match=field):
                    replace(decision, **{field: bad})
        for changes in (
            {"catalog_version": "stale"}, {"catalog_digest": "0" * 64},
            {"catalog_module_ids": decision.catalog_module_ids + ("unknown",)},
            {"catalog_module_ids": decision.catalog_module_ids * 2},
            {"mapping_complete": False}, {"replay_passed": False},
            {"ancestry_resolved": False}, {"unresolved": ("mapping hmmm",)},
            {"preserved_invariants": ()}, {"independent": 1},
            {"shared_ancestry": ("shared",)},
        ):
            with pytest.raises(ValueError):
                replace(decision, **changes)
    for bad_proof in (None, "", "   ", 1):
        with pytest.raises(ValueError):
            replace(same, equivalence_proof_id=bad_proof)
    with pytest.raises(ValueError, match="outcome"):
        replace(homologous, outcome="SAME_STRUCTURE")


def test_decisions_preserve_domain_path_and_unresolved_identity():
    source = evidence(unresolved=("UCNS mapping hmmm",), ancestry_resolved=False)
    decision = adjudicate_recurrence(source)
    assert decision.outcome == "HMMM" and decision.independent is None
    for name in RecurrenceEvidence.__dataclass_fields__:
        assert getattr(decision, name) == getattr(source, name)
    for name in ("source_domain", "target_domain", "source_origin_id", "target_origin_id", "source_path_id", "target_path_id"):
        changed = adjudicate_recurrence(replace(source, **{name: "different:" + getattr(source, name)}))
        assert changed != decision


def test_identifier_sequences_reject_malformed_values_and_freeze_lists():
    current = evidence()
    for field in ("declared_invariants", "preserved_invariants", "catalog_module_ids", "shared_ancestry", "unresolved"):
        for malformed in ("id", b"id", None, ("",), ("   ",), (1,), {"id": "value"}):
            with pytest.raises(ValueError):
                replace(current, **{field: malformed})
    for field in ("declared_invariants", "preserved_invariants", "catalog_module_ids"):
        with pytest.raises(ValueError):
            replace(current, **{field: getattr(current, field) * 2})
    with pytest.raises(ValueError):
        replace(current, declared_invariants=())
    with pytest.raises(ValueError):
        replace(current, preserved_invariants=("undeclared",))
    lists = {name: list(getattr(current, name)) for name in (
        "declared_invariants", "preserved_invariants", "catalog_module_ids", "shared_ancestry", "unresolved",
    )}
    frozen = replace(current, **lists)
    decision = adjudicate_recurrence(frozen)
    for values in lists.values():
        values.append("later")
    assert frozen == current
    assert decision == adjudicate_recurrence(current)
