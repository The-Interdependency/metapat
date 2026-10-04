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
#   given: mapping, replay, invariant status, or independence is unresolved
#   then: HMMM is emitted and independence remains unknown rather than guessed
#   class: safety
# id: recurrence_catalog_bound
#   given: recurrence adjudication is requested
#   then: evidence must bind the exact current METAPAT catalog plus domain-qualification and cross-domain-reconstruction modules
#   class: provenance_contract
# === END CONTRACTS ===

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .catalog import CATALOG_VERSION, canonical_semantic_catalog

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
    catalog_version: str
    catalog_digest: str
    catalog_module_ids: tuple[str, ...]
    equivalence_proof_id: Optional[str] = None
    shared_ancestry: tuple[str, ...] = ()
    ancestry_resolved: bool = False
    unresolved: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        for name in (
            "source_domain", "target_domain", "source_origin_id",
            "target_origin_id", "source_path_id", "target_path_id",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        object.__setattr__(self, "declared_invariants", tuple(self.declared_invariants))
        object.__setattr__(self, "preserved_invariants", tuple(self.preserved_invariants))
        object.__setattr__(self, "catalog_module_ids", tuple(self.catalog_module_ids))
        object.__setattr__(self, "shared_ancestry", tuple(self.shared_ancestry))
        object.__setattr__(self, "unresolved", tuple(self.unresolved))
        if not self.declared_invariants:
            raise ValueError("at least one declared invariant is required")
        if any(not isinstance(x, str) or not x.strip() for x in self.declared_invariants):
            raise ValueError("declared invariants must be non-empty strings")
        if any(not isinstance(x, str) or not x.strip() for x in self.preserved_invariants):
            raise ValueError("preserved invariants must be non-empty strings")
        if len(set(self.declared_invariants)) != len(self.declared_invariants):
            raise ValueError("declared invariants must be unique")
        if not set(self.preserved_invariants).issubset(self.declared_invariants):
            raise ValueError("preserved invariants must be declared")
        if type(self.mapping_complete) not in (bool, type(None)):
            raise ValueError("mapping_complete must be bool or None")
        if type(self.replay_passed) not in (bool, type(None)):
            raise ValueError("replay_passed must be bool or None")
        if type(self.ancestry_resolved) is not bool:
            raise ValueError("ancestry_resolved must be bool")
        if self.equivalence_proof_id is not None and (
            not isinstance(self.equivalence_proof_id, str) or not self.equivalence_proof_id.strip()
        ):
            raise ValueError("equivalence_proof_id must be non-empty when supplied")
        catalog = canonical_semantic_catalog()
        required_modules = {
            "metapat.axiom.12.domain_qualification",
            "metapat.postulate.1.partial_domains",
            "metapat.postulate.6.cross_domain_falsification",
            "metapat.theory.11.cross_domain_reconstruction",
        }
        if self.catalog_version != CATALOG_VERSION:
            raise ValueError("recurrence evidence catalog version mismatch")
        if self.catalog_digest != catalog.catalog_digest:
            raise ValueError("recurrence evidence catalog digest mismatch")
        if not required_modules.issubset(set(self.catalog_module_ids)):
            raise ValueError("recurrence evidence missing required catalog module bindings")

    @property
    def paths_distinct(self) -> bool:
        return (
            self.source_origin_id != self.target_origin_id
            or self.source_path_id != self.target_path_id
        )

    @property
    def independent(self) -> Optional[bool]:
        if not self.ancestry_resolved:
            return None
        return self.paths_distinct and not self.shared_ancestry


@dataclass(frozen=True, slots=True)
class RecurrenceDecision:
    outcome: str
    independent: Optional[bool]
    source_domain: str
    target_domain: str
    source_origin_id: str
    target_origin_id: str
    source_path_id: str
    target_path_id: str
    catalog_version: str
    catalog_digest: str
    catalog_module_ids: tuple[str, ...]
    declared_invariants: tuple[str, ...]
    preserved_invariants: tuple[str, ...]
    shared_ancestry: tuple[str, ...]
    equivalence_proof_id: Optional[str]
    semantic_transfer: bool = False
    proof_status_transfer: bool = False
    measurement_status_transfer: bool = False

    def __post_init__(self) -> None:
        if self.outcome not in RECURRENCE_OUTCOMES:
            raise ValueError("unsupported recurrence outcome")
        if self.independent not in (True, False, None):
            raise ValueError("independent must be bool or None")
        for name in ("semantic_transfer", "proof_status_transfer", "measurement_status_transfer"):
            if getattr(self, name) is not False:
                raise ValueError(f"{name} must remain false")


def adjudicate_recurrence(evidence: RecurrenceEvidence) -> RecurrenceDecision:
    """Classify recurrence while preserving domain and evidence boundaries."""

    unresolved = (
        bool(evidence.unresolved)
        or evidence.mapping_complete is None
        or evidence.replay_passed is None
        or evidence.independent is None
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
        source_domain=evidence.source_domain,
        target_domain=evidence.target_domain,
        source_origin_id=evidence.source_origin_id,
        target_origin_id=evidence.target_origin_id,
        source_path_id=evidence.source_path_id,
        target_path_id=evidence.target_path_id,
        catalog_version=evidence.catalog_version,
        catalog_digest=evidence.catalog_digest,
        catalog_module_ids=evidence.catalog_module_ids,
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
