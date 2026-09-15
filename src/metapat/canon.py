"""Canonical METAPAT terms, exact statements, and deterministic identity.

The importable canon and the byte identities of every canon-bearing Markdown
file are bound into one deterministic digest. The file manifest uses Git blob
identities because they are exact byte identities already carried by the
repository; the aggregate public identity remains SHA-256.
"""

# === MODULE_BUILD ===
# id: metapat_canon_core
#   module_name: metapat.canon
#   module_kind: schema
#   summary: exposes exact Meta Energy Theory root constants and a deterministic identity that includes every canon-bearing Markdown file
#   owner: The Interdependency
#   public_surface: CANON_VERSION, CANON_IDENTITY_SCHEMA_VERSION, CANON_FILE_BLOBS, root_spine, primitive_extension, definitions, canonical_canon_data, canonical_canon_manifest_data, canon_digest, canon_manifest_digest, canon_file_mismatches, assert_canon_files_match
#   internal_surface: _canonical_json_bytes
#   auth_boundary: none
#   storage_boundary: read
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
#   tests: tests.test_contracts, tests.test_envelope, tests.test_canon_integrity
#   rollout: importable_package
#   rollback: restore the prior canon epoch while preserving exact historical identities
#   requires: none
#   since: 2026-07-12
#   unresolved: formal governance process for future authorized canon rotations
# === END MODULE_BUILD ===

# === DOCS ===
# id: metapat_canon_docs
#   summary: documents METAPAT root doctrine and byte-complete canon identity
#   audience: agent, developer
#   source: AXIOMS.md, CHAPTER_ZERO.md, POSTULATES.md, THEOREMS.md, THEORIES.md, GLOSSARY.md, DOMAIN_RESTRAINT.md
#   covers: exact constants, canon file manifest, identity schema, drift detection
#   status: current
# === END DOCS ===

# === CAPABILITIES ===
# id: metapat_canon_constants
#   summary: provides exact importable constants and deterministic identity for METAPAT root doctrine
#   exposes: metapat.canon.definitions, metapat.canon.canon_digest, metapat.canon.assert_canon_files_match
#   inputs: optional repository root for file-integrity checks
#   outputs: dict, sha256 digest, mismatch map
#   boundaries: auth:none, storage:read-only, network:none, user_data:none
# === END CAPABILITIES ===

# === OWNERS ===
# id: metapat_canon_owner
#   owner: The Interdependency
#   steward: Erin Spencer
#   review_required_for: public_api, docs, canon, identity
#   escalation: hmmm
# === END OWNERS ===

# === BOUNDARIES ===
# id: metapat_canon_boundaries
#   summary: static doctrine constants plus read-only verification of canon-bearing repository files
#   auth_boundary: none
#   storage_boundary: read
#   network_boundary: none
#   user_data_boundary: none
#   admin_only: false
# === END BOUNDARIES ===

# === CONTRACTS ===
# id: metapat_root_spine_exact
#   given: canon definitions are imported
#   then: root spine contains the current five load-bearing structural lines in order
#   class: canon_contract
#
# id: metapat_time_not_registration
#   given: canon definitions are inspected
#   then: time and registration remain separate definitions
#   class: canon_contract
#
# id: metapat_canon_digest_deterministic
#   given: the same exact canon constants and file manifest are serialized repeatedly
#   then: canonical data and the sha256 digest remain byte-for-byte stable
#   class: canon_contract
#
# id: metapat_canon_identity_schema_current
#   given: the public canon identity shape is inspected
#   then: schema version 4.0.0 names the v4 field set and no earlier schema version is reused
#   class: safety
#
# id: metapat_canon_manifest_complete
#   given: the public canon file manifest is inspected
#   then: every canon-bearing Markdown file is named exactly once with an exact Git blob identity
#   class: evidence
#
# id: metapat_canon_files_match_repository
#   given: the repository canon files are read without modification
#   then: every observed byte identity matches the committed manifest
#   class: evidence
#
# id: metapat_canon_file_drift_visible
#   given: one canon-bearing file changes by one or more bytes
#   then: the mismatch is reported and strict verification fails closed
#   class: safety
# === END CONTRACTS ===

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Mapping

CANON_VERSION = "metapat-canon-v4"
CANON_IDENTITY_SCHEMA_VERSION = "4.0.0"

ROOT_SPINE: tuple[str, ...] = (
    "Thing is that which is.",
    "Boundary is the thing between things.",
    "State is a metricable property of a thing.",
    "A simplex is a thing with boundary and state.",
    "A tensor is structure produced when simplexes relate.",
)

PRIMITIVE_EXTENSION: tuple[str, ...] = (
    "Relate is this to that.",
    "Tensors emerge from simplexes.",
    "Vector alters state.",
    "Vector is inferred by scalar measurement.",
    "Scalar is a state metric.",
    "Transformation is resulting state change.",
    "Time is sequential transformation.",
    "Structural recurrence does not transfer a domain term.",
)

TIME_DEFINITION = "Time is sequential transformation."
DOMAIN_QUALIFICATION_DEFINITION = "Structural recurrence does not transfer a domain term."
ENERGY_THEORY_QUESTION = "What questions do I ask?"

