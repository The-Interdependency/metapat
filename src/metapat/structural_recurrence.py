"""Provisional METAPAT adjudication of cross-domain structural recurrence.

This module classifies evidence supplied by domain/geometry producers. It does
not compute UCNS geometry, transfer domain semantics, or promote recurrence to
truth. Usage: construct RecurrenceEvidence and call adjudicate_recurrence().
Direct RecurrenceDecision construction must carry the same mapping, replay,
ancestry, and unresolved evidence; its outcome must reproduce adjudication.
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
#   storage_boundary: none
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
# id: recurrence_domains_distinct
#   given: a cross-domain recurrence record is constructed
#   then: the source and target domain identifiers are distinct
#   class: boundary_contract
# id: recurrence_decision_evidence_coherent
#   given: a decision is constructed directly or through adjudication
#   then: immutable validated evidence reproduces its outcome and independence with every no-transfer flag exactly false
#   class: safety
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


def _identifiers(value: object, name: str) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise ValueError(f"{name} must be a list or tuple of identifiers")
    if any(not isinstance(item, str) or not item.strip() for item in value):
        raise ValueError(f"{name} must contain non-empty strings")
    return tuple(value)


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
            if name in {"source_domain", "target_domain"} and value != value.strip():
                raise ValueError(f"{name} must not contain surrounding whitespace")
        if self.source_domain == self.target_domain:
            raise ValueError("cross-domain recurrence requires distinct domains")
        for name in (
            "declared_invariants", "preserved_invariants", "catalog_module_ids",
            "shared_ancestry", "unresolved",
        ):
            object.__setattr__(self, name, _identifiers(getattr(self, name), name))
        if not self.declared_invariants:
            raise ValueError("at least one declared invariant is required")
        for name in ("declared_invariants", "preserved_invariants", "catalog_module_ids"):
            values = getattr(self, name)
            if len(set(values)) != len(values):
                raise ValueError(f"{name} must be unique")
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
        if not set(self.catalog_module_ids).issubset({module.module_id for module in catalog.modules}):
            raise ValueError("recurrence evidence contains unknown catalog module bindings")
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
    mapping_complete: Optional[bool] = None
    replay_passed: Optional[bool] = None
    ancestry_resolved: bool = False
    unresolved: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        if self.outcome not in RECURRENCE_OUTCOMES:
            raise ValueError("unsupported recurrence outcome")
        if type(self.independent) not in (bool, type(None)):
            raise ValueError("independent must be bool or None")
        for name in ("semantic_transfer", "proof_status_transfer", "measurement_status_transfer"):
            if getattr(self, name) is not False:
                raise ValueError(f"{name} must remain false")
        evidence = RecurrenceEvidence(**{
            name: getattr(self, name) for name in RecurrenceEvidence.__dataclass_fields__
        })
        if self.outcome != _outcome(evidence):
            raise ValueError("outcome does not match the supplied recurrence evidence")
        if self.independent is not evidence.independent:
            raise ValueError("independent does not match the supplied ancestry evidence")
        for name in RecurrenceEvidence.__dataclass_fields__:
            object.__setattr__(self, name, getattr(evidence, name))


def _outcome(evidence: RecurrenceEvidence) -> str:
    unresolved = (
        bool(evidence.unresolved)
        or evidence.mapping_complete is None
        or evidence.replay_passed is None
        or evidence.independent is None
    )
    if unresolved:
        return "HMMM"
    elif not evidence.mapping_complete or not evidence.replay_passed:
        return "DIVERGENT"
    else:
        declared = set(evidence.declared_invariants)
        preserved = set(evidence.preserved_invariants)
        if preserved == declared:
            if evidence.equivalence_proof_id is not None:
                return "SAME_STRUCTURE"
            return "HOMOLOGOUS" if evidence.paths_distinct else "HMMM"
        elif preserved:
            return "ANALOGOUS"
        else:
            return "DIVERGENT"


def adjudicate_recurrence(evidence: RecurrenceEvidence) -> RecurrenceDecision:
    """Classify supplied evidence; a proof identifier is not proof verification."""

    return RecurrenceDecision(
        outcome=_outcome(evidence),
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
        mapping_complete=evidence.mapping_complete,
        replay_passed=evidence.replay_passed,
        ancestry_resolved=evidence.ancestry_resolved,
        unresolved=evidence.unresolved,
    )


__all__ = [
    "RECURRENCE_OUTCOMES",
    "RecurrenceEvidence",
    "RecurrenceDecision",
    "adjudicate_recurrence",
]
