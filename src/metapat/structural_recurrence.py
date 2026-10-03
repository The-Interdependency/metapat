"""Provisional METAPAT adjudication of cross-domain structural recurrence.

This module classifies evidence supplied by domain/geometry producers. It does
not compute UCNS geometry, transfer domain semantics, or promote recurrence to
truth. Usage: construct RecurrenceEvidence and call adjudicate_recurrence().
"""

# === MODULE_BUILD ===
# id: metapat_structural_recurrence_v0
#   module_name: metapat.structural_recurrence
#   module_kind: engine
#   summary: adjudicates cross-domain recurrence evidence without transferring domain semantics
#   owner: The Interdependency
#   public_surface: RECURRENCE_OUTCOMES, RecurrenceEvidence, RecurrenceDecision, adjudicate_recurrence
#   internal_surface: canonical serialization and validation
#   auth_boundary: none
#   storage_boundary: serialization-only
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_structural_recurrence
#   rollout: provisional importable module
#   rollback: remove module and tests; no canon record is mutated
#   requires: metapat root doctrine structural recurrence does not transfer a domain term
#   since: 2026-10-03
#   unresolved: threshold-free geometric proof vocabulary remains owned by UCNS
# === END MODULE_BUILD ===

# === CONTRACTS ===
# id: recurrence_no_semantic_transfer
#   given: two domain-qualified structures recur
#   then: the decision records recurrence only and transfers no mechanism, ontology, theorem status, or measurement validity
#   class: boundary_contract
# id: recurrence_same_structure_requires_proof
#   given: mapping and invariants are complete and replay passes
#   then: SAME_STRUCTURE is emitted only when an explicit equivalence proof identity is supplied
#   class: correctness
# id: recurrence_homology_preserves_distinct_paths
#   given: distinct origins or paths preserve every declared invariant without an equivalence proof
#   then: HOMOLOGOUS is emitted and path distinction remains explicit
#   class: correctness
# id: recurrence_unresolved_fails_closed
#   given: mapping, replay, or invariant status is unresolved
#   then: HMMM is emitted rather than guessing
#   class: safety
# === END CONTRACTS ===

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

RECURRENCE_OUTCOMES = frozenset({
    "SAME_STRUCTURE",
    "HOMOLOGOUS",
    "ANALOGOUS",
    "DIVERGENT",
    "HMMM",
})


@dataclass(frozen=True, slots=True)
class RecurrenceEvidence:
    source_domain: str
    target_domain: str
    source_origin_id: str
    target_origin_id: str
    source_path_id: str
    target_path_id: str
    declared_invariants: tuple[str, ...]
    preserved_invariants: tuple[str, ...]
    mapping_complete: Optional[bool]
    replay_passed: Optional[bool]
    equivalence_proof_id: Optional[str] = None
    shared_ancestry: tuple[str, ...] = ()
    unresolved: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in (
            "source_domain", "target_domain", "source_origin_id",
            "target_origin_id", "source_path_id", "target_path_id",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        if not self.declared_invariants:
            raise ValueError("at least one declared invariant is required")
        if len(set(self.declared_invariants)) != len(self.declared_invariants):
            raise ValueError("declared invariants must be unique")
        if not set(self.preserved_invariants).issubset(self.declared_invariants):
            raise ValueError("preserved invariants must be declared")
        if self.equivalence_proof_id is not None and not self.equivalence_proof_id.strip():
            raise ValueError("equivalence_proof_id must be non-empty when supplied")

    @property
    def paths_distinct(self) -> bool:
        return (
            self.source_origin_id != self.target_origin_id
            or self.source_path_id != self.target_path_id
        )

    @property
    def independent(self) -> bool:
        return self.paths_distinct and not self.shared_ancestry


@dataclass(frozen=True, slots=True)
class RecurrenceDecision:
    outcome: str
    independent: bool
    declared_invariants: tuple[str, ...]
    preserved_invariants: tuple[str, ...]
    shared_ancestry: tuple[str, ...]
    equivalence_proof_id: Optional[str]
    semantic_transfer: bool = False
    proof_status_transfer: bool = False
    measurement_status_transfer: bool = False


def adjudicate_recurrence(evidence: RecurrenceEvidence) -> RecurrenceDecision:
    """Classify recurrence while preserving domain and evidence boundaries."""

    unresolved = (
        bool(evidence.unresolved)
        or evidence.mapping_complete is None
        or evidence.replay_passed is None
    )
    if unresolved:
        outcome = "HMMM"
    elif not evidence.mapping_complete or not evidence.replay_passed:
        outcome = "DIVERGENT"
    else:
        declared = set(evidence.declared_invariants)
        preserved = set(evidence.preserved_invariants)
        if preserved == declared:
            outcome = (
                "SAME_STRUCTURE"
                if evidence.equivalence_proof_id is not None
                else "HOMOLOGOUS"
            )
        elif preserved:
            outcome = "ANALOGOUS"
        else:
            outcome = "DIVERGENT"

    return RecurrenceDecision(
        outcome=outcome,
        independent=evidence.independent,
        declared_invariants=evidence.declared_invariants,
        preserved_invariants=evidence.preserved_invariants,
        shared_ancestry=evidence.shared_ancestry,
        equivalence_proof_id=evidence.equivalence_proof_id,
    )


__all__ = [
    "RECURRENCE_OUTCOMES",
    "RecurrenceEvidence",
    "RecurrenceDecision",
    "adjudicate_recurrence",
]