# Exact Git blob SHA-1 identities of the canon-bearing Markdown files on the
# canon-v4 source epoch. Git blob identities bind file bytes including length.
CANON_FILE_BLOBS: Mapping[str, str] = {
    "AXIOMS.md": "90b7fea71369f08bee09d4fa100491a66e0c498e",
    "CHAPTER_ZERO.md": "d820a5855867569e97f46bdd15bbd9ff3a67706c",
    "DOMAIN_RESTRAINT.md": "8d3626384c55350832767ba6f4fa913f48a5afd0",
    "GLOSSARY.md": "4976050700ccf538400f02d78e4cdf9082331a58",
    "POSTULATES.md": "e6003140a569e26fbe22ac63f34c0525b27cab48",
    "THEOREMS.md": "1cc788af8549ec6e84391ad1a6a8fe53a26610cb",
    "THEORIES.md": "9b351be6273872c6243898ae3aa6c38bcbef301b",
}


class CanonIntegrityError(ValueError):
    """Raised when repository canon bytes differ from the declared manifest."""


def _canonical_json_bytes(data: Mapping[str, Any]) -> bytes:
    return json.dumps(data, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def git_blob_sha1(data: bytes) -> str:
    """Return the exact Git blob identity for ``data``."""

    header = f"blob {len(data)}\0".encode("ascii")
    return hashlib.sha1(header + data).hexdigest()  # noqa: S324 - Git identity compatibility


def root_spine() -> tuple[str, ...]:
    """Return the exact current structural root spine."""

    return tuple(ROOT_SPINE)


def primitive_extension() -> tuple[str, ...]:
    """Return the exact current action, measurement, result, and qualification extension."""

    return tuple(PRIMITIVE_EXTENSION)


def definitions() -> dict[str, str]:
    """Return compact canonical definitions for contract checks and consumers."""

    return {
        "METAPAT": "Meta Energy Theory — Axioms, Postulates, Theorems, and Theories.",
        "thing": "That which is.",
        "boundary": "The thing between things.",
        "state": "A metricable property of a thing.",
        "simplex": "A thing with boundary and state.",
        "tensor": "Structure produced when simplexes relate.",
        "relate": "This to that.",
        "emerge": "Tensors emerge from simplexes.",
        "scalar": "A state metric.",
        "vector": "Alters state; inferred by scalar measurement.",
        "transformation": "Resulting state change.",
        "time": TIME_DEFINITION,
        "domain_qualification": DOMAIN_QUALIFICATION_DEFINITION,
        "energy": "A domain-qualified term; METAPAT does not call every state transformation energy.",
        "registration": "Capacity of a simplex to preserve, express, or transmit transformation.",
        "observer": "A simplex performing registration; observer does not necessarily mean mind.",
        "question": "A bounded unresolved state or relation available to transformation.",
    }


def canonical_canon_manifest_data() -> dict[str, Any]:
    """Return the deterministic byte-complete canon file manifest."""

    return {
        "identity_schema_version": CANON_IDENTITY_SCHEMA_VERSION,
        "canon_version": CANON_VERSION,
        "git_blob_algorithm": "sha1",
        "files": dict(sorted(CANON_FILE_BLOBS.items())),
    }


def canon_manifest_digest() -> str:
    """Return a SHA-256 digest of the canonical file manifest."""

    return hashlib.sha256(_canonical_json_bytes(canonical_canon_manifest_data())).hexdigest()


def canonical_canon_data() -> dict[str, Any]:
    """Return the deterministic public canon surface used for identity binding."""

    return {
        "identity_schema_version": CANON_IDENTITY_SCHEMA_VERSION,
        "canon_version": CANON_VERSION,
        "root_spine": list(ROOT_SPINE),
        "primitive_extension": list(PRIMITIVE_EXTENSION),
        "time_definition": TIME_DEFINITION,
        "domain_qualification_definition": DOMAIN_QUALIFICATION_DEFINITION,
        "energy_theory_question": ENERGY_THEORY_QUESTION,
        "definitions": definitions(),
        "canon_manifest_digest": canon_manifest_digest(),
        "canon_file_blobs": dict(sorted(CANON_FILE_BLOBS.items())),
    }


def canon_digest() -> str:
    """Return a stable SHA-256 digest for :func:`canonical_canon_data`."""

    return hashlib.sha256(_canonical_json_bytes(canonical_canon_data())).hexdigest()


def observed_canon_file_blobs(root: Path) -> dict[str, str | None]:
    observed: dict[str, str | None] = {}
    for name in sorted(CANON_FILE_BLOBS):
        path = root / name
        try:
            observed[name] = git_blob_sha1(path.read_bytes())
        except OSError:
            observed[name] = None
    return observed


def canon_file_mismatches(root: Path) -> dict[str, dict[str, str | None]]:
    observed = observed_canon_file_blobs(root)
    return {
        name: {"expected": expected, "observed": observed[name]}
        for name, expected in sorted(CANON_FILE_BLOBS.items())
        if observed[name] != expected
    }


def assert_canon_files_match(root: Path) -> None:
    mismatches = canon_file_mismatches(root)
    if mismatches:
        detail = "; ".join(
            f"{name}: expected {values['expected']}, observed {values['observed'] or 'MISSING'}"
            for name, values in mismatches.items()
        )
        raise CanonIntegrityError(f"canon file integrity mismatch: {detail}")


__all__ = [
    "CANON_FILE_BLOBS",
    "CANON_IDENTITY_SCHEMA_VERSION",
    "CANON_VERSION",
    "CanonIntegrityError",
    "DOMAIN_QUALIFICATION_DEFINITION",
    "ENERGY_THEORY_QUESTION",
    "PRIMITIVE_EXTENSION",
    "ROOT_SPINE",
    "TIME_DEFINITION",
    "assert_canon_files_match",
    "canon_digest",
    "canon_file_mismatches",
    "canon_manifest_digest",
    "canonical_canon_data",
    "canonical_canon_manifest_data",
    "definitions",
    "git_blob_sha1",
    "observed_canon_file_blobs",
    "primitive_extension",
    "root_spine",
]
